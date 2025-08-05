# Simulation_of_the_Chemical_Looping_Combu

**Fonte**: Simulation_of_the_Chemical_Looping_Combu.pdf  
**Data de conversão**: 2025-07-30 15:10:10  
**Origem**: base_relevantes

---

Engineering Conferences International
ECI Digital Archives
The 14th International Conference on Fluidization
Refereed Proceedings
– From Fundamentals to Products
2013
Simulation of the Chemical Looping Combustion
Process of Coal with a Synthetic Cu-Based Oxygen
Carriers
Marvin Kramp
Hamburg University of Technology; Institute of Solids Process Engineering and Particle Technology, Germany
Andreas Thon
Hamburg University of Technology; Institute of Solids Process Engineering and Particle Technology, Germany
Ernst-Ulrich Hartge
Hamburg University of Technology; Institute of Solids Process Engineering and Particle Technology, Germany
Stefan Heinrich
Hamburg University of Technology; Institute of Solids Process Engineering and Particle Technology, Germany
Joachim Werther
Hamburg University of Technology; Institute of Solids Process Engineering and Particle Technology, Germany
Follow this and additional works at:http://dc.engconfintl.org/fluidization_xiv
Part of theChemical Engineering Commons
Recommended Citation
Marvin Kramp, Andreas Thon, Ernst-Ulrich Hartge, Stefan Heinrich, and Joachim Werther, "Simulation of the Chemical Looping
Combustion Process of Coal with a Synthetic Cu-Based Oxygen Carriers" in "The 14th International Conference on Fluidization –
From Fundamentals to Products", J.A.M. Kuipers, Eindhoven University of Technology R.F. Mudde, Delft University of Technology
J.R. van Ommen, Delft University of Technology N.G. Deen, Eindhoven University of Technology Eds, ECI Symposium Series,
(2013). http://dc.engconfintl.org/fluidization_xiv/98
This Article is brought to you for free and open access by the Refereed Proceedings at ECI Digital Archives. It has been accepted for inclusion in The
14th International Conference on Fluidization – From Fundamentals to Products by an authorized administrator of ECI Digital Archives. For more
information, please contactfranco@bepress.com.

SIMULATION OF THE CHEMICAL LOOPING COMBUSTION-
PROCESS OF COAL WITH A SYNTHETIC Cu-BASED
OXYGEN CARRIERS
Marvin Kramp, Andreas Thon, Ernst-Ulrich Hartge,
Stefan Heinrich, Joachim Werther*
Hamburg University of Technology; Institute of Solids Process Engineering and
Particle Technology
Denickestr. 15, 21073 Hamburg, Germany
*T: +49 40 42878 3239; F: +49 40 42878 2678; E: werther@tuhh.de
ABSTRACT
A fluidized bed reactor model was implemented that allows the simulation of
multiple heterogeneous and homogeneous reactions. This reactor model is used
for the steady-state flow sheet simulation of the pilot plant for chemical looping
combustion of the Hamburg University of Technology. The pilot plant is equipped
with a two-stage fuel reactor. The simulated experiments were carried out with a
Cu based oxygen carrier and German lignite dust. The developed tool is used in
this study to investigate the behavior of the pilot plant and gives additional
insights into the occurring phenomena. Based on the simulations it is concluded
that the fuel does not mix into the bed of oxygen carrier of the lower stage of the
fuel reactor which leads to large quantities of combustible gases in the off-gas of
the first fuel reactor stage.
INTRODUCTION
The flow sheet simulation of solids processes
is still a challenging task due to the
complicated handling of distributed properties
whereas the flow sheet simulation of fluid
processes is state of the art. SolidSim is a
steady-state flow-sheet software package for
solids processes and has filled the gap in the
past years. Unfortunately there is still a lack
models for several unit operations like fluidized
bed reactors. Hence in the course of this work
a fluidized bed reactor module was developed
and is applied to a complex process, the
chemical looping combustion process of coal.
Chemical looping combustion allows an
inherent separation of the carbon dioxide
produced during the conversion of
carbonaceous fuels. The process is based on
a solid oxygen carrier (OC) that selectively
consumes oxygen in an air reactor and
provides this oxygen to the fuel conversion in
the fuel reactor. A mixing of air nitrogen with
the carbon containing off-gas is thus
prevented.
Recently a chemical looping combustion test plant for solid fuels with a rated
power of 25 kW was erected and commissioned at the Hamburg University of
th
rotcaeR
riA
O -depleted air
2
(CO )
2
CO
2
H O
2
MeO
Solid
Fuel
Me
Char
Air
rotcaeR
leuF
Stage
2
H O
2
Stage
1
Siphon
H O
2
H O 2
nohpiS
sdiloS saG S1
S2
Figure 1: Scheme of the Hamburg
University of Technology CLC
facility.

Technology. Different from most other plants a two-stage bubbling fluidized bed
fuel reactor was integrated into the plant. A scheme of the plant is shown in
Figure 1. The solid fuel is introduced into the lower stage of the fuel reactor and
the oxidized OC coming from the air reactor is added to the upper stage.
Volatiles and unconverted products of the char gasification in the lower stage
have to pass through the upper stage of the fuel reactor and get a second time
into contact with fresh OC particles. Hence the conversion of volatiles and the
products of char gasification should be improved.
In the present investigation a Cu-based OC is used with German brown coal.
First the experimental results are discussed and afterwards the simulation model
is described. Finally the results of the application of the developed simulation tool
are interpreted.
THEORY
Fluid Dynamics in the Fluidized Beds
The fuel reactor fluidized beds are divided into two zones, the bottom zone and
the freeboard. The bottom zone is further divided into the suspension phase and
the solids-free bubble phase. The fluid dynamics of the bottom zone are
calculated according to the Werther & Wein model (1). The freeboard above the
bed is treated as a single suspension phase. To calculate the elutriation from the
reactors an elutriation constant approach is used (2). Assuming a relative velocity
of the particles equal to the difference between the superficial gas velocity and
the terminal velocity of the particles (3), the solids volume concentration above
transport disengaging height is calculated. The particle size distribution is fully
considered. An exponential decay of the solids volume concentration in the
freeboard is assumed (4).
The air reactor is operated at high gas velocities that lead to low solids volume
concentrations. The measured height-dependent pressure profile is used for the
calculation of the height-dependent solids volume concentration in the air reactor.
A single solid-gas suspension phase is assumed.
Reactions
The heterogeneous reactions in the dense beds of the fuel reactors are assumed
to take place solely in the suspension phase since the bubble phase is assumed
to be free of solids. In the freeboards of the fuel reactors and in the whole air
reactor heterogeneous reactions take place on the entire cross-section.
Homogeneous gas phase reactions are allowed to take place in all gas carrying
phases. The reactions lead to changes in the volume flow. For the dense beds of
the fuel reactors the convective transport of gas between the suspension and
bubble phase and the dilution of reactant gases by product gases is accounted
for.
Fuel Devolatilization
The composition of the volatiles released from the solid fuel is approximated from
ultimate analyses of fuel and char according to a model by Jensen (5). The
formation of nitrous oxides and the sulfur content of the fuel are neglected.
Char Gasification
Char can be gasified both by CO and H O. The net reactions are:
2 2

(1)
(2)
( ) ( )
The factor in Eq. (1) describes the ratio between the formation of CO and CO.
2
Typically this value is close to unity (6) and taken as 1.2 here. Hence steam
gasificationβ leads predominantly to CO formation. The kinetic model of steam
gasification is taken from Matsui et al. (6):
(3)
( )
The kinetic m odel o f c h a r g a s if ic at ion b y CO
2
i s ta ke n f ro m M atsui et al. (7):
(4)
( )
X denotes the char c onv er si o n a n d ar e th e m o la r concentrations of species i.
Unfortunately the kinetic constants derived by Matsui et al. cannot be used since
the coal used in this investigation is f ine brown coal dust with a sauter diameter
of 24.3 µm while the measurements of Matsui et al. were carried out with char
derived from subbituminous coal of particle sizes in the range of 297-710 µm for
steam gasification and 44-710 µm for carbon dioxide gasification.
Char Combustion
Char transported to the air reactor combusts with the present gaseous oxygen.
Char combustion is assumed to lead solely to the formation of carbon dioxide.
The kinetics are taken from Field et al. (8).
OC Reactions
Shrinking core kinetics are applied to all OC reactions.
(5)
is the time until full conversion and def in(e d a s):
(6)
is a stoichiometric factor. den ot es t h e g r a in size and is the reaction order
towards the gaseous reactant. This shrinking core approach was used to
d escribe the reactions betwe en the OC and combustible ga ses in the fuel reactor
as well as the oxidation of OC in the air reactor. The reactivity of this particular
OC was not investigated beforehand and hence the kinetic constants are fitted by
comparison of model and experimental results.
Cyclone Model
The cyclone separation and pressure drop is calculated according to the model
by Muschelknautz et al. (9). In order to consider reactions in the cyclone solids
and gases are considered well mixed, hence an ideal CSTR model is applied.

Siphon Modeling
The steam used for fluidization of the lower siphon is distributed between the air
reactor and the fuel reactor. According to previous investigations at the cold
model of the experimental plant (10) it can be estimated that 80 % of the siphon
gas is sent to the air reactor and 20 % to the fuel reactor. For reaction modeling
the lower siphon S2 was approximated with well-mixed behavior and a solids
inventory corresponding to the measured pressure drops. The steam fluidizing
the upper siphon S1 does not influence the dry off-gas compositions and is thus
neglected.
Simulation Environment
The simulations have been carried out with SolidSim 1.2 (11), a steady-state
flowsheet simulation environment for solids processes.
EXPERIMENTAL
In the following sections the test plant is briefly introduced and experimental
results are shown. A more detailed discussion of the experiments is found
elsewhere (12).
Plant Design
A sketch of the test plant is shown in Figure 1. It consists of a riser as air reactor
and a two-stage bubbling fluidized bed as fuel reactor. The air reactor is 0.1 m in
diameter and has a height of 8 m. The fuel reactor has an inner diameter of
0.25 m and each stage is 2 m high. Each stage of the fuel reactor is equipped
with an overflow pipe with a height of 0.6 m above the gas distributor and an
inner diameter of 0.07 m. Hence, the bed height of each stage is kept constant.
Between fuel and air reactor siphons are located that separate the respective
atmospheres in the reactors from each other. Each siphon is connected to a
steam generator. Coal is pneumatically conveyed by a flow of CO into the lower
2
stage of the fuel reactor. A detailed description is given in (13).
Evaluation
The experiments are evaluated with the help of two key performance indicators
(14). The carbon capture ratio indicates the fraction of CO produced in the
2
air reactor instead of the fuel reactor. Char transported from the fuel reactor to
the air reactor combusts to a gre a t extent and the carbon dioxide produced is lost
to the atmosphere. Hence the carbon capture ratio should be as close to unity as
possible.
(7)
[ ̇ ̇ ̇ ] [ ̇ ]
[ ̇ ̇ ̇ ] [ ̇ ] [ ̇ ]
Another performance indicator is the oxygen demand of the gaseous products
leaving the fuel reactor (FR). It describes to what extent the products of char
gasification and fuel devolatilization are oxidized in the fuel reactor by the OC
p a r ticles.

(8)
[ ̇ ̇ ̇ ]
Experiments
The experiments were carried out with an OC composed of 11.5 % of CuO as
active ingredient impregnated on Al O particles (Sasol Germany, Puralox
2 3
NWa155). This CuO based OC releases only negligible quantities of gaseous
oxygen in the fuel reactor. A rapid solid-state reaction between the CuO and
Al O leads to the formation of copper aluminate (15) which hinders a
2 3
decomposition reaction of CuO to Cu O. The reactivity of the OC towards
2
combustible gases is not reduced by this solid-state reaction (15). Hence char is
mainly converted by gasification and not through combustion. The fuel was a
finely ground German Rhenish brown coal, provided by RWE AG. Details on fuel
and oxygen carrier can be found elsewhere (12).
The siphons and the fuel reactor were fluidized with varying amounts of steam.
The circulation rate between both reactors was determined indirectly from the
oxidation degree of OC samples taken from both siphons (13). The off-gas was
measured by continuous NDIR and heat conductivity analyzers and calibrated
each day. Additionally gas samples were taken and analyzed by GC
measurements. Gas sampling was done after the second stage approximately
1 m above the top end of the freeboard in the off-gas pipe. After the first FR
stage gas was sampled through a port situated at the top end of the reactor but
on the same axis as fuel injection. Gas was withdrawn at the reactor wall since
no probe was used.
RESULTS AND DISCUSSION
Results of CLC Tests
An overview on the experimental conditions and results of two exemplary
experiments are summarized in Table 1. In the experiments high carbon capture
ratios (>96 %) and low oxygen demands (< 2.5 %) could be achieved. Another
important result is that large quantities of combustible gases were measured at
the top end of the first fuel reactor stage and almost fully converted in the second
fuel reactor stage. The methane concentration after the first stage is low
compared to H and CO. In the experiment with the higher coal feed rate the H
2 2
concentration exceeds the CO concentration significantly while in the other
experiment both concentrations are similar.
Table 1: Experimental Results. Gas
composition N -free from GC analysis.
2

Parameter Run 1 Run 2
coal feed [kg/h] 5.0 3.9
CO feed [kg/h] 3.1 3.3
2
feed S2[kg/h] 3.6 3.6
feed FR [kg/h] 1.7 1.3
T[°C] 900 900
Δp [mbar] 99 108
AR
Δp [mbar] 42 43
PC
Δp [mbar] 45 46
FR
[kg/s] 0.136 0.145
u [m/s] 5.0 5.0
AR
ḞR s tage 2
cCoHnc [evnotl.r-a%ti odnrys] 0.53 0.07
4
CO [vol.-% dry] 97.8 99.4
2
CO [vol.-% dry] 0.77 0.21
H [vol.-% dry] 0.86 0.28
2
FR stage 1
cCoHnc [evnotl.r-a%ti odnrys] 3.72 1.79
4
CO [vol.-% dry] 37.1 60.97
2
CO [vol.-% dry] 24.8 18.84
H [vol.-% dry] 33.3 18.39
2
Air Reactor
coOnc [evnotl.r-a%ti odnrys] 5.15 9.12
2
CO [vol.-% dry] 0.27 0.14
2
98.6% 99.0%
1.5% 0.34%
Process Simulations
Since the kinetic constants for the gasification reactions and the reactions
between OC and combustible gases are unknown the kinetic constants had to be
fitted. The experimental run with the highest coal feed rate is used to derive the
appropriate kinetic rate constants. In order to reduce the calculation time during
the parameter fitting the fuel reactor was simulated independently from the air
reactor and fed with a flow of oxidized OC with steady-state particle size
distribution (fines free). It was possible to achieve a good agreement between the
measured and simulated concentrations after the second fuel reactor stage. It
was however not possible to simulate the measured high concentrations of CO
and H after the first stage (see Table 2 sim A). Hence an assessment was
2
started with the aim to investigate the occurring phenomena.
The continuous concentration measurements were subject to fluctuations but the
GC measurement generally confirmed the measured concentrations. The gas
sampling after the second FR stage should be more or less free of horizontal
concentration profiles due to the change of pipe diameter above the second
stage. After the first FR stage gas was sampled close to the wall on the same
axis as fuel injection. Hence it cannot be guaranteed that the cross-sectional
average concentrations are equal to the measured concentrations at the wall.
Previous studies with tracer gas injection into the upper dilute zone of a riser at
the Hamburg University of Technology have shown that local differences in
concentrations can be preserved over large distances (16). Hence it could be

possible that the sampled gas after the first fuel reactor stage is influenced by
local effects.
The comparatively low methane concentrations are likely to be attributed to the
steam reforming of methane. The following reaction is considered in the
simulations in order to account for steam reforming:
(9)
This reaction is catalyzed by r ed u ce d O C a s we ll a s
the reactor walls (Ni) (17,18) and could also explain
the comparatively high H concentrations.
2
The used model assumes a well-mixed behavior of
the solids in each stage of the fuel reactor. In case of
good mixing of fuel and OC the products of
gasification CO and H should be readily converted.
2
Thus the high measured concentrations are possibly
attributed to an isolated flow of fuel and products of
devolatilization and gasification inside a plume rising
through the lower stage. Cold model investigations
were carried out and indeed a visible bubble flow
above the coal injection port could be observed at
the reactor wall. Additional simulations and
calibration runs have been carried out with partial or
full coal injection into the freeboard of the second
stage. A calculation flow scheme for this case is
shown in Figure 2. A comparison of gas
compositions for different coal bypass situations is
shown in Figure 3 and Table 2 (sim B/C). The
simulations confirm that it is possible to raise the
amount of CO and H in the fuel reactor off-gas
2
significantly by assuming the coal to bypass the bed
of OC in the lower stage. If all coal bypasses the
dense bed the simulated H concentration reaches
2
21.4 % compared to 33.3 % which were measured.
In the experiment with high coal feed rate the H
2
concentration was higher than the CO concentration.
This ratio was different at lower coal feed rates (see
Table 1).
Figure 2: Flow scheme of
fuel reactor model. Dashed
lines indicate gas and solid
lines solids flow.
.beerf
deb
.lf
.beerf
deb
.lf
off-gas
& solids
oxidized
OC
coal &
reduced
CO
OC 2
steam

100%
80%
60%
CH4
40%
H2
20% CO
CO2
0%
Figure 3: Simulated dry gas compositions after first FR stage for different bypass
scenarios.
It was also tested whether an increased amount of fluidization steam could
elevate the H content after the first stage. The steam feed was doubled (sim D
2
Table 2) but has only a minor influence on the H /CO ratio. The CO content was
2
lowered by 1.5 % and the H concentration was increased by 0.2 %. To achieve a
2
greater effect the ratio of steam gasification to gasification by CO needs to be
2
altered which was not done here. Since the OC particles present in the bottom
region of the freeboard have a significant influence on the H and CO content
2
another study was carried out without coal bypass but also without consideration
of H and CO consumption reactions in the first stage. This measure leads to a
2
further great increase in H and CO concentrations after the first stage but it also
2
leads to greater H and CO concentrations above the second stage (3.6 % and
2
1.7 %, respectively). Greater amounts of char are gasified there and since
virtually no OC particles are present in the top freeboard region the products of
gasification cannot be converted anymore. From the experiments it is known that
in fact large amounts of char are elutriated in the fuel reactor (corresponding to
7 wt.-% of the fed char). The measured concentrations were nonetheless close to
zero which could either mean that the lost char is very unreactive or that in
practice OC particles are present in the upper region of the freeboard. Attrition
leads to a continuous production of fine particles that can be elutriated. The OC
loss was determined for the considered experiments to 24.6 g/h from bag house
filter samples. Assuming that 50 % of this loss originates from the fuel reactor
another simulation has been set up to consider this flow of fine particles. This
variation showed that the loss of fines due to attrition is too low to have a
noticeable effect on the gas conversion (identical results to sim E which was the
basis). Another possible explanation could be that particles ejected from
collapsing bubbles at the surface of the dense bed reach higher into the
freeboard than expected. Lowering the decay constant to 50 % of its original
value leads to a noticeable decrease of the CO and H concentrations after the
2
second stage but also the concentrations after the first stage are influenced (sim
F, Table 2).

Table 2: Comparison of results from experiment 1 and simulations. (A: reference case,
B: 50% bypass, C:100% bypass, D: double steam feed, E:no OC reactions in stage 1,
F: lowered solids decay in freeboard)
exp 1 sim A sim B sim C sim D sim E sim F
FR stage 2
cCoHnc [evnotl.r-a%ti odnrys] 0.5 0.3 0.6 0.4 0.3 0.1 0.1
4
CO [vol.-% dry] 97.8 98.6 97.0 96.8 97.2 94.6 97.6
2
CO [vol.-% dry] 0.8 0.4 0.9 1.0 0.9 1.7 0.9
H [vol.-% dry] 0.9 0.7 1.5 1.8 1.6 3.6 1.4
2
FR stage 1
cCoHnc [evnotl.r-a%ti odnrys] 3.7 2.4 3.2 2.8 2.5 3.4 3.8
4
CO [vol.-% dry] 37.2 80.2 62.4 53.5 55.1 12.5 12.5
2
CO [vol.-% dry] 24.8 8.5 17.0 22.2 20.7 42.4 42.7
H [vol.-% dry] 33.3 8.9 17.4 21.5 21.7 41.7 41.0
2
98.6% 98.9% 98.9% 98.7% 98.8% 98.8% 99.1%
1.5% 1.8% 3.8% 3.3% 2.8% 4.5% 2.2%
CONCLUSIO N S
A fluidized bed reactor model was implemented that allows the simulation of
multiple heterogeneous and homogeneous reactions. Hence a tool is derived that
allows the simulation of a full process with a complex reaction scheme. This tool
uses SolidSim as simulation framework which facilitated this investigation. The
extraction of simulation results is convenient and the full support of distributed
properties allowed an efficient implementation of the elutriation rate model for the
prediction of the solids circulation rate between the reactors. Furthermore the
implemented model for the solid separation in the cyclone could be used.
The developed tool can be used to investigate the behavior of a plant and gives
additional insights into the occurring phenomena. In this study it could be shown
that the lower stage of the fuel reactor operates in a different mode than
expected. The mixing of fuel and OC in the lower stage is poor due to complex
fluid dynamics. A different gas sampling strategy will also be necessary to get
reliable information on the performance of the first fuel reactor stage. It is planned
to investigate the kinetics of the occurring reactions individually in detail in order
to reduce the necessary parameter fitting.
ACKNOWLEDGEMENTS
The present work was financially supported by the German Federal Ministry of
Economics and Technology (FKZ 0327844B / CLOCK) with additional funding
from BASF SE, EnBW Kraftwerke AG, E.ON Energie AG, Hitachi-Power Europe
GmbH, RWE Power AG and Vattenfall Europe Generation AG. The responsibility
for the content of this report lies with the authors.
SYMBOLS AND ABBREVIATIONS
carbon capture ratio, - (def. by kinetic constants for gasification
Eq. (7)) modeling, m³/s mol or m³/mol
oxygen demand of fuel reactor OC circulation rate, kg/s
off-gas, - (def. by Eq. (8))
molar flow of compound i
̇
concentration of compound i,
mol/m³
̇
pressure drop, mbar

AR superficial gas velocity, m/s FR fuel reactor
X char conversion OC oxygen carrier
ratio of CO / CO production in PC post combustor (2nd fuel reactor
2
steam gasification stage)
AR air reactor
REFERENCES
1. Werther J., Wein J. (1994), AIChE Symp. Ser. 301, 90, 31–44.
2. Colakyan M., Levenspiel O. (1984), Powder Technol. 38, 223–232.
3. Werther J., Hartge E.-U. (2004), Powder Technol. 148, 113–122.
4. Kunii D., Levenspiel O. (1991), Fluidization Engineering, Butterworth-Heinemann.
Boston.
5. Jensen A. D. (1996), Nitrogen Chemistry in Fluidized Bed Combustion of Coal.
Ph.D. thesis. Technical University of Denmark. Lyngby, Denmark.
6. Matsui I., Kunii D., Furusawa T. (1985), J. Chem. Eng. Jpn. 18, 2, 105–113.
7. Matsui I., Kunii D., Furusawa T. (1987), Ind. Eng. Chem. Res. 26, 1, 91–95.
8. Field M. A., Gill D. W., Morgan B. B., Hawksley P. G. W. (1967), The British Coal
Utilisation Research Association. Leatherhead.
9. Muschelknautz E., Greif V., Trefz M. (2006), in VDI-Wärmeatlas. 10th ed., VDI
Gesellschaft Verfahrenstechnik und Ingenieurwesen V. D.I. (ed.), Springer-Verlag,
Berlin, Heidelberg.
10. Thon A., Kramp M., Hartge E.-U., Heinrich S., Werther J. (2012), in Proceedings of
the 21st International Conference on Fluidized Bed Combustion,
EnzoAlbanoEditore.
11. SolidSim Engineering GmbH (2010), SolidSim. http://www.solidsim.com/.
12. Thon A., Kramp M., Hartge E.-U., Heinrich S., Werther J. (2013), in Fluidization
XIV - From Fundamentals to Products, Engineering Conferences International,
New York.
13. Thon A., Kramp M., Hartge E.-U., Heinrich S., Werther J. (2012), in Proceedings of
the 2nd International Conference on Chemical Looping, Technische Universität
Darmstadt (ed.), Darmstadt.
14. Mendiara T., Abad A., Diego L. F. de, Garcia-Labiano F., Gayán P., Adánez J.
(2012), in Proceedings of the 21st International Conference on Fluidized Bed
Combustion, EnzoAlbanoEditore.
15. Diego L. F. de, Gayán P., García-Labiano F., Celaya J. de, Abad A., Adánez J.
(2005), Energ. Fuel. 19, 1850–1856.
16. Kruse M. (1994), Ph.D. Thesis. Hamburg University of Technology. Hamburg.
17. Adanez J., Abad A., Garcia-Labiano F., Gayan P., Diego L. F. de (2012), Prog.
Energy Combust. Sci. 38, 2, 215–282.
18. Xu J., Froment G. F. (1989), AIChE J. 35, 1, 88–96.
