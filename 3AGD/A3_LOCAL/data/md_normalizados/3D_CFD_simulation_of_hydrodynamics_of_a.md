# 3D_CFD_simulation_of_hydrodynamics_of_a

**Fonte**: 3D_CFD_simulation_of_hydrodynamics_of_a.pdf  
**Data de conversão**: 2025-07-30 15:09:20  
**Origem**: base_relevantes

---

ChemicalEngineeringJournal162 (2010) 821–828
ContentslistsavailableatScienceDirect
Chemical Engineering Journal
journal homepage: www.elsevier.com/locate/cej
3D CFD simulation of hydrodynamics of a 150MW circulating fluidized
e
bed boiler
NanZhanga,b,BonaLua,b,WeiWanga, ,JinghaiLia
∗
aInstituteofProcessEngineering,ChineseAcademyofSciences,ZhongguancunBeiertiao1,HaidianDistrict,Beijing100190,China
bGraduateUniversityoftheChineseAcademyofSciences,Beijing100049,China
a r t i c l e i n f o a b s t r a c t
Articlehistory: AnEuleriangranularmultiphasemodelwithadragcoefficientbasedontheenergyminimizationmulti-
Received5February2010 scale(EMMS)modelwasusedtoperformathree-dimensional(3D),full-loop,time-dependentsimulation
Receivedinrevisedform23June2010 ofhydrodynamicsofa150MWecirculatingfluidizedbed(CFB)boiler.Simulationresultswerepresented
Accepted25June2010
intermsofthepressureprofilearoundthewholeloopofsolidscirculation,profilesofsolidsvolume
fractionandsolidsverticalvelocity,aswellasthenon-uniformdistributionofsolidfluxesintotwo
Keywords: parallelcyclones.
CFD
© 2010 Elsevier B.V. All rights reserved.
Circulatingfluidizedbed
Multiphaseflow
Simulation
Fluidization
Hydrodynamics
1. Introduction andcombustion,etc.[5–7],inwhichthefurnacewasdividedinto
four zones according to the flow characteristics, each with indi-
Owing to the advantages of low emission and fuel flexibility, vidualmodule.Thismodelhasbeenappliedtoa12MW boiler
th
circulating fluidized bed (CFB) boilers for utility power genera- constructed in Chalmers University of Technology, Sweden. The
tionhavebeenincreasinginthepastdecadesinbothcapacityand influenceofmixingandgeometryontheoverallperformancewas
quantity.Properdesignandscale-upofaCFBboilerrelyheavily emphasized with validation against measured data. Pallares and
onitshydrodynamicunderstanding.Tothisend,experimentation Johnsson [8,9] divided CFB boiler into six zones in their reports,
is certainly an approach, while numerical simulation is another, reflecting different understanding of the hydrodynamics inside
receiving growing interest with the rapid development of com- boilers.Inpractice,howtoappropriatelydescribethehydrodynam-
putationaltechnologies,especiallycomputationalfluiddynamics icswithempiricallyreducedmodelsremainsachallenge,especially
(CFD). for the complex system like a CFB boiler with strong coupling
Reported simulations of CFB boilers in literature are mostly betweendifferentzonesarounditsentireloop.
basedonempiricalmodels,fromwhichwecanseeagrowingcom- CFDsimulationenablesmoredetailedhydrodynamicsdescrip-
plexityintermsofmultiphaseflowhydrodynamics.Forexample, tionandthusreceivesgrowingattentionsinrecentyears[10–12].
startingwithacombinationofzero-dimensionalsolidmassbalance FlourandBoucker[10]reportedsimulationsofanindustrialCFB
modelandaone-dimensional(1D)gaseousandsolidspeciesmodel test-rigbyusingthecodeESTET-ASTRID,inwhichtheyproposed
[1],Hyppänen’sgrouphaverecentlyturnedtothree-dimensional anewdefinitionofmeandiametertobetterclosethedragforce
(3D)descriptionofgaseousandsolidspecies[2–4]andpresented andintroducedaporositymodelestimatingthepressuredropon
simulationsofdifferentboilersrangingfrom15MWe[2],235MWe thefluidizationregime.Xiao[11]presentedaCFDsimulationofa
[3], up to 460MWe utility facilities [4]. Based on empirical flow 135MWeCFBboilerwithacorrecteddragforcemodel,andcom-
distribution and combustion behavior in the furnace, Werther’s paredhisresultswithmeasureddata.Hartgeetal.[12]presented
grouphavedevelopedacomprehensive,3Dboilermodelinvolving 3DCFDsimulationsofapilot-scaleCFBriserwithrectangularcross
primary fragmentation, char population balance, devolatilization section and found those simulations with a drag coefficient cor-
relationfromtheenergy-minimizationmulti-scale(EMMS)model
predictedthedensebottomzoneverywell.
CurrentCFDsimulationsareusuallyperformedonlyforthefur-
nacechamber[10–12]andevenwith2Dsimplifications,thereare
∗Correspondingauthor.Tel.:+861082616050;fax:+861062558065.
E-mailaddress:wangwei@home.ipe.ac.cn(W.Wang). onlyafewreportswithregardto3D,full-loopsimulationofCFBs
1385-8947/$–seefrontmatter© 2010 Elsevier B.V. All rights reserved.
doi:10.1016/j.cej.2010.06.033

822 N.Zhangetal./ChemicalEngineeringJournal162 (2010) 821–828
2.2. Dragcoefficientcorrelation
Nomenclature
Under the framework of the EMMS model [16], the hetero-
C dragcoefficient
d geneous gas–solid flow in each grid was characterized with the
ds particlediameter(m)
solid-richdensephase,thegas-richdilutephaseandtheirmeso-
ess coefficientofrestitutionforparticlecollisions
scaleinterface.Theeffectivegas–solidmomentumexchangeowing
g gravitationalacceleration(m/s2)
tothissub-gridstructureislowerthanthatforuniformsuspensions
g radialdistributionfunction,dimensionless
0 [17–19]. To characterize this structure-induced decrease, Wang
Gs solidflux(kg/(m2s))
andLi[18]definedaheterogeneityindexH as:
d
H heterogeneityindexofthedragcoefficientcorrec-
d
tion ˇ
H ,
I
2D
secondinvariantofthedeviatoricstresstensor d≡ ˇ0
p pressure(Pa)
where ˇ is the interphase momentum exchange coefficient cal-
Re Reynoldsnumber
culated from EMMS/matrix model, and ˇ0 is the interphase
Ug superficialgasvelocity(m/s)
momentum exchange coefficient derived from Wen and Yu [20]
v realvelocity(m/s)
foruniformlydistributedparticles,asfollows:
G
˛
reeklette
v
r
o
s
lumefraction
ˇ0= 3
4
C
d
˛s˛gg
d
| v
s
s − vg |˛−g 2.65.
collisionaldissipationofenergy(kg/(ms3))
s Table 1 summarizes the fitted correlation of H
d
for a typical
ˇ interphase momentum exchange coefficient
set of operating conditions. This H was obtained by using the
derivedfromEMMS/matrix(kg/(m3s)) d
two-stepschemeofEMMS/matrixmodel[18,21],andthecluster
ˇ0 interphase momentum exchange coefficient
diameterd ,oneofthekeyparameterstherein,wasobtainedusing
derivedfromWenandYu[20](kg/(m3s)) cl
themethodinreference[19].Thetwo-stepschemeherewasused
s granulartemperature(m2/s2)
tosavetime,andthedragcoefficientfromEMMS/matrixcanalso
k diffusioncoefficientofenergy(kg/(ms))
s be coupled into the Eulerian granular model directly during the
 bulkviscosity(kg/(ms))
calculation.
 shearviscosity(kg/(ms))
 density(kg/m3)
2.3. Geometryandmesh
(cid:2) stress–straintensor(Pa)
angleofinternalfriction(
◦
)
The150MWeCFBboilerwasdesignedbyHarbinBoilerCo.Ltd.
and installed in Guangdong, China. It was a natural-circulation,
Subscripts
480t/hboiler,asshowninFig.1,mainlyconsistingofafurnace,
g gasphase
twohigh-temperatureadiabaticcycloneseparatorsandnaturally-
s solidphase
balancedU-typereturnvalves.Themaincrosssectionofthefurnace
is a rectangle of 15.32 7.22m2; the chamber height is 36.5m;
×
thediameterofthetwocyclonesis8.08m;eachreturnlegiscon-
nectedwithareturnvalve,throughwhichthesolidmaterialsare
[13–15]. To better understand the CFB boiler behavior, we need
distributedintotwopipes,eachwithacoal-feedinlet,backtothe
detailedinformationintermsof,forexample,thedynamicmixing
furnace.Besidestheprimaryairinletsfromthebottom,thereare
ofgasandsolidfuelsbothhorizontallyandvertically,theeffects
26secondaryairinletslocatedattheinclinedbottomwalls,twoat
ofvariousnon-uniformgeometriessuchascoal-feedinlets,solid-
eachsidewalls,theother22distributedatthreeheightsofthefront
returnvalvesandsecondaryair-injectionnozzles,andthepressure
andthebackwalls.Inaddition,twoslag-coolerinletsarelocated
balanceoverthewholeloopofCFBcirculation.Alltheseconsider-
atthefrontoftheinclinedbottomwall.
ations necessitate 3D, full-loop CFD simulations, which may even
Thesimulationdomaincoversthewholeloopofthesolidmate-
be viewed as “virtual experimentation” if with reliable models.
rial as shown in Fig. 1. For convenience, the primary air was
A recent attempt of us has showed the advantages of such vir-
assumedtoenterthefurnaceinplugflowfromthewholebottomof
tualexperimentationwithdetailedvalidationagainstexperimental
thefurnaceandtheloop-sealaerationwasalsosimplifiedintoplug
dataonapilot-scalecold-modelCFB[15].Thispaperistoextend
flowfromitsbottom.Thesolidmaterialsexitingfromthecyclone
ourexperienceonvirtualexperimentationtoinvestigatethehydro-
outletswerereturnedviathecoal-feedinletstobalancethesolid
dynamics around the entire loop of an industrial 150MWe CFB
inventoryintheboiler.
boiler.Simulationresultswereshowedintermsofprofilesofsolids
The boiler was divided into several blocks, in which e.g. the
distribution,non-uniformdistributionofsolidfluxesintotwopar-
connectionsbetweenairinletsandthefurnaceweremeshedwith
allelcyclonesandsoon.Thisworkcanbeexpectedtohelpbetter
polyhedron,andtheothersweremeshedwithhexahedron,allwith
understandtheoverallbehaviorofCFBboilers.
sizescaleof0.1m.ThesurfacemeshisshowninFig.2.Theorigin
pointissetatthecenteroftheprimaryinletatthebottomofthe
2. Model furnace;thex-axisisalongthefront-to-backwalldirection(width
direction);they-axisisalongtheside-to-sidewalldirection(depth
2.1. Governingequations direction),andthez-axisisagainstthegravitydirection.
TheEuleriangranularmodelinFluent®6.3.26wasusedtostudy
2.4. Simulationsettings
theflowbehaviorintheboiler,inwhichthestressofthesolidphase
wasdescribedwiththekinetictheoryofgranularflow;thedrag Theboilerwasconsideredoperatedatthedesigntemperature
coefficientcorrelationwascorrectedwithconsiderationofparticle of 917 C, and atmospheric pressure, which means that the gas
◦
clusters.Moredetailsofthegoverningequationscanbefoundin phase was set with a density of 0.2928kg/m3 and a viscosity of
AppendixA. 4.71 10 5kg/(ms). The solid phase was set with a diameter of
× −

N.Zhangetal./ChemicalEngineeringJournal162 (2010) 821–828 823
Table1
Heterogeneity index calculated for a CFB boiler with (Ug=5.25m/s, Gs=5kg/(m2s), ds=0.2mm), Hd=A(Re+B)C/Hd,max,
Hd,max=1.376.
A =− 0.70 + 3.35 × ˛g− 5.36 × ˛2 g+ 2.93 × ˛3 g
0.65<˛g≤ 0.712 B = 107.42 − 509.47 × ˛g+ 799.18 × ˛2 g− 414.05 × ˛3 g
C = 3.87 − 16.80 × ˛g+ 29.54 × ˛2 g− 17.62 × ˛3 g
A = 0.99 − 2.09 × ˛g+ 0.08 × ˛2 g+ 1.33 × ˛3 g
0.712<˛g≤ 0.976 B = 25.28 − 79.46 × ˛g+ 83.31 × ˛2 g− 29.12 × ˛3 g
C = 0.91 + 4.52 × ˛g− 11.89 × ˛2 g+ 6.76 × ˛3 g
A = 22899.63 − 69915.92 × ˛g+ 71155.28 × ˛2 g− 24138.87 × ˛3 g
0.976<˛g≤ 0.998 B = 53478.28 − 162356.87 × ˛g+ 164292.53 × ˛2 g− 55413.85 × ˛3 g
C =− 39578.26 + 120883.43 × ˛g− 123073.51 × ˛2 g+ 41768.94 × ˛3 g
˛g≤ 0.65or˛g>0.998 Hd=1
Fig.1. Geometryofthewholeloopofthe150MWeCFBboiler.
0.2mmandadensityof2000kg/m3basedonempiricaldata[11]. model[22]wasselectedwithaspecularitycoefficientof0.6forthe
Table 2 summarizes solids properties and Table 3 the boundary solidphase.Itisdifficulttopreciselyestimatetheinitialpacking
andinitialconditions.Thegasvelocitiesatdifferentinletswereset height of solids for a given pressure drop, (cid:8)p, because the solid
accordingtothedesignedgasflowrates,whilethesolidsveloci- materialsinthereturnlegsandcyclonesaredifficulttobudget.By
tiesatthecoal-feedinletsweresetaccordingtothesolidfluxes trialsanderrors,inthisworktheboilerwasinitiallypackedwith
predictedatthetwocycloneoutletsbyusingUDF.Atthecyclone solidsvolumefractionof0.4andpackingheightof2.5minboth
outlets,atmosphericpressurewasprescribed.Atthewalls,theno- thefurnaceandthetworeturnlegs.Ifnotspecified,defaultvalues
slipboundaryconditionwasusedforthegasphaseandapartialslip inFluent®6.3.26wereusedfortheotherparameters.
2.5. Solution
Table2
Solidsproperties.
The Phase Coupled SIMPLE method was chosen for
Properties Setting
pressure–velocity coupling, the first-order upwind scheme
Density 2000kg/m3 was used for discretization of momentum and volume-fraction
Diameter 2
×
10− 4m
equations.Thetimestepsizewas0.0005s.Thesolidfluxesatthe
Granulartemperature Phasepropertya
Granularviscosity Gidaspowa outlets of the two cyclones were monitored to judge when the
Granularbulkviscosity Lunetal.a simulationreachessteadystate,thereafterthetimeaveragingwas
Frictionalviscosity Schaeffera performed.Ingeneral,simulationslastedforabout40sinphysical
a OptionalitemsofsolidspropertiesinFluent®6.3.26. timeandthelast20swereusedfortimeaveraginginouranalysis.

824 N.Zhangetal./ChemicalEngineeringJournal162 (2010) 821–828
Table3
Boundaryandinitialconditions.
Boundaryandinitialconditions Gasphase Solidphase
Flowrate(kg/s) Totalarea(m2) Inletvelocity(m/s)
Primaryairinlet 94.16 50.88 6.32 0
Secondaryairinlet 53.21 0.92 198.01 0
Slag-coolerinlet 8.00 0.75 36.32 0
Loop-sealinlet 2.32 8.02 0.99 0
Coal-feedinlet 12.48 1.16 36.70 UDF
Initialsolidpackingheight 2.5m
Cycloneoutlet Atmosphericpressure
Wall No-slip Partialslip
3. Resultsanddiscussion showninFig.3,thatis,densebottomcoexistingwithdilutetopin
boththefurnacechamberandthereturnlegs.Fig.5(b)showsthat
3.1. Pressuredistribution thesolidsvolumefractionwasnormallylargenearthewalland
smallinthecenterofthefurnace.
Fig.3showsthesimulatedpressurebalanceintheboiler.Itis Fig.6showsprofilesofsolidsvolumefractionatdifferentheights
obviousthatthepressuregradientislargeatthebottomandcom- withy-averagedvaluesalongwidth(x-)direction(Fig.6(a))andx-
parativelysmallatthetopinthefurnace,andthelargestgradient
occursatthereturnlegs,whichagreesqualitativelywithempirical
knowledge [23]. As there is no measured data of hydrodynam-
ics over this commercial boiler, for a rather rough comparison,
thepressuredistributiondatafromthefurnaceofanotherboiler
[11,24], which is similar in size to this one, are plotted in Fig. 4
againstthesimulationresults.Thegeneraltrendsoftheirvariations
werecomparableiftheirreferencepressuresnearthecycloneout-
lets,i.e.,thepressureatthehighestmeasurementposition,were
madethesame.
3.2. Distributionofsolidsvolumefraction
Fig.5showsasnapshotofthesimulatedsolidsvolumefraction
distributionwithseveralslicesinvertical(Fig.5(a))andhorizon-
tal(Fig.5(b))directions,respectively.Fig.5(a)confirmstheresults
Fig.3. Simulatedpressurebalanceintheboilersystem(simulatedpressuredata
weretakenfromthecenterlineacrossthefurnace,theleftcyclone,itsreturnleg
anditsleftreturnpipe).
Fig.4. Comparisonofpressureprofilesinthefurnacebetweensimulationand
experiment(Experimentaldatawereobtainedfromthereference[11]foranother
boiler,whilethesimulation-adjustedmeansthatthepressurebaselinewasadjusted
Fig.2. Surfacemeshofthe3DCFBboiler. tothesamelevelwiththeexperimental.)

N.Zhangetal./ChemicalEngineeringJournal162 (2010) 821–828 825
Fig.5. Simulatedsolidsvolumefractiondistributionswith(a)verticalslicesand(b)horizontalslices.
Fig.6. Profilesofsolidsvolumefractionatdifferentheightswith(a)y-averagedvaluesalongwidth(x-)directionand(b)x-averagedvaluesalongdepth(y-)direction.
Fig.7. Simulatedsolidsverticalvelocitydistributionwith(a)verticalslicesand(b)horizontalslices.

826 N.Zhangetal./ChemicalEngineeringJournal162 (2010) 821–828
Fig.8. Profilesofsolidsverticalvelocityatdifferentheightswith(a)y-averagedvaluesalongwidth(x-)directionand(b)x-averagedvaluesalongdepth(y-)direction.
averagedvaluesalongdepth(y-)direction(Fig.6(b)),respectively.
The curves in Fig. 6(a) are typical to the so-called core–annulus
structure,showingcomparativelydensesolidsconcentrationnear
thewallthaninthecenter.Fig.6(b)showsdifferentprofilesalong
thedepthdirection,whichareflatterthanthosealongthewidth
direction.Thisimpliesthata2D,x–zplanesimulationmayactas
areasonablesimplificationtothereal3Dcase.However,wecan
stillseethatthis2Dreductionwillbeviolatedgreatlyatthedense
bottomwithsignificantfluctuationofsolidsconcentrationatthe
height around 5m, which may be induced by the non-uniform
solidsrecyclinginlets.
3.3. Distributionofsolidsverticalvelocity
Fig.7showsthesimulateddistributionofsolidsverticalvelocity
withseveralslicesinvertical(Fig.7(a))andhorizontal(Fig.7(b))
directions,respectively.Fig.7(a)showsthatvorticescanbeformed
inthefurnaceandthesolidsvelocitycanbesignificantlyaffectedby
Fig.9. Comparisonofsimulatedsolidfluxesatthecycloneinlets.Thefluxvalues theinjectedairnearthesecondaryairinlet.Fig.7(b)showsthatthe
werearea-averagedfluxesattheinletsofthecyclones,i.e.,thebackwallofthe solidsverticalvelocityismainlypositiveinthecenterandnegative
furnace.
nearthewall.Thecomparisonamongtheseslicesseemsconfirms
Fig.10. Instantaneoussolidsvolumefractiondistributionintheboileratsimulationtimeof(a)no.28.9sand(b)no.38.7s.Theredcirclesindicatehighsolidsvolumefraction
onthetopwallofthefurnace.(Forinterpretationofthereferencestocolorinthisfigurelegend,thereaderisreferredtothewebversionofthearticle.)

N.Zhangetal./ChemicalEngineeringJournal162 (2010) 821–828 827
thatthenegativevelocitynearthewallowingtoclusteringofpar- AppendixA. Governingequations
ticlesdropswiththeincreaseofheight.
TheresultsdepictedinFig.8aremorecomplexthanthosein Continuityequations:
Fig. 6. The core–annulus structure can be confirmed in Fig. 8(a),
showing falling clusters near the front- or back walls while ris- ∂ (˛gg) (˛ggvg) 0,
ingparticlesinthecenter.However,thesolidsvelocityprofilesare ∂t +∇· =
morefluctuatingalongthedepth-wisedirectioninthesensethat
thex-averagedsolidsvelocitymaybepositiveornegativenearthe ∂
sidewalls;thetwomaximumrisingvelocitiesseemstobeaffected ∂t
(˛ss)
+∇·
(˛ssvs)
=
0.
bytwocyclonesgreatlyandtheirpositionsdeviatemuchfromthe
Momentumequations:
center(Fig.8(b)).AsasummarytotheresultsofFigs.6(b)and8(b),
wecanseethatthedepth-wiseflowdistributionishardlyuniform ∂
andthena2Dsimulationcannotbeviewedasareliablesimpli- (˛ggvg) (˛ggvgvg) ˛g p g ˛ggg
∂t +∇· =− ∇ +∇· +
ficationtothereal3Dcase.However,itshouldbenotedthatthe
fluctuatingvelocityinFig.8mightbearesultoftheaveragingtime +
ˇ(vs
−
vg),
due to limited computing capacity. Real process may take min-
utesandevenhourstoreachthesteady-stateoperation.Moretests
shouldbeperformedconcerningthisphenomenon. ∂
(˛ssvs) (˛ssvsvs) ˛s p ps s ˛ssg
∂t +∇· =− ∇ −∇ +∇· +
ˇ(vg vs),
+ −
3.4. Solidfluxesatcycloneinlets
Granularenergyequation:
As addressed by Grace et al. [25], “when two-phase suspen-
sions are conveyed through identical parallel flow paths, the
3 ∂
flow distribution can be significantly non-uniform in practice”.
2(cid:2)∂t
(s˛ss)
+∇·
(s˛svss)
(cid:3)=
(
−
psI
+
s):
∇
vs
This phenomenon has been verified in experiments [26–29].
Measurementofsolidfluxisdifficultforexperimentsespeciallyon
+∇·
(k
s∇
s)
− s−
3ˇs.
acommercialCFBboiler,butitiseasyforsimulations.Fig.9shows
themonitoredsolidfluxesinthissimulationatthesetwocyclones.
Inaverage,thesolidfluxesatthesetwocyclonesshowminordif- Constitutiveequations:
ference,whichare5.74kg/(m2s)and6.05kg/(m2s),respectively. Stresstensors:
Considering the non-uniform solids distribution in the furnace,
2
wecansaythatthetwocyclonesoperateidenticallyasdesigned. (cid:2) g = ˛gg( ∇ vg +∇ vT g ) + ˛g g −3 g ∇· vgI,
Fromtheinstantaneouspointofview,however,thefluxesshowa (cid:4) (cid:5)
seesawphenomenon,thatis,themaximumfluxalternatesinthese
2
t t w he o o c t y h c e l r on o e n s e ; i w s h ri e g n ht on n e ea c r y i c t l s on lo e ca re l a m ch in e i s m i u ts m lo . c S a u l c m h a p x h i e m n u o m me fl n u o x n , (cid:2) s = ˛ss( ∇ vs +∇ vT s ) + ˛s (cid:4) s −3 s (cid:5) ∇· vsI.
canalsobevalidated,asshowninFig.10,fromthesnapshotsof
Solidphasepressure:
alternatedenseaccumulationofsolidsnearthecycloneinletsat
the top wall. This is the first time that such non-uniform phe- ps
=
˛sss
+
2s(1
+
ess)˛s 2g0s.
nomenoniscapturedwithaCFDsimulation,whichisconsistent
with Grace’s experiment [26]. The current analysis is still at its Solidphaseshearviscosity:
preliminarylevel,callingformoresystematicworkinthefuture.
s
=

s,kin+

s,col+

s,fr
,
4. Conclusions 
s,col=
4
5
˛ssdsg0 (1
+
ess)
(cid:6)


s
(cid:7)
1/2 ,
A3D,full-loop,time-dependentCFDsimulationofa150MWe
CFBboilerwasperformed.Itisanextensiontoourexperienceon
virtualexperimentationtoinvestigatethehydrodynamicswithin 10sds s 4 2
a
cu
n
r
i
r
n
e
d
n
u
t
s
m
tr
o
ia
d
l
e
r
l
e
,
a
w
c
i
t
t
o
h
r.
e
S
m
im
ph
u
a
la
s
t
is
io
o
n
n
r
t
e
h
s
e
ul
E
t
M
ss
M
ho
S
w
-co
th
rr
e
ec
c
t
a
e
p
d
ab
d
i
r
l
a
it
g
y
c
o
o
f
e
t
f
h
fi
e
-
 s,kin= 96˛s(1
+
(cid:8)ess)g0(cid:9) 1 +5 g0˛s(1 + ess)
(cid:10)
,
cient,inpredictingthetwo-phaseflowbehavior.Moresimulations
canbeexpectedtoenableusbetterunderstandingCFBboilers. pssin
 .
s,fr=
2 I2D
(cid:8)
Gasandsolidphasebulkviscosity:
Acknowledgements
1/2
ver
T
si
h
ty
ea
fo
u
r
th
p
o
r
r
o
s
v
a
id
re
in
g
g
ra
th
te
e
fu
b
l
lu
to
ep
P
r
r
i
o
n
f
t
e
o
ss
f
o
t
r
h
J
e
u
b
n
o
fu
ile
L
r
u
,
o
a
f
n
T
d
s
t
in
o
g
P
h
r
u
o
a
fe
U
ss
n
o
i-
r
g
=
0, s
=
3
4
˛ssdsg0 (1
+
ess)
(cid:6)


s
(cid:7)
.
JohnR.GraceofUniversityofBritishColumbiaforemaildiscus-
Radialdistributionfunction:
sion on the phenomena of parallel cyclones and their efficiency.
T u
N
h n
o
e d
.K
e fi r
G
n N a
C
n o
X
c s
2
i .
-
a 2
Y
l 0 s
W
0 u 7 p
-2
A p
2
A o
2
r 0 t 5
a
s
r
0 f
e
r 3 o
a
0 m
l
2
s
-
o
N 0
g
3 S
r
F a
e
C n
a
u
t
d
l
n
y
2 d 0
a
e
c
0 r
k
8 G
n
B r
o
A a
w
F n 3
l
t
e
3 N
d
B o
g
0 .
e
1 2
d
, 0
.
a 8 n 2 d 10 C 9 A 2 S , u M n O d S e T r g0=(cid:2) 1
− (cid:4) ˛s
˛
,m
s
ax(cid:5)
1/3
(cid:3)
− 1 .

828 N.Zhangetal./ChemicalEngineeringJournal162 (2010) 821–828
Diffusioncoefficientofenergy: CirculatingFluidizedBedTechnologyVII—ProceedingsoftheSeventhInterna-
tionalConferenceonCirculatingFluidizedBeds,CanadianSocietyofChemical
150sds () 6 2 Engineers,Ottawa,2002,pp.467–474.
k (cid:11)s = 384(1
+
(cid:8)ess)g0
(cid:9)
1 +5 ˛sg0 (1 + ess)
(cid:10)
[11]
fl
X
u
.X
id
ia
iz
o
e
,
d
M
b
u
e
lt
d
i-
b
d
o
im
ile
e
r
n
f
s
u
io
r
n
n
a
a
l
ce
m
,
o
P
d
h
e
.D
lin
.D
g
i
a
s
n
s
d
er
e
t
x
at
p
i
e
o
r
n
i
,
m
T
e
s
n
in
ta
g
l
h
r
u
e
a
se
U
a
n
rc
iv
h
e
o
r
n
sit
c
y
ir
,
c
B
u
e
la
ij
t
i
i
n
n
g
g
,
2006.
+
2s˛s 2ds(1
+
ess)g0(cid:11) 

s . [12] c E u .U la . t H in a g rt fl g u e, id L i . z R e a d ts b c e h d o r w is , e R r . , W Pa i r s t c ic h u n o e l w og s y ki 7 ,J ( . 2 W 00 e 9 rt ) h 2 e 8 r 3 ,C –2 FD 96 -s . imulationofacir-
[13] K.G. Hansen, J. Madsen, A computational and experimental study of
gas–particleflowinascaledcirculatingfluidizedbed,in:9thSemesterProject,
Collisionenergydissipation: AalborgUniversitetEsbjerg,Esbjerg,2001.
[14] F. Johnsson, Fluidized bed combustion for clean energy, in: F. Berruti,
s = 12(1 ds − √ e  s 2 s )g0s˛2 s  3 s /2 . X e
h
n
t
.
t
c
p
B e
:
i
/
, o
/s
n T
er
. F
v
l P
i
u
c
u
e
id g
s
s i
.b
z le a
e
y t
p
io
re
( n E
s
,
s
d
.
E s
c
C .
o
) I ,
m
S P
/e
y r
c
m o
i
c
/
p e
fl
o e
u
s d
i
i
d
i u n
i
m
z
g
a
s
t
S
io
o e
n
f rie
x
t s
i
h
i
,
/
e
1
V
3
a 1
1
n 2
.
c t o h uv In er te , r 2 n 0 a 0 ti 7 o , n p a p l . C 4 o 7 n – f 6 er 2 - ,
Interphasemomentumexchangecoefficient: [15] N.Zhang,B.Lu,W.Wang,J.Li,Virtualexperimentationthrough3Dfull-loop
simulationofacirculatingfluidizedbed,Particuology6(2008)529–539.
ˇ = 3 4 C d ˛s˛gg d | v s s − vg |˛−g 2.65H d , [ [ 1 1 6 7 ] ] M J N . . u L Y l i t , a i n - M s g c . , a W K le w . M W au e a k t n h , g o P , d a W , r M t . ic G e l t e e a , – l J l F . u l L u r i g i , d i C c h a T l o w I o n o s d i - n u P g h st a s r s t y r e u P c F r t e l u o s w s re , : B -d e T e i h j p i e n e g n E , d n 1 e e 9 n r 9 t g 4 y d . - r M ag in c i o m ef i fi za c t ie io n n t
inmodelinggas–solidtwo-phaseflow,ChinaParticuol.1(2003)38–41.
where
[18] W.Wang,J.Li,Simulationofgas–solidtwo-phaseflowbyamulti-scaleCFD
C d= ˛
2
g
4
Re [1 + 0.15(˛gRe)0.687], and Re =
g
|
vg
 − g
vs
|
ds
. [19]
a
6 J.
p
2 W
p
(
r
a 2
o
n 0
a
g 0
c
, 7
h
W )
—
2 .
e
G 0
x
8 e
t
– ,
e
J 2
n
.L 3
s
i
i
1 ,
o
E .
n
u
o
le
f
r
t
i
h
an
e
s
E
i
M
m
M
ul
S
at
m
io
o
n
d
o
e
f
l
h
t
e
o
t
t
e
h
r
e
og
s
e
u
n
b
e
-
o
gr
u
i
s
d
g
l
a
e
s
v
–
e
s
l,
o
C
li
h
d
e
fl
m
ow
.E
s
n
i
g
n
.
C
S
F
c
B
i.
risers:EMMS-basedsub-gridscalemodelwitharevisedclusterdescription,
Chem.Eng.Sci.63(2008)1553–1571.
References [20] C.Y.Wen,Y.H.Yu,Mechanicsoffluidization,Chem.Eng.Prog.Symp.Ser.62
(1966)100–111.
[1] Y.Y.Lee,T.Hyppanen,Acoalcombustionmodelforcirculatingfluidizedbed [21] B.Lu,W.Wang,J.Li,Searchingforamesh-independentsub-gridmodelforCFD
boilers,in:A.M.Manaker(Ed.),ProceedingsoftheTenthInternationalConfer- simulationofgas–solidriserflows,Chem.Eng.Sci.64(2009)3437–3447.
enceonFluidizedBedCombustion,vol.2,ASME,NewYork,1989,pp.753–764. [22] P.C.Johnson,R.Jackson,Frictional–collisionalconstitutiverelationsforgran-
[2] K.Myöhänen,T.Hyppänen,M.Loschkin,Convertingmeasurementdatatopro- ularmaterials,withapplicationtoplaneshearing,J.FluidMech.176(1987)
cessknowledgebyusingthree-dimensionalCFBfurnacemodel,in:K.Cen 67–93.
(Ed.), Circulating Fluidized Bed Technology VIII—Proceedings of the Eighth [23] P.Herbert,L.Reh,R.Nicolai,TheETHexperience:experimentaldatabaseand
InternationalConferenceonCirculatingFluidizedBeds,InternationalAcademic resultsfromthepasteightyears,A.I.Ch.E.SymposiumSeriesNo.321,95(1999)
Publishers,WorldPublishingCorp.,Hangzhou,2005,pp.306–312. 61–66.
[3] K.Myöhänen,T.Hyppänen,Modelingofcirculatingfluidizedbedcombustion [24] X.Xiao,W.Wang,H.Yang,J.Zhang,G.Yue,Two-dimensionalcombustionmod-
withasemi-empiricalthree-dimentionalmodel.Availablefrom:http://www. elingofCFBboilerfurnacebasedonanEuler–Eulerapproachandthekinetic
automaatioseura.fi/confprog/downloadfilepublic.php?conference= theoryofgranularflow,in:K.Cen(Ed.),CirculatingFluidizedBedTechnol-
12&filename=12-12040.pdf(lastvisited2010.01.13). ogyVIII—ProceedingsoftheEighthInternationalConferenceonCirculating
[4] e K m .M is y s ö io h n ä s ne in n, c T o . a H l y fi p ri p n ä g ne w n i , th T. o P x ik y k - a fu ra e i l n c e i n rc , u T l . a E t r in ik g ss fl o u n i , d A iz . e H d o b tt e a d ,N b e o a il r e z r e , r C o h C e O m 2 . F H l a u n id g i z z h e o d u B ,2 e 0 d 0 s, 5, In p t p e . r 3 n 9 a 4 ti – o 4 n 0 a 1 l . AcademicPublishers,WorldPublishingCorp.,
Eng.Technol.32(2009)355–363. [25] J.R.Grace,H.Cui,S.S.Elnashaie,Non-uniformdistributionoftwo-phaseflows
[5] T.Knoebig,K.Luecke,J.Werther,Mixingandreactioninthecirculatingflu- throughparallelidenticalpaths,Can.J.Chem.Eng.85(2007)662–668.
idizedbed—athree-dimensionalcombustormodel,Chem.Eng.Sci.54(1999) [26] T.-W.Kim,J.-H.Choi,D.W.Shun,B.Jung,S.-S.Kim,J.-E.Son,S.D.Kim,J.R.
2151–2160. Grace,Wastagerateofwaterwallsinacommercialcirculatingfluidizedbed
[6] K.Luecke,E.U.Hartge,J.Werther,A3Dmodelofcombustioninlarge-scale combustor,Can.J.Chem.Eng.84(2006)680–687.
circulatingfluidizedbedboilers,Int.J.Chem.React.Eng.2(2004)A11. [27] T.-W.Kim,J.-H.Choi,D.W.Shun,S.-S.Kim,S.D.Kim,J.R.Grace,Wearofwater
[7] J.Werther,E.U.Hartge,L.Ratschow,R.Wischnewski,Simulation-supported wallsinacommercialcirculatingfluidizedbedcombustorwithtwogasexits,
measurementsinlargecirculatingfluidizedbedcombustors,Particuology7 PowderTechnol.178(2007)143–150.
(2009)324–331. [28] M.S.Masnadi,J.R.Grace,S.Elyasi,X.Bi,Distributionofmulti-phasegas–solid
[8] D.Pallares,F.Johnsson,Macroscopicmodellingoffluiddynamicsinlarge-scale flowacrossidenticalparallelcyclones:modelingandexperimentalstudy,Sep.
circulatingfluidizedbeds,Prog.EnergyCombust.Sci.32(2006)539–569. Purif.Technol.(2010),doi:10.1016/j.seppur.2009.12.027.
[9] D.Pallares,F.Johnsson,Modelingoffuelmixinginfluidizedbedcombustors, [29] G.Yue,H.Yang,L.Nie,Y.Wang,H.Zhang,Hydrodynamicsof300MWeand
Chem.Eng.Sci.63(2008)5663–5671. 600MWe CFB boilers with asymmetric cyclone layout, in: J. Werther, W.
[10] I.Flour,M.Boucker,Numericalsimulationofthegas–solidflowinthefurnace Nowak,K.E.Wirth,E.U.Hartge(Eds.),CirculatingFluidizedBedTechnology
ofaCFBcoldrigwithESTET-ASTRIDcode,in:J.R.Grace,J.Zhu,H.deLasa(Eds.), IX—ProceedingsoftheNinthInternationalConferenceonCirculatingFluidized
Beds,TuTechInnovation,Hamburg,Germany,2008,pp.153–158.
