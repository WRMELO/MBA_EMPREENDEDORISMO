# Evaluation_of_performance_of_industrial

**Fonte**: Evaluation_of_performance_of_industrial.pdf  
**Data de conversão**: 2025-07-30 15:10:37  
**Origem**: base_relevantes

---

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/263941750
Evaluation of Performance of Industrial-Scale
Dual Fluidized Bed Gasifiers Using the Chalmers
2–4-MWth Gasifier
ARTICLE in
ENERGY & FUELS · SEPTEMBER 2013
Impact Factor: 2.79 · DOI: 10.1021/ef400981j
CITATIONS READS
18 38
4 AUTHORS
, INCLUDING:
Anton Larsson Martin Seemann
Chalmers University of Technology Chalmers University of Technology
8 29 26 230
PUBLICATIONS CITATIONS PUBLICATIONS CITATIONS
SEE PROFILE SEE PROFILE
Henrik Thunman
Chalmers University of Technology
65 924
PUBLICATIONS CITATIONS
SEE PROFILE
Available from: Anton Larsson
Retrieved on: 05 February 2016

Article
pubs.acs.org/EF
Evaluation of Performance of Industrial-Scale Dual Fluidized Bed
Gasi fi ers Using the Chalmers 2−4-MW Gasi fi er
th
Anton Larsson,*,† Martin Seemann,† Daniel Neves,‡ and Henrik Thunman†
†Department of Energy and Environment, Chalmers University of Technology, SE-412 96 Göteborg, Sweden
‡DepartmentofEnvironmentandPlanning,CentreofEnvironmentalandMarineStudies,UniversityofAveiro,CampusUniversitaŕio
de Santiago, PT 3810-193 Aveiro, Portugal
*
S Supporting Information
ABSTRACT: A general approach to evaluating the performance of industrial-scale dual fluidized bed (DFB) gasifiers was
developed in this work. The approach is intended to simplify comprehensive evaluation of DFB gasifiers and to highlight
important parameters, some of which are often missed or omitted in the literature. By applying this procedure, experimental
resultscanbegeneralized,whichisverifiedinthisworkusingtheChalmers2−4-MW DFBgasifier.InaDFBgasifier,someof
th
the fuel is converted to the desired calorific gas, while the remaining portion is combusted to meet the heat demands of the
process.Asshownhere,thetotalheatdemandslimittheamountofchemicalenergythatcanberestoredfromthefuelintothe
producedgas,wherebythemainheatdemandsarefromthedryingandheatingofthefuel,inadditiontoheatingthecombustion
air and steam. By establishing a heat balance across the system, the chemical efficiency can be estimated. With lower heat
demands, higher chemical efficiency is achievable, whereas with higher heat demands, more of the fuel must be burned and a
lowerchemicalefficiencyisachieved.Itisexperimentallycomplicatedtoquantifytheleveloffuelconversionandheatdemands
ofaDFBgasificationsystem.Inthiswork,anexperimentalprocedureispresentedandimplementedusingtheChalmersgasifier
toquantifythefuelconversionandheatdemands.Furthermore,itwasinvestigatedhowavariationintheamountofsteamused
forfluidizationofthegasifieraffectsfuelconversionandotherimportantparameters.Toestablishareferencecase,silicasandwas
usedasbedmaterialandwoodpelletswasusedasfueltominimizetheeffectsofashandthebedmaterial.Byincreasingthelevel
offluidizationsteam,theaverageresidencetimeofthegaswasdecreasedandthegastemperature,gasvelocity,andsteam-to-fuel
ratio were increased, which resulted in increased conversion (up to 36%) of organic compounds (OC). However, limited char
conversion was achieved (0%−4%), and the chemical efficiency remained unaffected by the amount of steam added to the
process. The chemical efficiency of the Chalmers gasifier was determined to be 74% when using wood pellets as fuel. This is
comparabletoresultsfromthermo-economicmodelingofsecond-generationbiofuelsproductionprocesses,which,basedonthe
heat demand, report the chemical efficiency of the DFB gasifier as being in the range of 74%−77% to maximize the overall
efficiency.Thisshowsthattherequiredchemicalefficiencyisachieved,evenwithlowcharconversion,whenusingafuelwitha
high content of volatiles, such as wood pellets.
■
INTRODUCTION feedstocks vary significantly in their characteristics (i.e.,
Gasification is a process that is based on the thermochemical volatiles, ash, and moisture contents, as well as density and
conversion of a solid fuel into a calorific gas, hereinafter particle size, all of which can affect fuel conversion), a flexible
referredtoas“rawgas”.Therawgasfromgasifierscanbeused system that can still deliver stable gas quality is required.
Biomass conversion includes three general steps: drying,
forheatandpowerproduction,as,forexample,iscommercially
achieved by the Güssing unit,1 or it can be synthesized into devolatilization, and char conversion. The dry part of the fuel
consistsofvolatilesandchar.Thevolatilepartofthedryfuelis
various liquid and gaseous fuels, such as substitute natural gas
defined as the fraction of the fuel that can be converted to gas
(SNG). A demonstration unit for SNG is being constructed in
Göteborg, Sweden in the GoBiGas project,2 using a dual with heat as the only driving force. The remaining part of the
fluidizedbed(DFB)gasificationsystem,andthelong-termgoal dry fuel consists of ash and char. The char, which mainly
is to produce ∼800 GWh of SNG from biomassannually. The consists of carbon, can be converted in the presence of a
reactant (e.g., H O, CO , or O ) and a sufficiently high
demonstrationunitisplannedtobefullyoperationalattheend 2 2 2
of 2013 with an SNG production level of ∼160 GWh/yr. temperature. The char can be gasified by providing H 2 O or
The configurations applied to gasification processes are CO 2 as the reactant, which yields a calorific gas through
diverse,andtheoptimalsetupdiffersbasedonthefuelusedand endothermic reactions. However, to achieve a thermally stable
the desired end-products. To understand the differences process,partofthefuelshouldbecombustedtomeettheheat
between the various setups, it is important to understand the demands ofthe process. Thisis achieved either by introducing
nature of the thermochemical conversion of the fuel. By using
biomass as feedstock for a gasifier, the raw gas can be Received: May24, 2013
consideredtobeCO -neutral;3forthispurpose,biomassisthe Revised: August 30, 2013
2
mainfuelsourceconsideredinthepresentwork.Sincebiomass
©XXXXAmericanChemicalSociety A dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels ■ Article
O to the gasifier for combustion of part of the gas yielding THEORY
2
direct heating or by burning part of the fuel in a separate To enable comparison of different gasifiers, there is a need to
reactor for indirect heating.4 Thus, in the direct gasification define the general parameters that describe the reactor layout.
concept, the flue gases are mixed with the raw gas and, For a DFB gasifier, this is not a straightforward procedure,
consequently, the heating value of the gas is reduced. By
because there are two interconnected reactors, each of which
locating the combustion to a dedicated chamber, as is the case affects the other. However, by defining three control volumes,
of indirectly heated gasifiers, the flue gas is separated from the the description of the process can be simplified, as further
raw gas. This creates additional options for controlling the air-
illustrated by the dotted lines in Figure 1. In this case, the
to-fuel ratio (ARF) for the heat-generating reactor without volume of the gasifier, CV , is defined to include the main
affecting the quality of the raw gas. In this manner, stable gas gasificationreactorandthep G a 1 rtsoftheparticlesealswherefrom
quality and high heating value of the gas are ensured by an
the gas ends up in the raw gas. CV is the volume in the raw
indirectly heated gasifier. The present work focuses on DFB gas pipe from the gasifier the sa G m 2 pling point. CV is the
gasifiers, in which the heat from the combustion chamber is C
volume of the combustion reactor, including part of the loop
transported with fluidized bed material to heat the gasifier sealsfromwherethegasentersthecombustor.Thegasification
indirectly. ̇
reactor is described by the power-to-volume ratio: (Q/V)
G1
Figure 1 shows the general concept behind the DFB [MW/m3], in combination with a shape factor, β . The shape
gasification system. The main idea is to use the bed material factor describes the difference in volumeof the re V actor relative
to a cube with the same internal area and characteristic length
l 3 = V . From the characteristic length, a shape factor for
car cube
the bed span (β = l /l ) and the cross-sectional area of
l,bed bed car
the bed(β =A /l 2) isformulated. Furthermore, part of
A,bed bed car
the gasifier is occupied by solids that are described by the
volume fraction, ε =V /V where the subscript “s” stands
G1 s,G1 G1,
forsolids.Thedescriptionofthelayoutshouldalsoinvolvethe
type of fuel feed and the positioning of the solids inflow and
outflow, since these factors can influence how well the fuel is
converted. For instance, Kern et al.7 showed how the
positioning of the fuel feed affects the performance of a 90
kW DFB gasifier in terms of higher chemical efficiency, more
tar, and a gas composition that is further from the equilibrium
when feeding on top of the bed, as compared with in-bed
feeding. However, it remains to be determined whether this
Figure 1. Schematic of a dual fluidization bed (DFB) gasification effect holds true for larger-scale gasifiers.
system.
When investigating the functionality of a gasifier in terms of
performance,itisimportanttodescribethemeansbywhichthe
fuel is converted and how different process parameters affect
for transporting heat from the combustor to the gasifier, the conversion. A simplified scheme for the conversion of a
thereby supplying the heat needed for the endothermic solid dry fuel particle subjected to steam gasification is
gasification reactions and heating of the fuel. To prevent gas illustrated in Figure 2. The fuel is primarily converted through
leakage between the reactors, the solids passes through a loop
seal that is fluidized with steam. The fuel is fed to the gasifier,
whereitispartlyconvertedtogasbydevolatilizationandsteam
gasification.Theunconvertedfractionofthefuelistransported
with the solids through a second loop seal to the combustor,
where it is combusted in the presence of air. This process
assures the production of a raw gas that contains very little
nitrogen.Theonlynitrogensourceinthese systemsisaminor
purgegasflow,whichiscommonlyusedinfuelfeedingsystems
for suppressing the back-mixing of raw gas from the gasifier to
Figure2.Simplifieddescriptionofsolidfuelconversion.Yistheyield
the fuel storage.
from the devolatilization, and X is the degree of conversion of the
Relevant large-scale DFB biomass gasifier plants have devolatilization products; the subscript “cg” stands for cold gas, and
recently been reviewed by Kaushal and Tyagi5 and Göransson the subscript “rg”stands for raw gas.
et al.6 However, a detailed comparison of the performances of
thesegasifiersisdifficult,asenergyandmass balancestogether
withimportantprocessparametersarenotusuallyreported.As devolatilization, where the mass yields of char (Y ), organic
ch
such, it becomes problematic to formulate general correlations compounds (Y ), cold gas (or permanent gas), and steam
OC
or identify important fundamentals. To address this problem- depend on the fuel properties and process parameters. During
atic, the aim of this work was to establish a general procedure the devolatilization, the temperature and the heating rate are
for evaluating the performance, and important process thedominantparameters.8Here,theOCisdefinedasthesum
parameters, of large-scale DFB gasifiers. A generalized oftheorganiccompoundsintherawgas,withtheexceptionof
description of the effect of the level of fluidizing steam is the hydrocarbons measured in the cold gas (i.e., CH , C H ,
4 2 x
presented based on experimental results from the Chalmers and C H ). In the secondary conversion step, the converted
3 x
gasifier,whichwasquantifiedthroughtheproposed procedure. mass fractions of char and OC are described by X and X ,
ch OC
B dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
respectively. Based on the devolatilization and secondary SNG production, revealing a heat demand of 23% of the fuel
conversion, a simplified description of the fuel conversion is input when using a gasifier temperature of 850 °C, preheating
given by eqs 1−3: of steam to 300 °C, a SFR of 0.5, 50% fuel moisture, and air-
dryingto20%moisture.Tocketal.11madeasimilarevaluation
Y i =f(fuel properties,T b ̅ ed ,h eff ,bed material,layout) for Fischer−Tropsch (FT) crude, methanol (MeOH) and
i=ch,cg,steam,&OC (1) dimethyl ether (DME), revealing heat demands of 23%, 26%,
and 26% of the fuel input, respectively, using a gasifier
X
temperatureof850°C,preheatingofsteamto400°C,aSFRof
ch
0.5, 50% fuel moisture, and air-drying to 25% moisture. These
=f(fuel properties,T
b
̅
ed
,τ f̅,SFR,μ
p
,μ
O
,bed material,u
heatdemandsneedtobecoveredbythefuelinputandcangive
an estimate of the raw gas efficiency. For example, the raw gas
−u ,layout) (2)
mf efficiencies of the gasifier for the suggested biofuel production
are77% forSNGandFT-crudeproduction and74%for DME
X
OC
and MeOH production. It should be stressed that it is the raw
=f(fuel properties,T f ̅ ree ,τ r̅g ,SFR,μ p ,μ O ,bed material,u gasefficiencyofthegasifierthatisconsideredhere,ratherthan
theoverallplantefficiency.Furthermore,itisclearthattheheat
−u ,layout) (3)
mf demands and, thereby, the raw gas efficiency can change with
where T̅ is the average temperature, h is the effective heat- the level of integration10,11 or in the case of combination with
eff
transfer coefficient to a fuel particle, τ̅is the average residence heat and power production.12
time, SFR is the steam-to-fuel ratio, u − u represents the Figure 3 shows that, when wood pellets are used for SNG
mf
superficial velocity minus the minimum fluidization velocity, and FT production, a small fraction of the char is available for
andμisthemassperkgofdry-ash-free(daf)fuel(kg/kg ).
daffuel
Thesubscript“bed”indicatesthebedsectionofthegasifier,the
subscript “free” represents the freeboard, the subscript “p”
stands for purge gas, the subscript “O” denotes oxygen, the
subscript“ch”denoteschar,thesubscript“cg”denotescoldgas,
and the subscript “rg” is for the raw gas.
The performance of a gasifier can be described by the
chemical efficiency (η), which is defined as the chemically
stored energy ofthe gasin relation to the energy stored in the
fuel. The chemical energy in the raw gas and cold gas are
described as the raw gas efficiency and cold gas efficiency,
respectively. Assuming that the fuel is completely devolatilized
inthegasifier,therawgasefficiencyofaDFBgasifierisdirectly
coupled to the char yield (Y ) and the degree of conversion
ch
(X ).Figure3(presentedlaterinthiswork)illustratestheraw
ch
gas efficiency as a function of char conversion from
devolatilization to the maximum theoretical char conversion
(solid lines) and estimated raw gas efficiencies possible for the
different end-products (dash-dotted lines).
The maximum theoretical raw gas efficiency of a DFB
gasificationsystemis,bydefinition,equaltounity,assumingno
heat losses and thermally neutral conversion of the volatile
fraction. For the theoretical case, for the sake of simplicity, the
Figure3.TheoreticalrawgasefficiencyofaDFBgasifierasafunction
char is considered toconsist ofpure carbon, which means that ofcharconversionforfuelswithcharcontentstypicalforbiomass(Y ch
the maximum theoretical char conversion in the gasifier =0.16),peat(Y ch =0.28),andbituminouscoal(Y ch =0.78),and,the
rawgasefficienciesofagasifierintegratedforproductionofsubstitute
(X ) is given by
ch,max natural gas (SNG),10 Fischer-Tropsch (FT) crude,11 dimethyl ether
(1 − X )Δh = X Δh (DME),11 and methanol (MeOH).11
ch,max comb ch,max gasif (4)
whereΔh istheenthalpyofreactionforthecombustionof
comb
pure carbon with oxygen (−393.5 kJ/mol)9 and Δh is the
gasif
enthalpyofreactionforthegasificationreactionofpurecarbon gasification, whereas for DME and MeOH production, all the
with steam (+131.3 kJ/mol).9 This calculation gives the charisrequiredforheatproduction.Theseexamplesshowhow
maximum theoretical char conversion of X ≈ 0.75 for theexternalheatdemandcandeterminetheamountofcharto
ch,max
anyfuel.Indeed,thehigherthecharyieldfromafuel,themore be gasified or combusted, respectively.
important the char conversion becomes for the raw gas Considering overall plant efficiency, the heat and power
efficiency. production and/or consumption levels should be included, as
Considering aplantfortheproduction ofsecond-generation described by Heyne and Harvey:12
biofuels,multipleprocessstepsmustbeintegratedtomaximize
the total efficiency. Through process modeling, the heat μ LHV + (P e − l −α ref Q−) + Q−
prod prod η η
demands to be covered by the fuel burned in the combustion η = ref,el ref,q
sectionofanintegratedDFBgasifiercanbeestimated.Gassner sys
LHV +
(α
ref
Q−−P
e
−
l
)
+
Q+
et al.10 performed thermo-economic modeling of a plant for f η ref,el η ref,q (5)
C dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
whereLHVisthelowerheatingvalue,Pistheelectricalpower, the char yield can conveniently be investigated by proximate
Q is the heat, α is the electricity-to-heat ratio of a reference fuel analyses, it should be investigated with a heating rate
ref
plant, and η ref is the efficiency of a reference plant. The analogous to that of a fluidized bed (FB); otherwise, an
subscript “prod” denotes the chemical product of the plan, the
adjustment for the char yield should be applied so as to be
subscript “el” indicates the electricity, and the subscript “q” relevant to a fluidized-bed situation.4 As described by
denotes the district heating product. The following reference
Palchonok,17 the maximum heat-transfer coefficient to a single
values are used here: η = 0.32, η = 0.76, and α = 0.41.
Thesevaluesaredefined ref, f e o l rareferen re c f, e q biomasscomb r i e n f edheat fuel particle in a fluidized bed can be estimated by
andpower(CHP) plant, asdescribed byHeyne andHarvey.12
Using the values from Gassner et al.10 and Tock et al.,11 eq 5 Nuk g
h = 0.85
givesaplantefficiencyofη sys,SNG =0.75and,forliquidfuels,η sys eff d in (8)
= 0.33−0.68. It is clear that a high consumption of electricity
related to pressurized synthesis siginificantly decreases the with
efficiency. These scenarios do not consider any production of
districtheating,whichcouldfurtherincreasetheplantefficency. Nu = 0.85Ar 0.19 + 0.006Ar 0.5Pr0.33 (9)
Forexample,HeyneandHarvey12includeddistrictheatingand in in
showedasystemefficiencyforSNGwhereη =0.82−0.84.
Process Parameters. This work consi s d ys e ,S r N s G two types of gd 3(ρ − ρ)
in in g
parameters for the evaluation of a large-scale DFB gasifier: the Ar in = ν2ρ
process parameters and the performance parameters. The g g (10)
process parameters, which affect fuel conversion (as stated in
eqs1−3)areSFR,h ,T̅ ,T̅ ,τ̅ ,τ̅,u−u ,μ ,andμ ,and whereNuistheNusseltnumber,kisthethermalconductivity,
eff bed free rg s mf p O
these parameters are defined below. d is the particle diameter, Ar is the Archimedes number, Pr is
The SFR of a DFB biomass gasifier affects the gas the Prandtl number, g is the gravitational constant, ρ is the
composition and the amount of tar, as described, for instance, density, and ν is the viscosity of the bulk gas. The subscript
by Hofbauer and Rauch,13 who showed that the tar level “in”denotesan g inertparticleandthesubscript“g”indicatesthe
decreased with higher SFR. The SFR is defined as a mass of
bulk gas. The factor of 0.85 in eq 8 was proposed to
total water added to the gasifier per mass of dry ash-free (daf)
compensate for the observed effect of fuel particles floating on
fuel:
thesurfaceofthebed,17whichreducestheheattransfertothe
SFR = μ st ζ + μ m = (μ st,bed + μ st,S1 + μ st,S2 )ζ + μ m (6) fuel particle.
Theaverage temperatureofthebed(T̅ )affectsthe heating
whereζisthefractionofthesteamfedtothegasifierandloop G
seals that enters the gasifier, while the subscript “st” stands for rateandreactionrate,andanincreaseinbedtemperatureleads
steam, the usbscript “m” denotes fuel moisture, and the
toahighergasyieldandlowerleveloftars.6,15Thereisnoclear
subscript “bed” denotes the fluidized bed of the gasifier. The lowerlimitforthetemperatureatwhichtooperatethegasifier.
subscripts “S1” and “S2” denote loop seal 1 and loop seal 2, Nevertheless,attemperaturesof≥600°C,mostofthevolatiles
respectively.AconvenientwaytochangethevalueofSFRisto are released if the residence time is sufficient.8 Therefore,
change the level of fluidization steam (μ st,bed ). However, since operating the gasifier at <600 °C would result in unconverted
changing μ st,bed also affects other parameters, such as the volatiles leaving the gasifier. The reaction rate for char
fluidization velocity, itis important todescribe how the SFRis gasification is strongly coupled to the operating temperature,
changed when investigating its influence, which is however,
and an increase in temperature enhances char conversion.16,18
oftenforgottenoromitted.Alargefractionofthesteampasses
unreacted through the gasifier, and decreasing the amount of
Toachieverapidgasificationofchar,thetemperatureshouldbe
unused steam is, consequently, a key factor in improving the ashighaspossible.However,agglomerationissueslinkedtothe
performance of DFB gasifiers.6,13−15 The fraction of steam bedmaterialandfuelashesusuallydeterminetheupperlimitof
converted inthegasifiercanbeestimated byclosing thesteam the bed temperature. The highest temperature in the DFB
balance, which is defined as gasificationsystemisreachedinthecombustionsection.When
μ + μ lignocellulosesareusedasfuelandsilicasandisusedasthebed
st,rg st,reac
1 = material,thepeaktemperatureshouldbekeptbelow900°Cto
SFR + μ
st,vola (7) avoid agglomeration.19 At these temperatures, char gasification
wherethesubscript“reac”denotesreactionand“vola”denotes isstillaslowprocess,incomparisontothedevolatilizationand
volatiles.Forbiomass,thelevelofsteaminthevolatiles(μ ) the combustion of the char.4,16 Thus, char gasification is the
st,vola
typically is within the range of 0.05−0.20 kg/kg .8 rate-limiting step in the fuel conversion process.
daffuel
The heating rate of the fuel is an important parameter in The temperature in the freeboard (T̅ ) of the gasifier may
free
determining the yields of char, raw gas, and OC during differ from the temperature in the bed. Together with the
devolatilization,4,8 and it can also have an impact on the
average gas residence time, the temperature in the freeboard
t r h ea e c e ti ff v e it c y tiv o e f t c h o e effi ch ci a e r n .1 t 6 o T f h h e ea h t e t a r t a in n g sfe r r at ( e h ca ) n to be a d fu es e c l r p ib a e r d tic b le y . affects the gas-phase reactions, including the water-gas shift
The h parameter in a fluidized bed e d ff epends on several reaction (WGSR) and thermal tar decomposition.15,20 There-
propert e i ff es,suchasthesizedistributionoftheinertbedmaterial fore,itisimportanttomonitortheT̅ free value,aswellasthebed
particlesandthefuelparticles,locationofthefuelparticle,and temperature (T̅ ). Here, the average total residence time of
bed
fluidizationvelocities,asinvestigatedbyPalchonok.17Although the gas (τ̅) is estimated by
g
D dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
((1−ε s,G1 )V G1 +(1−ε s,G2 )V G2 )M g ⎛ P ⎞ devolatilized. The lateral mixing of fuel particles in a bubbling
τ g̅ =
ṁ rg ⎝
⎜
(cid:57) T f ̅ ree ⎠
⎟
w
be
h
d
ic
i
h
s
r
d
e
e
fl
s
e
c
c
r
t
ib
s
e
t
d
he
b
a
y
v
t
e
h
ra
e
g
D
e
a
fu
m
e
k
l
o
re
̈h
s
l
i
e
d
r
e
n
n
u
ce
m
t
b
im
er
e
(
i
D
n
a
r v e o l la a
=
tio
τ
n f
̅ /
t
τ
o vo t l h a
)
e
,
= ( ( ( 1 Q f − ) ε s ⎛ ⎜ ,G ( 1 1 ) − + Ych ( ) 1 +Y − chX ε ch s, + G2 S ) FR V V G G + 2 1 ) μ p M ⎞ ⎟ g⎛ ⎝ ⎜ (cid:57) T P f ̅ ree ⎞ ⎠ ⎟ 1 f t u i , m e s l e o c m f a o n e r o b d f e e t v a h o s e l s a u v t m i o li l z e a a t d i t l i e t o o s n l b e o e a f v f a e u s l f l u t y h e e d l e p g v a a o r s t l i a i fi c t e l i e l r i . z 4 u e n F d c , o o r a n n D v d e a r f v t o o e l r a d ≫ D w a i v t 1 o h , la t t ≪ h h e e
V G1 ⎝ LHVf ⎠ (11) char.
As mentioned above, the fluidization velocity can affect the
whereVisthevolume,Mthemolarmass,Pthepressure, the
(cid:57) fueldispersion,althoughitcanalsobeusedtodescribethebed
general gas constant, ṁ the mass flow, and LHV the lower
behavior and, for instance, the number of particles elutriated
heating value. The subscript “f” represents the daf fuel. into the freeboard.4,28 Therefore, it is important to include
Theaverageresidencetimeofafuelparticle(τ f ̅)inatop-fed fluidization as a parameter, here considered as the superficial
moving bubbling bed is estimated by a convective term (τ s ̅), velocity minus the minimum fluidization velocity:
which is a function of the solids flow through the reactor and
lateral dispersion (τ D ̅ ) of the fuel caused by the bubbling bed: μ (Q) T
1 u − u = st,bed V G1 (cid:57) st l 2β − u
τ f̅ = 1 + 1 mf M st P st LHV f car A,bed mf (15)
τ s̅ τ D̅ (12)
The fuel feeding to a gasifier requires a purge gas flow. The
τ s̅ = V G1 ε s,G1 ρ s amountofpurgegasthatentersthegasifierdependslargelyon
ṁ the design of the fuel feeding system. If the level of purge gas
s
(μ )ishigh,itmayaffecttherawgascomposition.Ifthepurge
ε ρC (T − T ) p
=
s,G1s p,s s,in s,out gas consist of inert gases, it dilutes the raw gas, but if reactive
(Q ) (Q ) gases are included, it will also change the composition of the
f s
V G1 Q f (13) gas. Therefore, the amount and composition of the purge gas
should be considered for the evaluation. If the purge contains
l2 β oxygen as when using recirculated flue gases or air, the oxygen
τ D̅ = car 2D l,bed (14) lev P el e i r s fo g r iv m en an b c y e μ O Pa = ra Y m O, e p μ te p . rs. Typical parameters used to
where C is the specific heat capacity, (Q/Q) is the energy describe the performance of a gasifier include the cold gas
transport p edtothegasifierrelatedtothefuel s inp f ut,andDisthe composition (C , the cold gas efficiency (η ) ; tar
i,cg cg
dispersion coefficient in accordance with Einstein.21 For concentration; carbon conversion; and steam balance.29,30
simplicity, it is assumed that the fuel particles have the same While these parameters provide vital information for the
average convective velocity as the bed material. Equation 14 is
processesdownstreamofthegasifier,theydonotgiveallofthe
validwhenthefuelfeedandoutflowofbedmaterialarelocated informationneededtodescribetheperformanceofthegasifier.
at opposite edges of the reactor. In the present study, these parameters are complemented with
Different methods have been proposed for quantifying the the gas yield (n ), raw gas efficiency (η ), conversion of char
i,cg rg
circulation flow of solids, whereby pressure measurements in (X ), and conversion of OC (X ), for the purpose of
ch OC
the top of the riser and the heat balance of an external cooler describing how and where in the process the fuel is converted.
have been applied for the Chalmers system.22,23 Another The carbon conversion is defined as the mass fraction of
approach for determining the circulation flowofsolids inDFB carboninthedaffuelthatisconvertedtogas.29Thisvaluedoes
systemsisbasedondefluidizationoftheloopseals,ashasbeen not give any information regarding whether the carbon is
appliedinthecoldflowmodelinvolvingan8-MWDFBgasifier convertedthroughchargasificationorthroughdevolatilization.
by Löffler et al.24 Since devolatilization is a much faster process than char
Fuel dispersion in fluidized beds has been investigated by conversion,4 this means that it is much easier to achieve high
several groups. Lui et al.25 prepared a summary of several carbonconversionwithamore-volatilefuel.Therefore,thiscan
studies that reported dispersion coefficients (D values) in the create a misleading impression when two different fuels are to
range of 10−2−10−4 m2/s for gas velocities relevant for the becomparedonthebasisofcarbonconversion,asitreflectsthe
present work of u − u < 0.5. More recently, Olsson et al.26 fuel characteristic rather than the gasifier performance.
mf
investigated the fuel dispersion in the Chalmers gasifier under Therefore, char conversion is the preferred parameter in the
cold conditions and derived a dispersion coefficient within the presentwork,andcarbonconversionisnotconsideredfurther.
samerange.Whileitisclearthatdispersionisdependentupon The composition of the cold gas (C ) is important for the
i,cg
several parameters, the parameters that have the greatest downstream equipment and is easily measured. However, to
impactsarethesuperficialgasvelocity,bedheight,particlesize, describe what happens inside the gasifier, it is preferable to
and pressure drop across the distributor.25−27 The phenomena study the gas yield (n ), which is directly coupled to the fuel
i,cg
thatgovernsthefuelresidencetimecanbeindentifyedfromthe conversion.Thecoldgasefficiency(η ),whichisacommonly
cg
dimensionless Peclet number (Pe = τ̅ /τ̅). For Pe ≪ 1, the used parameter, describes the amount of energy stored in the
D s
average fuel-particle residence time is controlled by dispersion, gas under ambient conditions in relation to the LHV of the
and for Pe ≫ 1, it is controlled by convection. If Pe ≈ 1, both fuel.29,30 The raw gas efficiency (η ) reflects the amount of
rg
the convective and dispersive effects should be considered to chemicallystoredenergyintheuntreatedgasinrelationtothe
describe the fuel-particle residence time. daf fuel, including both the cold gas and the OC.
ForaDFBgasifier,itisimportanttoknowifthefuelparticles The OC consists of tar and intermediate organics, which
have sufficient residence time in the gasifier to be completely cannotbemeasuredaspartofthecoldgas.Severalmethodsare
E dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
available to quantify the tar; among these methods, cold gasification reactor. Based on the total heat demands, the raw
trapping31andsolidphaseadsorption32(SPA)arethemethods gas efficiency is estimated through the heat balance:
that are applied most frequently. The amounts and
1 = ν + ν + η
compositionsofthetar20,33andOC8varywiththeoperational C G rg (22)
parametersofthegasifier,whichmeansthatthefractionofOC
where ν is the sensible heat (expressed in units of MJ/
that can be sampled with tar sampling methods may also vary. MJ ).Theenergyneededtoheateachmassflowisdivided
The fraction of tar in the OC is defined as dryfuel
into internal and external heat demands. The internal heat
μ μ demand must be covered by the heat produced in the
Y tar = μ tar ≈ μ C,tar combustor, whereas the external heat demand is provided to
OC C,OC (16) a mass flow prior to the reactor system. The heat demand for
the gasification reactor incorporates heating of the fuel, fuel
whereCstandsforcarbon.ThelevelofOCisestimatedasthe
difference in the levels of carbon in the raw gas and cold gas: moisture, steam, and purge gas, as well as the heat loss of the
reactor:
μ = μ − μ
C,OC C,rg C,cg (17) ν = ν + ν + ν + ν + ν
G G,f G,st G,m G,p G,hl (23)
The degrees of conversion (X and X ) are defined in a
OC ch
comparison with the devolatilization products, based in this γC (T − T )
study on the carbon contents for practical reasons that are ν G,f = f p,gas G ref
LHV (24)
explained further in the Experimental Section: f
μ γ ζμC (T − T )
X = 1 − OC ν = st st p,st G ref
OC Y OC G,st LHV f (25)
μ
C,OC
= 1 − ν =
Y G,m
C,OC
γ μ (C (T − T ) + h + C (T − T ))
μ m m p,st G evap evap p,m evap ref
C,tar
= 1 − LHV
Y Y f
tar C,OC (18) (26)
μ
X = 1 − ch μ p C p,p (T G − T p )
ch Y ch ν G,p = LHV (27)
μ f
C,ch
= 1 −
Y C,ch (19) ν = (A V out) G h c,G (T G − T sur )
Theamountofchar leavingthe DFBgasifiercanbe quantified G,hl (Q )
f
through balance calculations across the combustor34 or by a V (28)
G
carbonbalanceacrossthegasifier.35Byquantifyingtheamount
whereγisthefractionofinternalheatdemand,histhespecific
ofcarbonintherawgas,thecarbonbalanceenablescalculation
of the amount of char leaving the gasifier: enthalpy, (A out /V) is the outer surface area related to the
volume of the reactor, and h is the heat-transfer coefficient.
C
μ
C,rg
+ μ
C,ch
= Y
C,f
+ μ
C,p
+ μ
C,ch2 (20)
Thesubscript“evap”standsforevaporation,thesubscript“sur”
denotes the surrounding temperature, the subscript “ref”
where the subscript “ch2” denotes the amount of carbon
indicates the reference (reference conditions of T = 293 K
convertedfromcharentering thegasifierwiththe solids.If the and P = 101 kPa), and the subscript “hl” represents heat loss.
amountofunconvertedcharisknown,therawgasefficiencyis
The fraction of the heat demand to be covered internally is
η rg = 1 − X ch ⎛ ⎝ ⎜ L L H H V V c f h ⎞ ⎠ ⎟ (21) γ f = 1 − ⎛ ⎝ ⎜ ⎜ C C p p ,g ,f as ⎞ ⎠ ⎟ ⎟ T G * (29)
Heat Balance. In an SNG plant, the external heat demand
can be the limiting factor for the degree of fuel conversion in ⎛ C (T − T ) ⎞
h th e e at g d a e si m fie a r n . d H in ow th ev e e g r, as f i o fi r er a is st t a h n e d- n a e lo xt ne lim g i a t s i i n fi g er f , ac t t h o e r. in T t h e i r s na is l γ m = ⎝ ⎜ ⎜ 1 − C p,st (T G − T evap ) p + ,m H e f vap + re C f p,m (T evap − T ref )⎠ ⎟ ⎟
also the case for a gasifier in a plant with either low heat
(1 − X )
demand or additional heating sources. By establishing a heat evap (30)
balance for the process, the internal heat demand can be
calculatedandcomparedwiththetheoreticalrawgasefficiency. γ st = 1 − T G * (31)
The simplified heat balance proposed here describes where the dimensionless temperature (T*) is defined as
efficiency of a DFB gasifier, based on the internal heat
demands. A similar black box model was previously proposed T*= T i − T ref i = f, st, p, air; j = C, G
by Goḿ ez-Barea and Leckner4 to compare direct and indirect j T − T
gasifiers. In this work, the calculations are focused on DFB j ref (32)
gasifiers and to quantifying the heat demands based on the Theheatdemandofthecombustionreactorinvolvesheatingof
degree of conversion of char (X ) and OC (X ) in the the combustion air, char, and steam entering the combustor,
ch OC
F dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
Figure 4. Schematic of the system at Chalmers University of Technology.
togetherwith theheatlosses fromthe combustor,asdescribed ⎛Q̇ ⎞
by ν
C,B
=
⎝
⎜⎜
Q̇
B
f ⎠
⎟⎟
(38)
ν C = ν C,ch + ν C,air + ν C,st + ν C,hl + ν C,B (33)
̇ ̇
where AFR is the air-to-fuel ratio, the term (Q /Q) is heat
B f
Y (1 − X )C (T − T ) subtracted from the combustion section, relative to the fuel
ch ch p,flue C G
ν =
C,ch LHV (34) feed to the gasifier, and the subscript “air” stands for
f
combustionair,thesubscript“air,stoich”standsfortheamount
μ AFRγ C (T − T ) ofairneededforstoichiometriccombustionofthechar,andthe
ν C,air = air,stoich a
L
ir
H
p
V
,flue C ref
(35)
subscript“flue”representsthefluegas.Thecombustionaircan
f
be preheated through heat exchange, as described by
(1 − ζ)μC (T − T )
ν = st p,st C st ⎛C ⎞
C,st LHV f (36) γ air = 1 − ⎝ ⎜ ⎜ C p p ,f ,a lu ir e⎠ ⎟ ⎟ T C * (39)
(A out)
h (T − T )
ν = V C c,C C sur In all of the applications, with the exception of direct
C,hl (Q ) combustion of the gas, only the cold gas is utilized, and the
f
V G (37) cold gas efficiency is estimated based on the fuel conversion:
G dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
η = η − η availableforthegasifier,ensuringthattheheatdemandofthegasifier
cg rg OC
can be met across the entire range of operational settings and
Y (1 − X )LHV feedstocks, as the heat demand of the gasification process is always
= 1 − ν − ν − OC OC OC
C G covered.
■ LHV f (40) Measurements. To quantify the process parameters and the
evaluation parameters, as defined above, measurements are required
EXPERIMENTAL SECTION of all the ingoing and outgoing mass flows of the gasifier (fuel feed,
steam, solids, raw gas, and purge) (see Figure 6). Dimensionless
Procedures. Industrial-scale experiments were conducted in the
Chalmers gasifier to develop an experimental method for quantifying
the operational and performance parameters discussed above. In
addition, bench-scale pyrolysis experiments were conducted to
characterize the fuel, in terms of yields from the devolatilization step
of the fuel conversion, as described by eq 1.
The Process at Chalmers. The Chalmers 2−4-MW gasifier is
th
connected to the 12-MWth circulating fluidized bed (CFB) boiler at
ChalmersUniversityof Technology36−38(seeFigure4).Thefurnace
(1)hasasquarecrosssectionof2.25m2andaheightof13.6m;the
fuel is fed at the top of the furnace bed via the fuel chute (2). The
solids circulate via a cyclone (4) through a particle distributor (9).
From the particle distributor, the solids can be directed differently,
depending on the operational goals. For standard operation of the
boiler,the solidsaredirected straight backtothe boiler.Ifadditional
coolingofthebedmaterialisrequired,thesolidsaredirectedthrough
anexternalparticlecooler(10).Whentheexternalcoolerisfluidized,
the solids naturally pass through the cooler due to its vertical
alignment.Inaddition,theChalmerssystemhasbeenretrofittedwith
Figure 6. Illustration of the ingoing and outgoing mass flows of the
anadditionalgasificationreactor(11).Byfluidizingthetwoloopseals
gasifierandthepositioningofthetemperaturemeasurementsT1−T5.
(12and13),thesolidsenterthegasifieratthebottomofthebedand
exitby flooding over abarrier at the end of the gasifier.
Thegasificationreactorisfluidizedwithsteamorfluegases,anditis
operatedwithintheregimeofabubblingbed.Thefuelforthegasifier
is stored in a silo (15), and this fuel is fed by a screw feeder and Table 1. Summary of Dimensionless Reactor Parameters
eventually introduced at the top of the gasifier bed via two in-series
parameter value
coupledrotaryvalves(14).Figure5illustratesthefuelfedandthegas
volumetosampling/reactorvolume,V /V 0.04
G2 G1
characteristiclength,l (m) 1.58
car
shapefactor
volume,β 0.80
V
bedarea,β 0.59
A,bed
bedlength,β 1.17
l,bed
volumefractionoccupiedbysolids
ε 0.12
G1
ε n.a.a
G2
aNot available.
reactorparametersoftheChalmersgasifieraresummarizedinTable1.
Positions T1−T5 in Figure 6 identify the positions of the shielded
Type K thermocouples used for temperature measurements. The
averagetemperatureofthebed(T̅ )wasestimatedfromthelevelsat
G
positions T2 and T3. The average temperature of the gas in the
freeboard (T̅ ) was estimated as the average of the temperatures at
gas
T̅ and T5.
bed
All the investigated mass flows are related to the daf fuel, and the
massflowoffuelwasmeasuredasthelossofmassovertimeinthefuel
Figure 5. Schematic of the fuel feedingsystem. silo by four weighing cells. The fuel samples were characterized by
standardfuelanalysisintermsofultimateandproximateanalysesfor
biomass. Ultimate fuel analysis was performed by the Technical
purging system. Dried flue gases are used as purge gases to cool the Research Institute of Sweden, which determined the ash contents
rotary valves and prevent gas exchange between the gasifier and the (Method SS-EN 14775), carbon, hydrogen, and nitrogen (Method
fuel silo. CEN/TS 15104), heating value (Method SS-EN 14918), and the
Inthecurrentsetup,themajorfractionoftherawgasisfedtothe oxygen content by difference. The moisture content of the fuel was
boilerforincineration.However,asmallfractionofthegas(∼400W) measuredbygravimetricanalysisofthedryandwetfuel.Eachsample
is sampled for determination of the gas composition. For safety wasfirstdriedat105°Cfora24-hperiod.TheyieldsofcharandOC
reasons, the Chalmers gasifier is operated slightly below atmospheric fromthewoodpelletswereanalyzedusingabench-scalefluidizedbed,
pressure,whichismaintainedbythefluegasfanoftheboiler(8).The as described in the Pyrolysis section.
large amount of additional fuel that is fed to the combustion side The mass flows of steam to the loop seals and gasifier were
distinguishes the Chalmers system from a stand-alone plant, such as determined fromthe differential pressures induced over orifice plates
the plant in Güssing.39 This means that a large surplus of heat is inthesteamlines.Afractionofthesteamfedtotheloopsealsenters
H dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
thegasifier;the actuallevelswere estimatedusingatracer gas.Using Having determined the amounts of carbon in the raw gas and the
theBronkhorstmassflowcontroller(ModelMFCF-202AV),known cold gas, the amount of OC, μ , was estimated using eq 17. The
OC
amounts of helium were injected sequentially into each vessel while composition (Y ) and heating value (LHV ) of the OC were
j,OC OC
theheliumconcentrationinthecoldgaswasdetermined.Theaddition estimatedbytakingtheaveragevalueofthecomposition fortheOC
of helium to the gasifier gives a reference concentration of helium in sampled through SPA. Samples collected with SPA were eluted and
thegas,andaddingheliumtoasealgivesaconcentrationofheliumin analyzed in a gas chromatography-flame ionization detection (GC-
the gas that is proportional to the fraction of steam entering the FID)system,accordingtotheproceduredescribedbyBrageetal.9and
gasifier. In addition, the temperature and pressure of the steam were Israelssonetal.40Here,4−6amineswereusedforeachcase,andeach
measured, to estimate the superficial gasvelocity. sample was analyzed three times in the GC-FID system (for more
A continuous slipstream of raw gas was extracted and analyzed in details, see the work of Israelsson etal.41).
the gas conditioning system including particle removal through a
ceramic filter at 350 °C and a cooled isopropanol quench for tar μ rg LHV rg
η =
removal. For more information on the gas cleaning system, see the rg LHV
f
Supporting Information. A microgas chromatography (micro-GC)
system at position K is used to measure the permanent gas μ cg LHV cg +μ OC LHV OC
=
concentrations (C ). The micro-GC system (Varian, Model
CP4900) was equip i p ,c e g d with one molecular sieve column with argon LHV f (44)
as the carrier gas to include measurements of helium, and one Themassflowofsolids(ṁ )wasestimatedfromatemporaryholdup
s
Polarplot Q column with helium as the carrier gas. A three-point in the solids circulation in the system, which was achieved by
calibrationmethodwasused,andthegasspeciesthatweremeasured defluidizing loop seal 2 (Figure 6). As the circulation stops, the
withthisGCsetupwere:He,H 2 ,CO,CO 2 ,CH 4 ,C 2 H 2 ,C 2 H 4 ,C 2 H 6 , combustorisdrainedofitsbedinventory,whichresultsinadecrease
C 3 H 6 ,C 3 H 8 ,N 2 ,andO 2 .Themethodusedallowsforsamplingevery in the pressure drop over the furnace, from which the bed material
140s. Themolar yieldofgas (n i,cg ) wasquantified usingthe helium- flow is estimated by
tracer method, which also enables the calculation of the cold gas
efficiency:
ṁ =−
dΔP A
s dt g (45)
⎛V̇ ⎞ ⎛ P ⎞
n i ̇ = ⎝ ⎜ C H H e e ⎠ ⎟C i⎜ ⎝ (cid:57) T ⎟ ⎠ i=measured gas components (41) w se h c e ti r o e n d al Δ a P re / a dt of is th th e e C p F r B es , s a u n r d e g dr i o s p th c e h g a r n a g v e ity w c it o h n t s i t m an e t , . A Fo i r s v t a h l e id c a r t o io s n s- ,
theresultswerecomparedwithvaluesestimatedfromtheheatbalance
η = ∑ i n M i̇L i H ṁ V f i +⎜ ⎛ ⎝M μ O O 2 2 − μ M ch C 2 ⎞ ⎠ ⎟Δh comb,H2,CO o co f n T t s h h is e e te g m n a t a si s w fi s e it o r h , fc o p a p r r e e b v r o i a o n t u ed s co i w n n v v it e e h s r o t t e i u g d t at f i a r o d o n d m s it ( i c o e h n . a g r ., o e f t n h f t a u e t e r o i l n ; f g t E h t d i h s v e a p r g d r a o s s c s ifi o ed e n r u 22 r w ) e . it i h s
cg LHV f the solids (μ C,ch2 ) was quantified by the He-tracer method, when
i=measured gas components (42)
operatingthegasifierundersimilaroperationalconditions,butwithout
fuel.Thisshowsthatμ ≈0−0.02forsimilartemperatureandsolid
C,ch2
whereV ̇ isthevolumeflow,ṅisthemolarflow,andΔh isthe circulationrates.Thereactorheatlossesweremeasuredbyoperation
comb,H2,CO in the absence of any fuel fed to the gasifieritself:
enthalpyofreactionforcombustionofamixtureof50%H and50%
2
CO (Δh = −524.8 kJ/mol ). This holds true for removing ṁ
comb,H2,CO O2 ν = sC (T −T)−ν +μ Δh
the energy added to the cold gas by gasification of the char entering G,hl ṁ p,s 1 4 G,st C,ch2 gasif (46)
f
with the solids, without considering the water gas-shift reaction
(WGSR). It is also used to approximate the energy loss due to Pyrolysis. The yields of char and OC from the fuel were
combustionoftherawgaswithO,undertheassumptionthatH and investigatedinbatchpyrolysisexperimentsperformedinabench-scale
CO are the major gas componen
2
ts. Gas-phase thermochemical
2
data
fluidizedbed.Woodpelletsfromthesamebatchasthatemployedin
used for the calculations were retrieved from NIST.9 A gas cleaning experiments in the Chalmers gasifier were used for the batch
systemofthistypehasbeenevaluatedindetailbyKaufmanRechulski experiments, and the pellets were dried for 24 h at 105 °C. The
etal.40 andhas been shown to givereliable results when cooled to 0 experimental setup is described in detail by Neves et al.,42,43 and a
°C for all gas components, with the exceptions of CH and CH, summaryoftheprocedureisgivenhere.Singlepelletswereconverted
which exhibit slightly higher levels of uncertainty, be 2 ca 2 use of t 3 hei 6 r in a fluidized bed and the produced gas was cleaned using a dry
solubilities. Furthermore, with a negligible amount of nitrogen in the
impingertraincooledto0°C,followedbypassagethroughtwopaper
fuel, the purge gas is the only nitrogen source to the gasifier, which filterstoretainaerosols.Usingsamplingbags,asampleofthecoldgas
meansthattheamountofpurgegasenteringthegasifier(μ)isgiven was collected for each batch, and a known amount of helium was
bythe GCmeasurments:
p injectedintothebagasatracer,enablingquantificationofthecoldgas
yield.Thecompositionofthegaswasmeasuredwiththesamemicro-
⎛M P⎞ ⎛C ⎞⎛M P⎞ GC system used in the industrial-scale experiments described above.
μ p =V N2⎝ ⎜ ⎜ (cid:57) T g g ̅ as⎠ ⎟ ⎟ =V He ⎝ ⎜ C H N2 e ⎠ ⎟ ⎝ ⎜ ⎜ (cid:57) T g g ̅ as⎠ ⎟ ⎟ (43) C sc h al a e r , w an a d s c t o h l e le c c h te a d r c fr o o m m po th si e tio b n ed w , a to s o m b e t a a s in u e re d t f h ro e m ch a a n r y u i l e t l i d ma u t s e in f g ue a l
analysis.TheamountofOCwascalculatedbythedifferencefromthe
The total amount of carbon in the raw gas was quantifyed by carbon balance, asin eq 20.
combustion of the raw gas. A short description of the combustion Conditions. One parameter that influences fuel conversion is the
method follows, and the full experimental setup and detailed choice of bed material, since some materials can induce relatively
description are provided in detail by Neves et al.35 A slipstream of strong catalytic effects.44 To quantify the impacts of different bed
rawgaswasburnedinairandthefluegaswasanalyzedinthemicro- materials,areferencecasemustbeestablishedforabedmaterialthatis
GC system, as previously described. Furthermore, the He-tracing asinertaspossible.Sincesilicasandhasanegligiblecatalyticeffecton
methodwasappliedtothegasifiertodeducethemassflowofcarbon fuel conversion,44 it was chosen as the bed material for the present
in the raw gas, μ . The amount of C in the raw gas could then be work.Theaverageparticlediameterofthesilicasandwas300μm,as
C,rg
estimatedfromtheratioofCO toHe.TheOandHbalancesinclude measured for used particles through sieving.
2
alsowater,whichwasmeasuredwithlessaccuracythanthepermanent The effect of changing the amount of fluidizing steam was
gases.Therefore,tominimizeuncertainties,thecalculationsarebased investigated at three levels, referred to as cases A, B, and C, while
on the Cbalance. all the remaining parameters were maintained asconstant aspossible
I dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
(see Table 2). Wood pellets were used as the fuel (Table 3), and Table 4. Summary of Process Parameters Resolved from
during the period of the experiments, the combustor and the gasifier Three Cases with Different Levels of Fluidizing Steam
Table 2. Operational Parameters parameter equation caseA caseB caseC
steam-to-fuelratio,SFR 6 0.84 0.92 1.06
operationalparameter CaseA CaseB CaseC (kg/kg )
daffuel
bedtemperature,T (°C) 838 835 836 effectiveheat-transfer 8−10 928 929 929
f fl u u e i l di e z ff in e g ct, st Q e ̇ a G m /V , G μ 1 st 2 , ( be M d W (k / g/ m k 3 g ) daffuel ) 0 0 . . 5 5 9 9 0 0 . . 7 6 2 1 0 0 . . 8 6 5 1 av c p e o r a a e r g t ffi i e c c le b ie s e n , d h t e t f f e o f m ( r W p fu e / e r ( l a m tu 2 re K , )) 833 829 831
solidsflow,Q ̇ /Q ̇ (MW/MW ) 0.18 0.18 0.20 T̅ (°C)
s f daffuel bed
averagegastemperature, 791 797 801
Table 3. Fuel Composition
T̅
gas
(°C)
averagesolidsresidence 13 143 148 123
Case time,τ s ̅ (s)
fuelanalysis CaseA CaseB CaseC Pa averagefuelresidencetime, 12−14 78−132 79−136 72−115
τ̅ (s)
f
averagegasresidencetime, 11 3.91 3.58 3.25
moisture(% mass,as‑received ) 9.4 7.6 7.6 0b τ g ̅ as (s)
ash(% mass,dry ) 0.5 0.4 0.4 0.4 gasvelocityforfluidization, 15 0.07 0.11 0.16
u−u (m/s)
mf
C(% mass,daf ) 50.65 50.55 50.55 50.55 pu ( r k g g e / g k a g samo ) unt,μ p 43 0.044 0.053 0.046
H(% ) 6.13 6.13 6.13 6.13 daffuel
mass,daf oxygenamountinthe 0.002 0.003 0.002
O(% mass,daf ) 43.22 43.22 43.22 43.22 purgegas,μ O2
N(% mass,daf ) 0.06 0.07 0.07 0.07 (kg/kg daffuel )
S(% ) 0.01 0.01 0.01 0.01
mass,daf
Cl(% ) 0.01 0.01 0.01 0.01
mass,daf
lowerheatingvalue,LHV(MJ/kg ) 18.99 19.03 19.03 19.03
daf
aPyrolysis experiments. bDriedprior to experiments.
were operated continuously, producing heat for district heating. Fuel
wasfedtothegasifierfor∼8hperday,andtheresultspresentedfor
each case correspond to stable operation of ≥60 min. In addition,
c■ombustionof aslipstreamof theraw gaswas performedfor case C.
RESULTS AND DISCUSSION
The general evaluation method was demonstrated in the
Chalmers gasifier, to show how the method can be
experimentally applied for evaluations of the fuel conversion
and performance of a large-scale DFB gasifier. A characteristic
of large-scale applications is that the heat losses are small, in
relation to the fuel input. The heat losses from the Chalmers
gasifierwereestimatedas1.7% (recalleq46)ofthefuelinput.
Thus, heat losses had a minor impact on the results,
Figure 7. Solids flow as estimated by defluidization versus the solids
emphasizing that the following results are valid for industrial-
flow, as estimated by heat balance.
scale applications.
ProcessParameters.Thefuelconversion intheChalmers
gasifier was investigated for three operational cases, using which involve considerably less effort than the heat balance
different amounts of steam to fluidize the bed of the gasifier. approach.
Fuel conversion in a gasifier is affected by several process The average residence time of the fuel particles is given as a
parameters, as given by eqs 1−3, and these parameters are range, because of uncertainties related to the dispersion
summarized in Table 4. coefficient, D = 10−2−10−4 m2/s. Still, the Peclet number for
Table 4 shows that the gasifier temperature was maintained the fuel particles are in the range of Pe = 0.07−0.86, which is
within the range of ±2 °C in the three cases, which is <1,indicatingthatthesolidsflowgovernstheresidencetimeof
consideredequivalent.Furthermore,thelevelsofpurgegasand the fuel. Furthermore, the time for devolatilization was
O used for purging are comparable between the cases, and determined during the pyrolysis experiments to be 43 s,
2
sincetheamountofO islessthanthatneededtoconvert0.5% which, when compared to the fuelresidence time, gives a Da
2 py
of the fuel energy into heat, it had no significant effect on the valueof0.33−0.60.Thisindicatesnotonlythatthefuelisfully
product. The average residence time of the solids varied by devolatilized in the gasifier, but also that there is a
±10% of the average value (eq 13). The method for misdistribution of released volatiles, with higher levels of
quantification of the solids flow was validated by comparison volatiles being released near the fuel feed.
withtheheatbalance(seeFigure7).Thetwomethodsshowed The amount of steam that enters the gasifier was quantified
agreementwithin±10%.Thisshowsthatthesolidsflowcanbe by the He-tracer method by sequentially injecting helium into
determined in a satisfactory manner by defluidization tests, thegasifier,seal1,andseal2,asillustratedforcaseCinFigure
J dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
8. Approximatley 75%−85% of the steam followed the same When compared with the char yield this enables an estimation
directionasthesolids,morespecifically,83%forseal1and75% of the char conversion (eq 19) as X = 0−0.04, which shows
ch
that char conversion is very limited under the current
operational conditions.
The lack of char conversion, even at 830 °C, calls into
questionthepurposeofhavingatemperatureof>600°C,since
the major share of the devolatilization is completed at 600 °C.
However,thetemperaturehasastrongeffectontheamountof
OC formed, and as the yield of OC (Y ) decreases as the
OC
temperature increases, it can still be beneficial to use a high
temperature to reduce the amount of OC.8
Tar and OC. Figure 9 shows the mass and energy fractions
of the tar and OC, whereby tar is a fraction that is included in
Figure 8. Measured helium levels in the cold gas while injecting the
same flow into the gasifier, seal 1, and seal 2, sequentially, during
experimental case C.
forseal2duringcaseC.Thisgassplitismostoftenomittedin
the literature, assuming that all gas follows the direction of the
solids;however,resultsfromthisstudyshowsthatasignificant
amount of the gas can travel against the solids flow.
From Table 4, it is clear that increasing the amount of
fluidization steam results in an increase in SFR, T̅ , and u −
gas
u , as well as a decrease in the gas residence time. Therefore,
mf
eqs 1−3 is simplified: Figure 9. Levels of tar and OC as a function of the amount of
fluidizingsteam,wheretheOClevelsareestimatedfromboth(△)the
Y i = constant i = ch, cg, steam, andOC (47) amountofcarboninthecoldgasand(□)thefractionoftarintheOC
determined from case 3.
X
char
= f(τ f̅, SFR, u − u
mf
) = f(μ
st,bed
)
(48)
theOC.ForcaseC,theamountofcarbonintheOCwas0.062
X OC = f(T g ̅ as , τ g̅as , SFR, u − u mf ) = f(μ st,bed ) (49) kg C /kg daffuel and compared with the OC yield from
devolatilization; this corresponds to a degree of conversion of
This suggests that a more-detailed investigation is needed to
X =0.36(eq18).ThefractionofthemeasuredtarintheOC
distinguishtherespectiveimpactsofSFR,T̅ ,τ̅ ,andu−u . OC
gas gas mf for case C was Y = 0.35 (eq 16), which shows that a
However,theoveralleffectcanbedescribedasafunctionofthe
significant amount o
ta
f
r
the OC is not taken into account by the
amount of fluidization steam, relative to the daf fuel (μ ).
st,bed SPA method. The missing fraction is likely to be light
Several investigations can be found in the literature, which
components and include volatile hydrocarbons, such as
describes the effect of changing the SFR without stating the
benzene and butane.
mannerinwhichitwasalteredorifchangesarebeingmadeto
The levels of OC in cases A and B were not measured.
thefluidizationandresidencetime.Thereby,thereisariskthat
Instead,theamountsofOCinthesecasesarehereestimatedin
the combined effects of changes in several parameters are
two ways: from the tar fraction (eq 16 and the open triangle
ascribed as an effect of the SFR.
(△) in Figure 9), and, based on the amount of carbon in the
Devolatilization Yields. The results from the batch
cold gas (eq 50 and the open square (□) in Figure 9). If the
pyrolysisexperimentsshowthatthecharandOCyieldsduring char conversion (X ) and purge gas flow (μ ) are known, the
devolatilizationunderthefluidizedbedconditionat830°Care ch p
amountofOCcanbeestimatedbycomparisontotheamount
asfollows:Y =0.16kg/kg ;Y =0.258kg /kg and
ch daffuel cg,C C daffuel of carbon in the cold gas during the pyrolysis case:
0.004 kg /kg as soot; and Y = 0.094 kg /kg
C daffuel OC,C C daffuel
(where the yield of OC is calculated from the carbon balance, μ = Y − ( (μ − μ X − μ ) + Y )
as per eqs 20 and 17). The daf composition of the char was C,OC C,OC C,cg C,ch ch C,p C,cg
93.1%carbon,1.2%hydrogen,5.3%oxygen,and0.4%nitrogen. (50)
The char composition and yield of OC concur well with the Here, char conversion is assumed to be constant for all the
valueslistedintheliteratureforthegivenfuelandconditions.8 cases and equal to that observed for case C: X ≈ 0.02. In
ch
Char Conversion. The amount of unconverted char was Figure 9, it can be seen that the two approaches give similar
calculated for case C from the carbon balance (see eq 20). trends, with a somewhat higher amount of OC based on the
K dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
amount of tar (eq 16). The discrepancy is related to Figure 11 displays the molar yields, calculated from eq 41,
uncertainties associated with both the pyrolysis yields and the with the purge gases subtracted to show the actual yield. The
measurements of the cold gas, purge gas, and char conversion.
The degree of conversion of the OC, as a function of the
amount of steam, is described by X = 0.424 μ .
OC st,bed
The biggest difference in composition is noted for unknown
compounds larger than pyrene, which decreases, and for
naphthalene,whichincreases.Thedewpointoftariscontrolled
mainly by the levels of large components, such as pyrene and
coronene. Although no coronene was detected, several
unknown components were found after (although close to)
pyrene, which together with pyrene, define the dewpoint. The
dewpoint was roughly estimated as being <260 °C45 for all
cases, with a decreasing trend as the level of steam was
increased. The average elemental composition and heating
valueofthetararesummarizedinTable5.Theamountofeach
tar component can be found in the Supporting Information.
Table 5. Elemental Composition and Lower Heating Value
of the Tar Sampled with the SPA Method
CaseA CaseB CaseC
carbon(% ) 91.0 91.1 91.3
mass
hydrogen(% ) 6.7 6.6 6.6
mass
oxygen(% ) 2.3 2.3 2.1
mass
lowerheatingvalue,LHV(MJ/kg) 39.2 39.2 39.2
Figure 11. Gas yield as a function of the level of fluidization steam.
The purge gas is subtracted to show the gas yielded from the fuel
Gas Composition and Yield. Figure 10 shows the gas
conversion.
composition as a function of the μ , including the pyrolysis
st,bed
molar yields show that the level of CO is stable and, in fact,
resembles the yield from the pyrolysis case. Furthermore, the
amounts of H , CO , and CH increase with the μ , also
2 2 4 st,bed
showing that the amount of carbon in the cold gas increases.
Withverylimitedcharconversion,theincreaseofcarboninthe
cold gas indicates that conversion of OC increases with higher
valuesofμ .Basedonthisfinding,aglobalreaction(eq51)
st,bed
can be defined to describe the change in cold gas per mole of
carbon of OC converted while μ increases:
st,bed
CH O + zH O → 1.4H + 0.7CO + 0.3CH
x y 2 2 2 4 (51)
The amount of water consumed in this global reaction is
estimated based on the oxygen balance as z ≈ 1.4 mol/
mol , which for case C corresponds to a steam
CinOC
consumption of μ ≈ 0.07 kg /kg . Thus, eq 7 gives
st,reac H2O daffuel
an estimation of the pyrolytic water (μ ≈ 0.1 kg /
st,pyro H2O
kg ), which is consistent with the results in the literature
daffuel
for pyrolysis experiments.8 Therefore, the amount of water
consumedisevenlessthantheamountofwaterformedduring
devolatilization, and only ∼5% of the steam formed or
mass
added to the gasifier is converted. The OCs consist of
componentswithanenthalpyofformationpermoleofcarbon
Figure 10. Gas composition as a function of the level of fluidization in the range of −31 kJ/(mol °C) for butane and +15 kJ/(mol
steam.Errorbarsindicatethestandarddeviationfromthemeanvalue °C) for napthalene, from which the average enthalpy of
of the gasmeasurements for each case. reaction, Δh OC,reac , is estimated as being between +71 kJ/(mol
°C) and +117 kJ/(mol °C), indicating an endothermic
reaction. For case C, this corresponds to a total reaction
case with μ = 0. The gas composition tends toward higher enthalpy of 0.01−0.02 MJ/MJ .
st,bed daffuel
H and CO concentrations with increased μ . Meanwhile, The composition of the raw gas (Figure 12) includes steam,
2 2 st,bed
the concentration of CO decreases, leaving the CH content cold gas, and OC. The error bars are based on uncertainties
4
moreorlessunchanged.TheratioofH toCOisenhancedby associated with the condensation measurements and illustrates
2
theintroductionofmoresteam,from0.35forthepyrolysiscase arangeof±10%ofthemeasuredamountofwater.TheOCis
to 0.7 at μ = 0.85. roughly estimated to have the same average molar mass as the
st,bed
L dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
0.61whentheμ isincreasedfrom0.59to0.85.Thiscanbe
st,bed
compared with the pyrolysis process, which yielded a cold gas
efficiency of 0.52 at the same temperature. The raw gas
efficiency (denoted by the open circle (□) in Figure 13) was
estimated from eq 44, whereas the amount of OC was
calculated from eq 50. For case C, the raw gas efficiency was
also calculated based on the char conversion quantified from
combustion oftherawgas(denotedbythe solidtriangle(▲)
in Figure 13, eq 21). It is clear that the two approaches for
assessingtherawgasefficiencyconcurandthattheefficiencyis
moreorlessconstantforallthecases,whichitshouldbeifthe
char conversion is the same. The observed deviation may be
related to the assumed heating value of the OC and
uncertainties related to the quantification of both the OC
and char conversion. The raw gas efficiency for the Chalmers
gasifieris∼74%,whichiscomparabletothechemicalefficiency
of a plant for the production of second-generation biofuels
(74%−77%),asderivedbythermochemicalmodeling.10,11This
confirmsthat,evenwithaverylowcharconversion,agasifierof
thistypewouldperformwellinsuchaplantusingwoodpellets
asfuel.ThelargeamountofenergyintheOC,upto15%ofthe
energyinput,showsthe importanceofconvertingtheOCinto
Figure 12. Gas composition as a function of the level of fluidization cold gas, through either primary or secondary measures.
steam.Errorbarsindicate±10% ofthelevelofsteam.Notethat Heat Balance. To illustrate the information gained from
the OC concentration is multipli r e el d ativ b e y10, tomake itmore visible. establishing the heat balance of a DFB gasification system,
resultsfromtheChalmersgasifierareusedhere,togetherwitha
putative combustor reactor to exemplify a stand-alone DFB
SPAtar,M tar =145g/mol.Itcanbeseenthat,forallcases,the gasification system. The heat demand of the gasifier was
concentrationofOCis<1%.Toachievehigheraccuracyforthe estimatedbyeqs23−32,andtheputativecombustionpartwere
concentrations, the steam measurement should be improved roughly estimated to have the same size (and, thus, equivalent
andbetterknowledgeofthecompositionoftheOC,especially heatloss)asthegasificationsection,allowingtheheatdemand
in the range of 3−7 carbon atoms, should be acquired. of the combustor tobe calculated by eqs 33−39. Based onthe
Chemical Efficiency. Figure 13 shows the chemical heat demand, the raw gas efficiency (eq 22) and cold gas
efficiencies of the raw gas and cold gas, as well as the energy efficiency (eq 40) were estimated (see Figure 14). The trends
content of the OC as a function of the amount of fluidizing inFigure14showsthat,forμ ≈0.5,alloftheenergyinthe
steam.Thecoldgasefficiency(denotedbythesolidcircle(●) st,bed
in Figure 13) of the Chalmers gasifier increases from 0.58 to
Figure 14. Gasification performance as a function of the amount of
fluidizingsteam.Resultsshownarefromtheheatbalancecalculations
Figure13.Chemicalenergylevelsintherawgas,coldgas,andOCas and experiments: (a) the heat demand that can be covered by char
afunctionofμ .Therawgasefficiencyiscalculatedas(□)thesum combustion and (b) the additional heat demand. If there is no char
st,bed
ofthecoldgasandOC,aswellas(▲)fromthecharconversionfor conversioninthegasifier(X =0),then(c)heatshouldbesubtracted
ch
case C. from the combustion section.
M dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
charisneededforheatproduction,andforμ >0.5,someof Evaluation of Industrial-Scale DFB Gasifiers. A general
st,bed
thegasoradditionalfuelmustbecombustedtocovertheheat procedureforevaluationofindustrial-scaleDFBgasifiersishere
demand.Forμ <0.5,theheatdemandissufficientlylowto proposed. The parameters that should be included in such an
st,bed
make room for char gasification and thus, higher raw gas evaluation were considered and it was concluded that
efficiency. commonly evaluated parameters, such as the composition of
The cold gas efficiency is affected by the degree of permanentgasesandthetarconcentrations,provideimportant
conversion of char and OC where the char conversion is information for the design of downstream equipment.
given by the heat balance and the OC conversion is estimated However, in terms of describing and quantifying the fuel
as a function of the fluidization steam, as given by the conversion in a DFB gasifier, these parameters are not
measurements.Ifthelevelofcharconversioncanbecontrolled sufficient.
and a secondary measure to convert the OC into cold gas is Itisclearthat,foraDFBgasifier,thedegreeofconversionof
available, it may be valuable to reduce the amount of steam to char in the gasifier is a better indicator of fuel conversion than
increase the efficiency. If, alternatively, a scrubber is used to the total carbon conversion, as the latter is very dependent
remove the OC from the raw gas, it is better to increase the upon the fuel characteristics. Therefore, the fuel conversion is
amountofsteamasfarastheheatbalanceallows(μ ≈0.5, described,inthiswork,bythedegreeofconversionofcharand
st,bed
for the present case) to reduce the amount of chemical energy of organic compounds (OC) by comparing the product yields
in the OC and increase the cold gas efficiency. with the yields during devolatilization of the fuel. Investigating
As discussed, to have a high efficiency, the internal heat how the degree of conversion of char and OC is affected by
demand should be minimized and the contributing factors can differentprocessparametersenablesanalysisofhowtheprocess
be studied from the heat balance. The major contribution to can be improved.
the internal heat demand generally comes from heating of the Experimental Approach and Change in the Level of
fuel, steam, and combustion air. Through system integration FluidizingSteam.Themethodologypresentedherewasused
andheatexchange,theseinternalheatdemandscanbereduced to evaluate the performance of the Chalmers 2−4-MW
by preheating the ingoing mass flows to the system. For gasifier. The evaluation methodology was implemented t t o h
example, Figure 15 shows that preheating the combustion air investigate how changing the amount of fluidizing steam
influencestheconversionofwoodpelletsat830°Cusingsilica
sand as the bed material. The inert bed material and wood
pellets was used to avoid catalytic effects of the bed material
and to minimize the effect of each component, generating a
reference case. The experimentalevaluation is dividedintofive
levels (indicated in bold text below), each of which enables
further evaluation of the performance. Since the results was
generalizedbyrelatingtheyieldstomassorenergyunitsoffuel,
thefollowingconclusioncanbeconsideredvalidforlarge-scale
DFB gasifiers of similar design.
From measurements of the cold gas, H O, and tar
2
concentrations, it was concluded that increasing the level of
steam generates higher concentrations of H , CO , and H O,
2 2 2
while the concentrations of CO and tar decreased.
ApplicationoftheHe-tracingmethodisaneffectivemethod
for quantification of the total gas product yield and,
subsequently, the cold gas efficiency, which is obtained by
subtractingandanalyzingasmallslipstreamoftherawgas.The
cold gas yield and efficiency each increase with the level of
steam, with the highest cold gas efficiency of the Chalmers
Figure 15. Internal heat demand as a function of the temperature of gasifier being 61%. Furthermore, the injections of helium
the inletflows, relative to the process temperature, based on case C. provide information regarding the steam balance across the
gasifier,asitgivesameasureoftheamountofsteamfedtothe
gasifier from the particle seals. This investigation shows that
wouldbethemosteffectivemeasuretoreducetheinternalheat 75%−85% of the steam follows the direction of the bed
demand for case C. The internal heat demand for heating the material. Intotal, ∼5%ofthe steamformedinoradded tothe
fuel exhibits a step that corresponds to drying of the fuel. gasifierisusedforfuelconversion,andimprovingthisisavital
Indeed, even for an already rather dry fuel, such as wood task to increase the amount of chemical energy stored in the
pellets, predrying would give a significant reduction of the produced gas.
i■nternal heat demand. Through combustion of a slipstream of the raw gas, the
total carbonconversion wasquantified.Bycomparing thetotal
CONCLUSIONS
carbon conversion with the amount of carbon in the cold gas,
In the present work, evaluation of the performance of the amount of OC and the raw gas efficiency is quantified.
industrial-scaledualfluidizedbed(DFB)gasifiersisinvestigated Furthermore, the analysis ofthe tar usingSPA showed thattar
and discussed in relation to (i) a general evaluation procedure constitutes ∼35% of the total OC. This underlines the
mass
and (ii) the application of this methodology on the Chalmers importanceofquantifyingtheremainingundeterminedOCasa
2−4-MW gasifier to describe how changes in the level of supplement to the tar analysis when quantifying the raw gas
th
fluidization impact the DFB gasifiers. efficiency. The present investigation shows that the Chalmers
N dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels Article
gasifiercanbeoperatedwitharawgasefficiencyof74%.Thisis Liotta,C.L.;Mielenz,J.R.;Murphy,R.;Templer,R.;Tschaplinski,T.
comparable to efficiency values presented in the literature for The path forward for biofuels and biomaterials. Science 2006, 311
integrated DFB gasifiers in a plant for the production of (5760), 484−489.
second-generation biofuels, which show raw gas efficiencies of (4)Goḿ ez-Barea,A.;Leckner,B.Modelingofbiomassgasificationin
74%−77%. Thus, when using wood pellets as the fuel, the fluidized bed. Prog. Energy Combust. Sci. 2010,36 (4), 444−509.
requiredrawgasefficiencyofsuchaplantcanbereachedeven (5) Kaushal, P.; Tyagi, R. Steam assisted biomass gasificationan
overview. Can. J. Chem. Eng. 2011,90 (4), 1043−1058.
with very low char conversion.
(6)Göransson,K.;Söderlind,U.;He,J.;Zhang,W.Reviewofsyngas
In the present study, the devolatilization products were
production via biomass DFBGs. Renewable Sustainable Energy Rev.
investigatedinbench-scalepyrolysisexperiments.Thisenables 2011, 15(1), 482−492.
a description of the degree of conversion of the char and OC (7)Kern,S.;Pfeifer,C.;Hofbauer,H.Gasificationofwoodinadual
based on the devolatilization products. The results show that fluidized bed gasifier: Influence of fuel feeding on process perform-
thecharconversionratewas0%−4%andthatupto36%ofthe ance. Chem. Eng. Sci. 2013,90, 284−298.
OCwasconvertedintheinvestigatedcases.Theconversionof (8) Neves, D.; Thunman, H.; Matos, A.; Tarelho, L.; Gomez-Barea,
OCyieldsincreasesinthelevelsofH ,CO ,andCH ,whereas A.Characterizationandpredictionofbiomasspyrolysisproducts.Prog.
2 2 4
the level of H O decreases, which suggests that the combined Energy Combust. Sci. 2011,37 (5), 611−630.
2
gas-phase reactions are, in totality, endothermic. (9) Linstrom, P. J., Mallard, W. G., Eds. NIST Chemistry WebBook,
As the fuel conversion is described, a heat balance for the URL: http://webbook.nist.gov/chemistry/.
(10)Gassner,M.;Mareć hal,F.Thermo-economicprocessmodelfor
processcanbeestablished.Itwasconcludedthattoincreasethe
raw gas efficiency through enhanced char conversion, first the thermochemical production of Synthetic Natural Gas (SNG) from
internalheatdemandshouldbedecreased. Effectiveoptionsto
lignocellulosicbiomass.BiomassBioenergy2009,33(11),1587−1604.
(11) Tock, L.; Gassner, M.; Mareć hal, F. Thermochemical
decrease the internal heat demand are to preheat the steam,
productionofliquidfuelsfrombiomass:Thermo-economicmodeling,
fuel, and combustion air and decrease the amount of steam.
process design and process integration analysis. Biomass Bioenergy
However, this involves a tradeoff, since decreasing the amount 2010, 34(12), 1838−1854.
ofsteamdecreasestheconversionofOC.Iftherawgasistobe (12) Heyne, S.; Harvey, S. Assessment of the energy and economic
used for combustion or if efficient secondary measures to performanceofsecondgenerationbiofuelproductionprocessesusing
converttheOCareavailable,thelevelofsteamshouldbekept energy market scenarios. Appl. Energy 2013,101 (0), 203−212.
aslowaspossible,toreducetheheatdemand.Alternatively,ifa (13) Hofbauer, H.; Rauch, R. Stoichiometric water consumption of
scrubber isused toremovethe OC,the cold gasefficiencycan steam gasification by the FICFB-gasification process. Prog. Thermo-
■be increased by increasing the amount of steam. chem. Biomass Convers.2001, 1,199−208.
(14)Corella,J.;Toledo,J.M.;Molina,G.Areviewondualfluidized-
ASSOCIATED CONTENT bedbiomassgasifiers.Ind.Eng.Chem.Res.2007,46(21),6831−6839.
* S Supporting Information (15)Corella,J.;Toledo,J.M.;Molina,G.Biomassgasificationwith
puresteaminfluidisedbed:12variablesthataffecttheeffectivenessof
A detailed description of the gas cleaning system, yield of tar the biomass gasifier. Int. J. Oil, Gas Coal Technol. 2008, 1 (1), 194−
components and a table, which summarizes the input data
207.
applied for the heat balance calculations. This material is (16) Guizani,C.;EscuderoSanz,F.J.;Salvador, S.,Thegasification
■available free of charge via the Internet at http://pubs.acs.org. reactivityofhigh-heating-ratecharsinsingleandmixedatmospheresof
HOand CO.Fuel 2013,108, 812−823.
2 2
AUTHOR INFORMATION (17) Palconok, G. I. Heat and mass transfer to a single particle in
Corresponding Author fluidized bed. Doctoral Thesis, Chalmers University of Technology,
*Tel.:+46317721496. Fax: +46317721152. E-mail: anton. Göteborg, Sweden, 1998.
(18)DiBlasi,C.Combustionandgasificationratesoflignocellulosic
larsson@chalmers.se.
chars. Prog. Energy Combust. Sci. 2009,35 (2), 121−140.
Notes (19)O ̈ hman,M.;Nordin,A.;Skrifvars,B.J.;Backman,R.;Hupa,M.
T■he authors declare no competing financial interest. Bedagglomeration characteristics duringfluidized bedcombustionof
biomass fuels. Energy Fuels 2000,14 (1), 169−178.
ACKNOWLEDGMENTS (20)Milne,T.A.;Abatzoglou,N.;Evans,R.J.Biomassgasifier“tars”:
This work has been support by Akademiska Hus, Göteborg Their nature, formation, and conversion. Technical Report NREL/TP-
570-25357, National Renewable Energy Laboratory: Golden, CO,
EnergiAB, MetsoPower AB,the Swedish EnergyAgency, and
the Swedish Gasification Center. We thank Claes Breitholtz 1998.
(21) Einstein, A. Investigations on the Theory of the Brownian
(Metso Power AB, Sweden) for his contribution while
Movement; DoverPublications: New York, 1956.
establishing and running the experimental setup. The authors
(22)Edvardsson,E.InvestigationofSolidsDistributionandExternal
would also like to acknowledge research engineers Jessica
̈ Solids Flux in a Circulating Fluidized Bed Boiler. Licentiate thesis,
Bohwalli,RustanMarberg,andJohannesOhlinforhelpingwith Chalmers University of Technology, Göteborg, Sweden, 2006.
■the experimental equipment. (23) Johnsson, F.; Leckner, B. Vertical distribution of solids in a
CFB-furnace. In The 13th International Conference on Fluidized Bed
REFERENCES Combustion. Part 1 (of 2), Orlando, FL, USA, May 7−10, 1995; pp
(1) Pröll, T.; Aichernig, C.; Rauch, R.; Hofbauer, H. Fluidized bed 671−679.
steamgasificationofsolidbiomassPerformancecharacteristicsofan (24)Löffler,G.;Kaiser,S.;Bosch,K.;Hofbauer,H.Hydrodynamics
8 MW combined heat and power plant. Int. J. Chem. Reactor Eng. of adualfluidized-bedgasifierPartI: Simulationof ariserwith gas
th
2007,5. injection and diffuser. Chem. Eng.Sci. 2003, 58(18), 4197−4213.
(2) Gunnarsson, I. In The GoBiGas Project; Göteborg Energi, (25)Liu,D.;Xiao,S.;Chen,X.;Bu,C.Investigationofsolidmixing
Göteborg, Sweden, 2011. mechanisms in a bubbling fluidized bed using a DEMCFD
(3) Ragauskas, A. J.; Williams, C. K.; Davison, B. H.; Britovsek, G.; approach. Asia-Pac. J. Chem. Eng. 2012, 7 (Suppl. S2), S237−S244
Cairney,J.;Eckert,C.A.;Frederick,W.J.,Jr;Hallett,J.P.;Leak,D.J.; (DOI: 10.1002/apj.553).
O dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX

Energy & Fuels ■ Article
(26)Olsson,J.;Pallares̀,D.;Johnsson,F.Lateralfueldispersionina NOTE ADDED AFTER ASAP PUBLICATION
large-scalebubblingfluidizedbed.Chem.Eng.Sci.2012,74,148−159.
ThispaperwaspublishedontheWebonSeptember 23,2013.
(27)Pallares,D.;Diez,P.;Johnsson,F.Experimentalanalysisoffuel
Anadditionalcoauthorandreferencewereaddedtothepaper,
mixing patterns in a fluidized bed. In Proceedings of the 12th
and the corrected version was reposted on October 10, 2013.
International Conference on Fluidization; 2007.
(28)Kunii,D.;Levenspiel,O.FluidizationEngineering;Butterworth−
Heinemann: Boston, 1991; Vol. 2.
(29) Reimert, R.; Marschner, F.; Renner, H.-J.; Boll, W.; Supp, E.;
Brejc, M.; Liebner, W.; Schaub, G. Gas Production, 2. Processes. In
Ullmann’s Encyclopedia of Industrial Chemistry; Wiley−VCH Verlag
GmbH &Co. KGaA: Weinheim, Germany, 2000.
(30) Basu, P. Biomass gasification and pyrolysis: Practical design and
theory;Academic Press: New York,2010.
(31) Simell, P.; Stah̊ lberg, P.; Kurkela, E.; Albrecht, J.; Deutsch, S.;
Sjöström,K.Provisionalprotocolforthesamplingandanlaysisoftar
and particulates in the gas from large-scale biomass gasifiers. Version
1998. Biomass Bioenergy 2000,18 (1), 19−38.
(32) Brage, C.; Yu, Q.; Chen, G.; Sjöström, K.Use of amino phase
adsorbentforbiomasstarsamplingandseparation.Fuel1997,76(2),
137−142.
(33)Kirnbauer,F.;Wilk,V.;Hofbauer,H.Performanceimprovement
ofdualfluidizedbedgasifiersbytemperaturereduction:Thebehavior
of tar species in the product gas. Fuel2013, 108,534−542.
(34) van der Meijden, C. M. Development of the MILENA
gasification technology for the production of Bio-SNG. Thesis, TU
Eindhoven, Eindhoven, TheNetherlands, 2010.
(35) Neves, D.; Thunman, H.; Tarelho, L.; Larsson, A.; Seemann,
M.; Matos, A. Method for online measurement of the CHON
compositionofrawgasfrombiomassgasifier.Appl.Energy, accepted
for publication.
(36) Thunman, H.; Åmand, L.-E.; Leckner, B.; Johnsson, F. A cost
effective concept for generation of heat, electricity and transport fuel
from biomass in fluidized bed boilersUsing existing energy
infrastructure. In Proceedings of the 15th European Biomass Conference
&ExhibitionFromResearchtoMarketDeployment,Berlin,Germany,
May7−11, 2007; pp10751080.
(37) Seemann, M.; Thunman, H. The new Chalmers research-
gasifier. In The 20th International Conference on Fluidized Bed
Combustion,2009; pp659−663.
(38) Leckner, B.; Golriz, M. R.; Zhang, W.; Andersson, B. A.;
Johnsson,F.Boundarylayers-firstmeasurements inthe12MWCFB
research plant at Chalmers University. In The 11th International
Conference on Fluidized BedCombustion, 1991; pp771−776.
(39)Hofbauer,H.InScaleupoffluidizedbedgasifiersfromlaboratory
scale to commercial plants: Steam gasification of solid biomass in a dual
fluidized bedsystem,2006; pp21−24.
(40) Kaufman Rechulski, M.; Schneebeli, J.;Geiger, S.;Schildhauer,
T.; Biollaz, S.; Ludwig, C. Liquid-Quench Sampling System for the
AnalysisofGasStreamsfromBiomassGasificationProcesses, Part1:
Sampling Noncondensable Compounds. Energy Fuels 2012, 26 (12),
7308−7315.
(41) Israelsson, M.; Seemann, M.; Thunman, H. Assessment of the
SPA method for sampling of biomass derived tar in industrial
environment. Submitted to Energy Fuels,2013.
(42) Neves, D.; Matos, A.; Tarelho, L.; Thunman, H.; Larsson, A.;
Seemann,M.,Dependenceofcharyieldontheelementalcomposition
of biomass. Biomass Bioenergy, underreview, 2013.
(43) Neves, D.; Matos, A.; Tarelho, L.; Thunman, H.; Larsson, A.;
Seemann, M. Volatile gases from biomass pyrolysis under conditions
relevant for fluidized bed gasification. Submitted to Fuels,2013.
(44) Pfeifer, C.; Koppatz, S.; Hofbauer, H. Steam gasification of
variousfeedstocksatadualfluidisedbedgasifier:Impactsofoperation
conditionsandbedmaterials.BiomassConvers.Biorefinery2011,1(1),
39−53.
(45) Passen, S. V. B. “Thersites”: website for tar dew point
calculations. www.thersites.nl
P dx.doi.org/10.1021/ef400981j|EnergyFuelsXXXX,XXX,XXX−XXX
