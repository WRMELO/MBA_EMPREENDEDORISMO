# Thermal_Design_of_Heat_Exchangers

**Fonte**: Thermal_Design_of_Heat_Exchangers.pdf  
**Data de conversão**: 2025-07-30 15:13:39  
**Origem**: base_relevantes

---

Helsinki University of Technology Department of Mechanical Engineering
Energy Engineering and Environmental Protection Publications
Steam Boiler Technology eBook
Espoo 2002
Thermal Design of Heat Exchangers
Sebastian Teir, Anne Jokivuori
Helsinki University of Technology
Department of Mechanical Engineering
Energy Engineering and Environmental Protection
i

Table of contents
Table of contents..................................................................................................................................ii
General design issues...........................................................................................................................1
Heat transfer modes.........................................................................................................................1
Conduction...................................................................................................................................1
Convection...................................................................................................................................1
Radiation......................................................................................................................................2
Pressure losses..................................................................................................................................2
Definition.....................................................................................................................................2
Gas side pressure drop for inline tube arrangement.....................................................................3
Gas side pressure drop for staggered tube arrangement..............................................................3
Choice of tube surface......................................................................................................................4
Sizing of heat transfer surfaces........................................................................................................4
Furnace design.....................................................................................................................................6
General design..................................................................................................................................6
Furnace strain level..........................................................................................................................7
Tube wall design..............................................................................................................................8
Load characteristics..........................................................................................................................8
Fuel type effect on furnace size.......................................................................................................8
Typical furnace outlet temperatures.................................................................................................9
Furnace air levels...........................................................................................................................10
CFB furnace design........................................................................................................................10
BFB furnace design........................................................................................................................12
Heat recovery steam generator (HRSG) design.............................................................................12
Furnace dimensioning, stirred reactor............................................................................................14
Superheater design.............................................................................................................................15
General...........................................................................................................................................15
Design velocity..............................................................................................................................15
Design spacing...............................................................................................................................16
Tube arrangement..........................................................................................................................17
Economizer design.............................................................................................................................18
General...........................................................................................................................................18
Design method...............................................................................................................................18
Air preheater design...........................................................................................................................21
References..........................................................................................................................................22
ii

General design issues
Heat transfer modes
Conduction
Conduction is the transfer of heat from one part of a body at a higher temperature to another part of
the same body at a lower temperature, or from one body at a higher temperature to another body in
physical contact with it at a lower temperature. The conduction process takes place at the molecular
level and involves the transfer of energy from the more energetic molecules to those with a lower
energy level.
Heat power [W] by conduction is:
t −t
Φ =λA 1 2 (1)
s
Heat power depends on the heat transfer area (A), temperature difference (t -t ), thermal
1 2
conductivity of material (λ) and the thickness of separating wall (s). The thermal conductivity is a
property of the material; metals conduct well heat whereas gases not. An example of thermal
conductivities in various materials is shown in table 1.
Table 1: Thermal conductivities for various materials.
Material Thermal conductivity [W/(m*K)]
Copper 370
Aluminium 210
Steel 45
Stainless steel 20
Insulations 0,03-0,1
Convection
Convection is heat transfer between a moving fluid or gas and a fixed solid. Convection can be
natural or forced: if a pump, a blower, a fan, or some similar device induces the fluid motion, the
process is called forced convection. If the fluid motion occurs as a result of the density difference
produced by the temperature difference, the process is called free or natural convection.
Heat power by convection can be calculated as:
Φ =α A(t −t ) (2)
c 1 2
The heat transfer coefficient α varies much depending on e.g. flow velocity, type of fluid motion
c
and pressure. Heat transfer coefficients of liquids are much higher than those of gases, as can be
seen in the comparison presented in table 2.
1

Table 2: Convection heat transfer coefficients for various fluids.
Fluid Heat transfer coefficient [W/(m2K)]
Steady water 100-500
Water flow 500-10000
Water boiling 1000-60000
Steady air 3-15
Air flow 10-100
Radiation
Radiation, or more correctly thermal radiation, is electromagnetic radiation emitted by a body by
virtue of its temperature and at the expense of its internal energy. All heated solids and liquids, as
well as some gases, emit thermal radiation.
The importance of radiation heat transfer will increase, when the temperature becomes higher.
Radiation heat transfer is the main heat transfer mode for the furnace and radiation superheaters.
Emitted heat by radiation can be calculated as:
Φ =ε σA(T4 −T4) (3)
r fw f w
where ε is the view factor between the flame and the water walls:
fw
1
ε = (4)
fw 1 1
+ −1
ε ε
f w
where ε is the emissivity of the flame (typically 0,35-0,85), ε the emissivity of the water walls
f w
(typically 0,6), σ the Stefan-Boltzmann constant (5,6787*10-8 W/m2K4), A the effective water wall
surface (m2), T the average gas temperature in the furnace and T the average water wall surface
f w
temperature surrounding the flame.
Radiation heat can also be expressed as
Φ =α A(t −t ) (5)
rad 1 2
where α is the radiation heat transfer coefficient.
rad
Pressure losses
Definition
The difference between pressure gage readings in parts of a system operating with a positive
pressure relative to that of the atmosphere is generally called pressure drop. The pressure drop on
the gas side is equal to the friction losses, according to VDI Wärmeatlas [1]:
∆p = ∆p (6)
gs f
2

Gas side pressure drop for inline tube arrangement
For inline tube arrangement the pressure drop coefficient for heat transfer surface with horizontal
tubes is:
∆p = n ζ ∆p (7)
r r d
where nr is the number of tube rows in the heat transfer unit, ∆pd dynamic pressure calculated at
the gas side using the mean temperature and the smallest area. The single row pressure drop ξr for
inline tube arrangement is calculated as
Re−1000
−
ζ =ζ +ζ (1−e 2000 ) (8)
r l t
where
280π((s 0.5 −0.6)2 +0.75)
ζ = l (9)
l 1.6
(4s s −π)s Re
t l
t
 0.94 
(1- ) 0.6
 
s
ζ = 100.47(s t /s l -1.5)(0.22+1.2 l +0.03(s −1)(s −1) (10)
t  (s -0.85)1.3  t l
t
 
 
where ζ is the laminar part of the pressure drop coefficient, ζ is the turbulent part of the pressure
l t
drop coefficient, s is the dimensionless transverse pitch (s =S / d ), s is the dimensionless
t t t o l
longitudinal pitch (s =S / d ) and Re is the Reynolds number, calculated at the gas side mean
l l o
temperature and smallest area.
Gas side pressure drop for staggered tube arrangement
The single row pressure drop ζ for staggered tubes is calculated similarly to inline tube
r
arrangement, with the following exceptions:
 Re−200 
−
ζ =ζ +ζ 1−e 1000  (11)
r l t 
 
280π 
(
s0.5 −0.6
)2
+0.75 
 l 
ζ = (12)
l (4s s −π)c1.6 Re
t l
where
c =s ;s ≥ 2s -1/2
t l t
s (13)
c = ( t )2 +s 2 ;s < 2s −1/2
2 l l t
3

3 3
 1.2  s  s 
ζ = 2.5+ +0.4 l −1 −0.01 t −1 (14)
t 

(s
t
−0.85)1.08 



s
t




s
l


Choice of tube surface
Surfaces used in tubular heat transfer units can be finned or unfinned (smooth surface). Heat
transfer properties can be improved using finned tubes, because the fins enlarge the tubular heat
transfer area.
The tubes in the economizer are usually finned,
because the heat transfer properties of the flue
gas side are not so good as on the water side.
Economizers are made of cast iron or steel
tubes. Cast iron tubes are easily equipped with
fins, but also steel tubes can be equipped with
fins. Finned tubes are more difficult to clean
than unfinned tubes, thus economizers with
unfinned steel tubes are used in boilers burning
fuels with a high ash content.
Figures 1-3 provide some examples on finned
steel tubes. Spiral finned tubes are often used in Figure 1: Spiral finned tubes [Aircoil].
heat recovery steam generators. By bending fins
heat transfer properties can also be improved.
Steel tube with aluminium fins endures better in
corrosive conditions. Compound composition
conists of a cast iron tube equipped with fins and
steel tube inside. A compound composistion
endures higher pressure.
In air preheaters finned steel tubes are not used,
since the heat transfer properties are practically
the same on both air and flue gas sides. When
cast iron tubes are used, heat transfer surfaces
are usually finned on both sides to improve the
heat transfer.
Superheaters and evaporators use unfinned Figure 2: Finned tubes [Vulcan finned tubes].
tubes.
Sizing of heat transfer surfaces
When sizing the heat transfer surface of a heat
exchanger the heat power to be transferred and
stream temperatures of inlets and outlets have to
be known. The heat power is proportional to the
area of the heat exchanger, heat transmission
coefficient and temperature difference (between
the streams):
4

Φ = kA∆T (15)
lm
The mean logarithmic temperature difference in
equation 15 can be calculated as:
∆T −∆T
∆T = max min (16)
lm ∆T
ln max
∆T
min
where ∆T is the largest temperature difference
max
and ∆T the smallest temperature difference:
min
Figure 3: Parallel finned tube (Thermal-land).
∆T = t -t
max h1 c2
∆T = t -t (17)
min h2 c1
where the inlet and outlet temperatures are
explained in figure 4.
The heat surface area can be calculated from
equation 15, when temperatures and the heat
transfer coefficient have been determined, which
is the capability of the heat exchanger to transfer
heat between two fluids.
Figure 4: Heat exchanger stream descriptions
(for a cross-flow heat exchanger), used in
equation 17.
5

Furnace design
General design
The main parameters for the furnace sizing are furnace dimensions (height, depth, width and
configuration), furnace wall construction and desired furnace outlet temperature.
The heat transfer surface area of furnace consists of sides, base and beak, which is an "L"-formed
bending of the evaporator tubes that protect the superheaters from radiation. Most of utility and
industrial boiler furnaces have a rectangular shape. A large number of package boilers have a
cylindrical furnace. Furnace bottom for typical PCF boiler is double inclined or v-form, as shown in
figure 5. Flat bottom is more typical for grate or bubbling fluidized bed boilers.
The ratio of height and width varies 1-5 for
boilers with two-pass layout. The larger the
boiler is, the larger is also the ratio. The largest
boilers have a width of 20 m and a height of 100
m. The fuel and vaporization efficiency
determines the size of the furnace. To be able to
dimension furnaces the overall mass balance, h A
heat balance and heat transfer must be specified.
V
The overall furnace (gas side) mass balance is
m& = m& +∑m& −m& (18)
fg air fi ash
b2
b1
where the streams are described in figure 6.
∑m& is the sum of all the fuel streams into the
fi
boiler. The furnace heat balance can be specified Figure 5: Furnace dimensions. The painted
similarly: areas are the total effective furnace heat
transfer area.
Φ =Φ −Φ −Φ (19)
fur net loss exit
m&
fg
where the heat fluxes are shown in figure 7. If
the gas side temperatures and emissivities are
known, the furnace heat flux absorbed by the
furnace walls can be expressed as
m&
ε air
Φ = A ⋅σ⋅ w ⋅(ε T 4
fur eff dg g
α +ε −α ε (20)
dg w dg w m&
fi
−α T 4)+α ⋅A ⋅ ( T −T )
dg w c eff g w
m&
ash
where A is the effective heat transfer surface,
eff
σthe Stefan-Boltzmann constant, ε and ε Figure 6: Fuel/flue gas side mass balance.
w dg
the emissivity of the wall and the (dusty) gas
respectively, α the absorptivity of the (dusty)
dg
6

gas, α the convective heat transfer coefficient,
c
and T and T the temperature of the gas and loss exit
g w
wall respectively. The effect of convective term
is usually fairly small, often less than 10%.
Furnace strain level
The furnace is preliminarily dimensioned with a
net fur
suitable strain level. The volume (marked with a
“V” in figure 5) strain level is calculated as the
following:
Φ
q = pa (21) Figure 7: Furnace heat balance.
V bb h
1 2
Table 3: Strain level effects of various fuels
where Φ is the heat released from the fuel in
pa
the furnace and other variables furnace
Strain level
dimensions according to figure 5. The strain Fuel
[kW/m3]
level depends largely on different fuels.
Coal 145-185
Reference values on strain levels from different
Peat ~175
fuels are presented in table 3.
Oil, natural gas 290-690
The area strain level is calculated as the heat
power in the furnace per base area of the furnace
(marked with an “A” in figure 5):
Φ
q = pa (22)
F bb
1 2
If the electric power of power plant is known, strain levels for the volume and base area can be
chosen from the graphs in figure 8, and thereby the physical dimensions of the furnace can be
determined.
6 0,25
[MW/m3] [MW/m2]
5 0,20
4 0,15
3 0,10
2 0,05
0 200 400 600 MWe 0 200 400 600 MWe
Figure 8: Charts for selecting strain levels of the furnace.
The effective heat transfer surface area of the furnace, consisting of sides, base and beak, can be
calculated as following (assuming the beak adds 0,4*base area):
7

A =2lb +2lb +1,4bb (23)
eff 1 2 1 2
The first two terms forms the effective projected radiant surface (EPRS), which is a widely used
concept.
Tube wall design
When the size of the furnace has been dimensioned, the tube size and material can be chosen and
the wall thickness can be calculated according to the SFS 3273 standard. Then input velocity of
water to furnace is chosen and number of necessary tubes is calculated.
The diameter of an evaporator tube is usually 30-80 mm and the wall thickness can be calculated
from the following equation:
d ⋅ p
s = u +C +C (24)
1 2
 σ 
2⋅ l − p⋅ν+2⋅ p
 n 
where d is the outside diameter of tube, p the design pressure, σ the design strength, n a safety
u l
factor (usually 1,5), ν the strength factor (usually 1,0), C an additional thickness, (normally 10 %
1
of the wall thickness) and C an additional thickness considering corrosion.
2
Load characteristics
When designing of a steam-generating unit it is necessary to determine the following load
characteristics:
1. Minimum, normal and maximum load
2. Time duration of each load rate
3. Load factor
4. Nature of the load (constant or fluctuating)
The load factor is the actual energy produced by a power plant during a given period, given as a
percentage (share) of the maximum energy that could have been produced at full capacity during
the same period.
The design will determine the boiler's ability to carry a normal load at a high efficiency as well as to
meet maximum demand and rapid load changes. It will also determine the standby losses and the
rapidity with which the unit can be brought up to full steaming capacity. In smaller boiler sizes it is
possible to select a standardized unit that will meet the requirements; larger units are almost always
custom designed.
Fuel type effect on furnace size
The most important item to consider when designing a utility or large industrial steam generator is
the fuel the unit will burn. The furnace size, the equipment to prepare and burn the fuel, the amount
of heating surface and its placement, the type and size of heat recovery equipment, and the flue gas
treatment devices are all fuel dependent. The major differences among boilers that burn coal or oil
or natural gas result from the ash in the products of combustion.
8

Firing oil in the furnace produces relatively small amounts of ash. Natural gas produces no ash. For
the same power output, due to the high ash content of coal, coal-burning boilers must have larger
furnaces and velocities of the combustion gases in the convection-based heat exchangers must be
lower. Figure 9 presents an example of the relative sizes of furnaces using three different fuels:
natural gas, oil and coal. The power of the boiler is the same in all three cases.
Coal
Natural gas
Oil
1,5*h
1,2*h
h
b2
b1
1,05*b1
1,1*b1
1,06*b2
1,12*b2
Figure 9: Boiler fuel type effect on furnace size.
Typical furnace outlet temperatures
Furnace outlet temperature is the flue gas temperature after the radiation-based heat transfer
surfaces before entering the convection-based heat transfer surfaces. The outlet temperature
depends on the characteristics of the combusted fuel. If the temperature is too high, ash layers build
up on the surface of the superheater tubes. This leads to poorer heat transfer, increased corrosion
and it can even block flow paths.
The following factors affect the choice of furnace outlet temperature:
• Ash characteristics; the control of ash behaviour at superheaters is a key design parameter
• Fuel (gas and oil have low ash content and can have higher outlet temperatures)
• Choice of superheater material
• Desired superheating temperature
9

Table 4 presents some typical furnace outlet temperatures:
Table 4: Typical furnace outlet temperatures on various boiler types.
Fuel type Furnace outlet temperature [°C]
Biomass, circulating fluidized bed 900 - 1000
Peat, pulverized firing 950 - 1000
Coal, high volatiles 950 - 1000
Recovery boiler 900- 1050
Biomass, fluidized bed 1050 - 1150
Natural gas 900- 1200
Oil 900- 1200
Furnace air levels
The type of fuel determines the quantity of air required for combustion. It is necessary to provide air
in excess of this quantity to assure complete combustion. The amount of this excess air is
determined by the following factors:
1. Composition, properties, and condition of fuel when fired
2. Method of burning the combustible
3. Arrangement and proportions of the grate or furnace
4. Allowable furnace temperature
5. Turbulence and thoroughness of the mixing of combustion air and volatile gases
Excess air reduces efficiency by lowering the furnace temperature and by absorbing heat that would
otherwise be available for steam production.
NOx is formed when nitrogen of air reacts with oxygen of air in high temperature, over 1400 °C.
NOx can be reduced decreasing temperature, decreasing air excess, or using low-nox-burners. In
using low-nox-burner air will be fed into flame in two or three phases.
CFB furnace design
When dimensioning a circulating fluidized bed (CFB) furnace the high content of sand has to be
taken into consideration. This means that the temperature profile and thus the heat transfer near to
the furnace wall differs from other types of furnaces.
The furnace of a CFB (circulating fluidized bed) boiler contains a layer of granular solids, which
have a diameter in the range of 0,1-0,3 mm. It includes sand or gravel, fresh or spent limestone and
ash. The operating velocity of the flue gas stream in a CFB boiler is 3-10 m/s. The solids move
through the furnace at much lower velocity than the gas; solids residence times in the order of
minutes are obtained. The long residence times coupled with the small particle size produce high
combustion efficiency and high SO removal with much lower limestone feed than in conventional
2
furnaces. Figure 10 shows a flow chart of a typical CFB boiler.
After the furnace flue gas moves through a cyclone (named compact separator in figure 13), where
solids are separated from the gas and are returned to the furnace. Flue gas from the cyclone
discharge enters the convection back-pass in which the superheaters, reheaters, economizers and air
preheaters are located. A dust collector is separates the fly ash before the flue gas exits the plant.
10

The combustion air from the fan discharges pneumatically transports the solids for creating the
circulating fluid.
Steam Outlet
Steam Foster Wheeler CFB
Water
Steam Drum Flow Chart
Downcomer
Water
Wall
Compact Economizer
Fuel Limestone Separator
Feed Water Inlet
h A ea ir t er Dust Collector
Combustion
Chamber
Fly Ash
Induced Draft
Secondary Air Fan Fan
compact.eng/comflow.ds4/0801/tap
Bo
A
t
s
to
h
m
To Ash Silos Primary Air Fan
Figure 10: Flow chart of a CFB boiler [Foster-Wheeler].
The design of the furnace in a CFB boiler depends on:
• required velocity of gas
• time of complete combustion of fuel
• heat required for vaporization.
The amount of cyclones also has an influence on the shape of furnace. Flue gas must flow to the
cyclone fast enough (20 m/s), and the diameter of the cyclone must be below 8 m in order to get an
efficient removal of solids.
Circulating fluidized bed boilers have a number of unique features that make them more attractive
than other solid fuel fired boilers. Fuel flexibility is one of the major attractive features of CFB
boilers. A wide range of fuels can be burned in one specific boiler without any major change in the
hardware. The combustion efficiency of a CFB boiler is high. It is generally in the range of 99,5 to
97,5 %. Sulphur capture in a CFB is very efficient, due to the possibility to inject sulphur absorbing
limestone directly into the bed. A typical CFB boiler can capture 90 % of the sulphur dioxide. The
low emission of nitrogen oxides is also a major attractive feature of CFB boilers.
11

BFB furnace design
Bubbling fluidized bed (BFB) boilers use a low
fluidizing velocity, so that the particles are held
mainly in a bed, which have a depth of about 1
m and a definable surface. Sand is often used to
improve bed stability, together with limestone
for SO absorption. As the coal particles are
2
combusted and become smaller, they are
elutriated with the gases, and subsequently
removed as fly ash. In-bed tubes are used to
control the bed temperature and generate steam.
The flue gases are normally cleaned using a
cyclone, and then pass through further heat
exchangers, raising steam temperature.
In the furnace (photo in figure 11) of a BFB
boiler size of a grain of sand is about 1-3 mm
and the operating velocity is 0,7-2 m/s. Fuel is
fed onto the bed mechanically. Thanks to the
large heat capacity of the bed, a BFB furnace is Figure 11: Inside a BFB boiler furnace [photo
able to burn very moist fuel. Moist fuel will dry T. Rintala]
fast, when it is fed to the sand bed. Many
different kinds of fuels can be combusted in a
BFB furnace.
The temperature of a BFB furnace outlet is 700-1000 °C, and the air factor is usually 1,1-1,4. Air is
fed in several phases. The temperature of air varies from 20 to 400 °C. The overall thermal
efficiency of a BFB boiler is around 30%.
BFB furnaces with an atmospheric operational pressure are mainly used for boilers up to about 25
MWe, although there are a few larger plants where a BFB boiler has been used to retrofit an
existing unit. There are hundreds of small BFBC units in China.
Heat recovery steam generator (HRSG) design
Heat recovery steam generators (HRSGs) are used in power generation to recover heat from hot flue
gases (500-600 °C), usually originating from a gas turbine or diesel engine. The HRSG consists of
the same heat transfer surfaces as other boilers, except for the furnace. Since no fuel is combusted
in a HRSG, the HRSG have (instead of a furnace) convention based evaporator surfaces, where
water evaporates into steam. However, a HRSG can be equipped with a supplementary burner (as
can be seen in figure 12) for raising the flue gas temperature. A HRSG can have a horizontal or
vertical layout, depending on the available space.
When designing a HRSG, the following issues should be considered:
• the pinch-point of the evaporator and the approach temperature of the economizer
• the pressure drop of the flue gas side of the boiler
• optimization of the heating surfaces
12

The pinch-point (the smallest temperature Flue Gas
OUT
difference between the two streams in a system
of heat exchangers) is found in the evaporator,
and is usually 6-10 °C, which can be seen in Feedwater
Economizer IN
figure 13. To maximize the steam power of the
boiler, the pinch-point must be chosen as small
as possible. The approach temperature is the
temperature difference of the input temperature
Evaporator
in the evaporator and the output of the
economizer. This is often 0-5 °C. The pressure
drop (usually 25-40 mbar) of the flue gas side
has also an effect on the efficiency of power
Superheater
plant. The heat transfer of the HRSG is HP Steam
OUT
primarily convective. The flow velocity of the
flue gas has an influence on the heat transfer
coefficient.
Fuel
Supplementary burner
IN
The evaporator of heat recovery boiler can be of
natural or forced circulation type. The heat
exchanger type of the evaporator can be any of Flue Gas
IN
parallel-flow, counter-flow or cross-flow. In
parallel-flow arrangement the hot and cold fluids
Figure 12: Process scheme of single-pressure
move in the same direction and in counter-flow
HRSG with a supplementary burner.
heat exchanger fluids move in opposite
direction.
Heating surfaces of a heat recovery steam generator are usually heat transfer packages, which
consist of spiral-finned tubes. The thickness of the fin is 1-2 mm, the height 8-16 mm and the fin
distance 3,2-8 mm. Tube sizes vary a lot.
700
600
500
400
300
200
100
0
0 % 10 % 20 % 30 % 40 % 50 % 60 % 70 % 80 % 90 % 100 %
Share of heat load [%]
13
]C°[
erutarepmeT
Flue gas stream
Water/steam stream
Superheater Evaporator Economizer
Figure 13: Example of a heat load graph for a HRSG boiler.

Furnace dimensioning, stirred reactor
One of the most used furnace dimensioning methods is the stirred reactor model. The furnace is
approximated as being filled with a homogenous three-atom gas and a dust mixture at a uniform
temperature and pressure. At the furnace exit the temperature is decreased by a specified amount.
The stirred reactor furnace dimensioning process is as follows:
1. Guess initial furnace dimensions; shape, height, width, depth
2. Guess furnace exit temperature, T
exit
3. Calculate heat transfer using flue gas temperature T = T +∆T
fg exit
4. Calculate furnace exit temperature from heat balance with calculated heat transfer
5. If the mode does not converge, then return to step 2
6. If the calculated furnace exit temperature differs from the desired one, return to step 1
The typical values of ∆T to use for the different types of furnaces can be seen in table 5. The stirred
reactor model is not optimal for designing a recovery boiler furnace.
Table 5: Typical values of ∆T for various types of furnaces.
Boiler type ∆T [°C]
PCF (molten), coal 200 (100-300)
PCF (dry), coal 180 (100-250)
Grate firing, coal 130 (100-180)
PCF, lignite 120 (100-150)
Oil and gas 150 (100-200)
BFB 130 (100-150)
CFB 0
14

Superheater design
General
The production of steam at higher temperature than the saturation temperature is called
superheating. The temperature added to the saturation temperature is called the degree of superheat.
Superheated steam has no moisture; hence it is less erosive and corrosive than wet saturated steam
carrying droplets. In order to have a sustainable turbine operation, the steam cannot contain any
moist at all.
The design procedure for a superheater can be divided into the following steps:
• Tube size and material are chosen. Wall thickness is calculated.
• Flow velocity in tube is chosen, number of tubes is calculated, tube construction and width
of heat exchanger are chosen.
• Height of heat exchanger is calculated according to the chosen flue gas velocity.
• Internal heat transfer coefficient (for the inside, water side of the tube) is calculated.
• External heat transfer coefficient (for the outside, gas side of the tube) is calculated.
• Thermal resistance of dirt layer is calculated.
• Thermal resistance/tube length is calculated.
• Conductance is calculated
• Necessary tube length is calculated.
• Necessary number of passages is calculated.
• Assumed values are iterated.
• Main dimensions are calculated.
• Inside and outside pressure losses are calculated.
• Heat exchangers are drawn to the technical drawing of boiler.
Design velocity
Superheaters transfer heat from flue gas to steam. Heat transfer between two gases is not very
effective compared to heat transfer from gas to fluid. For that reason, steam must flow fast enough
(10-20 m/s) in order to give the superheater tubes enough cooling. Lower steam pressure weakens
the heat transfer rate, so with lower pressures, steam must have a greater velocity (15-40 m/s).
When flue gas is cooled, its volume decreases. In order to keep a constant flow rate of the flue gas,
the cross-sectional flow area decreases as well. In the radiant superheater, the velocity of gas is very
small (< 5 m/s). In the convection superheater, the velocity can be quite large (15-30 m/s). The
maximum velocity depends on the fuel used. To limit pressure-part erosion from fly ash, the flue
gas velocity must not exceed certain limits. Depending upon the ash quantity and abrasiveness, the
design velocity is generally 16-18 m/s. A furnace that burns coals yielding a heavy loading of
erosive ash (usually indicated by a high silica/aluminium content) may have a design velocity of
approximately 15 m/s. Such velocities are based on the predicted average gas temperature entering
the tube section, at the maximum continuous rating of the steam generator fired at normal excess-air
percentage.
15

Design spacing
Superheater of boiler consists of banks of tubes. A system of tubes is located in the path of the
furnace gases in the top of furnace. Heat transfer in superheaters is based mainly on radiation, but in
the primary superheaters convection often plays a major role.
A superheater must be built so that it superheats approximately the same amount of steam from low
to high loads. This can be achieved by a proper choice of radiative and convective superheating
surfaces. Changing tube lengths between passes can control temperature differences. The outermost
tube that receives the most radiative flux should be shorter than the rest of the tubes. Proper
superheater arrangement also eliminates much of the problems with uneven or biased flue gas flow.
Figure 14 and 15 shows examples of the arrangement of superheater and reheater surfaces in the
form of a process scheme.
Superheated
Steam OUT
Feedwater
IN
Saturated
Steam IN
Superheater III
Superheater II
Superheater I
Figure 14: An example of superheater block arrangements.
Superheated
Steam OUT
Reheated
Steam OUT
Feedwater
IN
Saturated Reheater
Steam IN IN
Reheater II
Superheater III
Superheater II
Reheater I
Superheater I
Figure 15: An example of superheater and reheater block arrangements.
16

Tube arrangement
Tubes in superheaters can be arranged according to inline or staggered arrangement (figure 16).
Inline tube arrangement is preferred for fouling boilers, PCF, bark and recovery. Staggered
arrangement is preferred for oil, gas and heat recovery steam generator. As free space with
staggered arrangement is much smaller than with inline arrangement the reason for decreased
fouling with inline is evident.
The superheater tube diameter is usually 30-50
mm. For convection heat surfaces the
dimension ‘a’ (figure 16) is 80-200 mm and ‘b’
is 60-150 mm. For radiation heat surfaces ‘a’ is
over 500 mm and ‘b’ is approximately the same
as the external tube diameter.
The number of tubes in the superheater is
calculated according to the average flow
velocity and volume flow. In the convection
superheater the width of the superheater is the
same as the width of the furnace. When the
number of tubes is known, all tubes are
preliminarily placed next to each other in the
flue gas channel. If the cross-sectional area of
the flue gas pass between two tubes (dimension
‘a’ in figure 16) becomes too small, the tubes
have to be placed in two or more rows.
17
wolf
sag
fo
noitceriD
Inline Staggered
enal
raelC
Figure 16: Inline and staggered tube
arrangement.

Economizer design
General
An economizer consists of an arrangement of tubes through which the feed water is passed
immediately before entering the boiler. The combustion gases leaving the boiler convection
surfaces pass over these tubes. As the entering feed water has a lower temperature than that of the
boiler steam, the heat transfer is more effective at this point than in the convection surfaces of the
boiler. This fact has prompted the present trend in boiler design to increase the economizer surface
and proportionally decrease the generator-heating surface. Economizers can be made of cast iron or
steel tube. Finned tubes are used, unless the flue gases origins from fuels with high ash content.
Design method
The following variables will be chosen
• Inside and outside tube diameters d and d , from which we can calculate the wall thickness:
i o
d −d
δ = o i (25)
2
• Distance of tubes in direction of flow and in side direction: s and s (named ‘a’ and ‘b’ in
1 2
figure 19)
• The size of flue gas channel: b and b
1 2
The number of tubes in one row (counter-flow) can then be calculated as:
b
M = 2 (26)
s
2
The cross-sectional area of the flue gas channel can then be calculated from equation 27.
A = b b – Md b (28)
fg 1 2 o 1
Holes of flow-through area combined circle are:
U = (M+1)*(2* b -2*(s - d )) (29)
1 1 o
The hydraulic diameter can then be calculated as:
4⋅A
d = fg (30)
h U
Then s /d , s /d , C and m can be read from charts. [2]
1 o 2 o
The average temperature of the economizer is:
T +T
T = fgsup fgeco (31)
f 2
18

The outside convection heat transfer coefficient is calculated from the following equation (turbulent
gas flow):
α d
Nu = oc h =C⋅Rem⋅Pr0,31
λ
fg
λ
-> α = fg ⋅C⋅Rem⋅Pr0,31 (32)
oc d
h
where λ is the thermal conductivity of the flue gas, Pr is Prandtl number, of flue gas, α the
fg o
outside convectional heat transfer coefficient and Re Reynolds number, which can be calculated as:
d ⋅w
Re = h fg (33)
ν
where w is the flue gas velocity in the flue gas channel, d the hydraulic diameter of the channel
fg h
and ν the kinematic viscosity of flue gas.
The needed tube surface area in the economizer can then be calculated as:
G
A= (34)
k
where G is the conductance (kW/K) and k the heat transfer coefficient, which can be calculated
according to equation 35:
1 d 1 δ
= o + + +m (35)
k dα α  δ  dirt
i i o 1− ⋅λ
 
d
 o 
where d andd are the inside and the outside tube diameter [m] respectively, α and α the inside
i o i o
and outside heat transfer coefficient respectively, δ the tube wall thickness, λ the thermal
conductivity and m the heat transfer resistance of a tube with a dirt layer on its surface. The
dirt
outside heat transfer coefficient is the sum of the outside radiative and convective heat transfer
coefficients:
α = α + α (36)
o oc rad
The surface area of one tube is:
A = π* d *b (37)
t o 1
The number of tube rows in depth direction is:
A
N = (38)
A ⋅M
t
19

And the depth of the economizer is:
h = N* s (39)
e 1
20

Air preheater design
The air preheater is design similarly to other heat transfer surfaces. The tubes of air preheaters are
larger than the tubes of superheaters and economizers: the diameter is about 50-80 mm.
Wall thickness is sized according to the strength of the construction, because the pressure difference
between air and flue gases is small. The lue gas velocity in the air preheater is 10-14 m/s in the
tubular heat exchanger type, 9-13 m/s in the plate heat exchanger type, 10-11 m/s in a finned tube
heat exchanger, and 13-15 m/s if both sides of the heat exchanger are finned.
In a vertical tube heat exchanger flue gas flows inside tubes and number of tubes can be chosen
according to the flue gas velocity and volume flow. By choosing suitable tube divisions, dimensions
of horizontal cross section of heat exchanger can be calculated. Air is flowing horizontally outside
tubes. By choosing air velocity height of heat exchanger can be calculated. According thermal
sizing length of heat exchanger can be found. In horizontal tube heat exchanger air flows inside
tubes and number of tubes can be chosen according to the air velocity and volume flow.
21

References
1. VDI Wärmeatlas
2. (Alvarez: Energiteknik, p. 368)
3. M. Huhtinen, A. Kettunen, P. Nurminen, H. Pakkanen, Höyrykattilatekniikka, Oy Edita Ab,
Helsinki 1994, ISBN 951-37-1327-X
4. Opetusmoniste kevät 2000: Ene-47.110 Yleinen energiatekniikka, erä 1, HUT
5. Opetusmoniste kevät 2000: Ene-47.124 Höyrykattilatekniikka, erä 1, HUT
6. Opetusmoniste kevät 2000: Ene-47.124 Höyrykattilatekniikka, erä 2, HUT
7. V. Meuronen, 4115 Höyrykattiloiden suunnittelu, Opetusmoniste 1999, LTKK, ISBN 951-
764-382-9
8. Combustion Fossil Power Systems
9. E.Vakkilainen, Steam boilers – Thermal design of boiler parts, lecture notes
22
