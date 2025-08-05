# Simulation_of_mass_balance_behavior_in_a

**Fonte**: Simulation_of_mass_balance_behavior_in_a.pdf  
**Data de conversão**: 2025-07-30 15:09:25  
**Origem**: base_relevantes

---

Particuology 25 (2016) 51–58
Contents lists available at ScienceDirect
Particuology
j our na l ho me page: www.elsevier.com/locate/partic
Simulation of mass balance behavior in a large-scale circulating
fluidized bed reactor
Artur Blaszczuka,∗, Anna Zylkaa, Jacek Leszczynskib
aCzestochowa University of Technology, Institute of Advanced Energy Technologies, Dabrowskiego 73, 42-200 Czestochowa, Poland
bAGH University Science and Technology, Faculty of Energy and Fuels, Department of Hydrogen Energy, Mickiewicza 30, 30-059 Cracow, Poland
a r t i c l e i n f o
Article history:
Received 3 November 2014
Received in revised form 10 March 2015
Accepted 9 April 2015
Available online 20 July 2015
Keywords:
Bed inventory mass
Mass flow of solids
Circulating fluidized bed
Population mass balance model
Sensitivity
a
analysis
b s t r a c t
We determine using a compound model the influence of the mass of granular matter on the behavior
of a supercritical circulating fluidized bed (CFB) reactor. Population balance enables a stationary-regime
modeling of the mass flow of granular matter inside a CFB unit in a large-scale. The simulation includes
some important dynamic processes of gas-particle flows in fluidized bed such as attrition, fragmenta-
tion, elutriation, and fuel combustion. Numerical calculations with full boiler loading were performed
of operational parameters such as furnace temperature, furnace pressure, feeding materials mass flows,
and excess air ratio. Furthermore, three bed inventory masses were adopted as experimental variables in
the simulation model of mass balance. This approach enables a sensitivity study of mass flows of granular
matter inside a CFB facility. Some computational results from this population balance model obtained for
a supercritical CFB reactor are presented that show consistency with the operational data for large-scale
CFB units.
© 2015 Chinese Society of Particuology and Institute of Process Engineering, Chinese Academy of
Sciences. Published by Elsevier B.V. All rights reserved.
Introduction
Bed inventory mass is a very important parameter in regard
to successfully operating a circulating fluidized bed (CFB) reactor.
This operational parameter influences the heat transfer (Blaszczuk
& Nowak, 2014; Blaszczuk, Nowak, & Jagodzik, 2014; Lakatos,
Süle, & Mihálykó, 2008), the combustion process (Basu, 2006;
Myöhanen & Hyppänen, 2011; Saastamoinen & Tourunen, 2012;
Scala & Chirone, 2010), and hydrodynamics (Chalermsinsuwan,
Boonprasop, Nimmanterdwong, & Piumsomboon, 2014; Qi, Zhu,
& Huang, 2008) in CFB reactors. The complex hydrodynamics and
combustion processes occurring inside a CFB boiler are very dif-
ficult to model and obtain accurate numerical predictions. A few
numerical (Adamczyk et al., 2014; Nikku, Myöhanen, Ritvanen,
& Hyppänen, 2014; Redemann, Hartge, & Werther, 2009; Wang,
Luo, Ni, & Cen, 2003; Yang & Gou, 2006) and experimental data
(Błaszczuk, Komorowski, & Nowak, 2012) from large-scale CFB
reactors are available in the literature. According to these authors,
the bed inventory mass is one of the main parameters having an
influence on the solids concentration profile along the height of
∗ Corresponding author. Tel.: +48 34 32 50 933; fax: +48 34 32 50933.
E-mail address: ablaszczuk@is.pcz.czest.pl (A.
the
Blaszczuk).
furnace chamber and heat transfer behavior inside the fur-
nace chamber. In this instance, the authors proposed using the
population balance to model the behavior in large-scale CFB reac-
tors. Based on the simulation model, it is possible to control bed
hydrodynamics and monitor large-scale CFB boilers. Nevertheless,
previous simulations of mass balance still have some limitations
when describing the particle properties and physical/chemical pro-
cesses in CFB boilers (Yang, Yue, Xiao, Lu, & Liu, 2005). A 1D model
of a CFB boiler, which is widely used in the literature, emphasizes
some important factors that influence the ash balance in CFB boil-
ers such as ash formation, attrition and size reduction, residence
time, and segregation in a dense bed. The model predicts only the
mass balance at different operating loads in the same boiler (Yang
et al., 2005) but does not take into account combustion processes.
The dynamic simulation model of the particle population in a CFB
combustor with an external heat exchanger is widely known. The
model enables the mass flows of solids to be calculated as well as the
corresponding particle-size distributions (PSDs) at any point inside
the combustion system (Grosschmidt, Habisreuther, & Bockhorn,
2007). In another study by Klett, Hartge, and Werther (2005), the
particle population balance for a CFB combustor was analyzed. The
population balance of particles enables the behavior of individual
particles to be taken into account during attrition and transport.
Apart from particle operation conditions and the size distribution
of particles, the residence time of particles in the CFB reactor is also
http://dx.doi.org/10.1016/j.partic.2015.04.003
1674-2001/© 2015 Chinese Society of Particuology and Institute of Process Engineering, Chinese Academy of Sciences. Published by Elsevier B.V. All rights reserved.

52 A. Blaszczuk et al. / Particuology 25 (2016) 51–58
Nomenclature
A ash content in Eqs. (2) and (3)
A cross-sectional
bed
area of the bed inventory (m2)
C parameter in Eq. (5)
d equivalent
k
diameter of the k-th particle class (m)
f probability density function (m−1)
fˆ modified probability density function (m−1)
fl (d )
bed k
an unknown particle distribution of the l-th granular
material (m−1)
g acceleration due to gravity (m/s2)
H height of furnace (m)
Hsep separator height (m)
h geometric coefficient for the cross-section of solids
separator
Kl (d )
attr k
attrition rate constant of granular materials (s−1)
Kl (d )
bott k
discharge constant (s−1)
Kl (d )
com k
combustion-rate constant of the k-th particle class
(s−1)
Kl (d )
elut k
elutriation constant (s−1)
Kl(d )
j k
a characteristic function of some internal processes
KR solid recirculation rate
M moisture content in Eq. (3)
m total mass of mixture of granular materials (kg)
m ,
1
m ;
2
n ,
1
n ;
2
s ,
1
s characteristic
2
constants in
Rosin–Rammler function
m˙ l(d )
k
mass flow rate for the k-th particle class (kg/s)
m total
bed
fluidized bed inventory mass (kg)
m˙ lf (d )
k
mass flow function of feeding process (kg/s)
m˙ il(d )
j k
mass flow function of internal process (kg/s)
m˙ el(d )
j k
mass flow function of external process (kg/s)
p mass fraction of the l-th granular material
RR(d ) k Rosin–Rammler function
Rrur a vortex diameter (m)
sac coefficient for accumulation function (m−1)
U minimum mf fluidization velocity (m/s)
U superficial 0 gas velocity (m/s)
Ut terminal velocity (m/s)
SA/PA secondary air to primary air ratio
T furnace
bed
temperature (K)
Q thermal
b
power (kW)
Wc lower
d
heating value (LHV) (kJ/kg)
V volume (m3)
V˙ g gas stream volumetric flow rate through compact
separator (m3/h)
X CFB b reactor’s load
X mass l fraction of the l-th granular material in total
mass in the CFB system
x ratio
Z height above the air distributor (m)
Greek symbols
ˇ a drag function described by Bis (2010)
(cid:2)d length
k
of the k-th particle class (m)
 CFB b reactor efficiency
(cid:2)p pressure drop (kPa)
 density (kg/m3)
Superscripts
ac accumulation
ad air dried
ar
basis
as received
l a kind of granular material (i.e., coal, ash or lime-
stone)
Subscripts
attr attrition of solids
bed bed
bott discharge of bottom ash
com fuel combustion
down recirculation of bed inventory between CFB furnace
and return system
elut elutriation of bed inventory
feed feeding
frag fragmentation of granular materials
g gas
k particle class indicator
max maximum
min minimum
N class number
p particle
rebod recirculation of bottom ash
refl recirculation of fly ash
s suspension
taken into account in modeling the abrasion and shrinkage of par-
ticles. The impact of these operational parameters was described
in detail in Klett et al. (2005) and will not be presented here.
In this work, numerical calculations for full boiler loadings were
performed for four basic operational parameters: furnace tempera-
ture, furnace pressure, mass flow rate of the feeding materials, and
excess air ratio. Moreover, the physical (i.e., attrition, fragmenta-
tion, and elutriation) and chemical (i.e., fuel combustion) processes
that mainly occur in CFB reactors were taken into account. The key
objective of this work was to use three different levels of bed inven-
tory masses, which were considered as experimental parameters
in the simulation model of mass balance. This approach enables a
sensitivity study to be performed of mass flows of solids inside a
large-scale CFB facility.
Description of population balance model
The approach taken in modeling a supercritical CFB reactor
assumes the transport of granular matter between the combus-
tion chamber and the return leg. The population balance takes into
account the dynamics of gas-particle flows (e.g., attrition, fragmen-
tation, and elutriation) and combustion processes. The quantities
occurring in the bed inventory are a result of the mass flows of the
feeding materials (i.e., fuel, sorbent, and ash obtained from burned
fuel) and of the two solids exiting the CFB facility (specifically, bot-
tom ash and the fly ash). In our study, the simulation assumes the
particles are spherical and classifies all particles in terms of their
mean size (Blaszczuk, Leszczynski, & Nowak, 2013). This partition-
ing is necessary to obtain balance formulae for a given particle class.
In the current approach, the balance equations take into account the
external and internal processes occurring in the CFB reactor. These
two groups of processes depend on the unknown distribution of
particles which depends on the mutual coupling between feed-
ing, and the external and internal processes. An internal process
is a process involving transitions between classes of particles; see
Leszczynski (2013) for details. External processes are responsible
for changes in the quantitative features of the particle distribution.
For each distinct particle class of solids considered (i.e., fuel, sor-
bent, ash from burnt out fuel) balancing equations are established

A. Blaszczuk et al. / Particuology 25 (2016) 51–58 53
for the external processes using mathematical difference equations
(Lakshmikantham & Trigiante, 2002):
m˙ el(d )
j k
=m˙ l (d )
feed k
−m˙ l (d )
elut k
+m˙ l (d )
down k
−m˙ l (d )
bott k
−m˙ l (d )
com k
+m˙ l (d )
refl k
+ ml (d )
rebod k
+ m˙ l frag (d k+1 ) −m˙ l (d ) frag k (cid:2)d
(cid:2)d k
k
+ m˙ l attr (d k+1 ) −m˙ l (d ) attr k (cid:2)d =
(cid:2)d k
k
0 (1)
In this balance equation, subscripts feed, elut, down, bott, com,
refl, rebod, frag, and attr signify feeding, elutriation of the bed
inventory, circulation of the bed inventory between the CFB furnace
and the return system, discharge of bottom ash, fuel combustion,
recirculation of fly ash, recirculation of bottom ash, fragmenta-
tion of granular materials, and attrition of solids, respectively.
Superscript l index indicates the three granular materials, namely,
bituminous coal as a main fuel, ash obtained from burned coal, and
limestone as sorbent. Subscript k enumerates the particle classes
and subscript j denotes the number for both external and internal
processes. Moreover, the parameter (cid:2)d denotes
k
the length of the
k-th particle class.
The balancing equations take into account the characteristics of
the CFB facility. A sketch of a supercritical CFB reactor with a capac-
ity of 966 MW is
th
shown in Fig. 1; a precise description is given
(Błaszczuk et al., 2012; Blaszczuk et al., 2013; Błaszczuk, Nowak, &
Jagodzik, 2013).
Some fundamental equations, Eqs. (2)–(9), for the external pro-
cesses used in the population balance are given in Table 1. However,
formulae needed for estimating several factors (i.e., elutriation con-
stant, discharge constant, combustion constant, and attrition rate)
and also the thermal properties of typical flue gas of a coal-fired flu-
idized bed can be found in (Basu, 2006; Bis, 1991; Blaszczuk et al.,
2013; Ghadiri & Zhang, 2002; Leszczynski, 2013; Tomeczek, 1992;
Wirth, 1991; Zhang & Ghadiri, 2002) and will not be given here.
The CFB reactor was operated under stationary conditions with-
out recirculation of the bottom ash and fly ash into the furnace
chamber. Therefore, the following components of the balancing
Eq. (1),m˙ l (d )
refl k
andm˙ l (d ),
rebod k
are not taken into account in the
simulation mass balance model. In Eqs. (6)–(9), the total fluidized
bed mass m is
bed
estimated from the pressure data (i.e., pres-
sure drop (cid:2)p )
bed
inside the furnace chamber of the CFB reactor
which were established during performance tests of the
Fig.
966-MW
th
1. Sketch of the 966-MWthsupercritical CFB reactor indicating certain basic
processes.
supercritical CFB reactor. In our work, m is
bed
calculated using the
semi-empirical formula (Howard, 1989):
(cid:2)p =
m
bed
(p −
bed
g)g
(10)
pA
bed
where (cid:2)p is
bed
the pressure drop inside the furnace chamber, m
bed
the mass of the bed inventory, pthe bed particle density, gthe
fluidizing gas density, A the
bed
cross-sectional area of the bed inven-
tory, and g the gravitational acceleration.
Table 1
Formulation of balance equations for external processes.
External processes Formula
Feeding process m˙f1(dk) =

X
b
b
W
Qb
d c
Afˆ
1
f(dk)(cid:2)dk for ash (2)
m˙f2(dk) = XbQb(1
bW
d
c
− A − M)Afˆ
2
f(dk)(cid:2)dk for coal (3)
m˙f3(dk) =m˙sfˆ
3
f(dk)(cid:2)dk for sorbent (4)
Recirculation of bed inventory m˙l down (dk) =m˙l elut (dk)(cid:2)1 − exp(cid:3) −h(cid:4) ˇ 2 d  ra C gR 2 n 2 H u s r e V p ˙ g (cid:5)(cid:6)(cid:7) (5)
Elutriation m˙l
elut
(dk) = XlmbedK
e
l
lut
(dk)f
b
l
ed
(dk)(cid:2)dk (6)
Discharge m˙l
bott
(dk) = XlmbedK
b
l
ott
(dk)f
b
l
ed
(dk)(cid:2)dk (7)
Combustion m˙l
com
(dk) = XlmbedK
c
l
om
(dk)f
b
l
ed
(dk)(cid:2)dk (8)
Attrition m˙l
attr
(dk) = XlmbedK
a
l
ttr
(dk)f
b
l
ed
(dk)(cid:2)dk (9)

54 A. Blaszczuk et al. / Particuology 25 (2016) 51–58
The unknown PSD of the l-th granular material is a non-linear
function calculated using the following expression:
f
b
l
ed
(dk) =
m˙fj(dk) +m˙l
attr
(dk+1) + (cid:2)m˙l
attr
(dk)
Xlmbed(cid:2)dk((1 − s)K
e
l
lut
(dk) + K
b
l
ott
(dk) + K
c
l
om
(dk) +
(11)
K
a
l
ttr
(dk))
Here, (cid:2)m˙ l (d )
attr k
denotes the mass flow for the accumulation pro-
cess and is calculated using the following formulae:
(cid:2)m˙ l (d )
attr k
= 0 for k > h (12)
j
(cid:2)m˙ l (d )
attr k
exp
−s
j
acdk hj+1
= m˙ l (d )(1
(cid:8) h k= j 1 exp −s j acdk (cid:9) N−1 attr k
− xac)
j
for k ≤ h
j
(13)
where sac is
j
the coefficient for the accumulation function
introduced by Leszczynski (2013).
For the dense region in a CFB furnace, the total mass of particu-
late solids within the bed (i.e., fuel, ash, and sorbent) is the sum of
three components:
m = m =
bed (cid:9) l
l=c,a,s
mc + ma + ms (14)
where mc denotes the mass of fossil fuel within the bed, ma the
mass of ash in the bed inventory, and msthe mass of limestone in
the bed. The mass fraction of the l-th granular material within the
bed is calculated using:
V
X = l (15) l V
bed
where V denotes l the l-th solid volume in the bed and V the bed bed
volume estimated based on the bed height in the dense region of
the furnace chamber and the cross-sectional area of the bed inven-
tory. In this study, the bed height for the dense region inside the
furnace chamber H = bed 0.47 m and the cross-sectional area of the
bed inventory A equals bed 292.5 m2.
Performance test on supercritical CFB reactor
A performance test was necessary to validate the impact of the
mass of the granular matter in simulations modeling the behavior of
a large-scale supercritical CFB facility. The study was performed for
a supercritical CFB reactor with a capacity of 966 MW ,
th
located at
the Tauron Generation S.A. Lagisza Power Plant, Poland. This reactor
has a height of 48.0 m and a cross-sectional area has 27.6 m × 10.6 m
in the transport zone, where the heat transfer surfaces in form of
the membrane water-walls are located. The fluidization grid with
nozzles for primary air is on the bottom of the combustion cham-
ber, whereas secondary air nozzles are located at three levels above
the grid in the two sidewalls. The CFB reactor design incorporates
altogether eight INTREXTMheat exchangers, one for each solids sep-
arator. Furthermore, the CFB steam generator contains a furnace
and a low-temperature flue-gas heat recovery system. The solids
separators are arranged in parallel, four separators on two opposite
walls of the furnace. The separators are formed of membrane walls
which are covered with a thin refractory lining of high heat con-
ductivity and are resistant to erosion. The INTREXTMintegrated heat
exchanger is located in the furnace and serves to extract heat from
the hot circulating material that is returned from the separator, or
solids taken directly from the lower part of the furnace.
The performance test was carried out with a maximum-
continuous-rating (MCR) load of 100% to investigate the effect of
bed inventory mass in simulations of population balance. Four mea-
surement series under stable operation conditions lasting 8 h were
conducted. In this work, as confidential commercial information
Fig.
is
2. Temperature distribution inside the furnace chamber of a supercritical CFB
reactor.
included, some process data used in testing are given in dimen-
sionless scale and normalized by the maximum value of furnace
data. The furnace data such as temperature and pressure were
recorded by an ADAM-6000 data acquisition system (Advantech
Equipment Corporation, Taiwan, China) located between 0.2 and
42.2 m above the primary air distributor level. All measurement
ports were 25 mm in diameter and were purged regularly with
compressed air. To measure the bed temperature, nine probes with
K-type thermocouples (type 206, Czaki Thermoproduct, Poland)
were installed on the front wall of the CFB reactor. Probes were
placed along the vertical direction in the furnace chamber at non-
dimensional spacings Z/H of 0.005, 0.02, 0.04, 0.10, 0.16, 0.50,
0.64, 0.87, and 1.00, respectively. Fig. 2 gives the vertical profile
of the temperature in the furnace chamber at 100% MCR unit load.
The highest bed temperature was recorded at Z/H = 0.64. This was
because the zero pressure area within the CFB furnace and gas-solid
flow structure is localized, as is the active heat transfer surfaces
(superheaters) in this region of the combustion chamber.
In the bottom region of the combustion chamber, the high bed
temperature results from the effect of secondary air on the fuel
combustion process. The combustion reaction in the bottom region,
where the oxidant concentration is high, is much stronger than near
the exit region of furnace chamber. The O concentration
2
changes
rapidly near the secondary air inlet (i.e., the region between 2 m
and 6 m above the level of the air distributor). During performance
testing, the furnace temperature difference (cid:2)T is 24 K. The regis-
tered furnace temperature was in the range typical for CFB boilers
(Sekret, 2011).
Pressure taps were provided at 0.25, 0.4, 0.6, 1.0, 2.0, 2.5, 5.0,
8.3, 24.0, 31.0, and 42.4 m above the air-distributor level and were
connected to the transducers by a shielded cable of 6.3-mm diame-
ter. The variation of pressure with height in the furnace chamber is
shown in Fig. 3, decreasing exponentially, with a dense phase at the
bottom and a dilute phase in the upper region of the CFB furnace.
This trend is consistent with the results obtained for large-scale CFB
facilities (Basu, 2006). Fig. 3 also indicates that in the furnace cham-
ber, the pressure drop equals 6.62 kPa. Moreover, a high pressure
gradient was observed in the bottom region. This situation arises
because of the highly turbulent flow and high circulation flux of
solids in this region of the furnace chamber.
In Table 2, the mass fractions of solids are given for the super-
critical CFB reactor. These parameters were determined based on
the mass flows of feed materials (coal and limestone) and mate-
rials led out of the furnace chamber (fly ash and bottom ash).
Bottom ash and fly ash collected in the storage silos were used to

A. Blaszczuk et al. / Particuology 25 (2016) 51–58 55
Fig. 3. Pressure profile versus relative furnace height in a supercritical CFB reactor.
Table 2
Solids mass fraction (wt%) at the 966-MWthsupercritical CFB reactor.
Solids Value
Bituminous coala 90.0
Limestonea 10.0
Circulating materialb 99.86
Fly ashb 0.13
Bottom ashb 0.01
a Feeding materials.
b Materials led out of furnace chamber.
determine these flows. By closing the damper, which is installed
under each silo, the increase in mass inside the silo can be mea-
sured. Mass flows of solids of feeding materials (i.e., coal and
limestone) were determined based on 5-min-interval changes in
weight contained in each silo. In contrast, the mass flow of the
circulating material was calculated from the recirculation rate of
solids and the compact separator efficiency from the performance
test.
During the performance test, fossil fuel from the Ziemowit coal
mine in Poland was used. The ultimate and proximate analysis data
are given in Table 3. Determination of proximate parameters of the
bituminous coal was made in accordance with normalized stan-
dards for fossil fuel in Poland, whereas the ultimate analysis data
were obtained by means of the LECO TrueSpecTM analyzer (LECO
Corporation, St. Joesph, MI, USA). All analytical data for fossil fuel
are averages from four repetitions for each fuel component giv-
ing an accuracy of 0.01 wt%, the exception being the caloric value
parameter. For a lower heating value, this parameter was measured
with an accuracy of ±0.20 MJ/kg.
Limestone as sorbent was used in the performance test for
in situ sulfur capture in the supercritical CFB reactor. The collected
limestone samples were subjected to an XRF analysis performed
using an X-ray fluorescence spectrometer (PW 4025/00 MiniPal,
Philips, Netherlands) with a semiconductor detector at ambient
pressure in the presence of an inert gas (helium). Table 4 gives the
Table 3
Ultimate and proximate analysis of the tested Polish coal (Ziemowit coal mine).
Ultimate analysis (air dried basis) Proximate analysis (as-received)
Carbon, Cad(wt%) 57.33 Caloric value, Qar(MJ/kg) 22.28
Hydrogen, Had(wt%) 4.62 Volatile matter, Var(wt%) 26.07
Oxygen, Oad(wt%) 5.70 Ash, Aar(wt%) 8.09
Nitrogen, Nad(wt%) 0.97 Total moisture, Mar(wt%) 18.47
Sulfur, Sad(wt%)
Table
1.31
4
Analysis data of Polish limestone (wt%) on performance test (Czatkowice limestone
mine).
Component Value
Ca 38.07
CaO 53.30
Mg 0.49
MgO 0.82
Table 5
Model input data.
Parameter Value
Capacity (MWth) 966
CFB reactor efficiency (%) 94.21
Bed temperature (K) 1139
Excess air ratio 1.21
Bed pressure (kPa) 6.16
Pressure drop (kPa) 6.62
Superficial gas velocity (m/s) 5.21
Fuel density (kg/m3) 1300
Sorbent density (kg/m3) 2530
Ash density (kg/m3) 2690
characteristics of Czatkowice limestone from Poland, in which CaO
is the main component; both Mg and MgO content were substan-
tially lower (<1.0%). The XRF analysis of a limestone sample was
performed to an accuracy of 0.02%.
Results and discussion
Our mass balance model along with the performance test results
was used in the simulations of the 966-MW CFB
th
reactor. To per-
form the sensitivity study, some geometrical construction data and
process data of the coal-fired CFB reactor were used. The model
input data listed in Table 5 were obtained from the performance
test of this CFB reactor.
Fig. 4 shows the PSD of the test granular materials, which were
obtained from the performance test and sieve analysis. Details
about the procedure and device applied to the sieve analysis were
presented by Blaszczuk and Nowak (2014) and will not be described
here. Nonetheless, the PSD of ash was obtained from 2-kg fuel sam-
ple, which was incinerated in a muffle furnace at 850◦C. In Fig. 4, the
corresponding PSDs of three solids samples are presented. These
experimental data were used as an indispensable starting point to
estimate the steady-state size distribution of the bed inventory and
Fig. 4. Measured PSDs in the combustion chamber of a 966-MWthsupercritical CFB
reactor.

56 A. Blaszczuk et al. / Particuology 25 (2016) 51–58
Table 6
Rosin–Rammler parameters for the three granular materials.
Parameter Solids samples
Coal Ash Limestone
p 0.47523 0.76781 0.81273
m1 0 0 0
n1 1.77746 1.9123 2.50604
s1 0.00277 2.66237 × 10−4 2.49457 × 10−4
m2 0.00488 2.7315212 × 10−4 3.00905 × 10−4
n2 2.40659 0.8254 5.04351
s2 0.00395 0.00221 1.12489 × 10−4
the simulation of population balance for the commercial supercrit-
ical CFB reactor. The PSDs of coal, ash, and limestone are marked
by different symbols for each granular material and were approxi-
mated by the Rosin–Rammler function,
RR(d ) k = (1 −
⎛
p) 1
⎝
− exp
−(cid:4) dk− s1 m1 (cid:5)
n1
⎞
⎠
+
⎛
p 1
⎝
− exp
−(cid:4) dk− s2 m2 (cid:5)
n2
⎞
(16)
⎠
where m ,
1
m ;
2
n ,
1
n ;
2
and s ,
1
s are
2
the characteristic constants for
the solids and p represents the mass fraction of the l-th granular
material.
The individual parameters of Rosin–Rammler function were
estimated using a least-squares technique. The obtained param-
eters for the RR functions are given in Table 6. The slope of the
PSD function for coarse particles (i.e., above the 0.5 oversize) is
unique to each granular material. However, the RR functions have
a similar shape for fine particles below the 0.2 oversize for all gran-
ular materials. The cumulative oversize curve of the RR function for
limestone indicates that the sorbent has more coarse particles with
hard structure than coal and ash.
Fig. 5 shows a comparison between the mean PSDs predicted by
the mass-balance model and the sieve analysis data. The computer
results from population mass balance model for fly ash were in
good agreement with the experimental data obtained based on the
sieve analysis. However, there are deviations between modeled and
measured PSDs for bottom ash.
From Fig. 5, attrition has an essential influence on the PSD of
bottom ash. For mean particle size of bottom ash covered in a
range of d –d ,
60 80
simulation results exhibit good agreement with
the sieve analysis data. For fine and coarse particles, the calculated
Fig. 5. Measured and modeled PSDs for fly ash and bottom
Fig.
ash.
6. Distributions of feeding material mass flow rate for the 966-MWthsupercrit-
ical CFB reactor.
errors between the computed values for cumulative oversize and
the experimental data for bottom ash do not exceed 20%. The main
reason for this is the occurrence of particles with soft structure.
Moreover, this indicates that the proposed mass-balance model is
a useful tool to assess and monitor the PSDs during operations of
large-scale CFB reactors.
Fig. 6 depicts the distribution of feeding material mass flow at
the 966-MW supercritical
th
CFB reactor. Changes in granular mat-
ter mass have no impact on feeding material mass flow in the CFB
reactor. Simulations were performed to establish process condi-
tions that prevail in the combustion chamber at full unit load. To
stabilize operations within the CFB reactor, feeding material mass
flow should be almost at the same level. Reducing the height of the
bed inventory is equivalent to decreasing the CFB-reactor load and
also dropping the pressure within the combustion chamber.
Fig. 7 shows the mass flow rate of bed inventory trans-
ported by elutriation from the region of dense fluidized bed to
the region of a dilute phase in the upper part of the CFB com-
bustion chamber. Clearly, the optimum particle size of the bed
inventory, which is elutriated to the region with low suspension
density (s< 4 kg/m3) in the furnace chamber, is in the range from
5.0 × 10−5to 2.05 × 10−4m.
The amount of bed inventory elutriated from the bottom to the
top of the combustion chamber is directly related to the mass of
the bed inventory located in the confines of the furnace chamber.
Increases in the bed inventory mass proportionately increases the
mass flow rate of particles elutriated. Within the range of changes in
bed inventory mass analyzed, the maximum particle size elutriated
Fig. 7. Elutriated bed inventory mass flow rate for a large-scale CFB facility at dif-
ferent bed inventory masses.

A. Blaszczuk et al. / Particuology 25 (2016) 51–58 57
Fig. 8. Attrited bed inventory mass flow rate for a large-scale CFB reactor at different
bed inventory masses.
under CFB conditions ranged from 1.23 × 10−4to 1.5 × 10−4m. For
each analyzed bed inventory mass, there is a recognizable char-
acteristic peak, which corresponds to maximal flow rate of that
particle size. Mass flow rate distributions of bed inventory elutri-
ated to the dilute phase in the combustion chamber impacts particle
attrition, especially in the dense phase of solids at the bottom of the
reactor. Fig. 8 presents the mass flow rate of bed inventory attrition.
Over the range of particle sizes, there are four characteristic peaks.
Each peak corresponds to a particle size that is dominant during
attrition. The characteristic peaks in the PSD for the bed inventory
are a result of the structure of particles among the feeding granular
materials. The higher mass flow rates during the attrition process
arise because of the soft structure of fine particles. The coarse par-
ticles characterized by a hard surface structure have almost zero
mass flow rates, particularly those in one of two particle-size ranges
5 × 10−4–5 × 10−3m. The presence of these characteristic peaks is a
consequence of the variation in internal circulation of bed inventory
between the combustion chamber and the return leg system.
The results of the numerical calculations were generated for
the solid recirculation-rate range of KR = 63–68 and separation
efficiency of solid phase of 99.68–99.84%. The operating parame-
ters of the return-leg system also have a significant influence on
particle distributions within the circulating material between the
combustion chamber and return-leg system. Fig. 9 presents the dis-
Fig. 9. Distributions of circulating material mass flow rate in a supercritical CFB
reactor at different bed inventory
Fig.
masses.
10. Distributions of fly-ash mass flow rate in a supercritical CFB reactor at
different bed inventory masses.
tributions of circulating material mass flow rate as a function of
particle size of the solid phase. For each bed inventory mass, char-
acteristic peaks appear that corresponded to a size of particle which
is recirculated in the combustion chamber by means of the return-
leg system. The results generated by the population balance model
confirm a certain regularity, i.e., an increase in bed inventory mass
is accompanied by a slight decrease in particle size, which can be
observed at maximum mass flow rate. With a fivefold increase in
bed inventory mass in the combustion chamber, a decrease can
be observed in the dominant particle size in the circulating mate-
rial mass flow rate from d =
min
1.23 × 10−4m to dmax= 1.5 × 10−4m.
Furthermore, the mass flow rate for particles in the range of bed
inventory mass analyzed increased nearly four times, and these
large changes arise from the attrition process. The greater the bed
inventory mass, the more importance the attrition process has on
mass flow rate during solids separation in the compact separator.
There is a qualitative similarity of the mass flow rate distribu-
tion for fly ash to the distribution of circulating material mass flow
rate (Fig. 10). This result from the fact that for both granular mate-
rials, the distribution of mass flow affects the same parameters of
the return-leg system, i.e., the effectiveness of the compact sepa-
rator and the circulation rate of the bed inventory. Nevertheless, it
is worth noting that for the fly-ash mass flow rate, there is only
one dominant particle size in all cases of bed inventory masses
analyzed. For each bed inventory mass, a characteristic peak in
the particle size at maximum mass flow rate was obtained. The
dominant particle size in the mass flow of granular material exit-
ing the CFB reactor was fixed at 1.03 × 10−4m for all fluidized bed
inventory masses considered.
A completely different characteristic occurs for the mass flow
rate distribution of bottom-ash. From Fig. 11, it is impossible to
distinguish unambiguously only one characteristic particle size in
distributions of bottom-ash mass flow rate. Instead, three char-
acteristic peaks are distinguishable for bed inventory masses in
the range from 24.67 × 103 to 49.35 × 103kg. Distributions of
bottom-ash mass flow rate for the highest bed inventory mass is
characterized by one dominant particle size, i.e., 1.45 × 10−4m,
which corresponds to a maximal mass flow rate. The charac-
teristic peaks in the distributions of bottom-ash mass flow rate
for each analyzed bed inventory mass derive from the impact of
discharge from the combustion chamber. The results generated
by simulations using the population balance model have been
obtained assuming a constant discharge constant for ash removal
of 3.55 × 10−5s−1. Together with a decrease in bed inventory mass,
a significant influence of discharge constant on bottom-ash mass
flow can be seen in the function of particle size of the material.

58 A. Blaszczuk et al. / Particuology 25 (2016) 51–58
Fig. 11. Distributions of bottom-ash mass flow rate in a supercritical CFB reactor at
different bed inventory masses.
Conclusions
The study confirmed some theoretical predictions concerning
the impact of granular matter mass on the behavior of a com-
pound model for a supercritical CFB reactor. The change in granular
matter mass has no impact on feeding material mass flow, but
influences the distribution of bed inventory elutriation mass flow
and the distribution of the bed inventory attrition mass flow. An
increase in granular matter mass causes increases both in these
mass flows. With bed inventory mass ranging between 24.67 × 103
and 98.7 × 103kg, four characteristic peaks corresponding to the
dominant particle size undergoing attrition were identified. The
dominant particle sizes depended on the surface structure of the
bed inventory particles. Coarse particles with a hard structure have
almost zero mass flow in contrast to that for fine particles with a
soft structure. Furthermore, an increase in granular matter mass
led to an increase in circulating material mass flow. Maximum cir-
culating material mass flow was observed at a particle size equal to
1.23 × 10−4m. Attrition during the separation of solids in the com-
pact separator has a significant effect on the circulating material
mass flow. The distribution of the circulating material mass flow
is characterized by similarity in quality regarding the range of the
particle size for the bed inventory undergoing the elutriation pro-
cess. The variation of granular matter mass has some impact on
fly-ash mass flow and bottom-ash mass flow. The increase in gran-
ular matter mass is caused by an increase in fly-ash mass flows and
a reduction in bottom-ash mass flows. The diameter of particles
is a very important geometric parameter for both mass flow dis-
tributions of fly ash and bottom ash. The results generated by the
population mass balance model indicate only one dominant par-
ticle size (i.e., 1.03 × 10−4m) in distributions of fly-ash mass flow,
which corresponds to the maximum value for the mass flow. Dis-
tributions of bottom-ash mass flow indicate multimodal character.
The characteristic peaks in the distributions of bottom-ash mass
flow arise from the influence of the discharge system within the
furnace chamber of CFB reactor. The bed inventory needs to be
maintained in terms of both quantity and quality. Quantity means
the total mass of solids inside the CFB furnace whereas quality
denotes the size distribution of particles in the bed. The simula-
tion model is a good tool enabling the PSD to be monitored during
operation conditions of large-scale CFB combustion systems.
Acknowledgments
The authors gratefully acknowledge the staff of Tauron Gener-
ation S.A. Lagisza Power Plant for technical support in
operating
supplying
data. This work was financially supported by Scientific
Research Grant No. BS-PB-406/301/11.
References
Adamczyk, W. P., We˛cel, G., Klajny, M., Kozołub, P., Klimanek, A., & Białecki, R. A.
(2014). Modeling of particle transport and combustion phenomena in a large-
scale circulating fluidized bed boiler using a hybrid Euler–Lagrange approach.
Particuology, 16, 29–40.
Basu, P. (2006). Combustion and gasification in fluidized beds. New York: Taylor &
Francis Group.
Bis, Z. (1991). Aerodynamics of circulating fluidised bed. Monograph no. 21. Poland:
Publ. Office of Czestochowa University of Technology (in Polish).
Bis, Z. (2010). CFB boilers. Theory and practice. Poland: Publ. Office of Czestochowa
University of Technology (in Polish).
Błaszczuk, A., Komorowski, M., & Nowak, W. (2012). Distribution of solids concen-
tration and temperature in the combustion chamber of the SC OUT CFB boiler.
Journal of Power Technologies, 92, 27–33.
Blaszczuk, A., Leszczynski, J., & Nowak, W. (2013). Simulation model of the mass bal-
ance in a supercritical circulating fluidized bed combustor. Powder Technology,
246, 317–326.
Blaszczuk, A., & Nowak, W. (2014). Bed-to-wall heat transfer coefficient in a super-
critical CFB boiler at different bed particle sizes. International Journal of Heat and
Mass Transfer, 79, 736–749.
Błaszczuk, A., Nowak, W., & Jagodzik, S. (2013). Effect of operating conditions on
deNOxsystem efficiency in supercritical circulating fluidized bed boiler. Journal
of Power Technologies, 93, 1–8.
Blaszczuk, A., Nowak, W., & Jagodzik, S. (2014). Bed-to-wall heat transfer in a super-
critical circulating fluidised bed boiler. Chemical and Process Engineering, 35,
191–204.
Chalermsinsuwan, B., Boonprasop, S., Nimmanterdwong, P., & Piumsomboon, P.
(2014). Revised fluidization regime characterization in high solid particle con-
centration circulating fluidized bed reactor. International Journal of Multiphase
Flow, 66, 26–37.
Ghadiri, M., & Zhang, Z. (2002). Impact attrition of particulate solids. Part 1: A theo-
retical model of chipping. Chemical Engineering Science, 57, 3659–3669.
Grosschmidt, D., Habisreuther, P., & Bockhorn, H. (2007). Calculation of the size
distribution function of soot particles in turbulent diffusion flames. Proceedings
of the Combustion Institute, 31, 657–665.
Howard, J. R. (1989). Fluidized bed technology: Principles and applications. New York:
Adam Hilger.
Klett, C., Hartge, E.-U., & Werther, J. (2005). Time-dependent behavior of the ash
particle size distribution in a circulating fluidized bed system. Proceedings of the
Combustion Institute, 30, 2947–2954.
Lakatos, B. G., Süle, Z., & Mihálykó, C. (2008). Population balance model of heat
transfer in gas–solid particulate systems. International Journal of Heat and Mass
Transfer, 51, 1633–1645.
Lakshmikantham, V., & Trigiante, D. (2002). Theory of difference equations: Numerical
methods and applications (2nd ed.). New York: Marcel Dekker Inc.
Leszczynski, J. S. (2013). Basic boiler cumulative distributions (fly ash, circulating
material, bottom ash) – oxy-fuel and classical combustion conditions. Powder
Technology, 249, 536–548.
Myöhanen, K., & Hyppänen, T. (2011). A three-dimensional model frame for
modelling combustion and gasification in circulating fluidized bed furnaces.
International Journal of Chemical Reactor Engineering, 9(1) http://dx.doi.org/10.
1515/1542-6580.2571. Article A25
Nikku, M., Myöhanen, K., Ritvanen, J., & Hyppänen, T. (2014). Three-dimensional
modeling of fuel flow with a holistic circulating fluidized bed furnace model.
Chemical Engineering Science, 117, 352–363.
Qi, X. B., Zhu, J., & Huang, W. X. (2008). A new correlation for predicting solids con-
centration in the fully developed zone of circulating fluidized bed risers. Powder
Technology, 188, 64–72.
Redemann, K., Hartge, E. U., & Werther, J. (2009). A particle population balancing
model for a circulating fluidized bed combustion system. Powder Technology,
191, 78–90.
Saastamoinen, J., & Tourunen, A. (2012). Model for char combustion, particle size
distribution, and inventory in air and oxy-fuel combustion in fluidized beds.
Energy & Fuels, 26(1), 407–416.
Scala, R., & Chirone, R. (2010). Combustion of single coal char particles under flu-
idized bed oxyfiring conditions. Industrial & Engineering Chemistry Research,
49(21), 11029–11036.
Sekret, R. (2011). An analysis of temperature distribution and heat transfer in a
large-scale CFB boilers. Rynek Energii, 6(97), 144–150.
Tomeczek, J. (1992). Coal combustion. Gliwice, Poland: Publ. Office of the Silesian
University of Technology, no 1667.
Wang, Q., Luo, Z., Ni, M., & Cen, K. (2003). Particle population balance model for a
circulating fluidized bed boiler. Chemical Engineering Journal, 93, 121–133.
Wirth, K. E. (1991). Fluid mechanics of circulating fluidized beds. Chemical & Engi-
neering Technology, 14, 29–38.
Yang, C., & Gou, X. (2006). Dynamic modeling and simulation of a 410t/h pyroflow
CFB boiler. Computers and Chemical Engineering, 31, 21–31.
Yang, H., Yue, G., Xiao, X., Lu, J., & Liu, Q. (2005). 1D modeling on the material balance
in CFB boiler. Chemical Engineering Science, 60, 5603–5611.
Zhang, Z., & Ghadiri, M. (2002). Impact attrition of particulate solids, Part 2: Experi-
mental work. Chemical Engineering Science, 57, 3671–3686.
