# Emissions_and_Furnace_Gas_Temperature_fo

**Fonte**: Emissions_and_Furnace_Gas_Temperature_fo.pdf  
**Data de conversão**: 2025-07-30 15:08:46  
**Origem**: base_relevantes

---

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
Emissions and Furnace Gas Temperature for Electricity Generation
via Co-firing of Coal and Biomass
Shoaib Mehmood1, Bale V. Reddy2, Marc A. Rosen*3
1Faculty of Engineering and Applied Science, University of Ontario Institute of Technology, 2000 Simcoe
Street North, Oshawa, Ontario, Canada
e-mail: shoaib.mehmood786@gmail.com
2Faculty of Engineering and Applied Science, University of Ontario Institute of Technology, 2000 Simcoe
Street North, Oshawa, Ontario, Canada
e-mail: Bale.Reddy@uoit.ca
3Faculty of Engineering and Applied Science, University of Ontario Institute of Technology, 2000 Simcoe
Street North, Oshawa, Ontario, Canada
e-mail: Marc.Rosen@uoit.ca
Cite as: Mehmood, S., Reddy, B. V., Rosen, M. A., Emissions and Furnace Gas Temperature for Electricity Generation
via Co-firing of Coal and Biomass, J. sustain. dev. energy water environ. syst., 3(4), pp 344-358, 2015, DOI:
http://dx.doi.org/10.13044/j.sdewes.2015.03.0026
ABSTRACT
The emissions of carbon dioxide and nitrogen and sulphur oxides for electricity
generation with coal and biomass co-firing are investigated and the furnace gas
temperature assessed. The study uses simulation and considers fuel combinations based
on two coals (bituminous coal, lignite) and four types of biomass (rice husk, sawdust,
chicken litter, refused derived fuel). With increasing biomass, net CO emissions are seen
2
to decline significantly for all types of selected biomass, while gross carbon dioxide
emissions increase for all blends except bituminous coal/refuse derived fuel,
lignite/chicken litter and lignite/refuse derived fuel. The reductions in emissions of
nitrogen and sulphur oxides are dependent on the contents of nitrogen and sulphur in the
biomass. The results also show for all fuel combinations that increasing the biomass
proportion decreases the furnace exit gas temperature.
KEYWORDS
Emissions, Furnace gas temperature, Biomass, Coal, Electricity generation, Co-firing.
INTRODUCTION
Various thermochemical and biochemical technologies exist for converting biomass
into useful energy [1, 2]. Among these, biomass co-firing with coal is relatively common
method which, according to some [3, 4], holds significant potential for fostering
increased biomass utilization in the future.
The use of biomass/coal co-firing has expanded in recent years, particularly for
electricity generation, due to its various advantages. These include fuel flexibility, an
increased use of renewable energy sources in terms of biomass and the potential the
co-firing approach for reducing greenhouse gas and other emissions.
Numerous studies [4-18] have been reported on biomass co-firing with coal.
Researchers have summarized their experiences and reviewed the literature on co-firing
in general studies [5-9] related to biomass co-firing. Experimental studies report into the
effects of co-firing on factors such as boiler performance, combustion characteristics, and
gaseous and particulate emissions. Modelling studies on biomass/coal co-firing have also
* Corresponding author
344

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
been published. For instance, a numerical model for sawdust co-firing with coal in a 0.5
MW pulverized coal boiler has been developed by Abbas et al. [14] to investigate the
influence of burner injection mode on burnout and NO emissions by utilizing the
turbulence decay model for volatile combustion, the diffusive radiation model, and the
k-ε model. Backreedy et al. [15] report the modelling of a pulverized coal/pinewood
co-firing process in a 1 MW combustor using a commercially available Computational
Fluid Dynamics (CFD) code (Fluent version 6) to examine the impact of biomass particle
size and shape on the burnout of blended char. Ghenai and Janajreh [16] apply CFD to a
co-pulverized coal/wheat straw furnace to investigate the effects of co-firing on flow
field, gas and particle temperature distributions, particle trajectories, and gas emissions.
Huang et al. [17] examine the impact of coal co-firing ratio of biomass on energy
efficiency, plant equipment, and gaseous emissions by using the ECLIPSE process
simulator on a Pressurized Fluidized Bed Combustion (PFBC) combined cycle power
plant. Dong et al. [18] model gasification based biomass co-firing, via a CFD analysis for
a 600 MW tangential pulverized coal boiler.
Modelling studies on biomass/coal co-firing are less common than experimental
studies, and thus are needed to help the technology develop and improve. This is, in fact,
the main rationale for this article.
Additionally, numerous energy analyses of biomass co-firing pulverized coal
electricity generation system and plant performance are reported in the literature [19].
Evaluation of slagging and fouling tendency and the related details for biomass and coal
co-firing, the performance under oxygen enriched combustion conditions are also
reported [20-22]. Advances in biomass co-firing with coal, the technology schemes,
impacts and future perspectives have also been investigated [23].
Biomass co-firing based on a conventional pulverized coal electricity plant is modeled
and assessed in this article, with the objective of improving understanding. Specifically,
the impacts of biomass/coal co-firing on the furnace exit gas temperature and the gaseous
emissions of CO , NO , and SO is investigated. Engineering Equation Solver (EES) is
2 x x
utilized in the analyses, and several combinations of fuels and co-firing conditions are
considered to provide a comprehensive set of results. Engineering Equation Solver (EES)
is a general equation-solving program that can numerically solve thousands of coupled
non-linear algebraic and differential equations. The accuracy thermodynamic and
transport property database provided for hundreds of substances in a manner that allows
it to be used with the equation solving capability is a major feature of EES.
CO-FIRING SYSTEM
A diagram of the co-firing electricity plant analyzed and simulated in this article is
shown in Figure 1. In the plant, there is a boiler, comprised of a combustor and heat
exchangers (superheater and reheater). Also, there are two turbines: a High Pressure
Turbine (HPT) and a Low Pressure Turbine (LPT). In addition, the plant has one
Feedwater Heater (FWH) and two pumps: a Boiler Feed Pump (BFP) and a Condensate
Pump (CP).
The schematic of the co-firing based power plant, modeled to facilitate the analysis, is
presented in Figure 1. A direct co-firing configuration is employed because this is the
most commonly applied co-firing configuration [24]. Pulverized biomass mixes with
pulverized coal in the fuel transport lines before the burners because co-firing at elevated
ratios can be achieved by this type of mixing [1]. Both air and the fuels enter the boiler at
the environment temperature and pressure. Combustion takes place in the combustion
chamber and the flue gases after exchanging heat with the feedwater exit through the
stack. Superheated steam enters the high pressure turbine. After expansion through the
first turbine, some of the steam is extracted from the turbine and routed to the open
feedwater heater while the remaining is reheated to original temperature and expands
345

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
through the low pressure turbine to the condenser pressure. The reheater pressure is ¼ of
the original pressure. Steam and condensate exit the feedwater heater as a saturated liquid
at the extraction pressure. The condensate leaving the condenser mixes with the
feedwater leaving the feedwater heater and is then pumped to the boiler pressure. Stream
data for all components for both base coals (100% coal) are listed in Table 1.
Figure 1. Co-firing power electricity generation plant considered, including Feedwater Heater
(FWH), Condensate Pump (CP), Boiler Feed Pump (BFP), High Pressure Turbine (HPT) and
Low Pressure Turbine (LPT)
Table 1. Flow data for the electricity plant fired only with coal
Bituminous coal Lignite
Pressure Temperature Mass Energy
Flow Mass flow rate Energy rate
[bar] [˚C] flow rate rate
[kg/s] [MW]
[kg/s] [MW]
1 1.013 8 1.00 28.33 1.00 20.07
2 1.013 8 2.31 0.00 2.31 0.00
3 1.013 600 0.002 0.01 0.001 0.009
4 1.013 Variable2 11.87 26.22 8.40 18.12
5 1.013 150 11.87 2.867 8.40 3.086
61 1.013 150 0.08 0.009 0.06 0.007
7 120 600 8.44 30.46 5.82 21.00
8 30 395.9 8.44 27.20 5.82 18.75
9 30 395.9 2.35 7.57 1.62 5.22
10 30 600 6.09 22.44 4.24 15.47
11 0.06 36.17 6.09 15.35 4.24 10.58
12 0.06 36.17 6.09 0.92 4.24 0.64
13 3 36.35 6.09 0.94 4.24 0.65
14 3 233.9 8.44 8.51 5.82 5.87
15 120 236.2 8.44 8.62 5.82 5.94
16 1.013 8 596.4 20.10 411.3 13.86
17 1.013 16 596.4 40.07 411.3 27.63
1Flow 6 (not shown in Figure 1) represents fly ash carried with flue gases through the stack
21,886 ˚C for bituminous coal and 1,734 ˚C for lignite
346

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
FUELS CONSIDERED
The analysis considers four biomass fuels: rice husk, pine sawdust, chicken litter, and
refuse derived fuel, as well as two coals: bituminous coal and lignite. Information is
presented in Table 2a for the biomass feedstocks and in Table 2b for the coals. The
Higher Heating Value (HHV) of biomass and the Lower Heating Value (LHV) of coal are
calculated as follows [1, 25]:
(1)
𝐻𝐻𝑉𝑏 = 0.3491C𝑏 +1.178H𝑏 +1.005S𝑏 +0.0151N𝑏 −0.1034O𝑏 −0.02 11A𝑏 (2)
In e𝐿q𝐻u𝑉a𝑐tio=n 4(217),. 0s3u8b2sc𝑛r𝐶ip+t b9 0d.e8n8o1te1s0 𝑛bi𝐻om−a2s0s,7 w.4h6i4le2 4C𝑛, 𝑂H+, S2,9 7N.0, 1O1, 6a𝑛n𝑆d A are the
carbon, hydrogen, sulphur, nitrogen, oxygen, and ash contents of biomass in weight %. In
equation (2), subscript c denotes coal, n is the number of moles of the respective
constituent, and other terms are as defined earlier in equation (1). Equation (1) was
developed using the calculated values of the lower heating value of numerous solid
homogeneous organic compounds and it has an average deviation of 0.70%, while the
validity of the equation (2) was established for fuels having wide of range of elemental
composition and it has an average absolute error of 1.45%. Note that the higher and lower
heating values are related for a substance:
(3)
Table 2𝐻a.𝐻 C𝑉ha r=act𝐿e𝐻ris𝑉tic+s o2f1 s.e9l7ec8t𝑛ed𝐻 types of biomass
Biomass
Parameter
Chicken Pine Refuse Rice
Heating value [kJ/kg] litter 1 sawdu st1 derive d husk 2
Higher heating value 14,240 17,280 16,620 14,980
Lower heating value 13,410 16,180 15,410 13,990
Proximate analysis [wt%, as received]
Fixed carbon 13.1 14.2 0.5 20.1
Volatile matter 43.0 70.4 70.3 55.6
Moisture 9.3 15.3 4.2 10.3
Ash 34.3 0.1 25.0 14.0
Ultimate analysis [wt%, as received]
Hydrogen 3.8 5.0 5.5 4.5
Carbon 34.1 43.2 38.1 38.0
Oxygen 14.4 36.3 26.1 32.4
Nitrogen 3.50 0.08 0.78 0.69
Sulphur 0.67 - 0.33 0.06
Ash analysis [wt%]
SiO 5.77 9.71 38.67 94.48
2
Al O 1.01 2.34 14.54 0.24
2 3
Fe O 0.45 0.10 6.26 0.22
2 3
CaO 56.85 46.88 26.81 0.97
SO 3.59 2.22 3.01 0.92
3
MgO 4.11 13.80 6.45 0.19
K O 12.19 14.38 0.23 2.29
2
TiO 0.03 0.14 1.90 0.02
2
Na O 0.60 0.35 1.36 0.16
2
P O 15.40 6.08 0.77 0.54
2 5
1Vassilev et al. [26]
2Madhiyanon et al. [27]
347

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
Table 2b. Characteristics of selected coals
Coal1
Parameter
Bituminous Lignite
Heating value [kJ/kg]
Higher heating value 28,330 20,070
Lower heating value 27,340 19,070
Proximate analysis [wt%, as received]
Fixed carbon 53.9 35.0
Volatile matter 28.2 44.5
Moisture 7.8 12.4
Ash 10.1 8.1
Ultimate analysis [wt%, as received]
Hydrogen 3.9 4.1
Carbon 70.3 51.0
Oxygen 6.4 23.8
Nitrogen 1.07 0.4
Sulphur 0.41 0.16
Ash analysis [wt%]
SiO 51.67 46.15
2
Al O 29.15 20.91
2 3
Fe O 10.73 6.77
2 3
CaO 3.72 12.54
SO 1.47 8.00
3
MgO 1.41 2.35
K O 0.29 1.49
2
TiO 1.24 0.77
2
Na O 0.31 0.73
2
P O - 0.29
2 5
1Vassilev and Vassileva [28]
ANALYSIS
The analysis focuses on the boiler, which is divided into two subsystems: combustor
and heat exchangers (superheaters and reheater). The analysis is carried out for steady
state conditions, so all components are taken to be operating at steady state.
Assumptions
All gases are ideal and ambient air is considered as 79% nitrogen and 21% oxygen on
a volume basis. Excess air is used, and it is fixed at 20%, as recommended for the
pulverized boilers [29]. The stack gas temperature is taken to be 150 °C [29]. Radiation
and convective heat losses through large boilers and unburned losses due to combustibles
in the ash are each 1.5% of the fuel energy input [29, 30]. Of the ash in the fuel, 80% exits
as fly ash 20% and is collected as bottom ash [31]. The ash is inert and the bottom ash
temperature is 600 °C, based on values reported for pulverized boilers with dry bottoms
[29].
All components of the steam cycle have adiabatic boundaries and kinetic and
potential energy effects are neglected. Each steam turbine is assumed to have an
isentropic efficiency of 85% and each pump to have an isentropic efficiency of 88% [31].
The mechanical efficiency of each turbine and the generator efficiency are 99% and 98%
respectively [31-33].
Methodology
In the analysis, the fuel flow rate remains the same and the calculations are on the
basis of a unit fuel flow rate. The mass flow rate of coal at one particular co-firing
348

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
condition for all combinations of fuels remains constant. The mass flow rate of coal is
decreased from 1 kg/s to 0.75 kg/s in intervals of 0.05 kg/s and that of biomass is
increased from 0 kg/s to 0.30 kg/s. For all co-firing conditions, the operating temperature
and pressure of all steam cycle components remain fixed. However, the mass flow rate of
the steam produced varies at different co-firing conditions due to the changing feeding
rate to the boiler which consequently changes the energy flows at the inlet and outlet of
all components.
The co-firing share of coal (P ) and the co-firing share of biomass, also named as
c
co-firing ratio (P ) are defined as:
b
(4)
𝑃𝑐 = [𝑚̇ 𝑐/(𝑚̇𝑐 + 𝑚̇𝑏)]×100% (5)
Here, and resp𝑃e𝑏ct=iv[e𝑚l̇y𝑏 r/e(p𝑚rė𝑐se+nt 𝑚ṁ𝑏a)s]s ×flo1w0 0ra%te of coal and mass flow rate of
biomass.
Abbre𝑚vi̇a 𝑐 tions𝑚 ȧr 𝑏 e used for the name of a fuel blend, based on the first letter of the coal
and first and last letters of the biomass. For example, the abbreviation for the bituminous
and rice husk blend is B/RH.
Combustion and emissions
The following general chemical reaction can be written for the combustion chamber,
accounting for reactants entering and products leaving:
C H O N S + O + A O +3.76N +
a 2 2 ash
b CO b H b O b N (6)
𝑎1 𝑎21 𝑎32 𝑎4 𝑎25 2 𝑎6H2 3 2 ( 4 2 ) 𝑚̇
→ + Og + + + 𝑏5NO + 𝑏6NO2
where A , +, a 𝑏nd 7S O2 + de𝑚ṅ𝑏 o 𝑎 te+ th 𝑚e ̇𝑓 a 𝑎 ir molar flow rate, the bottom ash mass flow rate
a
and the fly ash mass flow rate, respectively; a to a denote the molar flow rates of
1 6
carbon, hyd𝑚ṙo 𝑏 g 𝑎 en, ox𝑚ẏ𝑓 g 𝑎 en, nitrogen, sulphur, and moisture, respectively; and b to b
1 6
denote the molar flow rates of the corresponding flue gases exiting the combustion
chamber. Subscripts c and b denote coal and biomass, while the letters P and M represent
the percent share of co-firing and molecular weight, respectively.
The mass flow rate of all reactants excluding air is found from the ultimate analysis
and the molar flow rate of hot products and air are found by element balances, as
described elsewhere [19]. All carbon in the fuel is converted to CO . For pulverized coal
2
boilers, the incomplete combustion loss is zero [29, 34]. Moreover, the addition of
biomass in the blend enhances the combustion characteristics because of its high volatile
content. NO emissions from the combustion process are mainly NO with a small fraction
x
of NO , usually less than 5% [34-37]. It is assumed that 96% of NO emissions are
2 x
through the formation of NO and 4% are through NO formation. 10-50% of the fuel
2
nitrogen is normally converted to NO [35, 36]. 30% of the fuel nitrogen is assumed to
convert to NO here. For a typical pulverized coal system, approximately 80% of NO
emissions are due to fuel bound nitrogen [34] and NO emission through prompt
mechanism is less than 5% [36]. The formation of NO emissions through prompt,
thermal, and fuel bound paths are assumed to be 4%, 16%, and 80% of the total NO
emissions formed respectively. Also, 30% of fuel nitrogen is assumed converted to
nitrogen oxide. All sulphur in the fuel is oxidized to SO , which is the only source of SO
2 x
emissions. SO emissions are due to formation of SO and SO . However, sulphur
x 2 3
349

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
trioxide (SO ) only constitutes 10% of SO emissions [34]. Both biomass and coal
3 x
contain negligible amount of sulphur. So, if any traces of SO are produced, they would
3
be so small that they can be neglected.
Emissions factors
In determining the effects of co-firing on furnace exit gas temperature and gaseous
emissions, two types of emission factors that represent normalized mass emissions are
used to describe the effect of co-firing on emissions:
 Energy-based emission factors (in g/kWh). The energy-based factor represents
the mass of emission per unit output (1 kWh) of electrical energy from the overall
plant;
 Mass-based emission factors (in kg/t). The mass-based factor represents the mass
of emission per unit mass of fuel input (1 t) to the overall plant.
For both cases, CO emissions, gross (total) and net emissions are considered. The
2
gross emissions include all material exiting the plant stack, while the net emissions are
discounted by the CO used in growing biomass and thus take into account the fact that
2
biomass is relatively CO neutral.
2
RESULTS AND DISCUSSION
The effects are investigated of biomass/coal co-firing on gaseous emissions and
furnace gas temperature, considering four biomass (rice husk, pine saw dust, chicken
litter and refuse derived fuel) and two types of coal (bituminous and lignite). The gaseous
emissions are determined under various power plant operating conditions.
Effect of co-firing on furnace exit gas temperature
The furnace exit gas temperature is an important performance measure for the boiler
as it affects heat transfer between the furnace exit gas and feedwater. Figure 2 shows that
the furnace exit gas temperature decreases with increasing biomass content for all blends.
The extent of decrease in the furnace exit gas temperature is observed to depend on
the heating value, the moisture content, and the ash content of biomass fuels. Biomass
with a low heating value provides little energy input, and a high biomass moisture content
necessitates that part of the heat supplied be used to vaporize the moisture. A high ash
content results in more sensible heat leaving the combustion chamber with solid waste.
These factors lower the furnace exit gas temperature.
Among the considered biomass types, chicken litter has the lowest calorific value and
the highest ash content. It also contains more moisture than bituminous coal. Therefore,
the largest reductions in furnace exit gas temperature are observed for the bituminous
coal/chicken litter and lignite/chicken litter blends. When the co-firing ratio increases
from 0% to 30%, for instance, the furnace exit gas temperature decreases from 2,079 K to
2,031 K for the bituminous coal/chicken litter blend and from 2,007 K to 1,962 K for the
lignite/chicken litter blend.
The biomass moisture content is observed to affect the furnace exit gas temperature
more significantly than the ash content. Refuse derived fuel has much higher ash content
than sawdust, which has a much higher moisture content than refuse derived fuel. The
higher moisture content of sawdust requires more heat to be supplied for the latent heat of
vaporization during its combustion compared to refuse derived fuel. Hence, a more
pronounced decrease in furnace exit gas temperature is observed for the bituminous
coal/sawdust blend than for the bituminous coal/refuse derived fuel blend.
Similarly, lignite has higher calorific value and lower ash content than that of refuse
derived fuel, but contains about 8% more moisture. Much more heat is needed to
vaporize the moisture of lignite than of refuse derived fuel, diminishing the difference
350

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
between heating values of these two fuels. Thus, the furnace exit gas temperature
decreases the least for the lignite/refuse derived fuel blend compared to all other blends.
With respect to base coal, the furnace exit gas temperature decreases to 2,066 K and
2,004 K respectively for blends of bituminous coal/refuse derived fuel and lignite/refuse
derived fuel, at a 30% co-firing ratio.
Figure 2. Effect of co-firing on furnace exit gas temperature
Effect of co-firing on emissions
Mass-based emission factors. The mass-based emission factors (with the listing for
CO representing gross emissions) are shown in Table 3a for blends of biomass and
2
bituminous coal and in Table 3b for blends of biomass and lignite:
 Carbon dioxide: The gross mass-based CO emission factors (kg/t) found in all
2
cases are less than CO emission factors (3,125 kg/t for bituminous coal and 2,300
2
kg/t for lignite), suggested by the US Environmental Protection Agency [38].
Since biomass fuels have lower carbon content than coals, the mass-based CO
2
emission factors decrease for all blends as the biomass proportion increases in the
blend. The most advantageous biomass in terms of CO emissions reduction is
2
chicken litter because it has the lowest carbon content of the considered biomass
fuels. The mass-based CO emission factor decreases by 15.4% and 9.9%
2
respectively for the blends of bituminous coal/chicken litter and lignite/chicken
litter when the co-firing ratio increases from 0% to 30%;
 Nitrogen oxide: In all cases, except for chicken litter blends at high co-firing
ratios (<20%), the mass-based NO emission factor is also less than NO emission
x x
factors (15.5 kg/t for bituminous coal and 7.5 kg/t for lignite) proposed by the US
Environmental Protection Agency [38]. The mass-based NO emission factor
x
decreases for all bituminous coal/biomass blends except bituminous coal/chicken
litter. This is due to the fact that all considered biomass fuels except chicken litter
have lower nitrogen concentrations than bituminous coal. Similarly, since all
considered biomass fuels except sawdust contain more nitrogen than lignite, the
mass-based NO emission factor increases for all lignite/biomass
x
351

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
blends except lignite/sawdust. Sawdust is the most beneficial biomass for
reducing NO emissions because of its small nitrogen content. At a 30% co-firing
x
ratio, the mass-based NO emission factor declines by 27.8% for the bituminous
x
coal/sawdust blend and by 24.1% for the lignite/sawdust blend;
 Sulphur oxide: For the case of bituminous coal/biomass blends, the mass-based
SO emission factor at all co-firing ratios is less than mass-based SO emission
x x
factor (around 13 kg/t for bituminous coal) suggested by the US Environmental
Protection Agency [33]. However, in case of lignite/biomass blends, the
mass-based SO emission factor is less than proposed emissions factor (around 5
x
kg/t for lignite) by the US Environmental Protection Agency [38] for rice husk
and sawdust only. For bituminous coal and biomass co-firing, this factor
decreases for all blends except bituminous coal/chicken litter because all selected
biomass fuels except chicken litter have less sulphur content than bituminous
coal. However, for lignite and biomass co-firing, the mass-based SO emission
x
factor decreases for the blends of lignite/rice husk and lignite/sawdust, while this
factor increases for the blends of lignite/chicken litter and lignite/refuse derived
fuel. Sawdust is the most beneficial biomass in terms of SO reduction. The
x
mass-based SO emission factor decreases at a 30% co-firing ratio by 30.0% and
x
29.8% respectively for the blends of bituminous coal/sawdust and
lignite/sawdust.
Table 3a. Mass-based emission factors for various blends of bituminous coal and biomass
Co-firing share Emission factor
Fuel
[%] [kg/t]
blend
P P CO NO SO
c b 2 x x
Base1 100 0 2,839 10.08 9.03
95 5 2,773 9.90 8.64
90 10 2,708 9.72 8.26
85 15 2,643 9.54 7.87
B/RH
80 20 2,578 9.36 7.49
75 25 2,513 9.18 7.10
70 30 2,447 9.00 6.72
95 5 2,784 9.61 8.58
90 10 2,729 9.15 8.13
85 15 2,675 8.68 7.68
B/SD
80 20 2,620 8.22 7.22
75 25 2,565 7.75 6.77
70 30 2,510 7.28 6.32
95 5 2,766 11.23 9.31
90 10 2,693 12.37 9.60
85 15 2,620 13.52 9.89
B/CL
80 20 2,547 14.66 10.18
75 25 2,474 15.80 10.46
70 30 2,401 16.95 10.75
95 5 2,774 9.94 8.94
90 10 2,709 9.81 8.86
85 15 2,644 9.67 8.76
B/RDF
80 20 2,579 9.53 8.68
75 25 2,514 9.40 8.59
70 30 2,449 9.26 8.50
1B/RH, B/SD, B/CL, and B/RFD denote respectively
bituminous coal/rice husk, bituminous coal/sawdust,
bituminous coal/chicken litter, and bituminous coal/refuse
derived fuel
352

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
Table 3b. Mass-based emission factors for various blends of lignite and biomass
Co-firing Emission factor
Fuel
share [%] [kg/t]
blend
P P CO NO SO
c b 2 x x
Base1 100 0 2,062 3.77 3.52
95 5 2,036 3.91 3.41
90 10 2,009 4.04 3.30
85 15 1,983 4.18 3.19
L/RH
80 20 1,957 4.31 3.08
75 25 1,930 4.45 2.97
70 30 1,904 4.59 2.86
95 5 2,046 3.62 3.35
90 10 2,030 3.47 3.17
85 15 2,014 3.32 3.00
L/SD
80 20 1,998 3.17 2.82
75 25 1,982 3.01 2.64
70 30 1,966 2.86 2.47
95 5 2,027 5.23 4.09
90 10 1,993 6.69 4.65
85 15 1,959 8.15 5.21
L/CL
80 20 1,925 9.61 5.77
75 25 1,891 11.07 6.33
70 30 1,857 12.53 6.89
95 5 2,036 3.95 3.71
90 10 2,009 4.13 3.90
85 15 1,983 4.31 4.09
L/RDF
80 20 1,957 4.48 4.27
75 25 1,931 4.66 4.46
70 30 1,905 4.84 4.65
1L/RH, L/SD, L/CL, and L/RFD denote respectively lignite/rice
husk, lignite/sawdust, lignite/chicken litter, and lignite/refuse
derived fuel
Energy-based emission factors. Figure 3a-3d shows the energy-based emission
factors for all co-firing fuel blends:
 Carbon dioxide: The impact of co-firing, in terms of energy-based emission
factors, is illustrated Figure 3a for total (gross) CO emissions and in Figure 3b
2
for net CO emissions. The net CO emissions account for the fact that biomass is
2 2
considered to be CO neutral. The trends shown for energy-based CO emission
2 2
factor agree with those of Kwong et al. [11] and Huang et al. [17];
Figure 3a. Effect of co-firing on gross CO emissions (legend as in Figure 2)
2
353

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
Figure 3b. Effect of co-firing on net CO emissions (legend as in Figure 2)
2
 Nitrogen oxide: The effect of co-firing on NO emissions is illustrated in Figure
x
3c. Since all biomass fuels except chicken litter have higher concentrations of
nitrogen than lignite, NO emissions increase with co-firing ratio for all
x
lignite/biomass blends except lignite/sawdust. For bituminous coal/biomass
blends, however, regardless of the lower nitrogen concentrations of both rice husk
and refuse derived fuel relative to bituminous coal, NO emissions increase
x
slightly with co-firing ratio for blends of bituminous coal/rice husk and
bituminous coal/refuse derived fuel. The increase in NO emissions is due to the
x
decrease in net work output with increasing co-firing ratio. It is also evident that
the most advantageous biomass in terms of NO reduction is sawdust because of
x
its low nitrogen content. NO emissions decrease from 3.32 g/kWh to 2.75 g/kWh
x
for the bituminous coal/sawdust blend and from 1.80 g/kWh to 1.44 g/kWh for
the lignite/sawdust blend, as the co-firing ratio increases from 0% to 30%. The
findings and observations regarding NO emissions found in this study agree with
x
those of Spliethoff et al. [5], Kruczek et al. [10], Kwong et al. [11], and Huang et
al. [17];
Figure 3c. Effect of co-firing on NO emissions (legend as in Figure 2)
x
 Sulphur oxide: The sulphur content in fuel has a direct effect on the generation of
sulphur dioxide during combustion. Among the chosen biomass, rice husk and
sawdust have negligible sulphur content. So, their addition to a fuel mixture
results in an overall reduction in SO emissions with co-firing ratio, as illustrated
x
in Figure 3d. Since chicken litter has much higher sulphur content than
bituminous coal and lignite, the SO emission factor increases with co-firing ratio
x
for blends of bituminous coal/chicken litter and lignite/chicken litter. The sulphur
354

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
concentration of refuse derived fuel is slightly lower than that of bituminous coal.
The SO emission factor increases with co-firing ratio for the bituminous
x
coal/refuse derived fuel blend due to a decrease in the work output.
Figure 3d. Effect of co-firing on SO emissions (legend as in Figure 2)
x
The behaviours of the gross and net emissions of CO differ, as follows:
2
 The gross CO energy-based emission factor increases with co-firing ratio for all
2
bituminous coal/biomass blends except bituminous coal/refuse derived fuel (see
Figure 3a). In case of lignite/biomass blends, the gross CO energy-based
2
emission factor decreases with co-firing ratio for blends of lignite/chicken litter
and lignite/refuse derived fuel and increases for blends of lignite/rice husk and
lignite/sawdust. The increase in gross CO emissions is due to the decrease in net
2
work output with increasing co-firing ratio, which generally yields higher
emissions compared with 100% coal. The decrease in CO emissions with
2
co-firing ratio for blends of bituminous coal/refuse derived fuel, lignite/refuse
derived fuel and lignite/chicken litter is due to the relatively low carbon content of
refuse derived fuel and chicken litter, which diminishes the work output
reduction. The energy-based CO emission factors at a 30% co-firing ratio are
2
948 g/kWh, 946 g/kWh, 937 g/kWh and 929 g/kWh respectively for blends of
bituminous coal/rice husk, bituminous coal/sawdust, bituminous coal/chicken
litter, and bituminous coal/refuse derived fuel. The corresponding CO emissions
2
factors are 991 g/kWh, 987 g/kWh, 979 g/kWh and 964 g/kWh for blends of
lignite/rice husk, lignite/sawdust, lignite/chicken litter, and lignite/refuse derived
fuel respectively;
 The co-firing process exhibits significantly lower net CO emissions (see Figure
2
3b). With reference to base coal, net CO emissions decrease from 934 g/kWh to
2
770 g/kWh, 749 g/kWh, 777 g/kWh and 754 g/kWh respectively for the blends of
bituminous coal/rice husk, bituminous coal/sawdust, bituminous coal/chicken
litter, and bituminous coal/refuse derived fuel, at a 30% co-firing ratio. The
corresponding net CO emissions for blends of lignite/rice husk, lignite/sawdust,
2
lignite/chicken litter, and lignite/refuse derived fuel at a 30% co-firing ratio are
751 g/kWh, 725 g/kWh, 761 g/kWh, and 731 g/kWh respectively. The most
suitable biomass in terms of CO reduction is demonstrated to be sawdust due to it
2
having the highest carbon content among the considered biomass fuels.
CONCLUSIONS
Biomass co-firing with coal has strong impact on furnace gas temperature and
exhaust gas emissions. The biomass fuel, composition and co-firing ratio influences the
355

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
emissions from a electricity generation system, as do the biomass fuel and co-firing
conditions. The present results clearly demonstrate the significant effect of biomass type
and co-firing ratio on emissions and reduction in carbon dioxide. In fact, biomass
co-firing with coal results in significantly reduced CO emissions if biomass is
2
considered to be CO neutral. The gross (total) CO emissions are lower if the carbon
2 2
content of the biomass is relatively low. This characteristic also diminishes the work
output reduction caused by biomass addition to a fuel blend. Also, reductions in NO and
x
SO emissions are also achieved with biomass co-firing with coal if the selected biomass
x
has less nitrogen and sulphur than coal. Therefore biomass co-firing can lead to
substantial benefits in terms of CO , NO , and SO emissions reduction. Hence, co-firing
2 x x
of biomass with coal has significant environmental benefits and fosters an increased use
of renewable energy.
ACKNOWLEDGMENTS
The authors gratefully acknowledge the financial support provided by the Natural
Sciences and Engineering Research Council of Canada.
REFERENCES
1. Loo, S. V. and Koppejan, J., The Handbook of Biomass Combustion and Co-firirng,
London, UK: Earthscan, 2008.
2. Zhang, L., Xu, C. and Champagne, P., Overview of Recent Advances in
Thermo-Chemical Conversion of Biomass, Energy Conversion and Management,
Vol. 51, No. 5, pp 969-982, May 2010,
http://dx.doi.org/10.1016/j.enconman.2009.11.038
3. Lian, Z. T., Chua, K. J. and Chou, S. K., A Thermoeconomic Analysis of Biomass
Energy for Trigeneration, Applied Energy, Vol. 87, No. 1, pp 84-95, 2010,
http://dx.doi.org/10.1016/j.apenergy.2009.07.003
4. Hughes, E. E. and Tillman, D. A., Biomass Cofiring: Status and Prospects 1996,
Fuel Processing Technology, Vol. 54, No. 1-3, pp 127-142, 1998,
http://dx.doi.org/10.1016/S0378-3820(97)00064-7
5. Spliethoff, H., and Hein, K. R. G., Effect of Co-combustion of Biomass on
Emissions in Pulverized Fuel Furnaces, Fuel Processing Technology, Vol. 54, No.
1-3, pp 189-205, 1998, http://dx.doi.org/10.1016/S0378-3820(97)00069-6
6. Demirbas, A., Sustainable Co-firing of Biomass with Coal, Energy Conversion and
Management, Vol. 44, No. 9, pp 1465-1479, 2003,
http://dx.doi.org/10.1016/S0196-8904(02)00144-9
7. Savolainen, K., Co-firing of Biomass in Coal-fired Utility Boilers, Applied Energy,
Vol. 74, No. 3-4, pp 369-381, 2003,
http://dx.doi.org/10.1016/S0306-2619(02)00193-9
8. Pronobis, M., The Influence of Biomass Co-combustion on Boiler Fouling and
Efficiency, Fuel, Vol. 85, No. 4, pp 474-480, 2006.
9. De, S. and Assadi, M., Impact of Biomass Co-firing with Coal in Power Plants: A
Techno-Economic Assessment, Biomass and Bioenergy, Vol. 33, No. 2, pp 283-293,
2009, http://dx.doi.org/10.1016/j.biombioe.2008.07.005
10. Kruczek, H., Raczka, P. and Tatarek, A., The Effect of Biomass on Pollutant
Emission and Burnout in Co-combustion with Coal, Combustion Science and
Technology, Vol. 178, No. 8, pp 1511-1539, 2006,
http://dx.doi.org/10.1080/00102200600721297
11. Kwong, P. C. W., Chao, C. Y. H., Wang, J. H., Cheung, C. W. and Kendall, G., Co-
combustion Performance of Coal with Rice Husks and Bamboo, Atmospheric
Environment, Vol. 41, No. 35, pp. 7462-7472, 2007,
http://dx.doi.org/10.1016/j.atmosenv.2007.05.040
356

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
12. Casaca, C. and Costa, M. Co-combustion of Biomass in a Natural Gas-Fired
Furnace, Combustion Science and Technology, Vol. 175, No. 11, pp 1953-1977,
2003, http://dx.doi.org/10.1080/714923187
13. Demirbas, A., Co-firing Coal and Municipal Solid Waste, Energy Sources, Part A:
Recovery, Utilization, and Environmental Effects, Vol. 30, No. 4, pp 361-369, 2008,
http://dx.doi.org/10.1080/00908310600714055
14. Abbas, T., Costen, P., Kandamby, N. H. and Lockwood, F. C., The Influence of
Burner Injection Mode on Pulverized Coal and Biomass Co-fired Flames,
Combustion and Flame, Vol. 99, No. 3-4, pp 617-625, 1994,
http://dx.doi.org/10.1016/0010-2180(94)90055-8
15. Backreedy, R. I., Fletcher, L. M., Jones, J. M., Ma, L., Pourkashanian, M. and
Williams, A., Co-firing Pulvrerized Coal and Biomass: A Modelling Approach,
Proceedings of the Combustion Institute, Vol. 30, No. 2, pp 2955-2964, 2005,
http://dx.doi.org/10.1016/j.proci.2004.08.085
16. Ghenai, C. and Janajreh, I., CFD Analysis of the Effects of Co-firing Biomass with
Coal, Energy Conversion and Management, Vol. 51, No. 8, pp 1694-1701, 2010,
http://dx.doi.org/10.1016/j.enconman.2009.11.045
17. Huang, Y., Wright, D. M., Rezvani, S., Wang, Y. D., Hewitt, N. and Williams, B. C.,
Biomass Co-firing in a Pressurized Fluidized Bed Combustion (PFBC) Combined
Cycle Power Plant: A Techno-Environmental Assessment based on Computational
Simulations, Fuel Processing Technology, Vol. 87, No. 10, pp 927-934, 2006,
http://dx.doi.org/10.1016/j.fuproc.2006.07.003
18. Dong, C., Yang, Y., Yang, R. and Zhang, J., Numerical Modeling of the Gasification
Based Co-firing in a 600 MW Pulverized Coal Boiler, Applied Energy, Vol. 87, No.
9, pp 2838-2834, 2010, http://dx.doi.org/10.1016/j.apenergy.2009.05.033
19. Ghamarian, A. and Cambel, A. B., Exergy Analysis of Illinois No. 6 Coal, Energy,
Vol. 7, No. 6, pp 483-488, 1982, http://dx.doi.org/10.1016/0360-5442(82)90010-X
20. Vassilev, S. V., Baxter, D., Andersen, L. K. and Vassileva, C. G., An Overview of
the Chemical Composition of Biomass, Fuel, Vol. 89, No. 5, pp 913-933, 2010,
http://dx.doi.org/10.1016/j.fuel.2009.10.022
21. Madhiyanon, T., Sathitruangsak, P. and Soponronnarit, S., Co-combustion of Rice
Husk with Coal in a Cyclonic Fluidized-Bed Combustor (ψ-FBC), Fuel, Vol. 88,
No. 1, pp 132-138, 2009, http://dx.doi.org/10.1016/j.fuel.2008.08.008
22. Vassilev, S. V. and Vassileva, C. G., A New Approach for the Combined Chemical
and Mineral Classification of the Inorganic Matter in Coal 1. Chemical and Mineral
Classification Systems, Fuel, Vol. 88, No. 3, pp. 235-245, 2009,
http://dx.doi.org/10.1016/j.fuel.2008.09.006
23. Al-Mansour, F. and Zuwala, J., An Evaluation of Biomass Co-firing in Europe,
Biomass and Bioenergy, Vol. 34, No. 5, pp 620-629, 2010,
http://dx.doi.org/10.1016/j.biombioe.2010.01.004
24. Basu, P., Kefa, C. and Jestin, L., Boilers and Burners: Design and Theory, New
York, USA: Springer, 2000, http://dx.doi.org/10.1007/978-1-4612-1250-8
25. de Souza-Santos, M. L., Solid Fuels Combustion and Gasification, 2nd ed., Boca
Raton, USA: CRC Press, 2010, http://dx.doi.org/10.1201/9781420047509
26. Drbal, L. F., Boston, P. G. and Westra, K. L., Power Plant Engineering, New York,
USA: Springer, 1996.
27. Suresh, M. V. J. J., Reddy, K. S. and Kolar, A. K., 3-E Analysis of Advanced Power
Plants Based on High Ash Coal, International Journal of Energy Research, Vol. 34,
No. 8, pp 716-735, 2010, http://dx.doi.org/10.1002/er.1593
28. Ajundi, I. H., Energy and Exergy Analysis of a Steam Power Plant in Jordan,
Applied Thermal Engineering, Vol. 29, No. 2-3, pp 324-328, 2009,
http://dx.doi.org/10.1016/j.applthermaleng.2008.02.029
29. Bellhouse, G. M. and Whittington, H. W., Simulation of Gaseous Emissions from
Electricity Generation Plant, International Journal of Electrical Power and Energy
357

Journal of Sustainable Development of Energy, Water Year 2015
and Environment Systems Volume 3, Issue 4, pp 344-358
Systems, Vol. 18, No. 1, pp 501-507, 1996, http://dx.doi.org/10.1016/0142-
0615(96)00010-5
30. Sarofim, A. and Flagan, R. C., NO Control for Stationary Combustion Sources,
x
Progress in Energy and Combustion Science, Vol. 2, No. 1, pp 1-25, 1976,
http://dx.doi.org/10.1016/0360-1285(76)90006-X
31. Phong-Anant, D., Wibberley, L. J. and Wall, T. F., Nitrogen Oxide Formation from
Austrlian Coals, Combustion and Flame, Vol. 62, No. 1, pp 21-30, 1985,
http://dx.doi.org/10.1016/0010-2180(85)90090-2
32. Miller, A. and Bowman, C. T. Mechanism and Modeling of Nitrogen Chemistry in
Combustion, Progress in Energy and Combustion Science, Vol. 15, No. 4, pp 287-
238, 1989, http://dx.doi.org/10.1016/0360-1285(89)90017-8
33. US Environmental Protection Agency (USEPA), External Combustion Sources,
1998, http://www.epa.gov/ttn/chief/ap42/ch01/index.html, [Accessed:
14-April-2011]
34. Mehmood, S., Reddy, B. V. and Rosen, M. A., Energy Analysis of a Biomass
Co-firing Based Pulverized Coal Power Generation System, Sustainability, Vol. 4, pp
462-490, 2012.
35. Teixeira, P., Lopes, H., Gulyurtlu, I., Lap, N. and Abehla, P., Evaluation of Slagging
and Fouling Tendency during Biomass Co-firing with Coal in a Fluidized Bed,
Biomass Bioenergy, Vol. 39, pp 192-203, 2012,
http://dx.doi.org/10.1016/j.biombioe.2012.01.010
36. Tan, Y., Jia, L. and Wu, Y., Some Combustion Characteristics of Biomass and Coal
Co-firing under Oxy-Fuel Conditions in a Pilot-Scale Circulating Fluidized Bed
Combustor, Energy and Fuels, Vol. 27, pp 7000-7007, 2013,
http://dx.doi.org/10.1021/ef4011109
37. Pawtak-Kruczek, H., Ostrycharczyk, M., Baranowsk, M., Czerep, M. and Zgora, J.,
C-firing of Biomass with Pulverized Coal in Oxygen Enriched Atmosphere,
Chemical and Process Engineering, Vol. 34, pp 215-226, 2013.
38. Karampinis, E., Grammelis, P., Agraniotis, M., Violidakis, I. and Kakaras, E.,
Co-firing of Biomass with Coal in Thermal Power Plants: Technology Schemes,
Impacts and Future Perspectives, Wiley Interdisciplinary Reviews: Energy and
Environment, 2013, http://dx.doi.org/10.1002/wene.100
Paper submitted: 11.11.2014
Paper revised: 27.02.2015
Paper accepted: 28.02.2015
358
