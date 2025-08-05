# Comparative_study_on_air_and_oxy_combust

**Fonte**: Comparative_study_on_air_and_oxy_combust.pdf  
**Data de conversão**: 2025-07-30 15:07:15  
**Origem**: base_relevantes

---

Comparative study on air and oxy combustion in a pilot CFB boiler
Jenö Kovács*, Matias Hultgren*, Mikko Jegoroff**, Hannu Mikkonen**,
Antti Tourunen**, Ari Kettunen ***
* University of Oulu, Systems Engineering Laboratory, Oulu, Finland, jeno.kovacs@oulu.fi and
hultgrma@mail.student.oulu.fi
** VTT Technical Research Centre of Finland, Jyväskylä, firstname.lastname@vtt.fi
***Foster Wheeler Energy Ltd, Varkaus, Finland, ari.kettunen@fwfin.fwc.com
Abstract: In the present work, measurement experience of oxy combustion in a pilot scale circulating
fluidized bed (CFB) combustor is summarized. The aim was to study combustion dynamics under air-
and oxygen-firing conditions in order to develop and validated combustion controls for Flexi-BurnTM
CFB combustion technology. Dynamic CFB-pilot combustion tests were carried out including various
step and ramp tests in both air and oxy combustion and different operation strategies for oxy combustion.
Keywords: Dynamic modelling, simulation, control, power plant, efficiency, plant wide control.
1. INTRODUCTION
Fig. 1 shows a simplified process flow scheme of a power
CO Capture and Storage (CCS) is seen as one of the key plant designed for both air-fired and oxygen-fired operation
2
technologies for cutting CO emissions from coal power modes. It consists of an air separation unit (ASU), a high-
2
plants. CCS technology can capture approximately 80-90% efficiency steam cycle utilizing FW Flexi-Burn CFB boiler
of CO2 emissions before entering the atmosphere produced technology and a CO processing unit (CPU). For oxy-fuel
2
by coal power plants and heavy industry, transport them in combustion, which is the primary operation mode, oxygen is
liquid form by pipeline or ship, and subsequently inject them mixed with recycled flue gases, which creates a mixture of
into geological formations deep underground where they are primarily O and CO (and H O) used as oxidant in
2 2 2
stored permanently below the earth’s surface. CO2 can be combustion instead of air. The absence of air nitrogen
captured using three existing technologies: pre-combustion, produces a flue gas stream with a high concentration of CO ,
2
post-combustion or oxy-fuel combustion. making it much easier to separate the CO . In the air firing
2
mode, which serves risk mitigation purposes but may also be
The European Commission has selected six CO capture and applied during high load demand, the ASU and CPU are out
2
storage demonstration projects for funding by the European of service (or in stand-by) and the plant is operated like a
Energy Programme for Recovery (EEPR). The aim of the EU conventional power plant, leading flue gases to the
is to make zero emission power generation using CCS atmosphere.
commercially feasible by 2020. One of those is the
C
fu
o
ll
m p
C
o
C
st
S
il la
c h
(
a
S
i
p
n
a
,
in
u
)
s i
p
n
r
g
o je
o
c
x
t
y
w
-f
h
u
i
e
c
l
h
c
a
a
im
pt
s
u r
t
e
o
t
d
e
e
c
m
hn
o
o
n
l
s
o
tr
g
a
y
t e
a
t
n
h
d
e
M ix
95-97% O2, (Ar, N2)
N2, (Ar)
sepa
A
r
i
a
r
tion
Air
supercritical Flexi-Burn TM circulating fluidized bed (CFB) Flue gas recycle
t M ec W hn o co lo a g l- y f . i r T ed h is p i t l e o c t h p n l o a l n o t g ( y A w lv i a ll r e f z ir s e t t b a e l . te 2 s 0 t 1 e 1 d ) o t n h a a t n w e i w ll 3 b 0 e Fuels F C l F e B xi b -B o u il r e n r F cl l e u a e n g i a n s g CO2/H2O C C o o n m d p e r n e s s a s t i i o o n n Vent gas
Purification
scaled to a demonstration plant of about 323 MW by the end
H2O CO2
of 2015. The CO2 emissions capture rate is expected to be
91%. Captured CO2 will be stored in a nearby saline aquifer. t S u t r e b a in m e G T S ra to n r s a p g o e rt
It is estimated that five million tones of CO2 will be stored
during the first five years of operation. (EU Commission, Fig.1. Schematic of a Flexi-BurnTM CFB power plant.
2010)
The Flexi-Burn TM CFB technology by Foster Wheeler offers Experiments done at test facilities of different scales provide
the flexibility for bringing CCS or CCS-readiness to new information about the differences between the two modes of
power plants, as well as to existing plants as a retrofit option; operation, with the acquired knowledge being incorporated in
the boilers can be operated in either conventional or oxy-fuel boiler design tools. Pilot-scale tests were carried out at a pilot
combustion mode, preferably without any significant test rig at the VTT (Jyväskylä, Finland). The results of the
modifications needed to the plant. (Eriksson et al. 2009) tests were utilized to validate a Matlab/Simulink model,

which provides a basis for further simulation experiments sampling. Fly ash samples can be taken from the secondary
comparing air and oxy combustion. The rest of this paper cyclone, gas cooler, and bag house filter. The combustor is
includes the description of the pilot test rig and the test equipped with extensive temperature and pressure
matrix, followed by the description of the model and some measurements. Flue gas composition is measured by FTIR
experimental results. spectrometer and by traditional on-line gas analyzers.
Fuels can be fed into the combustor through two separated
fuel containers. Fuel containers are mounted on the scales in
2. PILOT PROCESS order to determine mass flows of fuels. Limestone, sand and
other additives can be fed into combustor to the same level as
A pilot-scale CFB combustor with a fuel power of 50-100
fuels, or into the circulating material loop below the primary
kW in oxy mode and 20-50 kW in air mode was investigated
cyclone.
in this study (Fig. 2). The height of the riser is 8.0 m and the
inner diameter is 167 mm. The combustor is equipped with
Flue gas recirculation system has been built up for oxygen
several separately controlled electrically heated and water/air
combustion tests. Oxygen combustion tests can be carried out
cooled zones in order to control the process conditions (for
also with bottled O and CO gases. Flue gas recirculation
example O level, temperature and load) and to create 2 2
2
system contains recirculation fan with flow measurement and
combustion conditions that better resemble those obtained in
control equipment. After the recirculation fan flue gas is
large-scale industrial boilers. Bed temperature can be
divided into primary and secondary gas lines. The flow rate is
controlled and heat transfer measured by different water
measured in the primary gas line, and the both lines have own
cooled tube-spiral type heat exchangers and by three
flow controlling valves. The oxidant gas can consist of air,
controllable water cooled tubes in the bed area. The CFB
N , O , CO , recirculated flue gas, or mixtures of these. Gas
pilot was controlled with a Siemens PCS7 automation 2 2 2
is divided into primary gas fed through the grid and
system, to which all measurement data was collected.
secondary gases fed to up to three different levels of the
combustor. The gas compositions can be adjusted
Bed material (bottom ash) can be sampled and discharged
independently for primary and secondary gases.
continuously or periodically above the grid by bottom ash
screw and circulation material sample can be taken below the
primary cyclone and from the loop seal. There are four ports
along the combustor freeboard area for gas and solid material
3. TEST MATRIX
The main goal of the test period was to obtain the major
Flue gas Deposit probes dynamic behaviour of oxy combustion. Therefore the tests
to stack
included a reference step-series for air combustion, a step-
series for oxy combustion, different load change in oxy
combustion and finally different strategies to switch between
Bag house Gas cooler air and oxy operation mode.
filter
The step-series were designed for the upper load levels
between 70 and 100%, for both air and oxy tests. Fuel,
Secondary cyclone limestone and gas flows (air flow in air mode and mixture of
Primary cyclone RFG and oxygen in oxy mode) were changed stepwise, see
Riser
Solids circulation sample Fig. 3. An hour settling time was provided between steps to
reach the final state.
Secondary and Temperature,
tertiary airs pressure and profile
In ramp tests in Fig. 4,, the main interest was to compare
sampling along the
different ramp speeds in oxy combustion. Three tests of this
combustor height
Fuel and type with one ramp down and one back up again were made:
additive feed
one slow ramp with a 15 % load change, one fast ramp with a
Gas tanks 15 % load change and one slow ramp with a 30 % load
(air, N2, CO2, O2) change.
In oxy combustion, there is an additional freedom –
Loop seal material
compared to air mode – namely that the fluidizing gas may
sample
Primary air
have oxygen content different from 21 vol-%. The higher
and grid
oxygen level of the gas allows to combust more fuel
Flue gas generating higher combustion power. The switch from air
recirculation Bottom ash mode to directly 28 vol-% oxy mode is presented in Fig. 5.
Fig.2. The pilot-scale CFB test rig of VTT (Tourunen et al.,
2011).

Table 1 The fuel properties used in simulation tests
Components Spanish Petcoke
anthracite
Ultimate analysis (wt%, dry)
C 59 86
H 1.9 657
N 0.95 1.7
O 3.0 1.2
S 1.1 6.0
Proximate analysis (wt%)
Moisture 8.3 6.6
Ash (dry basis) 34 1.4
Fig.3. Step-series in both air and oxy combustion. All mass Volatiles /dry basis) 7.0 11
flows were changed stepwise between 70% and 100%. Heat value (MJ/kg)
LHV (as received) 19.9 31.6
4. SIMULATION RESULTS
The Matlab/Simulink simulation software has been used for
the 1-D dynamic hot loop modelling. The model has been
developed by Foster Wheeler Energia Oy and further
upgraded and validated in co-operation with the
Lappeenranta University of Technology (LUT) and the
University of Oulu. The structure of the model version used
in this study is presented in Fig. 6. Both steady-state and
dynamic simulations can be performed. During simulation
experiments, the collected process input variables – fuel,
limestone, primary/secondary oxidant flows – were supplied
as inputs for the model.
Fig.4. Ramp test series in oxy combustion with different
ramp speed and load levels. The air and oxy combustion mode were compared in this
study via the temperature profile of the furnace. The model
determines the temperature in 20 different points of the
furnace. Fig. 7 and Fig. 8 present the simulated temperatures
for air and oxy combustion, respectively. The oxy
combustion showed definitively slower behaviour due to the
larger heat capacity of the oxidant gas; this result is in good
agreement with the literature.
Fig.5. The main input flows of the process during switch
from air to oxy combustion.
Table 1 shows analyses of the fuels considered in the study.
The design fuel is a mix of Spanish anthracite and petcoke
Fig.7. Response of the furnace temperatures due to load step
(70% / 30% on weight basis) with a lower heat value of 23.4
changes in air mode.
MJ/kg (as-rec.) and ash content of 23.8 % (d.m.). An oxygen
purity of about 97 vol-% was used.

5. CONCLUSION
Flexi-BurnTM CFB technology provides an option to utilize
both air and oxygen combustion in the same boiler. The
operation of such a boiler requires not only the understanding
of the fundamentals of air and oxy combustion, but rather the
differences between those. Experimental studies were
therefore carried out in a pilot-scale CFB plant. Three main
operation mode – load step change, load ramp change and
switch between air and oxy mode – were both tested and
simulated.
A simulation model developed in earlier studies was
successfully validated based on those measurement data. The
Fig.8. Response of the furnace temperatures due to load step
core of the model is the hot-loop (furnace); its behaviour –
changes in oxy mode. the combustion process – is best described by the flue gas O2
content.
The main difference in dynamic behaviour between air and
oxy combustion is well observed in the experimental tests
and also well described by the simulation model; namely, the
effect of the recirculated flue gas (RFG) on the furnace
dynamics via the vertical temperature distribution. Due to the
higher heat capacity of the RFG, the temperature profile has a
slower dynamics.
The current study will be continued in a larger-scale
(30MW ) unit.
th
6. ACKNOWLEDGEMENT
The research leading to these results has received funding
from the European Community’s Seventh Framework
Fig.9. Fuel input during load step changes in oxy mode.
Programme (FP7/2007-2013) under grant agreement n°
239188.
REFERENCES
Alvarez, I., Muñoz, F., Lupion, M., Otero, P., Hotta, A.,
Kuivalainen, R. and Alvarez, J.: CIUDEN CFB boiler
technological development, 2nd Oxyfuel Combustion
Conference, 13-15 September, 2011.
Eriksson, T., Sippu, O., Hotta, A., Fan, Z., Ruiz, J.A.,
Sánchez-Biezma, A., Jubitero, J.M., Ballesteros, J.C.,
Shah, M., Prosser, N., Haley, J. and Giudici, R.:
Development of FLEXI-BURNTM CFB technology
aiming at fully integrated CCS demonstration. PowerGen
Europe, Cologne, Germany, May 26 – 28, 2009.
EU Commission: CO2 Capture and Storage, Demonstration
Fig.10. Flue gas components during step load change in oxy projects (2010)
mode. http://ec.europa.eu/energy/publications/doc/2010_eepr_b
rochure_co2_en.pdf
Tourunen, A., Leino, L., Pikkarainen, T., Nevalainen, H. and
Finally, the simulation result of a step load change in oxy
Kuivalainen, R.: Small pilot scale CFB experiments
combustion in Fig. 9-10 demonstrate the accuracy of the
under air- and oxygen-firing conditions. 2nd IEAGHG
model. The main variable to test the performance of the hot-
International Oxyfuel Combustion Conference,
loop was the flue gas O2 content. The model could
Australia, September 12th-16th 2011.
successfully mimic the real process behaviour in both static
and dynamic sense.
