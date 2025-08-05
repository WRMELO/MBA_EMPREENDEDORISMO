# CHALLENGES_WITH_THE_COUPLING_OF_FLUIDIZE

**Fonte**: CHALLENGES_WITH_THE_COUPLING_OF_FLUIDIZE.pdf  
**Data de conversão**: 2025-07-30 15:10:27  
**Origem**: base_relevantes

---

Refereed Proceedings
The 13th International Conference on
Fluidization - New Paradigm in Fluidization
Engineering
Engineering Conferences International Year 2010
CHALLENGES WITH THE
COUPLING OF FLUIDIZED BEDS
FOR CHEMICAL LOOPING
COMBUSTION
Marvin Kramp∗ Andreas Thon† Ernst-Ulrich Hartge‡
Stefan Heinrich∗∗ Joachim Werther††
∗HamburgUniversityofTechnology
†HamburgUniversityofTechnology
‡HamburgUniversityofTechnology,hartge@tuhh.de
∗∗HamburgUniversityofTechnology
††HamburgUniversityofTechnology
ThispaperispostedatECIDigitalArchives.
http://dc.engconfintl.org/fluidization xiii/69

Kramp et al.: CHALLENGES WITH THE COUPLING OF FLUIDIZED BEDS FOR CHEMICAL LOOPI
CHALLENGES WITH THE COUPLING OF FLUIDIZED BEDS FOR
CHEMICAL LOOPING COMBUSTION
Marvin Kramp, Andreas Thon, Ernst-Ulrich Hartge, Stefan Heinrich, Joachim
Werther
Institute of Solids Process Engineering and Particle Technology, Hamburg
University of Technology
Denickestrasse 15
21073 Hamburg, Germany
ABSTRACT
In the present work the system of interconnected fluidized bed reactors of a
Chemical Looping Combustion (CLC) process is simulated in pilot plant scale and
100 MW scale. Attrition models, derived from small scale laboratory experiments,
th
are employed to predict the behavior of a large scale CLC process in terms of
attrition and oxygen carrier (OC) losses. Realistic circulation mass flows of OC are
calculated and the sources of the losses are further investigated. Different
arrangements of cyclones are evaluated for their potential to improve the solids
recovery. For example the introduction of a second-stage cyclone separation for the
air reactor reduces the OC losses significantly.
INTRODUCTION
Chemical Looping Combustion is an interesting variant for the inherent separation of
anthropogenic carbon dioxide inside a power generation process that has recently
attracted much attention by numerous research groups. The process consists of two
interconnected fluidized bed reactors. In between these two reactors are solids
circulated which transport chemically bound oxygen taken up from the air inside the
air reactor to the so called fuel reactor. The oxygen carrier particles provide the
fossil fuel (i.e. natural gas or coal) with oxygen and will themselves be reduced.
Reduced oxygen carrier particles are then cycled back towards the air reactor for re-
oxidation. CLC has the advantage that the carbon dioxide of the off-gas will not be
diluted by nitrogen. After condensation of water, almost pure carbon dioxide can be
derived and transported to its designated storage location.
Like other processes, the feasibility of this process is dependent on the process
costs, which will be greatly influenced by the oxygen carriers involved. Thus it is of
great importance to reduce the loss of oxygen carrier particles. This means, the
particles have to be attrition resistant and the losses through the gas-solids
separation devices like cyclones have to be minimized. Oxygen carriers can both be
of natural origin (ores etc.) or synthetically manufactured. Synthetic OC particles are
usually composed of an inert porous carrier material and a reactive metal oxide.
Published by ECI Digital Archives, 2010 1

The 13th International Conference on Fluidization - New Paradigm in Fluidization Engineering, Art. 69 [2010]
Their use can be advantageous in respect of both the attrition and reaction rate due
to the increased mechanical stability and the increased porosity.
The aim of this investigation is to study the process from the particle technology
point of view. Simulations have been carried out to study the circulation mass flow
between the interconnected fluidized bed reactors as well as the respective particle
size distributions and OC losses through the gas-solids separation devices. The
influence of attrition of the OC particles on the process performance is investigated
and possible improvements of the solids recovery are studied. Simulations have
been carried out in two scales: pilot scale and an upscale to a 100 MW Chemical
th
Looping Combustion process.
THEORY
Process Designs
Chemical looping combustion was studied in different
types of unit configurations (1-3) but systems of
interconnected fluidized beds dominate the literature
due to the implied good gas / solids contact. In 2001
Lyngfelt et al. (3) made a first sketch of a process
similar to the one shown in Figure 1. The air reactor is
realized as a circulating fluidized bed (CFB) whereas
the fuel reactor is a bubbling fluidized bed (BFB). The
setup sketched in Figure 1 is chosen as the reference
setup of the simulations.
Figure 1: Initial simulated
Fluid Dynamics in the Fluidized Bed Reactors CLC process setup,
The fluidized bed reactors are for the calculations according to Lyngfelt et al. (3)
divided into two zones, the bottom zone and the upper
dilute zone. The bottom zone is described by a semi-
empirical approach, dividing the bottom zone into two phases, the suspension phase
and the bubble phase which is assumed to be solids free. The fluid dynamics of the
bottom zone are calculated according to the Werther & Wein model (4). The initial
bubble size is calculated by the equation proposed by Davidson & Schüler (5). As
soon as the boundary of the bed is reached the upper dilute zone begins. This is
accompanied with a change in the description. The upper dilute zone is treated as a
single phase, where the solids are suspended in the gas flow. To calculate the
elutriation from the reactors above the transport disengaging height (TDH), an
elutriation constant approach is used. Out of numerous correlations two are chosen
for the simulations. The correlation of Colakyan & Levenspiel (6) was validated at
superficial gas velocities in the range of 0.9 – 3.7 m/s for particles of the size range
300 - 1000 µm. The second correlation from Tasirin & Geldart (7) was validated at
superficial gas velocities in the range of 0.2 - 0.8 m/s for particles of the size range
68 - 124 µm. Assuming a relative velocity of the particles equal to the difference of
the superficial gas velocity and the terminal velocity of the particles (8), the solids
volume concentration c above transport disengaging height (TDH) can be
v
calculated. Between the c above TDH and the c at the top of the bed, an
v v
exponential decay of the solids volume concentration is assumed and calculated
according to Kunii & Levenspiel (9).
http://dc.engconfintl.org/fluidization_xiii/69 2

Kramp et al.: CHALLENGES WITH THE COUPLING OF FLUIDIZED BEDS FOR CHEMICAL LOOPI
In case a CFB is to be described, the models stated above are extrapolated to the
present gas velocities and the bottom zone is described as a bubbling fluidized bed
at high gas velocities.
Reactions in the Fluidized Beds
Inside the fluidized bed reactors, the heterogeneous reaction between the oxygen
carrier particles and the respective gases have to be accounted for. Several
investigations (e.g. (10-13) ) have shown a good agreement between shrinking core
models (SCM) (9) and measurements of OC conversion by various gaseous
reactants.
t  r
1(1X )1/3,  m (1)

s bkCn
The SCM can both be applied to a description of the entire particle as well as a
description of reactive grains on an inert structure. In case a grain description is
favored the grain radius is a fitting parameter. In the bottom zone, the reaction is
assumed to exclusively take place in the suspension phase. The bubble phase is
regarded as solids-free. In dependency of the gaseous reactant, the reactions inside
a reactor can lead to changes in the volume flow. The model assumes the excess
gas to rise entirely in the bubble phase. In chemical looping combustion the
reactions can significantly influence the fluid dynamics of the fluidized beds. For
instance full conversion of methane will increase the volume flow by 200 % while the
stoichiometric full oxidation of the OC-particles will result in a volume flow decrease
of 21 %. Due to the change of volume flow the convective transport of gas between
the suspension and bubble phase and the dilution of reactant gases by product
gases can not be neglected. In this model the change in volume flow is accounted
for according to the approach suggested by Sitzmann et al. (14). Diffusive transport
between the suspension and bubble phase is calculated from the correlation of Sit &
Grace (15).
Population Balance Modeling
The focus of this investigation is to simulate the flows as well as the particle size
distributions inside this system of interconnected fluidized bed reactors. It is
assumed that particles do not break and the dominating attrition mechanism is
abrasion, which is a reasonable assumption for catalyst attrition under normal
conditions (16). The simulation of the population balances relies on the approach
suggested by Werther & Hartge (8). Employing this approach the fate of particles of
different size classes is individually followed. Mother particles undergoing abrasion
will slightly shrink in size while the produced fines are assumed to be small in size
and added to the first size interval. Three sources of attrition are regarded. First,
attrition can be caused by the solids movement induced by the bubbles in a fluidized
bed. Secondly, the attrition due to gas jets is regarded and the third considered
attrition source is the solids recovery in the cyclones. The mass of produced fines
inside a bubbling fluidized bed reactor is calculated by the equations given by
Merrick & Highley (17) and Reppenhagen & Werther (18). The attrition occurring in
the cyclone is calculated according to Reppenhagen & Werther (18). For the attrition
Published by ECI Digital Archives, 2010 3

The 13th International Conference on Fluidization - New Paradigm in Fluidization Engineering, Art. 69 [2010]
calculation one material specific constant for each attrition mechanism is needed (C ,
b
C, C ). These constants have to be calculated from experimental results.
j c
Simulation
For the investigation of the CLC process, the flow sheet simulation environment
SolidSim (19) has been selected. SolidSim is a commercial software package for the
simulation of solids processes and was originally developed at the Institute of Solids
Process Engineering and Particle Technology of the Hamburg University of
Technology (20). SolidSim employs a sequential modular approach for the
simulation of the steady-state behavior of solids processes. Unit operations are
calculated in series and loops are solved by fixed-point iteration of the loop unit
operations.
Results and discussion
Definition of the Test Case
For the simulations the copper based OC Cu10Al-I was selected because of the rich
information available in references (21) and (22). Of the fresh feed particles the
cumulative distribution is 0.3 % < 45 µm, 1.4 % < 90 µm, 31.4 % < 125 µm, 91.1 %
< 180 µm and 100 % < 212 µm. The simulation input parameters are shown in Table
1. The chosen pressure drops equal solid inventories of 47,800 kg OC for the large
scale and 17.1 kg for the pilot scale, respectively. The considered reactions are:
O 2Cu 2CuO (2)
2
CH 4CuO4CuCO 2H O (3)
4 2 2
According to equation 2 and 3 the stoichiometric coefficient b is 2 for the oxidation
and 4 for the reduction of the OC. Information on reaction kinetics was taken from
literature (21, 22).
Parameter Pilot Scale 100 MW scale
th
height fuel reactor: 2 m 12 m
height air reactor: 10 m 17 m
diameter fuel reactor: 0.3 m 10 m
diameter air reactor 0.1 m 4.2 m
∆p air reactor: 7000 Pa 7000 Pa
∆p fuel reactor 2700 Pa 2700 Pa
∆p air reactor cyclone 1200 Pa 1200 Pa
∆p fuel reactor cyclone (if applicable) 900 Pa 900 Pa
gas inlet velocity of cyclones approx. 20 m/s approx. 20 m/s
CH feed 0.0009 kg/s 1.993 kg/s
4
air feed 0.0165 kg/s 36 kg/s
gas distributors porous plate bubble cap
fuel reactor temperature 850°C 850°C
air reactor temperature 900°C 900°C
inlet gas pressure 101325 Pa 101325 Pa
C 3.5 x 10-8 1/m 3.5 x 10-8 1/m
b
C 4.5 x 10-3 s2/m³ 4.5 x 10-3 s2/m³
c
C not applicable 2.2 x 10-5 s2/m³
j
Table 1: Simulation input parameters of the test case
http://dc.engconfintl.org/fluidization_xiii/69 4

Simulation results
According to the simulation the 100 MW scale process reaches at steady-state a
th
circulation mass flow of OC of 627 kg/s while a circulation flow of 0.386 kg/s for the
pilot scale is reached. These values lead to specific circulation rates based on the
empty cross-section of the air-reactor (G ) of 45.8 kg/m² for the air reactor of the
s
large scale process and 49.6 kg/m²s for the pilot scale. These values are
significantly higher compared to regular CFB combustors for coal which are usually
expected to operate at roughly 15 kg/m²s (23). Higher G values exceeding 100
s
kg/m²s are known from the operation of Fluid Catalytic Cracking processes which
involve fine catalysts (23). Considering these values, the simulated circulation flow
rates appear reasonable. The methane conversion reaches 99.4 % in the small
scale but only 84.7 % for the large scale. In order to increase the gas conversion of
the large scale fuel reactor the hold-up was increased to a pressure drop of 10000
Pa and the gas velocity was decreased from 0.37 m/s to 0.25 m/s. The redesigned
fuel reactor has a diameter of 13 m and reaches a gas conversion of 93.1 %. This
value is still too low for a technical process and therefore the design of the fuel
reactor has to be further optimized by decreasing the bubble sizes which seem to
transport too much fuel gas, by-passing the OC. These and other measures to cope
with scale-up issues of fluidized bed reactors have for instance been discussed by
Werther (24). Nonetheless this improved reactor was employed for all further
investigations. The oxygen conversion in the air reactor reaches 82.5 % for the
small scale and 78.6 % for the large scale which equals oxygen mole fractions of
5.1 % and 6.2 % in the oxygen depleted off-gas.
The role of attrition
Simulations have been carried out both with and
8
without regard of particle attrition. Attrition leads to
fine particle generation while the mother particles
6
slightly shrink in size. It is difficult to retain the
produced fine particles in the system hence the 4
mass loss of OC is increased. The losses have to
be made up by a feed of fresh particles which 2
directly influences the operating costs. In Figure 2
0
the simulation results are shown in terms of OC
Pilot Scale 100 MWth
mass loss related to the amount of thermal energy
released. It is observed, that attrition will in fact
increase the OC mass losses but also that the pilot
scale plant has much lower OC losses compared to
the large scale plant. This is mainly due to the lower separation efficiency of large
scale cyclones. The separation efficiency of the pilot plant air reactor cyclone
reaches almost 100 % while the large scale cyclone reaches 99.976 % with attrition
being regarded. For the large scale process without attrition 94 % of the OC losses
originate from the overflow of the air reactor cyclone (80 % with attrition regarded).
On the other hand for the pilot scale the losses are almost completely originating
from elutriation from the fuel reactor.
]hWM/gk[
ssol
CO
Kramp et al.: CHALLENGES WITH THE COUPLING OF FLUIDIZED BEDS FOR CHEMICAL LOOPI
with attrition
no attrition
Figure 2: Influence of attrition
on OC mass loss
Published by ECI Digital Archives, 2010 5

Variation of the solids recovery
The simulation permits now to investigate how the OC loss in the large scale plant
can be reduced. The following changes were investigated:
 Introduction of a second-stage air reactor cyclone
 Additional fuel reactor cyclone with a return leg to the fuel reactor entry
 Changes 1 + 2 combined
Figure 3 shows the effect of these changes on the OC loss per MWh of released
thermal energy. Improved solids recovery at the air reactor gas exit significantly
reduces the OC losses of a large scale CLC process while improvements in the fuel
8
6
4
2
0
100 MWth
Figure 4: Influences of variations in
the solids recovery system on the
OC mass loss related to the
produced thermal energy reactor solids recovery do not exert a great
influence. Finally the particle size distribution of
the circulating OC flow in dependency of the attrition and the different cyclone
configurations are investigated. As Figure 4 shows the particle size distribution of
the circulating OC flow of the 100 MW scale preserves its general shape and is
th
shifted towards larger or smaller particles when the effect of attrition is considered
and when the solids recovery rate is increased.
CONCLUSION
In the present work a system of interconnected fluidized bed reactors was simulated
in two different scales. Based on laboratory attrition investigations the behavior of a
large scale Chemical Looping Combustion process was predicted. Realistic
circulation mass flows of oxygen carrier particles were obtained. With the help of
these simulations the individual sources of OC losses can be evaluated. Possibilities
to decrease the OC losses have been investigated. For example the introduction of
a second-stage cyclone separation for the air reactor reduces the OC losses
significantly.
]hWM/gk[
ssol
CO
1
0.8
0.6
0.4
0.2
0
standard case
50 100 150 200
with FR cyclone particle diameter [µm]
AR 2 stages of cyclones
with FR cyclone + AR 2
stages of cyclones
Figure 3: Cumulative mass distributions for the
100 MW scale and different simulations
th
]-[
ssam
evitalumuc
The 13th International Conference on Fluidization - New Paradigm in Fluidization Engineering, Art. 69 [2010]
without attrition
standard case
with FR cyclone
AR 2 stages of cyclones
with FR cyclone + AR 2 stages of cyclones
http://dc.engconfintl.org/fluidization_xiii/69 6

Kramp et al.: CHALLENGES WITH THE COUPLING OF FLUIDIZED BEDS FOR CHEMICAL LOOPI
ACKNOWLEDGEMENT
The present work is part of a joint research project of the Institute of Combustion
and Power Plant Technology of the University of Stuttgart, the Institute of Energy
Systems of the Hamburg University of Technology and the Institute of Solids
Process Engineering and Particle Technology of the Hamburg University of
Technology. This project received financial support of the German Federal Ministry
of Economics and Technology (FKZ 0327844B / CLOCK) with additional funding
from BASF SE, EnBW Kraftwerke AG, E.ON Energie AG, Hitachi-Power Europe
GmbH, RWE Power AG and Vattenfall Europe Generation AG. The responsibility for
the content of this report lies with the authors.
NOTATION
b stoichiometric factor [-] k chemical reaction rate
constant [mol1-n m3n-2 s-1]
C local reactant concentration n reaction order [-]
[mol/m³]
C constant for bubble induced r radius of the spherical grains
b
attrition [1/m] (or particle radius) [m]
C constant for cyclone  time necessary for full
c
induced attrition [s²/m³] particle conversion[s]
C constant for gas jet induced  molar density of the solid
j m
attrition [s²/m³] reactant [mol/m³]
REFERENCES
(1) Kolbitsch, P., Bolhar-Nordenkampf, J., Pröll, T., and Hofbauer, H. In
Circulating Fluidized Bed Technology IX, Werther, J., Nowak, W., Wirth, K.-E., and
Hartge, E.-U., editors, 795–801 (TuTech Innovation GmbH, Hamburg, 2008).
(2) Noorman, S., van Sint Annaland, M., and Kuipers, H. Ind. Eng. Chem. Res.
46, 4212–4220 (2007).
(3) Lyngfelt, A., Leckner, B., and Mattisson, T. Chem. Eng. Sci. 56, 3101–3113
(2001).
(4) Werther, J. and Wein, J. AIChE Symp. Ser. No. 301 90, 31–44 (1994).
(5) Davidson, J. and Schüler, B. Trans. Inst. Chem. Eng. 38, 335–342 (1960).
(6) Colakyan, M. and Levenspiel, O. Powder Technology 38, 223–232 (1984).
(7) Tasirin, S. and Geldart, D. Powder Technology 95, 240–247 (1998).
(8) Werther, J. and Hartge, E.-U. Powder Technology 148, 113–122 (2004).
(9) Kunii, D. and Levenspiel, O. Fluidization Engineering. Butterworth-
Heinemann, Boston, (1991).
(10) Garcia-Labiano, F., de Diego, L., Adanez, J., Abad, A., and Gayan, P.
Industrial & Engineering Chemistry Research 43, 8168–8177 (2004).
(11) Abad, A., Garcia-Labiano, F., de Diego, L., Gayan, P., and Adanez, J.
Energy & Fuels 21, 1843–1853 (2007).
(12) Ryu, H.-J., Bae, D.-H., Han, K.-H., Lee, S.-Y., Jin, G.-T., and Choi, J.-H.
Korean Journal of Chemical Engineering 18(6), 831–837 (2001).
Published by ECI Digital Archives, 2010 7

The 13th International Conference on Fluidization - New Paradigm in Fluidization Engineering, Art. 69 [2010]
(13) Richardson, J., Turk, B. M., and Twigg, M. Applied Catalysis A: General 148 ,
97–112 (1996).
(14) Sitzmann, W., Werther, J., Böck, W., and Emig, G. Ger. Chem. Eng. 8, 301–
307 (1985).
(15) Sit, S. and Grace, J. . Chem. Eng. Sci. 36, 327–335 (1981).
(16) Werther, J. and Hartge, E.-U. In Handbook of Fluidization and Fluid-Particle
Systems, Yang, W., editor, 113–128. Marcel Dekker, New York, (2003).
(17) Merrick, D. and Highley, J. AIChE Symp. Ser. 70(137), 367–378 (1974).
(18) Werther, J. and Reppenhagen, J. In Handbook of Fluidization and Fluid-
Particle Systems, Yang, W.-C., editor, 201–238. Marcel Dekker, New York, (2003).
(19) SolidSim http://www.solidsim.com/. (2009).
(20) Hartge, E.-U., Pogodda, M., Reimers, C., Schwier, D., Gruhn, G., and
Werther, J. KONA 24, 146–158 (2006).
(21) Abad, A., Adanez, J., Garcia-Labiano, F., de Diego, L., Gayan, P., and
Celaya, J. Chemical Engineering Science 62, 533–549 (2007).
(22) Garcia-Labiano, F., Adanez, J., de Diego, L., Gayan, P., and Abad, A.
Energy & Fuels 20, 26–33 (2006).
(23) Zhu, J. In Circulating Fluidized Bed Technology VIII, Cen, K., editor, 41–55.
International Academic Publishers / World Publishing Corporation, Beijing, (2005).
(24) Werther, J. Chem. Eng. Sci. 47. 9-11, 2457–2462 (1992).
http://dc.engconfintl.org/fluidization_xiii/69 8
