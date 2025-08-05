# Simulation_of_the_sulfur_retention_in_an (1)

**Fonte**: Simulation_of_the_sulfur_retention_in_an (1).pdf  
**Data de conversão**: 2025-07-30 15:05:00  
**Origem**: base_relevantes

---

Simulation of the sulfur retention in an oxy-fuel 20 MW CFB
combustor.
M. de las Obras-Loscertales, F. García-Labiano, L. F. de Diego, P. Gayán, A. Abad, J.
Adánez
Instituto de Carboquímica (ICB-CSIC), Miguel Luesma Castán 4, 50018-Zaragoza, Spain
mobras@icb.csic.es
Abstract
Oxy-fuel combustion is a CO capture technology which consists of burning the fuel with a
2
mix of pure oxygen and recycled flue gas, mainly composed of H O(v) and CO . Therefore,
2 2
after steam condensation, the CO concentration in the flue gas may be enriched up to 95%
2
(dry basis). Many of current researches are related to oxy-fuel pulverized coal combustion.
However, circulating fluidized bed combustors can be a promising technology because in
addition to other advantages, they have the possibility of carrying out the in situ
desulfurization process via Ca-based sorbent added into the combustor which is highly
dependent on the temperature and concentration of CO . Because under oxy-fuel combustion
2
the sorbent can be surrounded by CO concentrations ranging from 60 to 90%, the sulfation of
2
the Ca-based sorbent can be performed at calcining (CaO solid reactant) or non-calcining
conditions (CaCO solid reactant).
3
A particle sulfation model has been developed to describe the limestone sulfation reaction
which is carried out in two steps. The simplicity of the kinetic model permitted it to be
incorporated easily in a 1.5D computational simulation model of an oxy-fuel CFB to predict
the sulfur retention reached inside the boiler. The model is capable of giving important
information about the oxy-coal combustion process such as longitudinal profiles of the gases
(O , CO , H O, SO , etc.), char concentration distribution, combustion efficiency and sulfur
2 2 2 2
retention at different operating conditions. A simulation considering the main operating
variables such as temperature, sorbent reactivity, O concentration fed, type of coal and the
2
use of a desulfurization unit in the recycled flue gas was carried out to determine the most
influential ones. The model is considered a useful tool to optimize the oxy-fuel combustion
process in circulating fluidized bed combustors.
Keywords: Modeling, Oxy-fuel, Sulfur retention, Circulating Fluidized Bed
1. Introduction
Nowadays, there is a great public awareness about the emissions of pollutant gases into the
atmosphere from large power plants. The release of CO and SO gases from coal combustion
2 2
to generate electric power causes serious environmental problems. The former contributes to
the build-up of greenhouse gases and the latter to acid rain formation. According to the IPCC
2005 [1], CO capture and storage technologies could be promising to mitigate CO emissions
2 2
from large power plants into the atmosphere. The development of CO capture technologies to
2
obtain an outlet gas stream in energy generation processes with high CO concentration seems
2
to be one of the most reliable solutions to slow down the increase of CO in the future.
2
Oxy-fuel combustion is a Carbon Capture technological option which consists of burning the
fuel with a mix of pure oxygen and recycled flue gas which is mainly composed of CO .
2
Therefore, the CO concentration in the flue gas may be enriched up to 95% (dry basis) in
2
order to be subsequently transported and stored. Nowadays, oxy-fuel combustion is still under

development and it has been not yet used commercially for CO capture. Nevertheless,
2
several large-scale demonstration boilers are planned for the future: White Rose, FuturGen,
Datang Daqing and Shanxi International Energy Group CCUS projects [2]. All of them refer
to pulverized coal (PC) boilers. However, circulating fluidized bed combustors (CFBCs) can
be promising candidates for new coal fired power plants [3-5] because the circulation of
solids can provide an effective control of the temperature in the boiler and the in situ
desulfurization process can be carried out by supplying Ca-based sorbents into the combustor.
The OXYCFB 300 Compostilla project was expected to start in 2018 but, nowadays, this
project is considered cancelled due to lack of funding [2].
Depending on the operating conditions existing in fluidized bed (FB) combustors, the sorbent
can present different behavior. Figure 1 shows the thermodynamic equilibrium curve of
CaCO calcination. As can be seen, at typical air combustion in FB (≈15% CO and 850 ºC),
3 2
the sorbent always calcines (R1) and thus the sulfation of the CaO, so-called indirect
sulfation, takes place (R2). However, under oxy-fuel combustion, the sorbent can be
surrounded by CO concentrations ranging from 60 to 90 % in the FB reactor and thus the
2
sulfur retention can be produced under indirect (R2) or direct sulfation (R3).
CaCO CaO + CO (R1)
3 2
CaO + SO + ½ O CaSO (R2)
2 2 4
CaCO + SO + ½ O CaSO + CO (R3)
3 2 2 4 2
700 750 800 850 900 950 1000
Temperature (ºC)
)aPk(
erusserp
laitrap
OC
2
1.0
0.8 Oxy-fuel CFB
combustion
0.6
CaCO
3
Non calcining
0.4 conditions
CaO
0.2 Calcining conditions
Air CFB combustion
0.0
Figure. 1. Thermodynamic equilibrium curve of CaCO calcination.
3
In previous studies performed in a TGA and in a batch FB to analyze the reactivity of
different Ca-based sorbents, it was observed that that the highest sulfation conversions were
reached at calcining conditions and the sulfation reaction was carried out in two steps, the
former being faster than the latter. Therefore, a sulfation kinetic model operating under
calcining conditions was developed taking into account both steps. It was assumed that the
first step was controlled by the gas diffusion through the porous system of the particle and the
second step by the gas diffusion through the product layer according to shrinking core model
[6].
In this work, an air CFBC model (1.5D) previously developed and validated by the research
group [7-9] has been adapted to oxy-fuel combustion conditions. This oxy-fuel CFBC model
(1.5D) considers the recycled flue gas and the sulfation kinetic model previously developed.
The simulation of this CFBC model has been capable of predicting the longitudinal profiles of
the different gaseous products (O , CO, CO , H O and SO ) along the boiler, the combustion
2 2 2 2
efficiency and the sulfur retention reached at different operating conditions. In summary, the

simulation of the model has been very useful to know the effect of the main operating
variables on sulfur retention in this type of boilers.
2. Sulfation reaction model.
The sulfation reaction model has been subject of many experimental and theoretical
investigations. However, most of them are complex and their integration in a model of boiler
is difficult when combustion and sulfation processes are carried out simultaneously.
In this work, a model based on the shrinking core model was proposed to predict the behavior
of limestones during the sulfation reaction in oxy-fuel firing mode under calcining conditions
at typical time scales and particle sizes of CFBCs. This model was chosen due to its
simplicity in order to be easily incorporated into global CFBC models.
To develop this sulfation model, the techniques used for the sorbent characterization were a
TGA and a batch FB. The TGA permitted the study of gas-solid reactions for long time test in
differential operating conditions and the batch FB allowed the sorbent characterization in
similar conditions to those existing in fluidized bed combustors, such as simultaneous
calcination and sulfation, attrition, thermal shock and crackle.
It was observed that the model predicted properly the evolution of the sorbent sulfation
conversion assuming that the first step of the sulfation reaction was controlled by the gas
diffusion through the porous system of the particle up to the blockage of its outer pores by
CaSO formation, and the second step by the gas diffusion through the CaSO product layer.
4 4
The main equations that define the process were the following [6]:
First step: Controlled by the gas diffusion through porous system of the particle
 R3 r3R r  1 1 
t diff1  3 Ca D O C 0 R c r Z 0 1 c    x 1 Z 1     t diff1 < t 1 (1)
0 SO2 0 c  0 l 0 0 
X
s,max

1


0
Z 1
X
s
x
l
R 0 3
R

3
r c 3 (2)
0 0
D D  2 (3)
e 0
Second step: Controlled by the gas diffusion through product layer.
23 23
t diff2 t 1 3    1 X 1     1 X s     2  X s  X 1   t
diff2
>t
1
(4)
   X   X    X 
diff2  s,max   s,max   s,max 
 
 X d2
CaO lim p (5)
 
diff2 24D C
s SO2
The transition from the first to the second step is produced when D
e
()=D
s
which corresponds
to a time, t , and a sulfation conversion, X . Figure 2 shows the predictions of model at
1 1
different operating conditions using the kinetic parameters obtained for Granicarb limestone.

0 5 10 15
Time (h)
)-(
sX
0.6
Granicarb limestone Granicarb limestone Granicarb limestone
0.5 dp= 0.3-0.5 mm T=900 ºC T=900 ºC 0.2-0.3 mm
3000 vppm SO dp= 0.3-0.5 mm 3000 vppm SO
0.4 2 4500 vppm 2
900 ºC 0.3-0.5
0.3 3000
0.2 925
1500 0.5-0.63
950
0.1
0.0
0 5 10 105 5 10 15
Time (h) Time (h)
Figure 2. Sulfation conversion curves predicted by the sulfation reaction model.
3. Mathematical model of oxy-fuel CFBC (1.5D)
The mathematical model describes the behavior of a CFBC referred to coal combustion and
sulfur retention processes in oxy-fuel mode. The 1.5D model considers both radial and
longitudinal concentration profiles and assumes steady-state and isothermal operation at
macroscopic level. The model integrates different sub-models to describe the main processes
occurring inside the boiler as hydrodynamic, carbon combustion and sulfur retention. Figure 3
shows the scheme of the CFBC considered.
Figure 3. Scheme of the CFB boiler.
3.1. Hydrodynamic sub-model
The hydrodynamic characteristics of the CFBC are based on the works of Johnson et al. [10],
Johnson and Leckner [11] and Pallares et al. [12]. The riser is divided into three different
zones: bottom, similar to a bubbling bed; splash, with a predominant homogeneous particle
clustering flow; and transport zone, with a core-annulus structure.

The bottom zone consists of a bubble and emulsion phase where the total flow is assumed to
be the sum of three flows: the flow in the particulate phase, the visible bubble flow, and the
throughflow, that is, a flow through and between the bubbles. Likewise it was supposed that
the average voidage is constant in the entire zone and the emulsion phase remains under
minimum fluidization conditions.
In the splash and transport zones, the vertical distribution of solids was determined by means
of an exponential decay model. The solid concentration was assumed to be the sum of the
contribution from a cluster phase and a dispersed phase:
(  )expa(hH ) expK(H h) (6)
b d,b b exit 0
  expK(H H ) (7)
d,b exit 0 b
The upper level of the splash zone is defined as the height where the two terms (contributions
of cluster and dispersed phases) of equation (1) are equal. The decay constants in the splash,
a, and transport, K, zones as a function of the operating conditions, and are calculated with the
equations:
a4u /u (8)
t
K 0.23/(uu ) (9)
t
The solution of the hydrodynamic model gives at each height of the riser the mean voidage,
annulus and core voidages, core radius, upward solids flow in the core, downward solids flow
in the annulus and external circulation of solids flux.
3.2. Coal combustion sub-model
The carbon combustion model takes into consideration all the processes that coal particles
undergo when they are fed into the combustor such as drying, devolatilization and volatiles
combustion, and char combustion. The model developed by de Diego et al. [13] is used to
calculate the volatile generation rate of the coal. In this model the drying and pyrolysis of coal
particles are assumed to be a coupled process controlled by the kinetics of devolatilization and
the heat transferred to and through the particles. The volatiles generated during
devolatilization are considered as a mixture of H O, CO, CO , H , CH , C H and C H . The
2 2 2 4 2 4 3 8
excess of C is considered as elementary C, which is instantaneously oxidized to CO. The
volatile combustion process is modelled considering different chemical reactions with their
corresponding reaction rates [14].
Char combustion. To fulfill mass balances and determine carbon combustion efficiencies in a
CFB with shrinking particles, it is necessary to develop population balances of char particles
in the different zones of the CFBC (bottom, splash, and transport zones).
For discrete particle size distributions, the population balances of char particles in the bottom
and splash zones, involve the following system of equations [15]:
r
F* r W r (r ) i P (r)W k r
W i i cl,i1 shrink i1 r f i cl,i f i
P(r)r  cl,i  i1 (10)
3 i i W Fr W r (r)3W r (r)r /r W k r
cl 3 i cl shrink i cl shrink i i i cl f i
where F* = F + F + F
i 0,i 1,i 2,i
The population balances of char particles burning in each compartment j of the transport
region involve the following expression for the core region:

r
F r W r (r ) i P (r)W k r
P (r)r 
F
3i,j 
3i,j1 i cc,i1,j shrink i1 r
i1
f i cc,i,j f i
(11)
3,j i i F F r W r (r)T r 3W r (r)r /r W k r
3 3,j i cc,j shrink i 3,j i cc,j shrink i i i cc,j f i
The solution of the population balances in the bottom+splash and transport regions allows us
to determine the carbon flow rates in all streams of the process.
For the solution of char population balances, it is necessary to know the individual shrinking
rates (r) of the char particles. Assuming the shrinking unreacted particle model, with mixed
i
control by chemical reaction and mass transfer in the gas film and with a first order of
reaction, the shrinking rates of char particles are given by the expression:
dr 12C
 
r shrink (r i ) 

 dt 

 j
c
ρ
c
(1/k
c
d O2
p
/ShD
g
) (12)
The term C indicates the effective oxygen concentration around the char particles burning at
O2
any point of the boiler. Therefore, the population balances must be solved at the same time as
the oxygen profiles in the boiler. In addition, the following equation is used for the
combustion process according to the kinetic constants determined for the coal used in this
work:
k T exp(75.4/RT ) (13)
c s s
The solution of the mathematical model implies the simultaneous convergence of the char
particle population balances and the oxygen profile in the riser. Since the oxygen
concentration at each height depends on the char and volatile combustion, mass balances for
the char, oxygen and volatiles is simultaneously solved.
3.3. Sulfur retention sub-model
Sulfur retention (SR) rate inside the CFB boiler depends on both the SO generation rate and
2
sorbent sulfation rate (which depends on the sorbent characteristics). Both processes can be
produced in the different zones of the boiler (bottom, splash and diluted zone).
SO generation rate is a function of the coal combustion rate which includes the sulfur coming
2
from both volatiles and char. Therefore, the longitudinal profile of SO release along the riser
2
is a direct consequence of the coal combustion process and is determined by the previous
combustion model.
The SO retention rate strongly depends on the SO concentration existing at the different
2 2
zones of the boiler. This concentration is conditioned by the SO generation process and by
2
the sulfation capability of the sorbent.
In each location of the boiler with a given SO concentration, the mean reactivity is defined as
2
a function of the mean solids residence time (), assuming perfect mixing of the solids in the
whole bed.
 dX    dX  et/(r i )
 s    S  E(t)dt E(t) (14)

dt
 0 
dt

(r
i
)
The mean residence time of the sorbent is defined by solving the hydrodynamic model
previously developed. The sorbent reactivity was calculated using the sulfation model of two
step above-mentioned and defined by the equations (1) (2) (3) (4) and (5) where the first step
was controlled by the gas diffusion through porous system of the particle and the second step
by the gas diffusion through product layer.

The calculation of sulfur balance is solved at the different compartments from the bottom to
the top of the riser. Therefore, the SO concentration at the outlet gas stream is known.
2
Finally, the sulfur retention in the boiler is given by the following equation considering the
sulfur fed from the coal and the SO obtained at the outlet gas stream.
2
F x /M QC
R  0,coal S,coal S S .100 (15)
S F x /M
0,coal S,coal S
Once the sulfur retention is calculated, the mean sulfation conversion of the sorbent can be
determined by means of the following expression,
R
X  s (16)
S Ca/S
After solving both the carbon combustion and the sulfur retention processes, the model is able
to predict the longitudinal profiles of the different gaseous products (O , CH , C H , C H ,
2 4 2 4 3 8
H , CO, CO , H O and SO ) along the boiler. In addition, the model predict the concentration
2 2 2 2
and particle size distribution of the char particles in the different locations of the boiler as well
as the combustion efficiency and sulfur retention obtained at the different operating
conditions.
4. Simulation
Once the mathematical model 1.5D was developed, the simulation of the oxy-CFB combustor
model focused on the sulfur retention process at different operating conditions was carried
out. Table 1 shows the main input data used as reference case in the model simulation.
Table 1. Simulation conditions used in the reference case.
Units Units
Power [MW] 20 Coal composition Anthracite
t
Moisture wt.-% 2.3
Furnace dimensions Ashes wt.-% 31.8
Diameter [m] 2.5 C wt.-% 52.6
Height [m] 20 H wt.-% 1.7
N wt.-% 0.93
Cyclone dimensions S wt.-% 1.52
diameter [mm] 875 LHV [MJ/kg] 20
Particle size
Operating parameters n=2
Coal distribution (Rosin -
Rammler)
Temperature [ºC] 900 Sorbent [mm] 0.2
Linear velocity [m/s] 5.0
Pressure drop [Pa] 2500 Granicarb kinetic parameters
0
Inlet O [vol.%] 25 D [m2/s] 1.35 10-5
2 0
O
2
excess [vol.%] 5 e (m) 29
Ca/S [mol/mol] 2 D [m2/s] 1.5 10-8
s
Total solids flow in [kg/h] 1200
Hydrodinamic sub-model defines the solids distribution inside the reactor taking into account
the operating conditions used (temperature, gas velocity, pressure drop, etc.) and the different
height of zones (bottom, splash and diluted). Figure 4 shows the profiles of solids

concentration () in the combustor for the reference case. Likewise, hydrodynamic also
determines the coal and char distribution along the combustor and thus the distribution of the
different gases. Figure 5 shows the profiles of gases concentration in the combustor for the
reference case. As can be seen, an increase in CO concentration together with a decrease in
2
O concentration is produced in the splash zone because the majority of the combustion
2
process takes place in that zone, which combines high solids and oxygen concentrations.
Regarding SO gas, a decrease of SO concentration along the diluted zone is observed as a
2 2
consequence of the sulfur retention process which prevails over SO generation in that zone.
2
0.00 0.15 0.30 0.45 0.60
Solids concentration ( )
)m(
h
SO concentration (vppm)
2
0 500 100015002000
20
15
(Core)
10 Dilute zone
5
Splash zone
Dense zone
0
)m(
h
20
15
CO
2
10 SO
2
HO 5 2
Splash zone
O
2
Dense zone
0
0 20 40 60 80 100
Gases concentration (vol.%)
Figure 4. Solids concentration profiles. Figure 5. Gases concentration profiles.
4.1. Effect of the temperature
As stated above, the conditions exiting in the boiler can lead to a different behavior of the
sorbent. Therefore, depending on the temperature and the CO concentration in the flue gas
2
recirculation is likely to find conditions inside the boiler in which the sorbent could calcine or
not.
In Figures 6a and 6b are represented the SO profiles and sulfur retention values obtained in
2
the simulation at different temperatures ranging from 850 to 950 ºC, that is, from non
calcining to calcining conditions. It was observed that the highest sulfur retentions are
reached operating under calcining conditions. This can be attributed to the fact that the
porosity of the calcined limestone (CaO) is much higher than that of the raw limestone
(CaCO ) and thus, SO can easily diffuse through the porous system of the particle reaching
3 2
higher sulfation conversions. In addition, an optimum temperature was found to be around
900ºC. This is in agreement with the results obtained in previous works [16-18].

0 1000 2000 3000
SO concentration (vppm)
2
)m(
h
20
900
15 925 950
850ºC
10
5
0
800 850 900 950 1000
Temperature (ºC)
)%(
RS
100
80
60
Non calcining Calcining
40 conditions conditions
20
0
Figure 6a. SO profiles at different Figure 6b. Effect of temperature on sulfur
2
temperatures. retention.
4.2. Effect of the limestone reactivity
Another remarkable parameter to take into account in order to work in CFBCs is selecting an
adequate Ca-based sorbent to perform the desulfurization process. In this section, the
variation of the kinetic parameters determined in a previous work [6] for the first and second
steps has been simulated. Figures 7a and 8a show the sulfation conversion curves of the
limestone used for the first and second sulfation steps assuming that they present a maximum
sulfation conversion (X ) nearly 0.52. Figures 7b and 8b illustrate the results obtained in
s,max
the simulation at different Ca/S molar ratio.
0 2 4 6 8 10
Time (h)
)-(
sX
1.0
C = 3000 vppm
SO2
D = 1.5 10-8 m2/s 0.8 s
0.6 D 0
0.4
1.5 10-4 m2/s
1.35 10-5
0.2 6.0 10-6
0.0
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5
Ca/S (mol/mol)
)%(
RS
100
80 D 0
60
40
20
0
Figure 7a. Sulfation conversion curves of the Figure 7b. Effect of D on sulfur
0
limestone at different diffusional coefficients, D . retention at different Ca/S molar ratio.
0

0 2 4 6 8 10
Time (h)
)-(
sX
1.0
C = 3000 vppm
SO2
D = 1.35 10-5 m2/s
0.8 0
D
0.6 s
0.4
3.38 10-8
1.5 10-8
0.2 1.35 10-9 m2/s
0.0
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5
Ca/S (mol/mol)
)%(
RS
100
80 D s
60
40
20
0
Figure 8a. Sulfation conversion curves of the Figure 8b. Effect of D on sulfur
s
limestone at different diffusional coefficients, D retention at different Ca/S molar ratios
s
As it was expected, higher the Ca/S molar ratio leads to higher sulfur retention values.
Moreover, the higher the diffusional coefficient, the higher the sulfur retention values since an
increase in the diffusional coefficients is associated with an increase in the limestone
reactivity. Likewise, it was observed that the influence of the diffusional coefficient of the
second step has more relevance than those of the first step, corroborating the results reported
by other authors about the importance of the residual activity of the sorbent [19].
4.3. Effect of the inlet oxygen concentration
An important feature in oxy-fuel combustion is the O /CO ratio in the inlet gas stream. It is
2 2
known that a higher inlet O concentration leads to reducing the boiler size, and therefore
2
capital expenses, and to reducing the recycled flue gas which diminishes energetic penalty
[20].
0 600 1200 1800
SO concentration (vppm)
2
)m(
h
20
25 vol.%O
2
30 vol.%O
2
35 vol.%O
15 2
10
5
0
1.5 2.0 2.5 3.0 3.5
Ca/S (mol/mol)
)%(
RS
100
O
2
95
90
85
80 35 vol.% O
2
30 vol.% O
75 2
25 vol.% O
2
70
Figure 9a. SO profile generated in the Figure 9b. Effect of inlet oxygen
2
combustor at different inlet O concentration. concentration on sulfur retention at different
2
Ca/S molar ratios
In this section, the simulation of the effect of O concentration entering the reactor on the
2
sulfur retention is analyzed. Simulation tests with typical inlet O concentrations from 25 to
2

35 vol.% were performed, setting an outlet O concentration around 4 vol.%. As can be seen
2
in Figures 9a and 9b, an increase in O concentration causes an increase in coal feeding
2
leading to higher SO concentration inside the combustor and consequently higher sulfur
2
retention.
4.4. Effect of the type of coal.
One of the advantages of the CFBC is the high versatility that they present to burn different
types of fuel. This technology is feasible to burn both low reactivity coals, as anthracites, and
high reactivity coals, as lignite. Likewise, coals with low heating value due to their high ashes
content and even biomass can be also processed in CFBCs.
In this section, the simulation of three different coal ranks ranging from lignite to anthracite
was carried out. Table 2 gives the proximate and ultimate analysis of the coals used.
It is worth mentioning the different sulfur content of the coal used, lignite having the highest
content (5.91 %) and bituminous having the lowest content (0.8 %). The operating conditions
simulated were the same as those of the reference case.
Table 2. Ultimate and proximate analysis of the coals used.
Anthracite Lignite Bituminous
Proximate analysis (%wt)
Humedad 2.3 12.6 5.2
Cenizas 31.7 25.2 12.9
Volátiles 5.6 28.7 32.7
C Fijo 60.4 33.6 49.2
Ultimate analysis (%wt, d.b. )
C 61.02 51.95 69.2
H 1.71 2.85 4.3
N 0.95 0.74 1.6
S 1.55 5.91 0.8
LHV* (kJ/kg) 21807 16252 25398
According to Figure 10, to reach sulfur retention values close to 90-95 %, using lignite as
fuel, three or six times more limestone should be fed compared to anthracite and bituminous
coal which would imply an increase in the solids waste generation (CaSO ).
4
0.0 0.1 0.2 0.3 0.4 0.5
limestone/coal feeding (kg/kg)
)%(
RS
100
80
60 Anthracite
Lignite
40
Bituminous
20
0
Figure 10. Dependence of sulfur retention with the limestone/coal feeding ratio for different
coals.

In Figure 11 are plotted the SO concentrations emitted at the exit of the combustor. It was
2
observed that he SO generated from lignite combustion was higher than that from anthracite
2
and this latter higher than that from bituminous coal.
)3mN/gm(
OS 2
15000
Anthracite
12500 Lignite
Bituminous
10000
7500
5000
2500
200 mg/m3
0
1.0 1.5 2.0 2.5 3.0 3.5
Ca/S (mol/mol)
Figure 11. SO concentration as a function of the Ca/S molar ratio for different coals.
2
According to data published by Vattenfall [21], to get a CO stream with medium level of
2
quality in order to be subsequently transported, a flue gas stream with a SO concentration
2
lower than 200 mg/Nm3 must be needed. Last proposals made by the Dynamis study
regarding the gas composition are more restricted. SO concentration in the CO stream must
2 2
reach values below 100 vppm [22]. Therefore, from the results obtained in the CFBC
simulation (see Figure 11), it can be concluded that if a Ca/S molar ratio of 2.5-3 was fed into
the combustor, the use of a desulfurization unit after the oxy-fuel combustion process to fulfill
with the transport requirements would not be needed.
4.5. Effect of using a desulfurization unit in the recycled flue gas.
The flue gas recirculation to control the operating temperature and inherently the inlet O
2
concentration is one of the main characteristics of the oxy fuel combustion processes. This
recycled flue gas can previously be cleaned, in this case being almost free of SO , to avoid
2
operationg problems related to the material corrosion.
Figure 12a. Scheme of a CFB combustion Figure 12b. Scheme of a CFB combustion
system without SO recirculation system with SO recirculation
2 2
Up to now, in the simulation tests performed, SO and CO from flue gas has been considered
2 2
to be recycled together and thus an increase in SO concentration inside the boiler was
2
produced. In this section, it has been assumed that there was a cleaning step, i.e., a
desulfurization unit, in the recycled flue gas to completely remove the SO from the
2

recirculation stream (see scheme of Figure 12a). The results obtained in this simulation were
compared to the reference case (see scheme of Figure 12b).
In Figure 13, the sulfur retention using or not using a desulfurization unit is shown as a
function of the Ca/S molar ratio. As can be seen, the highest sulfur retention values were
reached when the desulfurization unit was not used. Nevertheless, SO emissions were also
2
the highest (see Figure 14). This fact was because the SO concentration inside the boiler was
2
higher and thus the sulfation reaction rate was increased. Based on these results, to operate
using anthracite as fuel and Granicarb limestone as sorbent, a molar ratio close to 2.5-3 would
be needed to fulfill with the requirements of CO transport commented above.
2
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5
Ca/S (mol/mol)
)%(RS
100
No desulfurization
Unit
80 Desulfurization
Unit
60
40
20
0
Figure 13. Sulfur retention values reached
using or not using a desulfurization unit in
the recycled flue gas
)3mN/gm(
OS 2
6000
5000
No desulfurization
Unit 4000
3000
2000 Desulfurization
Unit
1000
200 mg /Mm3
0
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
Ca/S (mol/mol)
Figure 14. SO concentration obtained using
2
or not using a desulfurization unit in the
recycled flue gas.
5. Conclusions
The simulation of a CFBC under oxy-fuel combustion conditions has allowed us to know the
effect of the main operating variables on sulfur retention process.
On the one hand, temperature, type of coal (especially sulfur content of the coal) and sorbent
reactivity has been found to be the most influential parameters affecting sulfur retention
process. On the other hand, inlet O concentration had a minor effect on the sulfur retention.
2
In order to reach high sulfur retention values and to fulfil with the requirements of CO
2
transport, it would be necessary to operate in calcining conditions, especially at 900 ºC, and
with Ca/S molar ratio close to 2.5 – 3 such that a desulfurization unit would have not to be
used from the viewpoint of the sulfur retention process.
Acknowlegments
This work has been supported by The Spanish Ministry of Science and Innovation (MICINN,
Project: CTQ2008-05399/PPQ) and by FEDER. M. de las Obras-Loscertales thanks to
MICINN for the F.P.I. fellowship.
Nomenclature
a decay constant (m-1) T char surface temperature (K)
s
C gas concentration (kmol m-3) T flowrate of transmitted carbon from the core to
3
d particle diameter (m) annulus (kg s-1)
p
D diffusivity (m2 s-1) u superficial gas velocity (m s-1)
g
D effective diffusivity (m2 s-1) u single particle terminal velocity (m s-1)
e t

D the porous system gas diffusion coefficient W mass (kg)
0
(m2 s-1) x sulfur conversion of the product layer
l
D the product layer gas diffusion coefficient x sulfur mass fraction of coal
s s,coal
(m2 s-1) X the sorbent sulfation at t1
1
E(t) function of the mean solids residence time X sulfation conversion
s
(s-1) X maximum sulfation conversion
s,max
F carbon flow rates (kg s-1) Z the molar volume ratio of CaSO to CaO
0-7 4
F coal feeding (kg s-1)
0,coal
h height (m) Greek symbols
H height of bottom region (m) Δr size interval of population i (m)
b i
H o height of riser (m) 0 sorbent initial porosity
j c carbon fraction in the char ρ solid concentration (kg m-3)
k c apparent kinetic constant for surface reaction ρ b solid concentration in the bottom region
(m s-1) (kg m-3)
k f fragmentation rate constant (m s-1) ρ c average density of char (kg m-3)
K transport region decay constant (m-1) ρ density molar of CaO (mol m-3)
CaO
M s sulfur atomic weight (g mol-1) ρ d,b solid concentration due to the dispersed
P normalized size distribution function of the phase in the upper portion of the bottom
0-7
char stream (m-1) region (kg m-3)
P f size distribution function on mass basis of ρ exit solid concentration at the gas outlet
the fragments (m-1) (kg m-3)
r char particle radius(m) (r
i
) residence time of particle size r
i
(s)
r c radius of unreacted core (m) diff2 time to reach the maximum sorbent
r i mean radius of particles in population i (m) sulfation conversion with the reaction
r shrink (r i ) shrinking rate of char particles of size r i controlled by gas diffusion through the
(-r i ) combustion rate of gas I (kmol m-3 s-1) product layer (s)
R gas constant (J mol-1 K-1) Subscripts
R 0 initial particle radius of the limestone (m) cc carbon in the core
SR sulfur retention (%) cl carbon in the bottom and splash regions
Sh Sherwood number i relative to the differential element at height
t time(s) h in the transport region
t 1 the transition time between the first and the O 2 oxygen
second step in the limestone sulfation S sulfur
reaction (s)
References
[1] Metz B, Davidson O, de Coninck HC, Loos M, Meyer LA. IPCC special report on carbon
dioxide capture and storage, Cambridge, UK: Cambridge University Press; (2005).
[2] Global CCS Institute. http://www.globalccsinstitute.com/project/( 2015).
[3] Lupion M, Navarrete B, Otero P, Cortés VJ. Experimental programme in CIUDEN´s CO
2
capture technology development plant for power generation, Chem Eng Res Des 89 (2011)
p. 1494-1500.
[4] Myöhänen K, Hyppänen T, Pikkarainen T, Eriksson T, Hotta A. Near zero CO emissions
2
in coal firing with oxy-fuel circulating fluidized bed boiler, Chem Eng Technol 32 (2009)
p. 355–363.
[5] Czakiert T, Sztekler K, Karski S, Markiewicz D, Nowak W. Oxy-fuel circulating fluidized
bed combustion in a small pilot-scale test rig, Fuel Process Technol 91 (2010) p. 1617–
1623.
[6] de las Obras-Loscertales M, de Diego LF, García-Labiano F, Rufas A, Abad A, Gayán P,
Adánez J. Modelling of limestone sulfation for typical oxy-fuel fluidized bed combustion
conditions, Energy fuels 27 (2013) p. 2266-2274.

[7] Adánez J, de Diego LF. Modeling of carbon combustion efficiency in circulating fluidized
bed combustor. 1. Selection of submodels and sensitivity, Ind. Eng. Chem. res 34 (1995) p.
3129-3138.
[8] Adánez J, Gayán P, de Diego LF. Modelling and simulation of the sulphur retention in
circulating fluidized bed combustors, Chem Eng Sci 51 (1996) p. 3077- 3082.
[9] Adánez J, de Diego LF, García Labiano F, Gayán P. Suphur retention in circulating
fludised bed coal combustion. Modeling and simulation, Coal Sci Tech (1995) p. 1839-
1842.
[10] Johsson F, Svensson A, Leckner B. Fluidization regimes in circulating fluidized bed
boiler. In: Potter O, Nicklin D, editors. Fluidization VII. Engineering Foundation
Conference, New York; (1992) p. 471.
[11] Johnsson F, Leckner B, Vertical distribution of solids in a CFB-furnace. Proc. 13rd
International Conference on FBC. ASME: Fairfield, NJ. (1995) p. 671.
[12] Pallares i Tella D, Johnsson F. Project report JOR3CT980306, Department of Energy
Conversion, Chalmers University of Technology. (2000).
[13] de Diego LF, García-Labiano F, Abad A, Gayán P, Adánez J. Modeling of the
devolatilisation on nonspherical wet pine wood particles in fluidised beds, Ind Eng Chem
Res 41 (2002) p. 3642-3650.
[14] Adánez J, Gayán P, de Diego LF, García-Labiano F, Abad A. Combustion of wood chips
in a CFBC. Modeling and validation, Ind Eng Chem Res 42 (2003) p. 987-999.
[15] Gayán P, Adánez J, de Diego LF, García-Labiano F, Cabanillas A, Bahillo A, Aho M,
Veijonen K. Circulating fluidised bed co-combustion of coal and biomass, Fuel 83 (2004)
p. 277-286.
[16] García-Labiano F, Rufas A, de Diego LF, de las Obras-Loscertales M, Gayán P, Abad A,
Adánez J. Calcium-based sorbents behaviour during sulphation at oxy-fuel fluidised bed
combustion conditions, Fuel 90 (2011) p. 3100-3108.
[17] de Diego LF, de las Obras-Loscertales M, García-Labiano F, Rufas A, Abad A, Gayán P,
Adánez J. Characterization of a limestone in a batch fluidized bed reactor for sulfur
retention under oxy-fuel operating conditions. Int J of Greenh Gas Control 5 (2011) p.
1190-1198.
[18] de Diego LF, Rufas A, García-Labiano F, de las Obras-Loscertales M, Abad A, Gayán P,
Adánez J. Optimum temperature for sulphur retention in fluidised beds working under oxy-
fuel combustion conditions Fuel 114 (2013) p. 106-113.
[19] Abanades JC., de Diego LF, García-Labiano F, Adánez J. Residual activity of sorbent
particles with a long residence time in a CFBC, AIChE J 46 (2000) p. 1888-1893.
[20] Bolea I, Romeo LM, Pallarés D. The role of external heat exchangers in oxy-fuel
circulating fluidized bed. Appl Energy 90 (2012) p. 215-223.
[21] PTECO2. Transporte de CO . Estado del arte, alternativas y retos. (2013).
2
[22] Vattenfall. CO quality requirements for CO capture, transport and storage from a
2 2
lignite fired power plant. A report within the CO free power plant project. Report no.
2
U04:64. (2004).
