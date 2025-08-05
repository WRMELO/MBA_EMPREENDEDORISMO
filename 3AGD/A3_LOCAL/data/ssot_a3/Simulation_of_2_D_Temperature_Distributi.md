# Simulation_of_2_D_Temperature_Distributi

**Fonte**: Simulation_of_2_D_Temperature_Distributi.pdf  
**Data de conversão**: 2025-07-30 15:10:23  
**Origem**: base_relevantes

---

782 Ind.Eng.Chem.Res.1998,37,782-792
Simulation of 2-D Temperature Distributions in Fluidized Bed
Reactors for Highly Exothermic Reactions
Stefan Artlich, Ernst-Ulrich Hartge, and Joachim Werther*
TechnicalUniversityHamburg-Harburg,D20171Hamburg,Germany
Fluidized bed reactors are generally known for their temperature uniformity, but with highly
exothermicreactions,significanttemperaturegradientsmayoccur. Thegenerationoftemper-
ature distributions inside the fluidized bed is the result of a competition between two
mechanisms: local feeding of reactants creates heat of reaction locally, and this heat must be
dispersedinsidethebedbysolidsmixing. Thepresentworkinvestigatesthesemechanismsfor
the case of coal combustion in pressurized bubbling fluidized beds. With a simple one-
dimensionalcarbonmassbalance,thegoverningparametersforthegenerationoftemperature
profiles are deduced. For the quantitative calculation of temperature, carbon and oxygen
distributions,atwo-dimensionalmodelwasformulated. Inpressurizedfluidizedbeds,thefuel
is often fed as a coal-water slurry, so the drying of the fuel also has been considered in this
model. The model has been validated with measurements made in the pressurized fluidized
bed combustor (PFBC) pilot-scale test unit of Deutsche Babcock. The results are in good
agreementwithmeasurementsforfull-loadaswellaspart-loadconditions. Feedingthecoalas
a slurry is shown to be a means to flatten the temperature distribution because the slurry
agglomeratesaredispersedinthefluidizedbedwhiledrying. Furthersimulationresultspoint
at and quantify critical parameters that have to be considered in the scaleup of pressurized
fluidized bed combustors.
1. Introduction
Oneofthemainadvantagesoffluidizedbedreactors
for gas/solid reactions or heterogeneous catalytic reac-
tionsistheirwell-knowntemperaturehomogeneity(e.g.,
Kunii and Levenspiel, 1991). The reason for this
homogeneoustemperaturedistributionthroughoutthe
fluidized bed is the very intense solids mixing and the
good heat transfer between gas and solids. However,
for highly exothermic reactions, the heat transport by
the solids may not always be sufficient to avoid the
formation of temperature gradients or even hot spots
insidethebed;areasonforthiscouldbethehighrate
ofheatreleaseifthereactantisintroducedlocallyinto
thefluidizedbed. Furthermore,insuchreactors,densely
packed heat exchanger tube bundles that are needed
towithdrawtheheatfromthereactormayhindersolids
mixingandtherebyreducetheheattransportacrossthe
reactor. In small-scale fluidized beds the absolute
temperature difference may even be tolerable under
theseconditions. However,temperaturedifferenceswill Figure 1. Pressurized fluidized bed combustion test rig of
become significant in fluidized beds with large bed DeutscheBabcock(HGF)hotgasfilter;Dehnetal.(1991)).
heightsand/ordiametersandmaycausesevereopera-
tional problems. An example of such a fluidized bed area. Tomakesufficientheatexchangersurfaceavail-
reactor where a highly exothermic reaction is carried ablethePFBCisnormallyoperatedwithabedheight
out in a large bed that is densely packed with heat- of ≈4 m. The coal is fed into the lower part of the
exchanger tubes is the pressurized fluidized bed com- fluidizedbed,whichisfreefromheatexchangertubes.
bustor (PFBC). Two different systems are in use for fuel feeding.
In a PFBC (Figure 1), coal is burned in a bubbling Alternatively,eitherpredriedcoalisfedpneumatically
fluidized bed operated at pressures of up to 1.6 MPa. orcoal-waterpasteispumpedintothebed. Thelatter
Compared with atmospheric bubbling fluidized bed systemispreferredforcoalswithhighcalorificvalues.
combustors,theheatreleasepercross-sectionalareais Duetothehighlocalheatrelease,thehinderedsolids
increasedroughlyproportionaltotheoperatingpressure mixingandthelargebedheighttemperaturedifferences
andcanthusreachvaluesofupto17MW th perm2bed across the fluidized bed may be expected and have
indeedbeenexperienced: insidedifferenttestfacilities,
*Corresponding author. Telephone: +49-40-7718 3039. temperature differences have been measured of up to
Fax: +49-40-77182678.E-mail: werther@tu-harburg.d400.de. 170 K between the coal feed point and the top of the
S0888-5885(97)00523-XCCC:$15.00 ©1998AmericanChemicalSociety
PublishedonWeb01/17/1998

Ind.Eng.Chem.Res.,Vol.37,No.3,1998 783
4-mhighfluidizedbedaswellasof70Koverthewidth dx ofthereactor,M isthemolecularweightofcarbon,
v C
of a bed with a 2 × 2 m cross-sectional area (Smith et k is the reaction rate constant, C is the oxygen
C O2
al., 1982). This macro-scale nonisothermicity must be concentration, and C is the carbon concentration.
C
distinguished from the micro-scale nonisothermicity 2.1. A One-Dimensional Model. The generation
that is present in any fluidized bed coal combustor oftemperaturedistributionsinsidethefluidizedbedis
because the temperature of the burning coal particles the result of a competition of two mechanisms: local
is typically 50 to 100 K above the temperature of the reaction creates heat and this heat must be dispersed
surrounding ash particles (e.g., Basu, 1977). inside the bed by solids mixing. If the local heat
There are several models of PFBCs available in the generation exceeds the amount that can be dispersed
literature;mostofthem,however,areone-dimensional bysolidsmixing,atemperaturegradientwillbuildup.
models. Inmostcases,modelsofatmosphericfluidized A simple one-dimensional model may illustrate the
bedcombustorshavebeenextendedtohigherpressure. governingparameters. Weconsideravolumeelement
For example, Miccio (1991) extended the IEA atmo- in the fluidized bed. Inside this element, carbon is
spheric fluidized bed model towards higher operating consumed by reaction. Across its boundaries, carbon
pressures. His model, like most other models for is transported into the x-direction. With the assump-
atmospheric fluidized bed combustors, neglects the tions just described, the carbon balance for this one-
existenceoftemperaturegradientsbysimplyassuming dimensional model is given by:
isothermicityforthewholebed. One-dimensionalmod-
els that include the competition of heat generation by δ2C
reactionandheatdispersionbysolidsmixinghavebeen 0)D C -M k C C (3)
presented,forexample,byRavenandSparham(1983) x δx2 C C C O 2
and by Werther et al. (1989). Groenewald (1990) ex-
tended the latter model to two dimensions, and Itami where D is the coefficient of dispersion into the x-
x
et al. (1995) presented a generalization to the three- direction.
dimensionalcase. However,inthelattertwoinvestiga- IntroducingacharacteristiclengthLinthedirection
tions, just the dry feed of coal has been considered. ofcarbonspreading(e.g.,thespacingbetweenneighbor-
WhereasItamietal.(1995)presentqualitativeresults ingcoalfeedpoints),withx′)x/Landanondimensional
only, Groenewald (1990) reports severe numerical dif- carbon concentration C′ ) C /C eq 3 can be rewrit-
C C C,0
ficultiesinthesolutionofhispartialdifferentialequa- ten as follows:
tions.
D δ2C′
2. Theory x C -C′ )0 (4)
L2M k C δx′2 C
To model the temperature inside the fluidized bed C C O 2
reactor, the heat release by the reaction and the heat
transport inside the bed have to be considered. Heat Replacingtheeffectivereactionrateconstantk C bythe
transportmaybedescribedbyadispersionprocess,with surface reaction rate constant k O (e.g., Avedesian and
theunderlyingideabeingthatheatisprimarilytrans- Davidson, 1973),
portedbythemotionofsolidsthatcanbedescribedby ( )
a dispersion model. The fuel transport inside the bed 6 1 d p,fuel -1
may be treated as a dispersion process, too. k C ) d F w k (T,T ) + ShD (5)
In the present fluidized bed model, the gas and the p,fuel fuel C,fuel O p G
solidsphasesaretreatedseparately. Nodistinctionwas
made between bubble and emulsion phases. This ap- yields
proachseemstobejustifiedbecauseintheunderlying
system of coarse bed particles, the mass transfer δ2C′
C
between bubbles and suspension phase is very fast. -
Furtherbasicassumptionsarethatthegasflowsasplug
δx′2
flow, that the temperature of gas is equal to the L2M C
temperatureofthesolidsateachlocation,andthatfuel C O 2 ( 6 )C′ )0
is transported by dispersion only. The model is cur- D x 1 d p,fuel C
d F w +
rently restricted to vertical walls of the combustion p,fuel fuel C,fuel k (T,T ) ShD
O p G
chamber.
(6)
Forthesakeofsimplicitytheoverallcarbonoxidation
reaction C + O f CO has been taken into account
2 2 The carbon balance eq 6 means that a steep carbon
only;thatis,devolatilizationprocessesaswellascarbon
concentration profile in the x-direction will occur if it
monoxide formation and oxidation were neglected. A
holds for the following dimensionless quantity:
simple first-order rate expression was used for the
carbon consumption:
L2M C
dm C O 2 ( 6 ).1 (7)
C )-M k m C (1) D x 1 d p,fuel
dt C C C O 2 d p,fuel F fuel w C,fuel k (T,T ) + ShD
O p G
where
Because the carbon concentration profile C′(x′) is di-
C
m )A dx C (2) rectly related to the temperature profile T(x′), the
C t v C
criterion of eq 7 means that a significant temperature
and m is the carbon mass in the volume element A profile may occur if the following conditions are met:
C t

784 Ind.Eng.Chem.Res.,Vol.37,No.3,1998
as:
δ δ
0)- H˙ (x ,x )∆x - H˙ (x ,x )∆x -
δx C,h h v h δx C,v h v v
h v
δ δ
H˙ (x ,x )∆x - H˙ (x ,x )∆x -
δx BM,h h v h δx BM,v h v v
h v
δ
H˙ (x ,x )∆x +Q˙ (x ,x )+Q˙ (x ,x )+
δx RG,v h v h R h v TB h v
v
Q˙ (x ,x ) (10)
E h v
Figure2. Enthalpybalanceonadifferentialvolumeelementof The heat transport by carbon dispersion is given by:
thefluidizedbedreactor.
δC
(1) D is small (i.e., if solids mixing is, for example, H˙ )-∆x Z(1-ǫ)cj D C (x ,x )(T(x ,x )-T )
x C,h v p,C h δx h v h v B
hinderedbyadensepackingofheat-exchangertubes). h (11)
(2)Lislarge(e.g.,ifthedistancebetweenneighboring
coalfeedpointsistoolargeorifthebedheightislarge). δC
H˙ )-∆x Z(1-ǫ)cj D C (x ,x )(T(x ,x )-T )
(3)d issmall(i.e.,finecoalsmaysimplyburntoo C,v h p,C v δx h v h v B
p,fuel v
fast before they are dispersed in the bulk of the bed). (12)
(4)k islarge(i.e.,highlyreactivecoalsthatarefed
O
TheconstantZisthedepthofthefluidizedbed(inthe
as fine particles may be critical).
directionperpendiculartothex ,x plane),Tisthelocal
(5)C islarge(i.e.,thesteepestprofileswilloccurin h v
O2 temperature,cj isthespecificheatofcarbon,andT
the lower part of the combustor); a reduction of the p,C B
is a reference temperature (T ) 25 °C).
steepness of the temperature profile may in this case B
Theheattransportbydispersionofthebedmaterial
be achieved by, for example, flue gas recirculation.
can be expressed as:
Because C is much larger in a PFBC than in atmo-
O2
spheric fluidized bed combustors, the risk of steep
δT
temperatureprofilesismuchhigherintheformercase. H˙ (x ,x ))-∆x Zλ (x ,x ) (13)
BM,h h v v hδx h v
2.2. The Two-Dimensional Model. Whereas the h
one-dimensional model, eq 3, has been formulated to
δT
illustratethemechanismsinvolvedintheformationof H˙ (x ,x ))-∆x Zλ (x ,x ) (14)
BM,v h v h vδx h v
temperature profiles, the following two-dimensional v
modelhasbeendevelopedforquantitativecalculations.
The model consists of mass balances for carbon and with the effective thermal conductivity of the bed as:
oxygen,respectively,andanenthalpybalance. Thetwo-
dimensional mass balance for carbon reads: λ h )(1-ǫ)F BM cj p,BM D h (15)
λ )(1-ǫ)F cj D (16)
δ2C δ2C v BM p,BM v
C C
0)D +D -M k (T)C C +F˘ (8)
h δx 2 v δx 2 C C C O 2 C,F The fluidizing gas transports heat according to:
h v
H˙ (x ,x ))u∆x ZF cj (T(x ,x )-T ) (17)
The first term describes the solids mixing in the RG,v h v h RG p,RG h v B
horizontal, and the second one describes the solids
mixingintheverticaldirection. Thecarbonconsump- The heat generation by reaction is given by:
tion by reaction is given in the third term, and F˘
C,F
describes a local carbon feed rate. Q˙ (x ,x ))∆x ∆x Z(1-ǫ)M k (T)C C (H /w )
R h v h v C C C O u C,fuel
2
The oxygen balance is much simpler because of the
(18)
assumption of plug flow of the gas (i.e., without hori-
zontalorverticalmixing). Thebalanceconsists,there-
The heat extraction by the tube bundle is given by:
fore,ofaverticalconvectiontermandatermdescribing
theoxygenconsumptionbythecombustionprocessonly:
A
Q˙ (x ,x ))-∆x ∆x Z TB ê(x )k (T-T ) (19)
δC O TB h v h v BH TB Z v TB KM
0)u 2+(1-ǫ)k (T)C C (9)
δx v C C O 2 whereA TB istotalsurfaceareaofthetubebundle,Bis
the width of the fluidized bed,H is the height of the
TB
Theenthalpybalanceismorecomplex(cf.Figure2). tubebundle,k TB istheheattransfercoeficient,andT KM
Ittakesaccountoftheheattransportbyhorizontaland is the temperature of the fluid inside the tubes. As is
vertical dispersion of bed material (index BM) and illustratedinFigure3,thefunctionê(x v )describesthe
carbon,theheattransportbytheupflowinggas(index presence of the tube bundle; that is, ê(x v ) ) 1 for
RG), the heat generation by the reaction, Q˙ R , the heat positionswithtubesandê(x v ))0forpositionswithout
extraction by the tube bundle, Q˙ , and an additional tubes. Finally, the additional heat sink is given by:
TB
heat sink, Q˙ , which will be explained in detail later.
From Figure E 2, the enthalpy balance can be deduced Q˙ E (x h ,x v ))-∆x v ∆x h Zq˘ E (x h ,x v ) (20)

Ind.Eng.Chem.Res.,Vol.37,No.3,1998 785
At the bed surface it holds that:
δT|
λ )0 (26)
v δnΓ
3
because the gas is leaving the bed with a temperature
that is equal to the temperature of the bed at Γ .
3
Because the walls along Γ , Γ , and Γ are cooled
2 4 6
membrane walls, the heat transported horizontally to
the wall has to be equal to the heat extracted through
the wall:
δT|
λ )-k (T-T )| (27)
Figure3. Sketchofthereactorgeometryanddefinitionofthe h δnΓ 2 ,Γ 4 ,Γ 6 w KM Γ 2 ,Γ 4 ,Γ 6
boundariesΓ 1-Γ 6.ThedimensionsarethoseofDeutscheBabcock’s
pilotPFBC. Thelastborderforwhichaboundaryconditionisneeded
isthefeedpoint. Hereanenthalpyflowisenteringthe
Combiningeqs10to20resultsinthefinalformofthe
fluidized bed with the coal. This enthalpy flow has to
enthalpy balance:
bebalancedbytheheattransportduetothedispersion
( ( )
of solids and of carbon:
0)(1-ǫ)cj D δ δC C (T-T ) +
(
p,C hδx
h
δx
)h)
B δT|
λ )
δ δC C δ2T δ2T h δnΓ
D (T-T ) +λ +λ - 5
vδx v δx v B h δx h 2 v δx v 2 m˘ fuel cj p,fuel (T fuel -T B )-m˘ fuel w fuel cj p,C (T-T B )|Γ 5 (28)
uF cj δT +(1-ǫ)M k (T)C C 1 H - H FE Z
RG p,RGδx
v
C C C O 2w
C,fuel
u
A
TB 2.3. The Submodel for Slurry Feeding. In the
ê(x )k (T-T )-q˘ (21)
BH Z v TB KM E case of slurry feeding, the coal has to dry prior to its
TB
ignition. During this drying process, the wet fuel will
Theboundaryconditionsthatareneededtosolvethe already be dispersed in the system. To take this
systemofdifferentialeqs8,9,and21maybeexplained premixing into account, a submodel for the dispersion
with the help of Figure 3, where the boundaries are duringcoaldryingissuggested. Thissubmodelisbased
designatedbyΓ 1 toΓ 6 aroundthecircumferenceofthe on the assumption of a known fixed drying time t dr . It
reactor. Theboundaryconditionsforthecarbonbalance isfurthermoreassumedthatthemassflowofdriedand
are as follows: At the feed point (Γ ), the dispersive heated carbon that leaves each local element for com-
5
transport of carbon in the horizontal direction has to bustionisproportionaltothelocalcarbonconcentration.
be equal to the carbon feed flux: Theresultinglocalmassbalanceforthedryingcarbon
can be written as:
δC | m˘ w
C fuel C,fuel
D h δn Γ 5 )- (1-ǫ)H FE Z (22) 0)D δ2C C,dr +D δ2C C,dr - 1 C (x ,x ) (29)
where n denotes the normal to the boundary that is h δx h 2 v δx v 2 t dr C,dr h v
positive when orientated into the reactor. There is no
where C is the local mass concentration of wet
carbon flow through any of the other boarders: C,dr
carbon.
δC | Thissubmodelisindependentlysolvedbeforesolving
C
D )0 thecombustionmodel. Themodelsarelinkedtogether
h δn Γ,Γ,Γ
2 4 6 bythelocalcarbonflowthatisleavingthedryingmodel
δC | (i.e., the sink term in eq 29) and is entering as a local
D C )0 (23) carbon feed flow:
v δn Γ,Γ
1 3
1
The entry condition for the oxygen is given by: F˘ C,F ) t C C,dr (x h ,x v ) (30)
dr
0.21
C ) F (24)
O 2 ,0 M L L i b n y to th th e e l c o o c m al b h u e s a ti t on flu m x od n e e l e . d A ed no f t o h r er ev li a n p k o i r s a e ti s o t n ab i l n ish th ed e
drying model, which is treated as the additional heat
The enthalpy flow entering the fluidized bed through
sinkq˘ ineq21ofthecombustionmodel. Theheatflow
thegasdistributor(i.e.,theenthalpyflowoftheincom- E
rate q˘ leaving the combustion model is equal to the
ingair)hastobebalancedbytheheattransportinside E
evaporationenthalpyfluxh˙ oftheevaporatedwater
the bed, which gives: H2O
in the drying model:
δT|
λ )-uF (cj T| -cj T ) (25)
v δnΓ RG p,RG Γ 1 p,L L q˘ E (x h ,x v ))h˙ HO (x h ,x v ) (31)
1 2

786 Ind.Eng.Chem.Res.,Vol.37,No.3,1998
Thelocalevaporationenthalpyfluxh˙ isproportional
H2O
to the absolute value of the gradient of the dispersive
mass fluxes of the drying coal:
h˙ (x ,x )∝
HO h v
2 ( ) ( )
x δC 2 δC 2
C,dr C,dr
D (x ,x ) + D (x ,x ) (32)
h δx h v v δx h v
h v
The total evaporation enthalpy flux required in the
reactorforheatingandevaporationofthewateristhe
integral of the local enthalpy fluxes over the reactor
volumeandisequaltotheenthalpyfluxneededtoheat
andevaporatethewaterm˘ containedinthecoalfeed:
H2O
∫H∫B
h˙ )Z h˙ (x ,x )dx dx
H 2 O,total 0 0 H 2 O h v h v Figure4. Verticalsolidsmixingincoldmodelfluidizedbedsfilled
withbundlesofhorizontaltubes(afterGroenewald(1990)).
)(c (T -T )+r+
p,HO S fuel
2
c (T-T ))w m˘ (33)
p,V S HO,fuel fuel
2
Combiningeqs32and33givesthelocalenthalpyflux:
h˙ (x ,x ))
H2O h v
( ) ( )
x δC 2 δC 2
D C,dr(x ,x ) + D C,dr(x ,x )
h δx h v v δx h v
( h ) ( v ) ×
Z
∫B∫Hx
D
δC
C,dr(y ,y )
2
+ D
δC
C,dr(y ,y )
2
dy dy
0 0 h δx h h v v δx v h v h v
h˙ (34)
H2O,total
3. Results and Discussion
For the numerical simulation, the finite element
method on a triangular mesh has been used. There
have been tests with piecewise linear and quadratic
basisfunctionsthatonlydifferintheconvergencerate.
The results that are presented in the following have
beencomputedonameshwith8385unknownsforeach Figure5. Temperatureprofilecalculatedwithoutconsideration
ofslurrydrying.
ofthemodelcomponentsC andT. ThenecessaryCPU
C
time for the entire model has been ∼13 min on a
The horizontal solids dispersion coefficient D was
HP9000/735 workstation with a 40 Mflops PA-RISC h
calculatedfromthecorrelationbyWertheretal.(1987),
processor.
whichrelatesD tolocalbubblesizesinabedfilledwith
In the simulations, the dimensions of the 15 MW h
th horizontal tubes.
pilotscalePFBCtestfacilityoperatedbytheDeutsche
TheverticalsolidsdispersioncoefficientD wastaken
Babcock at their Friedrichsfeld site (cf., Dehn et al., v
fromacorrelationinGroenewald’s(1990)dissertation.
1991)hasbeenused. Thecombustorhadabedheight
Because this reference is not easily accessible, the
of 4.2 m, and a cross-sectional area of 1.45 m2 at the
correlationisgivenhere. Foralargethree-dimensional
distributorlevelandof2.2m2atthebedsurface. This
bedwithabundleofhorizontaltubesitwasfoundthat:
pilot plant has been chosen because there exist tem-
perature profile measurements that could be used for
D )0.056(uj -u ) (36)
the validation of the present model. v mf
3.1. DeterminationofModelParameters. Model
whereD isinm2/s,anduj andu aretobeinsertedin
parametersofthedescribedmodelarethereactionrate v mf
m/s. Equation36hasbeenderivedfrommeasurements
constant,k,andthecoefficientsD andD ofdispersion
c h v withsublimingCO tracerparticlesinacold1:1model
in the horizontal and vertical directions, respectively. 2
ofDeutscheBabcock’spilot-scalePFBC. Themeasured
First of all, the reaction rate constant has been calcu-
results are presented in Figure 4. Because the PFBC
latedfromeq5usingthekineticssuggestedbyFieldet
wasequippedwithinclinedwalls,anaveragefluidizing
al. (1967):
velocity uj was defined for the average height between
( ) thedistributorlevelandthebedsurface. Alsoincluded
k )596 T+T p exp -149470 (35) in Figure 4 are measurements taken in another cold
0 2 RT model that was equipped with side-walls of variable
p
inclination. The measurements show that there is no
Aconstanttemperaturedifference(T-T )betweenthe significantinfluenceoftheinclinationofthewallsifthe
p
burningcarbonparticleandthebedof100Khasbeen measureddispersioncoefficientisrelatedtotheaverage
assumed. fluidizing velocity uj. The dispersion coefficients mea-

Ind.Eng.Chem.Res.,Vol.37,No.3,1998 787
Figure6. Influenceofthedryingtime(t dr)onthetemperatureprofiles.
Figure7. Drycarbonfeedflux(kgm-3s-1)andevaporationenthalpyfluxdistribution(kWm-3)foradryingtime(t dr)of60s.
sured in the latter cold model are lower than those ingmechanismsforadryingtimeof60s. Thelocalcoal
measuredinthePFBCcoldmodelbecauseathickness feedingsourceinthecaseofdrycoalfeedingisreplaced
ofthisbedof0.3mwhencomparedtothebedheightof by a field of dry feed sources that are spread all over
4 m results in a significant hindrance of bubble and thearea(orvolume)ofthecombustor,asillustratedin
solids motion in this nearly “two-dimensional” bed. theleft-handpartofFigure7wherethedrycarbonmass
3.2. ValidationoftheModel. Inafirstapproach, flux distribution is shown which represents the two-
the model was tested with the operating conditions of dimensional distribution of coal feed sources in the
the Babcock PFBC pilot plant without considering the combustor model. The corresponding evaporation en-
actual coal slurry feeding. The resulting two-dimen- thalpy flux distribution that is required in the drying
sional temperature distribution is shown in Figure 5. processisshownintheright-handpartofFigure7.The
Thetemperatureisseentoexceed930°Cinthevicinity highheatfluxrequiredfordryinginthevicinityofthe
of the coal feed port. The maximum temperature coal feed port helps to keep the temperature down in
difference inside the bed is >200 K. Because such this area.
temperaturedifferenceswereneverexperiencedinthe Figure 8 shows the two-dimensional concentration
PFBCpilotplantandbecausethesteepesttemperature distributions of carbon and oxygen for the 60-s drying
gradient is observed near the coal feed point, it must time. The carbon distribution reflects the fact that
be concluded that the smoothing effect of coal slurry verticalmixinginthefluidizedbedissignificantlybetter
drying has to be considered in the model. than horizontal solids mixing (Kunii and Levenspiel,
Theeffectofdryingthecoalslurryisclearlyseenin 1991). Oxygen,ontheotherhandisevenlydistributed
Figure 6 where temperature distributions are plotted atthedistributorlevelbutisconsumedveryfastinthe
fordryingtimes(t )of10,45,and100s. Theflattening vicinityofthecoalfeedpoint. Acharacteristicoxygen
dr
ofthetemperaturedistributionswithincreasingdrying concentration distribution results with a maximum
timeisobvious. Figures7and8illustratetheunderly- concentrationinthelowerright-handcornerontheside

788 Ind.Eng.Chem.Res.,Vol.37,No.3,1998
Figure8. Carbonandoxygendistributionsforadryingtime(t dr)of60s.
timesbetween150and700swereobservedforsludge
agglomerates with masses between 20 and 400 g.
Sewagesludgeisgenerallypumpedasapasteintothe
combustor with piston pumps as they are used for
concrete pumping. This procedure explains the pres-
ence of large agglomerates in the bed. Coal slurry
agglomerates will certainly be significantly smaller.
Theywillprobablyhavemassesoftheorderofseveral
grams depending on the nozzle design of the slurry
feedingarrangement. Nobetterinformationwasavail-
able,soallfurthercalculationswerecarriedoutwitha
drying time, t , of 60 s.
dr
The model was validated with measurements of
temperature distributions in Deutsche Babcock’s pilot
PFBC that were made during a 100% load run. Nu-
Figure9. Influenceofthedryingtimeonthecalculatedmaxi- merical values of the model parameters used for this
mumin-bedtemperaturedifference. calculationareH)4.1m;B)1.17m;Z)1.55m;H
TB
) 3.15 m; H ) 0.2 m; m˘ ) 0.57 kg/s; m˘ ) 5.69
FE fuel air
opposite to the feed point and a minimum level in the
kg/s; w ) 0.65; w ) 0.14; H of the coal )
upper left-hand corner above the coal feed port.
C,fuel H2O,fuel u
38400kJ/kg ,H ofthecoal-waterpaste)37300kJ/
C u
Figure 9 gives a summary of the influence of slurry kg ; d ) 0.758 mm; T ) 305.2 K; F ) 1,280
C p,fuel fuel fuel
dryingonthetemperaturedistributionbyplottingthe kg/m3;FΒΜ)2,600kg/m3,k
TB
)357W/m2K;k
W
)30
maximum in-bed temperature difference (T max - T min ) W/m2 K. The calculation was fitted to the measure-
against the drying time, t . With increasing drying
dr mentsbyvaryingthetwodispersioncoefficientsD and
h
time,thetemperaturedifferenceisseentoapproachan
D . AbestfitwasobtainedforD )0.011m2/sandD
v h v
asymptotical value that under the present operating
) 0.059 m2/s.
conditionsis∼25K. Thisfinitetemperaturedifference
Figure 10 shows the comparison between measure-
results in the model calculation from the fact that the
ments and calculation. The scatter of the measured
incoming air cools the bed at the distributor level and
temperatures is quite large, but it is understandable.
that heat is extracted by the tube bundle in the upper
partofthebedonly(cf.,Figure3). ForpracticalPFBC Thetemperatureshadtobemeasuredinsideadensely
operation, this small temperature difference is insig- packedtubebundlewherethedistancesbetweenneigh-
nificant. boring tubes were <50 mm. The small gaps between
the tubes inevitably led to inaccuracies in the temper-
Simpleheattransferanddryingcalculationsforthe
particleagglomeratesthatarereleasedatthecoalslurry aturemeasurementsbecausethecoldtubesweresimply
feed nozzle have shown that drying times of the order too close to the thermocouples. Heat conduction and/
of 1 min are not unreasonable. Direct measurements or radiation will in such a situation affect the thermo-
of drying times under PFBC conditions are not avail- couple readings. Another reason for the large scatter
able. However, Wirsum (1997) has recently reported isthatthethermocouplearraywasnotinstalledforan
results of an experimental investigation where he academic investigation but simply as a survey system
measuredthedryingtimesofsewagesludgeagglomer- for the overall combustor performance. In addition, it
atesinanatmosphericfluidizedbedcombustor. Drying hastobeadmittedthatthemodelisatwo-dimensional

Ind.Eng.Chem.Res.,Vol.37,No.3,1998 789
Figure10. Calculatedandmeasuredtemperaturedistributionsfora100%loadcase.
Figure11. Calculatedandmeasuredtemperaturedistributionsfora75%loadcase.
onethatiscomparedheretotheoperatingbehaviorof to the direction of dispersion. Following Pell (1990),
a three-dimensional unit. solidsmixingperpendiculartotheheatexchangertubes
Thebestfitvaluesofthedispersioncoefficientsmay tends to be poorer than in the direction parallel to the
nowbecomparedwiththepredictionsoftheempirical tubesbecausesolidscirculationisreducedbythebaffle
correlations (eq 36) and the correlation by Werther et effectofthetubes. Thecoefficientofdispersioninthe
al.(1987). Equation36yieldsforthepresentoperating direction parallel to the tubes will thus be higher.
conditionsanumericalvalueofD v )0.054m2/s,which Furthermore,thecoalslurryisfedintoasectionbelow
agrees quite well with the best fit value of 0.059 m2/s. the tube bundle, which is void of any internals. Thus
The correlation by Werther et al. (1987) for the coef-
intheregionwiththesteepestgradients,themixingis
ficient of horizontal dispersion yields a value D )
h notatallhinderedbytubes,whichagainincreasesthe
0.0043m2/siftheinfluenceoftheactualtubearrange-
overall horizontal dispersion coefficient.
mentisconsideredandD )0.011m2/siftheexistence
h Anothercomparisonofthemodelwithmeasurements
ofthetubesisneglectedandthebubblesarepermitted
is shown in Figure 11 for a 75% load case. Load
togrowwithoutbeingdisturbedbythepresenceofthe
tubes. The best fit value is D ) 0.011 m2/s, and this following is effected in a PFBC by varying the bed
v
value is in complete agreement with the empty-bed height. Foraloadof75%,thebedheightwasreduced
prediction. The physical reason for this at first sight to3m. Duetothelowerenergyinput,thetemperature
surprising result is that the underlying experiments distributionismuchflatterthaninthe100%loadcase.
leadingtothecorrelationbyWertheretal.(1987)were This calculation has been carried out with the same
carried out in a cold model fluidized bed where the numerical values of t dr , D h , and D v as the 100% case
horizontal tubes were arranged perpendicular to the (i.e.,nofittinghasbeendone).Thereisstillsomescatter
directionofdispersion,whereasinDeutscheBabcock’s in the differences between measured and calculated
pilot PFBC, the horizontal tubes were located parallel temperatures. However,theoverallagreementbetween

790 Ind.Eng.Chem.Res.,Vol.37,No.3,1998
Figure12. Scale-upsimulation: enlargementofthebedwidth.
simulationandexperimentseemstobeevenbetterthan
in the 100% load case.
3.3. ApplicationoftheModel. Ofprimaryinterest
toindustryisananswertothequestionhowfarasingle
fuel feed nozzle is able to disperse the fuel without
causingintolerablyhightemperaturedifferencesinside
thebed. Figure12showstheresultofsuchascale-up
calculation. Thedistributionsoftemperatureandoxy-
genareplottedhereforanenlargementofthebedwidth
fromthe1.17mofthepilotplanttoabedwidthof2m.
Thefuelfeedratehasbeenincreasedaccordingly. The
steepnessofthetemperaturedistributionhasincreased
considerably when compared with the standard 100%
load case depicted in Figure 10, and it is doubtful
whether such temperature differences are tolerable in
atechnicalPFBC. Anotherpointisthatthelargewidth
Figure13. Influenceofthebedwidthonthemaximumtemper-
ofthecombustorleadstoastronghorizontalprofileof
aturedifference
the oxygen concentration in the flue gas at the bed
surface. Above the fuel feed zone we find a region of
verylowoxygencontent,whichmeansinpracticehigh
concentrations of carbon monoxide in this region. On
theotherhand,onthesideoppositetothefuelfeedport,
thereisanexcessofoxygenthathasnotbeenusedfor
combustion. Suchanoxygendistributionisindicative
ofapoorperformanceofthecombustorwithrespectto
emissions.
In general, the model may be used to predict the
influence of the reactor width on the steepness of the
temperature distribution. As an example, Figure 13
shows its influence on the maximum temperature
difference (T - T ) inside the combustor bed.
max min
Calculations of this type may be helpful in the design
of large-scale PFBCs. The optimum width of the
combustion chamber may be chosen on the basis of
maximumtolerabletemperatures(e.g.,withrespectto
ash softening) and emission considerations. Figure14. Enlargementofthereactorwidthto4.0manduseof
As is shown in Figure 14 the model is also able to twofuelfeedpoints.
handle the situation of two coal feed ports that are
located on opposite sides of the combustor. Figure 14 the formation of temperature gradients inside the
showsthetemperaturedistributionforthecaseofa4-m fluidized-bedreactor. Temperaturegradientsgenerally
wide combustor. More information may be found in resultfromthecompetitionbetweenlocalheatgenera-
Artlich (1996). tioncausedbylocalreactantfeedingandheatdispersion
caused by solids mixing. A dimensionless group has
beenidentifiedthatfortheapplicationtocoalcombus-
4. Conclusions
tion reveals the parameters that are involved in this
A simple one-dimensional carbon balance has first process. These parameters are the mixing length, L,
beenusedtoillustratethebasicmechanismleadingto the reactivity of the coal (characterized by the surface

Ind.Eng.Chem.Res.,Vol.37,No.3,1998 791
reaction rate constant, k ), the coal feed particle size, k )heattransfercoefficienttothemembranewalls,W/m2
o W
and the local oxygen concentration. K
Thetwo-dimensionalmodelisintendedtobeusedfor L)characteristiclengthinthedirectionofcarbonspread-
quantitative calculations. It basically consists of two ing,m
mass balances for carbon and oxygen and an enthalpy M C )molecularweightofcarbon,kg/kmol
balance. Anewelementinthepresentmodelapproach M L )molecularweightofair,kg/kmol
is its consideration of the coal feeding process. In m C )carbonmassinthevolumeelementA t ‚dx v ,kg
PFBCsthecoalisoftenfedasaslurrythroughnozzles m˘ )fuelfeedflux,kg/s
thatintroducethecoalintheformofwetagglomerates m˘ L )massflowoffluidizingair,kg/s
into the combustor. Drying and heating of these ag- n)outernormaltotheboundary
glomeratesrequiresafinitetimeandduringthistime q˘ )specificevaporationheatflux,W/m3
E
theagglomeratesmaybedispersedinthebedwiththe r)specificheatofevaporationforwater,kJ/kg
result that the agglomerates are already far from the Sh)Sherwoodnumber
feed point when they ignite. This mechanism helps t)time,s
considerablytoreducethetemperaturegradients. The t )dryingtime,s
dr
calculations show that a quasi-homogeneous tempera- T)temperature,K
turedistributionmaybeachievedifonlythedryingtime T )referencetemperature(T )298K)
B B
ofthecoalslurryagglomeratesislongenough. Because T )temperatureofthefuelatthefeedpoint,K
fuel
the drying time is strongly related to the size of the T )temperatureofthefluidinsidetheheat-exchanger
KM
agglomerates, large agglomerates would be desirable. tubes,K
However, there may be practical considerations; for T )temperatureoftheairatthegasdistributor,K
L
example,theunknowninfluenceoftheagglomeratesize T )boilingtemperatureofwater,K
S
on the size distribution of the resulting ash and the u)superficialfluidizingvelocity,m/s
possible interference of larger agglomerates with the u )minimumfluidizingvelocity,m/s
mf
densely packed in-bed tube bundle, which may be w )carboncontentofthefuel,kg/kg
C,fuel
limiting for the agglomerate size. w )watercontentofthefuel,kg/kg
H2O,fuel
The model has been shown to be in fair agreement x )horizontalcoordinate,m
h
with measurements of temperature distributions in x )verticalcoordinate,m
v
DeutscheBabcock'spilot-scalePFBC. Themodelmay Z)depthofthefluidizedbed,m
thus be useful in industry to investigate the influence ǫ)porosityofthefluidizedbed
of different design parameters, particularly in the λ ) effective thermal conductivity of the bed in the
h
process of scale-up. The model is presently restricted horizontaldirection,definedbyeq15
totwo-dimensions. Ongoingwork,however,isdirected λ v )effectivethermalconductivityofthebedinthevertical
to extend it to three dimensions. direction,def.byeq16
F )densityofthebedmaterial,kg/m3
BM
Nomenclature F fuel )densityoffuel,kg/m3
F )densityofair,kg/m3
L
A t )crosssectionalareaofthefluidizedbed,m2 F RG )densityofthegas,kg/m3
A TB )totalsurfaceareaofthetubebundle,m2 F˘ F )localcarbonfeedflowbasedonunitbedvolume,kg/
B)widthofthefluidizedbed,m m3s
C )carbonconcentration,kg/m3
C
C′ ) nondimensional carbon concentration, C′ ) C /C
C C C C,0 Literature Cited
C )localmassconcentrationofwetcarbon,kg/m3
C,dr
C )oxygenconcentration,kmol/m3 Artlich, S. Zweidimensionale Simulation der Kohleverbrennung
O2
cj )specificheatofthebedmaterial,kJ/kgK in Druckwirbelschichtfeuerungen; VDI Verlag: Du¨sseldorf,
p,BM
cj )specificheatofcarbon,kJ/kgK Germany,1990;Reihe6,Nr.346.
p,C
cj )specificheatofcoal,kJ/kgK Avedesian,M.M.;Davidson,J.F.CombustionofCarbonParticles
p,fuel inaFluidisedBed.Trans.Inst.Chem.Eng.1973,51,121.
cj )specificheatofthefluidizinggas,kJ/kgK
p,RG Basu,P.BurningRateofCarboninFluidizedBeds.Fuel1977,
c )specificheatofwatervapour,kJ/kgK
p,V 56,390.
c )specificheatofwater,kJ/kgK
p,H2O Dehn, G.; Meier, H.; Mo¨llenhoff, H.; Rehwinkel, H.; von Wedel,
d p,fuel )particlesizeofthefeedfuel,m G. 15 MWth PFBC operating experience with the Deutsche
D G )coefficientofmoleculardiffusionofoxygeninair,m2/s Babcockpilotplantandoutlookonfuturedevelopment.InProc.
D ) coefficient of dispersion in the horizontal direction, 11thInt.Conf.FluidizedBedCombustion;Anthony,E.J.,Ed.;
h
m2/s ASME: NewYork,1991;p345.
D )coefficientofdispersionintheverticaldirection,m2/s Field, M. A.; Gill, D. W.; Morgan, B. B.; Hawskley, P. G. W.
v Combustionofpulverizedcoal.BritishCoalUtilisationResearch
D )coefficientofdispersioninthex-direction,m2/s
x Association: Leatherhead,England,1967.
H˙ )heatfluxbydispersionofthebedmaterial,kW
BM Groenewald,H.ZumEinflussvonWa¨rmetauscherbu¨ndelnaufdie
H˙ )heatfluxbycarbondispersion,kW
C Temperaturhomogenita¨tdruckaufgeladenerWirbelschichtfeuerun-
H FE )heightofthefeedelement,m gen;VDI-Verlag: Du¨sseldorf,Germany,1990;Reihe6,Nr.244.
H˙ RG,v )verticalheatfluxbythefluidizinggas,kW Itami, T.; Yoshioka, S.; Katori, T.; Oki, K.; Sakata, T. Three
H )heightofthetubebundle,m Dimensional Dynamic Simulation for Bubbling Pressurized
TB
H )lowercalorificvalueofthefuel(i.e.,drycoalorcoal Fluidized Bed Combustion Furnace. In Proc. 13th Int. Conf.
u
slurry),kJ/kg FluidizedBedCombustion;Heinschel,K.J.,Ed.;ASME: New
York,1995;Vol.2,p1303.
h˙ )evaporationenthalpyfluxbasedonunitbedvolume,
H2O Kunii, D.; Levenspiel, O. Fluidization Engineering, 2nd ed.;
W/m3
Butterworth-Heinemann: Boston,MA,1991.
k )reactionrateconstant,m3/kgs
C Miccio, M. The extension of the IEA-AFBC code to pressurized
k O )surfacereactionrateconstant,m/s conditions-Thecharcombustionsubmodel.IEA-AFBCMeeting
k TB )heattransfercoefficienttotheheat-exchangertubes, onMathematicalModelling,Firenze,Nov.8,1991.
W/m2K Pell,M.GasFluidization;Elsevier: Amsterdam,1992.

792 Ind.Eng.Chem.Res.,Vol.37,No.3,1998
Raven,P.;Sparham,G.A.Temperatureprofilesinfluidizedbed Werther,J.;Groenewald,H.;Schoessler,M.TheInfluenceofTube
combustors. In Proc. of the 7th Int. Conf. on Fluidized Bed BundlesonTemperatureHomogeneityinPressurizedFluidized
Combustion; DOE/METC/83-48, U.S. Department of Com- BedCombustion.InFluidizationVI,Proc.Int.Conf.Fluidiza-
merce: Springfield,IL,1982;p275. tion; Grace, J. R.; Shemilt, L. W.; Bergougnou, M. A., Eds.;
Smith,D.;Anderson,J.S.;Atkin,J.A.R.;Bekofske,K.L.;Brown, EngineeringFoundation: NewYork,1989;p401.
R.A.;Cavanna,J.;Christianson,S.;Failing,K.-H.;Friedman,
M.A.;Glenn,J.C.;Hebden,D.J.;Mainhardt,P.J.;Schuetz, Wirsum,M.TheoretischeBeschreibungundexperimentelleUn-
M.;Wheeldon,J.M.;Carls,E.L.IEAGrimethorpe2m×2m tersuchung der Verbrennung von Kla¨rschlamm in Blasenbil-
PressurizedFluidizedBedCombustionProject-Experimental dendenWirbelschichten.Ph.D.Dissertation,UniversitySiegen,
PerformanceResultsandFuturePlans.InProc7thInt.Conf. 1997.
Fluidized Bed Combustion; DOE/METC/83-48, U.S. Depart-
mentofCommerce: Springfield,IL,1982;p439.
Werther,J.;Bellgardt,D.;Groenewald,H.;Hilligardt,K.Influence Receivedforreview July21,1997
of immersed heat exchange surfaces on fluid mechanics and Revisedmanuscriptreceived September22,1997
solidsmixinginfluidizedbeds.InProc.9thInt.Conf.Fluidized Accepted September26,1997
BedCombustion;Mustonen,J.P.,Ed.;ASME: NewYork,1987;
p512. IE970523O
