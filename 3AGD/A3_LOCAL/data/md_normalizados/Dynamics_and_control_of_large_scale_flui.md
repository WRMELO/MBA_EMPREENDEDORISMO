# Dynamics_and_control_of_large_scale_flui

**Fonte**: Dynamics_and_control_of_large_scale_flui.pdf  
**Data de conversão**: 2025-07-30 15:05:44  
**Origem**: base_relevantes

---

AppliedThermalEngineering219(2023)119591
Contents lists available at ScienceDirect
Applied Thermal Engineering
journal homepage: www.elsevier.com/locate/apthermeng
Research Paper
Dynamics and control of large-scale fluidized bed plants for renewable heat
and power generation
´ ˜´ `
a,* b a a
Guillermo Martinez Castilla , Ruben M. Montanes , David Pallares , Filip Johnsson
aChalmers University of Technology, Division of Energy Technology, Ho ¨ rsalsva ¨ gen 7B, Gothenburg 412 96, Sweden
bSINTEF Energy Research, Sem Saelandsvei 11, Trondheim NO-7465, Norway
A R T I C L E I N F O A B S T R A C T
Keywords: As the share of variable renewable electricity increases, thermal power plants will have to adapt their operational
Plant flexibility protocols in order to remain economically competitive while also providing grid-balancing services required to
Dynamic modeling deal with the inherent fluctuations of variable renewable electricity. This work presents a dynamic model of
Simulation
fluidized bed combustion plants for combined heat and power production. The novelty of the work lays in that (i)
Thermal power plant
it provides an analysis of the transient performance of biomass-based fluidized bed combustion plants for
Fluidized bed combustion
District heating combined heat and power production, (ii) the dynamic model includes a description of both the gas and water-
steam sides and (iii) the model is validated against operational data acquired from a commercial-scale plant. The
validated model is here applied to analyze the inherent dynamics of the investigated plant and to evaluate the
performance of the plant when operated under different control and operational strategies, using a relative gain
analysis and a variable ramping rate test.
The results of the simulations reveal that the inherent dynamics of the process have stabilization times in the
range of 5–25 min for all the step changes investigated, with variables connected to district heating production
being the slowest. In contrast, variables connected to the live steam are the fastest, with stabilization times of
magnitude similar to those of the in-furnace variables (i.e., around 10 min). Thus, it is concluded that the proper
description of the dynamics in fluidized bed combustion plants for combined heat and power production requires
modeling of both the gas and water sides (which is rare in previous literature). Regarding the assessment of
control strategies, the boiler-following and hybrid control (combined fixed live steam and sliding pressure)
strategies are found to be able to provide load changes as fast as −5%-unit/s, albeit while causing operational
issues such as large pressure overshoots. The relative gain analysis outcomes show that these control structures
do not have a steady-state gain on the power produced, and therefore it is the dynamic effect of the steam
throttling that triggers the rapid power response. This study also includes the assessment of a turbine bypass
strategy, the results of which show that it enables fast load-changing capabilities at constant combustion load, as
well as decoupling power and heat production at the expense of thermodynamic losses.
variation management strategies [3]. In most current energy systems,
1. Introduction thermal power plants compensate for the fluctuating power generation
from VRE sources, providing flexibility. Therefore, it is expected that
Variable renewable electricity (VRE) sources are predicted to in- with increasing shares of VRE, thermal power plants will have to meet
crease their share in the worldwide electricity generation from 25 % in higher flexibility requirements [4], i.e., ensuring faster load changes,
2016 to 33 % in 2025 and by 2050 they are expected to play a crucial increasing their load range and/or increasing their product portfolio [5].
role in the electricity production capacities of most European countries At the same time, these plants will need to be climate-neutral. Biomass-
[1,2]. Such a rapid evolution of non-dispatchable electricity generation fired thermal power plants could contribute to a power system with net-
is expected to pose serious challenges to the power grid stability owing zero greenhouse gas emissions – or even negative emissions, if applied
to the inherent variability of VRE sources. In addition, the value of VRE together with carbon capture and storage (CCS) [6] and the use of sus-
will decrease when increasing its share unless flexibility in the demand tainable biomass sources. In the Nordic countries, thermal power plants,
(including storage) is employed, i.e., through the application of with the exception of nuclear installations, operate as combined heat
* Corresponding author.
E-mail address: castilla@chalmers.se (G. Martinez Castilla).
https://doi.org/10.1016/j.applthermaleng.2022.119591
Received 4 February 2022; Received in revised form 19 October 2022; Accepted 27 October 2022
Availableonline1November2022
1359-4311/©2022TheAuthor(s).PublishedbyElsevierLtd.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Nomenclature hyd hydraulic
is isentropic
Greek L liquid
α heat transfer coefficient L,M logarithmic mean
β Baumann factor m matrix element, measured
η efficiency mech mechanical
θ valve oppening n element
λ relative gain coefficient, thermal conductivity nom nominal
ρ density o-c for other control loops closed
τ stabilization time, time constant o-o for other control loops open
ψ enhancement factor p constant pressure
s simulated, steam
Latin
t turbine
A area
tp two-phase
AP absolute percentage error
v vapor, valve
Bo boiling number
vap vaporization
C controller, pre-exponential factor, valve flow coefficient
w wall
c heat capacity
0 initial, reference
Co Convection number ∞ final
d diameter
dp pressure drop Abbreviations
E total energy BF boiler following
F flow rate BFB bubbling fluidized bed
G static gain matrix, transfer function, mass flow density CCS carbon capture and storage
h specific enthalpy CFB circulating fluidized bed
HV heating value CHP combined heat and power
I instrument CP centrifugal pump
K flow area coefficient, friction loss coefficient, gain CV controlled variable
L level DH district heating
LF length factor DMC dynamic matrix control
m mass flow through a pipe, total mass DRGA dynamic relative gain analysis
n number ECO economizer
Nu Nusselt number HPT high pressure turbine
P power, pressure FB fluidized bed
Pr Prandtl number FBC fluidized bed combustion
p pressure FF feed-forward
Q heat flow FG flue gas
R resistance FP floating pressure
s thickness FWH feed water heater
T temperature ICPD integrated control plant design
t time IPT intermediate pressure turbine
x variable, steam quality LPT low pressure turbine
y variable MPC model predictive control
MV manipulated variable
Subscripts
OFWH open feed water heater
a arrangement
PI proportional integral
c controller, condensate
RGA relative gain analysis
comb combustion
SP set-point
crit critical point
SH superheater
el electrical
TF turbine following
f fuel, friction
VRE variable renewable electricity
fw feed water
VRR variable ramping rate
g gas
and power (CHP) plants, i.e. producing hot water for district heating flexibility levels. As identified in a previous publication [8], current
(DH) or steam for industrial facilities, as well as generating electricity. research towards improving the flexibility of biomass-based CHP plants
Typically, due to the heating demand in biomass-rich regions, the pro- mainly involves: (i) the implementation of energy storages within the
duction of DH is the main economic incentive for these plants. Conse- plant [9,10]; (ii) the investigation of primary frequency response ca-
quently, the production level has traditionally been planned to cover the pabilities [11,12]; (iii) the decoupling of power and heat production
aggregated DH demand in conjunction with other heat-only boilers or [13]; (iv) increasing the fuel flexibility [14]; and (v) retrofitting the
CHP plants in the local DH system [7]. With an increased share of VRE, furnace for the coproduction of biogas [15].
given its low operating costs, it seems likely that CHP plants will need to Control solutions for current thermal power plants [16] are often
be more flexible in order to maintain competitiveness, providing faster based on traditional industrial practices and are not optimized for flexi-
and larger load changes and increasing their operational and product bility. Moreover, process optimization of CHP plants has not placed an
2

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
emphasis on how flexibility requirements influence the operation and manipulation of one input affected several outputs. Their work was
profitability of the plant. Thus, with new requirements regarding flexi- subsequently expanded [33], whereby a simple mass storage capacity
bility, there is a need to understand the possibilities and limitations for model was developed to carry out an integrated control process design
transient operation of CHP plants. Different supervisory control strategies (ICPD) and optimize the dynamic performance of the steam side of a
(here defined as the control layer responsible for regulating the produc- coal-fired CFB unit. The results showed that an ICPD with boiler-
tion of heat and power in the hour-minute timeframe [17,18]) for thermal following control was capable of providing efficient load tracking,
plants have been proposed and investigated through process simulations, although the authors concluded that more detailed mechanistic
as reported in the literature [19,20]. However, the optimization strategy modeling would be required to derive more comprehensive results.
for biomass-based CHP plants presents two new challenges: the specific Beiron et al. [8] developed and validated a dynamic process model in
combustion behavior of fluidized beds (with slower response time Modelica and used it to investigate the transient characteristics of a
coupled to the larger fuel particles used and the thermal inertia of the bed waste-fired FBC-CHP steam cycle. Even though the model did not
material) and the fact of having two products (heat and power) in the include a representation of the gas side dynamics, the results of that
business planning. While the first aspect is given by the technology study showed that the process reacted more slowly to changes in the
choice, the second includes the strategic perspective on the product and boiler load than to changes in the DH system. Similarly focusing on the
customers portfolio (heat-driven or power-driven operation, maximized dynamics of waste-fired plants, Zimmerman et al. [34] compared
revenue operation). It is known that the chosen strategy has an impact on different control strategies, concluding that feed-forward (FF) model
plant efficiency, as well as on the ability to provide fast load changes predictive control (MPC) is the best system for disturbance rejection, i.
while maintaining process safety. A crucial question is whether the live e., to deal with unplanned changes. Gao et al. [30] have presented a
steam pressure should be fixed (such as in turbine-following and boiler- dynamic 1D furnace model combined with a boiler model (including the
following modes) or not fixed (sliding pressure, floating pressure and drum and the tubes), and validated it against a 300-MW condensing
hybrid control modes). Although these strategies have been published unit. The overall model was thereafter used to investigate control stra-
and implemented in industry for some decades, different nomenclatures, tegies for quick load changes based on the fuel accumulation within the
classification systems and definitions are given for these strategies in the furnace, such that it achieved a load ramping rate of 1.7–2.5 %/min. The
literature. Furthermore, as biomass-fired plants are expected to expand model in [30] was linearized and used for MPC by Zhang et al. [35], who
their product portfolio, allowing the decoupling of heat and power pro- successfully tested a dynamic matrix control (DMC) strategy for
duction and possibly also incorporating the co-production of biofuels, different ramping rates. Kim et al. [36] developed a dynamic model that
new control strategies will be required. accounted for both the in-furnace (1.5D, detailed in [37]) and water-
Besides control, operational strategies such as steam extractions and steam sides, which after validation with steady-state data from a 500-
turbine bypass are commonly applied to increase the flexibility of MW unit, was used to quantify the transient response of the steam
thermal power plants [21,22], especially when they are deployed with a temperature following changes in the feedwater and fuel flows. Stefa-
thermal energy storage in the form of steam accumulation [10]. Other nitsis et al. [38] presented a 1D dynamic model of CFB furnaces that was
alternatives to secure flexibility are also available, such as making the built in APROS and validated with data from a 1-MW pilot unit and
extracted steam to instead be condensed with the DH water, which can which was thereafter used to investigate the transient performance of
buffer the variations caused by the steam extraction. the cited plant after a thermal energy storage unit in the form of hot bulk
Dynamic power plant modeling and simulation can be used to solids was implemented within the plant; they concluded that the sta-
evaluate the transient capabilities of existing and future thermal power bilization time for load changes was reduced when adding storage (and
plants. An extensive up-to-date review of thermal power plant dynamic thereby decreasing the solids inventory within the furnace). Most of the
simulations has been published by Alobaid et al. [23], in which they literature cited above has focused on CFB units. However, with respect
highlight the lack of modeling studies of biomass-fired CHP plants that to BFB plants, it is worth mentioning the work of Zlatkovij et al. [39], in
take into account the dynamics of the combustion chamber. Avaginos which a linearized dynamic model of a biomass-fired BFB boiler that
et al. [24] have recently presented a dedicated review of the process included a 0-dimensional description of the gas side was used to test and
modeling of solid-fuel plants, in which once again the lack of publica- compare MPC strategies for disturbance rejection, concluding that FF-
tions focusing on biomass-fired CHP units was noted. Literature on the MPC was the preferred option (as in [34]).
dynamics of CHP plants is scarce (the above-referred [10,12], together In summary, regarding the literature on flexibility studies, studies of
with [25]) and focuses on the water-steam side of coal or waste-fired FBC units have mostly been concerned with coal-fired condensing
units. In this regard, it is important to point out the fact that the dy- plants, while those focused on CHP plants have mostly investigated gas-
namics of a given combustion plant are characterized by the combustion fired units [40,41]. Thus, there is a scarcity of publications regarding the
technology used, and therefore, the literature survey presented below flexibility of FBC-CHP plants with biomass as the fuel, the importance of
reviews studies focusing on the dynamics of FBC plants (for which a vast which has recently been reviewed by Atsonios et al. [42]. Note that the
majority are coal-fired power plants, but CHP biomass-fired plants are general differences between biomass-fired plants and coal-fired ones are
common in bioenergy-intensive regions). expected to yield fundamentally different plant dynamics (since biomass
Due to their strong mixing and heat transfer capabilities, fluidized plants are smaller, operating in CHP mode, biomass has a higher volatile
bed combustors (FBCs) are the preferred option for burning low-grade and hydrogen content than coal). Furthermore, works involving FBC
solid fuels (such as biomass) at large scales [26]. As a consequence, units generally lack a model of the gas side capable of describing the
FBCs represent a substantial percentage of the solid-fuel furnaces in dynamics of the combustion process in parallel with the dynamics of the
regions with strong availability of biomass and well-established CHP Rankine cycle. This hinders examination of the impacts on process dy-
plants [27,28]. A common feature of the FBC technology is the large namics of variables that are crucial for FBC operation such as the cir-
amount of solids inventory in the furnace, which yields a high thermal culation and inventory of solids, emissions, or fuel reactivity. The
inertia, strong intercoupling among process parameters and non-linear authors of the present work have recently presented a validated mech-
transients [29,30,31] all of which are crucial aspects to be addressed anistic dynamic model for the in-furnace side of industrial-sized FBC
when attempting to increase the flexibility characteristics of FBC plants. furnaces [29], which was used to investigate the dynamics of CFB and
When it comes to evaluating the flexibilization of FBC plants, BFB combustion processes. The model was used to elucidate the stabi-
Hultgren et al. [32] employed a process model of a coal-fired CFB boiler lization times of the temperature and heat extraction in different regions
developed in APROS to perform a control design analysis using static of the furnaces. In [31], the in-furnace model was used to study the
and dynamic relative gain analyses (RGA and DRGA, respectively), in sensitivity of the computed in-furnace stabilization times to mechanisms
which they identified substantial control loop interactions, i.e., the such as fluid dynamics, heat transfer and fuel combustion. However, the
3

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Fig. 1. Schematic process diagram of the reference plant. Steam and water lines are represented by red and blue lines, respectively. Regulatory and supervisory
control structures of the reference plant are included in orange, with signals represented in dashed lines. F: mass flow. T: Temperature. Q: heat load. P: electrical
power and pressure. SP: Set point. SH: Superheater. DSH: desuperheater. ECO: economizer HPT: high pressure turbine. IPT: intermediate pressure turbine. LPT: low
pressure turbine. DHC: District heating condenser. FWH: feedwater heater. CP: centrifugal pump. (For interpretation of the references to colour in this figure legend,
the reader is referred to the web version of this article.)
investigations in [29,31] focus on the in-furnace side and model studies
considering the interplay between this and the water/steam side remain Table 1
as a main gap in literature. Design data of the reference plant.
The aim of this work is to evaluate the transient operation of
Boiler capacity 100 MWth
biomass-based FBC-CHP plants in terms of the potential to operate in a Live steam mass flow 28.9 kg/s
future electricity system in which volatile wholesale prices for electricity Live steam pressure 67 bar
can be expected such that flexibility of plant operation will be valued Live steam temperature 505 ◦C
Electrical power 20.2 MW
higher than it is at present. To identify the limits of flexibilization, the
District heating load (DHC) 56.8 MW
present study focuses on operational and control strategies that can Power-to-heat ratio 0.36 –
maximize the plant ramp rate and extend the operational boundaries in Drum pressure 74.3 bar
the hour-minute timeframe, i.e., expand the product output area. This Steam turbine exhaust pressure 1.2 bar
paper includes a comprehensive description of the main supervisory Feedwater temperature 270 ◦C
control strategies for load changes that can be applied to FBC-CHP
plants. The in-furnace side model presented and validated previously
from 30 to 400 MWth, see for instance [43]). The unit has also been used
in [29,31] is here connected to a model of the water-steam side. The for the calibration and validation of the in-furnace side model [29]. The
resulting merged model is validated here with industrial plant data, and unit is normally operated with wood chips with moisture content of 50 %–
then used to: (i) perform a relative gain analysis (RGA), to evaluate the 55 % (for detailed fuel composition, see [29]). A simplified process dia-
interactions between the inputs and outputs of the plant so as to assess
gram with the main process variables and components is shown in Fig. 1.
the controllability of the process; (ii) characterize the inherent (uncon- The plant consists of the CFB furnace, a convective flue gas path,
trolled) dynamic behavior of the plant; and (iii) test how different
comprising three economizer tube bundles (ECO), two superheaters (SH1
control and operational strategies could provide fast load changes. and SH3), and a three-section air preheater (not included in Fig. 1), an in-
The novelty of the work lays in that (i) it analyses the transient
furnace superheater (SH2), a steam drum, a steam turbine with two in-
performance of biomass-based FBC-CHP plants, (ii) the dynamic model termediate extractions (each turbine section named HPT, IPT and LPT), a
includes a description of both the gas and water-steam sides, and (iii) the steam condenser (DHC) in which DH water at ~90 ⁰C (the main product of
model is validated against operational data acquired from a commercial- the plant) is produced, and one closed and one open feedwater heater
scale plant.
(FWH and OFWH, respectively). Table 1 lists the main design data for the
reference plant operated at full load.
2. The reference plant
2.1. Flue gas side
The present work uses a 100-MWth biomass-fired CFB boiler located in
Karlstad (Sweden) as the reference plant, as it has a size and plant layout
The fuel is combusted primarily in the CFB furnace, where the solids
that is representative of biomass-fired FBC-CHP plants (typically ranging
carried by the gas up to the furnace top and exit ducts are separated from
4

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Fig. 2. Summary of the methodology followed in the present work.
the gas in two parallel cyclones and returned to the furnace via the re- OFWH is controlled by manipulating the control valve placed in the
turn legs, where the fresh fuel is fed. The furnace has a height of 20 m. steam extraction. The feedwater pump and control valve located
Air is fed into the furnace partly as primary air, which fluidizes the downstream of the OFWH are used to control the level of the drum
bottom bed, and partly as secondary air at a height of 5 m. The immersed through a three-point control system. Regarding the supervisory control
superheater tube bundle SH2 is located at a height of 11 m. Most of the layer, a conventional boiler-following strategy (see Section 3.2.2 for
furnace walls consist of membrane walls that evaporate the feedwater. more details) is implemented, as shown in Fig. 1. Note that due to the
The hot flue gases leaving the cyclones flow through the convection absence of a condenser operating with cooling water, the output of the
path, where the superheaters, economizers and air preheaters are plant follows a constant power-to-heat ratio. The controller of the air
transversally located, before progressing towards the gas cleaning sys- mass flow is connected to the fuel flow controller using an FF signal from
tem and flue gas condenser (not included in Fig. 1). the oxygen concentration exiting the furnace. The air primary/second-
ary split depends on the fuel flow, i.e., boiler load. Finally, the mass flow
2.2. Water-steam side of feedwater sprayed in the DSHs is used to control the steam temper-
ature after each superheater section.
The water-steam cycle is a conventional subcritical, single-pressure
system that is typical of CHP plants in Sweden. The subcooled feed- 3. Methods
water is first preheated in the economizer ECO before being fed into the
drum, from which the water is naturally circulated through the evapo- Fig. 2 presents the overall methodology employed in this work. First,
rator, i.e., the downcomer and riser tubes located in the furnace walls. a mechanistic dynamic model of an FBC-CHP plant is built, which is
The evaporating mixture is separated in the drum prior to the steam presented in Section 4. The model is calibrated and validated (Section
superheating. Desuperheaters (DSHs) spraying subcooled feedwater are 4.4) using steady-state and transient operation data from an industrial
located between the superheating stages for temperature control. The unit. Model simulations are then used to carry out the following three
live steam is thereafter expanded in the steam turbine, producing elec- analyses:
tricity and DH water. As part of the heat integration of the plant and
bearing in mind that DH water is the main product in the business and (1) Steady-state interactions between the main inputs and outputs of
production planning, the DH water that flows through the turbine the plant are investigated through an RGA (Section 5.1), which is
˚
condenser DHC has previously been preheated up to 70C in the flue gas used to assess the steady-state performance of the control struc-
condenser (not included in Fig. 1). Intermediate-pressure steam at 6 bar tures presented in Section 3.1.
and 4 bar (at full load) are extracted for the OFWH and FWH, respec- (2) The inherent dynamics of the process are explored through sim-
tively, with the former being used as a deaerator to remove oxygen and ulations of open-loop tests (Section 5.2.1).
other non-condensable species. The feedwater pump CP3 recirculates (3) The control structures and operational strategies presented in
the water from the deaerator back to the boiler. Section 3 are tested dynamically, so as to study the capabilities of
the controlled process to provide fast load changes in different
2.3. Control future energy markets (Sections 5.2.2 and 5.2.3).
Conventional power plant regulatory control loops [44] in the water-
steam side to maintain the stability and controllability of the plant, as 3.1. Control structures for load changes in CHP plants
shown in Fig. 1. The levels of the DHC and FWH are controlled by
manipulating the condensate pump control valves. For inventory con- As stated in a previous publication [16], boiler control involves the
sistency, the OFWH level is not controlled continuously but is main- regulation of the outlet conditions of steam flow, temperature, and
tained within certain safety limits by the addition/removal of make-up pressure to attain their desired values. Supervisory control structures of
water to/from the loop (not included in Fig. 1). The pressure of the boiler-turbine units are in charge of controlling the plant outputs in a
5

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Fig. 3. Fixed pressure operation strategies for load changes. Blue lines represent the turbine-following strategy, while the red lines indicate the boiler-following
strategy. SP, Set-point; FG, flue gas. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
minute-hour timescale, and they handle disturbances connected to fuel structure design methodology applied to heat-to-power cycles, to which
heating value variations and load changes. Two main control strategies the reader is referred for a complete description of the general meth-
exist: one based on fixed live steam pressure, and the other one allowing odology followed when designing some of the control structures
the live steam pressure to change with load (in a controlled or uncon- described herein.
trolled manner). Jonshagen and Genrup [19] performed a thermody-
namic assessment of the steady-state implications of fixing or not fixing 3.1.1. Fixed pressure operation
the steam pressure in CHP units and concluded, similar to the findings of Turbine following: In this operation mode (indicated by blue lines
others [45], that a hybrid strategy is the most beneficial approach from in Fig. 3) the turbine follows the response of the boiler. Thus, the master
the perspective of efficiency. Within each of these strategies, several controller uses the combustion load (fuel/air flows) to control the power
control structures can be used, and the studies in the literature are often plant outputs, and the steam valve is used to keep the steam pressure at
discrepant in terms of the terminology and classification of these the desired set-point. When, for instance, increasing the combustion
structures, which are applied to industrial facilities but lack application load, the steam pressure will increase and, in order to keep a constant
to CHP plants. This section describes the control structures for load live steam pressure, the steam control valve will gradually open. The
changes that are investigated and tested in this work (see Section 5.2). major drawback of this strategy is that it is characterized by a large time
The work of Zoticӑ et al. [20] describes an up-to-date plantwide control constant connected to the combustion load and, therefore, it is not
Fig. 4. Variable pressure control strategies for load changes. Blue lines represent the floating pressure strategy, while the red lines indicate the sliding pressure and
hybrid control modes. SP, Set-point; FG, flue gas. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of
this article.)
6

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Table 2
CV-MV relationship of the control strategies included in this work.
Control structure Controlled variable (CV) Manipulated
variable (MV)
Turbine following Generated power/DH Combustion load
Live steam pressure Live steam valve
Boiler following Generated power/DH Live steam valve
Live steam pressure Combustion load
Floating pressure Generated power/DH Combustion load
Sliding pressure/ Generated power/DH Live steam valve
Hybrid control Live steam pressure Combustion load
(controlled but not fixed)
Table 3
Controlled and manipulated variables defined for the relative gain analysis.
Fig. 5. Variable pressure curves for the pure sliding pressure [46] and hybrid
CVs MVs
control [47,48] modes.
Live steam temperature, Tsteam Combustion load, Qcomb
suitable for fast load changes.
Live steam pressure, Psteam Live steam valve opening, Valvesteam
Power produced, Pel DSH spray water flow, FDSH
Boiler following: The rationale for boiler-following control (red
lines in Fig. 3) is the opposite to that for turbine-following control: the
master load controller now manipulates the live steam control valve and provided in Section 4.2 (all tuned parameters of the controllers are listed
the combustion load is used to control the steam pressure. Following a in Table 9).
load change, the boiler utilizes the energy stored in the drum to provide
a faster response than that seen with turbine-following, although the
3.2. Relative gain analysis
pressure control is less stable and efficient [16].
RGA is a well-established methodology [50] for evaluating the
3.1.2. Variable pressure operation
controllability of a process with multiple inputs and outputs such as an
Floating pressure: In this mode (blue lines in Fig. 4), the live steam
FBC-CHP plant, e.g.,a CFB combustor [32]. In a system with m manip-
pressure is not controlled but instead results from the energy balance in
ulated variables (MVs) and n controlled variables (CVs), the RGA is
the boiler as the master controller manipulates the combustion load. The
based on calculating the static gain matrix G through Eq. (1), computing
main advantages of this strategy are the reduction in the amount of
the relative gain coefficients λ of a certain variable pairing. These co-
power required by the feedwater pump at partial loads and the avoid-
efficients are a measure of the open-loop gain of a pairing when all
ance of live steam throttling. However, not controlling the pressure may
introduce issues related to steam pressure gradients in the turbine
control loops are open (gO-O) compared to the gain when all other con-
blades. In addition, the mean temperature of the heat supply is reduced
trol loops are closed (gO-C) [see Eq. (2)]. The results of such a comparison
are commonly used to select variable pairings that minimize the in-
at partial loads because evaporation occurs at lower temperatures,
teractions with/from other loops. Thus, the optimal value of λ for a good
which has a negative effect on the total efficiency of the plant [19].
control pairing is 1, while small positive values indicate poor control-
Sliding pressure: This mode (illustrated by red lines in Fig. 4) was
lability, values much greater than 1 identify variable pairs that would
first suggested by Klefenz [46] as a way to solve some of the operational
require very high controller gains, which are typically to be avoided, and
problems that arise at floating pressure mode for coal-fired power plants
negative values yield instabilities due to the sign change in the gain.
(i.e.,plants of larger size than the biomass-fired plant analyzed here). In
Lastly, it must be mentioned that RGA requires a square system, i.e.,m
this control structure, the pressure is controlled but not fixed; instead, its
= n, although alternatives are available for non-square systems The
set-point follows a pre-defined curve that varies with turbine load.
control structure (i.e., combination of pairings) with largest amount of
Under this mode, it is common to use the mass flow as a measurement of
good pairings (close to 1) in the RGA matrix is considered the one that
the power [20,46] (see Fig. 4).
minimizes the degree of loop interactions.
Hybrid control: Sliding pressure control can be purely sliding or
hybrid in form, depending on the pressure curve applied. Fig. 5 shows a λ 11 ⋯ λ 1n
pressure curve that combines the use of sliding pressure control at lower RGA=G×G−1= ⋯ ⋯ ⋯ (1)
⎡ ⎤
loads and the boiler-following strategy at higher loads. Hybrid control λ m1 ⋯ λ mn
operation was developed as a strategy to avoid the issues connected with ⎣ ⎦
g
fixed pressure operation (i.e., losses related to live steam throttling) and λ mn = g O−O (2)
with floating operation (i.e., slow response), and it has been studied over O−C
the past decades [47,48] in coal-fired plants. For simplicity, only the The CVs and MVs in the current setup of the chosen reference plant
hybrid type of sliding control is included in the present study, with the (Fig. 1) are listed in Table3. The electrical power produced by the steam
switch between constant and variable pressure being set to occur at 75 % turbine is strictly linked to the load of DH produced, since there is no
load. A detailed optimization study based on active constraint regions turbine bypass. Therefore, the plant is assumed to operate at a constant
[49] would be needed to determine the optimum switching point. Note power-to-heat ratio. Thus, the three CVs available for control are the live
that the pressure curves shown in Fig. 5 differ from those typically found steam temperature and pressure and the power output. Note that the live
in combined cycle power plants, where the slow response of the steam steam temperature can be controlled between each of the superheater
cycle is not a problem due to the rapid dynamics of the gas turbine, stages, and each of these would represent an independent CV, although
which yields variable pressure operation of the steam turbine at higher only one has been taken into account for the sake of simplicity. Having
loads and constant pressure operation at lower loads. three CVs, the three MVs chosen are the combustion load, live steam
A summary of the relationships between manipulated variables valve, and DSH spray water flow. The combustion load can be split into
(MVs) and controlled variables (CVs) of each strategy is shown in several MVs, although it is here assumed that the fuel and air flows are
Table 2, while the implementation of each strategy in the model is always manipulated together, i.e., changed simultaneously. To compute
7

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Table 4 Table 7
Disturbances and their magnitudes thereof simulated in the open-loop tests. Relative magnitudes of each of the cases simulated in the variable ramping rate
analysis.
Input variable step-changed Step-change magnitude
Combustion load, Qcomb ±20 % Very slow Slow Fast Very fast
Fuel heating value, HVf ±20 % Scenario I −0.005 %-unit/ −0.05 %-unit −0.5 %-unit −5 %-unit
DH water flow, FDH ±20 % s /s /s /s
DH water inlet temperature, TDH,in ±20 % Scenario II −0.001 %-unit −0.01 %-unit −0.1 %-unit −1 %-unit
/s /s /s /s
Table 5
Process variables tracked during the open-loop tests.
Main process variable, abbreviation, [unit]
Power produced, Pel, [MW]
DH load, QDH, [MW]
DH water outlet temperature, TDH,out [◦C]
Live steam mass flow, Fsteam [kg/s]
Live steam pressure, Psteam [bar]
In-furnace total heat to the waterwalls, Qwall [MW]
Table 6
Fig. 6. Turbine bypass scheme. Note that the bypassed steam is a fraction of the
Definition of scenarios and cases included in the variable
live steam and can be chosen freely.
ramping rate analysis.
Scenario Description operational issues arise when running at minimum loads, such as the
I 100 % to 50 % load change temporary appearance of too-low steam flow in certain sections of the
II 50 % to 40 % load change turbine. Four different ramping speeds are investigated in the present
work for each scenario. The combinations of these results in eight cases
the matrix G, changes in the MVs of −10 % were simulated when the with different load change rates (in %-unit/s) that are shown in Table 7.
plant was running at 100 % load. The gain of the three CVs was then To quantify the responses to each control strategy for each of the
computed from the variable responses after stabilization. Since the simulated cases, the rise time of the generated power is computed,
present study focuses on the supervisory control layer, the regulatory defined as the time that it takes for the output power to go through the
control loops are excluded from the analysis, i.e.,they are assumed to 10 %–90 % response window [53].
remain the same as in the current plant setup.
3.3.3. Turbine bypass
3.3. Dynamic analysis In order to investigate the potentials of other operational strategies
to provide fast load changes, the dynamic performance of a turbine
3.3.1. Inherent process dynamics – Open-loop tests bypass is evaluated. Since the effect of steam extractions on power
Open-loop tests are simulated to obtain the inherent transient per- output is maximized for higher pressures [54], the steam bypass from
formance of the process after a certain disturbance/input change occurs the high-pressure line, i.e., prior to the steam turbine, is studied. The
in the absence of supervisory control loops, i.e., only the regulatory bypassed steam is condensed in the DHC to producing DH water (see
control loops are activated. Individual step changes in the set-points of Fig. 6). Note that a valve is added to regulate the steam pressure down to
the main process inputs and disturbances are introduced in the model. the DHC pressure.
To ensure that the system is perturbed sufficiently to distinguish de- The performance of the bypass is assessed for the following
viations between test cases, the step-change magnitude is ±20 % and is situations:
introduced when the process is running steadily at 80 % load. To eval-
uate the effect of the boiler load on the inherent process dynamics, the – The bypass valve is opened (as a 1-s ramp) to allow 3, 5 and 7 kg/s of
analysis is also conducted when the process runs at 70 % load. Note that, steam to pass when the plant is running steadily at 50 % load; and
as pointed out in [20], the steam pressure is often considered to be su- – The bypass valve is closed (as a 1-s ramp) when the plant is running
pervisory control and, therefore, it is not controlled here. The inputs that steadily at 70 % load and has an initial bypass flow of 3, 5 and 7 kg/s.
are changed are listed in Table 4, while the variables used to charac-
terize the dynamic performance of the process are listed in Table 5. In 4. Dynamic modeling
this work, the open-loop performance of the process is assessed in terms
of the total stabilization time, i.e., the time that it takes for a certain The reference plant described in Section 2 is modeled with a dynamic
process variable to remain within an error band of ±10 % of the total FBC-CHP plant model developed in Dymola [55], which uses the Mod-
change in steady-state values [Eq. (3)]. elica language [56]. The time resolution of the model is defined by
t s =τ⌋ y0→y∞∓0.1(y0−y∞) (3) variable optimized time step values in the order of 100 s. The model
equations are solved using an explicit Runge-Kutta (ESDIRK) method
which is especially suitable for initializing stiff non-linear flow models.
3.3.2. Controlled process dynamics - variable ramping rate analysis
The plant model is the result of integrating a dynamic model of the in-
To assess the capabilities of the controlled plant to provide load
furnace side of the FB boiler previously developed and validated by
changes at different ramp speeds, a variable ramping rate analysis is
the authors [29] with a dynamic process model of the water/steam side
performed. Two load change scenarios are considered (see Table 6): I)
(similar as those in [8,57], i.e., built using the Modelon Thermal-
100 % to 50 % and II)50 % to 40 % load changes. Scenario I is based on
PowerLibrary [58]). Fig. 7 shows the input/output scheme of the inte-
studies (see, for example, [51]) that have proposed that thermal power
grated model. The in-furnace and the water/steam side models are
plants will be required to provide not only faster but larger load changes
connected through the following:
when running at full load. Scenario II represents the more moderate load
changes required when the plant is run at partial load (for most of its
operational time). Furthermore, it is well known [52] that some
8

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Fig. 7. Input/output scheme for the integrated dynamic model of the FBC-CHP plants.
In the present section, the main characteristics and formulations of
the model are discussed.
4.1. In-furnace model
The formulation, calibration and validation of the dynamic model
used for the in-furnace side is presented elsewhere [29]. The in-furnace
model uses semi-empirical modeling rather than pure empirical corre-
lations, i.e.,it closes mass and heat balances based on theoretical ex-
pressions containing experimental coefficients (e.g., mass transfer
coefficients, velocity fields) determined from dedicated experimental
campaigns. This theoretical ground gives the in-furnace model a rela-
tively robust ground. Furthermore, the validity scope and reliability of
such model for different boiler designs and conditions have recently
been explored in [31]. Yet, a brief summary of the in-furnace side model
is included below.
The model describes the in-furnace side of FB boilers through a
number of perfectly mixed control volumes (CSTR) that exchange mass
and energy. The model accounts for the three processes that govern the
energy and mass transfer in FB furnaces: (i) fluid dynamics (1.5D rep-
resentation, i.e., considering the wall layers hosting the internal recir-
Fig. 8. Scheme of the thermal connections between the evaporator and the in-
culation of solids [59,60]); (ii) thermochemical conversion; and (iii)
furnace solids wall layer. The vertical dashed line represents the boundary
heat transfer, covering both solids convection and radiation. The model
between the in-furnace and water/steam side models.
accounts for three phases: bulk solids, fuel, and gas. The fuel contains
three classes to account for changes in size and density during conver-
– The flue gas stream leaving the furnace enters the water/steam side
sion, while the gas consists of a mixture of nine components.
model via the convection path.
As shown in Fig. 7, the inputs to the in-furnace side model are the
– The waterwalls that make up the evaporator remove heat from the
geometry of the boiler, mass flows temperature and locations of the fuel
in-furnace side while evaporating the two-phase water flow, yielding
and gas streams fed, and the properties (size and density) of the bulk
a certain wall temperature. This connection, shown in Fig. 8, con-
solids. The model solves dynamic mass and energy balances for each of
tains as many connections as control volumes with the waterwalls
the control volumes defined, solving for each of them the concentrations
present the in-furnace side model (10 for the present case; see [29]).
and mass flows of each of the phase components, as well as the tem-
– The immersed superheater located in the furnace (SH2 in Fig. 1)
peratures and heat flows to neighboring cells and walls. To adjust the
extracts heat from the corresponding in-furnace control volumes
model to represent as closely as possible the reference unit, the model is
while superheating steam.
calibrated by tuning the solids particle size and gas mixing using process
site data.
9

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
4.2. Water/steam side model previously [64], in which dynamic energy and mass balances are solved
for the liquid and vapor volumes, accounting for bulk boiling and bulk
The present section summarizes the main correlations that describe condensation, respectively. Heat transfer through the drum wall and
each of the water/steam side components using the lumped parameter heat accumulation in the wall are neglected. Natural circulation in the
approach, which is confirmed to be a valid assumption for dynamic drum-evaporator is modeled through an ideal height difference model
power plant modeling [61]. A more extensive list of the main model with a pressure head such that the water flow through the downcomers
equations and references is included in Appendix A (Table A1). and risers is ensured. Detailed descriptions of the drum dynamics can be
For all the components, geometric data (e.g., dimensions, number of found in the papers of Åstro ¨ m and Bell [65] and Eborn [61].
tubes, tube pitch, existence of fins, metal thickness) are fed into the The steam turbine is described through a quasi-static model, which is
model according to the design of the reference plant. For those com- a valid assumption given that its characteristic time is much shorter than
ponents where a 0-dimensional representation is not appropriate (e.g., a the characteristic times associated with other components, such as the
tube), a 1D discretization into a series of volumes is applied, for each of condensers or the furnace [66]. The turbine is modeled according to
which the dynamic mass and energy balances are solved. The number of Stodola’s law of cones [Eq. (8)], where mn ˙ om is the nominal mass flow,
ρ
volumes in which a certain equipment can be discretized represents a pi,nom and i,nom the pressure and density of the steam at turbine inlet,
compromise that is made between model accuracy and computational respectively and p0,nom the nominal outlet pressure.
time in the calibration phase. The component models described below m˙
are calibrated through a pre-exponential factor in the correlations for K t = nom (8)
the heat transfer coefficient, C. The model is calibrated to operational p ρ 1− p0,nom 2
data collected at 100 % load (see Appendix A), whereas the prediction of √̅̅̅ i ̅ , ̅ n ̅ o ̅̅ m ̅̅̅̅̅ i ̅ ,n ̅̅ o ̅̅ m ̅̅(̅̅̅̅̅̅̅̅̅̅̅̅
(
̅̅̅ p ̅̅i,̅n̅o̅m̅̅̅
)
̅̅̅̅̅)̅̅̅̅
the partial-load performance of the reference plant represents the model
Therefore, the effects of rotor dynamics, turbine casing and rotor
validation (see Section 4.4).
Regarding the gas–water/steam heat exchangers, the heat transfer inertia are not captured by the model. Consequently, dynamic in-
teractions between the power grid and the steam cycle are here
on the gas side of superheaters and economizers in the convection path is
neglected. The dry isentropic efficiency of the turbine is assumed to be
modeled using a convective heat transfer coefficient for gas flowing over
constant (0.89) throughout all the load levels investigated [67]. Lastly, a
tube bundles [Eq. (4)], which uses the Nusselt (Nu) number correlated
from VDI-W ¨ armeatlas [62], where λ is the thermal conductivity and dhyd simple generator model is included to account for the mechanical shaft
efficiency, which is assumed to be constant (0.98).
the hydraulic diameter of the tube. In the water/steam side model of
All the pumps present in the feedwater line are modeled as centrif-
economizers and superheaters (monophasic flow), the heat transfer is
ugal pumps with mechanical efficiency of 0.98 and isentropic efficiency
also described using a Nu-correlation as in Eq. (4), but excluding the
of 0.80. The computation of the flow is based on the quadratic flow
tube arrangement factor, Fa. In the evaporator (biphasic flow) a Nu-
characteristic, assuming a constant rotational speed. Control valves are
correlation based on the Dittus-Boelter equation is used [8,63].
modeled with linear opening flow characteristics. Thus, a flow coeffi-
F Nu λ
α=C a
d hyd
0
(4)
c
T
i
h
e
e
n t
fl o
d
w
et e
is
r m
as
i
s
n
u
e
m
s
e
th
d
e
t o
o p
b
e
e
n
t
i
u
n
r
g
b u
w
le
h
n
e
t
n
[ 6
co
8
m
],
p
a
a
n
r
d
e d
th
t
e
o
a c
n
c
o
u
m
m
in
u
a
la
l
t
c
io
o
n
n d
o
i
f
t i
fl
o
u
n
i
s
d
.
and energy within the unit is neglected, i.e., the mass and energy bal-
The pipe pressure drops in both the gas and water/steam sides are
ances are formulated as static.
computed through a friction loss correlation based on a coefficient that
The two condensers present in the reference unit are modeled as
assumes turbulent flow, in which Kf is the friction
ρ
loss coefficient, dpnom
horizontal cylindrical vessels with immersed horizontal tubes, with the
the no ˙ minal pressure drop, LF the length factor, nom the nominal den- only difference being the cooling fluid (DH water and feedwater). At the
sity, mnom the nominal mass flow and nchannels the number of parallel
bottom of the units, there is a hotwell in which the condensate is
channels:
accumulated. A wall model such as that described in Section 4.2.1 [Eq.
dp= K f ρ m˙2 (5) ( a 7 ss ) u ] m se e p s a r t a h t e e r s m th od e y c n o a n m de ic n s e in q g u i s l t ib ea ri m um fr o b m et w th e e e c n o o th li e n g l i fl q u u i i d d . T an h d e m va o p d o e r l
phases. Regarding the heat transfer, a correlation for condensing steam
K f = dp nom m * ˙n L om F* ρ 2 nom (6) c o o v r e r r e l h a o ti r o iz n o f n o t r a l l i t q u u b id es s s is im u i s l e a d r t [ o 6 t 2 h ] a , t w d h e e p r i e c a te s d f o in r E th q e . ( c 4 o ) o i l s in u g s e m d, e d a i l a b , e i a t
nchannels one that is based on the logarithmic average of the inlet and outlet
( )
temperatures and that is valid for both turbulent and laminar flows.
Lastly, the wall representing the interface of the water/steam side
The deaerator (open feedwater heater) is modeled as a cylindrical
with the gas side is modeled as a 1D and flat domain, with a heat
open vessel, assuming thermodynamic equilibrium between the two
accumulation given by Eq. (7) (with mwall being the total mass of the wall
phases. The model neglects heat transfer through the vessel walls.
and cp its heat capacity). The thermal resistance Rw is a function of the
Regulatory control loops present in the reference plant (see Section
wall thickness, area and thermal conductivity.
2.3) are included in the model to ensure stable operation of the steam
m c dT 2(T −T
wal d l t p = wall,g R wall,steam/water) (7) cycle. The PI controllers, the well-known Laplace-domain transfer
w function (Gc) of which is depicted in Eq. (9) (Kc is the controller gain and
τ
The steam drum is modeled according to the formulations published I the integral time), are tuned according to the PID tuning rules pub-
lished by Skogestad [69], and Table 8 lists the resulting tuning param-
eters of the regulatory control loops. For cascade loops, the slave
Table 8
controller (i.e., the internal, faster controller) is tuned first. Thereafter,
Tuned parameters of the regulatory PI-controllers.
the loop is closed and the master controller is tuned.
Controlled variable (CV) Manipulated variable (MV) Kc τ I 1
DHC level Condensate valve opening 3,000 150 G c (s)=K c (1+ τs ) (9)
I
FWH level Condensate valve opening 2,800 200
OFWH pressure Steam valve opening 1 0.001 A similar approach is followed for implementing the supervisory
Drum level FW valve 85 500
SH2 temperature Attemperator water valve opening −0.015 1 control structures tested in this work (see Section 3.1). When tuning the
SH3 temperature Attemperator water valve opening −0.015 6 supervisory controllers, the regulatory control layer is kept in closed
10

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Table 9 unit presented in Section 2. As mentioned above, steady-state data at
Tuned parameters of the master supervisory PI-controllers (load controllers). design load, i.e., 100 % load, were used for calibration (tuned parame-
Control structure Kc τ I ters of the water-steam side are shown in Table A2 in Appendix A and of
the in-furnace side in [29]), leaving the off-design datasets, i.e., 75 %
Turbine following 0.00040 200
and 50 % load, for the validation of the model. The steady-state vali-
Boiler following 0.00007 440
Floating pressure 0.00040 80 dation of the integrated model is carried out by means of the absolute
Hybrid 0.00007 440 percentage error (AP) between the measured (xm) and the simulated (xs)
process variables [see Eq. (10)].
l t o h o e p t u w n i i t n h g t p h a e r a s m am et e e t r u s n o i f n t g h e p m ar a a s m te e r t e c r o s n a tr s o l l i l s e t r e s d ( i i . n e . T , l a o b a l d e c 8 o . n T t a ro b l l l e e r 9 s ; l i s s e t e s AP=100 |x m x − m x s | (10)
Figs. 2 and 3). Note that in all the control strategies in which the pressure
The results of the steady-state validation are shown in Table 10 (note
is fixed, this loop is tuned and closed before the master controller.
that the measurement dataset for 75 % load lacked three signals),
showing that all errors are <5 % with an average of 1.5 %, i.e.,the
4.3. Validation of the dynamic model model shows good agreement with the industrial data from off-design
operation. Although the control structure is typically linked to the
The integrated dynamic model presented here is validated against transient performance (such as that illustrated in Figs. 9 and 10 below),
steady-state and transient operational data from the industrial reference some assessment of the control structure can also be inferred from steady
Table 10
Steady-state validation of the main process variables simulated by the integrated process model (xs) against the measured values (xm) in the reference unit for different
loads. AP, absolute percentage error.
Variable (unit) 100 % load (calibration) 75 % load (validation) 50 % load (validation)
xm xs AP (%) xm xs AP (%) xm xs AP (%)
Pel (MW) 19.86 19.60 1.31 – 15.23 – 9.08 9.28 2.20
QDH (MW) 56.88 54.18 4.98 – 42.29 – 28.91 28.49 1.45
Fsteam (kg/s) 28.57 27.46 4.04 21.02 21.28 1.24 13.90 13.94 0.29
Tin,T (◦C) 494 493 0.17 494 491 0.55 496 492 0.81
TDH,out (◦C) 90 92 2.56 – 90 – 84 84 0.11
Pdrum (bar) 72.00 70.54 2.03 69.40 69.08 0.46 68.40 67.89 0.75
Fig. 9. Input trajectories to the model for transient operation validation.
11

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Fig. 10. Transient validation of the main process variables when comparing the simulated and measured trajectories over a 3-h load increase.
state analysis. In relation to this, when resembling the control structure model. The set-point (SP) of the live steam pressure was fixed to the
of an industrial plant, [17] two aspects of special importance are: (i) the design value (67 bar) according to the operational strategy of the
achievement of stability, and (ii)the good agreement with the steady reference plant.
state values measured in the industrial facility. Regarding these two, (i) Fig. 10 compares the simulated and measured transient values of the
the control layer model attains stable solutions for all off-design oper- main process variables used for model validation: power generation, Pel;
ational points tested, and (ii) the steady states reached by the model live steam mass flow, Fsteam; DH production, QDH; DH outlet temperature,
shows an average error of 1.5 % as compared to measured values, as TDH,out; and drum pressure, Pdrum. For each of these variables, the mean
shown in Table 10. Thus, the model can satisfactorily predict steady- and maximum error values (calculated as AP) over the 200 min of the
state operation within the operational window of interest in this work. simulated period are shown in Table 11. While all the average error
Validation of the transient performance of the model is performed by values are <6 %, the maximum errors observed in the electricity and DH
comparing the integrated model output with measurements taken over production are 15 % and 11 % respectively. According to the transient
3 h of operation during a load change from 50 % to 100 % load. Fig. 9 trajectories plotted in Fig. 10, the model describes fairly well the tran-
shows the transient input values to the model (the original time reso- sients of industrial operation, especially when it comes to predicting the
lution was 1 min and it was interpolated to yield a resolution of 1 s). electricity and DH generation as well as the live steam flow produced in
Note that this dataset was used for validation of the in-furnace dynamic the boiler. The reference data for the drum pressure exhibit some os-
model in [29], with the DH inlet mass flow and temperature (Fig. 9b) cillations for some minutes that the model cannot predict, which is most
being the new inputs added for validation of the integrated process likely due to differences in controller tuning procedures between the
12

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Table 11
Mean and maximum errors (AP, absolute percentage error) over the 200 min
period used for transient validation of the model.
Variable (unit) Mean AP (%) Maximum AP (%)
QDH (MW) 4.31 11.02
Pel (MW) 5.35 15.57
Fsteam (kg/s) 4.65 9.87
Pdrum (bar) 0.51 2.95
TDH,out (◦C) 1.39 3.15
Table 12
RGA matrix of the 3 ×3 MV-CV system. Green cells represent the best pairing
alternatives and orange cells indicate the pairings of turbine-following and
sliding pressure strategies.
MV
Qcomb Valvesteam FDSH
CV Pel 0.9721 0.0094 0.0185
Psteam 0.0177 0.9814 0.0009
Tsteam 0.0102 0.0092 0.9806
industrial site and the model. Other discrepancies observed in, for
instance, the outlet DH temperature, may be attributed to the fact that
some design data required to model the plant were not available to the
authors, so some assumptions were made (such as the residence time of
the condensate in the hotwell or the characteristic curve of some pumps,
among others).
In conclusion, based on the results presented previously [29] and in
the present section, it can be stated that the integrated furnace-water/
steam side dynamic model presented is capable of predicting the dy-
namic behaviors of industrial FBC-CHP plants with sufficient accuracy
for the scope of this study, i.e., the analysis of the inherent and Fig. 11. Computed open-loop stabilization times for the main process variables
controlled dynamics of industrial-sized FBC-CHP plants. for different process disturbances, i.e., step-changes in combustion load Qcomb,
live steam mass flow FDH, inlet district heating temperature TDH,in, and heating
5. Results and discussion
value of the fuel HVf (listed in Table 4).
5.2. Dynamic behavior of the reference plant
5.1. Relative gain analysis
Below, we explore the dynamic behavior of the reference FBC-CHP
The computed RGA matrix is shown in Table 12. The system studied
is 3 × 3 and as such allows for six possible control structures (i.e., plant. First, the uncontrolled dynamics of the system are computed in
an open-loop analysis. Second, the control strategies described in Sec-
combination of MV-CV pairings). However, it can be seen in Table 12
tion 3.1 are tested in the integrated dynamic model for the variable
(green cells) that only one structure provides a low degree of loop in-
ramping rate scenarios defined in Section 3.4. Third, the capabilities of
teractions (i.e.,all RGA elements close to 1), i.e., controlling the
the plant to achieve temporary overload by making use of the turbine
generated electrical power with the combustion load, the live steam
bypass are evaluated.
pressure with the main control valve opening, and the superheated
steam temperature with the DSH water flow. These pairings correspond
5.2.1. Open-loop analysis
to turbine-following control (see Section 3.1.1). The remainder of the
The computed stabilization times (in minutes) of the open-loop
MV-CV connections give RGA elements close to 0, a sign of poor
analysis performed when the plant is running at 80 % load are plotted
controllability [70]. Notably, among the structures showing poor
in Fig. 11 for the six process variables monitored during the simulations.
controllability are both the well-established boiler-following control
It is clear that for a step-change upwards or downwards (±20 %) for all
(see Section 3.1.2) and the sliding pressure control (Section 3.1.2.2), in
of the investigated disturbances (Table 4), all the stabilization times are
which the electrical power is controlled by opening the steam valve and
<25 min. In the water/steam side, the live steam pressure and mass flow
the steam pressure is controlled by the combustion load (orange cells in
are the variables that reach stabilization the fastest, with an average of 5
Table 12). The poor performances of these strategies in the RGA are
min, owing to the fact that pressure waves travel at the speed of sound in
explained by the fact that the valve opening only has a temporary effect
the fluid. This is in contrast to the velocity of the fluid in the pipe
on the power produced, due to the changes in pressure and mass flow,
whereby the temperature is propagated in a plug flow model, thereby
since the new steady-state reached after the transient effects is similar to
yielding faster stabilization times. The generated power stabilizes
that seen with the former valve opening. The only way to modify the
slightly more slowly (average stabilization time of 8 min), whereas the
steady-state pressure and flow (and, thereby, the electrical power) is
outlet DH temperature and the heat load in the DH condenser yield the
through manipulating the energy added to the system, i.e., the com-
slowest times for stabilization, averaging 10 min and 13 min, respec-
bustion load. Thus, it can be concluded that the steady-state effect of the
tively, for the cases investigated. It is important to highlight that the
steam valve opening on the power generated is negligible, and that the
times computed for the live steam variables can be related to the sta-
only MV that can effectively change the levels of heat and power pro-
duced is the combustion load. Similar effects have been observed pre-
bilization time of the in-furnace heat transfer Qwall (5–10 min in this
work; see [29] for details). This confirms the usefulness of modeling the
viously [20,32].
13

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Fig. 12. Electrical power output responses (in % of the design electrical power) compared to the load set point (SP) for Scenario I under different control structures
and ramping rates. BF, Boiler-following; FP, floating pressure; TF, turbine-following.
in-furnace side for understanding and describing the live steam dy- 5.2.2. Variable ramping rate analysis
namics. The computed stabilization times also reveal that in the water/ Fig. 12 shows the responses of the generated power (in percent of the
steam side, process equipment with steam-only inventories generally design load, i.e., 100 %) for each of the supervisory control strategies
have faster dynamics that those in which liquid and steam coexist. The and for all the cases simulated as part of Scenario I, i.e., when the power
stabilization times listed in Fig. 11 show that the process response is the output is reduced from 100 to 50 %. It is evident that for the very slow
fastest for changes in the DH mass flow, which is in line with the results and slow cases (cf. Table 7), all the strategies are capable of providing
from a previous study [8]. Note that changes in the DH flow and tem- load changes at the same rate as the set-point (SP) is changed, with the
perature do not affect the live steam conditions, and the change exception of the floating pressure operation, which shows some delay
observed in the generated power is caused by the variations in the and undershoot, reaching stabilization some 4 min after the SP. As
condensing pressure. The disturbances linked to the in-furnace side shown in Fig. 12, most of the differences between the control strategies
cause the slowest responses in the system, with the stabilization times occur in the faster cases. It is observed that while the control strategies
for changes in combustion load (Qcomb) and fuel heating value (HVf) that manipulate the live steam control valve (BF and hybrid control
averaging 11 min and 13 min, respectively, across all six variables (both strategies) provide very fast power output changes that follow the SP,
for the step-down case, i.e., Fig. 11a). those that manipulate the combustion load (FP and TF) are considerably
Differences in stabilization times between a step-change down and a slower. In both the fast and very fast cases, floating pressure operation
step-change up are observed when comparing Fig. 11, a and b. The shows the slowest response, with a rising time of 6 min and a stabili-
process tends to stabilize faster (15 % shorter stabilization times on zation time of 10 min. Turbine-following operation displays a faster
average) when heat is added to the system, i.e., when the combustion rising time than FP (4 min) and a similar stabilization time (10 min). The
load, fuel heating value and DH inlet temperature increase. This non- differences between FP and TF observed in the fast and very fast cases
linearity has been reported in several studies that have investigated are within expectations, since TF makes use of the steam control valve to
the inherent dynamics of various thermochemical processes (see for correct the pressure deviations, which has a dynamic effect on the power
instance [57,71]), and is in agreement with the results obtained from the production. Similar characteristics were observed in a previous study
analysis of the in-furnace side [29]. In a previous study [18], it has been [20], while [16] has claimed that FP operation provides up to 50 %
highlighted that the mechanism driving the load increase, i.e.,the fuel slower ramp rates than the BF and hybrid control strategies. The same
conversion, is an order of magnitude faster than that leading the load reasoning applies when explaining how the BF and hybrid strategies
reduction, i.e.,the heat transfer to the waterwalls (as a consequence of yield the fastest (and similar) responses: the dynamic effect of the con-
the thermal inertia caused by the furnace solids). trol valve uses the energy accumulated in the drum and steam lines to
When the same open-loop tests are simulated for the process running generate fast temporary changes in the steam pressure and mass flow,
at 70 % load instead, all six process variables are found to stabilize more which quickly propagate to the turbine. If the combustion load is not
slowly than they do in the 80 % load case. This difference ranges from 9 changed subsequently, the new steady state reached would be similar to
% slower in the case of the DH outlet temperature up to 25 % slower for the previous one, according to what was observed in the RGA. It is the
the generated electricity. This effect has been reported earlier for ther- combination of the steam control valve and the combustion load that
mal power plants [8,29], and is caused by the decrease in flows that is enables the quick and effective load changes plotted in Fig. 12.
intrinsic to partial-load operation, which inevitably increases the resi- Since the fast changes in power output reported in Fig. 12 occur due
dence time of the fluid both in the gas and water/steam sides. to the rapid dynamics of steam throttling, the live steam pressure is
plotted in Fig. 13 for the fastest ramping rates under TF, BF and hybrid
control operations. It is clear that the quick changes in power output
14

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
intermediate case, with higher process efficiency during transient
operation than is achieved with BF or hybrid control (since the tempo-
rary closure of the control valve is less drastic). These results highlight
the tradeoff that exists between flexibility and efficiency, as well as the
operational constraints associated with flexibilization, both of which
topics are explored further in Section 5.3. Regarding the question as to
whether the live steam pressure should be controlled, it can be
concluded from these results that controlling the pressure gives the
fastest power response (except for boiler-following operation), although
leaving the live steam valve opened enhances process efficiency and
controllability. With regards to the live steam temperature, very few
variations are found due to the fact that it is a controlled variable under
F to i g. t h 1 e 3 . se L t i v p e o s i t n e t a m (S P p ) r , e s f s o u r r e S p ce ri n o a r r t io o t I h e – m V a e s r t y e r f c a o s n t tr ( o 0 l . 0 v 0 a 5 lv % e - w u h n e it n / s c ) o . m B p o a il r e e r d - all the tested strategies, with measured undershoots of <5 %.
Conclusions analogous to those related to the power generation can
following, BF, floating pressure. FP; turbine-following, TF.
be drawn regarding the DH production. For simplicity, only the very fast
rate of Scenario I is plotted in Fig. 14, where again the operation with FP
shows the slowest response and BF and hybrid control strategies show
the fastest responses. For the case shown, FP displays a rising time of 7
min and a stabilization time of 10 min, as compared to the 3 min and 10
min, respectively, for the hybrid and BF control strategies. Note that the
DHC has been simulated with a constant mass flow and variable outlet
temperature, since this is a conventional way of operating DH networks
in order to avoid water hammering issues (although the operational
dataset used for model validation presented some flow fluctuations; see
Fig. 9).
Fig. 14. District heating (DH) production (as % of the design load) for) for
Scenario I – Very fast (0.005%-unit/s)-under different control strategies. BF, Similar findings to those presented above for Scenario I were ob-
Boiler-following; FP, floating pressure; TF, turbine-following. tained for Scenario II (50−>40 % load) and, therefore, these results are
not included here. In general, all the rising and stabilization times are
slightly shorter than in Scenario I, which can be attributed to the smaller
provided by the BF and hybrid control operations occur at the expense of
absolute change in load of Scenario II [29]. Similarly, the pressure
substantial steam throttling when the control valve is suddenly closed.
The overshoot in the pressure trajectory is +30 % for the BF case versus overshoots for hybrid and BF operations are decreased with respect to
±0.01 % for the TF strategy. In the case of BF operation (and similarly in Scenario I.
hybrid control operation), the temporary increase in the live steam
5.2.3. Other strategies – Turbine bypass
pressure is directly linked to exergy losses and, therefore, the loss of
Fig. 15 shows the responses of the simulated turbine bypass after the
available work, with a negative impact on process efficiency during the
bypass valve is opened to allow the flow of 3, 5 and 7 kg/s of live steam
transient. Furthermore, once the new steady-state is reached, the partial
when the boiler is running steadily at 50 % load. The rise time of the
closure of the control valve is also linked to reductions in enthalpy and
electrical power output (Fig. 15a) responses lies between 25 s and 60 s,
power-to-heat ratio [19]. The complete opposite situation occurs during
and it increases in line with the bypass flow. It can be seen that the
FP operation, whereby the valve remains fully open during all the
response of the DH output (Fig. 15b) is slower than that of the electrical
operational window simulated here. Thus, even though it provides the
output, with stabilization times in the range of 6–8 min. When the valve
slowest response due to the longer characteristic times of the in-furnace
is closed (Fig. 15, c and d) the power is increased with rise times of
side, it is the strategy that maximizes process efficiency during both
around 1 min, regardless of the magnitude of the bypass flow. These
transient and partial-load operation. TF operation represents an
Fig. 15. For different bypassed flows, simulated responses of the generated electrical power and district heating (Pel and QDH respectively) when the bypass valve is
opened (a and b) and closed (c and d).
15

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
results are in line with published work [54]. investigated) without the operational problems associated with steam
The fuel flow over the bypass opening has been added in Fig. 15, a throttling. Furthermore, the fuel supply can remain constant, which
and c, and, as expected, it remains constant. This is important for could solve the issues linked to undesired emissions. Thus, appropriate
emissions control, combustion efficiency and intraday trading, as dis- design and implementation of the turbine bypass could enable intraday
cussed further in Section 5.3. Another conclusion that can be drawn and balancing trading capabilities, as well as the reduction of minimum
from Fig. 15 is that turbine bypass allows for the decoupling of the heat load while maintaining DH generation. The latter is of particular interest
and power productions, effectively increasing the plant product flexi- when electricity prices are low but the demand for DH remains high.
bility [11]. It can also be concluded from Fig. 15 that operation with The implications that operating FBC-CHP plants to enable fast
turbine bypass expands the operational boundaries of the plant, allow- changes in power output have for the production of DH can also be
ing reduction of the minimum power load without altering the com- assessed. The DH networks are characterized by slow (and often pre-
bustion process. dictable) demand changes, as well as the high thermal inertia seen in
conventional DH systems, which dampens the oscillations connected to
5.3. Practical implications DH disturbances. Thus, the DH flow and temperatures could be assumed
to be quasi-static for the timeframe investigated. Furthermore, there is
The validity of the simulation results presented in Section 5.2 and the possibility to add thermal energy storage to the DH system, so as to
their practical implications for the flexibility of biomass-based FBC-CHP buffer the variations caused by the load-change scenarios investigated.
plants are discussed in this section. This would also allow the heat and power production outputs of the
First of all, the results from the variable ramping rate (VRR) highlight plant to be dispatched based on electricity prices, rather than on DH
the importance of the control strategy selected when it comes to demand, and would facilitate shifting heat production in time to remove
providing load changes. The results of this work demonstrate that con- peak heat-only boiler units of the DH system that may run on fossil fuels.
trol strategies using the turbine control valve can provide large changes
in load (magnitude of around 10 MWe) with response times of 30–60 s. 6. Conclusions
This is achieved by making use of the throttling reserve to store some
energy in the steam generator surfaces, allowing the plant to provide fast The present work entails an analysis of the inherent and controlled
load changes while avoiding the delay and inertia of the in-furnace side. transient operation capabilities of fluidized bed combustion plants for
However, throttling is by definition a purely dissipative process (isen- combined heat and power production. A model of the in-furnace side of
tropic) above the ambient temperature, decreasing the fluid enthalpy fluidized bed combustors is integrated into a dynamic process model of
without the production of useful work. It has been shown that the faster the water/steam side. After validation with industrial operational data,
the ramping rate, the more energy is dissipated through throttling, given the model is applied to perform both a relative gain analysis and dy-
that the control valve needs to close more swiftly. namic analysis, in which the inherent dynamics of the process as well as
In addition, other operational constraints must be considered when the performances of different control structures identified from the
assessing the capabilities for very fast load changes. For instance, the literature are evaluated.
reference plant considered in this work has a high-pressure alarm in the Based on the results obtained, the main conclusions of the work are
drum for steam pressures above 80 bar, which for the boiler-following summarized as follows:
response (Fig. 13) would be triggered for the load change simulated
for Scenario I. Moreover, thermal stresses in the turbine and thick- – While most of the literature has often assumed the water-steam side
walled components of the boiler and condensers are amplified when to be the limiting the transient operation of fluidized bed combustion
the steam pressure and temperature vary substantially and frequently. In plants, the present paper shows that the in-furnace and water-steam
contrast, in floating pressure operation, the live steam valve remains sides of fluidized bed combustion plants have inherent characteristic
unaltered, which combined with the live steam temperature control times in the same order of magnitude. Thus, modeling of the in-
makes the steam entering the turbine to be at a constant temperature at furnace side cannot be disregarded in dynamic analyses at plant
all loads. level.
Too-rapid load changes can cause undesired emissions from the – The use of control and operational strategies such as turbine bypass
furnace (see [29]). Thus, although physically feasible with the right can enhance the operational and product flexibility of fluidized bed
control strategy, detailed optimization studies are needed to determine combustion plants for combined heat and power production,
the profit loss and gain related to providing load changes in these short enabling temporary over-underload performance as well as
timeframes on a regular basis, for instance, to meet a need for primary providing load changes at constant combustion load, i.e., avoiding
control reserve (in most European markets characterized by response the delay associated with the in-furnace side. Yet, a more detailed
times in the order of 30 s). Note that the dynamics of other components assessment of component lifetime versus revenue is needed in order
not included in the present model, such as the fuel handling and feeding to extract further conclusions.
systems, would also play a role in the total transient capabilities of the
plant. Moreover, sometimes the bottleneck of the plant lays on the The results and conclusions derived from this work should be of
regulatory control layer, as it is tuned so slow that there is not a good importance when assessing the operational capabilities of fluidized bed
timescale separation between the layers, thereby creating potential in- combustion plants for combined heat and power production when they
stabilities or odd transients. Furthermore, slow tuning of the regulatory are operated to provide fast load changes. Nevertheless, further research
control layer can lead to noticeable undershoots in steam temperature accounting for the thermal stresses and lifetimes of key power plant
when the load is quickly ramped downwards. Lastly, it is worth components is required to construct a comprehensive economic picture
mentioning that there are a number of advanced control strategies (e.g., of the implications of flexible operation.
integrated, coordinated or parallel control) which, being extensions of
the ones presented here, have not been included in the present study. Funding
Nevertheless, they could partially contribute to solving some of the
operational issues identified here, e.g., the pressure overshoots. This work was supported by the Swedish Energy Agency (project
The addition of a high-pressure steam extraction that bypasses the 46459-1, “Cost-effective and flexible polygeneration units for maxi-
turbine is shown to resolve partially the problems of emissions and mized plant use”).
thermal stresses identified above. First, it allows the provision of fast
changes in power (with response times of around 1 min for the cases
16

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Declaration of Competing Interest Data availability
The authors declare that they have no known competing financial The authors do not have permission to share data.
interests or personal relationships that could have appeared to influence
the work reported in this paper. Appendix A. Water/steam side model
See Tables A1 and A2.
Table A1
Equations used to model the different components of the water/steam side model.
Component Formulation/magnitude Equation Ref
Economizers and Superheaters Heat transfer gas side α=C FaNu0 λ
[62]
dhyd
Energy balance gas side m ˙(hout −hin )=αA(Tgas −Twall ) –
˙
Mass balance gas side dm=0
[72]
dt
Heat transfer water/steam side α=C Nu0 λ
[62]
˙
dhyd
–
Mass balance water/steam side d
d
m
t
=m ˙
out
−m ˙
in
˙
Pressure drops dp=Kf
ρ
m 2
[8,73]
Kf =dpnom
˙
*LF*ρ n
2
o m
mnom
(nchannels)
Walls connecting pipes
Rw
=s
A
/λ –
mwallcpdT=2(Twall,g −Twall,steam/water)
dt Rw
Evaporator tubes Heat transfer water side α ψ tp = = f( ψ C α o L , Bo) [58]
λ
α
L
=0.023Re0.8PrL 0.4(
dh
L
yd
)
B C o o = = G [ 1 • − x q hv x a ] p 0 .8 [ ρ ρ L v ] 0.8
˙
Pressure drops dp=Kf
ρ
m2 =0 [8,73]
Kf =dpnom
˙
*LF*ρ n
2
o m
mnom
(nchannels)
Walls connecting pipes
Rw
=s
A
/λ –
mwallcpdT=2(Twall,g −Twall,steam/water)
dt
˙
Rw
Turbine Stodola Law of cones for off-design conditions Kt = mn [74]
2
√
√ √
̅p̅̅i̅,̅n̅̅ ρ ̅̅i̅,̅n̅̅
(
̅̅̅̅1̅̅̅̅ − ̅̅̅̅
(
̅̅̅ p ̅p̅̅ 0
i
̅
,
, ̅
n
n ̅̅̅)̅̅̅̅̅̅
)
̅̅̅̅
Dry isentropic efficiency degradation η is,wet √=η is,dry −β(1−x)
[75]
E G n e e n r e g r y a t b o a r lance h P o el u ˙ t − = η m h ec i h n m − ˙( η h is in (h − in h − ou h t ) is ) – – –
Condensers Mass balance hot side d
d
m
t
=m ˙
in
−m ˙
out
Heat transfer hot side Correlation for film condensation over horizontal tube bundles =f(Re,Pr,x,p,pcrit,dhyd )
[62]
Mass balance cold side m ˙ in =m ˙ out [8]
D W r a iv ll i s n g force heat transfer cold side Δ Rw TL = ,M s =
A
/λ T T w w a a ll ll − − T T o i u n t – [6 2]
mwallcpdT=2(Twall,g −Twall,steam/water)
dt Rw
–
Open feedwater heater Energy balance d
d
E
t ˙
=m ˙ chc +m ˙ sths −m ˙ fwhfw
–
Mass balance d
d
m
t
=m ˙
c
+m ˙
st
−m ˙
fw –
Pumps Volume flow rate V ˙ 2 =V ˙ 1 ( N N 2 1)( d d 2 1) –
Valves T Li o n t e a a l r h v e a a l d v e characteristic H m ˙ 2 = = θ H • 1 C ( v N N • 2 1) 2 ρ ( m ˙ • d d n 2 1 d o ) m pn 2 o m√̅ p ̅̅ i ̅ n d̅̅̅p − ̅̅n̅̅o̅ p m̅̅ o ̅̅ u ̅̅ t ̅ [68]
√̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
17

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
Table A2 [23] F. Alobaid, N. Mertens, R. Starkloff, T. Lanz, C. Heinze, B. Epple, Progress in
Calibration factors used to match steady-state operational data at 100% load. dynamic simulation of thermal power plants, Prog. Energy Combust. Sci. 59 (2017)
79–162, https://doi.org/10.1016/j.pecs.2016.11.001.
Component Calibration Factor [24] I. Avagianos, D. Rakopoulos, S. Karellas, E. Kakaras, Review of process modeling of
solid-fuel thermal power plants for flexible and off-design operation, Energies. 13
Gas side Water-steam side (2020). https://doi.org/10.3390/en13246587.
˜´
ECO 1 1.00 0.05 [25] J. Beiron, R.M. Montanes, F. Normann, F. Johnsson, Flexible operation of a
combined cycle cogeneration plant – a techno-economic assessment, Appl. Energy.
ECO 2 1.00 0.05
278 (2020), 115630, https://doi.org/10.1016/j.apenergy.2020.115630.
ECO 3 1.00 0.05
[26] T. Nussbaumer, Combustion and co-combustion of biomass : fundamentals,
SH1 10.00 0.14 technologies, and primary measures for emission reduction †, Energy Fuels. 17
SH2 0.50 1.30 (2003) 1510–1521, https://doi.org/10.1021/ef030031q.
SH3 1.00 0.12 [27] I. Obernberger, Decentralized biomass combustion : state of the art and future
Evaporator tubes – 2.00 development *, Biomass Bioenergy. 14 (1998) 33–56.
[28] C. Yin, L.A. Rosendahl, S.K. Kær, Grate-firing of biomass for heat and power
production, Prog. Energy Combust. Sci. 34 (2008) 725–754, https://doi.org/
References 10.1016/j.pecs.2008.05.002.
˜´
[29] G. Martinez Castilla, R.M. Montanes, D. Pallares, F. Johnsson, Dynamic modeling
[1] r In en te e r w na a t b i l o e n s a -2 l 0 E 1 n 9 e > rg . y Agency, Renewables 2019, 2019. <https://webstore.iea.org/ o (2 f 0 t 2 h 1 e ) r e 3 a 9 c 3 t 6 iv – e 3 9 si 5 d 6 e , i h n t t l p a s r : g / e / - d s o ca i. l o e r g fl / u 1 id 0 i . z 1 e 0 d 2 1 b / e a d c s b . o ie i c le r r .0 s, c 0 In 6 d 2 . 7 E 8 n . g. Chem. Res. 60
[30] M. Gao, F. Hong, J. Liu, Investigation on energy storage and quick load change
[2] International Renewable Energy Agency, IRENA (2019), Global Energy
Transformation: A Roadmap to 2050, 2019. <https://www.irena.org/ c (2 o 0 n 1 tr 7 o ) l 4 o 6 f 3 s – u 4 b 7 c 1 ri , t i h c t a t l p c s: i / rc / u d l o a i t . i o n r g g / fl 1 u 0 i . d 1 i 0 z 1 ed 6 / b j. e a d p e b n o e il r e g r y . u 2 n 0 i 1 ts 6 , .1 A 0 p . p 1 l 4 . 0 E . n ergy. 185
publications/2019/Apr/Global-energy-transformation-A-roadmap-to-2050- ˜´ `
2019Edition>. [31] G. Martinez Castilla, R.M. Montanes, D. Pallares, F. Johnsson, Comparison of the
¨ Transient Behaviors of Bubbling and Circulating Fluidized Bed Combustors, Heat
[3] L. Goransson, F. Johnsson, A comparison of variation management strategies for Transf. Eng. (2022) 1–14 (in press). <https://doi.org/10.1080/
w
(2
i
0
n
1
d
8
p
)
o
8
w
3
e
7
r
– 8
in
5
t
4
e
,
g
h
ra
tt
t
p
io
s
n
:/ /
in
d o
d
i
i
.
f
o
f
r
e
g
r
/
e
1
n
0
t
.
e
1
l
0
ec
0
t
2
r
/
ic
w
it
e
y
. 2
s
1
y
9
st
8
e
.
m contexts, Wind Energy. 21 01457632.2022.2059214>.
[32] M. Hultgren, E. Ikonen, J. Kova, Once-through Circulating Fluidized Bed Boiler
[4] R. Lund, B.V. Mathiesen, Large combined heat and power plants in sustainable
energy systems, Appl. Energy. 142 (2015) 389–395, https://doi.org/10.1016/j. C 20 o 1 n 7 tr . o < l h D t e t s p i s g : n // w do it i h .o t r h g e / 1 D 0 y .1 n 0 a 2 m 1 i / c a R cs e . l i a e t c i r v . e 7 b G 0 a 3 i 2 n 5 A 9 r > ra . y and Partial Relative Gain,
apenergy.2015.01.013.
[33] M. Hultgren, E. Ikonen, Integrated control and process design for improved load
[5] IEA, Harnessing variable renewa ¨ bles: a guide to the balancing challenge, 2011. changes in fluidized bed boiler steam path 199 (2019) 164–178. <https://doi.org/
[6] V. Johansson, M. Lehtveer, L. Goransson, Biomass in the electricity system : A 10.1016/j.ces.2019.01.025>.
complement to variable renewables or a source of negative emissions? Energy. 168
(2019) 532–541, https://doi.org/10.1016/j.energy.2018.11.112. [34] N. Zimmerman, K. Kyprianidis, C.-F. Lindberg, Waste fuel combustion: dynamic
[7] G. Bergendahl, Investeringar i kraftv ¨ arme – Ekonomiska och miljo ¨ m ¨ assiga fo ¨ rdelar, modeling and control, Processes. 6 (2018) 222, https://doi.org/10.3390/
pr6110222.
Gothenburg (2008). https://gupea.ub.gu.se/bitstream/2077/9629/1/2008-413.
[35] H. Zhang, M. Gao, F. Hong, J. Liu, X. Wang, Control-oriented modelling and
pdf.
˜´ investigation on quick load change control of subcritical circulating fluidized bed
[8] J. Beiron, R.M. Montanes, F. Normann, F. Johnsson, Dynamic modeling for
unit, Appl. Therm. Eng. 163 (2019), 114420, https://doi.org/10.1016/j.
assessment of steam cycle operation in waste-fired combined heat and power plants
applthermaleng.2019.114420.
absolute percentage deviation, Energy Convers. Manag. 198 (2019), 111926,
[36] S. Kim, S. Choi, T. Song, Dynamic simulation study of the steam temperature in a
https://doi.org/10.1016/j.enconman.2019.111926. ultra-supercritical circulating fluidized bed boiler system, 2020. <https://doi.org/
[9] E. Mollenhauer, A. Christidis, G. Tsatsaronis, Increasing the Flexibility of 10.1177/0957650920915304>.
Combined Heat and Power Plants With Heat Pumps and Thermal Energy Storage
140 (2018) 1–8. <https://doi.org/10.1115/1.4038461>. [37] S. Kim, S. Choi, J. Yang, Dynamic simulation of a circulating fluidized bed boiler
¨ system Part I : Description of the dynamic system and transient behavior of sub-
[10] M. Richter, G. Oeljeklaus, K. Gorner, Improving the load flexibility of coal-fired
models Dynamic simulation of a circulating fluidized bed boiler system Part I :
p (2 o 0 w 1 e 9 r ) p 6 l 0 an 7– ts 6 2 b 1 y , t h h t e t p in s: t ˜ / e ´ / g d r o at i. i o o r n g / o 1 f 0 a . 1 th 0 e 1 r 6 m /j a .a l p e e n n e e rg rg y y s .2 to 0 r 1 a 8 g . e 1 , 1 A .0 p 9 p 9 l. . Energy. 236 D 01 e 6 sc -1 ri 1 p 4 ti 8 o - n 8 > o . f the dynamic system and, 2016. <https://doi.org/10.1007/s12206-
[11] J. Beiron, R. M. Montanes, F. Normann, F. Johnsson, Combined heat and power
[38] D. Stefanitsis, A. Nesiadis, K. Koutita, Simulation of a CFB Boiler Integrated With a
o 2 p 0 e 2 r a (2 ti 0 o 2 n 0 a ) l . m < o h d tt e p s s f : o // r d i o n i c . r o e r a g s / e 1 d 0 . p 1 r 0 o 1 d 6 u / c j t . e fl n e e x r i g b y il .2 it 0 y 2 i 0 n . 1 a 1 w 76 a 9 st 6 e > i . n cineration plant < Th h e t r tp m s a :/ l / E d n o e i. r o g r y g / S 1 to 0 r . a 3 g 3 e 8 9 S / y f s e t n em rg . D 20 u 2 ri 0 n . g 0 0 T 1 r 6 a 9 n > si . e nt Operation, 8 (2020) 1–14.
[12] S. Kahlert, Investigation of different operation strategies to provide balance energy
[39] M. Zlatkovikj, V. Zaccaria, I. Aslanidou, K. Kyprianidis, Simulation study for
with an industrial combined heat and power plant using dynamic, Simulation 139
(2017) 1–8, https://doi.org/10.1115/1.4034184. comparison of control structures for BFB biomass boiler, in: 61st SIMS Conf. Simul.
Model., Oulu, Finland, 2020.
[13] Y. Gao, Y. Hu, D. Zeng, J. Liu, F. Chen, Modeling and control of a combined heat
and power unit with two-stage bypass 11 (2018) 1–20. https://doi.org/10.3390/ [40] M. De Rosa, M. Carragher, D.P. Finn, Flexibility assessment of a combined heat-
power system (CHP) with energy storage under real-time energy price market
en11061395. framework, Therm. Sci. Eng. Prog. 8 (2018) 426–438, https://doi.org/10.1016/j.
[14] A.D. Zareh, R.K. Saray, S. Mirmasoumi, K. Bahlouli, Extensive thermodynamic and
tsep.2018.10.002.
economic analysis of the cogeneration of heat and power system fueled by the
blend of natural gas and biogas, Energy Convers. Manag. 164 (2018) 329–343, [41] T. Takeshita, H. Aki, K. Kawajiri, M. Ishida, Assessment of utilization of combined
heat and power systems to provide grid flexibility alongside variable renewable
https://doi.org/10.1016/j.enconman.2018.03.003.
energy systems, Energy. 214 (2021), 118951, https://doi.org/10.1016/j.
[15] C.A. Salman, C.B. Omer, Process modelling and simulation of waste gasification-
energy.2020.118951.
based flexible polygeneration facilities for power, heat and biofuels production,
[42] K. Atsonios, A. Nesiadis, N. Detsios, K. Koutita, N. Nikolopoulos, P. Grammelis,
Enegies. 13 (16) (2020). https://doi.org/10.3390/en13164264.
Review on dynamic process modeling of gasification based biorefineries and bio-
[16] I S t . s S G tu en lt e z r , . J U . s K e i , t t T o h , e C B on ab tr c o o l k s f a o n r d F W os i s l i c l o F x u C e o l- m Fi p re a d n y S , t e 2 a 0 m 05 G : p en p e . r 4 a 1 t – in 1 g , 4 P 1 la – n 2 t 1 s . , < in h : t S tp te s a :/ m / based heat & power plants, Fuel Process. Technol. 197 (2020), 106188, https://
doi.org/10.1515/9783110214130.489>. doi.o ¨ rg/10.1016/j.fuproc.2019.106188.
[43] J. Kjarstad, F. Johnsson, The European power plant infrastructure-presentation of
[17] S. Skogestad, I. Postlethwaite, Multivariable Feedback Control, Wiley, Analysis and
the Chalmers energy infrastructure database with applications, Energy Policy. 35
design, 2006. (2007) 3643–3664, https://doi.org/10.1016/j.enpol.2006.12.032.
[18] R. Kehlhofer, et al., Combined Gas and Steam Power Plants, third ed.,, PennWell,
[44] E.M.B. Aske, S. Skogestad, Consistent inventory control, Ind. Eng. Chem. Res. 48
2009. (2009) 10892–10902, https://doi.org/10.1021/ie801603j.
[19] K. Jonshagen, M. Genrup, Improved load control for a steam cycle combined heat
and power plant, Energy. 35 (2010) 1694–1700, https://doi.org/10.1016/j. [45] R G e .E c . o v W e e r. b e S r y , s t W . C .M H . P W . 1 o 3 re ( k 1 , 9 S 9 li 3 d ) i n 2 g 5 3 p – r 2 e 6 ss 0 u , r h e t a tp n s a : l / y / s d is o i u .o si r n g g / 1 t 0 h . e 1 0 se 1 c 6 o / n 0 d 8 9 la 0 w -4 , 3 H 3 e 2 a ( t 9 3)
energy.2009.12.019.
´ 90015-N.
[20] C. Zotica, L.O. Nord, J. Kovacs, S. Skogestad, Optimal operation and control of heat
[46] G. Klefenz, Automatic Control of Steam Power Plants, Bibliographisches Institut,
to power cycles: a new perspective from a systematic plantwide control approach,
1986.
Comput. Chem. Eng. 141 (2020), 106995, https://doi.org/10.1016/j.
[47] C. Zhang, Y. Li, H. Wang, B.A.O. Zhang, F.E.I. Xie, Y.U. Huang, Selection of the
compchemeng.2020.106995. optimal steam pressure for coal-fired power units, ICMLC, 2005, pp. 1835–1838.
[21] Y. Zhao, M. Liu, C. Wang, X. Li, D. Chong, J. Yan, Increasing operational flexibility
[48] S. Sengupta, A. Datta, S. Duttagupta, Exergy analysis of a coal-based 210 MW
o d f u r s i u n p g e r t c ra ri n t s ic ie a n l t c o p a ro l- c fi e r s e s d e s p , o A w p e p r l . p E la n n e t r s g b y. y 2 r 2 e 8 gu ( l 2 a 0 ti 1 n 8 g ) t 2 h 3 e 7 rm 5– a 2 l 3 sy 8 s 6 t , e h m t t c p o s n :/ fi / g d u o r i a .o ti r o g n / thermal power plant, Internatinal J. Energy Res. (2007) 14–28, https://doi.org/
10.1002/er.
10.1016/j.apenergy.2018.07.070.
[49] M.G. Jacobsen, S. Skogestad, Active constraint regions for economically optimal
[22] Y. Zhao, C. Wang, M. Liu, D. Chong, J. Yan, Improving operational flexibility by
operation of distillation columns, Sep. Div. - Core Program. Top. 2011 AIChE Annu.
regulating extraction steam of high-pressure heaters on a 660 MW supercritical Meet. 1 (2011) 474–475.
coal-fired power plant: a dynamic simulation, Appl. Energy. 212 (2018)
1295–1309, https://doi.org/10.1016/j.apenergy.2018.01.017. [50] E T . r a B n r s is . t A ol u , t O om n . a C n o e n w tr m ol e . a 1 s 1 u r ( e 1 ) o f ( 1 in 9 t 6 e 6 r ) a c 1 t 3 io 3 n – 1 fo 3 r 4 m . ultivariable process control, IEEE
18

G. Martinez Castilla et al. A p p l i e d T h e r m a l E n g i n e e r i n g 2 19(2023)119591
[51] M.A. Gonzalez-Salazar, T. Kirsten, L. Prchlik, Review of the operational flexibility [63] K.S. Bhambare, S.K. Mitra, U.N. Gaitonde, Modeling of a coal-fired natural
and emissions of gas- and coal-fired power plants in a future with growing circulation boiler, J. Energy Resour. Technol. Trans. ASME. 129 (2007) 159–167,
renewables, Renew. Sustain. Energy Rev. 82 (2018) 1497–1513, https://doi.org/ https://doi.org/10.1115/1.2719209.
10.1016/j.rser.2017.05.278. [64] F. Casella, A. Leva, Modelica open library for power plant simulation: design and
[52] M. Thern, K. Jordal, M. Genrup, Temporary CO 2 capture shut down: implications experimental validation, in: Proc. 3rd Int. Model. Conf., 2003, pp. 41–50. <http://
on low pressure steam turbine design and efficiency, Energy Proc. 51 (2014) scholar.google.com/scholar?hl=en&btnG=Search&q=intitle:Modelica+open+
14–23, https://doi.org/10.1016/j.egypro.2014.07.002. library+for+power+plant+simulation+:+design+and+experimental+
[53] D. Seborg, T. Edgar, D. Mellichamp, F. Doyle, Process Dynamics and Control, John validation#0>.
Wiley & Sons, 2011. [65] K.J. Åstro ¨ m, R.D. Bell, Drum-boiler dynamics, Automatica 36 (3) (2000) 363–378.
˜´
[54] J. Beiron, R.M. Montanes, F. Normann, Operational flexibility of combined heat [66] R. Paranjape, Modeling and control of a supercritical coal fired boiler, Texas Tech.
and power plant with steam extraction regulation, in: Proc. 11th Int. Conf. Appl. Univ. (1996), https://doi.org/10.1080/00431672.1996.9925425.
Energy, Va ¨ sterås, 2019, pp. 1–4. [67] R. Beebe, Condition monitoring of steam turbines by performance analysis, J. Qual.
[55] D. Systemes, Dymola Systems Engineering, 2021, 2021. <https://www.3ds.com/ Maint. Eng. 9 (2003) 102–112, https://doi.org/10.1108/13552510310482361.
products-services/catia/products/dymola/>(Accessed June 15, 2021). [68] M.B. Dzodzo, B. Liu, A. Cioncolini, S.R. Spiegelman, Appl. CFD Model. Flows Feed-
[56] Modelica Association, Modelica and the Modelica Association, 1996. <https:// Water Pipel. (2006) 293–301, https://doi.org/10.1115/ICONE14-89549.
www.modelica.org/>(Accessed May 14, 2021). [69] S. Skogestad, Probably the best simple PID tuning rules in the world. AIChE Annu.
˜´ ´
[57] R.M. Montanes, S. GarÐarsdottir, F. Normann, F. Johnsson, L.O. Nord, Meet. Reno, NV, 2001.
Demonstrating load-change transient performance of a commercial-scale natural [70] K.E. Haeggblom, Partial relative gain: a new tool for control structure selection,
gas combined cycle power plant with post-combustion CO2capture, Int. J. Greenh. Aiche Annu. Meet. (1997).
Gas Control. 63 (2017) 158–174, https://doi.org/10.1016/j.ijggc.2017.05.011. [71] G. Martinez Castilla, M. Biermann, R.M. Montan ˜´ es, F. Normann, F. Johnsson,
[58] Modelon AB, Modelon Home, 2018. <https://www.modelon.com/>. Integrating carbon capture into an industrial combined-heat-and-power plant:
[59] A. Johansson, F. Johnsson, B. Leckner, Solids back-mixing in CFB boilers, Chem. performance with hourly and seasonal load changes, Int. J. Greenh. Gas Control. 82
Eng. Sci. 62 (2007) 561–573, https://doi.org/10.1016/j.ces.2006.09.021. (2019) 192–203, https://doi.org/10.1016/j.ijggc.2019.01.015.
[60] F. Johnsson, W. Zhang, B. Leckner, Characteristics of the formation of particle wall [72] P.J. Dechamps, Modelling the transient behaviour of heat recovery steam
layers in CFB boilers, in: 2nd Int. Conf. Multiph. Flow, Kyoto, Japan, vol. 3, Kyoto, generators, Proc. Inst. Mech. Eng. Part A J. Power Energy. (1995) 265–273, in:
Japan, 1995. https://doi.org/10.1243/PIME_PROC_1995_209_005_01.
[61] J. Eborn, On model libraries for thermo-hydraulic applications, Dep. Autom. [73] H. Liu, T. Hibiki, Flow regime transition criteria for upward two-phase flow in
Control. Lund Inst. Technol. (2001) 135. http://www.control.lth.se/documents vertical rod bundles, Int. J. Heat Mass Transf. 108 (2017) 423–433, https://doi.
/2001/ebo01phd.pdf. org/10.1016/j.ijheatmasstransfer.2016.12.029.
[62] Springer, ed., VDI Wa ¨ rmeatlas, 9th ed., Springer, 1997. <https://www.springer. [74] H.C. Cooke, On prediction of off-design multistage turbine pressures by Stodolás
com/gp/book/9783540778769>. Ellipse, J. Eng. Gas Turbines Power. 107 (July, 1985,) 596–606.
[75] O. Bolland, Therm. Power Gener. (2014).
19
