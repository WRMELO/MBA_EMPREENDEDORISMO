# Time_Averaged_Simulation_of_the_Furnace

**Fonte**: Time_Averaged_Simulation_of_the_Furnace.pdf  
**Data de conversão**: 2025-07-30 15:09:09  
**Origem**: base_relevantes

---

Engineering Conferences International
ECI Digital Archives
The 14th International Conference on Fluidization
Refereed Proceedings
– From Fundamentals to Products
2013
Time- Averaged Simulation of the Furnace of a
Commercial CFB Boiler
Juho Peltola
VTT Technical Research Centre of Finland, Finland
Sirpa Kallio
VTT Technical Research Centre of Finland, Finland
Hairui Yang
Tsinghua University, China
Xiaolong Qiu
Tsinghua University, China
Jingji Li
Tsinghua University, China
Follow this and additional works at:http://dc.engconfintl.org/fluidization_xiv
Part of theChemical Engineering Commons
Recommended Citation
Juho Peltola, Sirpa Kallio, Hairui Yang, Xiaolong Qiu, and Jingji Li, "Time- Averaged Simulation of the Furnace of a Commercial CFB
Boiler" in "The 14th International Conference on Fluidization – From Fundamentals to Products", J.A.M. Kuipers, Eindhoven
University of Technology R.F. Mudde, Delft University of Technology J.R. van Ommen, Delft University of Technology N.G. Deen,
Eindhoven University of Technology Eds, ECI Symposium Series, (2013). http://dc.engconfintl.org/fluidization_xiv/50
This Article is brought to you for free and open access by the Refereed Proceedings at ECI Digital Archives. It has been accepted for inclusion in The
14th International Conference on Fluidization – From Fundamentals to Products by an authorized administrator of ECI Digital Archives. For more
information, please contactfranco@bepress.com.

TIME- AVERAGED SIMULATION OF THE FURNACE OF A
COMMERCIAL CFB BOILER
Juho Peltolaa*, Sirpa Kallioa, Hairui Yangb, Xiaolong Qiub and Jingji Lib
aVTT Technical Research Centre of Finland;
Metallimiehenkuja 6, Espoo; P.O.Box 1000; FI-02044 VTT, Finland
bTsinghua University, Department of Thermal Engineering
Haidian District, Beijing, China
*T: +358 20 359 1860; F: +358 20 722 7077; E: juho.peltola@vtt.fi
ABSTRACT
A time-averaged simulation approach is applied to a 135 MWe circulating
fluidized bed combustor located in Ruzhou, China, in which also measurements
were carried out. The simulation results show a vertical solids distribution typical
for a CFB. Gas composition profiles show plausible but not fully correct
distributions of oxygen and combustion products inside the furnace.
INTRODUCTION
Dense gas-solid flows are usually computed as time-
dependent requiring a small time step and a fine mesh
which lead to time-consuming simulations. To reduce
computing time, Taivassalo & al. (1) introduced a time-
averaged CFD model and in Taivassalo & al. (2), the
approach was applied on CFB combustion in Chalmers 12
MW boiler. In addition to hydrodynamics, models for heat
transfer and chemistry, including homogeneous and
heterogeneous reaction mechanisms, were included in
the modeling. The behavior of fuel particles was simulated
with a Lagrangian approach.
The time-averaged simulation approach is applied to a
135 MWe circulating fluidized bed combustor located in
Ruzhou, China, to examine how the modeling approach
behaves in a commercial scale CFB. A measurement
campaign was carried out at 120 MWe load. In the paper,
results from the simulations are presented and compared
with measurement data, including pressure and Figure 1. Boiler
geometry
temperature distributions and gas composition data.
MEASUREMENTS AND SIMULATION SETUP
The combustion chamber geometry of the Ruzhou power plant is shown in Figure
1 in the simplified form in which it is described in the CFD simulation. The conical
bottom section of the furnace is refractory lined while other walls are membrane
walls. The figure also shows the six hanging super heaters and four re-heaters in
the upper part of the furnace. In the middle of the furnace there is a membrane
wall that to a large extent splits the furnace in two sections. This allows flexible

furnace operation. In the case measured and simulated in the present work, more
fuel and secondary air was fed to one side of the furnace.
In the boiler, coal is fed through six coal feeders located on the front wall.
Secondary air enters from two levels at the front and back walls and some air
also enters from the sides of the furnace from the four ash coolers located next to
the corners of the furnace. The furnace is equipped with two cyclones, of which
only the exit and return channels, shown in the picture, are included in the
simulated domain.
Primary and secondary air flows into the furnace and coal feed rates are listed in
Table 1. The primary air flow is 41% of the total air flow, which in this geometry
results in a relatively low primary fluidization velocity (1.96 m/s at assumed 800
°C temperature). The total coal feed rate is adjusted on basis of the oxygen
balance based on the measured O concentration in the backpass.
2
Table 1. Air and fuel flow rates.
Air Primary To coal To ash To loop seal Upper Lower
flow feeders coolers secondary secondary
Left Right Left Right Left Right
kg/s 46.5 4.7 10.7 0.34 0.35 21.7 9.2 19.1 11.0
Fuel flow Feeder 1 Feeder 2 Feeder 3 Feeder 4 Feeder 5 Feeder 6
kg/s 6.3 7.9 8.1 7.9 4.0 3.0
The fuel used in the experiments was a local high ash coal. Its size distribution
and primary fragmentation tendency were measured. The initial size distribution
and the distribution after primary fragmentation, which was used as an input to
the simulation, are shown in Table 2.
Table 2. Particle size distribution of coal before and after primary fragmentation.
Size, mm 0.0 - 0.5 0.5 – 1.0 1.0 – 2.0 2.0 - 3.2 3.2 – 6.0 > 6.0
Before, % 28.7 13.9 25.1 15.2 10.1 7.0
After, % 31.2 16.2 26.3 11.1 8.5 6.7
The chemical composition of the fuel is listed in Table 3. The heating value of the
fuel is 7.7 MJ/kg (a.r.).
Table 3. Fuel analysis
Volatiles Proximate [wt% a.r.] Ultimate [wt% daf]
[wt% daf] Comb. Ash Moist. C H O S N
41.7 32.6 62.6 4.8 56.9 7.7 32.1 1.8 1.6
Pressure and temperature profiles, flue gas composition and heat exchanger
data were collected during the experiment from the control system. A bottom ash
sample was taken for analysis of particle size distribution and the amount of
unburned in each size fraction. Additional measurements were carried out at four
distances from the wall through four measurement ports on the right side wall of
the furnace. The first measurement location was at 17.9 m height, the second at
27.4 m height, the third in the cyclone inlet channel at 30.6 m height and the
fourth at cyclone outlet. In addition to measurements of temperature and gas
composition, a suction probe was used to take samples of the solids.

The measurements were conducted in between normal power plant operation so
that the time the power plant was kept at the studied condition was only a few
hours. Thus the bed inventory and particle size distribution differ from what would
prevail at steady state.
MODELING
Hydrodynamic model for gas-solid suspensions
A steady-state CFD modeling approach based on time-averaged Eulerian-
Eulerian equations for hydrodynamics of gas-solid suspensions was introduced in
Taivassalo et al. (1). Time-averaged continuity and momentum equations were
developed by averaging the corresponding time-dependent equations over time
and, by ignoring density fluctuations, they can be summarized for a phase q as
follows
Ñ×ra U = 0 (1)
q q q
Ñ×a r U U =a r g-a Ñp-a¢Ñp¢+Ñ×a τ +Ñ×a τM
q q q q q q q q q q q q
(2)
+(-1)(d qs +1)K ( u -u ) -d Ñp -Ñ×rau" u"
gs g s qs s q q q q
Here ρ is the density, α volume fraction, p pressure, p solid pressure, g
s
gravitational acceleration, K inter-phase momentum transfer coefficient,
Kronecker delta, laminar stress, and local-scale turbulent stress. The time
average, also called the Reynolds average, of a variable is denoted by a(cid:2012)n (cid:3034) d (cid:3046)
(cid:3014)
the fluctuation par(cid:2254)t by . In the(cid:2254) equations above, u is the instantaneous
velocity, is the Favre average or phase-weighted a(cid:2030)verage velocity(cid:2030) (cid:3364) =
(cid:4593)
and (cid:2030) = (cid:2030)is −th(cid:2030)e(cid:3364) velocity fluctuation. The gas phase is denoted
(cid:1795)(cid:3044) (cid:1795)(cid:2199)
by g and solid p(cid:4595)hase by s.
(cid:3364)(cid:2009)(cid:3364)(cid:3364)(cid:3044)(cid:3364)(cid:1821)(cid:3364)(cid:3364)(cid:2199)(cid:3364)⁄(cid:2009)(cid:3364)(cid:3364)(cid:3364)(cid:3044)(cid:3364) (cid:1821)(cid:3044) = (cid:1821)(cid:3044) −(cid:1795)(cid:3044)
Equation (2) contains a number of terms that need to be modeled. Compared to
the transient equations, the averaging process produces new terms due to
correlations between fluctuations in velocities, volume fractions, pressure and
local stresses. The terms on the right hand side in Equation (2) are, from left to
right, the gravitation, pressure, pressure fluctuation, laminar stress, turbulent
stress, drag force, solid pressure, and Reynolds stress terms. The gravitation and
pressure terms can be directly calculated from the time-averaged flow properties
but for the rest of the terms closure relations need to be developed. In Taivassalo
et al. (1), closure relations were derived on the basis of transient simulation data.
Taivassalo et al. (1) solved only the normal Reynolds stresses for the solid phase
from balance equations, while in the present work also the cross terms are
included in a similar manner. The other terms are modeled through algebraic
correlations. In the description of mixing in the gas and solid phases, correlations
for the time scales of the velocity fluctuations based on the results of Peltola &
Kallio (3) are employed.
Homogenous chemistry
In the time-averaged transport equation for a gas-phase species, the velocity
fluctuations (Reynolds stresses) and their time scales are used to estimate a

local value for an isotropic dispersion coefficient needed in the calculation of the
dispersion flux. The gas phase is described as a mixture of seven species, O ,
2
N , CO , CO, H O, H and a general volatilized gas CHO that represents the
2 2 2 2 x y
complex gas mixture released during devolatilization. In this work, the complex
gas-phase chemistry is modeled by the following net reactions
R1: CH O + (x/2+1-y)/2 O -> CO + x/2 H O
x y 2 2
R2: CO + 0.5O -> CO
2 2
R3: H + 0.5 O -> H O
2 2 2
The time-averaged reaction rates are assumed to be limited by the gas-phase
mixing approximated by an isotropic dispersion coefficient. The time-averaged
mass-weighted mass fractions are used as such in the calculation of the reaction
rates.
Modeling fuel particles
The Lagrangian particle tracking approach is employed in this work to represent
the complex and varying behaviour of different kind of reactive particles with
broad size distributions. The drag forces on the tracked particle due to interaction
with both (solid and gas) phases are taken into account. The solid-phase average
velocity field, velocity fluctuations and time scales are used in determining the
instantaneous velocity components for the tracked particle. For the drag force
between the fuel particles and the Eulerian solid phase, the model of Syamlal (4)
is applied. Large fuel particles leaving the furnace that are assumed to be
separated by the cyclone, are returned to the furnace with the solid bed material.
Evaporation, devolatilazation, combustion and gasification of the fuel particles
are modelled with the approach presented by Taivassalo et al. (2)
Heat transfer
In the simplified time-averaged energy balance equation, the magnitude and time
scales of the velocity fluctuations are used to predict a representative value for
the isotropic heat transfer coefficient. In the calculation of the heat exchange
coefficient h , the model of Gunn (8) is used to evaluate the Nusselt number.
sg
The heat transfer coefficient between the gas-solid suspension and the walls is
evaluated utilizing the model of Nirmal Vijay and Reddy (9).
Simulation
The Ansys Fluent 14 (Ansys, 10) code was used to obtain a steady-state solution
of the coupled transport equations, Eqs. (1), (2), (3) and (4) as well as the
corresponding transport equation for the Reynolds stresses, and to carry out the
tracking of representative fuel particles. In addition, in the current case the
simplest radiation model, the P1 model, of Fluent was activated and the solids
volume fraction was used to evaluate the dispersion and scattering coefficient. In
typical CFB conditions, the range of visibility is so short that even the P1 model,
suitable for optically thick media (Ansys, 10), is considered satisfactory. The
computational mesh consisted of approximately 2 million elements.
A major weakness of the Eulerian model used in the present work is the
assumption of a single, locally fixed particle size. To approximate the distribution
of particles of different size in the furnace, the particle diameter was set as a
function of riser height. At the bottom the size was set at 0.45 mm on basis of an

analysis of bottom ash samples and at the top at 0.117 mm, which was roughly
the median size in the samples taken at 17.9 m height. Such an approach means
that to local mean particle diameter has to be chosen a priori and it is not affected
by changes in the flow solution. This kind of modelling approach should only be
considered as a temporary approximation to allow development of the other
submodels. The present simulation is particularly sensitive to this limitation,
because the low primary fluidization velocity causes a steep mean diameter
change above the bottom bed, as the gas velocity is too low to lift anything but
the small particles.
The bed mass was estimated from the measured pressure profile. Outlet
boundary pressures are set the same for both outlets, because the pressure
measurement provided by the automation system for the left outlet was not
credible
RESULTS AND DISCUSSION
The Lagrangian description of the fuel particles proved very time consuming in
such a large boiler. The fuel particles spend considerable time in the boiler which
requires a large number of time steps to be calculated for each particle. As the
results affect the Eulerian flow solution, iteration between the Eulerian and
Lagrangian results is required. It might be possible to reduce the computational
effort by optimizing to code, but this may require a different modelling platform.
The higher air and fuel mass flows in the left half of the furnace produce
asymmetric velocity and temperature fields as seen as higher flow velocities and
temperature in Figure 2. Generally there is a falling wall layer of solid on all the
walls and heat exchangers. The secondary air inlets tend to form high velocity
vertical channels all the way to the outlets. There is significant variation in the
wall layer thickness in different locations, but since no velocity profile data is
available from the furnace, there is significant uncertainty in the assessment of
the correctness of the results.
(a) (b) (c)
Figure 2. Contours of simulated gas (a) and solids (b) vertical velocities [m/s] and
gas temperature [°C] (c).

Similar asymmetry can be seen in the volume fraction contours of Figure 3. When
the vertical pressure profiles are compared to the measured ones, the
measurements show much stronger asymmetry. Because credible pressure data
was available only for the right outlet, it is unclear if the assumption of the same
pressure at both outlets is valid. However, the overall trend of the pressure profile
matches well with the measurements.
Figure 3. Solids volume fraction contour and comparison of simulated pressure
profiles to measured values.
Figure 4. Comparison of simulated vertical gas temperature, O and CO
2
concentration profiles to measured values.
Figure 4 shows a comparison of measured temperatures and O and CO
2
concentrations to selected vertical profiles from the simulation. The measurement
locations do not coincide exactly with the sampling lines of the simulation in all

locations. The simulated profiles are quite uneven, showing sharp local variations
in the temperature and species concentrations. This may be a symptom of
inadequate number of Lagrangian fuel particles. Highest temperatures have been
measured at 17.9 m height, but the simulated temperatures are generally lower
than measured.
The vertical oxygen concentration profiles show a region of low oxygen below the
secondary air level. At the measurement location near the walls the simulated
oxygen concentrations are higher than measured. This is probably an indication
that the vertical channels formed by the secondary air jets in the simulations may
not be as strong in the real boiler. There is a lot of variation in the vertical CO
profiles, but if any conclusion can be drawn, at the measurement locations the
results are in similar range.
CONCLUSIONS
A steady-state simulation approach was applied to a 135 MWe circulating
fluidized bed combustor to examine its behavior in a commercial scale CFB. The
results were presented and compared with measurement data from a
measurement campaign carried out at the power plant. Temperature, pressure
and gas composition data was compared with measurements.
While the Eulerian time-averaged simulation is quite fast, iterating the Eulerian
solution and the Lagrangian simulation of the fuel particles proved very time
consuming in a large boiler. There is a possibility for some improvement by
optimizing the Lagrangian particle code, but it is likely that if a Lagrangian fuel
description is used, the Lagrangian portion of the simulation will remain as the
limiting factor for simulation speed.
The simulation results show the typical characteristics of a CFB, i.e. a dense
suspension region at the furnace bottom and more dilute conditions higher up.
Dense, falling layers of solids are found on the walls and heat exchangers. The
asymmetric fuel and air inlets produce an asymmetric flow field also in the
simulation, but the difference is not as large as in the pressure measurements. In
the simulation, the pressure boundary condition was uniform at both outlets,
because credible pressure measurement data was available only from the right
outlet. The general trend of the pressure profiles matches well with the
measurements.
Gas composition profiles show local variation, possibly due to an inadequate
number of Lagrangian fuel particles. Simulated oxygen concentration at the near-
wall measurement locations is higher than measured, indicating that the near-
wall channeling effect of the secondary air may be over predicted in the
simulation.
The observed probable discrepancies to reality can be a consequence of the
fixed vertical mean particle diameter profile and of the limited amount of data
used as basis for the derivation of equation closures for the time-averaged
balance equations. The present simulation is particularly sensitive to the fixed
particle diameter approximation, because the low primary fluidization velocity
creates a very steep mean diameter gradient above the bottom bed, as the gas

velocity is too low to lift anything but the small particles. The small particle size in
the upper furnace is outside the parameter range used in the closure derivation
and thus the closures should in the future be extended to smaller particle sizes.
Similarly, new data on flow behavior near secondary air streams is needed to
improve the models. All in all, the results demonstrate a need for a better
modeling of the solids size distribution and sensitivity of the closure models to
changes in the operational conditions.
ACKNOWLEDGMENT
The authors gratefully acknowledge the financial support of Tekes, VTT
Technical Research Centre of Finland, Etelä-Savon Energia Oy, Fortum, Metso
Power Oy and Numerola Oy, and the support from Saarijärven Kaukolämpö Oy.
The invaluable contribution of the powerplant personnel and the assistance of all
the people participating in the experiments are gratefully acknowledged.
NOTATION
g gravitational acceleration α volume fraction
K drag coefficient δ Kronecker delta
ij
p pressure ρ density
u velocity σ standard deviation
x spatial coordinate τ stress
REFERENCES
1. Taivassalo, V., Kallio, S., Peltola, J., On time-averaged CFD modeling of
circulating fluidized beds, accepted for presentation at the 12th Int. Conf.
Multi-Phase Flow in Industrial Plants, Ischia, Italy, September, 2011.
2. Taivassalo, V., Peltola, J., Kallio, S., Time-averaged CFD modeling of a
circulating fluidized bed combustor, FBC21, Naples Italy, 2012.
3. Peltola, J., Kallio, S.: Estimation of turbulent diffusion coefficients in a CFB on
basis of transient CFD simulations, FBC21, Naples Italy, 2012.
4. Syamlal, M.: The particle-particle drag term in a multiparticle model of
fluidization. National Technical Information Service, Springfield, VA, USA.
DOE/MC/21353-2373,NTIS/DE87006500 1987 (referenced in Ansys Inc.,
2010).
5. Palchonok, G.: Heat and Mass Transfer to a Single Particle in Fluidized Bed,
Doctoral thesis, CTH, Sweden, 1998.
6. Ross, D.P., Heidenreich, C.A., and Zhang, D.K.: Devolatilisation times of coal
particles in a fluidised-bed. Fuel 79 (2000) 873-883.
7. Konttinen, J., Kallio, S., Kilpinen, P.: ”Oxidation of a single char particle –
Extension of the model and re-estimation of kinetic rate constants”, Report
02-4, Åbo Akademi University, Process Chemistry Group, 2002.
8. Gunn, D.J.: Transfer of heat or mass to particles in fixed and fluidized beds,
Int. J. Heat Mass Transfer, 21 (1978) 467-476 (in Ansys Inc., 2010).
9. Nirmal Vijay, G., Reddy, B.V.: Effect of dilute and dense phase operating
conditions on bed-to-wall heat transfer mechanism in a circulating fluidized
combustor. Int. J. Heat and Mass Transfer 48 (2005) 3276-3283.
10. Ansys inc.: Ansys FLUENT theory guide, Release 14.0, 2011.
