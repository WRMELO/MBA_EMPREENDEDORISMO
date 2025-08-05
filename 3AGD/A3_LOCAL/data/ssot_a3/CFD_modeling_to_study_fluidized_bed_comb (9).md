# CFD_modeling_to_study_fluidized_bed_comb (9)

**Fonte**: CFD_modeling_to_study_fluidized_bed_comb (9).pdf  
**Data de conversão**: 2025-07-30 15:04:29  
**Origem**: base_relevantes

---

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/257537726
CFD modeling to study fluidized bed
combustion and gasification
in
Article Applied Thermal Engineering · April 2013
DOI: 10.1016/j.applthermaleng.2012.12.017
CITATIONS READS
50 666
3 authors:
Ravi Inder Singh Anders Brink
Birla Institute of Technology and Science Pilani Åbo Akademi University
44 PUBLICATIONS 97 CITATIONS 86 PUBLICATIONS 601 CITATIONS
SEE PROFILE SEE PROFILE
Mikko Markus Hupa
Åbo Akademi University
466 PUBLICATIONS 6,659 CITATIONS
SEE PROFILE
All content following this page was uploaded by Ravi Inder Singh on 17 February 2015.
The user has requested enhancement of the downloaded file. All in-text references underlined in blue are added to the original document
and are linked to publications on ResearchGate, letting you access and read them immediately.

(Thisisasamplecoverimageforthisissue.Theactualcoverisnotyetavailableatthistime.)
This article appeared in a journal published by Elsevier. The attached
copy is furnished to the author for internal non-commercial research
and education use, including for instruction at the authors institution
and sharing with colleagues.
Other uses, including reproduction and distribution, or selling or
licensing copies, or posting to personal, institutional or third party
websites are prohibited.
In most cases authors are permitted to post their version of the
article (e.g. in Word or Tex form) to their personal website or
institutional repository. Authors requiring further information
regarding Elsevier’s archiving and manuscript policies are
encouraged to visit:
http://www.elsevier.com/copyright

Author's personal copy
AppliedThermalEngineering52(2013)585e614
ContentslistsavailableatSciVerseScienceDirect
Applied Thermal Engineering
journal homepage: www.elsevier.com/locate/apthermeng
CFD modeling to study fluidized bed combustion and gasification
Ravi Inder Singha,b,*,1, Anders Brinkb, Mikko Hupab
aDepartmentofMechanicalEngineering,GuruNanakDevEngineeringCollege,GillRoad,Ludhiana141006,India
bProcessChemistryCenter,DepartmentofChemicalEngineering,ÅboAcademyUniversity,Åbo,Finland
h i g h l i g h t s
<SummaryofCFDmodelingtostudycombustion/gasificationinfluidizedbedisdone.
<EquationsforCFDmodelingforfluidizedbedcombustion/gasificationexplained.
<CFDmodelingcanpredictheatflux,flow,temperature,ashdepositsandemissions.
<Trends,challengesandfutureresearchareasinthisfieldareexplored.
a r t i c l e i n f o a b s t r a c t
Articlehistory: Theincreaseinapplicationoffluidizedbedcombustionandgasificationdevicesthroughoutworldmeans
Received3August2012 thatmoreconsiderationwillbegiventoimprovedesignandreduceemissionsofthese.Duetoexcellent
Accepted18December2012 thermalandmixingpropertiesfluidizedbedsaregenerallypreferredoverthefixedbedcombustorsand
Availableonline2January2013 gasifiers. Computational Fluid Dynamic (CFD) is a technique which helps to optimize the design and
operation of fluidized bed combustor and gasifiers. Recent progression in numerical techniques and
Keywords: computingefficacyhasadvancedCFDasawidelyusedpracticetoprovideefficientdesignsolutionsin
Fluidization fluidized bed industry. In this paper an extensive review of CFD modeling to study combustion and
Combustion
Multiphaseflow gasification in fluidized beds has been done. This paper introduces the fundamentals involved in
Hydrodynamics
developingaCFDsolutionforfluidizedbedcombustionandgasification.Mathematicalequationsgov-
LagrangianandEulerianeEulerian erningthefluidflow,heatandmasstransferandchemicalreactionsinfluidizedbedcombustionand
gasifierssystemsaredescribedandmainCFDmodelsarepresented.Theaimistoillustratewhatcanbe
doneandalsotoidentifytrendsandthoseareaswherefurtherworkisneeded.
(cid:1)2012ElsevierLtd.Allrightsreserved.
1. Introduction aredevelopingatfastpaceinthepowergeneratingindustryasthey
combinefuelflexibilityandhighefficiencyespeciallyforbiomass
Fastdepletingfossilsfuels,energysecurityandenvironmental co-combustion.
concerns are demanding effective use of fossil fuels. Due to this Computational Fluid Dynamics (CFD) is an economical and
moreandmoreattentionhasbeenfocusedoncleancoaltechnol- effective modeling tool to study combustion and gasification in
ogies. Among these technologies fluidized bed combustion and fluidized bed. Reliable CFD models are essential for the opti-
gasificationdevicesisoneoftheimportanttechnologieshelpfulin mizationoffluidizedbedunit’sdesign,asitcanpredictinertma-
controllingthegreenhouseemissions. terial concentration in bed, fuel mixing efficiency, temperature
Fluidizedbedcombustorsandgasifiersarewidelyusedinmany profilesofsolidandgaseousphasepresentindensebed,temper-
chemicalandpowerindustriesduetotheirhighheattransferrates, atureprofileoffurnace,heatfluxetc.SimulationwithaidofCFDis
high efficiency, low combustion temperature and low pollutant regarded as one of the most appropriate approaches for the pre-
emissions. Applications of fluidized bed combustors and gasifiers diction of critical parameters required for the control of efficient
operationofsuchinstallations.TheseCFDtechniquesareexpected
tosubstituteempiricalorsemi-empiricalmodelsinlarge-scaleFB
designprocessinnearterm.
* Corresponding author. Johan Gadolin Fellow, Process Chemistry Center, Abo Fluidized bed combustion and gasification is a multiphase
AcademyUniversity,Abo,Finland.Tel.: þ 91(0)1612560327;fax: þ 911612502240. reactive flow phenomenon. It is a multiphase problem between
1 O E- n m E a O il L a ( d w dr it e h s o s: u d t r p .r a j y as l s e a a r v @ e g ) m fro ai m l.c D om epa (R rt .I m .S e i n n t g o h f ). MechanicalEngineering,Guru gases and fuel particles and also a reactive flow problem, which
NanakDevEngineeringCollege,Ludhiana,India. involveshomogeneousreactionsamonggasesandheterogeneous
1359-4311/$eseefrontmatter(cid:1)2012ElsevierLtd.Allrightsreserved.
http://dx.doi.org/10.1016/j.applthermaleng.2012.12.017

Author's personal copy
586 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
Nomenclature m viscosity(kgm(cid:2) 1s(cid:2) 1)
r densityofsolid(kgm(cid:2) 3)
A constant s turbulencePrandtlnumbers
k
A(cid:2) constant s ε turbulencePrandtlnumbers
C 1ε,C 2ε modelconstants s s scatteringcoefficient
C
d
Dragcoefficients s stresstensor(Nm(cid:2) 2)
C
p
specificheatatconstantpressure(Jkg(cid:2) 1K(cid:2) 1) s
tq
torque(Nm)
D differential F scatteringphasefunction
D
gs
diffusionofgas(m2s(cid:2) 1) f
i
instantaneousspeciesconcentrationdensityor
d particlediameter(m) temperature
p
d diameterofsolidparticle(m) u sourcetermforaspeciesi
s
e coefficientofrestitution
f initialvolatilefraction Subscripts
v,0
F force(N) g gas
g gravity(m2s(cid:2) 1) gs gassolid
g radialdistributionfunction i,j xandydirections,respectively
0
G turbulenceproductionterm mf minimumfluidization
k
H0 standardenthalpy(J) p particle
H enthalpy(J) pp particleeparticle
I radiantintensity r radiation
k turbulentkineticenergy(m2s(cid:2) 2) R heterogeneousreactionrate
k
s
granularconductivity(kgm(cid:2) 1s(cid:2) 1) s solidphase
m ashcontentintheparticle(kg) sg solidgas
a
m massofspeciesconcentration(kg)
i
m solidfuelparticlemass(kg) Abbreviations
p
m initialparticlemass(kg) B bubbling
p,0
m (t) volatileyielduptotimet(kg) BFB bubblingfluidizedbed
v
P gaspressure(Pa) BFBG bubblingfluidizedbedgasifier
Q heatExchangebetweendifferentphases(J) C circulating
r,r reactionratesforeddydissipationcombustionmodel CFB circulatingfluidizedbed
1 2
Re Reynoldsnumber CFD computationalfluiddynamics
Nu Nusseltnumber CLC chemicalloopcombustion
s
R universalgasconstant(Jkmol(cid:2) 1K(cid:2) 1) DEM discreteelementmethod
R reactionrateterm DOM discreteordinatemodel
f
!r,!s directions DPM discreteparticlemodel
Sh Sherwoodnumber EBM eddybreakupmodel
S sourceterm EDCM eddydissipationcombustionmodel
S sourceterm EDM eddydissipationmodel
gs
S transferofmassfromreactingparticles EeE EulerianeEulerian
m
t instantaneoustime(s) EeL EulerianeLagrangian
T meantemperature(K) ER equivalenceratio
T referencetemperature(K) FB fluidizedbed
ref
u,v velocity(ms(cid:2) 1) FBC fluidizedbedcombustion
n Instantaneousvelocity(ms(cid:2) 1) GKTM granularkinetictheorymodel
!n 0s solidsfluctuatingvelocity(ms(cid:2) 1) HC hydrocarbons
V volume(m3) LFR laminarfiniterate
w molecularweight(kg/kmol) LES largeeddysimulation
i
Y massfractionofspeciesienteringthefinestructures P pressurized
i
PDF probabilitydensityfunction
Greeksymbols RANS ReynoldsaverageNavierStokes
a volumefraction RDF refusedderivedfuel
b inter-phasedragcoefficients Ref reference
g energydissipationperunitvolume(kgm(cid:2) 3s(cid:2) 1) RNG re-normalizationgroup
g,g yieldfactor RTE radiativetransferequation
1 2
ε dissipationrateofturbulentkineticenergy(m(cid:2) 2s(cid:2) 3) S/B steamtobiomassratio
Q s granulartemperature(ms(cid:2) 2) SCM shrinkingcoremodel
l bulkviscosity(Pas) Sec secondary
s
l
mix
thermalconductivityofmixture(Wm(cid:2) 1K(cid:2) 1) TFM twofluidmodel
m
s
solidshearviscosity(kgm(cid:2) 1s(cid:2) 1) VM volatilematter
m
s,dil
diluteviscosity(kgm(cid:2) 1s(cid:2) 1) VOF volumeoffluid

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 587
reactionsbetweenfuelparticlesandgases.Fluidizedbedforcom- solid volume fraction and quantitative information like tempera-
bustion and gasification reaction consists of solid (fuel), liquid tureprofiles,heattransferandemissions.Mostofstudiesarenot
(fuel), gaseous (fuel), gas (medium) and inert particles. The fuel abletopredicttemperatureprofilesorthegasconcentrationinside
existsinthesolid,liquidorgaseousformintheinertsandparticles the bed quantitatively. Most of quantitative results mentioned in
andthegasifyingagentisairincombustionandsteam-airinthe literatureareusedtostudythetemperatureprofile,heattransferor
caseofgasification.Theinvolvementofmultiphaseflow,combus- emissions of freeboard/riser with EeL DPM model. The EeE TFM
tion and gasification in fluidized bed devices makes modeling of methodisadoptedinmostofstudiesbecausetrackingeachparticle
theseextremelycomplicatedandcontinuestobeachallengetothe with the Lagrangian method is not practical with the current
scientificcommunityandpracticingengineers. computational capacity. Furthermore, the available correlations
MajorityoftheCFDstudiesinliteratureonfluidizedbeddevices describing the interactions between particles and gases in the
inpasthasbeenfocusedonisothermalmodelingofdensebed(Gao Lagrangian method are all limited to a single particle or diluted
etal.[1],Behjatetal.[2],GnanapragasamandReddy[3],Wangetal. particleconcentrationconditionsandtheycan’tbeusedfordense
[4], Chen et al. [5]). CFD modeling to study the combustion and conditioninafluidizedbed.Thereisnoliteraturefoundwhichhave
gasification in fluidized bed is possible due to advancement in consideredtheapplicationofEeETFMwiththermo-chemicalre-
computational technology. Researchers in literature used CFD in actions in dense bed in commercial boilers. There is no paper
studyingemissions,operationalparameters,conversionoffuelsin reported on heat exchange coefficients between solids (i.e. inert
bed and freeboard/riser, ash deposition behavior prediction, ni- material and fuel) in dense beds of commercial fluidized bed
trogenchemistry,calcination,co-firingcoalwithbiomassandnon- boilers.
commercial technologies like chemical looping combustion sys- InthispaperanoverviewofCFDmodelingtostudycombustion
tems. Researcher also tried to use CFD to study fuel, char, ash, andgasificationoffuelsinfluidizedbedsystemsoflasttwodecades
physicalandchemicalbehaviorinfluidizedbed. hasbeendonekeepinginmindtofindnewchallengesinthisfield.
Currently there are three numerical techniques used for the There are no previous review studies related to review of CFD
studyingcombustionandgasificationinfluidizedbedsinliterature modelingoffluidizedbedcombustionandgasification.Theappli-
andtheseareEulerianeLagrangianwithsingleparticleoraparticle cationofCFDmodelingtostudycombustionandgasificationisin
parcelandagroupofparticles,EulerianeEulerianTFMandDiscrete developmentstageanditisimmaturefieldtostudy.Thecommon
ElementMethod(DEMeCFD)withinEulerianeLagrangianconcept. mathematical equations used for studying combustion and gas-
Literature concerning the numerical modeling of fluidized bed ification are explained and qualitative/quantitativeinformation is
combustorandgasifierdevicescouldbedividedmainlyintothree presented.
partsbasedonthegeometricregionsoffluidizedbedfurnace.Itis
densebed,splashzoneandfreeboard/riseroffluidizedbedunits.
1.1. Descriptionoffluidizedbedsystems
Regarding dense bed most of studies is concentrated on gas-
ificationanddonewithEulerianeEulerian(EeE)TwoFluidModel
Whenanevenlydistributedairorgasispassedupwardthrough
(TFM) approach and geometries considered in literature are very a finely divided bed of solid particles such as sand supported on
simple.Fewofthem[6e8]consideredCFDforcombustionofcoalin afinemesh,theparticlesremainundisturbedatlowvelocities.As
circulatingfluidizedbedcombustoroverlookingthree-dimensional
theairvelocityisgraduallyincreased,astageisreachedwhenthe
effects.Onlytwoauthors[9,10]consideredthethree-dimensional individualparticlesaresuspendedintheairstreamandthebedis
or full-scale device geometry to investigate the unit with EeE called “fluidized”. With further increase in air velocity, there is
approachconsideringcombustion/gasificationoccurringinbed.
bubbleformation,vigorousturbulence,rapidmixingandformation
The other CFD technique, i.e. EulerianeLagrangian DPM with ofdensedefinedbedsurface.Thebedofsolidparticlesexhibitsthe
singleparticleoraparticleparcelandagroupofparticlesismostly propertiesofaboilingliquidandassumestheappearanceofafluid
usedinregionabovethedensebed,i.e.freeboardwherethediluted “bubbling fluidized bed”. At higher velocities, bubbles disappear,
particleconditionsarepresent.Tostudyfreeboardinfluidizedbeds
andparticlesareblownoutofthebed.Someamountsofparticles
different authors have touched different aspects. They tried to havetobere-circulatedtomaintainastablesystemandiscalledas
applyCFDtostudycombustionandgasificationissuesofsolidfuels, “circulating fluidized bed”. This principle of fluidization is illus-
theiremissions,operationalparametersandotheraspectslikefate tratedinFig.1.
ofnitrogeninfreeboard[11e14].FewofthemusedCFDtolookthe
Fluidization depends largely on the particle size and the air
flow,temperatureandmainspeciesinthefluidizedbedcombustor
velocity. The mean solid velocity increases at a slower rate than
using their own code and Fluent. Few others tried to look ash
depositionpredictionwiththeuseofCFDincommercialfluidized
bed combustors [15e20]. They found deposition maps in boiler
with high probability of ash positions on boiler surfaces. Many
authors tried to model the freeboard using probability density
approach [21e23]. They considered the fuel to be in gas phase,
burningabovethebed.Thetrackingoffuelparticlesinadiscrete
phase with DPM is done by integrating the force balance on the
particle,whichiswritteninaLagrangianreferenceframe.
Andersetal.[24]formedsimplifiedmodelforthebehaviorof
largebiomassparticlesinthesplashingzoneofabubblingbed.Wu
et al.[25] found thatnewchallenges arise in the fieldof the nu-
merical prediction of hydrodynamic behavior, combustion and
emissions performance in fluidized bed. Most of the literature in
fluidized bed gasification is overlooking three-dimensional be-
haviors(Myöhänen[10]).
The CFD models considering combustion/gasification issues in
fluidizedbedarecapableofpredictingqualitativeinformationlike Fig.1. Principaloffluidization[26].

Author's personal copy
588 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
doesthe gasvelocity. Thedifference betweenthemean solidve- processes.Unfortunately,FMssofardonotconsiderthefullycomplex
locityandmeangasvelocityiscalledasslipvelocity.Maximumslip gas-particledynamicsthatCFDconsiders;however,theystillmain-
velocitybetweenthesolidsandthegasisdesirableforgoodheat tain the multiphase flow dynamics with the inclusion of semi-
transferandintimatecontact.Theproportionofcombustiblema- empirical fluid dynamic correlations for the flow behavior [28] in
terialwithinthebedisnormallyonlyaround5%.Ifsandparticlesin thebed.
fluidizedstateareheatedtotheignitiontemperaturesoffueland Mathematical modeling and simulations are helpful to under-
fuelisinjectedcontinuouslyintothebed,thefuelwillburnrapidly standcombustionandgasificationprocessesdeeplyandtheseare
and the bed attains a uniform temperature. The gas velocity is significantforfluidizationindustry[110]since1960.Severalmodels
maintained between minimum fluidization velocity and particle aredevelopedandimprovedinthelasttwodecades.Focuswasless
entrainmentvelocity.Thisensuresastableoperationofthebedand on three-dimensional models due to more costly computational
avoidsparticleentrainmentinthegasstream.TheglobalFBCca- power.Duetoadvancementincomputersthecomputationalfluid
pacityisgoingtogrowsteeplyinfuture.Fig.2presentsinformation dynamics is being applied on fluidization during the last decade.
available on cumulative number of fluidized devices worldwide. EarlierCFDmodelsneglectedcombustionandgasificationasthese
Fluidizedbed(FB)hasemergedasviablealternativeasithassig- bringsmorecomplexitytothesystem.Thefirstattempttomodel
nificant advantages over conventional firing system. FB offers fluidizedbeddevicenumericallywhichincludesgasificationisby
multiple benefits, such as: compact boiler design, flexibility with KimuraandKojima[29].Jichengetal.[30]alsodidthenumerically
fuel used higher combustion efficiencyand reduced emissions of simulationoffluidizedbedcoalgasifier.Earliernumericalmodeling
noxiouspollutantssuchasSOxandNOx.Thevarioustypesoffuels approachisquitedifferentfrompresentdayCFDmodels.
thatcanbeburntorgasifiedinfluidizedbedsarecoal,coalwashery Thedesiretoanalyze,designandoptimizetheperformanceof
rejects,biomass,refusedderivedfuelsetc. fluidizedbeddevicesimpliesthedevelopmentofmultidimensional
The basic principle of fluidized bed gasification is same as combustorsandgasifiersmodels.Thesemultidimensionalmodels
combustion. The only difference is that gasification is an endo- willbridgethegapbetweensub-scaletestingandtheoperationof
thermalconversiontechnologywhereasolidfuelisconvertedinto fluidizedbedfurnacesbyprovidinginformationaboutcombustion
a combustible gas. The product gas consists of carbon monoxide, and gasification processes that experimental data alone cannot
carbon dioxide, hydrogen, methane, trace amounts of hydrocar- provide.Fig.3showstheframeworkforCFDmodelingoffluidized
bons,waternitrogenandvariouscontaminantssuchascharpar- bedcombustorsandgasifiers.CFDisakindofnumericalsimulation
ticles,ashandtars.Thechemistryinvolvedinconvertingfuelinto that involves the fluid mechanics with numerical methods and
combustible gaseous products is complex, involving a number of algorithmstosolveandanalyzeproblemsthatinvolvefluidflows.
differentreactionswithnumerousintermediatestages.Pyrolysisis The process of modeling of physical and chemical processes in-
thermaldecompositionintheabsenceofair.Itisalwaysfirststep teractions in thermo-chemical conversion of fuels is shown in
before combustion and gasification. Depending upon the type of Fig.4. Fig. 4 shows the interrelation between models involved in
flowthefluidizedbeddeviceshavebeendividedintothreetypes, combustionandgasificationwithotherphysicalmodelsinfluidized
bubbling (B), circulating(C) and pressurized bed (P). From these beds.MyohanenandHyppanen[31]madetheframeworktodis-
three, the pressurized fluidized bed devices are in development tinguishtheCFDfromothermodelingtechniquesusedinfluidized
stage,notmanyindustrialapplicationsaretherepresently.Dueto bedtechnology.Thefundamentalsorientedmicroandmeso-scale
much diversified applications the use of circulating fluidized bed models are not yet capable for practical comprehensive calcula-
combustorsisincreasing. tionsofindustrialscalefluidizedbedunits,includingmodelingof
reactions, attrition of particles, and heat transfer. Fig. 5 presents
a scale-based classification [31] for the most popular model ap-
1.2. CFDmodelingandmultiphaseapproach proaches used for fluidized bed systems. The purpose is to show
roughly the different scales for which the different models are
Combustionandgasificationoffuelsinfluidizedbedhavebeen appliedandtorelatethepresentedsemi-empiricalsteadystate3D
consideredforanumberofdecades.Anearlycomprehensivemath- model to other model approaches. The ranges of space and time
ematicalmodelproducedwasstartingwithsimplifiedchemicalre- scalescannotbeexact,butthegivenvaluesprovidesomeideaof
actionstodetermineemissionpredictions.Thefirstmodel[109]tobe the vast range of different scales, which are encountered when
regarded as a fully complete model, which considers fluidization modeling the fluidized bed systems. The top region of Fig. 5 in-
modeling (FM) and it models the emulsion phase, the bubbles cludesareaforsteadystate modeling.Duetodifferentlong-term
through the mass balance of the drying and devolatilization phenomena (e.g. segregation, fouling, rusting), the real physical
Modeling
1 D Model 3 D Model 2 D Model
Time averaged 3D fluid dynamics
Gas Solid or Gas-Gas or Gas liquid Reactions Solid Solid Interactions Heat Transfer
Fuel mixing Fuel conversion
Combustion,gasification and pyrolysis
Fig.2. Cumulativenumberoffluidizedbeddevicesworldwide[27]. Fig.3. FrameworkforCFDmodeling.

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 589
Gas Phase High Performance,
Large Scale Computing
Turbulent Mixing Scalability
Robustness
Direct numerical simulation (DNS)
Large-eddy simulation (LES) Strong turbulent mixing/reaction rates
Reynolds averaged Navier stokes (RANS) interactions. Coupling between a wide
range of time and length scale
Drag forces
Chemistry
Porosity effect
Turbulence attenuation Heat, mass
Preferential concentration and momentum Heterogeneous chemistry
exchanges Biomass devolatization
Char Combustion
Gas phase chemistry
Multiphase flows
Primary tar decomposition
Secondary tar formation
Collision and friction forces
Polydisperse flows
Evolving particle Reduced order chemical schemes
Lagrangian particle tracking size distributions Tabulation techniques
Eulerian multi fluid approach
Fig.4. Modelingofphysicalandchemicalprocessesinteractionsinthermo-chemicalconversionoffuels[32].
processesareneveractuallysteadystate,iftheobservationtimeis dispersed,secondaryphaseisbelow10e12%,althoughitsmasscan
longenough(e.g.yearsordecades).Thus,thesteadystateisavir- begreaterthanthemassoftheprimaryphase.
tualstate,whichcanbereached[31]onlyinmodels,inwhichthe ThedifferentphasesintheEulereEulerapproachareconsidered
number of affecting variables is limited. The measurements are as inter-penetrating continua, thus introducing phasic volume
always quasi-steady values. The averaged values of transient cal- fractionsascontinuousfunctionsoftimeandspace.Thesumforall
culations are often quasi-steady values because the calculation phasevolumefractionsineachcomputationalcellisequaltoone.
capacitylimitstheaveragingtimes. Conservationlawsareappliedtoeachphaseinordertoobtainaset
Therearethreeapproachesusedforthenumericalsimulationof of equations that is similar for all phases. Constitutive relations
the multiphase flow in literature. They are known as Eulere obtainedfromempiricalinformationmustbeaddedtoclosetheset
Lagrange, EulereEuler approach and Discrete Element Methode ofequations.IntheEulereEulerapproach,therearethreemodels
CFD. In the EulereLagrangian the primary phase is treated as ofmultiphaseflow:thevolumeoffluid(VOF),themixturemodel
continuumbysolvingthetime-averagedNaviereStokesequations. and the Eulerian model. The Eulerian model is only suitable for
The behaviors of the dispersed phases are obtained by following modeling the fluidized bed systems and discussing other models
a large number of the particles, through the calculated primary arenotwithinscopeofthispaper.
phase flow field. Particle trajectories are calculated in the given TheEulerianmodelisthemostcomplexofallmodelsofmul-
intervalsduringtheprimaryphaseflowcalculations.Dispersedand tiphase flow. In this model the additional equations of mass and
primaryphasescanexchangemass,momentum,andenergy.The momentumconservationaresolvedforeachphaseseparately.Any
basicassumptioninthismodelisthatthevolumefractionofthe combination of liquid, gas and solid phases can be modeled. The
Eulerian method of determining the flow field is used for both
primary and secondary phases. The Lagrangian discrete phase
model is based on the EulereLagrange approach where the fluid
phase is treated as a continuum by solving the time-averaged
NaviereStokes equations, whereas the dispersed phase is solved
by numerically integrating the equations of motion for the dis-
persedphase,i.e.computingthetrajectoriesofalargenumberof
particlesordropletsthroughthecalculatedflowfield.
The EeE TFM model can easily be incorporated inpreexisting
CFDcodesandrelativelycomputationalinexpensive.Thismethod
requiresall processes at the particle scale such as drag, collision,
friction forces and heterogeneous chemistry to be included as
phase interaction terms into governing equations. It is less com-
putationally exhaustive in comparison to the DPM Euleriane
Lagrangian method which simulates the individual particle dy-
namics[34e36]andthecompleteLagrangianmodelwhichmodels
bothparticlesandfluidwithaLagrangianapproach.Acombination
oftheEulerianeEulerianmodelandtheEeLDPMmodelisrecently
consideredbyPapadikisetal.[37,38]whereoneortwoLagrangian
biomassparticlesareintroducedtoaEulerianeEulerianbubbling
Fig.5. Scale-basedclassificationofmultiphaseapproachesforfluidizedbed[31]. bedofinertsand.Althoughtheirapproachishighlybeneficialfor

Author's personal copy
590 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
theinvestigationatanindividualparticledynamicscale,thesim- anFBunit,knownasbedmaterial,arefuelash,sorbentsorsome
ulation is limited to up to 5.0s in physical time. Hence, their other non-combustible hot solids; and theyconstitute 95e99.5%
method does not prove to be computationally viable for realistic of thebedmaterial. Assoonas thesolidfuelentersinsidefluid-
industrialreactorswhichcontainfarmorefuelparticlesandrequire ized bed the process drying, devolatilization, combustion or
simulations overa longer period toallowfor the achievementof gasification occurs. The following sub-models will be incorpo-
possiblesteadystateconditionsandthestatisticalconvergenceof rated in basic equations of computational fluid dynamics to
averagedresults[39].Table1showsthesummarizeddescriptionof simulate the actual combustion and gasification processes in
modelsusedforsimulatingdensegasesolidflowincontextofgas- fluidizedbed.
fluidization [33]. More details about this could be referred from
[33]. 2.2.1. Devolatilizationsubmodel
Thedevolatilizationprocessbeginswhenthesolidfuelreaches
a particular level. Many devolatilization [113] models have been
2. MathematicaldescriptionofvariousCFDmodelsinFB
developed in past. One-step global mechanisms and semi-global
units
multi-step mechanisms can be basically distinguished. The sim-
plifiedapproachesdefinedevolatizationrateswithsingleortwo-
2.1. Basicgoverningequations
stepArrheniusreactionschemes.
The details of one-step devolatilization mechanism is shown
Following are basic fundamental equations for mass, mo-
below
mentum,energyandspeciesrespectivelyforgasphase.Theseare
the basic equations of flow for gas phase when combustion and CoalorBiomassorRDF/Volatiles Char/Tar Gases Char
gasification is taking place in fluidized bed. For multiphase flow þ þ þ
these equations could be modified and these are discussed in (2.5)
Section2.5.ThedetailsofthesecouldbereferredfromBakuletal. The reaction kinetic rate (k) can be expressed as single-step
[40]. Arrhenius fashion as k Aexp( Ea/RT) and the devolatilization
Continuityequation rate[41]is ¼ (cid:2)
v
vt r g þ V$ r g! n g ¼ Sg (2.1) (cid:2) d d m t p ¼ k mp (cid:2) 1 (cid:2) f v;0 m p;0 (2.6)
(cid:1) (cid:3) (cid:1) (cid:3)
h (cid:1) (cid:3) i
Momentumequation
HereAandEarenumericalconstantsofreactingsubstances.
v Fortwo-stepArrheniusreactionschemes,thekineticdevolati-
vt r g! n g þ V$ r g! n g! n g ¼ (cid:2) VPg þ V$ mV ! n g þ Sg (2.2) lizationrateexpressionsoftheformproposedbyKobayashietal.
(cid:1) (cid:3) (cid:1) (cid:3) (cid:1) (cid:3) [115]areasfollows:
Energyequation
k A exp E =RT (2.7)
v v t r g Hg þ V$ r g! n gHg ¼ V l g VTg þ S H (2.3) 1 ¼ 1 ð(cid:2) 1 Þ
(cid:1) Specie (cid:3) strans (cid:1) portequ (cid:3) ation (cid:4) (cid:5) k 2 ¼ A 2 exp ð(cid:2) E 2 =RT Þ (2.8)
v
wherek1andk2arecompetingratesthatmaycontrolthedevola-
vt r g Y i þ V$ r g! n gY i ¼ V ð DV ð rY iÞÞþ S Yþ R f (2.4) tilizationoverdifferenttemperatureranges.Thetwokineticrates
weightedtoyieldanexpressionforthedevolatilization[41]as
(cid:1) (cid:3) (cid:1) (cid:3)
t t
2.2. Combustionandgasificationsub-models 1
(cid:2)
f
v;
m
0
v m ð t
p
Þ
;0(cid:2)
ma ¼
Z 0
ð Y 1 k 1þ Y 2 k 2Þ exp 0(cid:2)
Z 0
ð k 1þ k 2Þ dt 1 dt
Thesolidfuelisgenerallyconstitutes0.5e5%byweightofthe (cid:1) (cid:3) @ ( A 2.9)
totalsolidspresentinFluidizedBed(FB).Theremainingsolidsin
Table1 2.2.2. Homogenousgasphasereactions
Classificationofvariousmodelsusedforsimulatingdensegasesolidflowincontext Thesolidfueldevolatilizationandcrackinggasspecieswillreact
ofgas-fluidization[33]. withsuppliedoxidizerandwitheachothersuchaswater-gasshift
Discretebubble Lagrangian Eulerian Dragclosures Industrial reaction.Theheatgeneratedbyexothermicreactionsisimportant
model forbubbles (<10m) for the release of volatiles and ignition of char. The general ho-
Twofluidmodel Eulerian Eulerian Gassoild Engineering mogenousreactionstakingplaceareasfollows.
drag (1m)
closures H 1=2O /H O 242kJ=mol (2.10)
Unresolveddiscrete Eulerian Lagrangian Gas-particle Laboratory 2þ 2 2 þ
particlemodel (Unresolved) drag (0.1m)
closures CO 1=2O /CO 283kJ=mol (2.11)
Resolveddiscrete Eulerian Lagrangian Boundary Laboratory þ 2 2þ
particlemodel (resolved) condition (0.01m)
atparticle CH 4þ 2O 2 /CO 2þ 2H 2 O þ 35:7kJ=mol (2.12)
surface
Moleculardynamics Lagrangian Lagrangian Elastic Mesoscopic
collisionsat (<0.001m) CH 4þ H 2 O/CO þ 3H 2(cid:2) 206kJ=mol (2.13)
particle
surface CO H O/CO H 41:1kJ=mol (2.14)
þ 2 2þ 2þ

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 591
Keeping thespaceconsiderations,hereonly basic and general all the scales of turbulence being modeled. The instantaneous
equationsarediscussed.Thedetailsofthesereactionmechanisms, propertiesintheconservationequationsintomeanandfluctuating
otherswhicharenotmentionedhereandkineticparameterscanbe componentsformedthebasisofRANSequationsas
found in literature [42]. Other models like Laminar finite rate
4 4 4 0 (2.18)
model, Eddy dissipation model, Eddy dissipation concept model ¼ þ
whichcouldbeusedwithhomogenousreactionsonly(forgaseous Theaveragingoftheflowfieldvariablesisusedtoaccountforthe
fuel)andthesecouldbereferredfromRef.[41].Thesearealsonot effects of density fluctuations due toturbulence. More details on
discussed here as the aim of fluidized bed is to burn/gasify solid aboveequationcanbereferredfromVersteegandMalalasekera[52].
fuelsnotgaseousfuels. TheReynolds-averagedapproachisgenerallyadoptedforpractical
engineeringcalculations.ThepresentRANSmodelsusetheBous-
2.2.3. Heterogeneousreactionsub-models sinesqhypothesistomodeltheReynoldsstressesterms.Itisbased
Char is the solid devolatilization residue. Heterogeneous re- ontheorythatanincreaseinturbulencecanberepresentedbyan
actions of char with the gas species is complex process which increase in effective fluid viscosity and the Reynolds stresses are
involve the balancing rate of mass diffusion of the oxidizing proportionaltothemeanvelocitygradientsviathisviscosity.
chemical species to the surface of fuel particle with the surface Inthepresentfluiddynamicsthevariousmodelsbasedonthis
reactionof thesespecieswiththechar.Theoverallrate ofachar theoryareSpalarteAllmaras,Standardkeε,RNGkeε,Realizableke
particleisdeterminedbytheoxygendiffusiontotheparticlesur- ε,keuanditstypes[41].TheReynoldsstressmodel(RSM)closes
face and the rate of surface reaction, which depend on the tem- theReynolds-averagedNaviereStokesequationsbysolvingtrans-
peratureandcompositionofthegaseousenvironmentandthesize, portequationsfortheReynoldsstressesdirectly,togetherwithan
porosityandtemperatureoftheparticle.Thecommonlysimplified equationforthedissipationrate.Thedetailsofabovemodelsand
reactionsmodelswhichconsiderthefollowingoverallreactions: RSMcouldbereferredfromBakuletal.[40].Inmajorityofworks
standardkeε[46]isusedincombustionandgasificationoffuelsin
C þ CO 2 /2CO (cid:2) 172kJ=mol (2.15) fluidizedbeds.
v m m
C 1=2O/CO 122:9kJ=mol (2.16) rk V$ rVk V$ þ tVk G rε (2.19)
þ þ vtð Þþ ð Þ ¼ s þ k(cid:2)
(cid:6) k (cid:7)
C þ T H he 2 O li / ter C at O ur þ e H th 2 a (cid:2) tr 1 ev 3 i 1 e k w J= e m dt o h l echarsurfacereactionsan (2 d .1 th 7 e ) v v tð rk Þþ V$ ð rVε Þ ¼ V$ (cid:6) ð m þ sε m tÞVε (cid:7) þ C 1ε k ε G k(cid:2) C 2ε r ε k 2
kineticrelationshipcanbefoundfromRefs.[43e45]. (2.20)
(b) LESmodels
2.3. Physicalmodels
In the present state NaviereStokes equations which describe
Whenunsteadyortransienteffectsinturbulentreactingflowsare
lawsofmass,momentumandenergyforeachphasefindlimited important,thenlargeeddysimulation(LES)istypicallyrequired.LES
scope in combustion and gasification of fuels in fluidized beds. is an approach that accounts for large-scale turbulent chemistry
interactioninadirectmanner.Largeeddysimulationsarecomputa-
These basic equations need to modify with additional physical
tionalveryexpensiveandarenowbecomingamorepracticalmethod
models or assumptions to fully represent the physical process.
toresolvetemporalandspatialscales.IntheLESmethod,thetransient
There are various physical models those will include turbulence
formsoftheconservationequationsgoverningfluidflow,reaction
models,heattransferwithradiationmodelsandmasstransferand
andheattransferaresolved.Improvednumericalaccuracy,withafine
diffusion etc. In this section only common models are explained
enoughgridandappropriatetimesteparerequiredforLESbecauseit
moredetailedoradvancedphysicalmodelscouldbereferredfrom
isusedtofullyresolvelarge-scalemotions.Onlytheeffectsofsmaller
Bakuletal.[40].
scalesaremodeled.Subgridmodelsarerequiredtocomputetheef-
fects of the small-scale turbulence on momentum, species and
2.3.1. Turbulentflow
enthalpy transport. The development and testing of turbulence
Turbulence plays important role during combustion and gas-
ificationoffuelsinfluidizedbed.Theturbulentflowinfluidization chemistryinteractionmodelsforthesubgridscaleLESmethodsisfar
is characterized by fluctuating velocity of air and particles. The less mature that the steady state methods presented earlier. The
turbulence affects the heat and mass transfer in fluidized beds
applicationofLEStocombustionandgasificationfluidizedbedsisnot
whichplaysimportantroleincombustionandgasificationoffuels foundinliteratureduetocomputationalexpensiveness.Moredetails
in fluidized beds. The solution of equation with turbulence to aboutthesemodelscouldbereferredfromBakuletal.[40].
multiphaseflowwithfullsolutionofthetransportequationsatall
2.3.2. Radiationmodeling
length and time scales is computationally very expensive due to
smallsizefluctuations.Theturbulencemodelsarerequiredtoac-
Theradiationprocessinfluencestheheattransferrateinfluid-
countfortheeffectsofturbulenceoncombustionandgasification ized bed units, which in turn influences combustion and gas-
ification process. The radiative transfer equation (RTE) for an
rather than simulate it directlyin engineeringapplications. Since
the small eddies are not directly simulated so the techniques of
absorbing, emitting, and scattering medium at position !r in the
Reynoldsaveragingandfilteringaregenerallyappliedtotransform direction!s canbewrittenasfollows:
s th u e bs N ec a t v io ie n r s e . Stokes equations. These are discussed in following dI ð ! d r s ;!s Þ þð a þ s s Þ I ð !r;!s Þ ¼ an2 s p T4
4p
s
(a) RANSbasedmodels þ4p s I !r;!s0 F !r;!s0 dU 0
Z
The Reynolds-averaged NaviereStokes (RANS) equations rep- 0 (cid:4) (cid:5) (cid:4) (cid:5)
resenttransportequationsforthemeanflowquantitiesonly,with (2.21)

Author's personal copy
592 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
A semi-transparent medium is considered and the refractive 2.4. DiscreteparticlemodelinLagrangianframeofreference
indexisequaltounity.
Thefollowingmodelsareapplicable. Theflowinfreeboardoffluidizedbedcombustorsorgasifiersis
akindofgasesolidflowwithchemicalreactions.Thefuelparticles
(a) Discreteordinatesmodel; presentinfreeboardareinsolidform.Thehydrodynamicsofthegase
(b) P-1model; solid flowcan beperformed basedonthediscrete particlemodel
(c) Rosselandmodel;and EulerianeLagrangianconcept.Mostofthesimulatedparticlepres-
(d) Discretetransferradiationmodel ents one particle or a particle parcel, a group of particles in this
concept.Inthisapproach,thefluidphaseistreatedasacontinuumby
The details of all these models should be referred from Bakul solvingthetime-averagedNaviereStokesequations,whilethedis-
et al. [40]. The above models could be used in combustion and persedphaseissolvedbytrackingalargenumberofparticles,bub-
gasificationprocessbasedonopticalthicknessaLwhereaiscon- bles, or droplets through the calculated flow field. The dispersed
stantandLisanappropriatelengthscale.TheP-1andRosseland phaseexchangemomentum,mass,andenergywiththefluidphase.
modelsareusefulwhenaL[l.TheP-1modelshouldtypicallybe Inthismodel,thefundamentalassumptionisthateventhoughhigh
used foroptical thicknesses largethan 1. The Rosseland model is massloadingisacceptable,thedispersedphaseoccupiesalowvol-
computationally cheaper and more efficient but should only be ume fraction. During the fluid phase calculation, the particle or
usedforopticalthicknesses largerthan3. The DiscreteOrdinates droplettrajectoriesarecomputedindividuallyatparticularintervals.
model(DOM)modelworksacrosstherangeofopticalthicknesses, This makes the model appropriate for the modeling of spray
but is substantially more computationally expensive than the dryers, coal and liquid fuel combustion, and some gas-particle
Rosselandmodel[41].TheDiscretetransferradiationmodelisalso flows.Thismodelisinappropriateforthemodelingoflowerpor-
usedrarelyasbeingcomputationallyexpensive. tionoffluidizedbedreactors,liquid-liquidmixturesoranyappli-
cation where the volume fraction of the second phase is not
2.3.3. Mixturefractionmodel negligible.Thediscretephasemethodcanbeappliedtotheparticle
The mixture fraction/PDF modeling approach involves the so- flowwhentheparticlephasecanbeconsideredtobesufficiently
lutionoftransportequationsforoneortwoconservedscalars(the dilutethattheparticleeparticleinteractionsandtheeffectsofthe
mixturefractions).Inthisapproach,insteadofsolvingthetransport particlevolumefractiononthegasphasecanbeassumedneglec-
equations for individual species, the individual component con- ted.DuetopresentcomputerefficacytheDPMLagrangeapproach
centrations for a certain species of interest are derived from the is more suitable for industrial size fluidized bed reactors. The
predicted mixture fraction. The basis of the mixture fraction governingequationsusedduringthemodelingstudyinfreeboard
approachisthatunderacertainsetofsimplifyingassumptions,the consisted of mathematical models of the gas phase, particle
instantaneous thermo-chemical state of the fluid is related to movementandreactivechemistry.
aconservedscalarquantityknownasthemixturefraction,f.Being
aconservedscalarquantity,thevalueoffateachpointintheflow 2.4.1. Equationofmotionforaparticle
domainiscomputed[41]throughthesolutionoftheconservation Thecouplingofthecontinuousphaseandthediscretephaseis
equationformean(time-averaged)valueoffintheturbulentflow importantanditissolvedbytrackingtheexchangeofmass,mo-
field,f: mentum and energy. The model computes the particle trajectory
usingaLagrangianformulationwhichincludestheinertia,hydro-
v v m vf dynamicdrag,andtheforceofgravity.Theparticletrajectorycanbe
vx i ð ru i f Þ ¼ vx i s t t vx i!þ S M (2.22) p C r a e r d te i s c i t a e n d c f o o o r r t d h in e a x te i( s i ¼ by 1, [4 2 1 , ] 3 : for three dimensions) direction in
m
va
i
r
x
i
I
a
n tu
n
a r
c
e d
e
d
,
fr
f
i
0
a t
2
i c o
i
t n
s
io
a
n t
l
o
s
,
o
a so
s
c l
o
o v
l
n i
v
n s
e
g e
d
r
:
t v h a e tio co n n e s q e u rv a a ti t o io n n fo e r qu th a e tio m n ix fo tu r r t e h f e ra m ct e io a n n d
d
2
t
x
2
i
¼
F
D
v
i(cid:2)
v
p;i þ
gx
i(cid:1)
r p
r
(cid:2)
p
r
(cid:3)þ
Fxi (2.26)
(cid:4) (cid:5)
v
v
x i(cid:6)
ru
i
f
0
2
(cid:7) ¼ v
v
x i0
m
s t
t v
v
f
x
0 2
i1 þ
Cg m
t v
v
x
f
i!
2
(cid:2)
C
d
r
k
ε f
0
2 (2.23) w pa h r e ti r c e le
1
Fx
8
m i
m
i a s s
C
t s he a
R
n a
e
d dditionalforce,FD(v (cid:2) ivp,i)isthedragforceperunit
Thevaluesofcon @ stantss t A ,CgandCdinEq.(2.23)willbetaken F D ¼ r p d2 p D 24 (2.27)
dependingonsimulationsandsituation,respectively.Ifasecondary
stream is included in a non-adiabatic system, the instantaneous 2.5. EulerianeEuleriantwofluidcomputationalfluiddynamics
valueswilldependontheinstantaneousfuelmixturefraction,fuel,
model
thesecondarypartialfraction,psecandtheenthalpy,H
The EulerianeEulerian method is one of the affordable CFD
f
i ¼
f*
i
f
fuel
;psec;H* (2.24) m
sca
o
l
d
e
el
g
in
as
g
e
a
s
p
o
p
li
r
d
oa
fl
c
o
h
w
es
s
f
y
o
s
r
te
p
m
er
.
f
C
or
o
m
m
i
b
n
u
g
st
s
i
i
o
m
n
u
a
la
n
t
d
ion
g
s
as
o
ifi
f
c
a
a
n
tio
in
n
du
b
s
ri
t
n
ri
g
a
s
l
(cid:1) (cid:3)
morecomplexityintothesystem.IntheEulereEulerapproach,the
HereH*isgivenby:
different phases are treated mathematically as inter-penetrating
continua. The concept of phase volume fraction is introduced in
T this approach. These volume fractions are assumed to be con-
H* ¼
X i 0
m i 0 H i 0 ¼
X i 0
m i 0 2
6
6
Tr Z efi0
Cp þ ho i 0
(cid:1)
T ref i0
(cid:3)
3
7
7
(2.25) t
F
o
i
o
f
n
r
u
e
e
o
q
a
u
u
c
s
a
h
t
f
i
u
p
o
n
h
n
c
a
s
t
s
i
e
w
o
,
n
h
c
s
i
o
c
o
n
h
f
se
s
h
p
r
a
v
a
v
a
c
e
t
e
io
s
a
n
i
n
m
d
e
i
q
l
t
a
u
im
r
at
e
s
i
t
o
a
r
n
u
n
s
c
d
t
a
u
t
r
h
r
e
e
e
d
ir
f
e
o
r
s
r
i
u
v
m
a
e
l
d
l
is
t
p
o
e
h
q
o
a
u
b
se
a
ta
s
l
.
i
t
n
o
T
a
h
o
e
n
s
s
e
e
e
t
.
4 5
MoredetailsaboutsolutioncouldbereferredfromRef.[41]. equations are closed by providing constitutive relations that are

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 593
obtained from empirical information, or, in the case of granular a 1=3 1
( t s h o e li g d e ) n fl e o r w al s e , q b u y a a t p io p n li s ca fo ti r o E n u o le f r k i i a n n e e ti E c u t l h e e ri o a r n y. p B h e a lo se w in m s e id n e ti fl on u e id d iz a e r d e go ¼ (cid:8) 1 (cid:2) (cid:6) a s;m s ax(cid:7) (cid:9) (cid:2) (2.39)
bed with combustion and gasification. Details of these could be Equivalent to the thermodynamic temperature for gases, the
referredfrom[28,39,47]. granular temperature can be introduced as a measure for the
fluctuating kinetic energyof theparticles. The granular tempera-
2.5.1. Continuityequations tureQ s isdefinedas
1
v Q s ¼ 3 n! 0s 2 (2.40)
vt
(cid:1)
a g r g
(cid:3)
þ V$
(cid:1)
a g r g! n g
(cid:3)
¼ Sgs (2.28) where!n (cid:11)
0s
isthesolidsfluctuatingvelocity.
Theequationofconservationofthesolidsfluctuatingenergyis
v
vtð a s r sÞþ V$ a s r s! n s ¼ Ssg (2.29) givenas
Ssg ¼ wc g (cid:1) c Rc ¼ (cid:3) (cid:2) Sgs (2.30) 3 2 (cid:8) v v tð a s r s Q Þþ V$ (cid:1) a s r s! n s $Q (cid:3)(cid:9) ¼ (cid:2)ð PsI þ a s s s Þ
Forthe X gasphasedensity,amixtureofidealgas :V ! n s V$k s VQ g (2.41)
þ (cid:2)
P where PsI a s s s :V ! n s isthegenerationofthefluctuatingenergy
r g ¼ RT n i 1w Y i (2.31) d th u e e c t o o n ð w du o c r t þ k io d n o o n f e Þ th by efl sh u e c a tu r a s t t i r n e g ss en in er t g h y e ; p g a i r s t t i h cl e e r p a h te as o e f ; d V is $ s k ip s V at Q io i n s
¼ i ofthefluctuatingenergyduetoinelasticcollision.
P
The granularconductivity k s and thecollisional rateofenergy
dissipationperunitvolumegareadoptedas:
2.5.2. Momentumequations
2k 6 2 Q 1=2
v v t a g r g! n g þ V$ a g r g! n g! n g ¼ (cid:2) a g VPg þ Va g $s g þ a g r g g k s ¼ ð 1 þ d e i Þ l go(cid:8) 1 þ5ð 1 þ e Þ go a s (cid:9) þ 2a2 s r s ds (cid:6) p (cid:7) (2.42)
(cid:1) (cid:3) (cid:1) (cid:3) þ b ! n s (cid:2) ! n g þ Sgs! n s k dil ¼ 7 3 5 8 p 4 p r s ds Q1=2 (2.43)
ffiffiffi
(cid:1) (cid:3) (2.32) 4 Q 1=2
v v t a s r s! n s þ V$ a s r s! n s! n s ¼ (cid:2) a s VPs þ Va s $s s þ a s r s g g ¼ Th 3 e (cid:1) d 1 ra (cid:2) g e b 2 e (cid:3) tw a s e r e s n go g Q as (cid:8) p d h s(cid:6) as p e (cid:7) ands (cid:2) o V li $ d ! n p s h (cid:9) aseistoplayimp ( o 2 rt .4 a 4 n ) t
(cid:1) (cid:3) (cid:1) (cid:3) roleinthemomentumexchange.
(cid:2) b ! n s (cid:2) ! n g þ Ssg! n s ð 2:33 Þ Fora 0.8,thedragcoefficientiswasgivenbasedonthework
(cid:1) (cid:3) byGidasp (cid:3) ow[50]
Intheaboveequationsthestresstensors gands sisgivenby
a r n n
s g ¼ m g V ! n g þ V ! n g T (cid:2) 2 3 a g m g V ! n g (2.34) b ¼ 3 4 C d s s (cid:12) (cid:12) ! d g s (cid:2) !s (cid:12) (cid:12) a (cid:2)g 2:65 (2.45)
h (cid:1) (cid:3) i (cid:1) (cid:3) (cid:12) (cid:12)
s s ¼ m s V$ ! n s þ V$ ! n s T (cid:2) 2 3 m s V$ ! n s þ l s $V$ ! n s (2.35)
where
2
th
4
edragcoefficientCdisgivenby
Here
h
l sisbulk
(cid:1)
visco
(cid:3)
sit
i
y,itisba
(cid:1)
sedon
(cid:3)
expressiongivenbyLun
C
d ¼ Res
1
þ
0:15Re0
s
:687 forRes
(cid:4)
1000 (2.46)
etal.[48]anditcanbeobtainedas (cid:1) (cid:3)
l s ¼ 4 5 a s r s dsgo ð 1 (cid:2) e Þ Q p s 1=2 (2.36)
C
d ¼
0:44; forRes
(cid:3)
1000 (2.47)
Forthecollisionalan (cid:6) dki (cid:7) neticeffectsthecoefficientofrestitu- Res ¼ a g r g ds m(cid:12) ! n g (cid:2) ! n s (cid:12) (2.48)
(cid:12)g (cid:12)
tionwasintroducedbyJenkinsandSavage[49]andtheequationof (cid:12) (cid:12)
solidshearviscositym s For a<0.8, the well known Ergun equation[51] is suitable for
describingthedenseregime
m ;dil 4 2 4 Q 1=2
m s ¼ ð 1 þ s e Þ go(cid:8) 1 þ5ð 1 þ e Þ go a s (cid:9) þ5 a2 s r s ds ð 1 þ e Þ go (cid:6) p (cid:7) (2.37) b ¼ 150 (cid:4) 1 (cid:2) a g a d g 2 s(cid:5) m g þ 1:75 r g a s (cid:12) (cid:12) ! n d g s (cid:2) ! n s (cid:12) (cid:12) (2.49)
(cid:12) (cid:12)
2.5.3. Energyequation
5pp
m
s
;dil
¼ 96
r
s
ds Q1=2 (2.38)
ffiffiffi
v
wherem s,dilisthediluteviscosityandgoistheradialdistribution vt a g r g Hg þ V$ a g r g! n gHg ¼ V l g VTg þ Qgs þ SgsHs
function expressing the statistics of the spatial arrangement of (cid:1) (cid:3) (cid:1) (cid:3) (cid:4) (cid:5) (2.50)
particles.Thefollowingexpressionsareused:

Author's personal copy
594 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
v
vtð a s r s Hs Þþ V$ (cid:1) a s r s! n sHs (cid:3) ¼ V ð l s VTs Þþ Qsg þ SsgHs (2.51) v v t a g r g! n g þ V$ a g r g! n g! n g ¼ (cid:2) a g Vpg þ V$ a g s g þ a g r g g
Thethirdtermontheright-handsideoftheexpressionisthe (cid:1) (cid:3) (cid:1) (cid:3) Sm (cid:4) (cid:5)
heattransferinthatthesolidphasechangedintothegasphase. (cid:2)
(2.59)
Qsg Qgs (2.52) wherer gisthegasdensity,s gthegasviscousstresstensor,Sgthe
¼ (cid:2) gas mass source due to heterogeneous reactions, Sm the gas mo-
mentumsourceduetointer-phaseinteraction.Fordensegasesolid
Qsg
¼
hsg Ts
(cid:2)
Tg (2.53) flowsinfluidizedbeds,two-waycouplingisrequired.Accordingto
(cid:4) (cid:5)
Newtonianthirdlaw,Sminafluidcellisdeterminedbyaddingup
hsg
¼
6kg a
d
s a
2
gNus (2.54) thedragforceoftheparticleslocatedinthefluidcell.
p
1
Np
HereNusisproposedbyGunn[51]
Sm
¼ V
cell k 1
F
d
(2.60)
X¼
where Vcell is the volume of the fluid cell. In the hydrodynamic
2.6. DiscreteelementmethodeCFDwithinEulerianeLagrangian DEMeCFDmodel,SginEq.(2.60)issettozero.Whenitisextended
model tomodelofthermo-chemicalconversionoffuelingasesolidsys-
temsinvolvedwithheterogeneousandhomogenousreactions,Sg
Adiscreteelementmethod(DEM)isafamilyofnumericalmethods shouldnotbezero.
for computing the motion of a large number of particles of
micrometer-scalesizeandabove.IntheDEMeCFDmodel,eachindi- 2.6.2. Heattransfer[53]
vidualparticleistrackedandgasphasedynamicissolvedbyNaviere Theheatbalanceforanindividualparticleisgivenbelow:
Stokesequations.DEMisverycloselyrelatedtomoleculardynamics,
t
d
h
e
e
gr
m
ee
e
s
t
-
h
o
o
f-
d
fr
i
e
s
e
g
d
e
o
n
m
er
a
a
s
ll
w
y
e
d
l
i
l
s
a
ti
s
n
s
g
t
u
at
is
e
h
fu
e
l
d
co
b
n
y
ta
it
c
s
t
i
a
n
n
c
d
lu
o
s
f
i
t
o
e
n
n
o
c
f
om
ro
p
ta
li
t
c
i
a
o
t
n
e
a
d
l m
i
C
p;i
d
d
T
t
i
¼
Qgp
þ
Qpp
þ
Q
radþ
Q
R
(2.61)
geometries.Thesedayswitharapiddevelopmentofcomputertech-
nologyandthenumericaltoolDEM(discreteelementmethod),anew where Qgp, Qpp, Qrad and QR represent gas-particle convective,
eraofresearchongasesolidheterogeneousreactionsystems,com- particleeparticle conduction, radiation heat transfer, and hetero-
bustionandgasificationisabouttocome.Thefollowingsectiondeals geneous chemical reactions, respectively. The conservation equa-
brieflywithbasicmathematicalequationsinvolvedinDEMeCFD. tionforthegasenergyis
v
2.6. I 1 n . t H h y e d D ro E d M yn e a C m F i D cs m of o D de E l M , e e a C c F h D in m d o iv d i e d l u [ a 5 l 3] particleistrackedby vt a g r g CpgTg þ V$ a g r g Cpg! n gTg
Newtonian equation. For each particle, the linear and angular ¼
(cid:1) V$ a gkg V(cid:3) Tg
þ
(cid:1) S
Q;cvþ
S
Q;Rþ
(cid:3) S
h
(2.62)
momentumequationsare (cid:4) (cid:5)
where Tg is the gas temperature, Cpg the gas capacity, kg the gas
dv N thermal conductivity, SQ,cv the heat source due to gas-particle
m
idt
i
¼ (cid:2)
V
i
Vpg
þ
F
dþ
Fg
þ
F
ij;nþ
F
ij;t
(2.55) convectiveheattransfer, SQ,R theheatsourceduetochemicalre-
j
X¼
1
(cid:4) (cid:5)
actions,ShtheheattransportedbymasssourceofSginEq.(2.58).
SQ;cviscalculatedinasimilarwayofSminEq.(2.62),
I i d d w t i ¼
j X¼
N
1(cid:1)
s tq ij
(cid:3)
¼
j X¼
N
1 (cid:4)
R j n ij(cid:5) F ij;t
(cid:5)
(2.56) Sm
¼ V c
1
ell k
Np
1
Qcv (2.63)
X¼
whereirepresentsasingleparticle,jtheparticlescontactedwith SQ;R is determined by heat release of chemical reactions. Sh is
particle i, m, V, I, R, v and w the particle mass, volume, inertia determined by the formation enthalpies carried along with the
moment,radius,linearvelocity,andangularvelocityrespectively, inter-phasetransferredmassofSginEq.(2.58).AlthoughDEMeCFD
Vpg thelocalpressuredrop,Fdthedragforce,Fgthegravitational has disadvantages like the maximum number of particles and
force, Fij,n and Fij,t the normal and tangential components of the durationofavirtualsimulationislimitedbycomputationalpower.
contactforcefromparticlejtoi,andtorques tq .Thecontactforceis Typicalflowscontainbillionsofparticles,butcontemporaryDEM
ij
calculated according to a linear spring-dashpot model where the simulations on large cluster computing resources have only
forceisafunctionofparticleoverlapandrelativevelocity.Thedrag recentlybeenabletoapproachthisscaleforsufficientlylongtime.
force,FdinEq.(2.55),iscalculatedby Moredetailscouldbereferredfrom[53,114].
Vb
F i u v (2.57)
d ¼ 1 a g ð (cid:2) iÞ 3. Combustionandgasification
(cid:2)
where (cid:4) uisthe (cid:5) localgasvelocity,a gthelocalgasvolumefraction, Therearetwokindsofsolidfuelsgenerallyincineratedorgasified
andbinter-phasemomentumtransfer.Thegasphaseistreatedas influidizedbed.Thiscouldbedividedintononrenewable(coal)or
continuumanddescribedbythevolume-averagedNaviereStokes renewable(biomass/RDFfuels).Thefuelcouldbecharacterizeddueto
equations.Massandmomentumconservationsare itsphysicalpropertieslikebulkdensity,particlesizeorpelletdura-
bility,togetherwithmoisturecontent.Assoonitentersreactoratfirst
v
vt a g r g þ V$ a g r g! n g ¼ Sg (2.58) i z t a d ti r o i n es s a t n ag d e t . h T e h n e th re e l r e e as is ed rel v e o a l s a e til o e fv m o a la tt t e il r e u m n a d t e te rg r o c e a s lle h d om de o v g o e l n at o i u li s -
(cid:1) (cid:3) (cid:1) (cid:3)

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 595
oxidation,whereastheremainingcharwillundergoesheterogeneous coldspotsinbed.Thebasicapproachinpredictionoftemperature
reactionsinbedorabovethebed.Theremainingpartisashanditwill in for coal and biomass/RDF is same. The study presented by
beremovedthroughdrainorthroughfluegas.Thestagesincom- Agraniotis [23] has not considered all stages of combustion, i.e.
bustionandgasificationprocessareshowninFig.6.Therearetwo drying, devolatilization, char combustion process as they have
main regions of fluidized bed unit dense bed or freeboard/riser. considereddriedfuelenteringincombustor.AtpresentMuelleret
EulerianeEulerianTFMCFDmodelalongwithchemistrymodelsare al.[15]andWangandYan[54]haveconsideredallstagesofcom-
used in literature to model solid fuel particles in dense bed. The bustiontopredict thetemperatureprofilesinfluidizedbedcom-
NaviereStokescoupledwithenergyasexplainedinSection2willbe bustors. Ravelli et al. [21] used two-mixture fraction approach to
used to modelthe process. CFD modelingofcombustion and gas- predictcorrecttemperature.Thefollowingsectiondealswithdif-
ificationofsolidparticlesinfreeboardusingdiscreteparticlemod- ferentstagesofcombustionoffuelsinsidefluidizedbed.
elingandtrackingofparticleisdoneusingLagrangianapproachas
explainedinSection2.PresentapproachusedbyCFDmodelersin 3.1.1.1. Devolatilization. Devolatilization is the process where
modeling combustion/gasification of fuel in freeboard in fluidized awiderangeofgaseousproductsisreleasedthroughthedecom-
furnacesissameinpulverizedfurnaces.ThemaindifferenceinCFD position of fuel. The volatile matter (VM) comprises a number of
modelingofcombustiongasificationoffuellies indense bed.The hydrocarbons which are released in steps. Devolatilization is in-
reviewofcombustionandgasificationprocesswithCFDmodelingis termediatestepbeforecombustionofparticleinfluidizedbed.CFD
doneinfollowingsections. model is able to predict this stage correctly. Presently devolatili-
zationisnotvalidatedinrealfluidizedbedcombustors.Onlyfew
authors have studied devolatilization of solid fuel particles in
3.1. Combustion
freeboard,althoughtheiraimistostudydifferentfuelsortovali-
datetheirnumericalmodel.Muelleretal.[15]andRavelietal.[21]
Combustion is an exothermic oxidation process occurring at
haveusedCFDtoformulatenumericalmodelofpeat-forestresidue,
a relatively high temperature. The time of reaction, temperature Refused derived fuel (RDF) respectivelyin bubbling fluidized bed
requiredforsustainingthereactionandbettermixingoffuelwith
combustors.Ravelietal.[21]showedthatthecomparisonbetween
oxidantarethreemajorrequirementofagoodcombustionprocess. thedevolatilizationandthecharburnoutprofilesattheentryports
ThesethreerequirementsareadequatelymetinanFBcombustor,
level, whichshowed thatdevolatilizationwasstartingaftershort
whoseexcellentinternalandexternalrecirculationofhotsolidsat
timewhenthefuelisinjected.ThefragilestructureoftheRDFand
the combustion temperature provides a long residence time and
its high intrinsic reactivity favor the fast activation of the homo-
adequatetemperaturetothefuelparticles.Thehighdegreeofgas
geneous combustion of volatiles (Fig. 7(a)). Fuel particles are
solid mixing in the FB furnace also provides the turbulence
expected to be broken into small fragments immediately after
necessary for good combustion. The stages of combustion have
feeding: since a small particle is burnt fasterthan a bigone, this
beendiscussedwiththeaidofCFDbymanyauthors.Instudying
would acceleratethe emission of volatile fromRDF. Fixed carbon
combustionoffuelinthedensebedtheinitialtimeistaken,where
combustionbeginsafterdevolatilizationandtakesplaceindiffer-
as in freeboard the real time is taken by many studies. In all of
ent freeboard zones by varying the furnace operating conditions.
studiesreportedthekeεturbulencemodelisused.
Fig.7(b)showsthatdevolatilizationtakesplaceintheregionclose
tothefurnaceexit whileitis confined totheareajustabove the
3.1.1. Physicalandchemicalprocesses bed.Consequently,inthefirstcase,alowpercentageofthefuelcan
Present CFD models can be used to study the physical and
be entrained to the furnace exit before the oxidation process is
chemicalprocessesoccurredduringcombustionoffuelinfluidized
completed.Thetwocasesonlowloadandhighloadincommercial
bed. The stages during combustion process can be studied with
combustorhavebeenshowninpicture.Theliteraturerevealsthat
different CFD models. The first step to initiate the combustion
devolatilization depends on fragile structure, intrinsic reactivity,
processisheatthefuelparticlesuptothetemperaturerequiredfor
size,temperatureanddensityofpropertiesofparticles.Ifthepar-
combustionprocess,whichisdeterminedandvalidatedbyvarious
ticles are less fragile, intrinsic reactivity is low, size is large and
authors.DuetothelimitationofthepresentCFDcodes(whichdid
denserthenthe chancesofchardevolatilization occurs inbed or
not allow for simultaneous modeling of burning particle (EeL duringflightfromfuelchutesasshowninFig.7(b)and(c).Tostudy
approach) andbubbling bed (EeE TFMapproach)),it isgenerally
devolatilizationbehaviorMuelleretal.[15]andRavellietal.[21]
assumedinallstudiesthattheheatrequiredtoinitiatethecom-
haveusedKobayashimodel.
bustion of biomass/RDF particlesis provided bythe fluidizing air
entering at the combustion temperatures. The Lagrangian phase
3.1.1.2. Char oxidation/burn out. The devolatilized fuel known as
and DPM method is applied by [15,21,23,24,54] few authors to
char burns slowly and it takes time depending upon intrinsic
studyvariouspropertiesoffuelsinBFBunits.Asthetemperatureis
reactivityandsizetoburncompletely.Thereischancethatsome
importantparameterthataffectscombustionprocess,thecorrect
particlewillnotburninbedbeforeleaving.Thelightparticleslike
prediction of it is very important for correct CFD model. Present
ricehuskwillburnduringtrajectory.Thecharoxidationandchar
CFDsimulationspredict thetemperature successfully in fluidized burn out profiles are difficult to study in dense bed due to com-
bedcombustors,butatthesametimesitfailstoanswerthehotand
putationallimitationsandduesurroundingofcharparticlebysand
particle.Withpresentcomputationalapproachitiseasiertostudy
charoxidation in freeboard of commercial as well lab scale units
with discrete particle model Lagrangian approach. The char burn
outisdifficulttovalidateinrealcombustorsanditisnotvalidated
inanyofstudies.Inmostofstudiestheaimisnottostudythechar
burn out rather tovalidatethe CFD model. The charoxidation of
RDF fuel [21] in commercial combustor is shown in Fig. 8(a).
Fig.8(a)showsthatcharcombustiontakesplaceintheregionclose
to the furnace exit in case of minimum load, while in case max-
Fig.6. Stagesincombustionandgasificationprocess. imum load it is confined to the area just above the bed.

Author's personal copy
596 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
Fig.7. (a)FractionsofDPMvolatilizations[21].(b)Devolatilizationofpeat.(c)Devolatilizationofforestresidue[15].
Consequently,inthefirstcase,alowpercentageofthefuelcanbe maximumchartemperaturewas50 5 Chigherthantheaverage
(cid:6) (cid:7)
entrained tothe furnace exit before the oxidationprocess [21] is temperature,whichisdeterminedbynearbyoxygenconcentration
completed.Intheminimumloadcondition,thetemperatureofthe and the heat transfer and the heat transfer properties of their
fluegascomingfromthebed(971.2K)isnothighenoughtorapidly surroundinggasandparticles.Daoyinetal.[53]simulatedcharand
ignite combustion thus fuel particles may be elutriated from the propane combustion in a fluidized bed by extending DEMeCFD
furnace,reducingitsefficiency.Onthecontrary,inmaximumload, approach. The model predicts that the gaseous fuel reduces the
the temperature of the flue gas coming from the bed (1078.5K) char combustion rate and this effect is more predominant with
causesallthefueltobeburnt.Forthelightweightparticleslikerice higher bed temperatures or highly reactive chars. The char com-
husk[22]thecharoxidationandcombustionwilltakeplaceduring bustionrateinbeddecreasesasthetemperaturerises.Thesimu-
trajectoryforthecaseofricehusk[22]asshowninFig.8(c)and(d). lation results shows the local heat source generated from the
InthecaseofdensebedinpresentcontextEeETFMandDEMe homogeneousreactionsfluctuateswithgasvolumefraction,indi-
CFD is used to formulate char combustion model. DEMeCFD to catingthegasreactionishighlyrelatedwithbubbles,whichagrees
formulate char combustion model in dense bed is done by Geng withtheopticalmeasurementsbyZukowskietal.[57].
andChe[55],RongandHorio[56]andDaoyinetal.[53].Rongand GengandChe[55]proposedaDEMeCFDforcombustionofchar
Horio[56]areamongfewwhousedDEMtosimulatethecharin inbubblingfluidizedbedofinertsand.Theypresentedanewchar
bubbling fluidized combustor. They took the fluctuations of char combustion sub model as shown in Fig. 8(b) considering sand
particle temperature into account to effect the particleeparticle inhibitoryeffectstodevelopanddescribecharparticlecombustion
heatconduction,particlegasheatconvection,radiationandcom- behaviorinthefluidizedbed.Theeffectsofbedtemperature,ox-
bustion.TheyfoundthatNOemissionsaregreatlyaffectedbythe ygen concentration and superficial velocity on char combustion
temperature of burning char particles. Later they concluded that behaviorare also examined through model simulation. The pres-
char temperature fluctuated at a frequency of 5e7Hz and the ence of the inert particles has shown significant effects on the

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 597
Fig.8. (a)FractionsofDPMburnout(%)[21].(b)Charcombustionmodelinfluidizedbedswithinertsandparticles[55].(c)CharfractionofaburningricehuskparticleinModelIII
(Oneofcases)[22].(d)CharfractionofburningricehuskparticleinModelIV[22].
processofheatandmasstransferandcharcombustioninfluidized meltingbehavior,afuelfieldstudiesandtheoperationalsetupof
beds. theboilerserveasboundaryconditionsfortheCFDcalculations.In
In studies reported above the freeboard is modeled by DPM thesecalculations,thephysicalandchemicalprocessesoccurringin
Lagrangian approach and char combustion in bed is modeled by thefreeboardregionofabubblingfluidizedbedcombustor-starting
DEMeCFD approach. The char combustion or oxidation is influ- fromthebeduptothefirstheatexchangerunit-arepredictedinthe
encedbybedhydrodynamics,individualparticletemperature,char formofcontinuousphaseandashparticletrajectorysimulations.
residencetimeandconcentrationsoftheproducts. Theexactpositionsofashparticleimpactontheboilersurfacesare
recordedandtheparticletemperaturesattheselocationsarethe
3.1.1.3. Ash behavior. CFD modeling is used in locating the ash linkingparametertothefuelspecificstickinesscriterion.Thepre-
deposition region in the fluidized bed combustors. Biomass mix- dicted locations of high ash depositionprobability on evaporator
tures currently used in heat and power production are, despite and heatexchanger surfaces are compared qualitatively with ob-
their environmental and economical advantages, also combined servationsmadeintheboilerandverygoodqualitativeagreement
with ash-related operational problems, such as slagging, fouling, is found. The chemical fractionation and the thermodynamic
andcorrosion.Toimproveboilerefficiency,reliableashdeposition equilibrium calculations deliver highly reliable data for the ash
predictionisessential.Ash-relatedproblemsarestronglydepend- meltingbehaviorofdifferentbiomasses.Thestrongdependenceon
entonfuelspecificaspects,suchasthemineralmatterdistribution thebiomasscompositionwouldcausetherelevantstickytemper-
inthefuel,agentsspecifictotheusedcombustiontechniqueaswell ature of an ash and it could be varied from 850 to 1000K. The
as design aspects unique for the combustion chamber of any higher temperature regions in furnace are found with help from
operating power plant. The overall goal in combustion related CFD. As shown in Fig. 9 the hot regions with red in color are
researchisthereforethepredictionofpotentialoperationalprob- responsible for ash prediction in fluidized bed furnace. In all of
lems originating from fuel streams entering the combustion studies reported, the basic methodology of ash prediction using
chamberaswellasthoseoriginatingfromfuelstreamsaswellas CFD remains same. But to illustrate the conceptof CFD, different
thoseoriginatingfromthedesignofindividualfurnaces.Theslag- fuelsanddifferentfurnacesareused.
gingandfoulingtendenciesofboilersusingCFDarediscussedby
authors[16e20,58,59]. 3.1.1.4. Particle trajectories. The CFD model computes the particle
Theexperimentalinvestigationsoftheoriginalfuelsprovidethe trajectory using a Lagrangian formulation which includes the
compositionoftheashformingelementsinthebiomass.Theseash inertia, hydrodynamic drag, and the force of gravity. The trajec-
specific data can be used as input for advanced thermodynamics toriesofparticlesdeterminedwillonlybepossibleinfreeboardas
equilibriumanalysisleadingtoadetaileddescriptionof thetem- theparticleconcentrationisquitelesscomparetogas.Whereasin
perature dependent melting behavior of the ash. Based on this the dense bed, with DPM Lagrangian approach and with present

Author's personal copy
598 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
800-1000 (K)
1000-1200 (K)
1200-1400 (K)
1400-1600 (K)
1600- (K)
Fig.9. Visualvalidationofashdepositpredictioninthefreeboardofabubblingflu-
idizedbedfurnace.
computational power it is not possible to track the particle as
concentrationofparticlesindensebedisquitehighascompareto
gas.Theparticletrajectorywillbedependingonsize,densityand
moisturecontentintheparticle.Thehistoryofeachsingleparticle
can be tracked both qualitatively and quantitatively. The trajec-
toriesofparticlescanbeplottedbyselectingthedesirednumberof
streams. Besides, the DPM report gives information about the
averageresidencetimeofthefuelparticlesinthefreeboardandthe
combustion efficiency: both greatly differ from case to case. As
these particles are denser and contain more moisture these will
vanishinbedinsteadinfreeboard.Theashparticleshoweverwill
beejectedoutoffurnace.
3.1.2. Fuelsingaseousphase
Thecombustionofgaseousphasefuelsinfluidizedbedelimi-
nates the heterogeneous reactions. It makes the system easier to
studyduelesscomputationalspace.Thereareonlyafewnumberof
researchpapersfoundoncombustionofgaseousfuelsinfluidized
bed. Fluidized bed technology is used mainly for incinerating or
gasifyingsolidfuels.Thecombustionofgaseousfuelsinfluidized
bedhasbeendiscussedinchemicalloopcombustionsystemsusing
CFDastool.Therearefew[53,60]whohavealsodiscussed com-
bustionofgaseousfuelsinfluidizedbedusingCFD.Mostofstudies
performed in this section are on two-dimensional geometries.
Despite advances in computational studies, some technical chal-
lengesstillneedtobesolvedtoenableittobeapplicabletolarge- Fig. 10. (a) Outline of interconnected fluidized bed chemical looping combustion
scaleindustrialprocesses. systems[68].(b)ContourplotsofmassfractionofCH4inthefuelreactor[68].
Chemical looping combustion (CLC) typically employs a dual
fluidized bed system (circulating fluidized bed process) where
ametaloxideisemployedasabedmaterialprovidingtheoxygen fluidized bed operated as the fuel reactor in combination with
for combustion in the fuel reactor. The reduced metal is then ahighvelocityriseroperatedasairreactorasoriginallyproposed
transferredtothesecondbed(airreactor)andre-oxidizedbefore by[65].Intensiveresearchhasbeenperformedoverthepastdec-
being reintroduced back to the fuel reactor completing the loop. adeinvolvingchemicalloopingcombustion[67],butitisstillaway
Theprocessofchemicalloopingcombustionmaybeutilizedwith from being a commercially available technology. Many authors
eithersolidorgaseousfuelsinvolvingstatic[61,62],moving[63,64] [68e73] studied chemical looping combustion in fluidized beds
or fluidized beds [65,66] in which the oxygen necessary for the usingEeETFMCFD.ThestudiesreportedusedCFDforfuelreactor
combustion is provided by a solid carrier. A basic outline of the mainly.
process is shown in Fig.10(a). Two steps are required: an initial Thedevelopmentandtestingofaninterconnectedmultiphase
oxidation and a subsequent reduction step of the oxygen carrier. CFDmodelforchemicalloopingcombustionisdonebyEmdenetal.
Currentlyimplementedsystemsaremostlybasedonthefluidized [68]. The air reactor is modeled as a high velocity riser, the fuel
bed technology due to the fact that solid fuels are addressable, reactorasabubblingfluidizedbed.Themodelsofbothreactorsare
agoodmixingofgasandsolidcarrierisprovidedandthecircula- implementedasseparateCFDsimulationsallowingforanexchange
tion and replacement of the carrier material become easy. The of solid mass through time-dependent inlet and outlet boundary
processisusuallyrealizedthroughthecombinationofabubbling conditionsaswellasmass,momentum,heatandheatsinksplaced

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 599
in thebubbling bedequipped withaweir. Thedeveloped frame-
workistestedforchemicalloopingoperatedwithmethaneasfuel
gasandMn3O4asoxygencarrier.Fig.10(b)showsthecontourplots
of CH4 in the fuel reactor. The simulation could not capture the
unexpected increase in methane conversion with an increase in
fuel injection rate. This counter-intuitive trend was explained by
notingthatthereactionrateexhibitedbytheparticlesissorapid
that the global reaction behavior was completely limited by the
species transfer in the particle lean regions towards the gas-
emulsioninterface.
Wang et al. [70] did the CFD simulation of fuel reactor in
chemical looping combustionprocess using TFM and GKTM. It is
foundduringsimulationoffuelreactorthatahighweightfraction
ofunburnedmethanefuelinthefluegasalongwithCO2andH2O.
Thisbehaviorimplieshighfuellossattheexitof thereactorand
indicatesthenecessitytoincreasetheresidencetimeandimprove
mixinginthefuelreactorusingcirculatingfluidizedbedtechnol-
ogy. Deng et al. [71,74,75] used multiphase CFD modeling for
achemicalloopingcombustionprocess.Inthiswork,thereaction
kinetics models of the (CaSO4 H2) fuel reactor are developed.
þ
Denget al. [71] applied multiphase CFD modeling fora chemical
loopingcombustionprocess(FuelReactor).Theyalsostudiedeffect
of various parameters on performance along with validation of
model. They checked the effect of various parameters like bed
temperature,particlediameter,flowrateetc.Fig.11(a)showsthe
effect of particle diameter on molar fraction of H2 and Fig.11(b)
displaystheeffectofbedtemperatureontheconversionofH2.Itis
observed that the conversion of H2 increases at higher tempera-
tures and decreases with particle size. Mahalatkar et al. [72] has
made simulations of a circulating fluidized bed chemical looping
combustionsystemutilizinggaseousfuel.TheCLCexperimentsare
simulatedusingmethaneasfuel.A2-Dcontinuummodelwasused
todescribeboththegasandsolidphases.Detailedsub-modelsto
accountforfluid-particleandparticleinteractionforcesareinclu-
ded.Globalmodelsoffuelandcarrierchemistryareutilized.The
resultsobtainedfromCFDarecomparedwithexperimentaloutlet
speciesconcentrations,solidcirculationrates,solidmassdistribu-
tioninthereactors,andleakageanddilutionrates.Thetransient
CFD simulations provided a reasonable match with the reported
experimentaldata.JungandGamwo[76]appliedmultiphaseCFD-
Fig.11. (a) Effect of particle diameter on conversion of H2 [71]. (b) Effect of bed
temperatureontheconversionofH2[71].
basedmodelsforchemicalloopingcombustionprocessusingMFIX
code. Wang et al. [73] applied multiphase TFM CFD modeling to
chemical looping combustion using a CUO/Al2O3 oxygen carrier. superficial velocity, etc. which affects combustion process in flu-
Theshrinkingcoremodel(SCM)withthereactioncontrolledbythe idized bed. Although numerous literature will be found on these
chemicalreactioninthegrainisapplied.Theresultsshowthatthe parameters,butwithCFDfewstudiesarereported.
fuel conversionwith the same inlet gas velocity would go up by
modestlyincreasingtheinitialbedheightandthetemperaturebut 3.2. Gasification
wouldslightlydecreasewithanincreaseintheoperatingpressure.
Thehighconversionofcoalgaswithalowsolidinventorycouldbe Gasificationisgenerallycarriedoutbyreactingfuelsuchascoal,
reachedinproperoperatingconditions. biomass, petroleum coke or heavy oil with restricted amount of
Intensive research has been performed over the past decade oxygen and often in combination with steam. Although much of
involving chemical looping combustion, but still it far awayfrom studies related to gasification of fuels in fluidized bed is already
beingacommercialavailabletechnology.CFDmodelingofchemical establishedandmanytextbooks[111,112]arefoundrelatedtothis,
loopcombustionsystemshasbeendonetoknowhowthefueland buttheaimofthisstudyistofindtheuseofCFDinstudyingthe
oxygen carrier is circulated in both the vessels along with other gasificationprocess.
parameters. Present CFD studies in all the cases are on two-
dimensional or third dimension is negligible. The solid volume 3.2.1. Physicalandchemicalprocesses
fractionsinallthecasesindicatethereactionoffuelwithoxidizer. CFD models are used to study the physical and chemical
Themajordifferenceinallthestudiesisintermsofcarriersandfuel behavioroffuelsinfluidizedbedgasificationprocess.Thenumer-
gas.Inallthesestudiestheheterogeneousreactionrateisimpor- ical model can present the detailed information about the gas-
tantforthedeterminationofthemasstransferbetweensolidand ification processes and bridge the gap effectively between large-
fluid phase and for the species transport equation which will be scale commercialized beds and small-scale testing models. To
usedtodeterminethesolidvolumereactionrates.Apartfromtime, improve the thermal efficiency and to predict product gas com-
temperature and turbulence there are other parameters like par- position and emission rates numerous mathematical models for
ticlediameter,designparameters,flowrate,oxygenconcentration, coalandbiomassgasificationindensebed[28,29,31,39,77e85]has

Author's personal copy
600 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
beendeveloped.MostofthemconsideredEulereEuler’smodelto reductionasaresultofpyrolysisandthemigrationofparticles.A
study fundamental investigations of the chemical and fluid me- lowvolumefractionisseentodescendneartheairinlet.Thisisdue
chanicalaspectsoffluidizedbeds.ItispartoftheirEeETFMCFD tothebiomassphasehavingahigherdensityanddiameterthanthe
modelwhichareformedtolookdifferentcharacteristics.Mostof charphasescausingtheparticlestofalltothebaseofthebed.The
simulationsaredoneintwo-dimensionalgeometries.Moststudies Fig.12(c)and(d)showsthevolumetricfractionofLimeandChar,
haveperformedoncoalasfuel.Onlysomeauthorshavereported respectively.Theparticlediametersremainthesamehoweverthe
[77,80,85]itforbiomassindensebed.Armstrongetal.[80]formed densitiesofthelimestoneandchardiffergreatly.Althoughnoclear
aCFDmodelforbiomassandcoal.Theyalsodiscussedvariousef- distinction is observed with regards to segregation in Fig. 12(d)
fectsregardinggaseousemissions.Theresultintheseearlystages closeinspectionindicatesthatthelowerdensityparticlesnamely
showsthattheinclusionofcoaltothemodelhasstrongeffecton char, are segregating to the top of the bed. The highest volume
thegaseousproducts produced.Thereappearstobea significant fractionofparticlesoccursatthefuelinletandreducesduetothe
increaseinthemolefractionsofCO2andH2O.Thiscouldbedueto massreductionasaresultofpyrolysisandthemigrationofparti-
anincreaseinthemassfractionofH2andaslightincreaseinCO cles.Alowvolumefractionisseentodescendneartheairinlet.This
released during the pyrolysis stage of the coal compared to the isduetothebiomassphasehavingahigherdensityanddiameter
biomass.Gerberetal.[77,85]formulatedCFDmodelbedmaterial thanthecharphasescausingtheparticlestofalltothebaseofthe
consistingofwoodandchar.Withincreasingtemperatureswithin bed.
the reactor they found higher reaction rates for pyrolysis, gas-
ification,andhomogeneousgasphasereactions.Theconcentration 3.2.2. Effectofoperationalparameters
of gasificationproducts like CO, H2, and CH4 is causing increased The parameters which control gasification in fluidized bed
temperature levels. Zeng et al. [79] discussed CFD model of coal include fuel properties, particle size, species concentration, flow
gasificationinfluidizedbedandtheeffectofvariousparameterson velocity, bed material, fluidization velocity, geometry etc. CFD is
gasificationparameters,i.e.emissions.Pressurecausingthecarbon beingusedtostudyalltheseparameters.CFDistooltostudythe
monoxidetoincreaseinreactorandbedtemperatureishavingno variationoftheseparametersonthegasificationprocessinfluid-
effect on molar concentration. However with increase in reactor ized bed. Because of complexity of process, i.e. gasification with
temperature,therateofBoudouardreactionwhichconsumesCO2 multiphase,notmuchdetailisfoundaboutvariationofparameters.
andproducesCOwillbecomefaster.Lietal.[84]alsodiscussedthe Moreover, the geometries like two dimensions discussed in liter-
aboveeffectsinpressurizedspoutedfluidbedforcoal. aturewillnotbehelpfultomakeanysolidconclusionsregarding
The numerical simulations of the bubbling fluidized bed coal study of gasification process in fluidized bed with CFD. The size,
gasification for two-dimensional bubbling fluidized bed gasifier design and conditions of each fluidized bed gasifier are different
(BFBG) is done by Yu et al. [47]. The coal gasification rates are and comparison is verydifficult. Fewstudies related tothese are
determined by combining Arrhenius rate and diffusion rate for reported.
heterogeneousreactionsorturbulentmixingrateforhomogeneous Gerberetal.[77]haveformedtheEeETFMCFDmodelforchar
reactions. The simulation results would give much more exact asbedmaterialintwo-dimensionalfluidbedgasifierandstudied
predictionsofthedistributionsofpressure,temperature,velocity, thevariousparameterslikeeffectofinitialbedheight,variationsin
volume fraction of the phases and gas composition along the fuelairratioandreactorthroughput.Theytriedtodothevariations
reactor which cannot be described by two-phase or three-phase in initial bed height by 25% in both directions and product gas
onedimensionalfluidizationmodels.Themathematicalmodeling concentrationsandtaryieldaredepictedforthebasecaseandthe
ofcoalgasificationinafluidizedbedreactorisdonebyCornejoand variations.Theydonotfindanyinfluenceoftheinitialbedheight
Farıas[86].ThisworkissimilartoworkdonebyYuetal.[47]with on the gaseous components in the product gas and found strong
more simplifications. Their chemical model involved five hetero- influenceonthereactivetarcomponent.Theyalsotriedtovarythe
geneousandfivehomogeneouschemicalreactions,trackingseven fueltoairratiobychangingthefuelmassflowbyvaryingthere-
speciesinthegasphase(CO2,CO,H2O,CH4,H2,O2andN2)andone sults in the gas yields. The higher the fuel input is, the more
species in the solid phase (C(s)). Drying and volatilization rates products gases and tars evolve. This trend is expected for the
wereestimated by mass conservation. The majordifference from product gases but not necessarily for tar as tar production rates
Yuetal.[47]isthatinthisprocesscoalenteringinthegasifierin showhighertemperaturedependencethanwood.Zengetal.[79]
driedstateandthereisnoashconsideredinthissystem.TheCFD have formed CFD model for pressurized spouted bed and dis-
simulationofafluidizedbedgasifieroperatingwithlignitecoalis cussedtheeffectofbedtemperatureandpressureonformationof
donebyKarimipouretal.[87].Theydiscussedthatthemethodof gaseous species. In their results the increase of bed temperature
implementingthewater-gasshiftreactionintothesimulationcode enhancestheformationofallothergasesexceptH2andCH4.There
ishighlyinfluentialonthecomputationalexpense. results indicate that the gas quality (combustible fractions and
TheTFMEeECFDtechniqueisalsousedtoplotthesolidvolume caloric value) improves at a higher operating pressure. They
fraction of char, toknow the movementof char. After the drying explainedtwopossiblereasonsbehindthis.Theyexplainedtheone
and devolatilization these char particles become less dense and aboutthegasificationrateenhanceddirectlybypressureduetothe
theirtendencytoflowatthetopofbed.Thistechniquecouldhelp increase in the partial pressure of reactants and otheras the flu-
toseeflowofcharinthebed.Thesolidvolumefractionoftwochars idizationinthereactorbecomesbetteratelevatedpressure.
[80]andLimeandCharisshowninFig.12(a).Thecharparticlesin Armstrong et al. [28] studied the parametric gasification of
the fluidized bed after some time will be segregated depending process in BFB gasifier using CFD. They studied the effect of bed
uponthetimeofsimulation.After5.0sforthebiomassgasification heightongasspecies.Thislowerbedheightincreasestheareaof
modelthevolumetricfractionofchar1[biomass]andchar2[coal] the freeboard providing more space for the relevant species,
phasesinthebed.Thediameterofthechar2phaseissmallerthan namely CO, CO2, H2, and H2O, to compete in the water-gas shift
thechar1phasethereforetheparticlemovetothetopofthebedas reaction thus indicating that equilibrium can be obtained in
the larger particles segregate tothe bottom. Fig.12(b) shows the asmall-scalereactorprovidedthefreeboardshouldbesufficiently
volumefractionofthebiomassat5.0s.Theparticlesareonlyseen tall.Resultsshowthatbedtemperatureishavingmoreinfluenceon
in the vicinity of the fuel inlet. The highest volume fraction of the gasification processes. The bed temperature results in an
particles occurs at the fuel inlet and reduces due to the mass increaseinCOandH2speciesandadecreaseinCO2andH2O.They

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 601
Fig.12. (a)Volumefractionofchar1andchar2[80].(b)Volumetricfractionofbiomass[80].(c)and(d)Volumefractionoflimeandchar[39].
explaineditduetohighlytemperaturedependentheterogeneous respectively. Zhou et al. [88] formed CFD model and discussed
reactions. As the temperature increases the reactions take place various parameters for biomass gasification in fluidized bed. The
fasterleadingtoafasterconsumptionofthereactantsH2OandCO2 sizeofparticleisincreasingthehydrogenyield,steamtobiomass
through the steam gasification reaction and Boudouard reaction, ratio(S/B)andequivalenceratio(E/R)initiallyincreasinggasyield

Author's personal copy
602 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
and then decreasing gas yield. As per Wang et al. [89] when the fluidizedbedwithCFDasdiscussedbyArmstrongetal.[28,39].For
airflow rate is fixed, the amount of hydrogen and carbon mono- mostthedevicesthebedmaterialisinertandhavingnoeffecton
oxideissensitivetothechangesofERandtemperature,andlower gasificationoffuelinfluidizedbed.Therearefewauthors[47,86,87]
ER value or higher temperature or both are beneficial for higher who studied gasification of fuels in fluidized bed without inert
yieldofsyngas. material.Theconsideredsolidfuelcharsasbedmaterial.Theyused
Heetal.[81]usedCFDtosimulatethewoodgasificationinalab EeE TFM approach to study gasification in fluidized bed. Few
scale bubbling fluidized bed. They discussed effect of various pa- simplifications include the negation of interaction forces like lift
rameterslikeERandS/Bongascomposition.TheeffectofERandS/ force,thermophoreticforce,Brownianforceandvirtualmassforces
BongascompositionisshowninFig.13(a)and(b),inwhichthe inallthesecases.Theintensityofparticlescollisiondoesnotvary
simulation results obtained from the kinetic model. Due to the withtemperature,i.e.,exothermicorendothermicreactionhasno
dilution effect from nitrogen and the combustion reactions, pro- impactonthefluctuationofsolidvelocityanddoesnothavearise
duction of gases with heating value (H2, CO and CH4) from air inthetemperatureofgranularareamongfewmoresimplifications.
gasificationislowwhilehavingahighCOpercentage.Anincreasing There is no known effect of char on gasification in fluidized bed
ERdecreasesH2,COandCH4yieldsbutincreasesCO2amountand whenitisusedasbedmaterial.Inallthestudiesreportedabove
drygasyield.WithincreasingS/Bratio,concentrationofH2andCO thereisnoashphaseconsidered,i.e.fuelwillbreakdownintochar
increaseswhilethatofCOdecreasesindicatinganenhancedwater- andcombustiblegases.
gasshiftreaction.Thesimulationresultsshowagoodagreementin Thefewstudiesreportedwhentheyconsideredbedmaterialas
H2andCH4productionbutdiscrepancyofpredictingtheCOandCO mixtureofsand,fuel,charorashes.Fewauthorshaveconsidered
trendscomparedwiththeexperimentalresults. [28,29,78,80,90] studied gasification using the above mixture.
SinceCFDinfluidizedbedgasificationisimmaturefieldanditis Howeverforanyofstudiesreportedtheeffectofvariationindif-
stillgrowingwithadvancementincomputationaltechnology.Most ferent percentage of bed material is not reported. In all cases
ofparametersdiscussedabovelikebedheight,feedingrate,ER,S/B reported these includes drying, devolatilization and gasification.
ratio etc. are known facts, but here attempt is study the above But no such parameters is discussed which will decrease or
parameterswithaidofCFD.Manyofparametersarenotreported enhance the gasification process. An Eulerian CFD modeling
formostofstudies.Thetarget/aimofmostofstudiesistovalidate approachofwoodgasificationinabubblingfluidizedbedreactor
CFDmodelintheircases. using char as bed material is done by Gerber et al. [77]. They
reported char to act as a catalyst capable of reducing tar, but no
3.2.2.1. Bedmaterial. Theinertbedmaterialishavingnoaffecton effects of performance or comparison with inert material is
thegasificationprocessinfluidizedbedaspredictedwithCFD.CFD reported.
can be used as tool to study the effect of bed material on gas-
ification process in fluidized bed. The bed material limestone to 3.2.2.2. Design. Theeffectofchangesingeometryordesignisnot
capturesulfur,i.e.calcinationprocessongasificationparametersin much reported in literature to affect the combustion and gas-
ificationinfluidizedbedwithaidofCFD.Benjaponetal.[91]have
made the hydrodynamic descriptions and chemical reaction re-
sponses using CFD modeling of tapered circulating fluidized bed
reactorrisers.TheytestedCFDmodelingfortaperinandtaperout
of riser. They found that the tapered-in riser increases the solid
particle residence time and gives a more uniform temperature
distribution,becauseitdoesnothavesufficientforcetosupportthe
weightoftheparticles.Theyfoundthatthetapered-inriserisbest
forreactionswithaslowratewhilstthetaperedoutriserbestfitted
the reactions with a fast rate. Mazumder et al. [92] used CFD in
designingconceptualhybridgasifierandinsecondpart[93]they
havemadesimulationofahybridentrained-flowandfluidizedbed
mild gasifier. It is simply newly conceptual design in two di-
mensionsandnothingisexplainedaboutanychemicalprocessthat
isaffectedbydesign.Theycalculatedvariousspeciesandconsid-
eredallthereactionsingasifierusingCFD.
AlthoughitisprovedthatCFDishelpfulindesignoffluidized
beddevices,butconsideringmultiphasereactions,i.e.gasification
itlacksinliterature.Thebedtemperature,bedheight,particlesize,
oxygen concentration in air, pressure in combustor, hydrogen to
carbon monoxide ratio, geometry, bed material and ash behavior
have unique effect on performance of fluidized bed performance
withgasificationanditisprovedbyaboveliteraturethatCFDisan
effectivetoolusedtostudyoperationalparametersthatarederiv-
ingaboveprocess.Table2summarizestheCFDstudyofcombus-
tion and gasification based on EeE TFM model and Table 3
summarizes the CFD study of combustion and gasification based
onDPMLagrangianapproach.
3.3. Emissions
The main source of air pollution is the combustion of fuels in
Fig.13. (a)EffectofERonH2/COandgasyield[81].(b)EffectofS/BonH2/COandgas
yield[81]. stationary and transportation systems. The boilers, furnaces and

Author's personal copy
Table2
VariousTFMEulerianeEulerianCFDchemicalreactivemodelsinfluidizedbedcombustorsandgasifiers.
Authors Year Title Type Code/software Dimension Turbulence Featuresofmodel Extramodel/UDF Agreementwith Remarks
model experimental
Fariasetal.[60] 2006 CFDstudyonnaturalgas-fluidizedbed B AnsysFluent NS keε Twostagekinetic No Yes ClusterofLinux
combustors model X86machinesis
used.
Yuetal.[47] 2007 Numericalsimulationofthebubbling B Owncode 3D keε Kineticmodel NA Yes Noinertmaterialis
fluidizedbedcoalgasificationbythekinetic [116]/EddyBreak usedindensebed
theoryofgranularflow(KTGF) up
JungandGamwo[76] 2008 MultiphaseCFD-basedmodelsforchemical B MFIX 2D NS LFRM Yes Yes MethaneandNiO
loopingcombustionprocess:fuelreactor ascatalystisusedin
modeling fuelreactor
Dengetal.[71] 2008 MultiphaseCFDmodelingforachemical B Fluent 2D keε Shrinkingcore Yes Yes Reactionkinetics
loopingcombustionprocess(fuelreactor) model[108]/LFRM modelsofthe
andEDM ( r C ea a c S t O o 4 rþ H2)fuel
ZhongyiDeng[79] 2008 Computationalfluiddynamicsmodelingof P Fluent 3D keε Shrinkingcore Yes Yes Experimental
coalgasificationinapressurizedspout-fluid model[108]/EDM verificationisdone
bed on0.1MWreactor
Zhouetal.[8] 2009 Numericalsimulationonhydrodynamics C NotSpecified 2D keε LFRM Yes Notall Validationwith3D
andcombustioninacirculatingfluidized testrigandnot
bedunderO2/CO2andairatmospheres promisingresults
Nikolopoulosetal.[9] 2009 Numericalinvestigationof3-dtransient C AnsysICEMand 3D keε Shrinkingcore Yes Yes Combustion
combustingflowina1.2MWthpilotpower StarCD model/LFRE chamberhas9.5m
plant model heightand0.4m2
diameter
Qianjumetal.[84] 2009 Simulationofcoalgasificationin P Fluent 3-D keε KineticmodelChen Yes Yes Themaximum
apressurizedspout-fluidbedgasifier etal.[116]/EDM errorinoneof
parametersof
model,i.e.methane
is25%.
Wangetal.[78] 2009 Three-dimensionalsimulationoffluidized B AnsysFluent 3D keε NS Yes Yes Gasifierof2mand
bedcoalgasification 0.2mdiameteris
usedforvalidation
Emdenetal.[68] 2010 Developmentandtestingofan B AnsysFluent 2D keε Linearand Yes NS Chemicalloopingis
interconnectedmultiphaseCFDmodelfor sphericalshrinking operatedwith
chemicalloopingcombustion core/FRMandED methaneasfuelgas
M andMn3O4as
oxygencarrier
Karimipouret.al[87] 2010 CFDsimulationofafluidizedbedgasifier B Opensource/MFIX 3-D NS Shrinkingcore No NS Simulationare
operatingwithlignitecoal Model doneDMP
(distributed
memoryparallel)
mode
Gerberetal.[77] 2010 AnEulerianmodelingapproachofwood B Opensource/MFIX 2D keε ArheniustypeLaw/ Yes Notall Charasbed
gasificationinabubblingfluidizedbed LFRandED materialisused
reactorusingcharasbedmaterial
Benjaponetal.[91] 2010 CFDmodelingoftaperedcirculating C AnsysFluent 3-D keε EDM No Yes Taperinofriser
fluidizedbedreactorrisers:Hydrodynamic givebest
descriptionsandchemicalreaction performancefor
responses reactions
Armstrongetal.[28] 2011 Parametricstudyofgasificationprocesses B AnsysFluent 3D keε EDM Yes Yes Limestone
inaBFBcoalgasifier calcinationis
incorporatedin
mainmodel
(continuedonnextpage)
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
603

Author's personal copy
Table2(continued)
Authors Year Title Type Code/software Dimension Turbulence Featuresofmodel Extramodel/UDF Agreementwith Remarks
model experimental
Wangetal.[73] 2011 Multiphasecomputationalfluiddynamics B KFix 2D keε EDM Yes NS Chemicalloopingis
(CFD)modelingofchemicallooping operatedwith
combustionusingaCuO/Al2O3oxygen methaneasfuelgas
carrier:effectofoperatingconditionson andNiOasoxygen
coalgascombustion carrier
Mazumderetal.[92] 2011 Designandsimulationofahybrid B AnsysFluent-12 2-D keε LFRMandEDM Yes NS CFDappliedto
entrained-flowandfluidizedbedmild conceptualand
gasifierpart1edesignconsiderationsand theoreticalhybrid
developmentofamultiphasemodel gasifier
Zhouetal.[6] 2011 Two-dimensionalcomputationalfluid C MFIX 2D keε LFRandEDM Yes No Two-dimensional
dynamicssimulationofcoalcombustionin withthefurnace
acirculatingfluidizedbedcombustor depthof0.1mand
noinertmaterialis
considered
CornejoandFarias[86] 2011 Mathematicalmodelingofcoalgasification C AnsysFluent 3D keε EDM Yes Yes Modelassumes
inafluidizedbedreactorusingaEulerian dryingoffuelat
granulardescription mouthofgasifier
andvariationofone
ofgasmethane
fromexperimental
isabove60%
MyohanenandHyppanen 2011 Athree-dimensionalmodelframefor C AnsysFluent 3D NS Notspecified Yes No Simulationsare
[31] modelingcombustionandgasificationin donein3Dtest
circulatingfluidizedbedfurnaces furnaceandmodel
includessulphation
andcalcination
model
Lietal.[94] 2011 Numericalsimulationofbiomass B AnsysFluent 3D NS Homogeneous No Yes Effectofmassratio
gasificationinafluidizedbed reactions/Arhenius steamandbiomass
expression isstudied
Mahalatkaretal.[72] 2011 Simulationsofacirculatingfluidizedbed C AnsysFluent 2D NS Uniformreaction Yes Yes Manganeseoxide
chemicalloopingcombustionsystem model(Sonand carrierwiththefuel
utilizinggaseousfuel Kim[66]) gases
Wangetal.[73] 2011 Multiphasecomputationalfluiddynamics B Notspecified 3D NS Shrinkingcore Yes Yes CuO/Al2O3oxygen
(CFD)modelingofchemicallooping model/LFRandED carrier
combustionusingaCuO/Al2O3oxygen M
carrier:effectofoperatingconditionson
coalgascombustion
Zhouetal.[7] 2011 CFDmodelingofoxy-coalcombustionin B MFIX 2D keε LFRandEDM Yes No Oxycombustionof
circulatingfluidizedbed coalin2Dgeometry
isconsidered
604
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614

Author's personal copy
Table3
DiscreteparticleEulerianeLagrangianapproachusedinfluidizedbedcombustionandgasificationdevices.
Authors Year Title Code/software Dimension Turbulence Extra Agreementwith Remarks
model model/UDF experimental
Zabettaetal.[95] 1999 NOxreductionbystaginginbiomass Fluent5.4 3D k-ε Yes Yes Stagedcombustionisdone
combustioneAkineticandCFDmodeling
study
SofialidisandFaltsi[96] 2001 Simulationofbiomassgasificationin Fluent 3D keε No Yes Thebiomassparticletrajectoriesareby
fluidizedbedsusingcomputationalfluid nomeansrepresentativeofthereal
dynamicsapproach situation,astheeffectofsolid-to-solid
interaction(sand-to-biomass)is
ignored.
Brinket.al.[11] 2001 CFDmodelingofthefateofbiomassfuel- Fluent 3D keε Yes Yes Effectofturbulenceismodeledwith
nitrogeninthefreeboardofa70MWFBC- eddydissipationmodel.
newaspectsoncontrollingmechanisms
Zevenhovanand 2001 Particle/turbulenceinteractions,mass Fluent 3D keε Yes Yes Theeffectofparticlesize,temperature,
Jarvinen[14] transferandgas/solidchemistryinaCFBC reactorsizeandfluidizationvelocityon
Riser NOischecked.
Muelleretal.[18] 2002 CFD-basedashdepositionpredictionin Fluent 3D keε Yes Yes NewconceptofcombiningCFDwith
abubblingfluidizedbedcombustorfiring chemicalfractionationanalysisand
mixturesofbiomasses multiphaseequilibriumcalculations
Grabneretal.[98] 2007 Numericalsimulationofcoalgasificationat Fluent 3D keε Yes Yes COisnotincorporatedinsimulation
circulatingfluidizedbedconditions
Lundmarketal.[19] 2007 Computationalfluiddynamicmodelingof Fluent 3D keε Yes Yes NewconceptofcombiningCFDwith
combustionandashdepositioninabiomass chemicalfractionationanalysisand
co-firedbubblingfluidizedbedboiler multiphaseequilibriumcalculations
Agraniotisetal.[23] 2009 Numericalinvestigationonthecombustion AnsysFluent 3D NS No Yes Measuredtemperatureincreaseatthe
behaviorofpre-driedGreeklignite furnaceexitwhichisnotexpected
Muelleretal.[15] 2005 Numericalsimulationofthecombustion AnsysFluent 3D keε Yes Yes Allfourstagesdrying,devolatization,
behaviorofdifferentbiomassesin charcarbonconversionandashparticle
abubblingfluidizedbedboiler formationareconsidered
Zhouetal.[88] 2006 Nonpremixedcombustionmodelof Fluent6.0 3-D keε No Yes Effectofparticlesize,steamtobiomass
fluidizedbedbiomassgasifierforhydrogen ratioandeffectofequivalenceratiois
richgas checked.
Brinket.al.[12] 2006 AmodifiedapproachforpredictingNOx Fluent 3D NS Yes Yes Splashzonemodelisformed
emissiontrendsfrombiomassfired
bubblingfluidizedbedboilers
Ravellietal.[21] 2008 Description,applicationsandnumerical Fluent6.1 3D keε No Yes Two-mixturefractionusingpdfisused
modelingofbubblingfluidizedbed
combustioninwaste-to-energyplants
WangandYan[89] 2009 CFD-basedcombustionmodelforsewage Fluent 3D keε No Yes Reactionmodelsusingnonpremixed
sludgegasificationinafluidizedbed combustionmodelandCHEMKIN
database
Xiaoetal.[99] 2009 Numericalsimulationofsludgedryness Fluent 3D keε No Yes Reactortemperatureisbelow432K
underfluegasatmosphereintheriserof whichseemsextremelylow
afluidizedbed
Brinket.al.[24] 2009 Asimplifiedmodelforthebehavioroflarge Fluent6.2 3D keε Yes Yes Modifiededdydissipationconcept
biomassparticlesinthesplashingzoneof modelisused
abubblingbed
Yuetal.[100] 2009 CFDmodelingappliedtotheco-combustion Fluent6.2.1 3D keε No Yes 130t/hboilerisunderconsideration
ofpapersludgeandcoalina130t/hCFB
boiler
Wischnewskietal.[101] 2009 3D-simulationofconcentration Notspecified 3D NS Yes Yes Fourzonesbottomzone,splashzone,
distributionsinsidelarge-scalecirculating upperdilutezoneandexitzoneare
fluidizedbedcombustors underconsideration
Ratschowetal.[102] 2009 Three-dimensionalsimulationof AnsysICEMandStarCD 3D NS Yes Yes Horizontaldispersioncoefficientsare
temperaturedistributionsinlarge-scale alsodiscussed
circulatingfluidizedbedcombustors
(continuedonnextpage)
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
605

Author's personal copy
enginesburningfossilfuelsemitgaseouspollutants,suchasSO2,
NOx,CO,N2Oandvolatileorganiccompounds(HC).Fluidizedbed
combustors or gasifiers have been used for long times to control
anddiscussingtheimpactofthesepollutants.CFDmodelingoffluid
dynamicshasalreadyreachedahighlevelwhilenumericalmod-
eling of reactive multiphase flows is still in an early stage. Many
researchers have done a lot of work on the pollutant emission
modelingintheFBcombustorsandgasifiers,butCFDmodelingof
emissionsinfluidizedbeddevicesisinstilldevelopingstage.Only
few papers [21,89,93,96,98,100] have been found discussing the
above.Mostoftheresearchintheliteraturedealingfuelsparticles
with DPM Lagrange approach and it is difficult to describe the
chemical processes properly with EeE TFM method. Only few of
them [28,31,39,107] discussed these emissions using EeE TFM
approach.Themostauthorsdiscussedthesepollutantsasapartof
CFD model and compared their results regarding pollutants with
experimentalvalues.
3.3.1. Carbonmonoxide
Carbon monoxide particularly in many areas comes primarily
fromautomobiles.Theemissionofcarbonmonoxidefromfluidized
bedboilerplantsisnotgenerallyperceivedtobeamajorproblem
andisnormallybelowthestatutorylimit.Theemissiondependson
thefuelcompositionandcombustiontemperature.Itisoneofmost
important green house gas; it received the greatest attention in
termsofemissioncontrol.CFDisbeingisusedtostudyitsbehavior
while combustion/gasification of fuel in fluidized bed. Many au-
thors [21,89,96,98,100] have reported the emissions using DPM
LagrangianandotherhaveusedEeETFMmodels[93]tostudyCFD
modelingofcombustion/gasificationin bed.Lagrangianapproach
using DPM is used to study carbon monoxide emissions in free-
board, whereas for dense bed EeE TFM approach is used. The
emissionsarepartofCFDmodelingforthecaseofcombustorsand
gasifiers, whichare validatedbymeasurements.Forthefluidized
bedcombustorstheformationofcarbonmonoxideisconsideredas
emissions, where as in gasifiers it is intermediate stage before
combustion.
Few authors [21,89,93,96,98,100] discussed carbon monoxide
emissionswithLagrangianDPMapproach.Sofialidisetal.[96]has
simulated biomass gasification in fluidized beds using computa-
tional fluid dynamics approach. Their simulation results include
various species and carbon monoxide is one of them. Fig. 14(a)
showsthecontoursoftheCOmassfractionsinthegasmixture.The
highervaluesforCOarelocatedimmediatelyabovetheairinlets,
while for CO2, at a greater height. Both gases acquire their exit
valuesveryquickly,belowthefreeboardarea.
Yu et al. [100] applied CFD modeling applied to the co-
combustion of paper sludge and coal in a 130t/h CFB boiler. The
carbon monoxide emissions are one of parameters in this. The
carbonmonoxideprofilesareshowninFig.14(b).Theyconcluded
thathighconcentrationCOcomesfromthedense-phasezoneand
thatisconsumedinboththefluidizedparticlecombustionandthe
collision of bed material. The high CO region coincides with the
mainpassofthegasflowandisclosetothesecondaryairinlet.In
thevolumespacenearthebedbottom,thereisonlylowconcen-
tration CO. In the dilute-phase zone, temperature reduces to
alowerlevelandanyfurtherCOreactionisveryslow.Grabneretal.
[98] also discussed the formation of carbon monoxide using nu-
mericalsimulationofcoalgasificationatcirculatingfluidizedbed
conditions.Wangetal.[89]formedCFD-basedcombustionmodel
for sewagesludge gasification in a fluidized bed. The model sen-
sitivityisanalyzedbyperformingthemodelinalaboratory-scale
fluidizedbedintheliterature,andthemodelvalidationiscarried
outbycomparingwithexperimentaldatafromtheliterature.Their
resultsshowthatreasonablygoodagreementisachieved.Theyalso
)deunitnoc(3elbaT
skrameR
htiwtnemeergA
artxE
ecnelubruT
noisnemiD
erawtfos/edoC
eltiT
raeY
srohtuA
latnemirepxe
FDU/ledom
ledom
spordrotsubmocfoerutarepmetdeB
seY
oN
εekGNR
D3
tneulFsysnA
fogniledomscimanyddiufllanoitatupmoC
0102
]22[.lateeeniazoR
yltneuqerf
debdezidiuflaninoitsubmocksuhecir
rotsubmoc
enodsinoitacfiisagegatS
seY
oN
SN
D-3
20.4mccratS
etsawydoowfonoitalumislaciremuN
0102
]301[.latekraP
debdezidiuflegatsowtninoitacfiisag
refiisag
noitazilatloved]24[.lataihsabyoK
seY
seY
εek
D3
tneulF
scimanyddiufllanoitatupmocD3
0102
]28[.lategnaT
desusiledom
maetsekoclarutanfonoitalumis
devorpmidnalarenegninoitacfiisag
sdebdezidiufl
ehtrofsnoitauqeyrtsimehcdnaygrenE
seY
oN
SN
D3
DFPC
-eerhtrofdohtemnaignargaLenaireluE
1102
]401[.lateredinS
.detneserperaDFPCnidohtemCIP-PM
htiwwoflgnitcaerlamrehtlanoisnemid
srefiisaglaocotnoitacilppa
sahseiticolevtnereffidfoecneuflnI
seY
seY
SN
D2
edoCnwO
doowfogniledomegnargaLereluE
1102
dnarebreG
detneserpneeb
sdebdezidiuflesnedninoitacfiisag
]501[nnamreveO
wenhtiwenodneebsahnoitalumisehT
seY
oN
SN
D3
aducarraB
dnastnemerusaemneewtebnosirapmoC
1102
dnagneW
dohtemaducarrabfotpecnoc
dnawoflelcitrapfonoitalumislaciremun
]601[reyemkcalP
tnalpCBFCgrubsiuDehttanoitsubmoc
606 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 607
Fig.14. (a)MassfractionsofCO[96].(b)COconcentrationsprofilesofcoalcombustion(i)andco-combustionofpapersludge/coal(ii)(x 0mm,rangefrom 2256.5mmto
¼ (cid:2)
2265.5mm[boilerdimensions])[100].(c)EffectofERonratioofH2/COforT
¼
1023K,1073K,and1123K(M)modelresults;(E)experimentdata[89].
discussedtheeffectsoftemperatureandequivalenceratio(ER)on oxide,CaO,whichmayabsorbapartofthesulfurdioxideascalcium
thequalityofproductsyngas(H2 CO).AsuitableratioofH2/COis sulfate. Some amount of it will escape to atmosphere and some
þ
useful for the chemical industry. The ratio of H2/CO slightly de- amount will be converted to sulfur trioxide. Primarily during
creaseswithincreasingERvaluewhenERislessthan0.35butin- combustionorgasificationoffuelin fluidizedbedthechances of
creases with increasing ER when ER is over 0.35 as shown in formation of these gases are very thin. The sub-models of sulfur
Fig.14(c). emissionsareaddedtomainCFDmodeltoknowtheemissions.The
Hydrogen to carbon monoxide ratio is one of critical output CFD modeling of SOx will make the process computational very
parametersforliquidfuelsynthesisandstillvariationsofnearlyan expensivewithmultiphaseapproach.TheCFDmodelingofSOxis
orderofmagnitudeareobserved,whichcannotbeexplainedbythe possible both with Lagrangian and EulerianeEulerian Approach.
currentstateofunderstandingofthesesystems.Onlyfewauthors Butforindustrialfluidizedbedunitsmorejourneyshavetotravel
[89]discussedhydrogentocarbonmonoxideratioinfluidizedbed. beforeanyprominentresultswithSOxCFDmodelsandmultiphase
Present research based on CFD models related to fluidized bed approach.Fewauthors[28,31,39,107]discussedformationSOxwith
combustionandgasificationrelatedhasbeensilentonthisissue. EeECFDmodelinfluidizedbed.
Zhouetal.[107]discussedcomputationalfluiddynamicssim-
3.3.2. SO2emissions ulation of nitrogen and sulfur oxides emissions in a two-
Duetoburningoffuelthesulfurisoxidizedprimarilytosulfur dimensional circulating fluidized bed combustor. Based on the
dioxide. The mineral matter in coal may contain some calcium previously established two-dimensional computational fluid

Author's personal copy
608 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
dynamics(CFD)modelwhichdescribedprocessesofcoaldevola- All the results are matching with the experimental values. Myo-
tilization,volatile combustionandcharcombustion incirculating hanen et al. [31] formed a three-dimensional model frame for
fluidized bed (CFB) combustors, nitrogen and sulfuroxides emis- modelingcombustionandgasificationincirculatingfluidizedbed
sionsarenumericallysimulatedandinvestigatedintheirresearch. furnaces. They included sub model for sulfur, i.e. limestone re-
Fig.15(a) shows thecontoursof molarfraction ofSO2 concentra- actionsalongwithothersub-modelsinCFDcalculation.Limestone
tion.ThecharofsulfurwillbeconvertedtoSO2duringcharcom- willactassorbentfortheabsorptionofsulfurdioxideinfluidized
bustion. SO2 was retained by CaO calcined from CaCO3. By bedcombustors.TheyhaveappliedCFDonthree-dimensionaltest
convertingreactionrateexpressionstosuitableformsforEuleriane furnacetolookvariouseffects.Thelimestoneiscalcinedquicklyas
Eulerianmodeling,sulfationreactionratesfromtwodifferentlit- itentersthefurnace.Regardingsulfurdioxidetheirontheresultsof
eratures were compared. Theyevaluated the performance of SO2 modelisshowninFig.15(c).Fig.15(c)presentsthecalcinationand
emission for conditions with/without considering sulfur self- sulphation rates. The resulting CaO is then reacting with sulfur
retention. Fig. 15(b) shows the comparison between simulated dioxideandthesulphationrateisnaturallyhighestinthelocations
andexperimentalpollutantconcentrationsatoutletondrybasis. wheretheconcentrationofSO2ishighest.Thehighestsulphation
Fig.15. (a)ContoursofSO2concentrationandrelatedreactionrateswithoutaddinglimestone[107].(b)Comparisonbetweensimulatedandexperimentalpollutantconcentrations
atoutletondrybasis[107].(c)Modeledcalcinationsandsulphationrates[31].

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 609
rateislocatedjustabovethebottomofthefurnaceandinthecore modeling. The main reasons are the largenumberof species and
ofthefurnace,wheretheSO2isreleasedfromcombustionofchar. radicalsinlowconcentrationsinvolvedinthenitrogenchemistry
The limestone calcination plays important role in capture of and their sensitivity to temperature and turbulent motion of the
sulfur.Limestonecalcinationisintroducedtoacomputationalfluid flow.Fewofauthorsstudied[11e14,95,97]mechanismofnitrogen
dynamicmodeloffluidizedbedgasificationprocessbyArmstrong chemistryinbubblingbedcombustor.Brinketal.[11,97]usedCFD
etal.[28,39].Thelimestonecalcinationinthisstudy[39]isshowing modeling to study the fate of biomass fuel-nitrogen in the free-
only slight effects on gasification process. The slight changes are boardofa70MWFBC-newaspectsoncontrollingmechanismfor
observed in the gaseous compositions due tothe introduction of forestresiduefuel.Theyhavedevelopedtwo-stepmechanismsfor
CO2 as a result of limestone decomposition. They explained the modelingthefateoffuel-Nfrombiomassfiredcombustiondevices.
reasons for this are because of relatively short simulation time. The effect of the turbulence is modeled with eddy dissipation
Armstrongetal.[28]studiedtheparametricgasificationusingEeE combustionmodel.TheyfoundthatnoinfluenceontheNOemis-
CFD modeling and one of parameters is the effects of limestone sionscouldbeobtainedusingadifferentairstagingstrategy.Itis
calcinationoncoalbubblingfluidizedbedgasifierinabedofchar becauseoffactthatmostofthevolatile-Nreactedinthelowerpart
and limestone. They checked the effects of limestone calcination ofthefreeboardbetweenthesecondandthirdlevelofairports.
abedconsistingof100%limestonewhichincludesinertlimestone Brink et al. [12] continued their previous work [11] and pre-
andcalcinatinglimestone.Acloseupoftheproducts,CO,CO2,H2 sented a modified approach for predicting NOx emissions trends
and CH4, in Fig.16(a) showsa significant increase in the concen- from biomass fired bubbling fluidized bed boilers. The modified
trationofCO2duetolimestonecalcination;however,asexpected modelisbuiltontheargumentthatallnitrogenreactionssharethe
thisincreaseisonlyslightincomparisontotheinfluencehetero- sameradicalpoolandthusproceedatthesamephysicallocationin
geneous reactions have on the gaseous compositions. Fig. 16(b) theturbulentflow.MathematicallythemodifiedEDCMforthetwo-
showstheaveragemolefractionofO2atdifferentheightsnearthe stepmechanismcanbewrittenas:
airinletforthethree-bedcompositions.Clearlythisishigherwhen
thepercentageoflimestoneishigher. u min A(cid:2) ε min Y NH3 ; Y O2 r 1 ;u (4.5)
1 ¼ (cid:8) k (cid:8) r NH3;R1 r O2;R1(cid:9) r 1þ r 2 1;chem (cid:9)
3.3.3. NOxemissions(nitrogenchemistry)
e co te m r C s b F u D ( s N t m O or o x s , d . e N T l H i h n e 3 g c a i o s n m d us b N e u d 2 s ) t i i n o in n pr t c e e o d m m ic p m t e in r e a g r t c u n ia r i l t e r b o w g u h e b n e b n l c in h fi g e ri m n fl g i u s i t b d r i y i o z m p ed a a r s a b s m e i d s - u 2 ¼ min (cid:8) A(cid:2) k ε min (cid:8) r N Y H N 3 H ;R 3 1 ; r O Y 2 O ;R 2 1(cid:9) r 1 r þ 1 r 2 ;u 2;chem (cid:9) (4.6)
typicallyfairlylowandmostoftheNOxemissionsstemfromthe HereÀisconstantandr1isthechemicalrateforNH3oxidation
fuel bound nitrogen. The NOx emissions can still be reduced by by O2 and reaction rate r2 is the chemical rate for the reaction
primarily bound nitrogen and air staging. CFD is helpful in mini- formingN2fromNH3andNO.Toinvestigatethedifferencebetween
mizingNOxemissionsusingoptimization.ButNOxemissionmod- eddy dissipation model and the modified version, a 295MWth
elingisoneofthemostchallengingtasksinCFD-basedcombustion bubblingfluidizedbedboilerismodeledapplyingthebothmodels
togetherwithatwo-stepreactionmechanismforfuel-NO.Withthe
standardEDCMthisincreaseresultedinamarginalincreaseofthe
predicted NOx emission level only, indicating the insensitivity of
this model to the NO chemistry. The modified EDCM showed
a significantly higher sensitivity to the nitrogen chemistry and
allowedpredictionofreasonableNOxemissiontrends.Themodi-
fiedEDCMshowsexpectedsensitivityoftheNOXemissionstothe
chemicaldescriptionofthereactionrates.Zabettaetal.[95]applied
CFDtostudyreductionofNOxbystaginginbiomasscombustionby
homogenous detailed chemical kinetic modeling. The effect of
temperature,devolatilizedhydrodynamics,volatilenitrogencom-
ponents (NH3, HCN) and number of air addition stages on NOx
formationisinvestigatedatonedimensional,isothermal,idealplug
flowconditions.Zhouetal.[107]hasdiscussedcomputationalfluid
dynamic simulation of nitrogen and sulfur oxides emissions in
atwo-dimensionalcirculatingfluidizedbedcombustor.TheirCFD
modelintwo-dimensionalfluidizedbedcombustorpredictedNOx
emissions using EeE approach. In their studies the char N con-
vertedtoNOduringcharcombustionandNOxisreducedtoN2by
charcarbonorCO.
In all the studies except one [107] presented above, the com-
putationaldomainfocusesonthefreeboardregion.Thereisdiffi-
cultyintheaccuratemodelingofthefuelsupplyasmostoffuelsare
80e90% pyrolyzed in flight before arriving at the bed. The
remaining10%fuelisassumedtobefullyoxidizedwhenentering
thefreeboardfromthebedsurface.Atpresent,therearenodetailed
modelsavailabletodeterminethecompositionofthepyrolysisgas
withrespecttonitrogencontainingspecies.Thevalueshavetobe
assigned based on experience and naturallyalso on the nitrogen
content of the fuel. The same uncertaintyexists for the determi-
Fig.16. (a)Closeupofthegaseouscompositionoftheproductsforabedofinertand
nation of the composition of the main pyrolysis gas. The firing
calcinatinglimestone[28].(b)AveragemolefractionofO2atdifferentheightsnearthe
airinletforthethree-bedcompositionscharratioislower[28]. mode of fuel to fluidized bed furnace is option tocontrol NOx as

Author's personal copy
610 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
explainedbyBrinketal.[13]intheirstudies.AccordingtotheCFD ThepresentEuleriantechniqueconsideredfewsecondsofflow
optimization it would be possible toreduce the NOxemission by timeofdensefluidizedbedsimulations.Forrealfluidizedbedunits
substantialamountonlybyadjustingtheairsupply. theinitialflowtimeisnotimportantasstartofunitsisusuallydone
withconventionalfuelsandinconventionalfashion.
4. Presenttrendsandchallenges Authors(We)alsotriedtoapplytheEeETFMapproachforbark
inreactivedensebedofcommercialscaleboiler.Theuserdefined
CFDmodelingof dense bed and freeboard/riserwith combus- function(UDF)forbarkcombustioninthefluidizedbediscreated
tion and gasification issues has been studied separately in liter- usingArrheniusequation.Theresultsarenotsatisfactory.Theone
ature. No study is reported when both bed and freeboard have reason is shape of bark particles. The other reason is that when
simultaneously considered for CFD simulation. In generally EeE combustionorgasificationoffuelsindensebedisconsideredfor
TFM is used for dense bed and Lagrangian model with DPM Eulerianphase,itcomeswiththethreephases;barkesandeairand
approach is used for freeboard/riser. As per trends turbulence thereactionofbarkwithairmakesthethingmorecomplex.Only
modelkeεisusedinmostofcasestostudycombustionandgas- one author [9] reported combustion in fluidized bed of 1MWth.
ificationoffuelsinfluidizedbedunits.Majorityofstudiesrelatedto BasedonthisitcannotbeconcludedthatTFMEulerianeEulerian
combustion and gasification in fluidized bed is done using Ansys model at present is suitable for dense beds in commercial units
Fluent software. However contribution of own codes and other when phase reactions has to be considered. Present models are
software’s like MFIX cannot be ruled out. The trends could be notadvancedenoughtobeconsideredasusefultoolforbiomass
dividedintothreedifferentapproachesdiscussedpreviously,i.e.Ee gasification-pyrolysisorcombustionindensebeds.
ETFM,DEMeCFDandLagrangianDPMapproach.
4.1.2. DiscreteparticlemodelwithLagrangianframe
4.1. Trends DPMusingLagrangian frameofreferenceisthesuitabletech-
niquetosimulatecombustionandgasificationoffuelsinfreeboard
4.1.1. TFMEulerianeEulerianandDEMeCFD area. In mainstream simulation models of gas-fluidized beds,
CFDmodelingofthedensebedareaiscomplicatedandaccuracy Lagrangianmodelsareonlyusedforthesolidphase,inwhichthe
inresultsisnotsufficient.Duringlastdecade,massconservationand particles are represented by perfect spheres for computation.
momentumbalanceforgasandsolidhavebeenappliedtosimulate Lagrangianmethodsassumeasmallparticlediameterascompared
the hydrodynamics of bubbling fluidized bed. DEM (Discrete ele- tothegasphasecomputationalgrid.Thisassumptionbreaksdown
mentmethod)isbasedonmoleculardynamicsandtwofluidmodel whenlargeparticles are gasified in moderatesize fluidized beds.
(TFM)isbasedontheassumptionthatthegasandparticulatephases ForLagrangianmodelofdifferentfuelsaparticlesizedistributionis
formtwointer-penetratingcontinuum.Tomodelcomplexdensebed prescribed and the corresponding initial particle diameters are
with combustion and gasification issues and with the millions of assumed to remain constant during simulation. The chemistry
particles, huge computational times put DEM method at a dis- involvedconsidersdevolatilization,heterogeneouscharconversion
advantage. In comparison to DEMeCFD, EeE TFM saves computa- andgasphasesreactions.
tional time. To study combustion and gasification, the EeE TFM Present trends in CFD modeling of fluidized beds using above
approach ismore suitableforcoal withsome approximations. For model is used to find various gas compositions, devolatilization,
biomasslikebark,cottonstalksoranyothertype,thereisvariationof heat flux, temperature, trajectories of particles, ash aspects. Con-
particlestream,density,porosityandthesizeofparticle(rectangular ventional fuel (coal) is used in most of cases. Most the cases are
orcylindrical),whichcausesproblemsduringmodeling.Themajor solved for commercial boilers or three-dimensional geometries.
hurdleinpredictionofaccuratesimulationresultsinthesecasesis Althoughsomeauthorsusedbiomassbutassumptionunderlying
complexityofbiomass.Formultiscaleresultsveryfinemeshreso- them (spherical shape) is same for all the particles. Species gas
lutionisrequired,whichrequireshugecomputationalpower.Pre- composition,heatreleasebyparticlesisgenerallymatchingforall
sent Eulerian technique and present computational power fails to thecases.
predictdensebedcharacteristicinthecaseofbiomassparticles. In one of case [105] it is being used in dense bed to look the
IntheEeETFMpresenttrendsareusedtopredictthecharac- characteristics of biomass in simple two-dimensional config-
teristicoffuelindensebedanditisdonemainlyforlabscaleunits. uration.Duetotheverylargenumberofparticlesinvolvedindense
ThefocusofmostofresearchdoneisforLabscaleunitsanditis beds,DPMapproachbecomeprohibitivelyexpensiveandmakingit
focused onpredicting solid volume fraction, i.e. qualitative infor- unsuitableforindustrialdensebeds.
mation. Researchers used CFD to study devolatization behavior, The computational time reported for simulationwith discrete
charoxidation,charparticlephysicalmovementinbed.EeETFM particleLagrangianapproachiscomparativelyverylessascompare
CFDmodelingisusedinliteraturetolooktheemissionsforsimple toEulerianapproach.AtpresentdiscreteparticleLagrangianmodel
two-dimensional or lab scale units. The quantitative information isworkedsuccessfullyforfreeboard/riseroffluidizedbedtostudy
forproductsofcombustionlikecarbondioxide,carbonmonoxide, combustionandgasificationissues.
SO2 and nitrogen emissions is studied in literature. Sensitivity
analysisisanotherissuewhichisbeingtouchedinliterature.Itis 4.2. Challenges
foundinliteraturethatbedmaterialishavinglittleornoeffecton
combustion/gasificationprocess. Present industrial units are mostly FB combustors. Simulating
The modelingof combustion, gasification and pyrolysis in flu- dense bed considering all physical and chemical reactions is
idizedbedispossiblewithextracodeinsidepresentAnsysFluent achallenge.Theactualdensebedisacomplexthing.Itismixtureof
Software.Thecomputationalcostofsuchsimulationsisveryhigh, sand,air,fuel,charandash.Thefuelfedtodensebedisamixtureof
even for two dimensions or lab scale units. The extensive code differentsizeofparticles.Uniformsizeoffuelparticlesinrealplant
developmentandtheextremelyhighamountofmemoryallocation is notpossible. The physicalcharacteristicsand chemical compo-
have been slowed down the simulations significantly. The mass, sition of biomass material influence how it can best be utilized.
momentumandenergysourcesofaninertmaterial,airandfuelsin Uponrapidheating,somebiofuelshavehighgasyieldsindense
Eulerianphaseincombustionandgasificationinthreedimensions bed, rendering them suitable for gasification and reburn applica-
wouldmakethingsverycomplicated. tions, but simulating them is major challenge for CFD. Very few

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 611
quantitativeresultsarefoundinliteratureforindustrialscaleflu- 4.3. FutureofCFDinfluidizationindustry
idizedbedboilers.
Although the CFD modeling is used to study combustion and
(a) Hydrogentocarbonmonoxideratio gasificationinfluidizedbedanditwillbenefittheunderstandingof
thedynamicsandphysicsofafluidizationoperation,butaidinthe
Quantification of hydrogen to carbon monoxide ratio in fluid- optimizationanddesignofexistingandnewequipments,laband
izedbedgasifierduringgasificationisacriticalissuethanneedsto commercialunits,constraintsaretherequirementsforfaster,easier
beexplored. andlessexpensiveCFDtechniques.Thefuturegrowthinapplica-
tionofCFDincombustionandgasificationinfluidizedbedboilers
(b) Fuelcharacteristics should not only be qualitative but it should be quantitative and
effectiveinwork.
PresentresearchinCFDfailstopredictaboutfuelcharacteristics Inthecomingyearsthecontinuedhighrateofadvancementin
in fluidized bed. The evolution of biomass particle size, density, computer power and in CFD software development will turn
porosity and composition during combustion and gasification in automatic design and optimization in realities and the develop-
dense bed are still unknown. These variables are affected those ment of fluidization with thermo-chemical reactions. All these
variablesareexpectedtogreatlyimpactboththehydrodynamicsof developmentswillcontributeCFDtobecomingamaturediscipline
bedandproductreleaseafunctionoftime. and a powerful engineering tool in this field. As a result, more
widespreadandrapid adoptionof theuseofCFDin thecomplex
(c) Fragmentation fluidizedbedindustrywilltakeplaceinfuture.
Allthereactivefluidizedbedstudieshaveconsideredonlyglobal 5. Conclusions
conversionstepsormulti-stepkineticschemesinvolvingonlyafew
majorspecies.Fragmentationoffuelintodensebedismajorchallenge This paper summarized the CFD modeling tool to study com-
thatmodernCFDmodelsfaced.Simulatingthecompleteprocessof bustionandgasificationoffuelsinfluidizedbeddevices.Thereis
pyrolysis,onecanhavearealisticviewofwhatishappeninginsidethe evidencethatCFDcanbeusedasapowerfultooltopredictchar-
reactor.Reactordesignscanbeoptimizedforefficientcharentrain- acteristicsoffuelsduringcombustionandgasificationprocessesin
ment,somethingthatwouldincreasebio-oilyields.Fewofauthors fluidizedbedunits.
triedtolooktarandnitrogeninfluidizedbed.Themodelsmentioned CFDhasplayedanactivepartinanalysisofthedistributionof
predicttheamountsoftar,gas,andcharreleasedduringpyrolysis,but products, heat flux, flow, temperature, ash deposits, CO, SOx and
the quantitative yields of the main gas species are not predicted. NOxemissionsduringcombustionandgasificationoffuelsinflu-
Quantitativeyieldofvariousgasesismajorchallenge.Fewbiofuels idized bed. These parameters could affect the performance and
havehighcharyieldsascomparetootherandarebettersuitedforco- design.NoevidenceofEeETFMCFDmodelinfluencingthedesign
firingindirectcombustionconfigurations. ofindustrialfluidizedbedunitswhencombustionandgasification
issuesinvolved.
(d) Charinventory The CFD model results are satisfactory and have made good
agreements with the experimental data in manycases. However,
Charinventoryisthemajorproblemincirculatingfluidizedbed. the simulations still have many approximate models as well as
Although fewauthors tried to study the solid volume fraction of someassumptions.ToensureCFDsimulationsaremorethanjust
sandincirculatingfluidizedbed.Thecharcomesinthebedalong theoretical exercises like two-dimensional units, experimental
withsand.ThisisimportantissuewhereapplicationofCFDneeds validationisnecessarytofacilitatethemodelaccuracy.
tobeexplored. CFD modeling of commercial fluidized bed considering com-
bustion and gasification aspects using EulerianeEulerian TFM
(e) Fueltrajectoryindensebeds approachstillrequiredtoexplore.Duetovariationinsizeofbio-
massparticlestheEulerianeEulerianapproachwithbiomasscon-
Thefuelparticlesinjectedontopofabedcouldremainontop, sidering combustion/gasification issues in dense fluidized beds is
sinktothebottomofthebedorbecaughtinarecirculationregion. notpossibleuntilwideapproximationsarechosen.Nostudieshave
Differentparticlesizedistributioniscausingdifferenttrajectoriesof been reported on CFD simulation investigating both the bed and
fuel,whichinvolvedifferenttypesofphysicalprocessanddifferent freeboard simultaneously and applied either technique to both
heattransfermodels.Thisisanimportantareawhereapplicationof densebedandriser/freeboardofcommercialunits.
CFDneedstobeexplored. TheunderstandingofEuleriantechniquetofluidizedbedswith
thermo-chemicalreactionsisstillinadevelopmentstage.Several
(f) Ashsintering mechanismmodelsare availablebutnoneof themissuitablefor
industrialscaleboilerswhenthenthermo-chemicalconversionof
Ashsinteringindensebedistheotherareawhichneedstobe fuelsisconsidered.AtpresentstageapplicationofDPMLagrangian
explored. techniquewith gas phase tofreeboard with thermo-chemical re-
actionsisseemstosatisfyfullywhichcanaffectandenhancethe
(g) Exitgascomposition performancetoindustrialscalefluidizedbedboilers.
Therearemanyaspectsoffluidizedbedswheretheapplication
Quantification of exit gas composition in reacting dense bed is of CFD modeling still needs to be explored. The aspects like fuel
anotherareawhereapplicationofneedstobeexplored.Althoughfew combustion/gasificationbehaviorduringfeeding,mixingoffuelin
studiesarereportedforlabscaleunits,butresultsofthesearefaraway thedensebed,ashsintering,fuelcharacteristics,charreactivityand
formakingsolidconclusiontowardsindustrialscalefurnacedesign. inventory,fragmentationoffuelindensebedwithCFDstillneeds
Withtheproperchoicesofbiomass,coal,densebedandfree- tobeexplored.
board and riser reductions in pollutant and net greenhouse gas Althoughtherearestillsomeobstaclessuchasinabilityinac-
emissionscanberealizedwithaidofCFD. curatesimulationoflarge3Dproblemsonanaffordablecomputer,

Author's personal copy
612 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
in particular, in large-scale sophisticated plants, the trend of bubbling fluidized bed boiler, International Journal Energy Cleaner Envi-
widespread application of CFD in the fluidization industry will ronment8(2007)2.
[20] D.Lundmark,C.Mueller,R.Backman,M.Zevenhoven,B.J.Skrifvars,M.Hupa,
continue in the 21st century. With the progressing of the com- CFDbasedashdepositionpredictioninaBFBCfiringmixturesofpeatand
puting power and the development of chemical and physical forestresidue,JournalofEnergyResourcesTechnology,Transactionsofthe
models,theCFDapplicationinthecombustionandgasificationof ASME132(2010)3.
fuelsinfluidizedbedunitswillmorewidelyspreadinthefuture. [21] S
ic
.
a
R
l
a
m
ve
o
ll
d
i,
el
A
in
.
g
Pe
o
rd
f
ic
b
h
u
i
b
z
b
zi
l
,
in
G
g
.B
fl
a
u
r
i
i
d
g
i
o
z
z
e
z
d
i,D
be
e
d
scr
c
i
o
p
m
tio
b
n
u
,
st
a
i
p
o
p
n
lic
in
ati
w
on
a
s
st
a
e
n
-t
d
o-
n
e
u
n
m
er
e
g
r
y
-
plants,ProgressinEnergyandCombustionScience34(2008)224e253.
[22] M.Rozainee,S.P.Ngo,A.A.Salema,K.G.Tan,Computationalfluiddynamics
Acknowledgements modeling of rice husk combustion in a fluidized bed combustor, Powder
Technology203(2010)331e347.
[23] M. Agraniotis, D. Stamatis, P. Grammelisand Kakaras, Numerical inves-
Financially support from Johan Gadolin scholarship program, tigationonthecombustionbehaviorofpre-driedGreeklignite,Fuel88(12)
Abo Academy University, Finland is gratefully acknowledged for (2009)2385e2391.
thiswork. [24] A.Brink,O.Karlström,M.Hupa,Asimplifiedmodelforthebehavioroflarge
biomassparticlesinthesplashingzoneofabubblingbed,in:Proceedingof20th
InternationalConferenceonFluidizedbedcombustion,2009,pp.764e767.
[25] W.Yuxin,L.V.Junfu,J.Zhang,L.Qing,YueGuangxi,Y.Zhang,Y.Long,Z.Yang,
References Conceptualdesignofan800MWsupercriticalpressurecirculatingfluidized
bedboiler,BoilerTechnology3(48)(2004)1e5.
[1] W.M.Gao,L.X.Kong,P.D.Hodgson,Computationalsimulationofgasflowand [26] EnergyEfficiencyinThermalUtilities.AGuideBookforEnergyManagersand
heattransfernearanimmersedobjectinfluidizedbeds,AdvancesinEngi- Auditors, Bureau of Energy Efficiency, Ministry of Power, Government of
neeringSoftware38(2007)826e834. India,2005.
[2] Y.Behjat,S.Shahhosseini,S.H.Hashemabadi,CFDmodelingofhydrodynamic [27] M.Hupa,Currentstatusandchallengeswithinfluidizedbedcombustion,in:
andheattransferinfluidizedbedreactors,InternationalCommunicationsin N.Syred,A.Khalatov(Eds.),AdvancedCombustionandAerothermalTech-
HeatandMassTransfer35(2008)357e368. nologies,Springer,Netherland,2005,pp.87e101.
[3] N.V.Gnanapragasam,B.V.Reddy,Numericalmodelingofaxialbed-to-wall [28] L.M.Armstrong,S.Gu,K.H.Luo,Parametricstudyofgasificationprocessesin
heattransferinacirculatingfluidizedbedcombustor,InternationalJournal aBFBcoalgasifier,IndustrialandEngineeringChemistryResearch50(2011)
ofHeatandMassTransfer52(2009)1657e1666. 5959e5974.
[4] W.Wang,B.Lu,N.Zhang,Z.Shi,J.Li,AreviewofmultiscaleCFDforgasesolid [29] T.Kimura,T.Kojima,Numericalmodelforreactionsinajettingfluidizedbed
CFBmodeling,InternationalJournalofMultiphaseFlow36(2010)109e118. coalgasifier,ChemicalEngineeringScience47(1992)2529e2534.
[5] X.Z.Chen,D.P.Shi,X.Gao,Z.H.Luo,AfundamentalCFDstudyofthegase [30] B.Jicheng,L.Chunhao,K.C.Aoki,S.Umea,T.Kojima,Anumericalsimulation
solidflowfieldinfluidizedbedpolymerizationreactors,PowderTechnology ofjettingfluidizedbedcoalgasifier,Fuel76(4)(1997)285e301.
205(2011)276e278. [31] K.Myohanen,T.Hyppanen,Athree-dimensionalmodelframeformodeling
[6] W.Zhou,C.S.Zhao,L.Duan,C.R.Qu,X.P.Chen,Two-dimensionalcomputa- combustionandgasificationincirculatingfluidizedbedfurnaces,Interna-
tionalfluiddynamicssimulationofcoalcombustioninacirculatingfluidized tionalJournalofChemicalReactorEngineering9(A25)(2011)1e55.
bedcombustor,ChemicalEngineeringJournal166(1)(2011)306e314. [32] P.Pepiot,C.J.Dibble,T.D.Foust,Computationalfluiddynamicsmodelingof
[7] W. Zhou, C.S. Zhao, L. Duan, D. Liu, X.P. Chen, CFD modeling of oxy-coal biomassgasificationandpyrolysis.Computationalmodelinginlignocellu-
combustion in circulating fluidized bed, International Journal of Green- losicbiofuelproduction,in:ACSSymposiumSeries,vol.1052,2010.pp.273e
houseGasControl5(6)(2011)1489e1497. 298,(Chapter12).
[8] WZhou,CSZhao,LDuan,CRQu,JYLu,XPChen,Numericalsimulationon [33] N.G. Deen, M.V. Annaland, M.A. Van der Hoef, J.A.M. Kuipers, Numerical
hydrodynamicsandcombustioninacirculatingfluidizedbedunderO2/CO2 simulationofdensegas-solidfluidizedbeds:Amultiscalemodelingstrategy,
and air atmospheres, in: Proceeding of 20th International Conference on ChemicalEngineeringScience62(2007)28e44.
Fluidizedbedcombustion,2009,pp.883e888. [34] D.Gera,M.Gautam,Y.Tsuji,T.Kawaguchi,T.Tanaka,Computersimulation
[9] Nikolopoulos I., Rampidis, N. Nikolopoulos, P. Grammelis, E. Kakaras, Nu- of bubbles in large-particle fluidized beds, Powder Technology 98 (1998)
mericalinvestigationof3-dtransientcombustingflowina1.2MWthpilot 3847.
powerplant,in:Proceedingof20thInternationalConferenceonFluidized [35] D.Gera, M.Syamlal,T.O. Brien,Hydrodynamicsof particle segregationin
bedcombustion,2009,pp.839e844. fluidizedbeds,InternationalJournalofMultiphaseFlow30(2004)419e428.
[10] K.Myöhänen,T.Hyppänen,A.Vepsäläinen,Modellingofcirculatingfluid- [36] C.Ibsen,E.Helland,B.Hjertager,T.Solberg,L.Tadrist,R.Occelli,Comparisonof
izedbedcombustionwithasemi-empiricalthree-dimensionalmodel,SIMS multifluidanddiscreteparticlemodelinginnumericalpredictionsofgaspar-
2006,in:Proceedingsofthe47thConferenceonSimulationandModelling, ticleflowincirculatingfluidizedbeds,PowderTechnology149(2004)29e41.
2006,pp.194e199. [37] K.Papadikis,A.V.Bridgwater,S.Gu,CFDmodelingofthefastpyrolysisof
[11] ABrink,SBostrom,PKilpinenandMHupa,CFDmodelingofthefateof biomass in fluidised bed reactors, part A: Eulerian computation of mo-
biomass fuel-nitrogen in the freeboard of a 70 MW FBC-new aspects on mentumtransportinbubblingfluidizedbeds,ChemicalEngineeringScience
controllingmechanisms,in:Firstbiennialmeeting,TheScandinavian-Nordic 63(16)(2008)4218e4227.
Section of the Combustion Institute 18th to 20th April 2001, Chalmers [38] K.Papadikis,S.Gu,A.V.Bridgwater,ACFDapproachontheeffectofparticle
UniversityofTechnology,Goteborg,Sweden. sizeoncharentrainmentinbubblingfluidisedbedreactors,Biomassand
[12] A. Brink, C. Mueller, M. Hupa, A modified approach for predicting NOx Bioenergy34(2010)21e29.
emissiontrendsfrombiomassfiredbubblingfluidizedbedboilers,in:Pro- [39] L.M. Armstrong, S. Gu, K.H. Luo, Effects of limestone calcination on the
ceedingof19thFBCconference,May21e24,2006. gasificationprocessesinaBFBcoalgasifier,ChemicalEngineeringJournal
[13] A.Brink,M.Hupa,E.Kurkela,M.Suomalainen,MinimizingNOxemission 168(2011)848e860.
fromawastederivedfuelgasifiergascombustorusingCFDcombinedwith [40] C.E.J.Bakul,V.Y.Gershtein,L.Xianming,ComputationalFluidDynamicsin
detailed chemistry, IFRF CombustionJournal. ISSN: 1562-479X 05(2005). IndustrialCombustion,CRCPress,NewYork,2001.
ISSN:1562-479X1e14. [41] FLUENT 6 User’s Guide, Fluent Incorporated, Centerra Resource Park, 10
[14] R.Zevenhoven,M.Järvinen,Particle/turbulenceinteractions,masstransfer CavendishCourt,LebanonNH03766,2002.
andgas/solidchemistryinaCFBCriser,FlowTurbulenceandCombustion67 [42] D.Lathouwers,J.Bellan,Yieldoptimizationandscalingoffluidizedbedsfor
(2)(2001)107e124. tarproductionfrombiomass,EnergyFuels15(2001)1247e1262.
[15] C. Mueller, A. Brink, M. Hupa, Numerical simulation of the combustion [43] A.M.Eaton,L.D.Smoot,S.C.Hill,C.N.Eatough,Components,formulations,
behaviorofdifferentbiomassesinabubblingfluidizedbedboiler,in:Pro- solutions,evaluation,andapplicationofcomprehensivecombustionmodels,
ceedings of 18th International conference on Fluidized bed combustion, ProgressinEnergyandCombustionScience25(1999)387e436.
Toronto,Ontario,Canada,2005. [44] J.C.Wurzenberger,S.Wallner,H.Raupenstrauch,J.G.Khinast,Thermalcon-
[16] C.Mueller,B.J.Skrifvars,R.Backman,S.Nickull,M.Hupa,Simulationofash version of biomass: comprehensive reactor and particle modeling, AICHE
particle behaviour on surfaces of biomass fired fluidized bed boilers- Journal48(10)(2002)2398e2411.
combination of computational fluid dynamics and advanced ash analysis, [45] J. Pallares, I. Arauzo, A. Williams, Integration of CFD codes and advanced
in:Proceedingsof16thInternationalconferenceonFluidizedbedcombus- combustionmodelsforquantitativeburnoutdetermination,Fuel86(2007)
tion,Reno,NevadaUSA,Sustainablefuels-Biomass,PaperNo.139,2001. 2283e2290.
[17] C.Mueller,B.J.Skrifvars,R.Backman,M.Hupa,Ashdepositionpredictionin [46] B.E.Launder,D.B.Spalding,LecturesinMathematicalModelsofTurbulence,
biomassfiredfluidizedbedboilers-combinationofCFDandadvancedfuel AcademicPress,London,1972.
analysis,ProgressinComputationalFluiddynamics3(2e4)(2003)112e120. [47] L.Yu,J.Lu,X.Zhang,S.Zhang,Numericalsimulationofthebubblingfluidized
[18] C.Mueller,D.Lundmark,B.J.Skrifvars,M.Hupa,CFDbasedashdeposition bedcoalgasificationbythekinetictheoryofgranularflow(KTGF),Fuel86
prediction in a bubbling fluidised bed combustor firing mixtures of bio- (2007)722e734.
masses,in:ProceedingFinnish-SwedishFlameDays,Vassa,Finland,2002. [48] C.Lun,S.Savage,D.Jeffrey,N.Chepurniy,Kinetictheoriesforgranularflow:
[19] D. Lundmark, C. Mueller, B.J. Skrifvars, M. Hupa, Computational fluid dy- InelasticparticlesinCouetteflowandslightlyinelasticparticlesinageneral
namic modeling of combustion and ash deposition in a biomass co-fired flowfield,JournalofFluidMechanics140(1984)223e256.

Author's personal copy
R.I.Singhetal./AppliedThermalEngineering52(2013)585e614 613
[49] J.Jenkins,S.Savage,Atheoryfortherapidflowofidenticalsmoothnearly [77] S. Gerber, F. Behrendt, M. Overmann, An Eulerian modeling approach of
elasticsphericalparticles,JournalofFluidMechanics130(1983)187e202. wood gasification in a bubbling fluidized bed reactor using char as bed
[50] D. Gidaspow, Multiphase Flow and Fluidization: Continuum and Kinetic material,Fuel89(2010)2903e2917.
TheoryDescriptions,AcademicPress,London,1994. [78] X.F.Wang,B.Jin,W.Zhong,Three-dimensionalsimulationoffluidizedbed
[51] D.J.Gunn,Transferofheatormasstoparticlesinfixedandfluidizedbeds, coalgasification,ChemicalEngineeringandProcessing48(2009)695e705.
InternationalJournalofHeatandMassTransfer21(1978)467e476. [79] Z.Deng,R.Xiao,B.Jin,H.Huang,L.Shen,Q.Song,L.Qianjun,Computational
[52] H.K. Versteeg, W. Malalasekera, An Introduction to Computational Fluid fluiddynamicsmodelingofcoalgasificationinapressurizedspout-fluidbed,
Dynamics:TheFiniteVolumeMethod,PearsonPublishers,2007. EnergyandFuels22(2008)1560e1569.
[53] D.Liu,X.Chen,W.Zhou,C.SZhao,Simulationofcharandpropanecom- [80] L.M. Armstrong, S. Gu, K.H. Luo, CFD modelling of the co-gasification of
bustioninafluidizedbedbyextendingDEMeCFDapproach,Proceedingsof biomassandcoalparticlesinfluidizedbeds,in:ProceedingsoftheBioten
theCombustionInstitute33(2)(2011)2701e2708. ConferenceonBiomassBioenergyandBiofuels2010,CRCPress,Birmingham,
[54] Y.Wang,L.Yan,CFDmodelingofafluidizedbedsewagesludgegasifierfor GB,2010.
syngas,Asia-PacificJournalofChemicalEngineering3(2008)161e170. [81] L. He, E. Schotte, S. Thomas, A. Schlinkert, A. Herrmann, V. Mosch, V.
[55] Y. Geng, D. Che, An extended DEMeCFD model for char combustion in Rajendran,S.Heinrich,2009,Woodgasificationinalab-scalebubblingflu-
a bubbling fluidized bed combustor of inert sand, Chemical Engineering idizedbed:experimentandsimulation,in:Proceedingof20thInternational
Science66(2011)207e219. Conferenceonfluidizedbedcombustion,Xian,China,2009,pp.686e692.
[56] D.Rong,M.Horio,DEMsimulationofcharcombustioninafluidizedbed”,in: [82] Y.L.Tang,D.JunLiu,Y.HongLiu,Q.Luo,3Dcomputationalfluiddynamics
Second International Conference on CFD in the Minerals and Process In- simulationofnaturalcokesteamgasificationingeneralandimprovedflu-
dustriesCSIRO,Melbourne,Australia,1999,pp.65e70. idizedbeds,EnergyFuels24(2010)5602e5610.
[57] W.Zukowski,J.Baron,E.M.Bulewicz,B.Kowarska,Propagationofreaction [83] R.S. Miller, J. Bellan, A generalized biomass pyrolysis model based on
between bubbles with a gas burning in a fluidized bed, Combustion and superimposedcellulose,hemicellulose,andligninkinetics,CombustionSci-
Flame156(2009)1445e1452. enceandTechnology126(1997)97e138.
[58] S.H.Enestam,M.K.Fabritius,S.K.Hulkkonen,J.T.R.öppänen,Controlofash [84] L.Qianjun,M.Zhang,W.Zhong,X.Wang,R.Xiao,B.Jin,Simulationofcoal
relatedoperationalproblemsinBFBcombustionofbiofuelsandwaste,in: gasification in a pressurized spout-fluid bed gasifier, Canadian Journal of
Proceedings of the 17th International Conference on Fluidized Bed Com- ChemicalEngineering87(2)(2009)169e176.
bustion,2003,pp.541e546. [85] S.Gerber,F.Behrendt,M.Oevermann,ComparativestudyofEulereEulerand
[59] C.Mueller,D.Lundmark,B.J.Skrifvars,R.Backman,M.Zehevhovan,M.Hupa, EulereLagrangemodellingofwoodgasificationinadensefluidizedbed,in:
CFDbasedashdepositionpredictioninaBFBfiringmixturesofpeatand Proceedingofthe20thInternationalConferenceonFBC,2009,pp.693e699.
forestresidue,in:Proceedingof17thInternational(ASME)Conferenceon [86] P.Cornejo,O.Farıas,Mathematicalmodelingofcoalgasificationinafluidized
FluidizedBedCombustion,Jacksonville,Florida.PaperNo.102,2003. bedreactorusingaEuleriangranulardescription,InternationalJournalof
[60] D.J. Farias, F. Severino, F. Maciel, R. Lucena, S. DaSilva, D. Jornandes, CFD ChemicalReactorEngineering9(A2)(2011)1e3.
study on natural gas fluidized bed combustors, in: IChE Annual Meeting, [87] S.Karimipour,T.Pugsley,R.J.Spiteri,CFDsimulationofafluidizedbedgasifier
ConferenceProceedings,AIChESpringNationalMeeting,2006. operatingwithlignitecoal,AICHE,AnnualMeeting,Paperno.465a,2010.
[61] S.Noorman,M.V.Annaland,H.Kuipers,Packedbedreactortechnologyfor [88] M.Zhou,L.F.Yan,Q.X.Guo,Q.S.Zhu,Nonpremixedcombustionmodelof
chemical-looping combustion, Industrial and Engineering Chemistry fluidized bed biomass gasifier for hydrogen rich gas, Chinese Journal of
Research46(12)(2007)4212e4220. ChemicalPhysics19(2)(2006)131e136.
[62] S.Noorman,M.V.Annaland,H.Kuipers,Experimentalvalidationofpacked [89] Y.Wang,L.Yan,CFDbasedcombustionmodelforsewagesludgegasification
bed chemical-looping combustion, Chemical Engineering Science 65 (1) inafluidizedbed,FrontiersofChemicalEngineeringinChina3(2)(2009)
(2010)92e97. 138e145.
[63] N.V. Gnanapragasam, B.V. Reddy, M.A. Rosen, Hydrogen production from [90] T.J. Obrien, M. Syamlal, C.Guenther, Computational fluid dynamic simula-
coalusingcoaldirectchemicalloopingandsyngaschemicalloopingcom- tions of chemical reactive fluidized bed process, in: Third International
bustion systems: assessment of system operation and resource re- ConferenceonCFDintheMineralsandProcessIndustriesCSIRO,Melbourne,
quirements,InternationalJournalofHydrogenEnergy34(2009)2606e2615. Australia,2003,pp.469e474.
[64] L.Fan,F.Li,S.Ramkumar,Utilizationofchemicalloopingstrategyincoal [91] B. Chalermsinsuwan, P. Kuchonthar, P. Piumsomboon, CFD modeling of
gasificationprocesses,Particuology6(2008)131e142. taperedcirculatingfluidizedbedreactorrisers:hydrodynamicdescriptions
[65] A. Lyngfelt, B. Leckner, T. Mattisson, A fluidized-bed combustion process andchemicalreactionresponses,ChemicalEngineeringandProcessing49
withinherentCO2separation;applicationofchemical-loopingcombustion, (2010)1144e1160.
ChemicalEngineeringScience56(10)(2001)3101e3113. [92] A.K.M.M.Mazumder,T.Wang,J.R.Khan,Designandsimulationofahybrid
[66] S.R. Son, S.D. Kim, Chemical-looping combustion with NiO and Fe2O3 in entrainedflowandfluidizedbedmildgasifierPart1eDesignconsiderations
a thermobalance and circulating fluidized bed reactor with double loops, anddevelopmentofamultiphasemodel,in:ProceedingsoftheASME2011
IndustrialEngineeringandChemicalResearch45(8)(2006)2689e2696. InternationalMechanicalEngineeringCongressandExpositionIMECE,2011,
[67] M.M.Hossaina,H.I.DeLasa,Chemical-loopingcombustion(CLC)forinherent pp.1e12.
co2separationseareview,ChemicalEngineeringScience63(18)(2008) [93] A.K.M.M.Mazumder,T.Wang,J.R.Khan,Designandsimulationofahybrid
4433e4451. entrained-flow and fluidized bed mild gasifier part 2 e case study and
[68] H. Kruggel-Emden, S. Rickelt, F. Stepanek, A. Munjiza, Development and analysis,in:ProceedingsoftheInternationalMechanicalEngineeringCon-
testing of an interconnected multiphase CFD-model for chemical looping gressandExpositionIMECE2011,Denver,Colorado,USA,2011,pp.1e12.
combustion,ChemicalEngineeringScience65(2010)4732e4745. [94] Q.J.Li,X.J.Pan,D.P.Zhang,B.Jiang,Numericalsimulationofbiomassgas-
[69] J.E.Readman,A.Olafsen,J.B.Smith,R.Blom,Chemicalloopingcombustion ificationinafluidizedbed,ChineseJournalofPowerEngineering8(2011)
usingNiO/NiAl2O4:mechanismandkineticsofreduction-oxidation(Red-ox) 624e629.
reactionsfrominsitupowderXraydiffractionandthermogravimetricex- [95] E.C.Zabetta,T.Norstrom,P.Kilpinen,M.Hupa,NOxReductionbyStagingin
periments,EnergyFuels20(2006)1382e1387. Biomass Combustion e A Kinetic and CFD Modelling Study, The Joint
[70] W.Shuai,Y.Yang,H.Lu,J.Wang,P.Xu,LiuGuodong,Hydrodynamicsimu- SwedishFinnishFlameDay,IFRF,Vexjo,Sweden,1999,pp.1e17.
lation of fuel-reactor in chemical looping combustion process, Chemical [96] D.Sofialidis,O.Faltsi,Simulationofbiomassgasificationinfluidizedbedsusing
EngineeringResearchandDesign8(9)(2011)1501e1510. computationalfluiddynamicsapproach,ThermalScience5(2)(2001)95e105.
[71] Z. Deng, R. Xiao, B. Jin, Q. Song, H. Huang, Multiphase CFD modeling for [97] A.Brink,S.Bostrom,P.Kilpinen,M.Hupa,Modelingnitrogenchemistryin
achemicalloopingcombustionprocess(fuelreactor),ChemicalEngineering thefreeboardofbiomassFBC,IFRFCombustionJournalA-07(2001)1e14.
Technology31(12)(2008)1754e1766. [98] M.Gräbner,S.Ogriseck,B.Meyer,Numericalsimulationofcoalgasification
[72] K.Mahalatkar,J.Kuhlman,E.D.Huckaby,T.O.Brien,Simulationsofacircu- atcirculatingfluidizedbedconditions,FuelProcessingTechnology88(10)
latingfluidizedbedchemicalloopingcombustionsystemutilizinggaseous (2007)948e958.
fuel,OilandGasScienceandTechnologyReview,IFPEnergiesNouvelles66 [99] H.M.Xiao,X.Q.Ma,K.Liu,Z.S.Yu,Numericalsimulationofsludgedryness
(2)(2011)301e331. underfluegasatmosphereintheriserofafluidizedbed,in:Proceedingof
[73] X.Wang,B.Jin,Y.Zhang,W.Zhong,S.Yin,Multiphasecomputationalfluid 20thInternationalConferenceonFBC,2009,pp.812e816.
dynamics(CFD)modelingofchemicalloopingcombustionusingaCuO/Al2O3 [100] Z.S. Yu, X.Q. Ma, Z.Y. Lai, H.M. Xiao, CFD modelling applied to the co-
oxygencarrier:effectofoperatingconditionsoncoalgascombustion,Energy combustionofpapersludgeandcoalina130t/hCFBboiler,in:Proceed-
Fuels25(2011)3815e3824. ingof20thInternationalconferenceonfluidizedbedcombustion,2009,pp.
[74] B.Jin,R.Xiaoy,Z.Deng,Q.Song,Computationalfluiddynamicsmodelingof 1165e1170.
chemicalloopingcombustionprocesswithcalciumsulphateoxygencarrier, [101] R. Wischnewski, L. Ratschow, E.U. Hartge, J. Werther, 3D-simulation of
InternationalJournalofchemicalReactorEngineering7(2009)A19. concentration distributions inside large-scale circulating fluidized bed
[75] Z.Deng,R.Xiao,B.Jin,Q.Song,Numericalsimulationofchemicallooping combustors,in: Proceedingof20th InternationalConference onFluidized
combustion process with CaSO4 oxygen carrier, International Journal of bedcombustion,2009,pp.774e779.
GreenhouseGasControl3(4)(2009)368e375. [102] L. Ratschow, R. Wischnewski, E.U. Hartge, J. Werther, Three-dimensional
[76] J. Jung, I.K. Gamwo, Multiphase CFD-based models for chemical looping simulationoftemperaturedistributionsinlarge-scalecirculatingfluidized
combustion process: fuel reactor modeling, Powder Technology 183 (3) bedcombustors,in:Proceedingof20thInternationalConferenceonFluid-
(2008)401e409. izedbedcombustion,2009,pp.780e785.

Author's personal copy
614 R.I.Singhetal./AppliedThermalEngineering52(2013)585e614
[103] P.Jinsoo,T.Y.Mun,J.S.Kim,G.H.Rhee,Numericalsimulationofwoodywaste [108] H.M.Yan,C.Heidenreich,D.K.Zhang,Mathematicalmodelingofabubbling
gasificationintwostagefluidizedbedgasifier,JournalofKoreaSolidWastes fluidized-bedcoalgasifierandthesignificanceofnetflow,Fuel77(1998)
Recycling27(8)(2010)700e708. 1067e1079.
[104] S. Dale, M.C. Samuel, J. O’Rourke Peter, EulerianeLagrangian method for [109] R.M.Taha,ModellingandSimulationforCoalGasification,IEAPubs,2000.
three-dimensionalthermalreactingflowwithapplicationtocoalgasifiers, [110] D.Kunii,O.Levenspiel,FluidizationEngineering,Butterworth-Heinemann,1991.
ChemicalEngineeringScience66(2011)1285e1295. [111] P.Basu,CombustionandGasificationinFluidizedBeds,TaylorandFrancis,
[105] S.Gerber,M.Overman,EulereLagrange modeling ofwood gasificationin 2006.
densefluidizedbeds,in:FirstERCOFTACconferenceonsimulationofmul- [112] S.Oka,FluidizedBedCombustion,MarcelDekkerInc,2003.
tiphaseflowsingasificationandcombustion,2011,pp.40e46. [113] M.L.D.Santos,SolidFuelsCombustionandGasification,MarcelDekkerInc,
[106] M.Weng,J.Plackmeyer,Comparisonbetweenmeasurementsandnumerical 2005.
simulationofparticleflowandcombustionattheDuisburgCFBCplant,in: [114] Y. Tsuji, T. Kawaguchi, T. Tanaka, Discrete particle simulation of two-
Proceeding of International conference on circulating fluidized beds and dimensionalfluidizedbed,PowderTechnology77(1)(1993)79e87.
fluidizationtechnology-CFB-10,May1e5,2011. [115] H.Kobayashi,J.B.Howard,A.F.Sarofim,Coaldevolatilizationathightem-
[107] W.Zhou,C.S.Zhao,L.B.Duan,X.P.Chen,C.Liang,Two-dimensionalcom- peratures,in:Proc.16thInternationalSymposiumonCombustion,1976.
putationalfluiddynamicssimulationofnitrogenandsulfuroxidesemissions [116] C.X.Chen,M.Horio,T.Koijima,Numericalsimulationofentrainedflowcoal
inacirculatingfluidizedbedcombustor,ChemicalEngineeringJournal173 gasifiers. Part I: Modeling of coal gasification in entrained flow gasifier,
(2011)564e573. ChemicalEngineeringScience55(2000)3861e3874.
VViieeww ppuubblliiccaattiioonn ssttaattss
