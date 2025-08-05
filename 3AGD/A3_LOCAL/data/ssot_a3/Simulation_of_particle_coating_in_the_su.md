# Simulation_of_particle_coating_in_the_su

**Fonte**: Simulation_of_particle_coating_in_the_su.pdf  
**Data de conversão**: 2025-07-30 15:10:18  
**Origem**: base_relevantes

---

CHINA PARTICUOLOGY Vol. 3, Nos. 1-2, 113-124, 2005
SIMULATION OF PARTICLE COATING
IN THE SUPERCRITICAL FLUIDIZED BED
Carsten Vogt, Ernst-Ulrich Hartge*, Joachim Werther and Gerd Brunner
Technical University Hamburg-Harburg, D21071 Hamburg, Germany
Author to whom correspondence should be addressed. E-mail: hartge@tu-harburg.de
Abstract Fluidized bed technology using supercritical carbon dioxide both as a fluidizing gas and as a solvent for the
coating material makes possible the production of thin, uniform and solvent-free coatings. But operation at low fluidizing
velocities, which is favorable to facilitate gas cleaning under the high pressure conditions, may lead to uneven distribution
of the coating in the fluidized bed and to unstable operation due to agglomeration. Therefore a model has been devel-
oped which describes local fluid dynamics within the high pressure fluidized bed. Based on this model, the coating
process is described and the distribution of the coating inside the fluidized bed is calculated. Furthermore a submodel for
the calculation of local concentrations of liquid paraffin has been set up, which may be used as a basis for the prediction
of agglomeration and thus stability of operation.
Keywords particle coating, fluidized bed, supercritical fluid, fluid mechanics
1. Introduction parameters for uniform coating, a mathematical model of
the process was formulated and validated with experi-
Coating of particles finds application in, amongst others,
mental results. The model was adapted to the process
the protection of high-value products, the encapsulation of
operated by Schreiber et al. (2002a). They studied as an
hygroscopic or toxic substances, and in the selective or
example the coating of glass beads with paraffin. A sche-
controlled release of drugs in the pharmaceutical industry
matic diagram of their experimental setup is shown in Fig.1.
(Kleinbach & Riede, 1995).
Into a fluidized bed of glass beads operated with CO un-
2
Fluidized bed technology using supercritical carbon di-
der supercritical conditions (8 MPa, 313 K) CO is injected
2
oxide both as a fluidizing gas and as a solvent for the
which is saturated with paraffin at a pressure of 24 MPa
coating material makes possible the production of thin,
and a temperature of 343 K. The injection nozzle is posi-
uniform and solvent-free coatings. Solubility in supercritical
tioned about 15mm above the gas distributor on the cen-
carbon dioxide can be varied easily by changing pressure
terline of the fluidized bed.
and/or temperature, down to practically zero at ambient
conditions. Besides, the reduction of surface tension at
high pressures makes the production of thin and smooth
coatings possible. Because of the comparatively low criti-
cal temperature of carbon dioxide of 304 K, coating can be
realized at relatively low temperatures, thus enabling the
coating of temperature-sensitive substances. Therefore,
the combination of the advantages of the fluidized bed
(good solids mixing, reduced risk of agglomerate formation)
with the potentials of a supercritical fluid constitutes a very
promising process for the production of coatings.
The process described in this work follows the RESS
(Rapid Expansion of Supercritical Solutions) process
(Tsutsumi et al., 1995) with the modification that a super-
critical solution is expanded into supercritical carbon diox-
ide. Previous work (Schreiber et al., 2002a) showed that
very thin and uniform coatings could be produced using Fig.1 Sketch of the experimental setup used by Schreiber et al.
this method, though often the coatings were incomplete (2002b).
and agglomerates tended to build up, primarily because of
insufficient mixing in the fluidized bed due to the low gas For modelling of fluid mechanics of fluidized beds dif-
velocities used. Gas velocities had to be as low as possible ferent approaches are widely used. Semi empirical ap-
in order to prevent solids entrainment and thus to minimize proaches like the two-phase models (e.g. Werther & Wein,
the requirements on expensive gas cleaning under the 1994) offer the advantage of low requirements for compu-
high pressure conditions. tational resources and good accuracy for standard ge-
To acquire more insight into the coating process, the ometries and conditions. A disadvantage of these models
fluid mechanics of the fluidized bed and the governing is that they usually assume uniform flow patterns across

114 CHINA PARTICUOLOGY Vol.3, Nos.1-2, 2005
the bed. Thus the influence of a strong jet on the solids solids and the adjacent bubble wake (Fig.2). This bubble
flow inside a fluid bed cannot be simulated. On the other rises in a surrounding suspension phase, which is kept in
hand, there are other models using methods of computa- the fluidized state by the percolating gas. The suspension
tional fluid dynamics (CFD). Here Euler-Euler-approaches phase is treated as a continuous fluid. Thus the flow of this
or two-fluid models (TFM) have to be distinguished from fluid can be modelled by means of the Navier-Stokes
Euler-Lagrange approaches and from the special case of equations and mass balance.
the discrete particle modelling (DPM).
The Euler-Euler approach treats the solids as a pseudo
suspension phase
continuous phase. To model particle-particle interactions in
this pseudo-continuous phase, generally the granular the-
ory (e.g. Gidaspow, 1994) is used. Up to now the use of
TFM is restricted to Geldart group B particles, while the
bubble phase
fluidized bed under supercritical conditions behaves more
like a Geldart group A system. The classical
Euler-Langrange approach can not be used for dense Fig. 2 Two-phase model of fluidized bed: the bubble phase consists
fluidized beds, since for the simulation of the movement of of a solids-free void and the wake adjacent to the void.
individual particles within a given gas flow field only the
Since the reactor to be modelled is cylindrical and ra-
interactions between particles and gas are considered
dially symmetrical, radial symmetry was assumed and the
while direct particle-particle interactions are neglected.
model was formulated in polar coordinates. The original
While this approach is valuable for systems with low solids
model by Kobayashi et al. (2000) has been extended by
volume concentrations, direct particle-particle interactions
the consideration of solids transport by the bubble wake.
dominate the flow in dense fluidized beds.
The most fundamental approach among the above men- Suspension phase
tioned models is the DPM approach. Here all individual The density of the suspension or emulsion phaseρ
e
particles are tracked simultaneously and collisions be-
can be calculated by
tween particles are calculated (e.g. Li & Kuipers, 2003; Ye
ρ =ερ+(1−ε)ρ, (1)
et al., 2004). The major drawback of this approach is the e e f e s
very high requirement for computing resources and the from the gas density ρ=f(p,T) and the solids densityρ,
f s
limitation in the maximum number of particles which can be
treated, e.g., about 105~106 particles, while the actual when the porosity within the emulsion phase ε e is known.
number of 100 µm particles in a fluidized bed, 10 cm in The porosity of the suspension phase ε was found ex-
e
diameter and 10 cm in height, is in the order of 109. perimentally in a former work (Vogt et al., 2005) to be in-
Therefore this approach is yet not suited for reactor mod- dependent of pressure. For the glass beads with a mean
elling. surface diameter d =169μm, which are used for the
p,s
Some kind of compromise is a model suggested by
model validation, the measured suspension porosity was
Kobayashi et al. (2000), which computes the movement of
found to be ε =0.525.
bubbles in a fluidized bed on the basis of empirical corre- e
lations for their rise velocity, for their coalescence, and for Fig.3 depicts the flow of the suspension phase into and
the interaction between neighbouring bubbles. In contrast, out of a single volume element. The mass balance can
the surrounding dense suspension (emulsion) phase is accordingly be formulated as the change of mass within
modelled as a pseudo fluid with CFD-methods. A modified the volume element with time minus the sum of in- and
model has been used by Bruhns and Werther (2005) for out-flowing mass flows:
the 3D-simulation of the injection of liquids into a fluidized
bed. The model used in the present paper will follow the
s l
w
a a
e
t T i m
t
o o
ti
n e
n
s
g
o a i f m p
a
t p h u
n
r e l
d
o a a t s e
f
c o
o
h l
r
t i , d h
t
s e s
h
i n i
e
n c c d o e
s
u a
o
c t i
l
t i
i
e n
d
a d g
i
l
f
l
i
o b
c
p w
a
y r o
t
s a
io
c d e
n
lo e s c s s
o
a c
f
l i r l t y i
t
s b
h
e i i
e
n n l f j g e
p
a c
a
t h t
r
e m e
a
d
f
o
f
g
i
j d
n
e ro e t. s l
u
s
s
f o
e
c r
d
i r t c h
b
u e
y
- ⎜⎜
⎝
⎛⎛ ⎜⎜
⎝
ρρ
ee
v⋅v
zz
++ ∂∂(ρρ
∂z
e
∂
e v
z
⋅ z v) zdzdz ⎞ ⎟⎟
⎠
⎟⎟
⎠
⎞ (1⋅(1−−ε
b
ε)
b
⋅)d⋅rdr⋅2⋅2ππ ⎜⎜ ⎝ ⎛ r ⎝ ⎜⎜ ⎛ r ρρ ee v⋅v rr ++ ∂∂( r rrρ ⋅r ⋅ ∂ e ρ ⋅r v ∂ er r ⋅)v drr ⎠ ⎟⎟ ⎞ d(r1 ⎠ ⎞ ⎟⎟−⋅(ε1 b −)ε⋅d b )z⋅⋅d2zπ⋅r2π r
Schreiber et al. (2002a) as coating is added.
2. Theory
ρρee ⋅vv
rr
(⋅11−−ε
b
ε) b⋅d⋅zdz⋅2⋅2ππrr
2.1 Fluid mechanics of the fluidized bed
The model approach used here assumes the existence bubble-volume fraction εε
of two phases, a bubble phase and a suspension phase, ρρee ⋅vv
zz
(⋅11−−εε
b
) b⋅⋅ddrr⋅⋅22ππrr bb
respectively. The bubble phase consists of voids free of Fig. 3 Flows into and out of the suspension phase in a volume element.

Vogt, Hartge, Werther & Brunner: Simulation of Particle Coating in the Supercritical Fluidized Bed 115
∂ ( ρ e ( ∂ 1 t −ε b )) + 1 r ∂ ∂ r ( rρ e (1−ε b )v r ) + ∂ ∂ z ( ρ e (1−ε b )v z ) =m(cid:5) e . C tio O n 2 s a ( t C 4 O 0 2 ° C a a t n 4 d 0 8 ° 0 C b a a r n : d η 1 = b 2 a .2 r: × 1 η 0− = 4 1 k . g 6 ⋅( × m 1 - 0 1 − ⋅ 4 s- k 1) g ) ⋅ , ( m an -1 d ⋅s t - h 1) e ;
(2) influence of solids properties dominates the viscosity of the
Here the velocity of the suspension phase is denoted by emulsion phase. Therefore measurements by Grace (1970)
v in radial direction andv in vertical direction; m(cid:5) denotes under ambient conditions (cf. Table 1) have been used to
r z e
determine, by interpolation, the dynamic viscosity.
sources and sinks within the emulsion phase and ε is
b
the volume fraction of the bubble phase.
Table 1 Viscosities of suspension phase measured with air as fluid-
Also the Navier-Stokes equation is written in cylindrical
izing gas at ambient conditions (Grace, 1970)
coordinates. Kobayashi et al. (2000) neglected the con-
Density Particle size Viscosity
vective momentum transport in their model in order to re- Type of solids
ρ (kg⋅m-3) d μm η Pa⋅s
duce computational requirements and to improve the s p,s e
convergence of the solution. This simplification is possible Quartz sand 2650 72 0.7
Quartz sand 2650 140 0.9
when the fluid has high viscosity and only small velocity
Quartz sand 2650 330 1.3
gradients. Since in the present case of jet injection high
velocity gradients occur in the vicinity of the jet, this simpli-
To solve the system of differential equations, boundary
fication was not possible. Thus the momentum transport in
conditions for pressure and for velocities of the suspension
radial direction is described by
phase have to be given. For the pressure boundary, condi-
∂(ρ(1−ε)v ) ∂(ρ(1−ε)v ) ∂(ρ(1−ε)v )
tions of the Neumann type can be formulated for the outer,
e b r +v ⋅ e b r +v ⋅ e b r =
∂t z ∂z r ∂r inner, upper and lower boundaries of the calculation do-
∂p ∂((1−ε)τ ) 1∂(r(1−ε)τ ) (1−ε)τ main, that is, the component of the suspension velocity in
− ∂r + ∂z b rz + r ∂r b rr − r b φφ+F r −m(cid:5) e v r , normal direction to the boundary is zero, and thus the
(3) pressure gradient normal to the boundary has to be zero:
and in vertical direction by ∂p ∂p
=0 =0
∂(ρ(1−ε)v ) ∂(ρ(1−ε)v ) ∂(ρ(1−ε)v ) ∂z ∂z
e b z +v ⋅ e b z +v ⋅ e b z = z=0 z=zmax . (7)
∂t z ∂z r ∂r ∂p ∂p
=0 =0
∂p
∂((1−ε)τ ) 1∂(r(1−ε)τ )
∂r ∂z
−
∂z
+
∂z
b zz +
r ∂r
b zr −ρ
e
(1−ε
b
)⋅g
z
+F
z
−m(cid:5)
e
v
z
. r=0 r=rmax
At the upper bound additionally a Dirichlet boundary
(4)
condition can be given with
Here F and F are external forces in the radial and
r z p(z )=p . (8)
vertical directions and p denotes the local pressure. For max abs
To set the boundary conditions for the velocities, it is
Newtonian fluids in a radially symmetric system the tension
assumed that there is no friction in the suspension phase
terms in normal directions are given by
at the inner (center) and the upper (bed surface) bounda-
τ
zz
=2⋅η
e
⋅ ∂
∂
v
z
z −
3
2 ⋅η
e
⋅⎜⎜ ⎛
⎝
1
r
∂(r
∂
⋅
r
v r ) + ∂
∂
v
z
z⎟⎟ ⎞
⎠
r
r
i
i
e
e
s
s
.
a
T
re
h u
s
s
e t
t h
to
e
z
v
e
e
r
l
o
o
:
c ity gradients parallel to these bounda-
τ rr =2⋅η e ⋅ ∂ ∂ v r r − 3 2 ⋅η e ⋅ ⎛ ⎜ ⎜ ⎝ 1 r ∂(r ∂r ⋅v r ) + ∂ ∂ v z z ⎞ ⎟ ⎟ ⎠ , (5) ∂ ∂ v z r z=zmax =0 ∂ ∂ v r z r=0 =0. (9)
v 2 ⎛1∂(r⋅v ) ∂v ⎞ At the walls friction between suspension phase and wall
τ φφ =2⋅η e ⋅ ∂r r − 3 ⋅η e ⋅ ⎝ ⎜ ⎜r ∂r r + ∂z z ⎠ ⎟ ⎟ is assumed according to Ding et al. (1992):
∂v ∂v
and in tangential direction by v zr=rmax =−λ⋅ ∂r z v r z=0 =−λ⋅ ∂z r . (10)
τ rz =τ zr =η e ⋅ ⎝ ⎜ ⎛∂ ∂ v z r + ∂ ∂ v r z ⎠ ⎟ ⎞ , (6) se F t u to rt h ze e r r o m o fo re r a th ll e b o v u e n lo d c a it r i i e e s s , n i o .e rm . n a o l t s o u t s h p e e n b s o i u o n n d f a lo ri w es s a o r u e t
whereη is the dynamic viscosity of the emulsion. The of the calculation domain:
e
viscosity of the suspension has a significant influence on v r r=0 =0 v zz=0 =0 . (11)
the simulation results. It may be determined either by fitting v =0 v =0
the model to experimental data or it can be taken from
r r=rmax zz=zmax
independent measurements which can be found in the Bubble phase
literature. Although no such measurements are available The mass balance for the bubble phase with volume
for fluidized beds under supercritical conditions, meas- fraction ε is given by
b
urements at ambient conditions may be used as an ap- ∂(ρ ε) 1∂(ρ εru ) ∂(ρ εu )
proximation since the viscosity of the fluidizing gas at su- bub b + bub b r + bub b z =m(cid:5) , (12)
∂t r ∂r ∂z bub
percritical conditions is close to that under ambient condi-

116 CHINA PARTICUOLOGY Vol.3, Nos.1-2, 2005
where the velocity of the bubble phase is denoted as u, for a 2-dimensional model as in this work, since the num-
and m(cid:5) is a source or sink within the bubble phase. The ber of the bubbles over the whole cross-section of the
bub
fluidized bed is needed to calculate the interactions.
density of the bubble phase ρ is the mean density
bub Therefore the correlation by Bruhns and Werther (2005)
averaged over the solids-free void and the wake. Assum-
has been modified such that the bubble volume fraction
ing that the fraction of the bubble volume taken by the
instead of the number of bubbles in a volume element is
wake is constant for all bubbles, the mass balance can be
used. With this modification the correlation for the radial
simplified to
drift velocity is given by
∂ε b + 1∂(ε b ru r ) + ∂(ε b u z ) = m(cid:5) bub . (13) 1rmaxϕmax 1 ⎛ 1a2 ⎞
∂t r ∂r ∂z ρ bub u d,r = 2 ∫ 0 ∫ 0 ε b ′s r u z ⋅ 2πD b ′2 ⋅exp⎜ ⎝ − 2D s b ′2 ⎟ ⎠ dϕ′⋅r⋅dr′, (17)
The absolute velocity of the bubble phase in the (vertical)
where a is the distance between the centers of the two
z-direction is defined as s
u =(u −u )+u +v , (14) bubbles (cf. Fig.4) and s is the distance in radial direc-
z 0 e b z r
tion. These values can be calculated from
where u is the superficial gas velocity and u is the
0 e a2 =(r′⋅cosϕ′−r⋅cosϕ)2+(r′⋅sinϕ′−r⋅sinϕ)2, (18)
superficial velocity (related to the empty tube) of the gas s
which percolates through the emulsion. The velocity u is and
b
the rise velocity of a single bubble calculated according to s r =r′⋅cosϕ′−r⋅cosϕ. (19)
Davidson and Harrison (1963) by To get the absolute radial velocity of the bubble phase,
u =0.71 gD . (15) the drift velocity has to be added to the local radial velocity
b b
of the suspension phase, that is,
The superficial gas velocity in the emulsion phase is
u =u +v . (20)
calculated following the approach of Hilligardt and Werther r d,r r
(1986): The bubble diameter D can be determined by a bub-
b
u −u 1 ble growth model such as that by Hilligardt and Werther
e mb = , (16)
u −u 3 (1986) for the case of fluidized beds under ambient condi-
0 mb
tions. In the case of fluidization under supercritical condi-
where u is the minimum bubbling velocity, i.e. the low-
mb tions experimental data were used for the determination of
est velocity at which bubbles occur.
the bubble diameter. According to previous experiments
Closely neighboring bubbles (cf. Fig. 4) will attract each
(Vogt et al., 2005) in supercritical fluidized beds, a constant
other (e.g. Clift & Grace, 1984), giving rise to a radial drift
bubble size results from a balance between bubble splitting
velocity u which increases with decreasing distance. and bubble coalescence after a very short distance above
d,r
The intensity of the drift between bubble A and bubble B is, the gas distributor. Therefore a constant bubble size of
according to Clift and Grace (1984), determined by the D =7.5 mm has been adopted throughout the whole flu-
b
distance a between the centers of the two bubbles idized bed.
s
In the models of Kobayashi et al. (2000) and Bruhns and
normalized with the bubble diameter D .
b Werther (2005) solids are transported only by the flow of
the suspension phase. But measurements of many authors
showed that especially vertical mixing of solids is mainly
due to the transport of solids within the wake of the bub-
bles, that is, solids are taken by the wake from the bottom
region and transported without significant exchange to the
surface of the fluidized bed, where they are released by the
exploding bubbles. Since bubble volume flow is not con-
stant across the bed surface, some radial mixing is also
induced by the solids transport in the wake. This mecha-
nism has been simulated within the model by relating the
sources of bubble gas at the distributor and at the jet with
corresponding sinks for the solids inside the suspension
Fig. 4 Radial interaction between two neighboring bubbles. phase. At the surface of the fluidized bed the sinks for
bubble gas are related to source terms in the suspension
For the determination of the radial drift velocity u
d,r phase balance. The strength of the suspension sinks or
Kobayashi et al. (2000) and also Bruhns and Werther sources is given by the strength of the corresponding gas
(2005) used a number balance for the bubbles in each
sources or sinks and the fraction f of the bubble volume
volume element and accumulated the interaction between w
which is taken by the wake. According to Werther (1976),
all individual pairs of bubbles. This approach is hard to use

Vogt, Hartge, Werther & Brunner: Simulation of Particle Coating in the Supercritical Fluidized Bed 117
the wake fraction is correlated with the shape factor ψ of bubble rise velocity u for the dispersion in axial direction.
b b
the bubble by The correlation they gave, transformed to cylinder coordi-
1−ψ nates, reads
f = b . (21)
w ψ D =0.35εDu ,
b r b b d,r (28)
D =0.35εDu .
The shape factor ψ is defined as the volume of the z b b b
b
Due to the much higher bubble rise velocity compared to
bubble divided by the volume of a sphere with the same
the radial drift velocity this results in a non-isotropic dis-
diameter
persion with the dispersion in vertical direction significantly
V
ψ = b . (22) larger than in radial direction.
b V
sphere
2.2 The coating process
With the wake fraction the strength of the solid sinks and
sources can be calculated as The first step of the coating process is the injection of the
m(cid:5) =(1−ε)ρf V(cid:5) . (23) coating agent, in this work paraffin, which is dissolved in
s e w b CO , the same fluid as used as fluidizing gas, but at higher
2
Neumann boundary conditions for all borders but the
pressure and higher temperature. In the nozzle the pres-
lower border are given by
sure of the fluid is reduced, the fluid is cooled down due to
∂ε ∂ε ∂ε expansion and the solubility is lowered. Therefore the dis-
b b b , (24)
∂z ∂r ∂z solved paraffin precipitates on the bed particles. Following
z=zmax r=0 r=rmax
this precipitation the coating will solidify by cooling. In the
and for the lower boundary of the domain, the bubble
current model these steps are not described in detail, but a
volume fraction ε is set to a given starting value ε
b b,0 simplified empirical approach is used.
ε =ε . (25) Injection of the paraffin
bz=0 b,0
Figure 5 gives a schematic sketch of the injection of the
The bubble volume fraction at the distributor is given by
paraffin. For the description of the jet the spray angle α and
Hilligardt and Werther (1986):
the penetration length L are required. The spray angle α
Ψ(u −u )
ε = 0 mb , (26) has been measured for spraying into air under ambient
b,0 u
b conditions. For the injection of a liquid into a fluidized bed
where Ψ is the fraction of the surplus volume flow Bruhns (2002) found that the spray angle in the fluidized
(u −u )A which can be seen in the form of bubbles bed is the same as that in air. Therefore the measured
0 mb t
angle for a spray in air has been used as the spray angle in
(visible bubble flow).
the supercritical fluidized bed. For the determination of the
Solids mixing
As already stated above, the dominant mechanisms for
solids mixing are the solids movement due to the flow of
the suspension phase and the solids transport in the wake.
Besides these mechanisms which act on a gross scale α
α
there is also a dispersive mechanism due to the random
small scale movement of the particles. The spreading of a
tracer or of tagged solids may therefore described by
∂C 1∂(r⋅v ⋅C) ∂(v C) L
+ r + z =
∂t r ∂r ∂z L inij nj
1 ∂ ⎛ ∂C⎞ ∂ ⎛ ∂C⎞
r ∂r ⎝ ⎜r⋅D r ⋅ ∂r ⎟ ⎠ + ∂z ⎜ ⎝ D z ⋅ ∂z ⎟ ⎠ +m(cid:5) C .
(27)
where C denotes the concentration of the tracer and m(cid:5)
C
is a source or sink term given as mass of tracer per unit
volume and unit time. The mechanism of the wake trans- Fig.5 Sketch of jet injection.
port is included hidden in this source/sink term.
According to Kobayashi et al. (2000) the dispersion is penetration length of a jet into a fluidized bed many corre-
influenced by the bubble volume fraction ε , the bubble lations are available in the literature, e.g. Basov et al.
b
(1969), Merry (1975) and Yang and Keairns (1979). In this
size D and the velocity of the bubble in the direction of
b work the correlation of Yang and Keairns (1979) has been
dispersion relative to the suspension phase, i.e. the drift
chosen, since it is based on the broadest range of ex-
velocity u for the dispersion in radial direction and the perimental conditions and it includes the influence of den-
d,r

118 CHINA PARTICUOLOGY Vol.3, Nos.1-2, 2005
sity and viscosity of the fluid and may thus be extrapolated heat of solidification has to be balanced by the heat trans-
to the present supercritical conditions: ferred from the paraffin to the solids plus the heat trans-
ferred to the fluid
L ⎛ρd ⎞ −0.585 ⎛ρd u ⎞ −0.654 ⎛u 2 ⎞ 0.47 k (T −T )A +k (T −T )A =h m(cid:5) , (33)
=814.2⎜ s p,s ⎟ ⎜ f o inj ⎟ ⎜ 0 ⎟ . (29) par,f f par par par,s s par par sol par,sol
d o ⎝ ρ f d o ⎠ ⎝ η ⎠ ⎝gd o⎠ where T f and T s are the temperatures of the fluid and
For modeling the precipitation of the paraffin on the par- the solids, respectively; T is the temperature of the par-
par
ticles it is assumed that the probability that a paraffin
affin, assumed to be its melting point; h is the heat of
droplet hits a particle decreases linearly with the distance sol
from the jet orifice. With this assumption it holds for the crystallization, which is released during the solidification;
local wetting mass flows m(cid:5) par,inj (r,z): k par,f and k par,s denote the heat transfer coefficients be-
tween paraffin and fluid and between paraffin and particle,
rspray(z−zinj)
∫ 2πrm(cid:5) (r,z)⋅dr =c⋅(z−z ), respectively. The heat transfer coefficient between paraffin
par,inj inj
0 and fluid k is calculated according to the procedure
par,f
∀ z∈⎡ ⎣ z inj … (z inj +L)⎤ ⎦ , given in the VDI-Heat Atlas (1997). For a typical fluidizing
(30) velocity u=0.024 m⋅s-1 and for the heat capacity
where c is a proportionality constant, z inj is the height of the c =4.946 kJ⋅(kg-1⋅K-1) and the heat conductivity
p
nozzle and r (z−z ) is the height dependent radius of
spray inj λ=0.04257 W⋅(m-1⋅K-1) of the supercritical CO , this
the spray cone. With the assumption that the entire mass 2
of injected paraffin per unit time is deposited on the bed procedure gives the high value of k =2800W⋅(m-2⋅K-1).
par,f
particles within the spray cone with the length L, the con-
This high value of k implies that the heat transfer be-
stant c can be determined by par,f
tween the paraffin and the fluid will be the dominating
zinj+L rspray(z−zinj)
∫ ∫ 2πrm(cid:5) (r,z)⋅dr⋅dz=m(cid:5) . (31) process and the heat transfer between the paraffin and the
par,inj par,tot
particle is negligible. By neglecting this latter process,
zinj 0
Assuming furthermore that the local wetting mass flows Eq.(33) is simplified to
m(cid:5) (r,z) is independent of the radial distance from the k (T −T )A =h m(cid:5) . (34)
par,inj par,f f par par sol par,sol
jet center for any given distance from the jet orifice, the This simplification allows the calculation of the mass of
local wetting mass flows m(cid:5) (r,z) can be calculated by solidified paraffin per unit time m(cid:5) without solving a
par,inj par,sol
m(cid:5) (r,z)= unsteady-state heat balance around a single particle. The
par,inj
particle surface A coated with a layer of liquid paraffin
⎪ ⎪ ⎧ ⎨ ⎪ m(cid:5) p L a 2 r,tot ⋅ π(z L − − z ( i z nj ) − 2 z ta inj n ) 2α for r z in < j < ( L z − < ( z z in − j + z in L j )) sinα. d e e le p m e e n n d t s a o n n d t t h h e e m th a p i a c s r k s n o e f s l s iq o u f i d th p e a l r i a q f u fi i n d la m y p e ar r i s n : t he volume
⎪ ⎩ 0 else ⎧V m
Solidification of the deposited paraffin (32) A par = ⎪ ⎪ ⎨ s par = ρ pa p r a s r for not completely covered particles .
⎪
If only the distribution of coating thickness under stable ⎪ A particle for completely covered particles
operating conditions has to be calculated, it suffices just to ⎩
model the deposition of paraffin on the particles as de- (35)
scribed in the previous section. Under stable conditions Finally, the mass of liquid paraffin in a volume element is
solidification only takes time, but will not change the dis- calculated with the help of Eq.(27), where C is now
tribution of paraffin on the particles. If the simulation aims defined as the mass of liquid paraffin per unit volume m
par
also at the prediction of stable and unstable operation
and the source and sink term m(cid:5) is given by the mass
conditions, i.e. conditions under which severe agglomera- C
tion occurs, the solidification process has to be taken into flow of injected paraffin as the source and the mass of
consideration. To form agglomerates wet particles have to solidified paraffin per unit time m(cid:5) as the sink term.
par,sol
come into contact. If the amount of un-solidified paraffin in
a volume element becomes too high, the formation of ag-
3. Results
glomerates will dominate the destruction of agglomerates
by mechanical stress. On the other hand, the solidified 3.1 Validation of the fluid-dynamic model
paraffin will not cause any agglomeration.
Due to the lack of experimental data obtained under high
The mass of paraffin solidified per unit time m(cid:5) in a
par,sol pressure, validation of the fluid-dynamic model has been
volume element can be estimated by a heat balance: the carried out using data measured in fluidized beds under

Vogt, Hartge, Werther & Brunner: Simulation of Particle Coating in the Supercritical Fluidized Bed 119
ambient conditions. A detailed investigation of the local
flow in fluidized beds was carried out by Werther (1976),
who used capacitance probes to measure local flow prop-
erties at various radial positions in fluidized beds with di-
ameters varying from 0.2m to 1.0m. The experimental
conditions of his experiments are given in Table 2 together
with the model parameters used for simulation.
Table 2 Operational conditions used in Werther’s experiments
(1976) and model parameters for simulation
Operational conditions (Werther, 1976)
Solids Quartz sand
Solids density ρ 2650 kg⋅m-3
s
Surface-volume mean diameter d p,s 83 μm
Gas Air
Gas density ρ 1.2 kg⋅m-3
f
Minimum fluidization velocity u 1.8×10-2 m⋅s-1 mf
Superficial fluidizing velocity u 0.09 m⋅s-1
0
Model parameters
Suspension viscosity η (after Grace, 1970) 0.8 Pa⋅s
e
Fraction of visible bubble flow Ψ
0.61
(Hilligardt & Werther, 1986)
Wake fraction f (Werther, 1976) 0.18 w
Figure 6 shows Werther’s measurements (1976) of visi-
ble bubble flow. For comparison, the visible bubble flow
has been calculated from the simulation results by
v(cid:5) =ε(1−f )u . (36)
b b w z
0.14 H=30 cm
H=15 cm
0.12 H=5 cm
0.10
0.08
0.06
0.04
0.02
0.00
-100 -50 0 50 100
)1-s
m(/v
b
also in the simulation by Bruhns and Werther (2005) and
may result from simplifications in the description of the gas
flow through the suspension.
A gross circulation of the suspension, depicted in Fig.7,
is induced by the uneven distribution of the bubble flow as
shown in Fig.6, that is, there is a downward movement of
the suspension in the vicinity of the walls, and a corre-
sponding upward flow in the center region in addition to
horizontal compensation flows at the top and near the
bottom of the bed. This kind of gross circulation is typical
for fluidized beds with small diameters (Kunii & Levenspiel,
1991).
0.5
0.4
0.3
0.2
0.1
0.0
-0.10 -0.05 0.00 0.05 0.10
r/mm
Fig.6 Comparison of measured and simulated radial profiles of the
visible bubble flow v(cid:5) . (bed diameter 0.2 m, bed height 0.5 m,
b
measurement data of Werther (1976)).
Basically there is satisfactory agreement between the
simulated and the measured profiles. The tendency for the
bubbles to move towards the center with increasing height
is well described, and even the positions of the maxima are
predicted with good accuracy. Only the absolute values for
the visible bubble flow are higher than experimental in the
lower region and lower than experimental in the upper part
of the fluidized bed. This divergence has been observed
m/h
thgieh
distance from centerline r/m
Fig.7 Calculated suspension flow in a fluidized bed 0.2 m in diameter
and 0.5 m in height.
3.2 Fluid dynamics in the high pressure fluidized
bed
In a second step the fluid-dynamic model has been ap-
plied to the fluidized bed operated under supercritical con-
ditions with the injection of a paraffin-laden CO -jet. The
2
dimensions, operating parameters, and gas and solids
properties have been taken from Vogt et al. (2005), as
listed in detail in Table 3. The geometry of the fluidized bed
(cf. Fig.1) has been simplified for the simulation by as-
suming that the gas distributor is in the same plane as the
injection nozzle (Fig.8).
Fig.8 Simplified geometry of the high pressure fluidized bed for
simulation.

120 CHINA PARTICUOLOGY Vol.3, Nos.1-2, 2005
Table 3 Operational parameters, gas and solids properties and mod- (Fig.9) as it results from the momentum of the jet. The
eling parameters for the simulation of the fluidized bed under suspension is accelerated upward by the jet issuing from
supercritical conditions
the nozzle, where the suspension attains its highest veloc-
Fluidized bed geometry ity. For continuity reasons fresh suspension has to flow
Diameter 39.4 mm along the bottom from the walls towards the center. With
Bed height 140 mm
increasing height the momentum disperses and the sus-
Operating conditions
pension decelerates, thus making the suspension flow
Pressure p 8 MPa
Temperature T 313 K radially away from the center. From the velocity plot it can
Fluidizing gas CO2 be seen that the velocities within this local swirl at the jet
Fluid density ρ 277 kg⋅m-3 are much higher than those within the gross circulation,
f
causing intense mixing in the bottom region.
Fluid viscosity η 2.23×10-5 Pa⋅s
f In order to estimate the influence of the suspension
Bed material Glass beads
viscosity on the gross flow pattern, another simulation run
Surface-volume mean diameter d p,s 169 μm was performed with the same parameters as before (cf.
Solids density 2485 kg⋅m-3 Table 3), except for the suspension viscosity η which has
e
Minimum fluidization velocity u at
mf 0.016 m⋅s-1 been changed from η e =1.3Pa⋅s to η e =0.7Pa⋅s. This latter
operating conditions value is the lower limit of the range of suspension viscosi-
Minimum bubbling velocity u mb at 0.023 m⋅s-1 ties experimentally determined by Grace (1970). The re-
operating conditions sults for the suspension flow calculated with this lower
Fluidizing velocity u 0.027 m⋅s-1 suspension viscosity are shown in Fig.12. The flow pattern
0
Mass flow of injection gas m(cid:5) inj 0.46 g⋅s-1 is very similar to that with the higher suspension viscosity;
except for the slight difference that the jet region is ex-
Model parameters
tended upward. Due to the lower viscosity the high vertical
Suspension viscosity η 1.3 Pa⋅s
e suspension velocity just above the jet needs greater dis-
Fraction of visible bubble flow Ψ 0.61 tance to be damped out, and thus the high velocity region
Wake fraction f 0.18 is slightly elongated in the vertical direction.
w
0.040
Compared to the simulation for ambient conditions a
0.035 slightly increased suspension viscosity was used; h = 0.05 m
η =1.3 Pa⋅s, due to the higher viscosity of the super- 0.030 h = 0.13 m
e 0.025
critical CO as compared to that of air under ambient con-
2 0.020
ditions. To study the sensitivity of the simulation against
0.015
this parameter an additional simulation run has been car-
0.010
ried out with a lower viscosity.
0.005
The results of the simulation are shown in Fig.9 to Fig.11.
0.000
Fig.9 shows the visible bubble flow in the high pressure 0.000 0.005 0.010 0.015 0.020
fluidized bed which is highly dominated by the influence of
the jet. The influence of bubble drift as seen for the at-
mospheric fluidized bed is negligible as compared to the jet.
Only about 5% of the total CO mass flow are contributed
2
by the jet; this highly concentrated flow in a small area is
mostly transported as bubbles through the fluidized bed,
causing a high local bubble flow in the center. Fig.10
shows the corresponding plot of the bubble volume fraction,
high in the center and decreasing towards the walls.
Intense circulation of suspension is expected from the
pronounced profiles of bubble flow and bubble fraction, as
can be seen in Fig.11 for the suspension. In the plot on the
left hand side the direction of flow is plotted, in the plot on
the right hand side the velocity, shown in logarithmic scale.
The velocities near the jet are about two orders of magni-
tude higher than those in the upper part. As expected,
circulation with up flowing suspension in the center and
down flowing suspension near the wall exists. But besides
this gross circulation, a second swirl in the bottom part can
be seen, which results from the jet at the centerline. This
lower swirl can not be explained by bubble flow alone
1-s m/v
wolf
elbub
elbisiv
b
r/m
Fig.9 Calculated profiles of visible bubble flow in the high pressure
fluidized bed with a jet (data cf. Table 3).
0.12
0.10
0.08
0.06
0.04
0.02
0.00
-0.010.000.01
r/m
m/h
thgieh
.
bubble
volume
fraction
ε
b
0
0.0125
0.0250
0.1000
0.1500
0.2000
Fig.10 Calculated two-dimensional profile of bubble volume fraction
in the high pressure fluidized bed with a jet (data cf. Table 3).

Vogt, Hartge, Werther & Brunner: Simulation of Particle Coating in the Supercritical Fluidized Bed 121
0.12
0.10
0.08
0.06
0.04
0.02
0.00
-0.010.00 0.01
r/m
m/h
thgieh
0.14
0.12
0.10 1E-5
6.9E-5
0.08 4.8E-4
0.0033
0.023 0.06
0.16
1.1
0.04
0.02
0.00
-0.010.000.01
m/h
thgieh
r/m
Fig.11 Simulated flow of the suspension in the high pressure fluidized
bed. Left: direction of flow; right: velocity v = ( v 2+v 2) of
r z
the suspension phase.
0.12
0.10
0.08
0.06
0.04
0.02
0.00
-0.01 0.00 0.01
r, m
m
,h
thgieh
0.14
0.12 1E-5
6.922E-5
0.10 4.791E-4
0.003317
0.08 0.02296
0.1589
0.06 1.100
v, m/s
0.04
0.02
0.00
-0.01 0.00 0.01
m
,h
thgieh
X =m m . (37)
par solids
Table 4 Comparison of calculated and measured paraffin loading of
particles at 8 MPa and 313 K (experimental values in pa-
rentheses)
Paraffin loading of particles
mass X / %
u 0/(cm⋅s-1) m(cid:5) inj /(g⋅s-1) m(cid:5) par,inj /g Upper region Lower region
2.7 0.46 11.9 4.5 (10.6) 2.6 (2.7)
2.4 0.70 7.7 2.6 (3.8) 1.9 (1.9)
2.5 0.93 8.0 2.8 (2.6) 2.0 (2.2)
2.4 1.49 8.2 3.5 (3.3) 2.9 (2.9)
During the experiments samples of the bed were with-
drawn after shutdown of the fluidized bed and after pres-
sure release. Several samples of about 2 g each were
taken from the top of the bed, The paraffin loading of these
samples were used to get an average value of the loading
in the upper part of the fluidized bed. To get the paraffin
loading in the lower section of the bed, the bed was emp-
tied down to the lower two to three centimeters of the set-
tled bed. Then one sample of about 2 g was taken from the
center just above the nozzle.
To get comparable values from the simulation, the cal-
culated loadings of the uppermost 3 cm of the fluidized bed
have been averaged and used as the value of the paraffin
loading of the upper section. For the lower region of the
bed the average loading in a cylindrical region with 1 cm
diameter and at a height of about 2 cm starting 1 cm above
the jet was used.
The values of the measured and the calculated paraffin
loadings are plotted in Fig. 13. The plot shows a good
agreement between calculated and measured values for
the loading in the upper region. Also in the lower region the
agreement is reasonable, only at low injection flows there
is some discrepancy which might be related to agglomera-
tion of particles observed during the experiments with low
injection flows. Such agglomeration increases the ten-
dency of segregation, particularly at the low fluidizing ve-
r, m locities of about 2.5 cm⋅s-1, which is quite close to the
minimum bubbling velocity u =2.3 cm⋅s-1. At this low ve-
Fig.12 Simulated flow of the suspension in the high pressure fluid- mb
ized bed, calculated with a lower suspension viscosity locity solids mixing by the fluidizing gas is quite weak and
ηe=0.7Pa⋅s, left: direction of flow; right: velocity calls for the assistance of the jet.
v = ( v 2+v 2) of the suspension phase.
r z
0.10
experiment simulation
3.3 Paraffin distribution in the fluidized bed 0.08 lower region upper region
Knowing the fluid dynamics and especially the solids
0.06
movement and mixing it is possible to simulate the coating
process and the distribution of the paraffin in the fluidized
0.04
bed. This simulation has been carried out for the conditions
which have been experimentally investigated in previous 0.02
works (Vogt et al., 2004b; Vogt et al., 2004a), as shown in
0.4 0.6 0.8 1.0 1.2 1.4 1.6
Table 4 together with a comparison of measured and cal-
culated values of the paraffin loading of the particles. The
loading X is defined as the mass of paraffin in a sample
related to the mass of solids in that sample,
X gnidaol
niffarap
v / (m⋅s-1)
v / (m⋅s-1)
r /m r /m
Fig.13 Calculated and measured paraffin loading X versus injection
mass flow m(cid:5) .
inj
m/h
thgieh
m/h
thgieh
Injection mass flowm(cid:5) /(g⋅s-1)
inj

122 CHINA PARTICUOLOGY Vol.3, Nos.1-2, 2005
Figure 14 portrays the development of paraffin distribu- about the mass of liquid paraffin within the fluidized bed,
tion in the fluidized bed with time for the run with a low simulations have been carried out which include the injec-
injection mass flow of m(cid:5) =0.46 g⋅s-1. Basically the same tion and the solidification of the liquid paraffin. Results of
inj such simulation run with u =2.4cm⋅s-1 and a quite high
pattern is to be observed in all the three plots consisting of 0
a zone with high paraffin loadings at the center and above injection mass flow of m(cid:5) =1.49 g⋅s-1 are depicted in
inj
the jet, and dwindling paraffin loadings toward the wall. Fig. 15. Due to fast solidification, liquid paraffin can be
Obviously vertical mixing is much more effective than observed only in the immediate vicinity of the jet, even
horizontal mixing. While the pattern of the distribution does though the mass flow of the injected paraffin is quite. Al-
not change much with time, the absolute values do vary. In though, according to Bruhns and Werther (2005) it would
order to better resolve the gradients in all the three plots, be expected that the spray angle in the fluidized bed is
their scales have been adjusted individually. The absolute nearly the same as outside in free air, the spreading of the
values of the minimum and maximum concentrations in- liquid paraffin in the high pressure fluidized bed is wider,
crease nearly linearly with time. possibly because of the swirl flow of the suspension near
From the simulations it follows that it is difficult to the bottom.
achieve uniform distribution of the paraffin coating with low
fluidizing velocities, even in a small apparatus as was used
for the present experiments. If such low velocities are 0.12
necessary, at least a high injection mass flow should be
used in order to enhance solids mixing.
0.10
All the calculations presented up to now deal only with
solid paraffin, while the solidification process is not taken 0.08
into account. Such calculations allow the prediction of the
homogeneity of the coating process, but they give no in-
0.06
formation as to the stability of the process. From experi-
ments it is known that under certain conditions, such as
0.04
low fluidizing velocity, high paraffin concentration in the
injection gas and low mass flow of the jet, the system tends
0.02
to form large agglomerates, which may cause defluidiza-
tion of the bed. Such formation of agglomerates will occur if
0.00
too much liquid paraffin is present in a volume element. In 0.01
such a case the probability of collision of two ‘wet’ particles r/m
each with a layer of liquid paraffin will increase. Such a
collision of two ‘wet’ particles may lead to the formation of a
liquid bridge between the particles, which will solidify to
become a stable bonding. To acquire more information
m/h
thgieh
0.12 0.12 1.0
1.2
1.3
0.10 0.10
1.5
1.7
0.08 0.08
1.9
2.0
0.06 0.06 2.2
X/%
0.04 0.04
0.02 0.02
0.00 0.00
-0.01 0.00 0.01 -0.01 0.00 0.01
r/m r/m
2.5E-7
2.9E-5
5.7E-5
8.6E-5
1.1E-4
1.4E-4
1.7E-4
2E-4
spray angle = 20o
Fig. 15 Paraffin loading on the solids, 30 seconds after injection
(u =2.40 cm⋅s-1, m(cid:5) =1.49 g⋅s-1). The spray angle fol-
0 inj
lows the measurement outside the fluidized bed (Schreiber
et al., 2002b).
m/h
thgieh
0.50 0.12 2.0
0.59 2.4
0.67 2.7
0.10
0.76 3.1
0.84 3.5
0.08
0.93 3.9
1.0 4.2
1.1 0.06 4.6
X/% X/%
0.04
0.02
0.00
-0.01 0.00 0.01
r/m
after 11 min after 22 min after 45 min
Fig. 14 Development of paraffin distribution in the fluidized bed with time (u =2.72 cm⋅s-1, m(cid:5) =0.46 g⋅s-1).
0 inj
2.5E−7
2.9E−5
5.7E−5
8.6E−5
1.1E−4
1.4E−4
1.7E−4
2E−4

Vogt, Hartge, Werther & Brunner: Simulation of Particle Coating in the Supercritical Fluidized Bed 123
More investigations are needed to validate these latter p absolute pressure, Pa
results and to formulate a stability condition, which will r radial distance from the center line, m
allow the prediction of the range of stable operating condi- Re Reynolds number
tions. s thickness of layer, m
s separation distance between two bubbles in radial
r
direction, m
4. Conclusions
t time, s
T temperature, K
For the prediction of product quality and for deeper un-
derstanding of the coating process in a fluidized bed oper-
u
0
superficial velocity of fluidizing gas, m⋅s-1
ated under supercritical conditions, a model has been de- u inj jet outlet velocity, m⋅s-1
u, u velocity of the bubble phase in radial and axial di-
r z
veloped, which combines CFD-methods with semi empiri- rection, m⋅s-1
cal models. This hybrid-model uses the full set of conser-
v, v velocity of the suspension phase in radial and axial
r z
vation equations for the description of the suspension flow, direction, m⋅s-1
while for the description of the bubbles well proven V volume, m3
semi-empirical models are utilized. This approach allows z vertical distance from the distributor plate, m
the simulation of the fluid dynamics within a high pressure Greek letters
fluidized bed with quite low computing requirements. Fur- α jet angle, °
thermore the distribution of the paraffin and the uniformity ε porosity of the fluidized bed
of the paraffin loading on the particles can be described ε bubble volume fraction at the distributor plate
b,0
with good accuracy. In combination with a model of the
ε bubble volume fraction
solidification of the paraffin, the instantaneous loading of b
the fluidized bed with liquid paraffin can also be predicted. ε e porosity of the suspension phase
These latter simulations can be used as the basis for the Φ sphericity of the particles
s
prediction of stable operating regimes.
η dynamic viscosity of the fluid, Pa⋅s
f
The calculations show that the central jet dominates the
η dynamic viscosity of the suspension phase, Pa⋅s
flow structure in the fluidized bed and that it significantly e
enhances solids mixing. Therefore the homogeneity of the λ coefficient of friction
paraffin distribution depends strongly on a sufficiently high ρ density of the bubble phase, kg⋅m-3
b
jet mass flow and thus a high jet momentum. First simula- ρ density of the suspension phase, kg⋅m-3
e
tions of the spreading and solidification of the liquid paraffin
ρ density of the fluid, kg⋅m-3
show that only in the close vicinity of the jet, can liquid f
paraffin be found. Provided the jet mass flow is sufficiently ρ paraffin density of paraffin, kg⋅m-3
high, the formation of stable agglomerates in this region ρ solids density, kg⋅m-3
s
will be suppressed by the high shear forces, which result
τ viscous stress, Pa
from the jet.
Indices
b bubble, bubble phase
Acknowledgement e suspension (emulsion) phase
max maximum value
This work was funded by the German Research Foundation
mb conditions of onset of bubbling, minimum bubbling
(Deutsche Forschungs Gemeinschaft, DFG) under grant No. WE
point
935 / 7-1. The authors gratefully acknowledge this support.
mf minimum fluidization conditions
p particle
Nomenclature r radial direction
z axial (vertical) direction
A area, m2
C tracer concentration, kg⋅m-3
References
d diameter of jet outlet opening, m
0
D bubble diameter, m
b Basov, V. A., Markhevka, V. I., Melik-Akhnazarov, T. K. & Orochko,
D, D dispersion coefficients in radial and vertical direc-
r z D. I. (1969). Investigation of the structure of a nonuniform fluid-
tion, m⋅s-1
ized bed. Int. Chem. Eng., 9, 263-266.
d mean surface diameter of solids, m
p,s Bruhns, S., (2002). On the Mechanism of Liquid Injection into
f fraction of the bubble volume taken by the wake
w Fluidized Bed Reactors. PhD thesis, Hamburg University of
g gravity, m⋅s-2 Technology, Hamburg.
h height above gas distributor, m Bruhns, S. & Werther, J. (2005). 3-D modeling of liquid injection
H height of fluidized bed, m into fluidized beds: flow structure, solids mixing, heat and mass
k w heat transfer coefficient, W⋅(K-1⋅m-2) transfer. Chem. Eng. Sci., in press.
L penetration depth of the jet, m Clift, R. & Grace, J. R. (1984). Continuous bubbling and slugging.
m mass, kg In Harrison, D. (Ed.), Fluidization. London: Academic Press.
m(cid:5) mass flow, kg⋅s-1 Davidson, J. F. & Harrison, D. (1963). Fluidized Particles. Cam-

124 CHINA PARTICUOLOGY Vol.3, Nos.1-2, 2005
bridge: Cambridge University Press. Tsutsumi, A., Nakamoto, S., Mineo, T. & Yoshida, K. (1995). A
Ding, J., Lyczkowski, R. W., Burge, S. W. & Gidaspow, D. (1992). novel fluidized-bed coating of fine particles by rapid expansion
Three-dimensional models of hydrodynamics and erosion in of supercritical fluid solutions. Powder Technol., 85, 275-278.
fluidized bed combostors. AIChE Symp. Ser., 88(289), 85-98. VDI-Heat Atlas (1997). Duesseldorf: VDI Verlag.
Gidaspow, D. (1994). Multiphase Flow and Fluidization. Boston: Vogt, C., Hartge, E.-U., Werther, J., Schreiber, R. & Brunner, G.
Academic Press. (2004a). Simulation der Beschichtung von Partikeln in einer mit
Grace, J. R. (1970). The viscosity of fluidized beds. Can. J. Chem. überkritischem Fluid betriebenen Wirbelschicht. In Teipel, U.
Eng., 48, 30-33. (Ed.), Produktgestaltung in der Partikeltechnologie (pp.245-
Hilligardt, K. & Werther, J. (1986). Gas flow in and around bubbles 258). Stuttgart: Fraunhofer IRB Verlag.
in gas fluidized beds ⎯ local measurements and modelling Vogt, C., Schreiber, R., Werther, J. & Brunner, G. (2004b). Influ-
considerations. World Congess III of Chem. Eng. (p.429-432), ence of hydrodynamics on fluidized bed coating at supercritical
Tokyo, Japan. fluid conditions. In Arena, U., Chirone, R., Micchio, M. &
Kleinbach, E. & Riede, T. (1995). Coating of solids. Chem. Eng. Salatino, P. (Eds.), Fluidization XI (pp.51-58). Brooklyn: ECI.
Process., 34, 329-337. Vogt, C., Schreiber, R., Brunner, G. & Werther, J. (2005). Fluid
Kobayashi, N., Yamazaki, R. & Mori, S. (2000). A study on the dynamics of the supercritical fluidized bed. Powder Technol.,
behavior of bubbles and solids in bubbling fluidized beds. accepted.
Powder Technol., 113, 327-344. Werther, J. (1976). Convective solids transport in large diameter
Kunii, D. & Levenspiel, O. (1991). Fluidization Engineering. Bos- gas fluidized beds. Powder Technol., 15, 155-167.
ton: Butterworth-Heinemann. Werther, J. & Wein, J. (1994). Expansion behavior of gas fluidized
Li, J. & Kuipers, J. A. M. (2003). Gas-particle interactions in dense beds in the turbulent regime. AIChE Symp. Ser., 90(301),
gas-fluidized beds. Chem. Eng. Sci., 58, 711-718. 31-44.
Merry, J. M. D. (1975). Penetration of vertical jets into fluidized Yang, W.-C. & Keairns, D. L. (1979). Estimating the jet penetration
beds. AIChE J., 21, 507-510. depth of multiple vertical grid jets. Ind. Eng. Chem. Fundam., 18,
Schreiber, R., Reincke, B., Vogt, C., Brunner, G. & Werther, J. 317-320.
(2002a). Fluidized bed coating at supercritical fluid conditions. J. Ye, M., van der Hoef, M. A. & Kuipers, J. A. M. (2004). A numeri-
Supercrit. Fluids, 24 (2), 137-151. cal study of fluidization behavior of Geldart A particles using a
Schreiber, R., Reincke, B., Vogt, C., Werther, J. & Brunner, G. discrete particle model. Powder Technol., 139, 129-139.
(2002b). High pressure fluidized bed coating utilizing super-
critical carbon dioxide. Proc. World Congress Particle Tech- Manuscript received March 7, 2005 and accepted March 24, 2005.
nology 4, Sydney, Australia.
