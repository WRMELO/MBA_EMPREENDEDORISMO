# Oxidant_control_and_air_oxy_switching_co

**Fonte**: Oxidant_control_and_air_oxy_switching_co.pdf  
**Data de conversão**: 2025-07-30 15:14:52  
**Origem**: base_relevantes

---

Computers and Chemical Engineering 61 (2014) 203– 219
Contents lists available at ScienceDirect
Computers and Chemical Engineering
jo u r n al homep age: www.elsevier.com/locate/compchemeng
Oxidant control and air-oxy switching concepts for CFB furnace
operation
Matias Hultgrena,∗, Enso Ikonena, Jenö Kovácsb
aSystems Engineering Laboratory, University of Oulu, Linnanmaa, POB 4300, FI-90014 Oulun yliopisto, Finland
bFoster Wheeler Energia Oy, Relanderinkatu 2, POB 201, FI-78201 Varkaus, Finland
a r t i c l e i n f o
Article history:
Received 12 June 2013
Received in revised form 12 October 2013
Accepted 24 October 2013
Available online 8 November 2013
Keywords:
Power plant
Oxy combustion
CCS technology
Simulation
System dynamics
Process
a
control
b s t r a c t
Oxy combustion in circulating fluidized bed (CFB) boilers was investigated in this paper. Oxy combustion
is a carbon capture and storage technology, which uses oxygen and recirculated flue gas (RFG) instead of
air as an oxidant. Air and oxy combustion were compared through physical considerations and simula-
tions, focusing on process dynamics, transients and control. The oxidant specific heat capacity and density
are elevated in oxy combustion, which leads to slower temperature dynamics. Flue gas recirculation
introduces internal feedback dynamics to the process. The possibility to adjust the RFG and oxygen flows
separately gives an additional degree of freedom for control. In the simulations, “direct” and “sequenced”
switches between air- and oxy-firing were compared. Fast “direct” switches with simultaneous ramping
of all inputs should be preferred due to the resulting smooth temperature responses. If these process
input changes are unfeasible, the fuel should be altered after the gaseous flows (“sequenced” method).
© 2013 Elsevier Ltd. All rights reserved.
1. Introduction
This paper investigates the differences between oxy combustion
(“oxyfuel” process) and air combustion in circulating fluidized bed
(CFB) power plants, with a particular focus on the process dynamics
and transient behaviour in the oxy-CFB. Oxy combustion is one of
the major industrial carbon capture and storage (CCS) technologies,
which also include pre- and post-combustion capture, as well as
chemical looping combustion (CLC). Carbon dioxide emissions have
received an increasing attention because of the concern for climate
change, especially for industrial branches consuming fossil fuels.
One solution for reducing CO emissions
2
in power plants is to cap-
ture the CO from
2
flue gases with CCS. The captured and processed
CO is
2
transported to underground or underwater high-pressure
storage sites or, alternatively, used in industrial applications.
In oxy combustion, solid fuel is combusted with a mixture
of pure oxygen and recirculated flue gas (RFG) from the process
instead of air as an oxidant, resulting in a flue gas CO concentra-
2
tion of 70–98 vol.% (dry) and thus an easier recovery of the carbon
dioxide from the flue gas. Oxy combustion has been deemed as
one of the most promising options for CO capture,
2
when consid-
ering the energy, cost efficiency and extremely small atmospheric
CO release
2
of the process. The main structural and operational
∗
Corresponding author. Tel.: +358 503502923; fax: +358 85532304.
E-mail addresses: matias.hultgren@oulu.fi (M. Hultgren), enso.ikonen@oulu.fi
(E. Ikonen), jeno.kovacs@fwfin.fwc.com (J.
differences
Kovács).
between air and oxy combustion plants are presented
in this paper, concentrating on the dynamic aspects leading to con-
trol considerations. Even though the ultimate goal of the overall
research is to develop controls for oxy-CFB, this paper deals with
the general aspects and concepts of combustion control suitable for
both air- and oxy-fired CFB boilers.
In fluidized bed (FB) combustion of solid fuels, fuel particles
are fluidized and combusted in a bed of incombustible material
of e.g. sand or ash in the furnace riser. The fluidizing medium is the
primary input gas flow, which commonly contains the oxidizing
agent needed for combustion. In circulating fluidized beds (CFBs),
a sufficiently high gas velocity and small particle size enable the
solids to become entrained with the bed and to leave the furnace
riser tube. The solids are separated from the flue gas in a gas–solid
separator, from which the flue gas continues to the backpass and
the solids are recycled back to the bed through the solids circula-
tion system. Together, these process components form the hotloop
(Fig. 1), which is the studied CFB boiler subsystem of this paper. CFB
combustion is used for solid fuels and also for liquid fuels to some
extent.
When designing control solutions for CFB combustion, the main
issues affecting both the steady-state and dynamic behaviour of the
process can be summarized with the key points below:
• Fluidization
As the furnace input gas (oxidant) flows are responsible for
the fluidization in the CFB, any effects the oxy-firing process
0098-1354/$ – see front matter© 2013 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.compchemeng.2013.10.018

204 M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219
Fig. 1. Operation schematic of the CFB boiler, with the hotloop highlighted with the dashed line.
Modified from Foster Wheeler Energia Oy (2012).
configuration has on the gas flows have the potential to alter the
fluidization and thus the mixing and heat transfer in the bed. Proper
fluidization has to be maintained in the bed.
• Input oxidant flows, i.e. input gas flows
The oxidant flow is air for air-fired FB processes and oxy-
gen + recirculated flue gas for oxy combustion. This is the main
cause for the differences between air and oxy combustion. The heat
capacity, density and chemical component concentrations of the
oxidant are directly related to the differences between the com-
bustion atmospheres. For the combustion dynamics, especially the
oxygen input and thus the oxidant O percentage
2
are of importance.
• Heat transfer & boiler MW output
The heat transfer in the dense bed, the upper furnace, the flue gas
path and the return leg affects the selection of heat exchanger sizes
and the power plant performance optimization. The differences in
heat transfer between air and oxy combustion are thus significant
factors for combustion control. Maintaining a correct heat transfer
distribution is especially important for once-through (OTU) boilers,
as these units don’t contain a water-steam drum as a buffer for
steam generation.
• Combustion & firing power
The combustion in the CFB furnace riser determines the gener-
ated amount of heat in the boiler. When comparing air and oxy
combustion, the effect of the atmosphere change on the com-
bustion reactions and the heat generation has to be considered.
Important process variables are furnace temperatures at different
points in the riser and the flue gas O content. 2
• Combustion-related
Because
reactions
of the flue gas recirculation and absence of air in oxy
combustion, the concentrations of emission components such as
SOx, NOxand CO will be affected by the combustion mode. This has
the potential to cause changes in the gaseous emissions of power
generation, as well as in the mechanisms and balances of emission
formation reactions.
• Fuel
The fuel input determines the combustion progression and
the emission formation. Knowledge of fuel flow properties such
as heating values, carbon and moisture contents, solids/volatiles
distributions, as well as mass flow accuracies can be used in feed-
forward and model-based control solutions. As the fuel flow is set
separately from the input gas flows, no notable differences between
air and oxy combustion should occur because of the fuel alone.
• Integration of the boiler and supporting units
In oxy combustion, the boiler island depends on the oxygen pro-
duction and CO post-processing 2 units. As a result, coordinated or
plant-wide boiler island control might be of importance. The O 2
is produced with an air separation unit (ASU), while the CO is 2
captured using carbon compression (CCU) and purification (CPU)
units. Dynamic properties such as production rates, startup times
and load following capabilities of these units need to be considered
in the overall control design.
• Water-steam cycle
The water-steam cycle contains the main power plant control
loops, such as live steam temperature control, boiler-turbine unit
control, feedwater control and drum level control. As the heat used
on the water-steam side comes from the combustion and as the

M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219 205
main focus of this work was on hotloop dynamics, the water-steam
control issues in oxy-firing boilers were not discussed in this paper.
• Boiler island in grid control
Special requirements arise, when the boiler participates in grid
frequency or district heating network control. As the focus of this
paper was on the CFB hotloop, these matters were not discussed
here.
Currently oxy combustion is in its pilot testing and early com-
mercialization stage. Both theoretical and experimental research
is being conducted on the CCS process chain by universities and
companies in the field. For example, six demonstration projects are
supported by the European Energy Programme for Recovery (EEPR
2010–2013), with the aim of making CCS zero emission power
generation commercially feasible by the year 2020. One of these
projects is the planned CCS supercritical CFB Compostilla project in
Spain. The necessary technology for this process is currently being
tested at the same location with the CIUDEN 30MW oxy combustion
and CCS test facility. From large-scale general CCS investigations,
the “Special Report on Carbon Dioxide Capture and Storage” report
by the IPCC (IPCC, 2005) is one of the most extensive and it includes
a section on oxy combustion. Aside from solid fuel combustion, oxy
combustion is being researched for other power generation sys-
tems like natural gas burners and gas turbine cycles (e.g. Hasegawa,
2013; Thorbergsson, 2012; Yin, Rosendahl, & Kaer, 2011).
So far, oxyfuel research has mostly considered steady-state
process conditions and the pulverized coal (PC) oxy-coal process.
Although this paper focuses on the fluidized bed combustion tech-
nology, oxy-PC research results offer valuable insights into the
general differences between air- and oxy-firing. Toftegaard, Brix,
Jensen, Glarborg, and Jensen (2010) combined a wide array of oxy-
fuel PC references into an extensive review article focusing on the
differences between air and oxy combustion. Davidson and Santos
(2010) also reported on pulverized fuel oxy combustion and the
overall development of the oxy-firing technology. Wall et al. (2009)
focused on fuel reactivity, combustion characteristics, heat transfer
and emission formation in oxy-PC.
Despite the usefulness of the oxy-PC research results, the CFB
has its own requirements and thus calls for specific CFB refer-
ences. In general, the fluidized bed technology has been widely
documented in the literature; see e.g. Basu (2006). For oxy-CFB,
Czakiert et al. concentrated on combustion kinetics and conver-
sion rates of different fuel components (Czakiert & Nowak, 2010;
Czakiert, Bis, Muskala, & Nowak, 2006; Czakiert, Sztekler, Karski,
Markiewicz, & Nowak, 2010). Duan, Zhao, Zhou, Chengrui, and
Chen (2011) presented results from 50 kW pilot
th
oxy-CFB mea-
surements. The particular focus of these authors was on the input
oxidant O percentage
2
and its effects on the differences between
air and oxy combustion. Practical design issues were considered
by Romeo et al. (2011). Oxy-CFB research from Foster Wheeler
was presented e.g. by Eriksson et al. (2007) and Hack et al. (2008),
who described the air/oxy Flexi-BurnTMtechnology, oxy modelling
studies, pilot and bench scale experiments and conceptual oxyfuel
retrofit designs. E.g. Suraniti, ya Nsakala, and Darling (2009) and
ya Nsakala et al. (2004) discussed the oxy-CFB research work and
experimental testing of Alstom Power.
Few papers related to oxyfuel control design have been pub-
lished up to date, for oxy-CFB in particular. Oxy combustion results
in several changes in the operation of the process which require
attention during boiler control design. Due to a different com-
position of the combustion atmosphere, the furnace temperature
and heat transfer dynamics will become slower. In addition, the
flue gas recirculation in oxy mode introduces internal feedback
dynamics to the system, a feature not found in basic air combustion
(without flue gas recirculation). As modern fossil fuel power
Table
plants
1
The properties of the fuels that were used in the simulation tests.
Components Spanish anthracite Petcoke
Ultimate analysis (wt%, dry)
C 55.2 86.4
H 2.2 3.9
N 0.8 1.7
O 4.4 1.8
S 1.8 5.7
Proximate analysis (wt%)
Moisture 12.1 3.1
Ash (dry basis) 35.6 0.4
Volatiles (dry basis) 10.2 12.8
Heat value (MJ/kg)
LHV (as received) 20.3 34.5
(including oxyfuel plants) have to be able to provide fast responses
to load changes, careful control design is needed. For oxy combus-
tion, switches between air and oxy mode are also an essential part
of e.g. the startup and shutdown sequences of the plant. Some ref-
erences about air-oxy-air switches can be found in the literature
(e.g. McDonald & Zadiraka, 2007; Weigl, 2009). The separate oxy-
gen and RFG gas flow inputs in oxy combustion give more degrees
of freedom for performing combustion control. The investigation
of the specific features of oxy-CFB dynamics and the combustion
control challenges related to the technology form the motivation
for this paper.
After this introduction, the process model used in this paper
and its background experimental research are presented in Section
2. Section 3 deals with oxyfuel static aspects and the steady-state
differences between air and oxy combustion in order to form a
background for understanding oxy-firing process dynamics. Sec-
tion 4 discusses the main differences in the process dynamics of oxy
and air combustion and presents the challenges and possibilities in
the oxy-CFB hotloop control structure. The dynamic simulations
of this work are discussed in Section 5 through switching tests
between air and oxy combustion. Section 6 summarizes the con-
clusions of this work.
2. Experimental setup
A dynamic 1-D Matlab/Simulink hotloop model was used to
investigate the dynamics of the oxy-CFB process. This model has
been developed in cooperation between Foster Wheeler Energia
Oy, the Lappeenranta University of Technology (LUT) and the Uni-
versity of Oulu. A description of the model can be found in Ritvanen
et al. (2012). The hotloop model structure had been previously
validated and used extensively for various air-fired circulating flu-
idized bed boilers of different sizes. In the preparation work for
this paper, a successful initial model validation in oxy mode was
performed using measurement data from an air/oxy-fired pilot
combustor (Tourunen, 2010) with a fuel power of 50–100 kW in
th
oxy mode and 20–50 kW in
th
air mode. The pilot contained a fur-
nace tube (height 8 m, inner diameter 167 mm), a solid material
circulation tube, cyclones for solids and fly ash separation, flue gas
processing equipment, a flue gas recirculation system, as well as
fuel, limestone and oxidant feeding lines. In the testing campaign,
a fuel blend with an approximate 70/30 mass percentage ratio of
anthracite (primary fuel) and petcoke (secondary fuel) was burned
(Table 1). To form the oxyfuel oxidant, RFG from the flue gas line
was mixed with room temperature high purity bottled O ,
2
resulting
in a realistic oxy-firing process configuration. The primary oxidant
was introduced through the grid with primary air preheating for
air mode, while the secondary oxidant was fed from three different
levels in the riser.
The model validation was conducted through air/oxy load steps
and oxy load ramps, using filtered actual input data from the pilot.

206 M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219
Fig. 2. The hotloop module of the air/oxy dynamic model used in this study.
For the measurement campaign, the pilot was equipped with exten-
sive temperature, heat transfer, pressure, solid material sampling
and flue gas composition measurements. The input data included
RFG, pure O and
2
air mass flows, fuel silo weight measurements
and fuel feeding screw RPM values, as well as primary and sec-
ondary oxidant temperatures. The calculation of fuel mass flows
was based on least squares fits from fuel silo weight decreases with
minor modifications based on alternations in the process outputs.
Output measurements used in the validation mainly contained flue
gas composition data and furnace temperatures.
For this paper, separate air-oxy-air switch test simulations were
conducted with the hotloop model. Like the validation cases, the
model was configured according to the pilot plant and thus only
contained the furnace, the gas–solid separator and the solids cir-
culation system. These subsystems were included in the hotloop
Simulink model (Fig. 2), while the calculation codes of the furnace
and the separator had been implemented as C-coded s-functions.
For oxy-firing simulations, a separate input gas mixing module for
mixing the RFG, pure O and
2
air flows to form the primary and sec-
ondary oxidants was also included into the simulator. A pure O
2
flow purity of 96.6 wt% was used for all simulations in this study,
with the rest of the pure O consisting
2
of nitrogen.
The CFB process was modelled using both physical and empir-
ical approaches. The furnace riser tube consisted of 20 ideally
mixed calculation elements, for which element specific mass and
energy balances were solved against time with an ODE solver. A
combined energy equation for the gaseous and solid phases was
defined to solve the element temperatures, while the hydrody-
namics, combustion characteristics, vertical density profile and
heat transfer inside the modules were calculated using empirical
and semi-empirical correlations. The heterogeneous reactions of
carbon, hydrogen and sulphur were considered for the solid fuel
combustion. Hotloop cooling could be applied through element-
specific surface temperature parameters to simulate the effects of
the water-steam cycle. Although the model contained no water-
steam side calculations, it is usually used as the hotloop component
in a complete power plant simulation software application.
The number of hotloop model system states depended on the
process configuration and the inputs. For this paper, 855 states in
total were used. Because of the large amount of states, the model
Fig.
is
3. Simplified input–output structure of the hotloop model.
mainly a simulator for investigating process dynamics and testing
control solutions, and should not be applied directly in e.g. model-
based control. Nevertheless, a state estimation approach for model-
based analysis of an experiment campaign has also been developed
(Ikonen, Kovács, & Ritvanen, 2013). An input–output “black box”
structure of the model is illustrated in Fig. 3.
3. Oxy-CFB combustion, static aspects
The static aspects of oxy combustion need to be considered
before investigating, how oxy process dynamics will differ from
air-firing. This chapter presents the oxyfuel-related changes in the
CFB operation that lead to steady-state differences in heat transfer,
fluidization, combustion and emission formation. Furthermore, the
additional process units needed for oxy combustion are discussed.
3.1. Recirculated flue gas
Replacing the input air with oxygen and recirculated flue gas
(RFG) is the source for the various differences between air and oxy
combustion, although the basic operational principle of solid fuel
combustion remains the same in both combustion modes. In the
oxy-CFB, pure oxygen is required for the combustion, while RFG
serves as the main fluidizing medium. The RFG is essential for the
fluidization, as the pure O volumetric
2
flow rate is much smaller
than the corresponding amount of input air. The other main func-
tions of the RFG are to act as a heat transporting medium and to
bring furnace temperatures to the optimal operating regions (typ-
ically 850–900◦C in CFB) of combustion, heat transfer and bed
sulphur capture. It is important to acknowledge that the cooling and
fluidizing effects of the RFG are opposite: an RFG-based increase
in fluidization simultaneously contributes to lowering the furnace
temperatures. This is different from air-firing, as an increase in the
air input automatically leads to an increased O input,
2
as well. As
the RFG is extracted from the flue gas, the exhaust gas heat loss will
be smaller in oxy mode than in air mode.
A flue gas recirculation system with mixers for mixing oxygen,
RFG and also air during combustion mode switches is mandatory
for the oxy-firing operation. Even though flue gas recirculation can
also be used in air-fired boilers for e.g. temperature control, the
RFG is the main component of the input oxidant in oxy combus-
tion. The flue gas recirculation system can be designed in various
ways, mainly involving the choice of the RFG withdrawal point from
the flue gas line and the operations performed to the recycled flue
gas. The chosen recirculation point affects the RFG composition and
thus the properties of the process input oxidant, as well as the size,
energy and material requirements of flue gas and RFG processing
units. Choosing between a wet and a dry flue gas recycle is espe-
cially important (Toftegaard et al., 2010; Eriksson et al., 2007). Air
leakage into the boiler also needs to be dealt with in the process
chain, as the CO product
2
quickly becomes diluted by nitrogen and
the CO separation
2
difficulty is increased, if air leakage into the
oxyfuel boiler is extensive.
Due to the oxy-firing process configuration, the concentrations
of gaseous components in the oxidant and the flue gas become
markedly different from air combustion (Table 2). Especially the
remarkable increases in CO and
2
H O
2
and the reduction in N
2
should be noted here. As the specific heat capacities of both CO
2

M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219 207
Table 2
Typical concentrations of gaseous components in the oxidant and the flue gas before
water condensing in air and oxy combustion.
Percentage vol.% in gas (wet basis)
Air combustion Oxy combustion
Input oxidant gas O2 21 21–30
N2 79 0–10
CO2 0 40–50
H2O Small 10–20
NOx, SOx No Yes
Flue gas O2 3–4 3–4
N2 70–75 0–10
CO2 12–14 60–70
H2O 10–15 20–25
NOx, SOx Yes Yes
Data from Davidson and Santos (2010).
Fig. 4. Density values for various gaseous components and mixtures at 1 atm and dif-
ferent temperatures, when the ideal gas assumption is used for non-water species.
and H O
2
are higher than that of N (Table
2
3) in the boiler tem-
perature range, the heat capacities of the gaseous flows in the CFB
will increase in oxy combustion. CO also
2
has a larger molecular
weight and density than nitrogen (Fig. 4), resulting in a higher oxy-
fuel oxidant gas density than the density of air. Therefore, if the
nitrogen of air is simply replaced with RFG and the total input gas
mass flow is kept constant, the oxidant gas volume flow will be
smaller in oxy mode than in air mode, which causes a change in
the fluidization conditions. Like in air combustion, the steady-state
composition and thus the physical/chemical properties of the oxy-
fuel flue gas flow will depend on the input fuel feed
However,
properties.
the flue gas recirculation in oxy mode will also link the
oxidant composition to the fuel flow in the oxy-CFB.
3.2. Heat transfer distribution
The oxyfuel oxidant heat capacity and density elevations mean
that furnace temperatures will be lowered, if the heating power or
furnace cooling in oxy mode remains unchanged from air mode.
As the oxidant O contents
2
of Table 2 and research literature indi-
cate, the lower temperature levels can be prevented by oxidant O
2
enrichment, i.e. by controlling the mixing ratio of pure oxygen and
RFG to increase the oxidant O content
2
above the 21 vol.% value
of air. The O percentage
2
required for air-like furnace tempera-
tures depends on several factors, most notably the fuel type and
the flue gas recirculation system. The oxidant O enrichment
2
issue
is elaborated on in Section 3.4.
Since the gas flow through the boiler would not give up heat as
willingly in oxy combustion as in air combustion due to its elevated
heat capacity, combustion heat is transported further downstream
in oxy mode and the heat distribution between heat exchang-
ers might be affected. In general, the conduction of heat further
downstream in the process chain contributes towards an improved
convective heat transfer, while the radiative heat transfer close to
the furnace decreases. Indeed, improved heat transfer efficiencies
at least in the convective section of the boiler have been reported
by e.g. Hack et al. (2008) and IPCC (2005).
Despite the heat capacity elevation, it is difficult to make conclu-
sions about the overall heat transfer differences between air- and
oxy-firing, as heat transfer is influenced by multiple factors. For
convective heat transfer, these include the fluid dynamics of the
system and thus the fluidization (e.g. Reynolds and Prandtl num-
bers), the heat conductivity of the gas and the gas temperatures
of the superheaters (Toftegaard et al., 2010). Moreover, the main
gaseous components of oxy combustion (CO and
2
H O)
2
are radia-
tive species, unlike N in
2
air combustion. This, along with possible
furnace temperature or particle size distribution effects, has the
potential to boost oxy mode radiative heat transfer. Radiative heat
transfer is also not as crucial for the CFB as convective heat transfer
(Romeo et al., 2011). Although the oxy heat transfer is thus going to
be case specific, a potential shift in heat exchanger duties should not
be overlooked, as it might affect the operational points of process
subsystems and bring models used in control outside their validity
regions.
3.3. Combustion and emissions
A basic point of comparison between air and oxy mode is how
the gaseous atmosphere affects the combustion reactions. The com-
bustion progression is determined by the combustion reaction rate
and the oxygen diffusion rate to the particle surface. Basically, the
diffusivity of both oxygen and small hydrocarbons is lower in a
CO -based
2
medium than in an N atmosphere
2
(Toftegaard et al.,
2010; Wall et al., 2009). As a result, oxygen will be less available for
combustion and the volatile consumption rate will be hindered. If
Table 3
Experimental values of gaseous species at 1123◦C.
Quantity Unit Species CO2/N2property ratio
H2O O2 N2 CO2
Density () kg/m3 0.157 0.278 0.244 0.383 1.6
Specific heat capacity (cp) kJ/kmol K 45.67 36.08 34.18 57.83 1.7
Specific heat capacity (cp) kJ/kg K 2.53 1.00 1.22 1.31 1.1
Heat sink (cp) kJ/m3K 0.397 0.278 0.298 0.502 1.7
Mass diffusivity of O2(DO2/species) m2/s – – 1.70E−04 1.30E−04 0.8
Data from Toftegaard et al. (2010).

208 M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219
the oxidant O content
2
is thus kept at 21 vol.% in oxy mode, the
combustion reactions will slow down, the particle heat genera-
tion rate decrease and the amount of unburned carbon potentially
increase because of the diffusivity change and the lowered oxy-
firing furnace temperatures. However, with oxidant O enrichment,
2
the oxygen partial pressure in the furnace will be larger than in
air-firing and the temperatures will increase, resulting in raised
combustion efficiency, reaction rate and char burnout levels (Duan
et al., 2011; Czakiert et al., 2006), although the burnout depends
heavily on the fuel type, as well. Furthermore, carbon gasification
increases in oxy-firing due to the high CO and
2
H O
2
contents in the
gas.
The formation of emission components will be affected by the
flue gas recirculation and the changes in reaction mechanisms. Due
to the accelerated fuel gasification, the formation of CO will be
larger in oxy-firing than in air-firing, although the formed extra
CO will probably be consumed before leaving the furnace (Duan
et al., 2011). Due to the lack of elemental nitrogen from air and
through several specific reaction mechanisms, NOxformation can
be minimized in oxy combustion (Toftegaard et al., 2010). The abso-
lute amount of char and ash will stay approximately similar for
both combustion modes, while the size distribution of the solids
might be altered e.g. by changes in furnace temperatures. So far,
bed agglomeration, slagging and fouling have not presented any
significant problems for oxy combustion in FB boilers.
In fluidized bed limestone sulphur capture, the CO partial
2
pres-
sure and furnace temperature changes in oxy combustion have the
potential to alter the predominant sulphation reaction mechanism
from indirect (first calcinated, then sulphated) to direct sulphation
(Toftegaard et al., 2010). The overall differences between the air
and oxy combustion sulphur capture efficiencies are debated upon.
Additional oxyfuel process requirements come from the possibility
of limestone recarbonation into CaCO and
3
from locally elevated
concentrations of acidic SOxgaseous species.
3.4. Oxyfuel boiler configuration
Because of the different air and oxy combustion oxidant and flue
gas compositions, existing air-fired boiler designs would not nec-
essarily be optimal for oxy-firing from a heat transfer, fluidization
or combustion perspective. Therefore, it should be defined whether
the goal of the design is an oxyfuel retrofit of an existing boiler or an
oxyfuel greenfield plant optimized mainly for oxy combustion. The
target of oxy retrofits is to obtain air-like combustion conditions in
the furnace, as the structure of the oxyfuel power plant will then
differ from air-fired plants with slight modifications only.
In order to produce similar furnace temperatures and tempera-
ture profiles to air-firing in oxy combustion, oxidant O enrichment
2
is needed. In principle, the O content
2
of the oxidant and
furnace
the
temperatures can be increased either by primarily reduc-
ing the cooling RFG flow or by raising the firing power by increasing
the pure oxygen input. Consequently, the latter option results in a
simultaneous increase in the fuel flow and thus a greater heat gen-
eration through combustion. Both of these methods have their own
disadvantages: a smaller RFG flow leads to a smaller input gas vol-
ume flow (RFG is the main gas component) and might thus hamper
the fluidization in the bed, while increasing the pure O input
2
flow
results in higher oxygen production costs. However, as proper flu-
idization has to be ensured at all times in the CFB, the temperature
target will most likely mainly be achieved by increasing the pure
O flow
2
and firing more fuel (Hack et al., 2008).
In oxy greenfield plants with no restrictions from air combustion
compatibility, the oxidant O percentage
2
can be raised well beyond
the values required for air-like combustion conditions, leading to
higher temperatures, smaller entropy losses and potentially a more
efficient combustion with better char burnout and a smaller oxy-
gen excess. If the RFG flow can be reduced to achieve this, the gas
flows and total gas volume in the system will be reduced com-
pared to air-fired boilers, resulting in smaller oxy power plants
with an unaltered firing power. This will lead to reduced construc-
tion costs, thermal radiation heat losses and flue gas recirculation
power requirements. Because of the risks associated with new tech-
nologies like oxy combustion with high oxidant O levels,
2
the first
generation of oxyfuel boilers is likely to consist of modifications of
existing air-fired units.
The notions presented for retrofits can, to some extent, be
applied to dual-firing and oxy-ready boilers, which strive for the
process to function well in both air and oxy mode. Beside new tech-
nology risk mitigation, these solutions offer operational flexibility
regarding the power demand and the prices of emission rights. The
Foster Wheeler Flexi-BurnTMboiler (Fig. 5) is one example of a flex-
ible air/oxy boiler technology. As both air- and oxy-firing are used,
switches between air and oxy combustion and also between dif-
ferent oxy-firing oxidant O percentages
2
are an integral part of the
operation. Air-firing is also used in retrofits during startups and
shutdowns of the boiler.
3.5. ASU, CCU and CPU
On a plant-wide scale, the major differences between air and
oxy combustion come from the oxy-firing pre- and post-processing
units, namely the ASU, CCU and CPU. The necessary processing steps
and product quality requirements in the carbon compression and
purification units (CCU + CPU) are largely determined by the uses
and storage methods of the CO .
2
The CCS flue gas processing will at
least require a stage-wise compression of the gas to high or even
supercritical pressures, dehydration, cooling and non-condensable
species removal. The input oxygen is usually produced with one or
Fig. 5. Schematic of a Flexi-BurnTMCFB power plant (Foster Wheeler Energia Oy, 2012).

M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219 209
Fig. 6. Air/oxy-CFB output power distribution example.
Data from ya Nsakala et al. (2004).
several parallel air separation units (ASU), which will typically be
based on cryogenic distillation of air, when considering the current
industrial scale O production
2
options.
The ASU, CCU and CPU are perhaps the most important chal-
lenge of the oxyfuel development, as the high pressures and low
temperatures in oxygen production and CO compression
2
require
a lot of energy and thus have a negative effect on the power plant net
efficiency (Fig. 6). This applies especially to the ASU, which might
cause the power plant efficiency to drop 7–9% and be responsible for
60% of the additional energy requirement of CCS (Toftegaard et al.,
2010). The operating costs of the ASU, CCU and CPU are influenced
by the purity of the produced oxygen and the RFG withdrawal point
in the flue gas line, forming an optimization problem between air
separation and post-processing costs. The oxygen production limi-
tations in the ASU might also restrict the performance of the boiler,
as current air separation solutions are only able to reach a load
range of 60–100% and a maximum ramp rate of 3%/min (Toftegaard
et al., 2010). The startup time of the ASU also needs to be considered.
4. Dynamic aspects and control: differences between air
and oxy combustion
The main differences in the process dynamics and control of
air and oxy combustion can be examined from three different
angles. Firstly, the altered gaseous atmosphere composition affects
the heat transfer, combustion reactions and emission formation in
the bed. Secondly, the flue gas recirculation introduces dynamic
aspects to the process, which need to be considered in oxy com-
bustion control. Thirdly, the possibility to adjust the input oxygen
and RFG flows separately gives an additional degree of freedom for
process control. These differences present challenges and possibil-
ities for the oxy-CFB control and will be discussed in detail in this
section.
4.1. Oxidant and combustion atmosphere
The most important effect of the oxidant and flue gas composi-
tions on the oxy-CFB dynamics are derived from the increases in gas
specific heat capacity and density in oxy mode. The elevated heat
capacity will cause the gas flow inside the oxyfuel boiler to heat
up and cool down more slowly than in air combustion, resulting in
slower temperature transients and thus slower process
Fig.
responses
7. Normalized furnace temperature responses at different riser heights (T) of
air combustion (upper) and oxy combustion (lower) load step simulations, hotloop
model validation simulations.
to load changes. The slower oxy-firing transients are demonstrated
in the load step simulations of Fig. 7. As the furnace temperatures
are directly connected to the heat transfer and water-steam cycle
of the power plant, the indicated changes will most likely be vis-
ible in the time constants and settling times of the process MW
responses, as well. The slower temperature dynamics can be con-
sidered as a disadvantage for the load following capabilities of oxy
control and special attention should be paid to the selection of the
combustion control structure, as the slower dynamics might have
to be compensated with adjustments to the furnace cooling or fuel
firing power.
The effect of the oxidant gas density on fluidization is a point
of concern in the oxy-CFB switching control. The oxidant density
increase in oxy mode presents an optimization problem between
the particle residence time and the fluidization efficiency. As indi-
cated in Fig. 4, the gas densities in air and oxy mode will also
respond differently to temperature changes. The oxidant density
effects can be summarized with the following points:
• If the oxidant mass flow is kept constant during a switch from
air to oxy combustion, the gas volume flow will decrease due to
its elevated oxy mode density. This means that without sufficient
control measures the velocity of the fluidizing gas will decrease,
which will hamper the fluidization in the bed by decreasing
the turbulence and the mixing efficiency of solids. However, the
smaller gas velocity will also contribute to a longer residence time
of solids and thus potentially even to a better burnout.
• If the gas volume flow is kept constant during the air to oxy switch
by adjusting the RFG and pure O feeds
2
to compensate for the gas

210 M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219
density increase, a denser oxyfuel oxidant with a similar velocity
to a corresponding air flow will be able to carry solids better in the
riser and improve fluidization. Similarly, this mode of operation
could lead to smaller residence times and larger solids circula-
tion amounts, as well as larger pressure difference requirements
and thus an increased energy demand of the input gas feeding
equipment.
In practice, the best way to run the switches will most likely be
to maintain a constant gas volume flow at least for the primary oxi-
dant in order to ensure a proper fluidization throughout the switch.
Furthermore, the residence time of the fuel will have a small impor-
tance in the CFB because of the solids circulation in the hotloop. The
overall effect of the oxidant on the residence time also does not
seem to be straightforward and contradictory results have been
presented in the literature.
The changes in the oxidant properties affect the oxy-CFB process
dynamics and should be considered in its control design, as mea-
surement and control components might need to compensate for
the property differences. The task is especially problematic dur-
ing load and combustion mode transitions due to the alternating
gaseous component concentrations. This could lead to an adap-
tive control system, a lookup-table based feedforward solution or
even online calculations. The effects of oxy-firing on heat transfer
and fluidization depend on the fuel feed properties (see Section
3.1). However, as the dominating effect is caused by the elevated
CO and
2
H O
2
contents in the gaseous flows, the fuel type consid-
erations can be omitted in this context from a process dynamics
point of view. Compared to air-firing, the gas property changes
also call for additional strategies for selecting the level of oxi-
dant O enrichment,
2
handling possible heat transfer distribution
changes in the steam generation and ensuring proper fluidization
at all times. The special requirements of oxy-firing become espe-
cially apparent for retrofits, which are based on air-like combustion
conditions.
4.2. Flue gas recirculation
The dynamics of the flue gas recirculation mainly concern
oxidant and flue gas component concentrations, although gas com-
positions are also related to other furnace properties, as described
in the previous chapters. The RFG is a combustion reaction product
of the process and because it is also the main component of the
oxyfuel oxidant, the fluidization and heat transfer are more linked
to the combustion in an oxy-CFB than in air-firing. However, at
the same time the degree of fluidization greatly affects the com-
bustion and heat transfer in the boiler. This kind of a cause-effect
relation introduces new dynamic aspects to the oxy-CFB process. As
the recirculation links the oxidant to the fuel feed properties, varia-
tions in the fuel quality will cause different responses in the furnace
outputs compared to air combustion. Apart from the recirculation
itself, additional features to the total process dynamics might be
presented by O /RFG/air
2
mixers.
For control engineering, the most crucial flue gas component
is oxygen, as the flue gas O contains
2
information about the com-
bustion in the furnace. Because of the flue gas recirculation in oxy
combustion, the total oxygen input is a combination of pure O
2
from the ASU and RFG O from
2
the flue gas. However, at low fre-
quencies the actual oxygen demand of the process is unaffected by
the recycled oxygen, as the required O amount
2
is determined by
the corresponding fuel flow and the set O excess.
2
The hotloop and
the RFG system can be viewed as a combined process, in which the
flue gas recirculation is an internal circulation of gaseous compo-
nents in the CFB furnace. Consequently, the required O amount
2
is
determined by the mass balance of this
Like
system.
the flue gas O ,
2
the steady-state values of other flue gas
components are not affected by flue gas recirculation, as indi-
cated by the RFG step simulations of Fig. 8. This is dictated by the
input–output mass balances of the system. However, the recircula-
tion amount and the changes in the RFG have an effect on the flue
gas composition dynamics, for example on the settling times of flue
gas composition responses (Fig. 9). From these viewpoints, the flue
gas recirculation system once more has analogies with an inner cir-
culation, although the gases in the RFG line are not in active contact
with the solid bed. It should be noted that the steady-state compo-
sitions remain constant with different RFG amounts only when no
flue gas components are removed outside the mass balance bound-
ary as a result of RFG processing. In Fig. 8, this was observed to a
minor degree due to SO removal
2
from the RFG. The RFG amount
might thus become significant for oxy-firing steady-states, if e.g.
H O
2
is removed from the RFG line in a dry flue gas recirculation.
The feedback nature of flue gas recirculation will cause both
additional flue gas composition dynamics and larger time constants
during load or process operation changes. Furthermore, the delay
of the firing system will increase, as a change in the combustion
reactions will not immediately be visible in the input oxidant com-
position. The distance of the flue gas recirculation point from the
furnace thus not only influences the flue gas processing require-
ments, but also the process time delay for combustion-related
changes. In general, controlling oxidant properties is difficult in
oxy-firing, because changes in the combustion or fuel quality will
also have an indirect effect on the oxidant quality. This has the
potential to cause accumulation or even stability issues for the
combustion, if controlled poorly.
The delay and dynamics of flue gas recirculation become visi-
ble during air-oxy-air switches, in particular. Based on the results
of Weigl (2009), the most important changes in flue gas compo-
nent concentrations during a switch seem to occur only after the
actual switch or during the last stages of the transition ramps of air,
pure O and
2
RFG, forming an s-shaped figure in the concentrations.
This would suggest that special attention should be paid to the last
stages of the transitions and that quick gas flow ramps would be
useful in order to obtain the full oxy combustion steady-states as
quickly as possible.
Unlike the switch dynamics, hotloop model load test validation
simulations showed no major effects related to flue gas recircula-
tion for flue gas composition responses. The flue gas O in
2
oxy mode
behaved in a similar way to air combustion and no large changes in
the CO and
2
H O
2
were seen as a result of load steps and ramps. The
results indicated that the crucial control parameter of the flue gas
composition dynamics is the RFG/pure O ratio
2
rather than sim-
ply the O input.
2
These findings were also supported by literature.
When the goal is to alter the fluidization and the firing power in the
same way to reach different load levels, the oxidant composition
and thus the RFG/pure O ratio
2
should remain similar on all opera-
tional levels. As a result, the dynamics of the flue gas recirculation
should not disturb the process in these cases.
4.3. Separate control of oxidant components
In oxyfuel boilers, the oxygen supply is independent from the
RFG flow, meaning that both the pure O from
2
the ASU and the RFG
from the process can be adjusted with their own control structures.
This gives an additional degree of freedom to the oxy-CFB control
design compared to air-firing, which uses a single oxidant compo-
nent with an unaltered gas composition. As a result, it is possible
to use oxidant O contents
2
differing from air and to alter the oxi-
dant O percentage
2
during the operation in oxy mode. In a way, the
oxygen supply, temperature and fluidization become decoupled to
some degree: the pure O flow
2
is connected to the combustion,
while the RFG is mainly responsible for adjusting temperatures

M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219 211
Fig. 8. Normalized simulated flue gas O2, CO2and H2O responses, furnace temperatures and bed/freeboard velocities for RFG step changes in oxy combustion with a constant
firing power (constant fuel and pure O2flows).
and fluidization. For example, zone-wise fluidizing RFG flows could
be used during load changes to speed up furnace temperature
dynamics and to obtain a more uniform temperature profile with-
out directly affecting the combustion. These kinds of considerations
introduce entirely new control tasks for solid fuel combustion.
In oxy combustion, the freedom to control the pure O sep-
2
arately from the RFG can be used in flue gas O or
2
oxidant O
2
control. In flue gas O feedback
2
control, one or several pure O or
2
oxidant flows are adjusted according to the measured flue gas O
2
percentage. A flue gas O trim
2
is often compulsory for combustion
processes. Like air combustion, the most reasonable flow to be used
for flue gas O control
2
is most likely the secondary pure O or
2
oxi-
dant flow, so as not to disrupt the fluidization or the combustion.
These control ideas have been illustrated on a conceptual level in
Fig. 10, which shows the flue gas O control
2
concepts separately
from other hotloop control
Since
loops.
the pure O can
2
be controlled independently from the RFG,
flue gas O control
2
alone will result in a time-variant input oxidant
O percentage
2
in oxy combustion, which might be undesirable for
the process operation. Oxidant O control
2
concepts (Fig. 11) can
be used in oxy combustion to maintain the input oxidant O per-
2
centage. The oxidant O is
2
often regarded as a significant process
parameter, as it is connected to the pure O /RFG
2
ratio and thus the
relation between furnace cooling and heat generation. Moreover,
the input oxidant O concentration
2
contains information about the
flue gas O content
2
because of flue gas recirculation. Oxidant O
2
control is especially important from a safety point of view, as hand-
ling gaseous flows with high oxygen contents together with small
fuel particles or oxidant preheating might pose risks for the solid
fuel power plant. Oxidant O control
2
is essentially a feedforward
control solution, as its aim is to supply an oxidant stream with a
certain O percentage,
2
regardless of its effect on the combustion.

212 M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219
Fig. 9. ±1% and ±5% settling times (time steps) of flue gas CO2, H2O and O2contents
with different flue gas recirculation rates, when the fuel mass flow was decreased
with a 10% step. “RFG kg/s” is the nominal RFG mass flow value for the respective
load level.
The oxidant O content 2 can be maintained by adjusting either
the pure O flow
2
or the RFG flow. As stated in Section 3 (also illus-
trated in Fig. 11), the oxidant O percentage
2
should preferably be
adjusted with the pure O flows
2
and by modifying the fuel input
accordingly. However, controlling the oxidant O without
2
consid-
ering the changes in the fluidization might not be enough for the
CFB operation. As a result, it might be necessary to control the
input gas flow rate beside its O content
2
in oxidant O control.
2
A
combined flue gas O ,
2
oxidant O and
2
total oxidant flow control
structure (Fig. 12) would offer a convenient way to control the oxy-
gen input, the combustion and the fluidization in the boiler, even
though attention must be paid to conflicting control actions in this
solution. Oxidant O control
2
could also be applied only to certain
input gas flows.
In oxy combustion, the oxygen excess is easier to maintain at
a desired level than in air combustion, as the pure O flow
2
can be
determined based on the fuel requirement of the load level, while
Fig. 10. Flue gas O2control concepts in oxy-CFB. The secondary pure O2(a) and
the secondary oxidant (b) are used to control the flue gas O2content. The control is
displayed on a conceptual level and the figure only shows the flue gas O2control,
excluding other hotloop control
Fig.
loops.
11. Example of an oxidant O2 control concept in oxy-CFB. The primary and
secondary pure O2flows are used to control the respective O2contents. The control
is shown on a conceptual level and the figure only displays the oxidant O2control,
excluding other hotloop control loops.
the RFG flow can be set according to the desired CFB gas velocity.
It is also important to note that the excess air supply of air-firing
differs from the excess in oxy-firing, as the  parameter has to be
selected in a different way for a pure O flow
2
with no N and
2
as flue
gas recirculation reduces the flue gas flow in the boiler. O excess
2
considerations are important in oxy combustion, because too high
 values carry an ASU oxygen production energy penalty.
One particular advantage and challenge for oxyfuel control is
presented by the possibility of using different oxygen concen-
trations for different oxidant inlets (primary air, secondary air,
etc.). This is called oxidant O staging
2
and it can be used in oxy
combustion to provide improved furnace profile control for e.g.
Fig. 12. Concept for input oxidant control: combined flue gas O2, primary oxidant
O2and total input oxidant flow control. The gas volume/mass flow measurement
can be designed in various ways. The control is illustrated on a conceptual level and
the actual implementation is not considered here.

M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219 213
Fig. 13. Oxidant O2staging concept for adjusting riser temperature profiles. The
primary oxidant O2content is used to modify the dense bed temperature, while
the secondary oxidant O2content controls the freeboard temperature. The solu-
tion is shown on a conceptual level: no other control loops are included and the
implementation of control loops or measurements is not considered.
temperatures and heat transfer (Fig. 13). Through oxygen staging,
the main combustion zone can be shifted along the bed, which
affects the principal burning zones of volatiles and char, as well
as the oxidative and reductive potentials of the bed. When a low
oxidant O level
2
is used in the dense bed, char ascends higher
up in the riser, leading to a more uniform riser temperature pro-
file, but possibly also to increases in unburned fuel, the flue gas
O content
2
and exhaust gas heat losses. An elevated O content
2
of the primary oxidant, on the other hand, prolongs the contact
between the fuel and the oxygen, improving the combustion effi-
ciency, but also increasing the temperature differences along the
furnace (Duan et al., 2011). If oxygen staging is used in the hot-
loop control, it has to be taken into account in the boiler O control
2
designs and it should not clash with systems such as flue gas O
2
control.
Oxidant O staging
2
could be used to selectively assist load tran-
sitions in certain parts of the riser. This might be important for
load changes with slow and large responses in the furnace tem-
peratures and the heat transfer, as was hinted by the oxy-ramp
hotloop model validation simulations. Interestingly, oxygen can
also be fed directly into the oxy-firing furnace bed to perform more
extreme operations related to combustion and temperature con-
trol (McDonald & Zadiraka, 2007). This oxygen boost might help
to increase the speed of transitions between combustion modes or
load levels and provide a significant advantage in oxy combustion
compared to air-firing.
The oxyfuel oxidant temperature presents additional variation
to the furnace temperatures compared to air-firing, as the oxidant
is a mixture of low-temperature oxygen and RFG from the process
flue gas line, much unlike an air flow. If extensive air flow preheat-
ing or RFG cooling is not used to make the gas temperatures similar
in both combustion modes, oxidant temperature differences will
almost certainly occur. Preheating is often not an option in oxy
mode due to safety aspects of handling pure oxygen flows or oxi-
dants with elevated O percentages.
2
The oxidant temperature issue
might be especially problematic during air-oxy-air switches, as the
RFG is a reaction product of the process, leading to potential oxidant
temperature changes during the switch. The oxidant temperatures
will further be reflected in the furnace
Fig.
temperatures.
14. Air to oxy switch schematic with matching ramp speeds and starting times
for all inputs.
It is evident that the number of control possibilities for the oxy-
CFB plant will increase compared to air-firing. The flue gas O ,
2
oxidant O and
2
total gas flow controls can be combined in various
ways and the oxyfuel oxidant components can be used to adjust dif-
ferent furnace properties. This will complicate the overall control
structure of the power plant and make control design more chal-
lenging. In a sense, the SISO control problem of air-firing becomes
more of a MISO problem in oxy mode. One approach to facilitate
the design could be to put more emphasis on controlling input
oxygen mass flows instead of the total oxidant flows and their O
2
percentages, as the oxidant O percentage
2
alone offers no definite
information about the actual oxygen input to the process. This was
pointed out by Fig. 8, as the flue gas O base
2
level remained constant
throughout the testing despite the significant changes in the oxi-
dant O percentage.
2
The oxygen mass flow control concept would
potentially lead to a more straightforward control solution.
4.4. Switch dynamics
One specific point of concern in the control of the oxyfuel
oxidant components lies in the air-oxy-air switches and in the tran-
sitions between oxy modes with different oxidant O contents.
2
These tasks are especially challenging, as up to three different
gaseous inputs (oxygen, RFG and air) and the solid process flows
Fig. 15. Normalized furnace temperature responses at different riser heights (T) for
two oxy load ramp sets (ramp to a lower load level and back, similar load change),
hotloop model validation simulations. The input flow ramping speeds of set (2) were
three times larger than those of set (1).

214 M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219
(at least one fuel flow and limestone) need to be adjusted simulta-
neously. Furthermore, the sequence of the input adjustments has
to be determined, which is more complicated in oxy-firing than
with an air input flow. The relation between the solid and gaseous
inputs is especially important. As a result, input flows need to be
coordinated in order to keep process variables at their desired val-
ues and achieve stable combustion mode transitions.
Switching between air and oxy mode requires great care, as
fast switches have a tendency to cause rapid changes in furnace
temperatures and FB velocities (Romeo et al., 2011), which may
disturb the process operation. At the same time, switches should
also be performed with a required speed, especially when they are
based on load demands or cost factors. Fast transitions between
combustion modes are also attractive, as the major changes in the
flue gas composition take place at the end of the switch ramping
(see Section 4.2). The control problem is further complicated by the
possible interactions between the switching schemes and the con-
trol loops of the process. This might produce unexpected responses
and limitations to the switch, which might require decoupling or
feedforward control actions.
Testing different switching methods is an integral part in the
characterization of oxy-CFB process dynamics. Switches between
air and oxy mode can be conducted in different ways by varying
the slopes and starting times of gaseous and solid input transi-
tion ramps between combustion mode steady-states. The switching
scheme often contains one main gaseous flow ramp, during which
the major changes in the air, pure O and 2 RFG take place. Ramping
sequences with similar ramping speeds for all gaseous flows seem
to be common in the literature (Fig. 14). In these sequences, the
fuel/oxidant O ratio 2 remains constant throughout the switch.
Beside combustion mode switches, the sequencing of process
inputs needs to be configured for oxy load changes, as well. For
example, it was discovered during oxy load ramp simulations that
a fast ramping of process inputs did not necessarily produce a
faster temperature response compared to slower ramps. Fig. 15
shows that even though the temperature time constant for the
faster ramp set (2) was smaller than for the slower ramp set (1),
the response settling time was actually longer for the faster ramps
than for the slower ones. It was suspected that the low reactivity
of anthracite-based fuels and the simultaneous change of fuel, RFG
and O flows
2
made the furnace cooling change faster than the com-
bustion heat generation during the ramps, creating a momentary
imbalance between these two factors. This would have the poten-
tial to slow down the response, and the effect would be more visible
for fast ramps with rapid RFG transitions than for slower
5.
ones.
Simulations of switches between air and oxy combustion
Air-oxy-air switches present challenges for CFB process control
due to their influences on the combustion dynamics. The switches
should ensure good fluidization, combustion and heat transfer con-
ditions, and be sufficiently fast for flexible dual-firing operation. In
this section, switching schemes between air and oxy combustion
are examined with the dynamic 1-D hotloop model.
5.1. Test setup
The simulated switching schemes from air-firing to oxy-firing
were derived from pilot tests. In all simulations, the starting state
was air combustion and the target state full oxy mode with oxidant
O enrichment.
2
The pure O input
2
was mainly used for oxidant O
2
enrichment and the elevated pure O flow
2
was accompanied by
an increase in fuel power. Different oxidant O percentages
2
above
21 vol.% (typically 28 vol.%) were examined in oxy mode to obtain
air-like combustion temperatures. In the tested switches, the nor-
mal volumetric flow rate (in STP conditions) of the total input gas
flow was kept constant. Apart from the final oxy-firing states, a
switching scheme could include possible intermediate states for
the fuel flow and the oxidant O content.
2
In the switching schemes reported here, a “direct” ramp was
compared to a “sequenced” approach to investigate the relation
between gaseous (pure O ,
2
RFG, air) and solid inputs (fuel and
limestone). In the “direct” method (Fig. 16), the solid feeds were
ramped together with the pure O ,
2
RFG and air flows. All ramps
were started and ended at the same time, making the method fast.
In the “sequenced” method (Fig. 17), the RFG, pure O and 2 air flows
were first ramped from air (21 vol.% O )
2
to oxy mode without oxi-
dant O enrichment.
2
After the main gas flow ramps, the oxidant
O content
2
and the solid feeds were raised to their full oxy mode
setting.
The minor anomalies in the sequences of Figs. 16 and 17 were
due to the pilot testing practical implementation and they were
also reflected in the simulation test runs. Similarly, the fuel power
level increase in the “sequenced” method was simulated with a few
small steps in the fuel mass flow. Note that analysis of the pilot test
outcomes is outside the scope of this paper.
5.2. Simulation results
The two switching schemes resulted in significantly different
process responses. The “sequenced” scheme was more affected by
Fig. 16. Input flow setpoints of the “direct” air to oxy switch method. The fuel flow was increased simultaneously with the main gas flow ramps. The normalized inputs
correspond to percentages.

M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219 215
Fig. 17. Input flow setpoints of the “sequenced” air to oxy switch method. The fuel was increased gradually after the main gas flow ramping. The normalized inputs correspond
to percentages.
the oxyfuel gaseous medium specific heat capacity elevation than
the “direct” method (Fig. 18). As the CO and
2
H O
2
concentrations in
the oxidant increased, the furnace temperatures slowly decreased
for the “sequenced” switch. The lowest temperatures were
observed during the final stages of the main gas flow ramps before
the oxidant O content
2
elevation and the temperatures
their
regained
original levels, when the fuel steps were performed. This illus-
trated the phenomena discussed in Sections 3 and 4. In the “direct”
scheme, the change in the fuel firing rate was conducted simul-
taneously with the shift in the atmospheric conditions. Therefore,
the temperature drop associated with the heat capacity increase
was compensated. The transition in the furnace temperatures from
Fig. 18. Simulated furnace temperatures of different riser calculation elements (T) for the “direct” and “sequenced” switch simulations, normalized by the global furnace
temperature maximum.

216 M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219
Fig. 19. Simulated bed/freeboard velocities and solids densities of different riser elements (points 1 and 2, point 1 located lower than point 2) for the “direct” and “sequenced”
switch simulations, normalized by velocity and global density maxima in the furnace.
air to full oxy mode was smooth and the full oxy-firing steady-state
temperatures were reached faster than in the “sequenced” method.
In both switching schemes, the deviations between different
temperatures in the CFB riser increased in oxy combustion com-
pared to air combustion. This was most likely caused by the
different input oxidant temperatures in air- and oxy-firing. In oxy
combustion, the primary and secondary oxidants had the same
temperatures, while primary air preheating was used in air mode.
The lower secondary air temperature thus led to a more even tem-
perature profile in air mode than in oxy mode. E.g. oxidant O
2
staging could be used as a solution for this issue in oxy mode.
The simulations indicated that it was possible to achieve oxy
mode combustion temperatures comparable to those of air mode,
if oxidant O enrichment
2
was used. With the selected fuel type,
the oxidant O concentrations
2
of the “sequenced” method were
close to the ones required by air-like furnace temperatures. The
final temperatures of the “direct” scheme were higher than this due
to its slightly higher oxidant O enrichment
2
level. The heat transfer
power values for the various riser elements followed the trends in
the furnace temperatures.
Fluidization during switches was analyzed by examining the
gas velocities in the bed and the freeboard, as well as the respec-
tive solid material densities (Fig. 19). In general, the gas
remained
velocities
relatively constant throughout the switches, ensuring
proper fluidization conditions. The solids densities were in close
agreement with the velocities: whenever the gas velocity increased,
the dense bed solids content decreased and the densities higher up
in the riser increased.
On closer inspection, the “direct” method seemed to produce
better fluidization conditions than the “sequenced” switch. The
small density and velocity variations during the switch were also
less monotonous in the “direct” method than for the “sequenced”
switch. The “sequenced” scheme showed a reduction in fluidiza-
tion at the end of the main gas flow ramps, although the input
gas normal volumetric flow rate remained constant. The changes
in the fluidization could be addressed to the observed drop in fur-
nace temperatures before the oxidant O enrichment,
2
as the actual
input gas volume flow entering the process was altered due to
thermal expansion. This highlights the importance of keeping fur-
nace temperature levels constant during the switch. The changes in
the fluidization were mostly dictated by the furnace temperatures
rather than the oxidant temperatures.
A flue gas and oxidant density increase in oxy mode was clearly
observed for both switching methods (Fig. 20). The differences
between the methods were quite small, as the main density changes
took place during the main gas flow ramps and the densities

M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219 217
Fig. 20. Flue gas densities (calculated with the ideal gas law and water-steam tables), input primary oxidant mass flows and flue gas CO2contents for the “direct” and
“sequenced” switch simulations, normalized by the respective maxima.
showed a non-linear response to the switches. The results also dis-
played that maintaining a constant oxidant volumetric flow caused
an increase in the gas mass flow. However, any effects the density
changes had on the fluidization were not directly visible in Fig. 19.
The flue gas CO and
2
H O
2
responses were very similar for the two
methods and the component concentrations especially increased
towards the end of the gas flow ramping. The flue gas SO marked
2
no preference between the switching methods.
The flue gas O contents
2
(Fig. 21) remained largely constant
during both switches and the differences between the methods
were small. Since the combustion of fuel was not radically affected
by the shift in the atmosphere, air-like combustion conditions
could be obtained in oxy mode. The small variability in the flue
gas O was
2
particularly surprising for the “direct” scheme, which
included rapid and large changes in the process inputs. Some
flue gas O drops
2
could be observed during the oxidant adjust-
ments prior to the main gas flow ramps, when air was replaced
by RFG with a significantly lower O content.
2
This illustrated the
fact that air, pure O and
2
RFG need to be considered as a com-
bined gaseous input during the switch rather than as individual
flows.
On a whole, the switch simulations indicated that feasible tran-
sitions between air and oxy mode can be performed in CFB boilers.
The main differences between the methods were observed in the
furnace temperatures, as the fluidization properties were linked
the
to
temperatures. The flue gas O content
2
behaved similarly for
both switching schemes and indicated similar oxy-firing combus-
tion conditions to air-firing. The other flue gas emission responses
were very similar for both schemes.
The “sequenced” method resulted in a rather slow combustion
mode switch with an intermediate drop in furnace temperatures,
which was connected to the elevation in the gas specific heat
capacity. The “direct” method resulted in smoother and faster tem-
perature responses than those of the “sequenced” method and the
drop in furnace temperatures could be compensated with the fir-
ing power. “Direct” switching can turn out to be especially useful
for rapid transitions, when requirements for combustion and heat
transfer are high (e.g. cost/demand-based switches). However, the
extensive adjustments to the manipulated variables of the “direct”
method might be restrictive in real-world applications. This was
already hinted during pilot experiments, with partial clogging of
the boiler grid and setpoint tracking problems for the RFG. The
simultaneous ramping of all inputs may be more sensitive to pro-
cess disturbances and more challenging to conduct than a gradual
switch. The “sequenced” method thus has potential for startups and
shutdowns, when the speed requirements are less strict and when
simultaneous input changes are not necessarily feasible. In the sep-
arate fuel and gas flow ramping, particular attention has to be paid
on the last stages of the oxidant ramps because of the changes in
the gas specific heat capacity and the furnace temperatures.

218 M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219
Fig. 21. Flue gas and oxidant O2concentrations for the “direct” and “sequenced” switch simulations, normalized by the oxidant O2percentage maximum.
6. Conclusions
This paper investigated the differences between oxy- and air-
firing in circulating fluidized bed (CFB) boilers. Specific oxy-firing
CFB combustion control features and process dynamics were
highlighted. Both static and dynamic aspects of the process were
investigated through physical considerations and dynamic hotloop
simulations. In particular, oxy-CFB control structures were dis-
cussed. Two switching methods between air- and oxy-firing were
examined through simulations, with the focus on determining how
combustion mode transitions should be carried out in the CFB.
The oxidant and flue gas specific heat capacities and densities
will be elevated in the oxyfuel boiler compared to air-firing due
to the higher gas CO and
2
H O
2
contents. The increase in the heat
capacity leads to lowered furnace temperatures, slower temper-
ature responses and possible shifts in heat exchanger duties. The
temperature level changes can be compensated by increasing the
pure O and
2
fuel inputs in oxy mode, i.e. through oxidant O enrich-
2
ment. To maintain a similar fluidization in air and oxy mode, the
input gas volume flow should be kept constant during combustion
mode transitions. The oxyfuel atmosphere also influences the com-
bustion and emission formation, e.g. by reducing the diffusivity of
oxygen and small hydrocarbons and by increasing fuel gasification.
Flue gas recirculation introduces specific process dynamics to
oxyfuel boilers, as the RFG is both a reaction product and the
component
main
of the oxidant flow. The recirculation will add to the
time delay of the system and introduce an internal feedback to
the process. Although steady-state concentration levels are not
affected by the flue gas recirculation amount, the RFG flow deter-
mines the concentration dynamics. This is particularly important
for air-oxy-air switches, and the RFG/pure O ratio
2
is also an impor-
tant control parameter for load changes in oxy combustion.
The possibility to adjust the RFG and pure O inputs
2
separately
from each other introduces an additional degree of freedom for
oxy-CFB control. The RFG is mainly responsible for fluidization and
furnace cooling, while the pure O input
2
is regulated by the fuel fir-
ing power. Separate pure O and
2
RFG flows enable a more accurate
and zone-wise control of furnace properties, profiles and dynamics,
including the possibilities to use varying oxidant O percentages,
2
different oxidant O contents
2
for different inlets (O staging),
2
as
well as oxygen boosts or extra RFG flows during load or combus-
tion mode transitions. On the other hand, the separate oxidant
components call for more advanced combustion control solutions,
increasing the complexity of the overall power plant control struc-
ture. One comprehensive way to design the combustion control in
the oxy-CFB would be to combine a flue gas O trim
2
with oxidant
O control
2
and total oxidant volume flow control.
For air-oxy-air combustion mode switches, the most important
thing to consider is how the fuel, limestone, pure O ,
2
RFG and air
flows should be altered to obtain optimal combustion, fluidization

M. Hultgren et al. / Computers and Chemical Engineering 61 (2014) 203– 219 219
and heat transfer conditions throughout the switch. Particular
attention has to be paid to the relation between solid and gaseous
flows. Based on the simulation results, fast “direct” transitions
between air- and oxy-firing with simultaneous ramping of all input
flows should be used whenever possible. This switching method
produced smooth temperature transitions with no decreases in fur-
nace temperatures or deterioration of combustion and fluidization
conditions. However, these switches may be challenging to per-
form correctly. If “direct” switching results in changes that are too
extreme for the process, the fuel flow should be altered only after
the main gas flow ramping. With this “sequenced” method, a drop
in the furnace temperatures due to the elevated oxyfuel oxidant
heat capacity should be expected at the end of the main gas flow
ramping. This decrease will also be reflected in the fluidizing gas
velocities due to temperature effects on the oxidant volume flow.
Air-fired combustion control cannot be applied directly to the
oxy-CFB, as the specific features and dynamics of oxy combustion
need to be considered in the control design and tuning. Indeed,
oxy combustion presents both challenges and advantages for boiler
control. Future oxy-CFB control research will involve implemen-
ting control solutions for the process and investigating new control
possibilities e.g. by ramping oxidant components in different ways
during load and combustion mode transitions. Oxy-CFB control
should also be analyzed on a plant-wide scale, as the greatest chal-
lenges for the technology are derived from the operating costs,
efficiency penalties and performance restrictions of oxygen pro-
duction (ASU) and CO processing 2 units (CCU + CPU). Furthermore,
as the oxyfuel gaseous atmosphere influences heat transfer in the
boiler, water-steam side modelling should be included in the oxy-
firing power plant simulations.
Acknowledgements
The authors would like to acknowledge the cooperation
between the University of Oulu and Foster Wheeler Energia Oy
(Varkaus, Finland). Funding has been received from the Gradu-
ate School in Chemical Engineering (GSCE). The research leading
to these results has received funding from the European Com-
munity’s Seventh Framework Programme (FP7/2007–2013) under
grant agreement no. 239188. For the experimental research related
to previous hotloop model validation, acknowledgements go to the
VTT Technical Research Centre of Finland (Jyväskylä, Finland). The
work of the Lappeenranta University of Technology (LUT) has been
important for the hotloop model development.
References
Basu, P. (2006). Combustion and gasification in fluidized beds. Boca Raton: CRC Press,
Taylor & Francis Group.
Czakiert, T., & Nowak, W. (2010). Kinetics of coal char combustion in oxygen-
enriched environment. In G. Yue, H. Zhang, C. Zhao, & Z. Luo (Eds.), Proceedings
of the 20th international conference on fluidized bed combustion; 2009 May 18–21
(pp. 618–623). Xi’an, China/Beijing: Springer/Tsinghua University Press.
Czakiert, T., Sztekler, K., Karski, S., Markiewicz, D., & Nowak, W. (2010). Oxy-fuel
circulating fluidized bed combustion in a small pilot-scale test rig. Fuel Processing
Technology, 91(November (11)), 1617–1623.
Czakiert, T., Bis, Z., Muskala, W., & Nowak, W. (2006). Fuel conversion from oxy-fuel
combustion in a circulating fluidized bed. Fuel Processing Technology, 87(June
(6)), 531–538.
Davidson, R. M., & Santos, S. O. (2010, June). Oxyfuel combustion of pulverized coal.
London (UK): IEA Clean Coal Centre. Report No.: CCC/168, ISBN:
Duan,
978-92-9029-
488-7.
L., Zhao, C., Zhou, W., Chengrui, Q., & Chen, X. (2011). O2/CO2coal combus-
tion characteristics in a 50 kWthcirculating fluidized bed. International Journal
of Greenhouse Gas Control, 5(July (4)), 770–776.
Eriksson, T., Sippu, O., Hotta, A., Fan, Z., Myöhänen, K., Hyppänen, T., et al.
(2007). Oxyfuel CFB boiler as a route to near zero CO2 emission coal firing
[Internet]. In Power-Gen Europe (Ed.), 15th POWER-GEN Europe conference, con-
ference proceedings – power-gen europe [CD-ROM]; 2007 June 26–28; Madrid,
Spain. Madrid (ES): PennWell Corporation [cited 2011 Nov 28]. Available from
http://www.fwc.com/publications/tech papers/files/TP CCS 07 02.pdf
Foster Wheeler Energia Oy. Foster Wheeler figure material [database]. Varkaus: Fos-
ter Wheeler Energia Oy; [Date unknown] [updated 2012; cited 2013 June 05].
Available from internal company database.
Hack, H., Fan, Z., Seltzer, A., Eriksson, T., Sippu, O., & Hotta, A. (2008).
Development of integrated flexi-burn dual oxidant CFB power plant [Inter-
net]. In American Society of Mechanical Engineers: Power Division, United
States: Department of Energy, National Energy Technology Laboratory (US),
Coal Technology Association, American Public Power Association (Eds.), The
Proceedings of the 33rd International Technical Conference on Coal Uti-
lization & Fuel Systems; June 01–05. Clearwater (FL), USA. Clearwater (FL,
US): Coal Technology Association 2008 [cited 2011 Nov 28]. Available from
http://www.fwc.com/publications/tech papers/files/TP CCS 08 02.pdf
Hasegawa, T. (2013). Development of semiclosed cycle gas turbine for oxy-fuel IGCC
power generation with CO2capture. In E. Benini (Ed.), Progress in gas turbine
performance (pp. 25–50). Rijeka: InTech.
Ikonen, E., Kovács, J., & Ritvanen, J. (2013). Circulating fluidized bed hot-loop
analysis, tuning, and state-estimation using particle filtering. International
Journal of Innovative Computing, Information and Control, 9(August (8)),
3357–3376.
IPCC. (2005). 3 capture of CO2. In B. Metz, O. Davidson, H. C. de Coninck, M. Loos,
& L. A. Meyer (Eds.), Working group III of the intergovernmental panel on climate
change. IPCC special report on carbon dioxide capture and storage (pp. 105–178).
Cambridge (UK) and New York (NY, US): Cambridge University Press.
McDonald, D. & Zadiraka, A. (2007). Control of pulverized coal oxy-combustion
systems [Internet]. In The International Society of Automation (ISA) (Ed.),
Power – 17th annual ISA power industry division and EPRI controls and
instrumentation conference [CD-ROM] 2007 June 10–15, Pittsburgh (PA),
USA. Pittsburgh (PA, US): ISA; [cited 2011 Nov 28]. Available from
http://www.babcock.com/library/pdf/BR-1798.pdf
ya Nsakala, N., Liljedahl, G. N., Marion, J., Levasseur, A. A., Turek, D., Cham-
berland, R., et al. (2004). Oxygen-fired circulating fluidized bed boilers
for greenhouse gas emissions control and other applications [Internet].
In The National Energy Technology Laboratory (NETL) (Ed.), 3rd annual
conference on carbon capture & sequestration, conference proceedings [Inter-
net]; 2004 May 03–06; Alexandria (VA), USA. Alexandria (VA, US): NETL,
U.S. Department of Energy (DOE) [cited 2011 Nov 28]. Available from
http://www.netl.doe.gov/publications/proceedings/04/carbon-seq/031.pdf
Ritvanen, J., Kovács, J., Salo, M., Hultgren, M., Tourunen, A., & Hyppänen, T. (2012).
1-D dynamic simulation study of oxygen fired coal combustion in pilot and large
scale CFB boilers. In International Conference on Fluidized Bed Combustion (Ed.),
21st international conference on fluidized bed combustion proceedings (Vol. 1, pp.
72–79). 2012 June 03–06; Naples, Italy. Naples (IT): EnzoAlbanoEditore.
Romeo, L. M., Díez, L. I., Guedea, I., Bolea, I., Lupián˜ez, C., González, A., et al. (2011).
Design and operation assessment of an oxyfuel fluidized bed combustor. Exper-
imental Thermal and Fluid Science, 35(April (3)), 477–484.
Suraniti, S. L., ya Nsakala, N., & Darling, S. L. (2009). Alstom oxyfuel CFB boilers: A
promising option for CO2capture. Energy Procedia, 1(February (1)), 543–548.
Thorbergsson, E. M. (2012). Conceptual gas turbine modelling for oxy-fuel power cycles.
Gothenburg (SE): Chalmers University of Technology (Dissertation)
Toftegaard, M. B., Brix, J., Jensen, P. A., Glarborg, P., & Jensen, A. D. (2010). Oxy-fuel
combustion of solid fuels. Progress in Energy and Combustion Science, 36(October
(5)), 581–625.
Tourunen, A. (2010). A study of combustion phenomena in circulating fluidized beds by
developing and applying experimental and modelling methods for laboratory-scale
reactors, Acta Universitatis Lappeenrantaensis 419. Lappeenranta: Lappeenranta
University of Technology (Dissertation).
Wall, T., Liu, Y., Spero, C., Elliott, L., Khare, S., Rathnam, R., et al. (2009). An overview on
oxyfuel coal combustion – State of the art research and technology development.
Chemical Engineering Research and Design, 87(August (8)), 1003–1016.
Weigl, S. (2009). Modellierung und experimentelle Untersuchungen zum
Oxyfuel-Prozess an einer 50 kW Staubfeuerungs-Versuchsanlage [‘Disserta-
tion, Internet]. Dresden (DE): Technische Universität Dresden 2009 [cited
2011 Nov 28]. German. Available from http://www.qucosa.de/fileadmin/data/
qucosa/documents/2612/100110%20Promotion%20Sebastian%20Weigl.pdf
Yin, C., Rosendahl, L. A., & Kaer, S. K. (2011). Chemistry and radiation in oxy-fuel
combustion: A computational fluid dynamics modeling study. Fuel, 90(July (7)),
2519–2529.
