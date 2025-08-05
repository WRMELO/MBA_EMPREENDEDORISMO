# CFB_air_blown_flash_pyrolysis_Part_I_Eng

**Fonte**: CFB_air_blown_flash_pyrolysis_Part_I_Eng.pdf  
**Data de conversão**: 2025-07-30 15:10:06  
**Origem**: base_relevantes

---

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/222067106
CFB Air-Blown Flash Pyrolysis. Part I:
Engineering Design and Cold Model
Performance
in
Article Fuel · July 2007
DOI: 10.1016/j.fuel.2006.11.002
CITATIONS READS
25 83
4 authors, including:
Grammelis Panagiotis Tony Bridgwater
The Centre for Research and Technology, Hel… Aston University
191 PUBLICATIONS 1,673 CITATIONS 164 PUBLICATIONS 11,153 CITATIONS
SEE PROFILE SEE PROFILE
Some of the authors of this publication are also working on these related projects:
S2Biom View project
All content following this page was uploaded by Stella Bezergianni on 04 March 2014.
The user has requested enhancement of the downloaded file. All in-text references underlined in blue
are linked to publications on ResearchGate, letting you access and read them immediately.

Fuel86(2007)1372–1386
www.fuelfirst.com
CFB air-blown flash pyrolysis. Part I: Engineering design
and cold model performance
I.Ph. Boukis a, P. Grammelis b,*, S. Bezergianni c, A.V. Bridgwater d
aHelectorSA,KritisandGravias12,16451Athens,Greece
bInstituteforSolidFuelsTechnologyandApplications/CentreforResearchandTechnologyHellas,
4thkmN.R.Ptolemais-Kozani,P.O.Box95,50200Ptolemais,Greece
cChemicalProcessEngineeringResearchInstitute/CentreforResearchandTechnologyHellas,Thessaloniki,Greece
dBio-EnergyResearchGroup,ChemicalEngineeringandAppliedChemistry,SchoolofEngineeringandAppliedScience,
AstonUniversity,BirminghamB47ET,UnitedKingdom
Received29August2006;receivedinrevisedform27October2006;accepted2November2006
Availableonline29November2006
Abstract
Theobjectiveofthisworkwastodesign,constructandtestanovelcirculatingfluidbedfastpyrolysisreactorsystemforproductionof
liquidsfrombiomass.Thenoveltyliesinincorporatinganintegralcharcombustortoprovideautothermaloperationofthereactor.A
reactordesignmethodologywasdevisedwhichcorrelatedinputparameterstoprocessvariables,namelytemperature,heattransferand
gas/vaporresidencetime,forboththecharcombustorandbiomasspyrolyser.Fromthismethodology,aCFBreactorwasdesignedwith
integralcharcombustionfor10kg/hbiomassthroughput.Afull-scalecoldmodeloftheCFBunitwasdevelopedandtestedtoderive
suitablehydrodynamicrelationshipsandperformanceconstraints.ThehotCFBreactorwasconstructed,itsoperabilitywastestedand
appropriate modificationswere accomplished priorto thecommissioning.
Amajorrequirementforthedesireddual-modeoperationofthereactorsystemconceivedwastheclosecouplingofthetworeactor
subsystems,namelythepyrolysisriser(mediumtemperature)andcharcombustor(hightemperature).ThebasicCFBreactordesignwas
proveneffectiveinprovidingthehighheattransferrates–expressedaslowvoidagevaluesintheriserandhighsolidcirculationrates–to
biomassparticlesintheveryshortvaporresidencetimes(VRTs)required.Theunderstandingofthecomplicatedaspectsrelatedtotwo-
phasegas–solidsflowinthestandpiperesultedinasmooth,stabletransferofsolidsoverawiderangeofoperatingparametersduring
coldCFBreactoroperation.InthehotCFBunittesting,theuseoftwoandthreecyclonesinserieswasprovedinsufficienttocapture
char and unconverted wood particles, especially during the reactor start-up phase. These problems were partially faced by adopting a
configurationofaprimarycycloneandinertiaimpingerinseries,butfurtherdevelopmentisstillrequired.Avarietyofconfigurations
fortheproductcollectionsystemwerebuiltandtested,themostefficientbeingacombinationofashell-and-tubeheatexchanger(con-
denser)andacottonwoolfilter.However,theliquidrecoveryconfigurationgaverisetoanumberofproblems,themostimportantbeing
gradualplugging oftheheatexchangerdue totheformation of sticky solid–liquid agglomerates.
(cid:2)2006Elsevier Ltd. Allrights reserved.
Keywords: Biomass;Reactor;Pyrolysis
1. Introduction supplysuchthatgasificationdoesnotoccurtoanapprecia-
ble extent [1]. For biomass pyrolysis temperatures of 400–
Biomass pyrolysis is the thermal degradation in the 800(cid:3)C are employed. Gas, liquid and solid char are
absolute absence of an oxidising agent, or with a limited produced,therelativeproportionsofwhichdependmainly
on the reaction parameters of temperature and reaction
time as well as of the rate of heat transfer to biomass
* Correspondingauthor.Tel.:+302107722865;fax:+302107723663.
E-mailaddress:pgra@central.ntua.gr(P.Grammelis). feedstock.
0016-2361/$-seefrontmatter (cid:2)2006ElsevierLtd.Allrightsreserved.
doi:10.1016/j.fuel.2006.11.002

I.Ph.Boukisetal./Fuel86(2007)1372–1386 1373
Nomenclature
AGF aeration gas flowrate [Nlit/min] Q total heat requirements for biomass pyrolysis
pyr
A, B, C, D constants given in Table 2 [–] process [kJ/h]
i i i i
CFB circulating fluidised bed [–] T temperature [K]
c specific heat capacity for each gaseous compo- T temperature in the combustor [K]
p,i C
nent i [kJ/kmolK] T temperature of the return solids [K]
st
c solids specific heat capacity [kJ/kgK] T datum temperature (=298K) [K]
p,s 0
E overallprocessenergysurplus/deficitofthepro- T temperature of the entraining gas stream [K]
sur/def 2
cess [–] U fluidising gas flowrate [Nm3/h]
f biomass mass fraction (maf) converted to char u superficialgasvelocityofairapproachingempty
1 or
[kg/kg] riser [m/s]
f total carbon content in char [kg/kg] w moisture content [–]
c
g acceleration due to gravity (=9.81) [m/s2] x char combustion efficiency (0<x61) [–]
G biomass throughput (on maf basis) [kg/h] DH(cid:2) enthalpy of the component i in entraining gas
B i
Gout mass flowrate of component i in entraining gas stream [kJ/h]
g;i
stream [kg/h] (cid:3)DH(cid:2) heat of char combustion (– for exothermic)
c
G solids circulation rate (=SCR) [kg/h] [kJ/h]
s
H static height of solids in the bubbling bed [m] DP pressure drop along the riser section [N/m2]
0
IBI initial bed inventory [–] Dz distance between pressure measurements [m]
PTO pyrolysis-to-organics [–] a ash content [–]
Q externally provided heat input (measured as e voidage [–]
ext
enthalpy of incoming air) [kJ/h] e average riser voidage [–]
avg
Q various heatlosses along the CFB system [kJ/h] q gas density [kg/Nm3]
loss g
Q heat losses in the combustor [kJ/h] q solids (sand) density [kg/m3]
loss,C s
Q heat losses in the riser [kJ/h] q suspended solids density [kg/m3]
loss,R susp
Fast pyrolysis of biomass to produce pyrolysis liquids tional secondary reactions/cracking are taking place in
has already been defined in terms of process conditions the vapor phase, which subsequently lower the liquid yield
requirements,suchastemperatureandgas/vaporresidence andhencetheperformanceofthepyrolysissystem[4].The
time, and has been characterised in terms of heat transfer results from the GTRI experience emphasise the impor-
requirements. High heat transfer is applied to avoid unde- tance of reaction severity in terms of heat transfer and
sired charring reactions of woody feedstocks. Since the the decisive role this factor plays on determining product
controloftemperatureandresidencetimemaybeadjusted yields [5]. The idea of a cyclonic reactor was explored by
inavarietyofreactorconfigurations,thecrucialcharacter- EGEMIN. However, the operation of this unit resulted
istic that most usually determines the applicability of the in lower liquid yields due to several problems [6], all indi-
different reactor configurations as successful candidates cating poor heat transfer characteristics. The Institute of
for biomass fast pyrolysis is the heat transfer mechanism Process Engineering of the Chinese Academy of Sciences
to the biomass particles. Each mode of heat transfer has also studied flash pyrolysis of lignite via a fast-
imposes certain limitations on the reactor operation and entrained bed reactor [7]. The FTIR analysis of coal and
may increase its complexity. The two dominant modes of chars showed that aliphatic structures in chars are gradu-
heat transfer for fast pyrolysis technologies are conductive ally replaced by aromatic structures with the increasing
and convective. Each mode can be maximised or a contri- of pyrolysis temperature and coal particle sise, providing
bution can be made from both, depending on the reactor fundamentaldataandoptimalconditionstomaximiselight
configuration [1].Themost successfulreactorsystemspro- oils yields for the coal topping process.
posed in the literature are listed in Table 1 [2]. These reac- Intheearly1970s,fluidisedbedreactorsweredeveloped
tor configuration systems are classified based on the forthepyrolysisofcoal,municipalsolidswaste(MSW)and
mechanism of heat transfer to biomass particles. biomass,rangingfrompilotplantstocommercialsuccessful
Georgia Tech Research Institute (GTRI) developed an demonstrations by organisations such as Energy Research
entrained flow pyrolysis process [3]. The experimental Company(ERCO)andUniversityofWaterloo.Inaddition
resultsindicatedthatthismethodwaslimitedasheattrans- totheirflexibilityandthermalstability,theyexhibitanum-
ferwasprovidedalmostentirelybyconvectionbetweenhot ber of advantages mainly in terms of operation simplicity
entraining gases and biomass particles. As a result of the and heat provision [8,9]. However, higher capacities might
higher gas/vapor residence times, which are needed to provedifficult,duetotheinherentdifficultytoscaleupshal-
ensure adequate heat transfer to biomass particles, addi- low fluidised bed systems. At the same time, Occidental

1374 I.Ph.Boukisetal./Fuel86(2007)1372–1386
Table1
Fastpyrolysisreactorconfigurations[2]
Reactortype Organisation/country Modeofheattransfer
Upflowentrainedflowbed GTRI/USA 5–10%Conduction
95–90%Convection
Downflowentrainedflowbed Egemin/Belgium 5–10%Conduction
95–90%Convection
Fluidisedbed1 ERCO/USA 80–90%Conduction
20–10%Convection
Fluidisedbed2 Univ.ofWaterloo/CanadaandUnionFenosa/Spain 80–90%Conduction
20–10%Convection
Transportreactor1 OccidentalResearchCorporation/USA 30–40%Conduction
70–60%Convection
Transportreactor2 Ensyn,Inc./Canada 50–60%Conduction
50–40%Convection
Ablativepyrolysissystems NREL/USAandAstonUniversity/UK 10%Convection
90%Conduction
Vacuumpyrolysis UniversityLaval/Canada
Table2 [13]. Even though flash pyrolysis gave the most higher
Constantsforc p,i calculation(c p inkJ/kmolKandTinK) liquid product yields, fast pyrolysis was the most interest-
Component Constant ing technology since it provided better quality products
A B C D (denser and easily transferable).
O 28.11 (cid:3)3.680·10(cid:3)2 1.746·10(cid:3)5 (cid:3)1.065·10(cid:3)8 Ablative pyrolysis for liquids was the method that
2
N 31.15 (cid:3)1.357·10(cid:3)2 2.680·10(cid:3)5 (cid:3)1.168·10(cid:3)8 National Renewable Energy Laboratory (NREL) and
2
CO 2 19.80 7.344·10(cid:3)2 (cid:3)5.602·10(cid:3)5 1.715·10(cid:3)8 Aston University were involved in which on a small scale,
most of the requirements for effective fast pyrolysis are
met. However, the potential for commercial application is
Research Corporation developed a method based on indi- minimal,becauseoftheinherentlimitationofheattransfer
rect charcombustion to provide theheat forpyrolysis in a rate through a reactor wall, complexity associated with
transport reactor [10], which however exhibited various scale-up and the general absence of other commercial
operational problems. The Chemical Process Engineering applicationofthesereactorsinthechemicalprocessindus-
Research Institute (CPERI) compared the conventional try [14]. Finally, the University of Laval proposed the
andcatalyticbiomasspyrolysis[8].Intheirstudy,theyhave method of vacuum pyrolysis of liquids [15]. The problems
achieved fast pyrolysisconditions reaching liquid products of building large leak proof equipment, in combination
yields (cid:4)70% on biomass feed. The University of Alicante with relatively low unit throughputs, render vacuum pro-
[11]performedaseriesofexperimentstostudytheproduc- cessing of wastes and low value materials impractical.
tion of gases from thermal pyrolysis of high-density poly- As seen from the extensive review of biomass fast pyro-
ethylene (HDPE) in a fluidised bed reactor, analysing the lysis reactor configurations, the energy exploitation of
effect ofthe bed temperatureand type of catalyst. byproduct char has been given little attention, the only
EnsynInc.appliedrapidthermalprocessingintransport exceptions being the Occidental Research Corporation
reactorswhichappearedtohavethemostpositiveresultsin and Ensyn Inc. with their transport reactor configuration
fast pyrolysis of biomass, since it overcame the limitations processes. However, in a commercial application of bio-
imposed by heat transfer, scalability and residence time mass fast pyrolysis, the energy content of char has to be
controllability. In this process, recirculating hot solids utilised internally in order to reduce imported energy
(sand) are used to heat biomass instead of gas, leading to and,hence,minimiseproductioncosts.Forthedesigncon-
a more compact design since the heat capacity of solids figuration proposed in this paper, the following important
per unit volume is higher than for gas. According to Gra- aspects are discussed:
ham[12]intherapidthermalprocessingreactorconfigura-
tions, ablation of the reacting particles plays a dominant • Conceptual char energy exploitation schemes to supply
role in overcoming heat transfer limitations and attaining the heat for pyrolysis.
high yields of pyrolysis liquids. Solids, moreover, facilitate • Classification of reactor configuration according to the
the separation from the product gas stream, thus avoiding desired gas–solids contacting patterns.
dilution and providing a higher energy density. Slow, fast • Conception of a new integral biomass fast pyrolysis/
and flash pyrolysis of rapeseed oil were also investigated char combustion reactor concept.

2. CFB pyrolysis design ticles incorporates some form of solid conductive heat
transfer, such as ablation. Ablation is especially dominant
Thenecessityofsatisfyingthespecificprocessconditions when relative motion between particles and inert heat car-
for biomass fast pyrolysis, namely moderate temperature, rier [12] or heated surfaces [16] is encountered. In general,
short vapor residence time (VRT) and high heat transfer the ability to control and design CFB reactors is propor-
rates,hasemergedfromthedifferentsystemconfigurations tional to the ability to predict heat transfer and fluid
adopted to overcome the various limitations imposed on mechanics.Highmomentumtransferratesareveryimpor-
biomass pyrolysis reactor design, as reviewed in the previ- tanttoremovequicklyandeffectivelytheproductsofpyro-
oussection.Asclearlyseenfromtheliteraturereview,there lysis (the product organic vapor and the byproduct char
is a need for a new reactor configuration which can over- that are formed) and thus to minimise the effects of slow
cometherestrictionsimposedbyshortgas/vaporresidence heat-up which enhances charring reactions, and extended
times (VRTs) and high heat transfer rates incorporating vapor residence times promoting secondary reactions.
integral char combustion operating on the CFB principle. The total heat transfer coefficient between the biomass
The proposed circulating fluidised bed (CFB) reactor particles and the reactor environment is the main parame-
configuration is schematically depicted in Fig. 1. Besides terforevaluatingthehighheatfluxestoincomingbiomass
the basic components, the proposed configuration must feedstock.AsreviewedbyLide´n[17],thetotalheattransfer
alsoincorporateapropersolidscirculationdevicetoensure coefficient,h,rangesbetween300and510W/m2Kforbio-
t
a stable and continuous circulation of solids between the massparticlesinabubblingfluidisedbedofsilicasandwith
biomass pyrolysis and char combustion sections. In order mean particle size of 450lm (voidage e=0.40), as derived
to combine the different dimensions of the CFB reactor from correlations applied to immersed surfaces assuming
components (biomass pyrolyser/riser and char combustor) 1mm wood particles. Temperature profiles for spherical
with the specific biomass fast pyrolysis conditions, the andcylindricalparticleshaveshownthatthewoodparticle
basic process requirements must be properly defined and centre attains a temperature of 400(cid:3)C within 2s, even in
related to operating parameters. the worst case where h =300W/m2K, satisfying the heat
t
One of the critical elements for successful fast pyrolysis transfer criterion for biomass fast pyrolysis. Therefore,
isahighheattransferratetothepyrolysingbiomassparti- heat transfer rates in a bubbling bed of small particles
cles. Heat transfer in a fluidised bed reactor configuration are considered to be sufficient for the fast pyrolysis of
combines the characteristics of various mechanisms, 1mm wood particles.
including gaseous convection heating and heat transfer. ACFBreactorisaleanphasereactoroperatingathigh
Gaseousconvectionheatingisadifficultapproachtoattain velocities and high voidages, i.e. much lower solids densi-
highheatfluxes,whileheattransferfromtheinertbedpar- ties than those encountered in a dense, bubbling fluidised
bed.Inspite,however,ofthesignificantlylowergas–solids
suspensiondensities(alternativemeasureofgas–solidssus-
pension voidage), Kobro and Brereton [18] correlated h
t
with the density of the suspension flowing past heat
exchange surfaces and estimated around 100 and 300
W/m2Kdependingontheparticlesize,seeFig.2.Various
300
250
200
150
100
50
0
0 10 20 30 40 50 60
Suspension density [kg/m3]
Fig.1. CFBbiomassfastpyrolysisreactormaincomponents.
]K2m/W[
tneiciffeoCrefsnarT
taeH
I.Ph.Boukisetal./Fuel86(2007)1372–1386 1375
Sand Particle Size [m]
250 x 10E-6
170 x 10E-6
Fig.2. HeattransfercoefficientversussuspensiondensityinaCFB[11].

1376 I.Ph.Boukisetal./Fuel86(2007)1372–1386
other researchers [19–21] also confirmed the linear depen- kinetics, solids circulation rate correlation to biomass
dence between the measured heat transfer coefficients and throughput,massandenergybalancesintheriserandchar
the suspended solids density in circulating bed boilers. combustor,andconcludeswithCFBreactorsystemperfor-
Therefore,consideringtheheattransfereffectivenessofcir- mance for biomass fast pyrolysis.
culatingversusbubblingfluidisedbedpyrolysers,compara- Experiments performed by various researchers [17,22]
ble heat transfer characteristics are obtained, even though haveclearlyshownthatthemaximumyieldforliquidprod-
circulating fluidised bed reactor systems had a much lower uctsfrombiomassfastpyrolysisisobtainedattemperatures
voidage. around500(cid:3)Candoccursoveralimitedtemperaturerange,
TheabovephenomenonofCFBreactorsystemsisdueto whileitdropsoffsharplyonbothsides.Toaccountforthe
uniquefeatures,suchasthehighslipvelocitiesandtheclus- liquid yield dropping at elevated temperatures, a reliable
tering of such configurations, which promote substantial kinetic model of biomass fast pyrolysis should incorporate
conductive heat transfer (ablation) between the pyrolysing both primary and secondary pyrolysis reactions. Such a
biomassparticlesandthesurroundinghotheatcarrierpar- model realistically predicts pyrolysis vapors yield at
ticles(clusters).Asitwasmentionedintheprevioussection, elevated temperatures.
thephenomenonofablationwasalsoencounteredintrans- Very few kinetic models incorporating secondary reac-
port reactor systems [12], where ablation was defined as a tions have been proposed in the literature and even fewer
physical/mechanical mechanism that removes the primary have been tested and verified. The kinetic model proposed
depolymerised liquids from biomass reacting surface at a by Lide´n [17,23], which was also tested by Scott et al. [24],
surfaceregressionratethatiscomparablewiththethermal has been established as one of the most successful models
penetration rate. It should also be noted that the pyrolysis in predicting pyrolysis liquid yields over a wide range of
regime for a single particle is approaching the ablative conditions. Moreover, this model tends to be validated
pyrolysisregime, where thetemperatureat aninfinitesimal by the fact that the total liquid and organic liquid (i.e.
distance below the retreating particle reaction surface excluding moisture and reaction water) yields have been
remainsfar below the reaction temperature. successfullypredicted.Anothermodelforwoodflashpyro-
As a result, the intensive mixing and high turbulence lysisinfluidisedbedreactors[25]wasdeveloped,whichwas
characteristics of the CFB reactor systems provide nearly in good agreement with experimental data. The model
the same heat transfer characteristics in them as those explored the effect of particle size and feed rate, and also
encountered in much denser reactor systems, such as the identified heating-up rate as an important factor affecting
bubblingfluidisedbedsystems,whichlackhoweverinflex- product yields.
ibilityandwaystoutilisecharenergycontentinanintegral Inordertoprovidetheenergyandmassbalancesforthe
reactor configuration concept. CFB pyrolyser we need to define the system boundary as
If the results of Kobro and Brereton [18] depicted in described in Fig. 3. The overall energy balance, derived
Fig. 2 are extended qualitatively from suspension-to-sur- over the boundary for the entire CFB system as shown in
face to suspension-to-immersed particles (biomass) heat Fig. 3 gives,
transfer,itcanbeclaimed thatahighersuspensiondensity
Heat released Heat in the
(lower voidage), resulting in a denser riser, will promote þ
by char combustion incoming stream
higher ablation and hence a higher overall heat transfer (cid:2) (cid:3) (cid:2) (cid:3)
coefficient. This extrapolation was also followed by Lide´n Heat required Various heat
¼ þ ð1Þ
[17] in his derivation of the heat transfer coefficients for a for biomass devolisation losses
(cid:2) (cid:3) (cid:2) (cid:3)
bubbling fluidised bed system. This will further enhance
whichassumingthatcharisstoichiometricallyburntbythe
theextentofpyrolysisreactionevenforlargerbiomasspar-
fluidising air becomes
ticles, as reported by Graham [12].
Theabilitytocontrolheattransferratesisaccomplished xf f G ð(cid:3)DH(cid:2)ÞþQ ¼Q þQ ð2Þ
1 c B c ext pyr loss
by manipulating the density in the riser by adjusting the
solids circulation rate (SCR) around the CFB reactor sys- If char is assumed to be entirely consumed in the combus-
tem.Thus,SCRisacriticalparameterandhastobecalcu- tor, i.e. entirely converted to CO 2 , then the char combus-
lated carefully, so that the desired heat transfer rate to tion efficiency to CO 2 , x, is equal to 1 in Eq. (2).
biomassparticlesisachievedinordertomeetthefastpyro- For the char combustor the energy balance of Eq. (1)
lysis high heat flux requirements and bypass the low heat becomes
transfer region, where the undesired charring reactions
f f G ð(cid:3)DH(cid:2)ÞþQ
prevail. 1 c B c ext
¼ GoutDH(cid:2) þG c ðT (cid:3)T ÞþQ ð3Þ
g;i i;Tc!T0 s p;s C st loss;C
2.1. Sizing the CFB reactor
X
Similarly,theenergybalanceforthebiomasspyrolysisriser
In the following sections, the CFB sizing methodology may be written as
both for biomass pyrolysis and char combustion sections
GoutDH(cid:2) þG c ðT (cid:3)T Þ¼Q þQ ð4Þ
is described. This methodology incorporates pyrolysis g;i i;Tc!T0 s p;s 2 R pyr loss;R
X

I.Ph.Boukisetal./Fuel86(2007)1372–1386 1377
Fig.3. MassandenergybalancesintheCFBreactorsections(thesymbolsandtheirsignificancearedenotedinthetext).
The heat losses are assumed to be 10% of the incoming tion stoichiometry, described by the following, simple
energy in the riser [6], which corresponds to the energy equation:
carried by entraining gases and the entrained solids:
Q ¼0:1 GoutDH(cid:2) þG c ðT (cid:3)T Þ ð5Þ
loss;R g;i i;Tc!T0 s p;s 2 st
hX i
ThethreeenergybalancesdescribedbyEqs.(1),(3)and(4)
represent two independent equations, so that any of the
three balances can be obtained from the other two. There-
fore, the main parameter of solids circulation rate can be
described by either of the two individual energy balances,
i.e. Eqs. (3) and (4):
f f G ð(cid:3)DH(cid:2)ÞþQ (cid:3) GoutDH(cid:2)
G ¼ 1 c B c ext g;i i;Tc!T0
s c ðT (cid:3)T Þ
p;s 2 Pst
Q þQ (cid:3) GoutDH(cid:2)
¼ pyr loss;R g;i i;Tc!T0 ð6Þ
c ðT (cid:3)T Þ
p;s 2P R
The above equations provide a correlation between bio-
mass throughput, G , and solids circulation rate (SCR),
B
G. In order to quantify this correlation, and hence deter-
s
mine the necessary heat carrier-to-biomass ratio, the mass
and energy balances of the two CFB components have to
be fully analysed and correlated to biomass throughput,
G .Thisisachievedbyconsideringthecombustorandriser
B
independently and analysing the different terms in detail
while correlating input and outlet streams to biomass
throughput, which is varied accordingly.
2.1.1. Mass and energy balance of char combustor
ThecharcombustorisshowninFig.4indetail.Inorder
to formulate the appropriate energy equation, a mass
balance for the char combustor must be written. The mass
balanceforthecombustorisbaseduponthecharcombus- Fig.4. CharcombustoroftheCFBreactor.

1378 I.Ph.Boukisetal./Fuel86(2007)1372–1386
Expanding the energy balance for the char combustor (ii) theheatrequirementstoreachcharignitiontempera-
extends (Eq. (3)) as follows: ture are very limited in comparison to those for the
solids heat carrier;
External Energyin Energyprovideby
þ þ (iii) G (cid:5)G, so that G +G may be approximated
char s char s
energyinput incomingsolids charcombustion
(cid:2) (cid:3) (cid:2) (cid:3) (cid:2) (cid:3) by G s ;
Energyin Energyin Various (iv) thereactionproductsintheexitofthecombustorare
¼ þ þ
entraininggas entrainedsolids heatlosses solely CO and N (CO is negligible since it results
(cid:2) (cid:3) (cid:2) (cid:3) (cid:2) (cid:3) 2 2
from the incomplete conversion of carbon char to
ð7Þ
CO , i.e. x<1, as well as of unreacted O ).
2 2
where
External T
¼ Gin c dT
"energy input#
X
g;i
ZT0
p;i 2.1
T
.2
h
.
e
M
ri
a
s
s
e
s
r
a
is
nd
an
e
a
n
l
e
y
r
t
g
ic
y
al
b
l
a
y
la
d
n
e
c
p
e
ic
o
te
f
d
ri
i
s
n
er
Fig. 5. Based on the
Energy in boundarysystemdefinitionoftheriser,theenergy balance
¼f f G DH(cid:2)
"incoming solids# 1 c B c is written as follows:
Energy in External Energy in Energy in
¼Gc ðT (cid:3)T Þ þ þ
s p;s st 0
"incoming solids# "energy input# "entraining gas# "entrained solids#
Energy in T2 Various Heat required for the
¼ Gout c dT ¼ þ ð10Þ
"entraining gas# g;i ZT0 p;i "heat losses# "pyrolysis-to-organics #
X
Energy in
where
¼Gc ðT (cid:3)T Þ
s p;s 2 0
"entrained solids#
½External energy input(cid:6)¼0
Thespecificheatcapacity,c ,foreachgaseouscomponent
p,i ½Energy in entraining gas(cid:6)
i is given, as a function of T, by the following equation:
c p;i ¼A i þB i T þC i T2þD i T3 ð8Þ ¼f 1 f c G B 4
3
4
:
:
6
0
6
1
T2
c p;CO2 dT þ 2
8
8
:
:
8
0
0
2
T2
c p;N2 dT 1
Inlet and outlet gas flowrates can be correlated to G by (cid:2) ZTR ZTR (cid:3)
B
means of char combustion reaction stoichiometry. These
correlations are given in Table 3.
½Energy in entrained solids(cid:6)¼Gc ðT (cid:3)T Þ
s p;s 2 R
Substitutingtheabovevaluesofinandoutenergyterms
in Eq. (7), the energy equation for char combustor can ½Variousheatlosses(cid:6)¼0:1 GoutDH(cid:2) þGc ðT (cid:3)T Þ
finally be written as
g;i i;Tc!T0 s p;s 2 st
2:66 T1
hX i
f f G c dT þð(cid:3)DH(cid:2)Þ Furthermore,inordertocalculatetheenergyrequirements
1 c B 32 p;O2 c
(cid:2) ZT0 (cid:3) for the transformation of biomass to organics (simply,
3:66 T1 8:80 T2 pyrolysis-to-organics/PTO) a detailed analysis of biomass
¼f f G c dT þ c dT
1 c B 44:01 p;CO2 28:02 p;N2 thermal decomposition, that is a mass balance for the
(cid:2) ZT0 ZT1 (cid:3)
pyrolysis reaction, is required. Unfortunately, this is not
þGc ðT (cid:3)T Þ
s p;s 2 0 possibledirectly,duetothelackofdefinedandclearmech-
ð9Þ anisms, exact temperatures of decomposition and suitable
For deriving the above equations, the following assump- model compounds. However, the total heat requirements
tions were made: for the pyrolysis of biomass feedstock may be approxi-
matedbyconsideringthatitiscomposedofdifferentparts,
(i) char particles entering the combustion chamber namely:
instantaneously attain the fluidised bed temperature
(i.e. from T to T ); • sensible heat requirements for the dry biomass feed;
st c
• the heat of vaporisation of the primary products;
Table3 • the heat of reaction;
Inletandoutletgasmassflowrates • thesensibleandlatentheatrequirementsofthemoisture
G (kg/h) AsafunctionofG content.
g,i B
Gin 2.66ff G
g;O2 c1 B
Gi g n ;N2 8.80f c f 1 G B 1 The combustor flue gases (entraining gases) are not undergoing any
Gout 3.66ff G chemicalreaction,i.e.thecombustionandaerationgases,whicharesolely
G
g
o
;
u
C
t
O2
¼ðGin Þ 8.80f
c
f
1
G
B
N 2 andCO 2 ,areconsideredinertinthetemperatureintervalconsidered,
g;N2 g;N2 c1 B leavingtheriseratT (=T ).
3 R

I.Ph.Boukisetal./Fuel86(2007)1372–1386 1379
Fig.5. TherisersectionoftheCFBreactor.
Atthisstageitshouldbenotedthataconsiderableeffort
tone,aceticacidandsoon)andgas.Atabout300(cid:3)Cwater
has been dedicated to determine the heat of reaction for is produced from the rupture of biomass structure. Heavy
primary pyrolysis, with a wide range of values existing in organics (‘‘oil product’’ or ‘‘primary tar’’) are vaporised
the literature [12,14,23] as estimated for different biomass at 350(cid:3)C. The non-condensible gases are being formed
feedstock, experimental equipment, reaction conditions, over the entire range of temperatures and they originate
andtheextenttowhichthereactionsarepermittedtooccur (evolve) directly from the biomass. In this case biomass
ineachcase[12].Thereis,however,generalagreementthat pyrolysis would occur between 250 and 350(cid:3)C and all
primary fast pyrolysis is moderately endothermic [26,27] products are generated directly from the biomass. For this
whileafewauthorsspeculatethatfastpyrolysisisathermic case, the total heat requirements for fast pyrolysis is given
at approximately 700(cid:3)C and increases in endothermicity as a function of G B , w and a as
with increasing temperature [28]. For engineering applica-
Q
tions, the heat of reaction of primary pyrolysis is often Q ¼ Q þ Q ) pyr
pyr pyr;iðAÞ wat;iðAÞ G
assumed to be negligible when compared to other heating B
effects referred to above. Thus, the energy requirements X X w
¼ 991:5þ3392 ð11Þ
are limited to heat for raising the temperature of biomass 1(cid:3)ðwþaÞ
(cid:2) (cid:4) (cid:5)(cid:3)
to reaction temperature (sensible heat) and heat of vapori-
sationofrawmaterialand/orproducts.Theheatofvapori- where w and a indicate the moisture and ash content,
sation is estimated from the distribution of the vaporised respectively.
products out of the pyrolysis reactor. The reaction occur- Inthis case, themean heatof vaporisation will be(on a
ring in the riser is simply biomass thermal decomposition maf basis, i.e. w=a=0) 1166.5kJ/kg of actually vapor-
to vapors/organic products, char, water and non-condens- ised biomass (excluding the char).
ible gases. The vaporisation energy of products as well as In the second case, referred to as subsequent products
sensible heat to bring biomass and pyrolysis products to evolution, the different products are subsequently released
reaction temperature is required. The problem is that the from biomass. Steam is evolved at 135(cid:3)C, light organics
temperature at which the pyrolysis products are vaporised at150(cid:3)Candheavyorganics(‘‘oilproduct’’)atanaverage
isuncertain,whichstronglyinfluencestherequiredheat.As of275(cid:3)C. The gases are formed in avaporphasecracking
this temperature is unknown, two cases have been studied ofthe‘‘oilproduct’’,whichmeansthattheirheatofvapori-
in the past [29]. sation isthe same asthat ofthe‘heavy’ organics,inaccor-
In the first case, which is referred to as direct products dance with Lide´n’s model. The adaptation of this
evolution, biomass remains intact up to a temperature of assumption considers the fact that at least some products
about 250(cid:3)C. It is assumed that at this temperature, a are formed before others when the temperature is
breakdown starts releasing light organics (methanol, ace- increased, a hypothesis also confirmed by Elliot [30].

Thepyrolysiswouldoccuratapproximately275(cid:3)Candthe Therefore the energy balance for the riser (Eq. (10))
final products are either generated directly from the bio- becomes,
massorevolvedbyheavyorganicsbyvaporphase,second-
3:66 T2 8:80 T2
ary reactions. The heat for PTO is estimated from the f f G c dT þ c dT
1 c B 44:01 p;CO2 28:02 p;N2
following equation as a function of G B , w and a: (cid:2) ZTR ZTR (cid:3)
þG c ðT (cid:3)T Þ
s p;s 2 R
Q
Q pyr ¼ Q pyr;iðAÞ þ Q wat;iðAÞ ) G p B yr ¼0:1 Go g; u i tDH(cid:2) i;Tc!T0 þG s c p;s ðT 2 (cid:3)T st Þ
X X w hX w i
¼ 1332:9þ3702:7 ð12Þ þ1:15G 1332:9þ3702:7 ð13Þ
1(cid:3)ðwþaÞ B 1(cid:3)ðw(cid:3)aÞ
(cid:2) (cid:4) (cid:5)(cid:3) (cid:2) (cid:4) (cid:5)(cid:3)
At this point, the energy balances for both the char com-
From the above analysis the last term of Eq. (10) can be
bustorandriserunitsoftheCFBreactorsystemhavebeen
estimated as a function of G , w and a below, considering
B derived and all the different energy terms have been corre-
an additional 15% increase compensating for unaccounted
latedwithbiomass(maf)throughput(G ),feedstockmois-
energy requirements: B
ture (w) and ash content (a). This detailed analysis will
permit in the following the calculation of the required sol-
Heat required for the
idscirculationrates(SCR),bymeansofEq.(6),derivedby
pyrolysis-to-organics
(cid:2) (cid:3) the char combustor (Eq. (9)) and riser (Eq. (13)) energy
w
balance equations, for a wide range of biomass through-
¼1:15G 1332:9þ3702:7
B 1(cid:3)ðw(cid:3)aÞ puts and feedstock moisture content.
(cid:2) (cid:4) (cid:5)(cid:3)
1.40
1.30
1.20
1.10
1.00
0.90
0.80
7.50 10.00 12.50 15.00 17.50 20.00 22.50 25.00
Biomass Moisture Content [% wt]
ticifeD/sulpruS
ygrenE
Fig.6. CFBreactorenergysurplus/deficitforbiomassfeedstockmoisturecontentsbetween7.5and25wt%(wetbasis).
140.00
120.00
100.00
80.00
60.00
40.00
20.00
0.00
5 6 7 8 9 10 11 12 13 14 15
Biomass Flowrate [kg maf/h]
]h/gk[
etaR
noitalucriC
sdiloS
1380 I.Ph.Boukisetal./Fuel86(2007)1372–1386
Water content
[% wt]
7.5
10.0
12.5
15.0
17.5
20.0
22.5
25.0
Fig.7. TheeffectofwatercontentonSCRforbiomassthroughputs(5–15kgmaf/h).

I.Ph.Boukisetal./Fuel86(2007)1372–1386 1381
2.2. CFB system performance for biomass fast pyrolysis Table4
Main CFB fast pyrolysis reactor dimensions based on a 10kgmaf/h
biomassthroughput
The energy balance equations for the char combustor
(Eq.(9))andriser(Eq.(13))areusedtodeterminetheover- Reactortype CFB
Biomassthroughput(kgmaf/h) 10.0
all process energy surplus/deficit, E , of the process,
sur/def Riserheight–L (m) 2.0
incorporating integral char combustion in the lower part R
Riserdiameter–D (m) 0.05
R
of the CFB reactor, which is defined as Combustordiameter–D (m) 0.175
B
Combustorheight–L (m) 0.50
Energyprovidedbycharcombustion(cid:3)Energyprovidedtofluidisinggas B
Esur=def¼
PTOenergyrequirementsþVariousenergylosses
Solidscirculationdevice L-valve
Solidsseparationsystem 2Cyclones
ð14Þ
From the above equation, the overall process energy sur-
plus/deficitforfeedstockmoisturecontentsisestimatedbe-
tween 5 and 25wt% (wet basis). Fig. 6 demonstrates that
for low-moisture content biomass feedstocks (<17.5wt%
moisture content), energy self sufficiency is achieved
(E >1), while for medium and high moisture content
sur/def
feedstocks (>17.5wt% moisture content), additional fuel
must be imported (E is below unity; energy deficit).
sur/def
When deriving these correlations and for safety reasons,
PTO energy requirements were deliberately overestimated
by 15% while the pyrolysis gas energy content utilisation
wasnotbeentakenintoaccount.Iftheaboveassumptions
are relaxed, the proposed CFB reactor system energy self
sufficiency could further be improved.
Moreover combining Eqs. (6), (9) and (13), SCR is
correlated to biomass throughput, G , and water content,
B
w, as shown in Fig. 7.
As seen from Fig. 7, a higher biomass throughput will
require higher solids circulation rates to meet the energy
requirements for the fast pyrolysis process. Moreover,
wet feedstocks would require higher SCRs than dry ones
as expected after combining Eqs. (6) and (13).
2.3. CFB reactor system sizing
In order to size the CFB reactor system, we firstly con-
sidersizingtherisersectionandsecondlythecharcombus-
tor section. The gas/vapor residence time constraints as
well as the requirements for the operation of the CFB
system in the fast fluidisation regime set up a spectrum of
specific reactor sizing requirements. Regarding the char
combustorsizing,thespecialfeaturesofthedesiredhydro-
dynamicsconstitutethemajorfactorforthedetermination
ofitsdimensions.TheCFBreactorsystemperipheralcom-
ponents include the gas distributor, the solids reinjection
system and the solids recovery system. The CFG reactor
system sizing and peripherals were selected and designed
Fig. 8. The circulating fluidised bed (CFB) fast pyrolysis reactor (scale
for a 10kgmaf/h biomass throughput. The main equip-
1:20)(1,combustionchamber;2,riser(pyrolysisreactor);3,alternatefeed
ment dimensions are described in Table 4. ports; 4, expansion joints; 5, primary cyclone; 6, secondary cyclone; 7,
Finally the detailed drawing of the circulating fluidised standpipe;8,L-valve;9,wind-box;10,fluidisinggasinlet;11,productgas
bed reactor is given in Fig. 8. The construction material outlet;12,aerationgasinlet).
was AISI 316 L and the thickness of the equipment
between 3 and 4mm in order to achieve an acceptable ports for biomass feeding have been considered, the upper
resistance to the abrasion phenomenon, readily encoun- feeding port was never used because of the very low gas/
tered in CFB reactors.Biomass was fedinto theCFB riser vapor resistance time already achieved when the lower
section via the lower feeding port. Although alternate feed feeding port was employed.

1382 I.Ph.Boukisetal./Fuel86(2007)1372–1386
3. Cold model performance • A dense bed of 172mm internal diameter (i.d.) and
500mm long (the combustion chamber), operating in
Since there was no previous experience on CFB reactor the bubbling/slugging mode. Solids are entrained
operation, it was decided that a full scale, cold model rep- through a conical section by the gas (air) into the riser
licaoftheproposedCFBreactorshouldbebuiltandoper- section.
ated.Thecoldmodelconstructionandtestingwasjustified • A high velocity riser, of 50mm i.d. and 2500mm long.
inordertogainoperationalexperience,examinethehydro- • A solids separation system, consisting of a single
dynamics and establish operating regimes and system cyclone.
limitations. • A solids reinjection system, comprising a long (3000
Two series of experiments were conducted in the CFB mm) but narrow standpipe of 25mm i.d., and a non-
cold model. During these experiments, the main operating mechanical L-valve for aerating the standpipe and
variables crucial to the CFB operation and their effect on allowing the separated solids to return to the dense
importantoperatingparameters,associatedwithheattrans- bed.
fer and solids circulation stability, were identified and
discussed. Two series of experiments were performed with the
above CFB cold model configuration with the following
3.1. Design specifications objectives:
The necessary measurements for the determination of • to get acquainted with CFB operation;
hydrodynamic characteristics were conducted on the cold • to obtain preliminary data on the interaction of initial
model CFB unit, constructed specifically for this work. bed inventory (IBI) and fluidising gas flowrate (U) on
Theconstructionofthisunitandtheaccompanyinginstru- riser average voidage, which was investigated during
mentation are described below. the first series of experiments; and
The CFB cold flow model was built of similar dimen- • to derive detailed correlations for IBI and U, defining
sionstothehotunitandmadetransparenttopermitobser- the desired operating regimes;
vation of the flow phenomena. The CFB cold model, • to evaluate the achieved solids circulation rate (SCR)
shown in Fig. 9, comprised four sections, namely: values along the CFB loop;
Fig.9. TheCFBcoldmodel.

• to determine the operating parameters for standpipe the two most important process parameters, namely the
stability. static height of solids in the bubbling bed, H (denoting
0
changes in IBI), and the superficial gas velocity of air
Thelastthreeissueswereinvestigatedduringthesecond approachingemptyriser,u (denotingchangesinU).Pres-
or
seriesofexperimentsintheCFBcoldmodelconfiguration. sure drop measurements were estimated by evaluating the
water manometer indications and correlating them with
3.2. Series I of experiments mean pressure transducer response. The variation of the
operating parameters during the first series of experiments
In this first series of experiments, the dense phase of is summarised in Table 5.
inertsolids(silicasand)isdeterminedbyreachingacertain Inserting the experimentally derived pressure drop data
heightinthebubblingbed.Thedensephaseofsolidspres- evaluated and correlated as in Eqs. (15) and (16), voidage
ent is called thereafter initial bed inventory (IBI). These and suspension density correlations for different IBIs (H )
0
solids are then fluidised by a given amount of fluidising andUs(u )areobtained.AsshowninFig.10,alowervoi-
or
air, referred to as fluidising gas flowrate (U). During oper- dage, i.e. a denser riser, can be achieved for a given U by
ation, air is passed through the bed via the wind-box and varyingIBI,adjustingthesandheighttoahigherlevel,H .
0
the gas distributor, which causes the bed to expand. Subsequently,theaveragesuspensiondensityintheriser
Highvelocityairisusedtobringthefluidisedbedatthe is derived applying Eq. (16). The results are shown in
bubbling/slugging operation mode and to cause the solids Fig. 11, clearly indicating that a denser suspension, and
entrained in the conical section, Fig. 9, to accelerate and henceahigherheattransferrate,canbeachievedforhigher
to be carried up the riser. The gas–solid suspension then totalsolidscharging(higherH )forthesamefluidisinggas
0
passes through the cyclone, where solids are recovered flowrate (U). Also it may be concluded that the perfor-
and recirculated to the dense bed (combustion chamber) mance of the CFB reactor as a biomass fast pyrolyser is
via the reinjection system. The height of the solids in the
standpipe is controlled by varying the rate of aeration to
the L-valve, a procedure used to ‘‘fine-tune’’ the solids cir-
culationrateatadesired,predefinedvalue.Duringthisfirst
series ofexperiments,theaerationgasflowrate(AGF)was
not recorded and was kept at a constant value for a given
setofIBIandU.ThesignificanceofAGFonhydrodynam-
ics and standpipe stability is examined in detail during the
second series of experiments.
HeattransferinCFBsdirectlyrelatestoaveragevoidage
and hence suspension density in the riser section. In order 1.005
to evaluate quantitatively the suspension density along the 1
riser, it is necessary to estimate the average voidage in this 0.995
section of the CFB reactor, which can be calculated from 0.99
the pressure gradient. If the combined effect of gas-wall 0.985
friction, solids-wall friction and solids acceleration is 0.98
neglected, the pressure measured across the riser section 0.975
of the CFB riser section is mainly attributed to the static 0.97
20 22 24 26 28 30 32
head of solids in the suspension, that is, to the weight of U [Nm3/h]
thesolidsandfluidperunitarea,asshowninthefollowing
equation:
DP ¼ðq (cid:3)q Þ(cid:7)g(cid:7)ð1(cid:3)eÞ(cid:7)Dz ð15Þ
s g
The suspension density in the riser section is then directly
correlated to the voidage by the following relationship:
q ¼ð1(cid:3)e Þ(cid:7)ðq (cid:3)q Þ ð16Þ susp avg s g
In order to measure static pressures at different points
along the length of the riser and the standpipe, access
ports/pressure taps were located at regular intervals along
the system as shown in Fig. 9. Riser pressure profiles were
determined using the pressure taps located at 400mm
increments along the riser length.
The experiments that were carried out aimed to obtain
average pressuredropsintheCFB risersectionby varying
resir
eht
ni
egadiov
gvA
Table5
Variationoftheoperatingparameters(IBI,UandAGF)duringthefirst
seriesofexperimentsintheCFBcoldmodel
IBI(H inm) 0.245 0.310 0.335
0
U(Nm3/h) 21,26,28,31 21,26,28 21,26,28
AGF(Nlit/min) KeptconstantforagivensetofIBIandU
Height of static
bed [m]
Ho=0.245
Ho=0.310
Ho=0.335
Fig.10. AverageriservoidageversusUfordifferentIBIs.
1.005
1
0.995
0.99
0.985
0.98
0.975
0.97
20 22 24 26 28 30 32
U [Nm3/h]
resir
eht
ni
egadiov
gvA
I.Ph.Boukisetal./Fuel86(2007)1372–1386 1383
Height of static
bed [m]
Ho=0.245
Ho=0.310
Ho=0.335
Fig.11. SuspensiondensityversusUfordifferentIBIs.

1384 I.Ph.Boukisetal./Fuel86(2007)1372–1386
Table6
Variationoftheoperatingparameters(IBI,UandAGF)duringthesecondseriesofexperimentsintheCFBcoldmodel
LowIBI HighIBI
IBI(kg) 9.5 9.5 9.5 10.5 10.5 10.5
U(Nm3/h) 27.95 32.86 37.33 24.96 28.78 32.86
AGF(Nlit/min) Variedaccordingly,coveringtherangefrom2.5to11.5
greatly dependent on riser density profile, which in turn is variation of the operating parameters during the second
mainly determined by IBI (H ) and U (u ). series of experiments is summarised in Table 6.
0 or
Fromthisfirstseriesofexperimentsinthecoldmodel,it TheaveragevoidageintheriserversusAGFforthelow
can be concluded that IBI and Uhave apronouncedeffect IBI(9.5kg),alsogiveninTable6,andtherespectiveUsare
on the macroscopic structure of the gas–solids suspension, shown in Fig. 12. It is clear that AGF variations affect the
characterised by suspension density/voidage in the riser densityprofileintheriserasindicatedbytheminimumvoi-
section of the CFB. More specifically, it was shown that dage, being obtained for the higher U values, as expected
higherrisersuspensiondensitiesareobtainedathighersol- from the results obtained during the first series of experi-
idsinventoriesforagivengasvelocity.Despitetheseinitial ments.Thus,givenasetofIBIandU,itispossibletovary
findings, important issues such as a more reliable riser the average voidage profile and regulate the rate of heat
density profile characterisation, and the role of the non- transfer by simply manipulating AGF. After examining
mechanical valve operation in both standpipe stability the family of curves in Fig. 12, it may also be concluded
and control of SCR required further experimental investi- that the lower voidage values, and hence the higher riser
gation, which was undertaken during the second series of densities,areobtainedatlowerUsforthehigherIBI(Table
experiments on the cold CFB model. 6),whichshowsthepositiveeffectofanincreasedIBIinthe
CFB reactor.
The standpipe pressure drop per unit length (standpipe
3.3. Series II of experiments
pressure gradient) versus AGF for high IBI (10.5kg) and
the respective Us is shown in Fig. 13.
Literature data from similar circulating fluidised bed
Referring now to standpipe stability and analysing
experimentalstudies[8,31]indicatethatmoreexperimental
Fig. 13, where the change in DP/L as a function of the
pointsarerequiredinordertoderiveameaningfulcorrela-
amount of aeration gas added to the standpipe is plotted,
tion between riser voidage and fluidisation parameters,
it may be seen that the pressure drop per unit length
expressedasvariationsinIBIandU.However,thesubjec-
increasesuptoacertainvalueandthenbeginstodecrease.
tive estimation of pressure drop variation observations
The initial increase in DP/L causes the solids level in the
from both the U-tube water manometers and the slow
standpipe to decrease since the total standpipe DP must
response transducer during the first series of experiments
remain constant. Therefore, aerating the standpipe near
in the CFB cold flow model could not provide a rigorous
the bottom has a great effect on decreasing the solids seal
andaccurateacquisitionofexperimentaldata.Forthesec-
height, maintaining the moving solids in the moving bed
ondseriesofexperiments,theslowresponsepressuretrans-
or near the fluidised bed flow mode.
ducers was substituted by fast response (0.5s) differential
The solids circulation rates (SCR) were also estimated
pressure transmitters (Fischer–Rosemount Model 1151
during this second series of experiments in the CFB cold
DP) connected to a data acquisition system to obtain reli-
model, since they constitute an important process variable
abledataforthecriticalpressuredropmeasurementsalong
for the effective utilisation of the CFB reactor as a high
the entire CFB loop. Furthermore, in the second series of
heat transfer reactor configuration. SCR was measured
experiments, the L-valve aeration gas flowrate (AGF)
usingtheflowdiversiontechnique,accordingtowhichsol-
was varied as it was constant during the first series of
ids are diverted while descending the standpipe for a mea-
experiments.2
sured time interval. At the same time, solids are
In order to characterise the riser solids fraction and
transferred from the standpipe to the fluidised bed via
standpipe stability in terms of the CFB operating parame-
the L-valve, so that the bubbling bed inventory (IBI) is
ters, namely U, IBI and AGF, a second series of experi-
kept constant. The measurement is interrupted when the
ments, discussed below, were conducted. During these
standpipe is depleted of solids. The collected solids are
experiments, two given IBIs and three different values of
reinjected to the system and a new experiment for SCR
Us were tested via a total of six (2·3) experiments. The
determination begins.
Anadditionalsequenceofexperimentswasconductedin
ordertodeterminetheeffectsoftheoperatingvariableson
SCR. More specifically, for a set of two different IBIs and
2 Inthefirstseriesofexperiments,themajorobjectivewastoidentifythe
two different Us, the SCR is determined as a function of
significance of the major operating parameters ensuring CFB stable
operationbysettingAGFtoapresetvalue. AGF. The SCR versus AGF for the two different sets of

1.001
1
0.999
0.998
0.997
0.996
0.995
0.994
2 4 6 8 10 12
Aeration Gas Flowrate [Nlit/min]
IBI and U is presented in Fig. 14, denoting that a higher mass pyrolysing feedstocks rather than heat transfer rates
SCR and hence a denser riser may be obtained at much to biomass particles.
lower Us provided there is a high initial bed inventory in Nevertheless,heattransferratesareconsideredsufficient
the system. according to the data derived from the CFB cold model
AsseenfromtheSCRmeasurementdatainFig.14,val- experimentsgiventhefactthatforabiomassfastpyrolysis
ues higher than 100kg/h are obtained for the two sets of process,asand:biomassratioofapproximately10:1–20:1is
IBIandUinvestigated.TheseSCRvaluesareconsiderably practicallyrequired[12,32].ThedatashowninFig.14indi-
higher than those theoretically calculated to transfer the cate that the proposed CFB reactor operating conditions
required energy, Fig. 7, even to wet biomass feedstocks. successfully satisfy both the energy and the imposed heat
However, the calculation procedure employed for Fig. 7 transferraterequirements,evenatthemostextremecondi-
isrelated tothesatisfaction ofenergy requirementsto bio- tions (low values for IBI, U and AGF).
resiR
eht
ni
egadioV
gvA
U [Nm3/h]
27.95
32.86
37.33
Fig.12. RiseraveragevoidageversusAGFfordifferentUs(IBI=9.5kg).
10000
8000
6000
4000
2000
4 5 6 7 8 9 10 11 12
Aeration Gas Flowrate [Nlit / min]
]m/aP[
P∆
U [Nm3/h]
24.96
28.78
32.86
Fig.13. StandpipepressuregradientversusAGFfordifferentUs(IBI=10.5kg).
240
220
200
180
160
140
120
100
80
3.5 4 4.5 5 5.5 6 6.5
Aeration Gas Flowrate [Nlit / min]
noitalucriC
sdiloS
]h/gk[
etaR
I.Ph.Boukisetal./Fuel86(2007)1372–1386 1385
IBI=10 kg
U=35 Nm3 / h
IBI=11 kg
U=25 Nm3 / h
Fig.14. SCRversusAGFfortwodifferentpairsofIBIsandUs.

1386 I.Ph.Boukisetal./Fuel86(2007)1372–1386
4. Conclusions [8] LappasAA,SamoladaMC,IatridisDK,VoutetakisSS,VasalosIA.
Biomasspyrolysisinacirculatingfluidbedreactorfortheproduction
offuelsandchemicals.Fuel2002;81(16):2087–95.
A circulating fluidised bed (CFB) reactor with integral
[9] DaiX,YinX,WuCh,ZhangW,ChenY.Pyrolysisofwastetiresina
char combustion was selected for biomass fast pyrolysis,
circulatingfluidized-bedrector.Energy2001;26(4):385–99.
as it incorporated the most desirable features to maximise [10] BogleyWJ,MixonWR,DeanC,LizdasDJ.Solidwasteutilization-
pyrolysis liquids yields. A major requirement for the pyrolysis. OakRidge(TN): OakRidgeNationalLaboratory;1977.
desired dual-mode operation of the reactor system con- [11] Herna´ndezM,Garc´ıaA´N,MarcillaA.Studyofthegasesobtainedin
thermal and catalytic flash pyrolysis of HDPE in a fluidized bed
ceived was the close coupling of the two reactor subsys-
reactor.JAnalApplPyrol2005;73(2):314–22.
tems, namely the pyrolysis riser (medium temperature)
[12] GrahamRG.Acharacterisationofthefastpyrolysisofcelluloseand
and char combustor (high temperature). A design proce- woodbiomass.PhDthesis,UniversityofWesternOntario;1993.
dure was developed leading to the establishment of the [13] Onay O, Kockar MO. Slow, fast and fast pyrolysis of rapeseed.
appropriate design variables, including biomass flowrates, RenewEnerg2003;28(15):2417–33.
[14] Peacocke CVC. Ablative pyrolysis of biomass. PhD thesis, Aston
reactor dimensions and process parameters, such as riser
University,UK;October1994.
temperature and VRT.
[15] Roy C, de Caumia B, Plante P, Menard H. In: Proceedings of the
A cold CFB reactor model was further constructed and conference on energy from biomass and wastes VII, Lake Buena
tested. The macroscopic phenomena of CFB reactor Vista,FL,24–28January1983.Inst.GasTechn.,Chicago(IL);1983.
hydrodynamics,inparticular theriservoidage, were inves- p.1147.
[16] DieboldJP.Thecrackingkineticsofdepolymerizedbiomassvapours
tigated in a cold model of similar dimensions to the pro-
inacontinuoustubularreactor.MasterofSciencethesis,Colorado
posed hot CFB bench scale biomass pyrolyser. The cold
SchoolofMines,Golden(CO);1986.
CFBmodelexperimentswereusedtodeveloprelationships [17] Lide´n AG. A kinetic and heat transfer modelling study of wood
between heat transfer and operating parameters and fur- pyrolysis in a fluidized bed. Master thesis, University of Waterloo,
ther to develop the experimental methodology, which Waterloo(Ont.);1985.
[18] Kobro H, Brereton C. In: Basu P, editor. Circulating fluidized bed
would provide stable and unhindered reactor operation.
technologyII. Toronto: Pergamon;1986.p.263–72.
Inconclusion,itmaybeclaimedthattheproposedCFB
[19] StrombergL.ArchCombust1981;1:95–107.
reactorsystem meetsboththeobjectivesofenergyselfsuf- [20] StrombergL.In:Proceedingsofthe7thinternationalconferenceon
ficiency, by utilising the energy content of byproduct char fluidizedbedcombustion,vol.2;1982.p.1152–63.
in an integral approach, and high heat transfer rates, by [21] ZhengQY,WangX,LiX.In:BasuP,HorioM,HasataniM,editors.
Circulating fluidized bed technology III. Nagoya-Japan: Pergamon
properly regulating SCR therefore adjusting heat car-
Press;1990.p.263–8.
rier:biomass ratio. It should also be noted that process
[22] SamoladaMC,VasalosIA.Fuel1991;70:883–9.
costs as well as complexity were considered and further- [23] Lide´nAG,BerrutiF,ScottDS.ChemEngCommun1988;65:207.
more heat losses were greatly minimised. [24] Scott PS, Piskorz J, Radlein D. Pyrolysis as a basic technology for
largeagro-energyprojects.In:MattucciE,GrassiG,PalzW,editors.
ProceedingsofaworkshopheldinL’Aquila(Italy);1987.p.115–24.
References
[25] LuoZ,WangS,CenK.Amodelofwoodflashpyrolysisinfluidized
bedreactor.RenewEnerg2005;30:377–92.
[1] Bridgwater AV, Evans GD. An assessment of thermochemical [26] Antal MJ, Friedman HL, Rogers FE. Combust Sci Technol
conversionsystemsforprocessingbiomassandrefuse,ETSUB/T1/ 1980;21:141–52.
0020/REP;1993. [27] ScottDS,RadleinD,PiskorzJ,MajerskiP.Potentialoffastpyrolysis
[2] BridgwaterAV,MeierD,RadleinD.Anoverviewoffastpyrolysisof fortheproductionofchemicals.In:Meetingonbiomassliquefaction,
biomass.OrgGeochem1999;30:1479–93. AlternateEnergyBranch,Canmet,Energy-Mines-Resources,Ottawa;
[3] Kovac RJ, Gorton CW, Knight JA, Newman CJ, O’ Neil, DJ. 1991.p.171–8.
Research on the pyrolysis of hardwood in an entrained bed PDU. [28] Deglise X, Morliere P, Sclicklin Ph. Proceedings of the 1st EC
Prepared for the USDoE under Contract DE-ACO6-76RLO 1830, conference on energy from biomass, Brighton, 4–7 November
PNL-7788/UC-245;August1991. 1980. London: AppliedSciencePublishers;1981.p.569.
[4] Knight JA, Gorton CW, Kovac RJ. Entrained flow pyrolysis of [29] McKeoughP.etal.IEAco-operativeprojectD1:biomassliquefac-
biomass. In: Proceedings of the 16th Biom Thermochem Conv tiontestfacilityproject,vol.5.App.J,DOE/NBM-1062;1988.
Contractmeeting,8–9May1984,Portand-Oregon,CONF-8405157/ [30] ElliotDC.Analysisandcomparisonofbiomasspyrolysis/gasification
PNL-SA-12403;1984.p.287. condensates–interimreport.PNL-5555,PacificNorthwestLabora-
[5] Demirbas A. Analysis of liquid products from biomass via flash tory,Richland(WA);1985.
pyrolysis.EnergSource2002;24(4):337–45. [31] Arena U, CammarotaA, Pistone L. In: Basu P, editor. Circulating
[6] ManiatisK.Fluidizedbedgasificationofbiomass.PhDthesis,Aston fluidizedbedtechnologyI. NewYork: Pergamon;1986.p.119.
University;1986. [32] SERI,Specialists’workshoponfastpyrolysisofbiomass.SERI/TR-
[7] Cui L-J, Lin W-G, Yao J-Z. Influences of temperature and coal 33-239.Sol.Energ.,Res.Inst.,Golden(CO);1980.
particle size on the flash pyrolysis of coal in a fast-entrained bed.
ChemResChinUniv2006;22(1):103–10.
