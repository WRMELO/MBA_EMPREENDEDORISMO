# Advances_in_mathematical_modeling_of_flu

**Fonte**: Advances_in_mathematical_modeling_of_flu.pdf  
**Data de conversão**: 2025-07-30 15:07:43  
**Origem**: base_relevantes

---

RenewableandSustainableEnergyReviews40(2014)688–715
ContentslistsavailableatScienceDirect
Renewable and Sustainable Energy Reviews
journal homepage: www.elsevier.com/locate/rser
Advances in mathematical modeling of fluidized bed gasification
Chanchal Lohaa,n, Sai Gub, Juray De Wildec, Pinakeswar Mahantad, Pradip K. Chatterjeea
aThermalEngineeringGroup,CSIR–CentralMechanicalEngineeringResearchInstitute,Durgapur713209,India
bSchoolofEngineering,CranfieldUniversity,Cranfield,BedfordshireMK430AL,England
cMaterialsandprocessengineering(IMAP),UCL,PlaceSainteBarbe2bteL5.02.02à,1348Louvain-la-Neuve,Belgium
dMechanicalEngineeringDepartment,IndianInstituteofTechnologyGuwahati,Guwahati781039,Assam,India
a r t i c l e i n f o a b s t r a c t
Articlehistory: Gasificationisthethermochemicalconversionofsolidfuelintothegaswhichcontainsmainlyhydrogen,
Received14November2013 carbonmonoxide,carbondioxide,methaneandnitrogen.Ingasification,fluidizedbedtechnologyiswidely
Receivedinrevisedform usedduetoitsvariousadvantageousfeatureswhichincludehighheattransfer,uniformandcontrollable
18July2014 temperature and favorablegas–solid contacting.Modelingand simulationoffluidized bedgasification is
Accepted30July2014 useful for optimizing the gasifier design and operation with minimal temporal and financial cost. The
present work investigates the different modeling approaches applied to the fluidized bed gasification
Keywords: systems.Thesemodelsarebroadlyclassifiedastheequilibriummodelandtheratebasedorkineticmodel.
Gasification Ontheotherhand,dependingonthedescriptionofthehydrodynamicofthebed,fluidizedbedmodelsmay
Fluidizedbed also be classified as the two-phase flow model, the Euler–Euler model and the Euler–Lagrange model.
Euilibriummodel
Two-phaseflowmodel Mathematical formulation of each of the model mentioned above and their merits and demerits are
Euler–Eulermodel discussed.Detailreviewsofdifferentmodelusedbydifferentresearcherswithmajorresultsobtainedby
Euler–Lagrangemodel themarepresentedwhilethespecialfocusisgivenonEuler–EulerandEuler–LagrangeCFDmodels.
&2014ElsevierLtd.Allrightsreserved.
Contents
1. Introductionandobjective ............................................................................................ 689
1.1. Drying ...................................................................................................... 689
1.2. Pyrolysisordevolatilization ..................................................................................... 689
1.3. Combustionoroxidation........................................................................................ 689
1.4. Gasificationorreduction........................................................................................ 689
2. Fluidizedbedgasifiers................................................................................................ 689
2.1. Bubblingfluidizedbedgasifier................................................................................... 690
2.2. Circulatingfluidizedbedgasifier ................................................................................. 690
2.3. Twin-fluidizedbedgasifier...................................................................................... 691
3. Reactionmechanismandkinetics....................................................................................... 691
3.1. Equilibriummodel............................................................................................. 691
3.1.1. Stoichiometricequilibriummodel..........................................................................691
3.1.2. Non-stoichiometricequilibriummodel......................................................................692
3.2. Ratebasemodelorkineticmodel ................................................................................ 693
3.2.1. Pyrolysis..............................................................................................693
3.2.2. Gasificationwithair.....................................................................................693
3.2.3. Gasificationwithsteam..................................................................................694
3.2.4. Gasificationwithcarbondioxide...........................................................................694
3.2.5. Othergasificationreactions...............................................................................694
4. Fluiddynamics...................................................................................................... 694
4.1. Two-phaseflowmodel......................................................................................... 694
4.2. Euler–Eulermodel............................................................................................. 698
nCorrespondingauthor.
E-mailaddress:chanchal.loha@gmail.com(C.Loha).
http://dx.doi.org/10.1016/j.rser.2014.07.199
1364-0321/&2014ElsevierLtd.Allrightsreserved.

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 689
4.3. Euler–Lagrangemodel.......................................................................................... 702
5. Numericalsolution .................................................................................................. 706
6. Conclusion......................................................................................................... 710
Acknowledgment ....................................................................................................... 713
References............................................................................................................. 713
1. Introductionandobjective
These reduction reactions are mostly endothermic. The final pro-
ducts from these reactions are mainly gas mixtures including
The rapid growth in industrialization all over the world with
hydrogen,carbonmonoxide,carbondioxideandmethane.
simultaneous increase in population, air pollution has reached a
Mostofthetimedrying,pyrolysisordevolatilization,combustion
very critical level, which threatens the public health, deteriorates
oroxidationandgasificationorreductionstepsarenotseparatedbut
theenvironmentanddamagespropertyandlandscape.Analarming
they are overlapped in gasification process. For example, in case of
deterioration of the quality of the life nullified the advantages
large particle, these steps can take place simultaneously. When the
gainedbyariseinlivingstandardsduetoindustrialdevelopment.
largeparticleisheatedup,theoutside portionisdried anddevola-
The problem became so serious thatover the lastfew decades all
tizationalsostarts.Inthecore,the particle isstillcooler.Whenthe
industrialized and some developing countries introduced increas-
centerofalargeparticleisheatedup,too,anddryinganddevolatiza-
inglystringentlegislation,restrictingpermissiblelevelsofpollutant
tionalreadystartedontheoutsideoftheparticle,theresidualcharis
emission from major combustion systems such as electricity gen-
likelytobealreadygasified.
eratingpowerstations,furnacesandindustrialplantsaswellasby
Inordertoinvestigatethegasificationprocess, differenttypes
automobiles and aircrafts. Therefore, the conservation of limited
ofgasifiersaredevelopedlikeupdraftgasifier,downdraftgasifier,
supplyoffossilfuel,climatechangeandtheincreasingconcernover
cross draft gasifier, bubbling fluidized bed gasifier, circulating
globalwarmingpromptedasearchforanewandcleantechnology.
fluidized bed gasifier, twin fluidized bed gasifier, entrained flow
Amongst the different technologies, one of the most promising
gasifier etc. Detailed descriptions of the gasification technologies
futureenergytechnologiesisthefluidizedbedgasification.
areavailableintheliterature[1,2].Amongstthedifferenttypesof
Gasificationisthethermochemicalconversionofsolidfuelinto
gasification technologies, the fluidized bed technology has a
the fuel gas which contains mainly hydrogen, carbon monoxide,
number of advantages which include but not limited tothe high
carbon dioxide, methane andnitrogen. The product gas fromthe
heat transfer, uniform and controllable temperature, favorable
reactoralsocontainssomecontaminantslikecharparticle,ashand
gas–solidcontacting,higherefficiencyandfuelflexibility.
somehigherhydrocarbonsortar.Alimitedsupplyofoxygen,air,
In order to analyze the process of fluidized bed gasification,
steam or a combination of these serves as gasifying agent. The
several modeling approaches have been deployed and they are
gasificationconsistsoffourdifferentstepse.g.drying,pyrolysisor
broadlyclassifiedintotwogroups;equilibriummodelingandrate
devolatilization, combustion or oxidation and gasification or
baseorkineticmodeling.Equilibriummodelingisindependentof
reduction.Thesefourstepsaredescribedbelow.
thetypeofgasifierbecauseitdoesnotconsiderthehydrodynamic
ofthebed.Dependingupontheprocessofcalculatingtheproduct
1.1. Drying gas composition, the equilibrium model may be classified as the
stoichiometric equilibrium model or non-stoichiometric equili-
Dryingoccursatabout100–2001Cwhenthemoisturefromthe
brium model. Whereas, the kinetic model generally consider the
solidfuelisdrivenoutandconvertedintovapor.Thesolidfuelin
hydrodynamics of the bed coupling with the reaction kinetics.
thisstageisnotdecomposedbecausethetemperatureisnothigh Based on the hydrodynamic modeling, the fluidized bed models
enoughtocauseanychemicalreaction. canalsobeclassifiedastwo-phaseflowmodel,Euler–Eulermodel
and Euler–Lagrange model. In hydrodynamic modeling, the most
1.2. Pyrolysisordevolatilization establishedmodelisthetwo-phaseflowmodel.Veryrecently,the
computational fluid dynamic (CFD) modeling of fluidized bed
Thisisathermaldecompositionprocesswherethedriedsolid gasification based on Euler–Euler approach and Euler–Lagrange
fuel is decomposed into low to high molecular weight volatiles approach are attempted by researchers due to the increasing
including tar and solid charcoal in the absence of oxygen. The computational power of the modern computers. But, application
pyrolysis or devolatilization reactions are endothermic and thus ofCFDmodeltostudythefluidizedbedgasificationprocessisin
theheatneededforthesereactionsissuppliedfromthecombus- the developing stage and more studies are needed [3,4]. In the
tionoroxidationreactions. presentwork,adetailedreviewofdifferentfluidizedbedgasifica-
tionmodelspublishedintheliteratureispresented.Mathematical
1.3. Combustionoroxidation equations governing fluid and solid flow, heat and mass transfer
andchemicalreactionsforeachmodelarepresented.Advantages
The products of the pyrolysis or devolatilization process are and disadvantages of different modeling approaches and major
partiallyoxidized byoxygensupplied throughair, and then from results obtained are discussed. The special attention has been
carbon monoxide, carbon dioxide and water vapor or steam. given to the recently published Euler–Euler and Euler–Lagrange
As the combustion reactions are exothermic and other reactions CFDmodels.
in gasification are endothermic, the overall heat required for
endothermicreactionsissuppliedbythiscombustionoroxidation
process. 2. Fluidizedbedgasifiers
1.4. Gasificationorreduction There are different types of fluidized bed gasifiers reported in
theliterature.Amongstthem,adetaileddescriptionofthebubbling
Ingasificationstepseveralreductionreactionsoccurinabsence fluidizedbedgasifier,thecirculatingfluidizedbedgasifierandthe
ofoxygenbecauseoxygenisconsumedinthecombustionreactions. twin fluidized bed gasifier are presented here. Fig. 1 shows the

690 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
Product
Product gas Gas
Biomass
Biomass
Air
Air
Fig.1. Schematicdiagramof(A)bubblingfluidizedbedgasifierand(B)circulatingfluidizedbedgasifier.
schematic diagramof bubbling, circulatingand twinfluidized bed Flue
gasifiers.
Gas
2.1. Bubblingfluidizedbedgasifier
In a typical gasifier, when the gas velocity is increased, Product
a situation is reached when the particles are just suspended in
Gas
the upward flowing gas. At this situation the frictional force
betweenaparticleandfluidcounterbalancetheweightofparticle,
theverticalcomponentofthecompressiveforcebetweenadjacent
Gasifier Combustor
particlesdisappearsandthepressuredropthroughanysectionof
the bed equals the weight of fluid and particles in that section.
Atthisinstance,thebedisconsideredtobeatminimumfluidiza- Biomass
tioncondition.Withanincreaseinvelocitybeyondtheminimum
fluidizationvelocity,largeinstabilitieswithbubblingandchannel-
ingofthegasareobserved.Athigherflowratesagitationbecomes
moreviolentandthemovementofsolidsbecomesmorevigorous.
However, the bed does not expand much beyond its volume at
minimumfluidization.Suchabediscalledbubblingfluidizedbed
(Fig.1A).Inabubblingfluidizedbed,gasmovesthroughthebedin
voidandinbubbleswithhighervelocity.Someoftheparticlesare
entrainedintothefreeboardalongwiththesefastmovingbubbles Gasifying
andsomefineparticlesaretransportedwiththeproductgasand
agent
leavethereactoratthetop.Butmostoftheentrainedparticlesfall Air
back and can be continuously removed from the fluidized bed
withtheremainingashatthebottom.Thebubblingfluidizedbed Fig.2. Schematicdiagramofatwinfluidizedbedgasifier.
gasifiers have a number of advantages over non-fluidized bed
gasifiers which include fuel flexibility, uniform temperature, circulating fluidized bed (Fig. 1B). The advantage of circulating
higherefficiency,lowercapitalandmaintenancecostetc. fluidizedbedsinmainlyduetothelongeroverallresidencetime.
Thesolidscirculateintheouterloop,goingupintheriser,leaving
2.2. Circulatingfluidizedbedgasifier at the top, going down in the return leg and entering the riser
again at the bottom. But there is also internal circulation of the
When the gas velocity is increased further, beyond the bub- solids, which fall back from the higher region of the riser and
blingfluidizedbedregime,thesolidswillbedistributedacrossthe move downwards at the riser wall. Circulating fluidized bed
whole riser height and entrained by the gas at the top of the gasifiersarenormallyusedforlargeapplications.Ithasenhanced
gasifier.Particles are separatedfromthegasinacycloneandare flexibilityoverbubblingfluidizedbedgasifierforfiringmulti-fuels
returned to the fluid bed near the bottom. Then it becomes a withhighmoisturecontentandsignificantlyhigherefficiency.

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 691
2.3. Twin-fluidizedbedgasifier Itrequiresaclearlydefinedreactionmechanismthatincorporates
allchemicalreactionsandspeciesinvolved.Itusestheelemental
Anotherformoffluidizedbedgasifierwhichisalsoreportedin balance and the equilibrium constants of selected reactions.
theliteratureisthetwinfluidizedbedgasifierasshowninFig.2. AstoichiometricequilibriummodelmayalsouseGibbsfreeenergy
In one fluidized bed (generally bubbling) the gasifying agent data to determine the equilibrium constants of a propose set of
(mostly steam) is brought into contact with the fuel fed to this reactions.
fluidizedbed.Thereiscontinuousdischargeofbedmaterialwith A brief description of stoichiometric equilibrium model based
unreactedcharparticlesfromthisfirstfluidizedbed,whichisthen on the work of Loha et al. [6,7] is given below. In stoichiometric
fedtoasecondfluidizedbed(generallycirculating)operatedwith equilibrium model, the gasification process is represented by a
air and used as a combustor to burn the remaining char and to globalgasificationreactionasfollows:
heat the fluid bed particles. Then the hot bed material from the
second fluidized bed is circulated to the first fluidized bed to
CHxOyþ wH
2
O
þ
mH
2
O
¼
γ
H2
H
2þ
γ
CO
CO
þ
γ
CO2
CO
2þ
γ
H2O
H
2
O
þ
γ
CH4
CH
4
supplytheheatfortheendothermicsteamgasificationreactions.
ð
1
Þ
This technology is especially interesting for biomass gasification where CH O represents the solid fuel which contains carbon,
x y
due to the higher volatiles content in the biomass compared to hydrogenandoxygen.Otherelementsareneglected.Here,xandy
coal.Hereonlythevolatilesareusedforsynthesisofgasproduc- representnumbersofatomsofhydrogenandoxygenpernumber
tion. The fixed carbon content is burned to supply the heat. ofatom ofcarboninthe solidfuel andcanbeobtainedfromthe
Therefore, the slow gasification reactions of fixed carbon with ultimate analysis of the solid fuel, w is the mole of moisture per
steamorcarbondioxideareavoided.Anotheradvantageisthatif moleofdryashfreesolidfuelandmisthemoleofsteamadded
steam is used in the first fluidized bed, the producer gas is not per mole of dry ash free biomass. On the left hand side all are
dilutedbynitrogenfromtheair. inputs.Ontherighthandside,γ ; γ ; γ ; γ and γ arethe
H2 CO CO2 H2O CH4
numbersofmoleofgasspeciesontheproductgasandwhichare
obtained by solving material balance and equilibrium constant
3. Reactionmechanismandkinetics equationsofselectedreactions.Thematerialbalanceequationsof
carbon,hydrogenandoxygenaregivenbelow.
Mathematical modeling of fluidized bed systems can broadly Carbonbalance
beclassifiedintotwogroups;thermodynamicequilibriummodel
1 γ γ γ 2
andratebaseorkineticmodelasdescribedindetailsbelow. ¼ COþ CO2þ CH4 ð Þ
Hydrogenbalance
3.1. Equilibriummodel
x 2w 2m 2γ 2γ 4γ 3
þ þ ¼ H2þ H2Oþ CH4 ð Þ
The parametric study and the thermodynamic analysis of the
gasification process by using equilibrium model is a popular
Oxygenbalance
method because it provides a useful design aid in evaluating the
possiblelimitingbehaviorofacomplexreactingsystemandalsoit y þ w þ m ¼ γ COþ 2γ CO2þ γ H2O ð 4 Þ
is computationally inexpensive. Though, it is independent of Now, it is required to select the major chemical reactions for
gasifierdesign, still it canprovide a guideline for process design, calculating the product gas composition. For the present calcula-
evaluation and improvement. It can also be used to study the tionfollowingreactionsareselected.
influence of most important process parameters. For this reason
Water gasshiftreaction CO H O CO H 5
manyauthorsusedthethermodynamicequilibriummodetostudy (cid:3) þ 2 ¼ 2þ 2 ð Þ
thefluidizedbedgasificationprocess.
Methanereaction: C 2H CH 6
Equilibrium models are generally developed based on follow- þ 2¼ 4 ð Þ
ingassumptions: All gases are assumed to be ideal and all reactions form at
atmosphericpressure.Therefore,theequilibriumconstantsofthe
Theprocessoccursatsteadystate. above two reactions, which are functions of temperature, are
(cid:1)
Thegasifierisisothermalandatequilibriumcondition. givenbelow.
(cid:1)
Reactionratesarefastenoughandresidencetimeissufficient Theequilibriumconstantofwater–gasshiftreactionis
(cid:1)
toreachequilibriumcondition. P P x x
(cid:1) G
Ch
a
a
se
r
s
co
ex
n
c
ta
e
i
p
n
t
s
H
o
2
n
,
l
C
y
O
s
,
o
C
li
O
d
2
c
a
a
n
rb
d
o
C
n
H
.
4 ,N 2 andH 2 Oarenegligible. K 1¼P C C O O P 2 H H 2O 2 ¼x C C O O x 2 H H 2O 2 ð 7 Þ
(cid:1)
Ashresidueisnegligible. wherex i isthemolefractionofthegasspeciesiinthegasmixture,
(cid:1)
(cid:1)
Theproductgasisatthegasifiertemperature. x i¼ γ i =γ total andhere
Allthegasesobeytheidealgaslaw. γ γ γ γ γ γ :
(cid:1) total¼ H2þ COþ CO2þ H2Oþ CH4
Potentialandkineticenergiesarenegligible.
(cid:1) Theequilibriumconstantformethaneformationreactionis
There are two general approaches for equilibrium modeling viz. K P CH4 x CH4 8
stoichiometricequilibriummodelandnon-stoichiometricequilibrium 2¼ ð P H2Þ 2¼ ð x H2Þ 2 ð Þ
model. However, both approaches are conceptuallysimilar[5], they
Equilibrium constant K is a function of temperature and can
differs.Thedetaileddescriptionofstoichiometricequilibriummodel
directly be obtained from JANAF thermochemical tables [8] or
andnon-stoichiometricequilibriummodelispresentedbelow.
canbecalculatedfromtheGibbsfunctionasgivenbelow.
ΔGo
3.1.1. Stoichiometricequilibriummodel lnK T 9
¼(cid:3) RT ð Þ
The stoichiometric equilibrium model is based on selecting
thosespecieswhicharepresentinthelargestamounts,i.e.those ΔGo ∑γ Δgo 10
specieshavingthelowestvalueofGibbsfreeenergyofformation. T¼ i i f;T;i ð Þ

692 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
where R is the universal gas constant, ΔGo is the standard Gibbs initialelementalabundancevectoranditscurrentiterationvalue
T
function of reaction and Δgo f;T;i represents the standard Gibbs ð b k(cid:3) bðk m Þ Þ ,isaddedtotherighthandsideofEq.(15)toeliminate
functionofformationatgiventemperatureT(K)ofthegasspecies erroraccumulationduringtheiterationprocess[14].
iwhichcanbeexpressedbytheempiricalequationgivenbelow: Finally,thenewnumbersofmolesvector,nm 1,isdeterminedby
ð þ Þ
Δgo f;T¼ h o f(cid:3) aTln ð T Þ(cid:3) bT2 (cid:3)2 c T3 (cid:3)3 d T4 þ2 e Tþ f þ gT ð 11 Þ nð m þ 1 Þ ¼ nð m Þ þ ωð m Þδnð m Þ ð 18 Þ
whereωm isthestepsizeparameter.
ð Þ
Finally,themolarfractionsofallspeciesaredeterminedby
The values of coefficients a–g and the enthalpy of formation
(h o f )ofdifferentgasesareavailableintheliterature[9]. x i¼n n t i ð 19 Þ
3.1.2. Non-stoichiometricequilibriummodel Equilibriummodelsareextensivelyusedbymanyauthors[15–23]
The non-stoichiometric equilibrium model is based on the duetoitsadvantageousfeatureofsimplicityanditgivesquickidea
minimization of Gibbs freeenergyof the systemwithout specifi- of limits of operation compared to the rate base model. It can
cation of the possible reactions taking place. Here, only the provide the final gas composition variationwith operating condi-
elementalcompositionofthefuelisneededtospecifywhichcan tion, gas yield, calorific value of gas, carbon conversion etc. The
beobtainedfromtheultimateanalysisofthefuel.Thismethodis predictionusingequilibriummodelmatcheswellwiththeexperi-
particularly suitable for problems with unclear reaction mechan- mentwhentheequilibriumconditionisprevailedi.e.whentherate
isms.Anon-stoichiometricequilibriummodelingapproachbased ofreactionisveryfastcomparedtotheresidencetimeofreactants
ontheliterature[10,11]ispresentedbelow.Themodelisbasedon in the gasifier. The equilibrium model cannot predict the spatial
theRAND[12,13]algorithm.Here,thechangeinmoleofaspecies variationoftheproductinsidethegasifieraswellasthetemporal
inthemthiterationcanbeexpressedexplicitlyasafunctionofits variation. It is also important to note that the predicted methane
currentchemicalpotential,thephasedistributionofthespeciesat concentrationfromequilibriummodelisalwayssubstantiallylower
a given system temperature and pressure and the Lagrange than the experimentally observed data for gasification process.
multiplierasgivenbelow: Thehighamountofmethaneintheexperimentalgascomposition
δnði m Þ ¼ nði m Þ k ∑ ¼ K 1 a ik ψ kþ u α(cid:3) μ R ði m T Þ ! formulti (cid:3) speciesphase i l g s i a m s a it c n e o o d m n c - p h e o a q s r u it g i i l a o ib s n r ifi i i u c s m a l t a i r s o g p n e e i l c y s ie a a s c t h t r r i e i e b s v u u e l t d t e in d in g to t f h ro p e m y g r a o p s l i y y fi s r e o is r l . y w S s o i h s , i t c r h e h a e t c m h ti e o e n a e s s q u u a r i n e li d d -
¼ u α nði m Þ forsingle (cid:3) speciesphase brium model cannot account for. The equilibrium model cannot
i 1;2;…;N; k 1;2;…;K; α 1;2;…;π 12 predict highly accurate result for fluidized bed gasifier due to its
ð ¼ ¼ ¼ Þ ð Þ inherent assumptions. The residence time, feed configuration,
Here,Ndenotesthetotalnumberofspecies,nði m Þdenotesthemole internal mixing and gas–solid contacting pattern in fluidized bed
of species i in the mth iteration, a ik is the coefficient in species- gasifieraccountforlargedeviation.
element matrix, μði m Þ is the chemical potential of species i in the Thus, in order to predict more accurately the behavior of
mthiteration,ψ k isafunctionrelatedtoLagrangemultiplierλ k and fluidized bed gasifier, different modifications of the existing
u
α
isthephasesplitofδnði m Þ.
equilibrium models have been done as discussed below. Li et al.
Here,ψ k isgivenby [10,11] modified their non-stoichiometric equilibrium model by
ψ λ k 13 introducing the experimental carbon conversion from fluidized
k¼RT ð Þ bed gasification and got better agreement to the experimental
andu isgivenby data.Forexample,theycomparedthehigherheatingvalue(HHV)
α
oftheproductgasasafunctionofairratiofromexperiment,pure
u α¼ i ∑ N 1 δnðiα m Þ=nðt m Þ ¼ δn tð m αÞ=nðt m Þ ð 14 Þ i e n qu F i i l g ib . r 3 iu . m It w m a o s de o l bs a e n r d ved mo th d a ifi t e t d he eq m u o il d ib ifi ri e u d m eq m u o il d ib e r l iu a m s s m ho o w de n l
¼
wheresubscripttmeanstotalandαreferstothephasetowhicha
speciesbelongs.
Therefore,asetof K π simultaneousalgebraicequationsthat
ð þ Þ
are to be solved iteratively by the RAND algorithm includes K
linearequationsregardingelementabundance
∑ K ∑ N a ik a ij nði m Þψ kþ ∑ π bðjα m Þu α¼ ∑ N a ij nðk m Þ μ R ði m T Þ þ b k(cid:3) bðk m Þ 15
k j ¼ 1i 1 ¼ ;2 1 ;…;K α ¼ 1 i ¼ 1 ð Þ
ð ¼ Þ
andπ supplementaryequationsfordifferentphases
∑ K bðk m αÞψ k(cid:3) n zα u α¼ ∑ N nðiα m Þ μ R ðiα m T Þ 16
k α ¼ 1 1;2;…;π i ¼ 1 ð Þ
ð ¼ Þ
The initial elemental abundance vector b is calculated from the
feedstockandthekthelementofthebvectoratthemthiterationis
N
bðk m Þ ¼ ∑ a ik nði m Þ ð 17 Þ
i 1
¼
Mass balance constraints are imposed at every iterations
duringsolutionofaboveequations,whilethealgorithmiteratively Fig.3. EffectofairratioondrygasHHVforas-receivedhighvaluecoalgasifiedat
minimizes the Gibbs free energy. The difference between the 155kPaand1020–1150K.Pointsareexperimentalvalue[9].

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 693
Table1
Gascompositionbyusingpureequilibriummodelandmodifiedequilibriummodelandexperiment[5].
Tempe(1C) S/B Experiment Pureequilibriummodel RMSerror Modifiedequilibriummodel RMSerror
H2 CO CO2 CH4 H2 CO CO2 CH4 H2 CO CO2 CH4
690 1.32 50.50 14.30 26.60 8.60 48.76 12.99 31.21 7.03 2.667429 48.4 16.26 28.88 6.46 2.123064
730 1.32 52.20 16.40 23.50 7.90 50.71 15.48 28.74 5.06 3.10603 50.14 18.94 26.33 4.6 2.720023
750 1.00 49.50 23.70 21.20 5.60 50.37 20.59 25.01 4.02 2.619232 49.64 24.22 22.52 3.62 1.219918
750 1.32 52.30 17.75 22.25 7.40 51.43 16.64 27.65 4.28 3.197006 50.76 20.15 25.22 3.87 2.711706
750 1.70 52.90 16.40 22.90 7.80 52.26 13.50 29.74 4.50 4.077229 51.67 16.78 27.47 4.08 3.015817
770 1.32 54.40 18.50 19.40 7.70 52.00 17.72 26.66 3.62 4.350931 51.24 21.28 24.23 3.25 3.900173
AverageRMS 3.33631 AverageRMS 2.615117
predicted the experimental values much better than the pure model,two-equationmodeloracombinationofreactions.Thesingle
equilibrium model. Loha et al. [6] studied the fluidized bed equationmodelisthesimplestoneanditisrepresentedas[26]
biomassgasificationbyusingastoichiometricequilibriummodel.
The pure equilibrium model was modified by multiplying equili-
Fuel-k
η volatile 1 η char 20
þð (cid:3) Þ ð Þ
brium constants with pre factors. Results from the pure equili-
E
briummodel,themodifiedequilibriummodelandtheexperiment k Aexp (cid:3) 21
werecomparedasshowninTable1.Itwasobservedthataverage ¼ (cid:2) RT p(cid:3) ð Þ
RMS error reduced from 3.33631 to 2.615117 while using the Intwoequationsmodel,thepyrolysisofanysolidfuelisrepresented
modifiedequilibriummodel.Frydaetal.[24]andSchusteretal.[25] bytwoequationsasgivenbelow[27]:
also evaluated the product gas composition from fluidized bed
gasification by using equilibrium model. They modified the equili-
Fuel-k1η
1 volatile þð 1 (cid:3) η 1Þ char ð 22 Þ
brium model by introducing the un-reacted char carbon as some
percentageofthebiomasscarboninputandgotbetteragreementto
Fuel-k2η
volatile 1 η char 23
2 þð (cid:3) 2Þ ð Þ
theexperimentaldata.
where
Therefore,iftheequilibriummodelismodified,itcanbeuseto
s s t t u u d d y y t t h h e e i fl n u fl i u d e iz n e c d e o b f ed m g o a st si i fi m ca p t o io rt n an p t e p rf a o r r a m m a e n t c e e r , s p o a n rt t i h cu e la o r v l e y ra t l o l k i¼ Aexp (cid:2) R (cid:3) T E p i (cid:3) ð 24 Þ
performance.Equilibriummodelalsoprovidesthethermodynamic Parameters kand η in the above equations are to be obtained
limits of the gasification system. Hence, the equilibrium model fromexperiments.Manypublicationsdealwiththecalculationof
maybeusefulforpreliminarydesignandcomparisonoffluidized
those parameters for various fuels, but there is a great variation
bedgasificationprocessiftheyaremodifiedasmentionedabove.
between the representations, probably because a number of
But,itcannotprovidehighlyaccuratedataforallcasesbecauseit physicalandchemicalfactorsareincorporatedinoneexpression.
does not consider the hydrodynamic behavior of the system as Despitethisfact,thistypeofexpressionhasbeenwidelyusedin
wellasthereactionkinetics.Hence,togetmoreaccuratedatafor reactor models due to its simplicity making it computationally
detail design, the rate base modeling or kinetic modeling with tractable, needing only a small set of input data. In most cases,
hydrodynamic consideration of the fluidized bed system is however,itdoesnotgiveenough informationforcomprehensive
requiredasdiscussedinthefollowingsections. modeling.
Themodelsmentionedabovecanpredicttheamountsofvolatile
3.2. Ratebasemodelorkineticmodel and charreleasedduringpyrolysis,but theyieldsof the maingas
species are not predicted which also varies with the type of fuel.
Ratebasemodelorkineticmodelismorecomprehensiveand Thepyrolysisgascompositionisgenerallymodeledeitherbasedon
realisticcomparedtotheequilibriummodel.Ittakesintoaccount theexperimentaldataavailablefromtheliteratureforaparticular
thehydrodynamics,transportprocessandreactionkinetics.Inrate
fuel[28–30]orbasedonthedevelopedcorrelation[31–33].These
base model, a detailed reaction mechanism with rate of each correlations are also developed for a particular set of operating
reactions are considered depending on the type of fuel used. conditionsandtypeoffuelwhichisnotalwayssimilartothosehas
Modeling the reaction kinetics in gasification process requires tobesimulated.Therefore,morefundamentaldataaredesirableto
the consideration of complex reaction network which consists of increasethepredictivecapabilityofmodelsimulations.
pyrolysis, heterogeneous gas–solid reactions and homogeneous
gasphasereactionsasdiscussedbelow. 3.2.2. Gasificationwithair
Incaseofgasificationwithair,theheterogeneousreactionsof
carbonwithoxygenintheairarehighlyexothermicandtherefore
3.2.1. Pyrolysis provide the heat required for the subsequent gasification reac-
The solid fuel particles undergo pyrolysis upon entering into
tions. The heterogeneous reactions of carbon with oxygen are
thehotfluidizedbedgasifier.Pyrolysisisbasicallythedecomposi-
givenbelow
tion of solid fuel resulting from heat. In gasification, the final
product gas composition is important because it determines the C þ O 2 -CO 2; Δh0 R¼(cid:3) 393:5kJ=mol ð 25 Þ
heatingvalueoftheproductgas.Therefore,thekineticmodelfor
t
d
o
u
t
c
a
e
l
d
de
c
v
h
o
a
l
r
at
a
il
n
iz
d
at
i
i
n
o
d
n
i
,
v
w
id
h
u
i
a
c
l
h
c
d
h
e
a
t
r
er
r
m
ele
in
a
e
s
s
ed
b
,
o
s
t
h
h
o
t
u
h
ld
e e
b
x
e
te
t
n
a
t
ke
o
n
f p
in
ro
to
- C
þ
1
2
O
2
-CO; Δh0
R¼(cid:3)
110:5kJ=mol
ð
26
Þ
consideration. Inadditiontotheheterogeneousgas–solidreactions,therearealso
Kinetic models used for determining the pyrolysis product, manyhomogeneousgasphasereactions.Thesearethecombustion
available in the literature, are either based on a single equation reactions of all the gases produced during the pyrolysis step.

694 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
Thehydrogenandcarbonmonoxidewillbeoxidizedcompletelyto Otherhomogeneoussteamgasificationreactionsarethereactions
carbondioxideandwaterasgivenbelow: of steam with higher hydrocarbons. The main product of these
reactions will be other hydrocarbons, carbon monoxide and
1
H 2þ2 O 2 -H 2 O; Δh0 R¼(cid:3) 241:8kJ=mol ð 27 Þ hydrogen.
CO þ 1 2 O 2 -CO 2; Δh0 R¼(cid:3) 283:0kJ=mol ð 28 Þ 3.2. T 4 h . e G g a a s s ifi ifi ca ca ti t o io n n w r i e th ac c t a io rb n on wi d t i h ox c i a d r e bon dioxide requires higher
Inaddition,thecompletecombustionofhydrocarbonswithoxygen temperature because this reaction proceeds very slowly. The
willproducecarbondioxideandwater.But,inthereducingatmo- heterogeneous gasification reaction of carbon dioxide with char
sphereofgasifierandlackofoxygen,theproducswillbehydrogen carbonisgivenbelow:
andca
1
rbonmonoxide. C
þ
CO
2
-2CO; Δh0
R¼þ
172:5kJ=mol
ð
35
Þ
CH 4þ2 O 2 -CO þ 2H 2; Δh0 R¼(cid:3) 35:7kJ=mol ð 29 Þ The homogeneous gas phase reaction of methane with carbon
dioxideisgivenbelow.
C 2 H 4þ O 2 -2CO þ 2H 2; Δh0 R¼(cid:3) 35:7kJ=mol ð 30 Þ CH 4þ CO 2 22CO þ 2H 2; Δh0 R¼þ 247:3kJ=mol ð 36 Þ
In gasification, the amount of air added to the gasifier is not
sufficient to completely combust the fuel to carbon dioxide and
3.2.5. Othergasificationreactions
water. Therefore, once all oxygen is consumed, further reaction
In addition to the reactions discussed above, there may be
taking place are homogeneous equilibrium reactions or heteroge-
someotherreactionsinthegasificationprocess.Forexample,the
neous reactions between char carbon and produced gases so far.
heterogeneousgasificationreactionofcharcarbonwithhydrogen
Therefore, the gasification with air is basically a combination of
isgivenbelow.Thisreactionissignificantonlyathigherpressure:
steamandcarbondioxidegasification.
C þ 2H 2 -CH 4; Δh0 R¼(cid:3) 74:9kJ=mol ð 37 Þ
3.2.3. Gasificationwithsteam
If steam is used as the gasifying agent or all oxygen in air
gasificationisconsumed,thegasificationreactionswithsteamare 4. Fluiddynamics
the main reactions in the temperature range normally used in
fluidized bed. The products of the reactions of solid carbonwith Hydrodynamicsplaysanimportantroleindefiningtheperfor-
steamarehydrogen,carbonmonoxideandtoasmallerextentalso mance of fluidized bed gasifier. Fluidized bed exhibits verycom-
carbondioxidemaybeproduced. plex hydrodynamics due to the nonlinear interactions between
fluidandparticleandtheirownindividualmovementtendencies.
C þ H 2 O-CO þ H 2; Δh0 R¼þ 131:3kJ=mol ð 31 Þ Dependingonthedescriptionofthehydrodynamics,thefluidized
bed gasification models may be classified as the two-phase flow
C þ 2H 2 O-CO 2þ 2H 2; Δh0 R¼þ 211:4kJ=mol ð 32 Þ model, the Euler–Euler model and the Euler–Lagrange model.
The homogeneous gas phase reaction of steam with methane is Detaileddescriptionsofeachofthesemodelsarepresentedbelow.
givenbelow:
4.1. Two-phaseflowmodel
CH
4þ
H
2
O2CO
þ
3H
2
Δh0
R¼þ
206:2kJ=mol
ð
33
Þ
The very well known water–gas-shift reactionwhich is indepen- Twomostpopularandoldesttwo-phaseflowmodelsareaspro-
dentofthechoiceofthegasifyingagentandoperatingconditionis posedbyDavidsonandHarrison[34]andKuniiandLevenspiel[35].
givenbelow: In two-phase flow model, the fluidized bed is divided into two
phasee.g. the bubblephase and the emulsionphase(Fig.4). The
CO þ H 2 O2CO 2þ H 2; Δh0 R¼(cid:3) 41:2kJ=mol ð 34 Þ bubble phase is assumed to be particle free. The emulsionphase
Dispersion
Convection,u
mf
D Convection, u b
s,ax
And dispersion, D g,ax
Reaction (g- Reaction (g-g) Reaction (g-
(1-α) α Mass transfer, α
c v b mf b
Solids Suspension phase gas Bubble phase
Fig.4. Divisionoffluidizedbedintobubbleandemulsionphasesintwo-phaseflowmodel.

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 695
containsparticlesandremainsinminimumfluidizationcondition. rate of reaction jin bubble phase, r is the reaction rate of
emul;j
Gasflowsinplugflowinboththebubbleandemulsionphase.The reaction j in emulsionphase, m_‴ is the volumetric mass flow
Feed;i
solidsareevenlydistributedandaretransportedbydispersiononly. rate at the feeding section, m‴ is the volumetric mass flow
Return;i
Theheterogeneousgas–solidreactionsoccurintheemulsionphase rateatthereturnlegandM isthemolarmassofspeciesi.
i
only.Homogeneousgasreactionstakeplaceinboththebubbleand Theabovemassbalanceequationsarediscrelizedandnumeri-
the emulsion phase. The model posses separate mass balance cally solved with appropriate initial and boundary conditions.
equation for each phase and mass interaction between phases. In In two-phase flow model, the fluid dynamic parameters are
two-phase flow model, the momentum equation is not explicitly calculatedbasedoncorrelationsandsuppliedasinputparameters.
solved rather the hydrodynamic of the fluidized bed is calculated Several expressions exist to calculate these parameters. A list of
fromcorrelations.Whilemodelingfluidizedbedbyusingtwo-fluid hydrodynamic parameters generally used in two-phase flow
model, the gasifier is axially divided into different zones (bottom modeling is given in Table 2. Therefore, the need to solve the
zone,freeboardandexitzone).Thefreeboardandtheexitzoneare momentum equations is avoided and the model becomes com-
generallymodeledbycomparativelysimplemixturemodel.Thetwo- parativelysimple.Atypicalsolutionprocedurefortwo-phaseflow
phase flow concept is used to model the dense bottom zone in modelingoffluidizedbedgasificationprocessisshowninFig.5.
fluidizedbedsystems.Mathematicalequationsusedforsuchatwo- Several studies are reported on fluidized bed gasification by
phaseflowmodelfollowingtheworkofKruseandWerther[36]and usingthetwo-phaseflowmodelingconceptdiscussedaboveorin
PetersenandWerther[22,37]aregivenbelow. modifiedformbyassumingorestimatingseveralterms.Jiangand
In two-phase flow model, separate mass conservation equa- Morey[33]studiedthefluidizedbedbiomassgasificationbyusing
tions are solved for gas and solid species. Gaseous species are one dimensional steady-state two-phase flow. The model pre-
present both in bubble and emulsion phases and hence separate dicted fuelfeed rate, compositionofproduct gasandfuel energy
massconservation equations are solved for gasspecies inbubble conversion.Modelresultswerecomparedwithexperimentaldate.
andemulsionphases. It was observed that model worked well at higher temperature
The conservation equation for the gaseous component iin the
bubblephaseisgivenby START
∂C ∂u C
α gb;i ð b gb;iÞ K C C α ∑ v r 38
b ∂t þ ∂z ¼(cid:3) beð gb;i(cid:3) ge;iÞþ b i;j b;j ð Þ INPUT
jg g
ð (cid:3) Þ
The conservation equation for the gaseous component i in the
emulsionphaseisgivenby INITIAL ASSIGNMENT
ð 1 (cid:3) α bÞ α mf ∂C ∂ g t e;i þð 1 (cid:3) α bÞ u mf ∂ ð C ∂ g z e;iÞ (cid:3)ð 1 (cid:3) α bÞ α mf D g;ax ∂2 ð ∂ C z g 2 e;iÞ t=t+n∆t
¼ K beð C gb;i(cid:3) C ge;iÞþð 1 (cid:3) α bÞ α mf ∑ v i;j r emul;jþ c v;bz ∑ v i;j r emul;j
j ð g (cid:3) s Þ j ð g (cid:3) g Þ FUEL FEED
39 Calculation of pyrolysis gas and solid
ð Þ distribution
The particles are present in the emulsion phase only. Hence, the
massbalanceequationofsolidcomponentiintheemulsionphase n=n+1
OVERALL GASIFICATION
isgivenby CALCULATION
cvρ s ∂ ∂ x t s;i (cid:3) cvρ s Ds;ax ∂2 ∂ ð z x 2 s;iÞ ¼ m_‴ Feed;iþ m_‴ Return;iþ cvM i ∑ v i;j r emul;j ð 40 Þ MASS BALANCE
j ð g (cid:3) s Þ Balance of inert solid, char and gaseous
components
where α is the void fraction of bubble phase, α is the void
b mf
fractionatminimumfluidizationcondition,c isthesolidvolume
v
concentration,u b isthevelocityofgasinthebubblephase,u mf is t=tend ? No
theminimumfluidizationvelocity,C istheconcentrationofgas
gb;i
species i in the bubble phase, C is the concentration of gas
ge;i
species i in the emulsion phase, x is the mass fraction of solid Yes
s;i
speciesi,K isthemasstransfercoefficientbetweenbubbleand
be
emulsionphase,v i;j isthestoichiometriccoefficientofspeciesiin END
reaction j, D is the axial dispersion coefficient of gas phase,
g;ax
D is the axial dispersion coefficientof solid, r is the reaction Fig.5. Flowchartforsolutionprocedureoftwo-phaseflowmodel.
s;ax b;j
Table2
Correlationsusedforcalculatingthehydrodynamicparametersintwo-phaseflowmodel.
AwidelyusedcorrelationgivenbyWenandYu[38]forcalculatingumfisgivenby
umf¼ Re d p p ;m ρ f g μ g,whereRep;mf¼ qffi C ffiffiffi 2 1 ffiffi þ ffiffiffiffiffi C ffiffiffi 2 ffiffi A ffiffiffi r ffiffi (cid:3) C1andAr ¼ dpρ gð ρ μ s 2 g (cid:3) ρ gÞ g
SeveralvaluesforC1andC2areproposedintheliterature[39].
Thevoidfractionatminimumfluidization(αmf)canbecalculatedbysolvingtheequationderivedfromErgunequation[79]
α
1
3 m
:7
f ϕ
5
s
Re2
p;mfþ
150
α
ð
2 m
1
f
(cid:3)
ϕ2 s
αmfÞRep;mf¼ Ar
Thevoidfractionofbubble(αb)canbecalculatedas
αb¼ 1
(cid:3) ð 1 (cid:3)
c
α
v
mfÞ
Thesolidvolumeconcentrationcvcanbecalculatedas
cv¼ð 1
(cid:3)
αbÞð 1
(cid:3)
αmfÞ

was 71%andmaximumdeviationoftemperaturewas51C.Hamel
and Krumm [43] used the two-phase flow model to simulate four
bubblingfluidized bedgasifiersofdifferentscalefromatmospheric
lab-scaletopressurizedcommercial-scale.Simulatedresultsofover-
all carbon conversion, freeboard temperature and the gas species
concentrationdeviated 710%fromexperiment.FiaschiandMiche-
lini [44] used a two-phase flow model to study the biomass
gasification kinetics in bubbling fluidized bed gasifier. The model
predicted temperature and concentration gradient along the axis.
The model result showed largely satisfactory agreement with the
experimental result from the literature and the requirement of
furthervalidationofthemodelwasidentified.Sadakaetal.[45–47]
developed a two-phase model for predicting the performance of
dualdistributortypefluidizedbedbiomassgasifier.Theyassumed
that the fluidized bed consisted of a dilute phase (jets, bubbles
and/or slugs) and an emulsion phase. The emulsion phase was
divided into an interstitial gas phase and a solid phase. Model
predicted the bed temperature, gas composition, heating value
and gas yield. Sensitivity analysis was carried out by varying
fluidizationvelocity,steamflowrateandbiomass-to-steam ratio.
20
The model results predicted the experimental data with higher
accuracy(R2 0.88 0.98).ChejneandHernandez[48]developed
aonedimens ¼ ional (cid:3) two-phasemodeltosimulatethecoalgasifica-
15 tion in fluidized bed. The model predicted temperature, gas
composition, volume fraction, velocity and other fluid dynamic
parameters.Themodelresultsshowed20%errorwhilecompared
10 withthe experimental resultsfromtheliterature.Ross etal.[49]
improved the isothermal two-phase flow model by considering
the non-isothermal behavior of gases and heat transfer mechan-
5
ismsandusedtostudythefluidized-bedcoalgasificationprocess.
Isothermalandnon-isothermalsimulationswererunforthepilot-
scale and commercial-scale gasifier. Gas composition, bed tem-
perature and reaction rate were predicted. The good agreement
0
with experimental results was found for non-isothermal simula-
10 11 12 13 14 15 16
tionandsignificantdeviationwasfoundforisothermalsimulation.
Petersen and Werther [22] used two-phase flow models for
simulating the gasification of sewage sludge in a pilot-scale
circulating fluidized bed gasifier. Initially, a pseudo-two-
dimensional model was developed and the gas composition was
and for low temperature it was not good. Chatterjee et al. [40] calculated by selecting the reaction kinetics from the literature.
studied the gasification of high ash Indian coal in a lab-scale Thenthekineticsofpyrolysisandmaingasificationreactionswere
fluidizedbedgasifierbyusingtwo-phase flowmodel.Steam-and determined by comparing the pseudo-two-dimensional model
air was used as the gasifying agent. The gas composition, tem- results with the experimental data. Finally, a three-dimensional
perature, carbon conversion and calorific value of gas with model [36] was developed with the modified reaction kinetics.
different operating conditions were simulated. The comparison Fig. 7 shows the axial gas composition profile for pyrolysis, CO
2
between simulated and experimental results showed similar gasification and air-gasification obtained from experiment and
trend.Forexample,thesimulatedandexperimentalgascomposi- pseudo-two-dimensional model with fitting parameters. Good
tion,calorificvalueandtemperatureasafunctionofoxygenfeed agreement between calculated and measured gas composition
rateforcoke-breezeandbituminouscoalwereshown(Fig.6)and was seen after fine tuning the reaction kinetics. Radmanesh
the estimated error between prediction and experiment was etal.[50]usedonedimensionalisothermaltwo-phaseflowmodel
within12%.Yanetal.[41]studiedthefluidizedbedcoalgasifica- to study the fluidized bed gasification of biomass. Two different
tionbyusingtwo-phaseflowmodelandshowedthatthechange kinetic models for pyrolysis were used and their impact was
involumeofgasduetoreactionresultedinahighervelocity.The studied. The effect of equivalence ratio, steam-to-biomass ratio,
suspension phase gas stayed at minimum fluidization, only the bed temperature, feed location, and mass transfer between the
bubblephasegasvelocitywasincreased.Thus,anet-flowconcept countercurrentregionsonthegascompositionwasstudied.They
wasaccountedforwhichconsideredtheproductionorreduction showedtheimportanceofthepyrolysisstepinpredictingthefinal
of gaseous volume by reaction and it was directed from the gascompositionbycomparingthesimulatedgascompositionwith
suspension phase to the bubble phase. The results showed that experimentaldata.Thepyrolysismodelderivedathigherheating
the net-flow is significant, in the range 71–87 %, relative to the ratesestimatedthefinalgascompositionrelativelybetterthanthe
feed gas rate. Simulation without net-flow deviated significantly onederivedatlowerheatingrate.Thestronginfluenceofpyrolysis
from experiment. Jennen et al. [42] studied the gasification of step on the overall performance of the fluidized bed biomass
wood in a pilot-scale circulating fluidized bed by using one- gasificationwasalsoidentifiedbyKaushaletal.[51]intheirtwo-
dimensional two-phase flow model. The calculated axial profile phase flow modeling study. Pengmei et al. [52] studied the
of the gas composition and the temperature are compared with biomassgasificationinfluidizedbedusingtwo-phaseflowmodel
the experimental data and very good match was found. The andshowedthatthetrendofchangingthegascompositionwith
differencebetweenthemeasuredandthecalculatedgascomposition temperaturewasinaccordancewiththeexperiment.However,the
)v/v
%(
noitisopmoc
sag
tcudorP
4.0
CV
Prediction
3.5
3.0
2.5
2.0
1.5
11 12 13 14 15 16
CO
H
2
CO
2
CH
4 Prediction
Oxygen in feed (mol %)
))PTS(3m/JM(
eulav
acifirolaC
)Co(
erutarepmeT
696 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
1020
T 1000
980
960
940
920
900
880
860
840
820
800
Oxygen in feed (mol %)
Fig.6. Effectofoxygeninthefeedon(A)bedtemperatureandcalorificvalueand
(B)productgascomposition.Steam:6.8kg/h;Coal:coke-breeze,10kg/h[40].

12
11
10
9
8
7
6
5
4
3
2
1
0
after cyclone
Feed
gasyieldfromthesimulationwashigherthatexperiment.Itwas model to study the fluidized bed biomass gasification process
explained that, in simulation, all char particles were assumed to includingthetarconversion.Effectsofgasificationtemperature,bed
take part in the reaction and no illusion or escape from the bed operational velocity, equivalence ratio, biomass particle size and
which resulted more gas yield. Goyal et al. [53] studied the biomass-to-steam ratio on the hydrogen production was studied.
fluidizedbedgasificationofmixtureofcoalandpetcokebyusing Themodelwascapableofpredictingconcentrationdistributionofgas
two-phaseflowmodel.Theeffectofvariousoperatingparameters speciesandtaralongtheheightofthegasifier.Simulatedhydrogen
suchascompositionoffeed,locationoffeedpointandashcontent production was compared with experimental data which showed
on the performance of the gasifier were studied. Results showed largely satisfactory agreement but the effect of considering the tar
thattheincreaseinpetcokecontentinthefeedmixturetendsto conversionwasnotshown.
lower the efficiency and carbon conversion but increases the Till date, the two-phase model is the most established model
amount of syngas produced and increase in ash content of coal for simulating the fluidized bed gasificationprocess published in
decreasesthecarbonconversion.Themodelresultsalsoidentified theopenliterature.Itiscomparativelysimplebecauseitdoesnot
thatfeedpointofthesolidsshouldbeabovethepointwhereO in consider the complex gas–solid dynamics but still maintains the
2
the bed gets exhausted, in order to obtain the maximum carbon fluiddynamiceffect.Therefore,itcanprovideimportantinforma-
conversion and efficiency. Gungor [54] used two-phase flow tionaboutthefluidizedbedgasifierlikethetransientnatureofthe
war
%-lov
,noitartnecnoC
Height, m
25
20
15
10
5
0
after cyclone
Feed Height, m
war
%-lov
,noitartnecnoC
0 2 4 6 8 10 12 14 16 18
18
16
14
12
10
8
6
4
2
0
after cyclone
Feed top of riser
war
%-lov
,noitartnecnoC
C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 697
0 2 4 6 8 10 12 14 16 18
O2
CO2
CO
H2
CH4
C2H4
H2O
0 2 4 6 8 10 12 14 16 18
Height, m
Fig.7. Axialprofileofsimulatedandmeasuredgascompositionin(A)pyrolysis,(B)CO2gasification,and(C)air-gasificationexperimentsandmodelingresultsfrompseudo-
two-dimensionalmodel[36].

698 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
gasifier,distributionofgasspeciesandreactingparticlesinsidethe where μ is the solid shear viscosity and λ is the solid bulk
s s
reactor,bubblesizeandvelocity,temperaturedistributionetc.But, viscosity.
duetothefactthatthehydrodynamicsisbasedonsomecorrela- The Euler–Euler model became more popular after the devel-
tions, the applicability of the two-fluid model is restricted tothe opmentofKineticTheoryofGranularFlow(KTGF)whichisbased
operating condition on which these correlations are valid. The on the theory of non-uniform dense gases described in the
mostcommonassumptionoftwo-phaseflowmodelistheperfect literature [55]. The pioneering paper of Lun et al. [56] applied
mixing of solid and plug flow of gas in bubbles and emulsion thekinetictheoryofgasestogranularflow.SinclairandJackson[57]
phaseswhicharesometimesnotprevailinthebed.Thetwo-phase appliedthegranularflowmodeltoafullydevelopedgas–solidsflow
flowmodelingapproachcannotbeappliedtothefreeboardregion in a pipe. Ding and Gidaspow [58] derived expressions for solids
of the bed, the freeboard is separatelymodeled. Besides, mostof viscosity and pressure of a dense gas–solids flow. Gidaspow [59]
thetwo-phaseflowmodelsareeitheronedimensional.Therefore, extended the Ding and Gidaspow [58] formulation to both dilute
the computational fluid dynamic (CFD) model by coupling the anddensephasebyconsideringanon-Maxwellianvelocitydistribu-
detail fluidized bed hydrodynamics and reaction kinetics may tion.Huilinetal.[60]appliedKTGFtostudythemotionofparticles
overcome the above disadvantages of two-fluid model and can in the gas bubbling fluidized bed with the binary mixtures. Louge
providesmoreinsideintothefluidizedbedgasifier.InCFDmodels, etal.[61],Pita and Sundareasan[62]andHrenyaandSinclair[63]
thehydrodynamicsoffluidizedbedisbasedoneithertheEuler– incorporated the effects of gas turbulence into their models by
EulerconceptortheEuler–Lagrangeconceptasdiscussedbelow. modifying single-phase turbulence closures to account for the
presenceofparticlephase.SamuelsbergandHjertager[64]included
4.2. Euler–Eulermodel the gas turbulence by using LES method and particle–particle
interaction using the kinetic theory approach. Nieuwland et al.
InEuler–Eulermodel,thegasandthesolidphasesaretreated [65], Balzer et al. [66] and Neri and Gidaspow [67] conducted
as interpenetrating continuum present at the same time in the simulationsofgas–solidsflowinthecirculatingfluidizedbedusing
same controlvolume. The hydrodynamic model uses the conser- KTGF. Armstrongetal.[68]applied KTGFtostudythe wall-to-bed
vationofmassandmomentumofeachphaseandrepresentedby heattransferinabubblingfluidizedbed.Lohaetal.[69–71]studied
respective conservation equations. The interaction between two the effect of gas–solid drag model, the solid phase wall boundary
phases is expressed as additional source terms added to the conditionandcoefficientofrestitutiononthehydrodynamicbeha-
conservationequations.Theconservationequationsformassand vior of a bubbling fluidized bed by using KTGF. Papadikis et al.
momentumaresolvedforthegasandsolidphaseseparatelyand [72,73]usedKTGFtostudytheeffectofdragmodelandparticlesize
areclosedwithappropriateconstitutiverelations. influidizedbedsystem.DeWildeandTrujillo[74]appliedKTGFto
Continuityequationforthegasphaseisgivenby studythecatalyticcrackingofgasoilinarotatingfluidizedbed.
∂ InKTGF,thekineticenergyassociatedwiththeparticlevelocity
∂tð α g ρ gÞþ ∇: ð α g ρ g!v gÞ¼ S gs ð 41 Þ fluctuations is represented by a pseudo-thermal or granular
temperature which is proportional to the mean square of the
Continuityequationforthesolidphaseisgivenby
random motion of particles. A separate partial differential equa-
∂ ∂ tð α s ρ sÞþ ∇: ð α s ρ s!v sÞ¼ S gs ð 42 Þ t fo io r n th is e so tu lv r e b d ul f e o n r c t e he m g o r d a e n l u in la g r i t n em th p e er s a o t l u id re p w h h as ic e h . T fo h r e m n s , t t h h e eb so a l s i i d s
whereαisthevolumefraction,ρisthedensity,!v isthevelocity phasepropertieslikesolidviscosityandpressurearedescribedas
vectorandS isthemasssourcetermduetochemicalreactions. afunctionofgranulartemperature.
gs
The momentum equation for gas phase is given by the Navier– Thegranulartemperatureequationisrepresentedas
Stokes equation, modified to include the inter-phase momentum
3 ∂
transferterm. 2 ∂tð α s ρ s Θ sÞþ ∇U ð α s ρ s!v s Θ sÞ ¼ð(cid:3) p s I þ τ gÞ
Momentumequationforthegasphaseisgivenby (cid:5) (cid:6)
∂
:∇!v
sþ
∇U
ð
κ Θs∇Θ
sÞ(cid:3)
γ
Θsþ
φ
gs
∂tð
αgρ g!vgÞþ ∇:
ð
αgρ g!vg!vgÞ¼(cid:3) αg∇p
þ
∇:τgþ αgρ g!g
þ
Kgsð !vs(cid:3) !vgÞþ Sgs!vg
47
ð Þ
43
ten w so h r, er g ep is is t t h h e eh a y c d c r e o le d r y a n t a io m n ic d s u p e res t s o ur g e r , a τ v g it is y th a e nd vis K co gs us is st ð r t e h s e s Þ t w c e o h n e e s ffi o re r c . i ð e ∇ (cid:3) n : t ð p ) κ s . Θ I γ s þ ∇ Θs τ Θ g i s s Þ Þ : t i h ∇ s e ! t v h c s e o i l s d li i t s f h i f o u e n s g a io e l n n d e i o r s a f s t i e p io n a n e ti r o o g n f y e o n ( f κ e Θ r e s g n y i e s r b g t y h y s e o an l d i d d iff s u φ t s g r s i e o s i n s s
momentumtransferbetweengasandsolidphases. theexchangeoffluctuatingenergybetweenphase.
Thestresstensorofthegasphasecanbegivenas Intheliterature,thereisageneralagreementonthecorrelation
T 2 of solid bulk viscosity and solid pressure [56] which are given
τ g¼ α g μ gð ∇!v gþ ∇!v gÞ(cid:3)3 α g μ g : ð ∇:!v gÞ I ð 44 Þ below.
where μ is the coefficient of viscosity which depends on the 4 Θ 1=2
thermodynamic state of the fluid for laminar flow and have an λ s¼3 α s ρ s d s g o;ssð 1 þ e ssÞ π s ð 48 Þ
addededdyviscosityforturbulentflow. (cid:2) (cid:3)
Since the solid phase is treated as continuous fluid, it has p αρΘ 2ρ 1 e α2g Θ 49
similarpropertiestoafluid. s¼ s s sþ sð þ ssÞ s o;ss s ð Þ
Momentumequationforthesolidphaseiswrittenas where e ss is the restitution coefficient and g o;ss is the radial
distributionfunction.
∂
∂tð αsρ s!vsÞþ ∇U ð αsρ s!vs U!vsÞ¼(cid:3) αs∇p (cid:3) ∇p sþ ∇Uτsþ αsρ s!g þ Kgsð !vg(cid:3) !vsÞþ Sgs!vs Forthesolidsshearviscositydifferentdescriptionsaregivenby
45 different authors and theyare listed in Table 3. For example, the
ð Þ
equationgivenbyGidaspow[59]doesnotaccountfortheinelastic
wherep isthesolidpressureandτ isthesolidphasestresstensor.
s s natureofparticlesinthekineticcontributionofthetotalstress,as
Thestresstensorforthesolidphaseisgivenby
Lunetal.[56]did.ThesolidsshearviscosityofSyamlaletal.[75]
τ
s¼
α
s
μ
s
∇!v
sþ
∇!v T
s (cid:3)
α
s
λ
s(cid:3)
2
3
μ
s ð
∇U!v
sÞ
I
ð
46
Þ
n
di
e
l
g
u
l
t
e
e
c
-
t
p
e
h
d
a
t
s
h
e
e
fl
k
o
i
w
ne
.
t
H
ic
re
o
n
r
y
s
a
tr
a
e
n
am
d
i
S
n
i
g
nc
c
l
o
ai
n
r
tr
[
i
6
b
3
u
]
ti
f
o
o
n
ll
,
o
w
w
h
e
i
d
ch
Lu
d
n
om
et
in
a
a
l
t
.
e
[
s
56
in
]
(cid:2) (cid:3) (cid:2) (cid:3)

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 699
Table3
Solidshearviscosity.
Equation Reference
μ s¼ 5p 96 τΘρ sds η 1 g0þ 8 5 αs 1 þð 8=5 Þ2 η
(cid:3)
ð 3η η(cid:3) 2 Þ αsg0 Lunetal.[56]
ffiffiffiffi h(cid:8) (cid:9)(cid:8) (cid:9)i
μ s¼ 4 5 α2 s ρ sdsg 0ð 1 (cid:3) e Þ p π Θ þ αs 6 ρ ð s 3 d (cid:3) sp e π Þ Θ1 þ 2 5ð 1 þ e Þð 3e (cid:3) 1 Þ αsg 0 Syamlaletal.[75]
μ s¼ 4 5 α2 s ρ sdsg 0ð 1 þ e Þ p π ffi Θ ffiffi þ ð 5pπ ð 1 =4 þ 8 ffiffi eÞ ffi Þ ffi ρ ffi g (cid:10) s 0 dspΘ1 þ 4 5ð 1 þ e Þ αsg 0 2 (cid:11) Gidaspow[59]
μ s¼ 5p 96 ffi π ffi Θ ffiffiffi ρ sds (cid:5)(cid:2) 1 þð λ 1 mfp ffi = ffiffi R Þ η 1 g0þ ffiffi 8 5 αs (cid:3)(cid:8) 1 þ ffiffiffi ð (cid:10) 8=5 Þ2 η (cid:3) ð 3η η(cid:3) 2 Þ αsg0 (cid:9) þ (cid:11) 7 2 6 5 8 π ηα2 s g 0 (cid:6) HrenyaandSinclair[63]
Table4
Gas–soliddragmodels.
Equation Reference
Kgs¼u ρ
t
s
α
α
sn
g
(cid:3)
g
1
RichardsonandZaki[76]
Kgs¼ 3 4 CD ρg d α s s!vs(cid:3) !vgα g(cid:3) 2:65 WenandYu[77]
CD¼αg 2
R
4
es
1
þ
(cid:7) (cid:7)
(cid:7)
0:15
ð
αgR (cid:7) (cid:7)
(cid:7)
esÞ 0:687
Kgs¼ 3
4
α
v
s
2r
α
;s
g h
d
ρ
s
gCD R
vr
e
;s
s !vs(cid:3) !vg; i Syamlal-O’Brine[75]
(cid:8) (cid:9)(cid:7) (cid:7)
CD¼
(cid:2)
0:63
þpR
4
e
:
s
8
=v
(cid:7) (cid:7)
r;s(cid:3)
2 ; Res (cid:7) (cid:7)
¼
ρgds
(cid:7) (cid:7)
!v
μ
s
l
(cid:3) !v g
(cid:7) (cid:7)
;
(cid:7) (cid:7)
vr;s¼ 0:5 A (cid:3) 0:ffi0ffiffiffi6ffiffiffiRffiffiffieffiffi sþ ð 0:06ResÞ 2 þ 0:12 ð 2B (cid:3) A Þþ A2 ;
(cid:2) qffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi(cid:3)
A
¼
α4
g
:14; B
¼
0:8α1
g
:28 for αg r0:85; B
¼
α2
g
:65 for αg40:85
Kgs¼ 1 R 7 e : s 3 þ 0:336 ρ d g s !vs(cid:3) !vgαsα g(cid:3) 1:8 Gibilaroetal.[82]
h i (cid:7) (cid:7)
Res¼ dsαg
(cid:7) (cid:7)
!v
2
s
μ
(cid:3)
g
!v g
(cid:7) (cid:7)
ρg (cid:7) (cid:7) (cid:7) (cid:7)
Kgs¼ 1 R 7 e : s 3(cid:7) þ 0:336 (cid:7)ρ d g s !vs(cid:3) !vgαsα g(cid:3) 2:8 Arastoopouretal.[80]
h i (cid:7) (cid:7)
Res¼ ds
(cid:7) (cid:7)
!v s
μ
(cid:3)
g
!v g
(cid:7) (cid:7)
ρg (cid:7) (cid:7) (cid:7) (cid:7)
K K g g s s ¼ ¼ 1 3 4 C 5 (cid:7) D 0 ρ α α d g g 2s α p d μ s g 2 s ! þ v 1 s (cid:7) : (cid:3) 75 !v α d s g ρ s g (cid:7) (cid:7) (cid:7) α ! g v (cid:3) 2 s : (cid:3) 65 ! ; vg α (cid:7) (cid:7) (cid:7) ; g Z α 0 g : o 8 0:8 Gidaspow[59]
(cid:7) (cid:7)
CD¼8
<
αg
0
2
R
4
:
e
4
s
h4
(cid:7)
(cid:7)
1
;
þ
0:15
ð
α(cid:7) (cid:7)gResÞ 0:687
i
;Res
R
o
es
1
Z
00
1
0
000
Res¼ :ρg
(cid:7) (cid:7)
!v s
μ
(cid:3)
g
!v g
(cid:7) (cid:7)
ds
K Re gs s ¼ ¼ C ρg (cid:8) (cid:7) ds 1 R (cid:7) (cid:7) 7 ! e v : s 3 þ μ s g (cid:3) 0 !v :3 (cid:7) g 3 (cid:7) (cid:7) 6 εg (cid:9) ρg (cid:7) (cid:7) (cid:7) !v s d (cid:3) s !v g (cid:7) (cid:7) (cid:7) αsα g(cid:3) 1:8 McKeenandPugsley[81]
Kgs¼ 150 (cid:7)
α
α
g
2s
d
μg
2 sþ
1:7 (cid:7) 5α
d
sρ
s
g!vs(cid:3) !vg; αg o0:74 Yangetal.[83]
Kgs¼ 3
4
CD ρgα
d
g
s
αs!vs(cid:3) !vg (cid:7) (cid:7)
(cid:7)
ω (cid:7) (cid:7)
(cid:7)
(cid:3) 0:5760 þ4 ð αg (cid:7) (cid:7) (cid:7)(cid:3) 0:7 0 4 :0 6 2 3 1 Þ 2 4 þ (cid:7) (cid:7) (cid:7)0:0044 ; 0:74rαg r0:82
(cid:3)
0:0101
þ4
ð
αg(cid:3) 0:7
0
7
:0
8
0
9
3
Þ
2
8
þ
0:0040
; 0:82rαg r0:97
(cid:3)
31:8295
þ
32:8295; αg40:97
approach, but constrained the mean free path of the particle by a than 0.2. Arastoopour et al. [80] proposed a drag model which
dimensioncharacteristicoftheactualphysicalsystem. gave continuous value over all range of solid volume fraction.
The gas–solid dragmodel plays animportant rolein fluidized McKeenandPugsley[81]proposedadragmodelbyintroducinga
bedmodeling.Differentgas–soliddragmodelsareavailableinthe constant scale factor in Gibilaro et al. [82] model to reduce the
literatureandtheyarelistedinTable4.Anearlierdragmodelwas dragforceandtakingintoaccounttheinterparticlecohesiveforce
proposedbyRichardsonandZaki[76].WenandYu[77]proposed onparticleagglomeration.Toinvestigatethedependence ofdrag
adragmodelbyextendingtheworkofRichardsonandZaki[76]. coefficient on structure parameters, Yang et al. [83] adopted a
ThemodelproposedbySyamlal-O'Brien[78]whichwasbasedon structure-dependent drag model based on the energy minimiza-
the measurement of terminal velocity of solid particle in the tionmulti-scale(EMMS)approach.
fluidized bed. The Gidaspow mode [59] was a combination of TheEuler–Eulertwo-fluidmodelincombinationwithKTGFis
Wen and Yu model [77] for solid volume fraction lower than widely applied for investigating the hydrodynamics of fluidized
0.2andErgunmodel[79]forsolidvolumefractionequalorlarger bedsystem.But,itisdifficulttocouplethecomplicatedchemical

700 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
reactionswiththefluidizedbedhydrodynamicsduetothecomplex
START
mechanism of heat transfer and chemical reaction need to be
modeledinfluidizedbedgasificationprocess.Tomodelthechemical
reactions,morecarefulconsiderationhastobegivenonthesolution INPUT
of large numbers of energy and species transport equations and
nonlinear source terms of complicated chemical reactions. For INITIAL ASSIGNMENT
modelingthefluidizedbedsystemwithchemicalreactionbyusing
Euler–Euler model, in addition to the continuity and momentum
equation, species conservation equation for each gas species and t=t+n∆t
energyequationforgasandsolidphaseisrequiredtosolve.
Thespeciestransportequationisgivenby SOLVE MOMENTUM EQUATIONS
using calculation for granular temperature,
∂ ∂ tð ρ g α g Y g;iÞþ ∇ ð ρ g α g!v g Y g;iÞ¼(cid:3) ∇U ð α g J g;iÞþ α g R g;iþ R s;i ð 50 Þ drag stress for the relevant phases
where J , R and R are the diffusion flux of species i in gas SOLVE FOR PRESSURE CORRECTION
g;i g;i s;i update velocity and mass
phase,thenetrateofproductionofhomogeneousspeciesiandthe
n=n+1
homogeneousreactionrate,respectively.
SOLVE FOR REMAINONG SCALAR EQUATION
In species transport equations of gas phase, mass diffusion
Energy, species, turbulence
coefficient are used to calculate the diffusion flux of chemical
speciesinturbulentflowusingmodifiedFick'slaw
μ CHECK IF No
J g;i¼(cid:3) (cid:2) ρ g D m;iþσ Y t (cid:3) ∇UY g;i ð 51 Þ CONVERGED?
whereσ istheSchmidtnumber,whichissetas0.7.Thediffusion Yes
Y
coefficientofthemixture,D iscalculatedfromthebinarymass
m;i
diffusioncoefficientD asfollows:
i;j No t=tend ?
1 X
D m;i¼∑ja (cid:3) i X j = i D i;j ð 52 Þ Yes
Theenergytransportequationsaresolvedforthespecificenthalpy
ofgasphaseandsolidphase,whichtaketheform: END
∂ ∂ tð α g ρ g H gÞþ ∇U ð α g ρ g!v g H gÞ¼ ∇ ð k g T gÞþ Q gsþ S gs H s ð 53 Þ Fig.8. FlowchartforsolutionprocedureofEuler–EulerCFDmodel.
and Table5
∂ Comparison between simulated and experimental data for steam reforming of
∂tð α s ρ s H sÞþ ∇U ð α s ρ s!v s H sÞ¼ ∇ ð k s T sÞþ Q sgþ S sg H s ð 54 Þ glycerolinfluidizedbedreactor[87].
where H, k, Q are the specific enthalpy, the gas mixture thermal Experimentaldata Simulation
conductivityandtheintensityofheatexchangebetweenthegasand
Inletgasvelocity(m/s) 0.5 0.5
solidphases,respectively.Thethirdtermontherighthandsideisthe
Steamtocarbonmolarratio(S/C) 2:1 2:1
heattransferinthatthesolidphasechangedintogasphase. Catalyst NiO/Al2O3 NiO/Al2O3
Thespecificenthalpyisdefinedby Temperature(1C) 600 600
H ¼ i ∑ n 1 Y i H i ð 55 Þ H C C O H 2 2 4 (v ( ( o v v o o l% l l % % ) ) ) 5 5 27 . 9 9 . . 2 1 1 5 3 3 2 3 . . . 9 6 5
where
¼
H istheenthalpyforeachchemicalspeciesinthemixture
CO(vol%) 7.8 0.0(3.5
(cid:4)
10(cid:3) 15)
i
andconsidersboth,thermalandchemicalenthalpy
T distributionexhibitedamoreheterogeneouscore-annulsstructure
H i¼ C P;i dT þ ΔH f;i ð 56 Þ of gas–solid flow which led to back mixing and internal circula-
ZT0 tion.Thisflowstructuresuggestedthatthebedshouldbeagitated
where T , C and ΔH are the reference temperature, the heat tomaintainsatisfactoryfluidizingconditions.Theglycerolconver-
0 P;i f;i
capacityatconstantpressurefortheithspecies,andtheenthalpy sion and H production variation with inlet gas velocity was
2
offormationfortheithspeciesinthestandardstate. studied. The simulated results were also validated with experi-
The above conservation equations are solved by using CFD mental results as shown in Table 5. The difference between
technique to get the gas and solid velocity distribution, volume simulated and experimental gas composition was less than 8%.
fraction distribution, gas composition distribution and tempera- But, the model predicted very less (3.5 10(cid:3) 15%) amount of CO.
turedistributioninsidethegasifierandtheirvariationwithtime. Though, it was mentioned that the erro (cid:4) r incurred in calculation
AtypicalsolutionprocedureforEuler–Eulertwo-fluidmodelingof derivedfromseveralsourcessuchasflowandreactionratemodel,
fluidized bed gasification process using Phase Couple SIMPLE numericaltreatmentofinitialandboundaryconditionsandother,
algorithmisshowninFig.8. but, the specific reason for predicting very less amount of CO
Very few studies on fluidized bed gasification process using compositionwasnotdescribed.Papadikisetal.[86,87]studiedthe
Euler–Euler model are available in the literature. Dou et al. [84] fast pyrolysis of biomass in a lab-scale bubbling fluidized bed
and Dou and Song [85] studied the hydrogen production from reactor by using Euler–Euler model. The Eulerian approach was
steamreformingofglycerolinalab-scalefluidizedbedreactorby used to model the bubbling behavior of sand. The discrete
usingtheEuler–Eulermodel.Thesimulationwasperformedfora description was used for modeling the biomass particle injected
two-dimensional computational domain. The simulated flow inside the reactor and the motion of the particle was computed

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 701
using local volume fraction dependent drag laws. 2-D and 3-D to devolatilization and equilibrium of water-gas-shift reactions.
simulationswererun.Itwasshowedthatinthe3-Dsimulationa ThisshowedthattheEuler–Eulermodelgavemoreexactpredic-
bubble was formed close to the feeding point of the reactor and tionwhich couldnotbe described bytwo-phaseflow model. For
the drag forcewas quitereduced at the injection time compared validation, the predicted outlet gas compositions for sixdifferent
with the 2-D case. The simulated hydrodynamic behavior of the operatingconditionswerecomparedwiththeexperimentalresult
bed at different time where biomass particle position was indi- from the literature as shown in Fig.11. It was observed that the
catedbyblackspotisshowninFig.9.Themodelgaveimportant predicted results agreed well tothe experiment with 5% error in
information like hydrodynamic of bed with biomass particle CO andN molarfractionandwithin20%errorforotherresults.
2 2
position, degradation and evolution of tar with time but no Wang et al. [90] extended the above simulation in three dimen-
experimental validation was provided. Xue et al. [88] also simu- sional geometry to take into account the influences of bed walls
lated the fast pyrolysis of biomass in a lab-scale fluidized bed and geometry on the flow pattern and other aspects in 3D.
reactor by using Euler–Euler model. Here, gas–particle flow was Armstrong et al. [91] also simulated the same lab-scale bubbling
modeled with a multi-fluid description (gas, sand and biomass). fluidized bed coal gasifier using Euler–Euler model. They have
Results indicated that biomass particle size and superficial gas introducedthelimestonecalcinationstotheirmodel.Theirmodel
velocityinfluenced the tar yield and residence time considerably consideredtwosolidphasesoneforlimestoneandotherforchar
withafixedbedheight. Thesimulatedyields ofbio-oil,charand which enabled to simulate the segregation of lower density
non-condensablegaswerecomparedwiththeexperimentaldata particles(char)tothetopofthebed.Thehydrodynamicinvestiga-
forpurecelluloseandredoakasshowninTable6.Thepredicted tionrevealedthebubbleformationexogenouslyandendogenously
resultsshowedgoodquantitativeagreementwiththeexperimen- asaresultofthereactionkineticsasshowninFig.12.Adetailed
tal data for the yield of each product. But, the model over- analysis of gasification process was presented from the distribu-
predictedtheunreactedbiomass(residue)particularlyforsmaller tionofgascomposition,temperatureandreactionrateinsidethe
particles.Therefore,itwassuggeststhataparticlesizedistribution gasifier. The model results considering inert limestone and lime-
mayneedtobeconsideredtoimprovethesimulation.Yuetal.[89] stone calcinations were comparedtothe experimental data from
simulated the lab-scale bubbling fluidized bed coal gasifier by theliteratureasshowninTable7.Themodelgavereasonablygood
using Euler–Euler model. Their model was two dimensional and representationofexperimentalcompositionsasawhole.However,
the gasification kinetic was described by 15 species and 11 unlike experiment, model 1 predicted higher CO than CO . They
2
chemical reactions which include pyrolysis, homogeneous reac- expectedthatthiswasduetofactthatexperimentalbedconsisted
tions and heterogeneous reactions. The devolatalization and dry- of limestone whereas the model was formed of both char and
ing was assumed as instantaneous process in the feed zone. limestone.However,model2gavehigherCO comparedtomodel
2
Pressure, temperature, velocity, volume fraction of gas composi- 1 due to the lower initial temperature of the bed. The gas
tion were predicted. The simulated distribution of gas composi- compositiondidnotchangesignificantlybyconsideringlimestone
tions within the gasifier was plotted for six different operating calcinationsduetoslowconversionrateoflimestonedecomposi-
conditions and two of them are shown here in Fig. 10. It was tion. The above simulation was also extended to determine the
observedthatoveralltrendofeachcompositionwasinconsistence effectsofdifferentbedratiosandoveralongerperiodoftime[92].
withtheoperatingconditions.Forexample,theconcentrationsof Theaboveliteratureshowedthat,theEuler–Eulermodelisan
CO andCOincreasedalongtheheightofthegasifier,whileH and efficientwaytostudythefluidizedbedgasificationprocesswhere
2 2
CH goupatfirstandthendropdowntothetopofthereactordue the gas and the solid phases are treated as the interpenetrating
4
continuum and detail momentum equations are solved for both
thephasesincombinationwithreactionkineticstogetadetailed
insightintothegasifier.Incontrasttothetwo-phaseflowmodel,
the Euler–Euler model can simulate the dense bottom bed and
freeboard region both simultaneously and the three dimensional
flowscanbe solved.Itcanprovidemuchmoredetailed informa-
tioncomparedtothetwo-phaseflowmodelwhichareverymuch
useful for design and optimization. The Euler–Euler model can
predict thebubble formation, bubble ricethroughthe bed, inter-
actionwithotherbubblesandgrowthinsizeanderuptionatthe
uppersurfaceofthebedduringfluidizedbedgasificationprocess.
Itcanprovidetheaxialandradialvariationofgasandsolidvolume
fractions, gas composition, temperature and reaction rates inside
thegasifier.Inadditiontotheeffectofoperatingparameters,other
Fig.9. Fluidizedbedhydrodynamicswithbiomassparticleposition[89]. effectslikepositionoffuelinlet,gasinlet,outlet,geometryofthe
Table6
Comparisonbetweensimulatedandexperimentalproductyieldforfluidizedbedfastpyrolysisofbiomass[88].
Method Bio-oil Char Non-considerablegas Residual Temperature(1C)
Productyields(wt%)ofpurecellulosepyrolysisfromexperimentandsimulation
Experiment 82.1 2.2 12.4 – 500
Simulation 82.2 3.3 13.9 0.5 493
Productyields(wt%)ofatypeofredoakpyrolysisfromexperimentandsimulation
Experiment 71.771.4 13.071.5 20.571.3 – 500
Simulation(dp¼ 250µm,2D) 60.5 12.3 16.2 11.0 497
Simulation(dp¼ 325µm,2D) 62.4 14.1 17.3 6.2 498
Simulation(dp¼ 325µm,2D) 61.5 12.9 16.5 8.7 499
Simulation(dp¼ 400µm,2D) 63.4 15.1 18.1 3.4 499

702 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
Fig.10. ConcentrationdistributionofH2,CO2,N2,CH4andCOfordifferentoperatingconditions:Case1:8.0kg/hcoalfeed,21.9kg/hairsupply,4.6kg/hsteamsupply,4201C
airandsteamtemperature,8551Creactortemperature.Case2:8.0kg/hcoalfeed,17.0kg/hairsupply,4.6kg/hsteamsupply,4131Cairandsteamtemperature,and8121C
reactortemperature[84].
gasifier, initialbed heightetc. canalso be studied. InEuler–Euler gasification process cannot be modeled here. Therefore, to get
model, the mixing and segregation between inert bed material more particle level information of fluidized bed gasification
and solid fuel particle inside the gasifier can also be studied by process,Euler–Lagrangemodelingisrequired.
taking two different solid phases with different material proper-
ties. The Euler–Euler model is computationally less expensive 4.3. Euler–Lagrangemodel
comparetotheEuler–Lagrangemodelbecauseitassumesparticles
ascontinuuminsteadoftrackingeachandindividualparticleand In Euler–Lagrange model, the gas phase is treated as a con-
hencecanbeusedformodelinglargescalefluidizedbedgasifier. tinuumandtime-averagedNavier–Stoke equationsaresolvedfor
But,duetotheapproximationofparticleflowsasfluid,successof thegasphase,whilethesolidphaseissolvedbytrackingeachand
the Euler–Euler model depends on the proper description of individual particle in Lagrangian frame of reference. The solid
particle viscosity and pressure. Besides, to simulate particle size phaseexchangemass,momentumandenergywiththegasphase.
distribution, more than one pseudo-fluid has to be included and InEuler–Lagrangemodel,forparticledescription,discreteelement
all conservation equations are needed to be solved for each model(DEM)/discreteparticlemodel(DPM)iscommonlyapplied.
pseudofluid which represents one particle size. Therefore, gener- InDEM/DPMmodel,thecollisionbetweenparticlesmaybeeither
allyEuler–Eulermodelingisperformedforoneortwoparticlesize basedonsoft-sphereapproachorhard-sphereapproach.
notforawiderangeofparticlesizedistribution.TheEuler–Euler In a hard-sphere approach, the trajectories of the particles are
model cannot provide information about the residence time of determinedbymomentum-conservingbinarycollisions.Theinterac-
individual reacting particles. Another drawback of Euler–Euler tions between particles are assumed to be pair-wise additive and
model is that, the particle degradation and shrinkage during instantaneous.Inthesimulation,thecollisionsareprocessedoneby

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 703
Fig.11. Comparisonbetweenpredictedandexperimentaloutletgascompositionfordifferentcases[84].
Fig.12. Volumefractiondistributionwithinthebedfor(A)gases,(B)limestoneand(C)char[90].

704 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
Table7
Comparisonofmodelresultswithinertlimestoneandcalcinatinglimestoneandexperimentalresult[91].
CO CO2 H2 CH4 N2 H2O Tar
Model1
Inertlimestone 0.13464 0.09150 0.06226 0.00020 0.54675 0.16428 0.00037
Limestonecalcinations 0.13249 0.09279 0.06094 0.00020 0.54671 0.16649 0.00037
Difference 0.00214 0.00130 0.00132 0.00000 0.00003 0.00220 0.00000
(cid:3) (cid:3) (cid:3)
Model2
Inertllimestone 0.10135 0.09742 0.05230 0.00014 0.52268 0.22584 0.00026
Limestonecalcinations 0.10268 0.09818 0.05422 0.00014 0.52379 0.22073 0.00026
Difference 0.00132 0.00076 0.00192 0.00000 0.00111 0.00511 0.00000
(cid:3)
Experiment
Exp.1 0.1094 0.1931 0.0853 0.0084 0.6037 N/A N/A
Exp.2 0.1059 0.1838 0.0884 0.0107 0.6110 N/A N/A
one according to the order in which the events occur. For not too applied to gas-fluidized beds by Tsuji et al. [119], where the linear
dense systems, the hard-sphere models are considerably faster than spring/dashpot model similar to the one presented by Cundall and
thesoft-spheremodels.Occurrenceofmultiplecollisionsatthesame Strack [115] was employed. Kawaguchi et al. [120] extended this
instant cannot be taken into account in hard sphere model [93]. model to three dimensions as far as the motion of the particles is
CampbellandBrennen[94]reportedthefirsthard-spheresimulation concerned.Yuandco-workers[121–123]independentlydevelopeda
used to studygranular systems. Since then, the hard-sphere models two-dimensional model of a gas-fluidized bed. However, in their
are applied to study a wide range of complex granular systems. simulationsacollisiondetectionalgorithmthatisnormallyfoundin
Hoomansetal.[95]usedthehard-spheremodelincombinationwith hard-sphere simulations was used to determine the first instant of
a CFD approach for the gas-phase conservation equations to study contactprecisely.FengandYu[124]andFengetal.[125]appliedthis
gas–solid two fluidized beds. By using this model, they studied the modeltostudysegregationprocessesofabinarymixture.Iwadateand
effect of particle–particle interaction on bubble formation and the Horio[126]andMikamietal.[127]developedamodelbasedonTsuji
particle segregation induced by particle size differences and density etal.[119]wheretheyincorporatedVanderWaalsforcestosimulate
differences [96]. This model has been further used to study high- fluidizationofcohesiveparticles.Furtherstudiesoftheinfluenceofgas
pressure fluidization [97,98], circulating fluidized [99], spout-fluid andparticlepropertiesforGeldartAparticleswereperformedbyYe
beds[100,101]andparticleflowsthroughcontractions[102].Similar etal.[128,129]andPanditetal.[130].Kafuietal.[131]developeda
simulations are also carried outby manyother research groups. For DPMbasedonthetheoryofcontactmechanics,therebyenablingthe
example, Dahl et al. [103] and Dahl and Hrenya [104,105] applied a collisionof theparticlestobedirectlyspecifiedintermsof material
hard-sphere model tostudysegregationincontinuous size distribu- properties such as friction, elasticity, elastoplasticity and auto-
tions.OuyangandLi[106,107]developedaslightlydifferentversionof adhesion.Limtrakuletal.[132]usedthesoft-spheremodelwithmass
thismodel.Hellandetal.[108]developedaDPMinwhichhard-sphere transferandchemicalreactionstostudythedecompositionofozone
collisionsareassumed,butatime-drivenschemeisusedtolocatethe on catalyst coated particles in a two-dimensional fluidized bed.
collisionalparticlepair.Effectofthegasturbulencehasalsobeentaken Kuwagietal.[133]coupledthesoft-sphere modelwithamodelfor
intoaccountinsomehard-spheremodels[109–114].Athighparticle thedescriptionofmetallicsolidbridgingbysurfacediffusionmechan-
numberdensitiesorlowcoefficientofnormalrestitution,thecollision ismsincludingtheeffectofsurfaceroughness.Oevermannetal.[134]
willleadtoadramaticaldecreaseinkineticenergy.Thisisthesocalled studiedEuler–Lagrange/DEMsimulationusingsoft-spheremethodto
inelasticcollapse,inwhichregimethecollisionfrequenciesdivergeas study wood gasification in bubbling fluidized bed. The soft-sphere
relative velocities vanish. In that case, the hard sphere method DEM model combining with CFD was also used in the literature
becomes useless. In more complex situations, the particles may [135,136] to study the heat transfer in bubbling fluidized beds.
interact via short or long-range forces and the trajectories are Recently, In the following section, only soft-sphere DEM/DPM is
determined by integrating Newtonian equation motion. The soft- discussed because it can in principle handle any situation (dense
spheremethodoriginallydevelopedbyCundallandStrack[115]was regimes, multiple contacts) and also additional interaction force.
the first granular dynamics simulation technique published in the Mathematical equations used for describing the soft-sphere DEM/
openliterature.Soft-spheremodelsuseafixedtimestepandconse- DPMaregivenbelow.
quentlytheparticlesareallowedtooverlapslightly.Thecontactforces Foreachparticle,thelinearmomentumequationsisgivenby
are subsequently calculated from the deformation history of the
contact using a contact force scheme. The soft-sphere models allow m dv i m d2r i F F F 57
formultipleparticleoverlapalthoughthenetcontactforceisobtained idt ¼ idt2 ¼ contact;iþ pp;iþ ext;i ð Þ
fromtheadditionofallpair-wiseinteractions.Thesoft-spheremodels
wheretheRHSisthetotalforceonparticle,whichhasthreebasic
are essentially time driven, where the time step should be carefully
contributions:
choseninthecalculationofthecontactforces.Thesoft-spheremodels
that can be found in literature mainly differ from each other with
(i) ThetotalcontactforceF ,whichisthesumofindividual
respecttothecontactforceschemethatisused.Areviewofvarious contact;i
contact forces exerted byall other particles being in contact
popularschemesforrepulsiveinter-particleforceswaspresentedby
with the particle i, which are divided into a normal and a
Schaferetal.[116].WaltonandBraun[117]developedaforcemodel
tangentialcomponent:
which uses two different spring constants to model the energy
dissipation in the normal and tangential directions respectively. In F contact;i¼ F contact;N;iþ F contact;T;i ð 58 Þ
the force scheme proposed by Langston et al. [118], a continuous
potential of an exponential form was used, which contains two (ii) ThetotalexternalforceF :
ext;i
unknownparameters:thestiffnessoftheinteractionandaninterac-
tion constant. A two-dimensional soft-sphere approach was first F ext;i¼ F g;iþ F d;iþ F p;i ð 59 Þ

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 705
where F is the gravitational force, F is the drag force conditions but did not take particle collisions into account.
g;i d;i
exertedbythesurroundinggasphaseandF isthepressure Recently, Bruchmuller et al. [141] studied the thermochemical
p;i
force. degradationofbiomassinsidealab-scale(38.1mmdiameterand
(iii) The sum of all other particle–particle forces F , which can 460mm height) fast pyrolysis fluidized bed reactor by using
pp;a
include short range cohesive force form the van der Walls Euler–LagrangeDEM/DPM.Theyhavetacked0.8millionindividual
interaction between the molecules, as well as long range discretesandandbiomassparticles.Thismadeitpossibletolook
electrostaticforces. ataccurateanddetailedmulti-scaleinformation(i.e.,anydesired
Theangularmomentumequationofparticleisgivenby particle property, trajectory, and particle interaction) over the
entire particle life time which revealed that the overall thermo-
dω
I i dt i ¼ T i ð 60 Þ chemical degradationprocess of biomass was influencedbylocal
flowandparticleproperties.Multiprocessorsimulationwithhigh-
where I is the moment of inertia of particle i and T is the
i i endcomputer(2.3GHz,192coresintotaldistributedon48quad
torque which depends only on the tangential component of
cores) was carried out which took 320,000 CPU hours to run 5s
theindividualcontactforces.
realtime.
The Euler–Lagrange DEM/DPM is the most comprehensive
Theheatbalanceforindividualparticleisgivenby model developed till date to study the fluidized bed system.
dT Because,ithasthehighestpotentialtorealisticallyrevealthermo-
m i C p;idt i ¼ Q gpþ Q ppþ Q radþ Q R ð 61 Þ chemical processes in granular multiphase flow applications.
DEM/DPMmodelsareabletoaccuratelypredictinterparticleand
where Q is the gas–solid convection heat transfer, Q is the
gp pp interphase exchange of mass, momentum and energy at the
particle–particle conduction heat transfer, Q is the radiation
rad individual particle level without any approximation. Therefore,
heat transfer and Q is the heat transfer due to heterogeneous
R trajectories, temperature, composition and any other additional
chemicalreactions.
particleinformationaremorereliablyandmorenaturallyincluded
Thegas-phasemassandmomentumequationsareasfollows:
whichareessentialtostudyeffectslikethermochemicaldegrada-
∂ tion, shrinkage, breakage, segregation, mixing and entrainment.
∂tð
α
g
ρ
gÞþ
∇U
ð
α
g
ρ g!v
gÞ¼
S
g ð
62
Þ But,the computational time andcost involved in Euler–Lagrange
DEM/DPM simulation, restricting the applicability of the model
∂
∂tð
α
g
ρ g!v
gÞþ
∇U
ð
α
g
ρ g!v g!v
gÞ¼(cid:3)
α g∇p
gþ
∇U
ð
α
g
τ
gÞþ
α
g
ρ g!g
þ
S
p
particularlyforsimulatinglarge-scalefluidizedbedreactorwhich
involves more particles and reaction kinetic. Besides, due to its
63
ð Þ complexity, Euler–Lagrange DEM/DPM simulations are mostly
whereαisthevolumefraction,ρisthedensity,!v isthevelocity performedin2-Dorquasi-3-D.
vector of gas phase. S g is the mass source term due to chemical Very recently, Euler–Lagrange Computational Particle Fluid
reactions.τ g istheviscousstresstensorandS p isthemomentum Dynamics(CPFD)modelisemployedforcalculatingdenseparticle
source due to inter-phase interaction. For gas–solid phase in flow. The CPFD numerical methodology incorporates the multi-
fluidized bed, two-way coupling is required. The S
p
is computed phase-particle-in-cell(MP-PIC)method[142,143],wherethefluid
by adding up the drag force of the particles located in fluid cell phase is solved by using an Eulerian computational grid and the
whichisgivenby solidsaremodeledusingLagrangiancomputationalparticles.Here
a computational or numerical particle is accounted for via an
1 Np
S p¼V ∑ F d ð 64 Þ ensemble of particles displaying the same properties such as
celli 1 chemical composition, size and density. Hence, the number of
¼
whereV isthevolumeofthefluidcell. particlesneededtosolvecanbereducedfrombillionstomillions
cell
Thegas-phaseenergyequationisgivenby and this model can be applied to simulate lean as well as dense
particle phase flow. Therefore, this model is in between Euler–
∂
∂
tð
α
g
ρ
g
C
pg
T
gÞþ
∇U
ð
α
g
ρ g!v
g
C
pg
T
Þ¼
∇U
ð
α
g
k g∇T
gÞþ
S
Q;CVþ
S
Q;Rþ
S
h
E
an
u
d
ler
O
t
'
w
Ro
o
u
-fl
rk
u
e
id
[
m
14
o
2
d
]
el
fi
a
rs
n
t
d
p
E
r
u
o
l
p
e
o
r–
se
L
d
agr
t
a
h
n
e
ge
M
D
P
E
-
M
PIC
/DP
m
M
e
.
th
A
o
n
d
dre
a
w
nd
s
65
ð Þ demonstrated the method with one-dimensional simulations
where T is the temperature, C is the heat capacity, k is the compared to analytical solutions and experimental data. In CPFD
g pg g
thermalconductivityofthegasphase.S istheheatsourcedue three-dimensional forces on each particle is considered which
Q;CV
togas–solidconvectiveheattransfer,S istheheatsourcedueto include fluid drag, gravity, static–dynamic friction, particle colli-
Q;R
chemical reactions and S is the heat transported by the mass sion and possibly other forces. Using this method, the particle
h
sourceS . stress gradient, which is difficult to calculate for each particle in
g
Euler–Lagrange DEM/DPM allows solution for flows with a denseflow,iscalculatedasagradienttothegrid,fullycoupledto
widerangeofparticletypes,sizes,shapesandvelocities.Itisable the other particle and gas acceleration terms and is then inter-
tolookatindividualdiscreteparticlesandtheirinteractionwithits polated to the discrete particles [144]. In CPFD, cell averaged
localenvironment.But,duetohighcollisionfrequencyforvolume chemistry is used to calculate the reaction kinetics. Average
fractionsabove5%andthecomputationalcomplexityofcalculat- properties for the particle phase in the chemical rate equations
ing dense particle–particle interactions, DPM calculations have are calculated by interpolating discrete computational particle
beenlimitedtoonthesystemhavingcomparativelylessnumbers properties to the grid. The reaction rates are calculated in each
ofparticles[137].Generally,Euler–LagrangeDEM/DPMisusedto grid cell by solving a set of ordinary differential equation. The
study the combustion and gasification of fuel in freeboard area mathematical equations used for describing the fluid and solid
wheretheparticlevolumefractionisless.Therehasbeenlimited phaseinCPFDmethodaregivenbelow.
study on the simulation of dense gas–solid flow coupling with The volume averagedfluid phase massand momentum equa-
chemicalreactionsbyusingEuler–LagrangeDEM/DPM.Silaenand tionsaregivenby
Wang [138] and Watanabe and Otaka [139] applied Euler–
[
L
1
a
4
g
0
ra
]
n
u
g
s
e
ed
DE
E
M
ul
/
e
D
r–
P
L
M
ag
i
r
n
an
e
g
n
e
tr
D
ai
E
n
M
ed
/D
fl
P
o
M
w
a
c
t
oa
c
l
ir
g
c
a
u
s
la
ifi
ti
e
n
r
g
.G
fl
r
u
ä
i
b
d
n
iz
e
e
r
d
et
be
a
d
l.
∂
∂
tð
α
f
ρ
fÞþ
∇U
ð
α
f
ρ f!v
fÞ¼
ρ_C
fs ð
66
Þ

706 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
∂ where,Ristheuniversalgasconstant,T isgasmixturetempera-
∂tð
α
f
ρ f!v
fÞþ
∇U
ð
α
f
ρ f!v f!v
fÞ¼(cid:3)
∇p
(cid:3)
F
þ
α
f
ρ
f
g
þ
∇Uα
f
τ
f ð
67
Þ tureandM isthemolecularweightofg
f
asspeciesi.
i
where v is the fluid velocityand α is the fluid volume fraction, The dynamics of particle phase is calculated by solving a
f f
ρ isthefluiddensity,pisthefluidpressure,τ isthefluidstress transport equation for the particle distribution function (PDF) f.
f f
Itisassumedthatfisafunctionofparticlespatiallocation,particle
tensor and g is the gravitational acceleration. F is the rate of
momentumexchangeperunitvolumebetweenthefluidandthe velocity, particle mass, particle temperature and time. The trans-
solidphase.Thefluidmassproductionrateperunitvolumefrom portequationforf,whichisderivedfromBoltzmann-BKGapprox-
solid–fluidchemistryisρ_C. imationmodelofgasdynamics[146],isgivenby
fs
Theconstitutiveequationforthefluidstressτ f isgivenby ∂f ∂ fv ∂ fA f d(cid:3) f 76
∂tþ∂xð Þþ∂vð Þ¼ τ ð Þ
τ μ
∂v
i
∂v
j
2
μδ
∂v
i 68
d
f;ij¼ (cid:2) ∂x jþ∂x i(cid:3) (cid:3)3 ij∂x j ð Þ whereAistheparticleacceleration,f d isthePDFforthelocalmass
averaged particle velocity, and τ is the collision damping time.
where μ is the coefficient of viscosity which depends on the d
TheparticleaccelerationAisgivenby
thermodynamic state of the fluid for laminar flow and have an
a
tu
d
r
d
b
e
u
d
le
e
n
d
ce
dy
m
v
o
i
d
sc
e
o
l
s
[
i
1
t
4
y
5
f
]
o
.
r turbulent flow based on Smagorinsky A
¼
d
d
!v
t
s
¼
θ
ð
!v
f(cid:3)
!v
sÞ(cid:3)ρ
1
s
∇p
þ
g
(cid:3)α s
1
ρ s
∇τ
s ð
77
Þ
Theturbulenceviscosityisgivenby
wherev isthesolidvelocity,ρ isthesoliddensity,α isthesolid
s s s
volume fraction, τ is the solid normal stress and θ is the
μ C2ρ Δ2
∂v
i
∂v
j
2
69 momentumtransfer
s
coefficient.
t¼ f sffi
(cid:2)
ffiffiffi∂ffiffixffiffiffijffiþffiffiffiffiffi∂ffiffixffiffiiffiffi
(cid:3)
ffiffiffiffiffi ð Þ
Theequationforsolidmovementisgivenby
where C is the subgrid scale eddy coefficient and Δ is the
lengthscale.
d
d
!x
t s ¼ !v s ð 78 Þ
Thefluidphasespeciesequationisgivenby
Theenergyequationforsolidisgivenby
∂
∂tð α f ρ f Y f;iÞþ ∇U ð α f ρ f Y f;i!v fÞ¼ ∇U ð ρ f α f D∇Y f;iÞþ δm i;chem ð 70 Þ C dT s 1 k f Nu f;pA T T 79
vdt ¼m s 2r s sð f(cid:3) sÞ ð Þ
whereY isthemassfractionofeachfluidspeciesandδm is
the net p f;i roduction rate of species i due to fluid phase ch i e ;c m hem ical whereC v is the specific heatof the solid material, T s is the solid
reactions. The coefficient D represents the turbulent mass diffu- temperature, Nu f;p is the Nusselt number of heat transfer in the
fluidtotheparticle.
sivity which is related to the viscosity by the Schmidt number
Theparticlevolumefractionα isdefinedas
(μ=ρ D Sc). s
give
T
n
f he
a
¼
s
fluid phase energy equation in terms of the enthalpy is α
s¼ ZZZ
f m
ρ s
sdm
s
d!v
s
dT
s ð
80
Þ
∂
∂
tð
α
f
ρ
f
h
fÞþ
∇U
ð
α
f
ρ
f
h f!v
fÞ¼
α
f
∂
∂
p
tþ
!v
f
U∇p
þ
Φ
þ
Q_
þ
S
hþ
q_
Dþ
∇U
ð
α
f
k f∇T
fÞ
F
fr
r
a
o
c
m
tio
c
n
o
s
ns
e
e
q
r
u
v
a
a
l
t
s
io
u
n
n
o
it
f
y
v
.
olume,thesumoffluidandparticlevolume
(cid:2) (cid:3)
ð
71
Þ
α
fþ
α
s¼
1:
ð
81
Þ
whereh f isthefluidphaseenthalpy,T f isthefluidtemperature,Φ The fluid momentum equation implicitlycouples fluid and parti-
_
istheviscousdissipation,Q istheenergysourcepervolume,S h is clesthroughtheinter-phasemomentumtransfer.Theinter-phase
theenergyexchangefromthesolidfacetothefluidphase,andq_
D momentumtransferatisgivenby
is the enthalpy diffusion. The thermal conductivity k is the
molecular conductivity plus eddy conductivity. For the e f nthalpy, F
¼(cid:3)
f m
s
θ
ð
!v
f(cid:3)
!v
sÞ(cid:3)
∇
ρ
p
þ
!v
s
d
d
m
t
s dm
s
d!v
s
dT
s ð
82
Þ
ideal gas approximation is used, wherethe enthalpy depends on ZZZ (cid:5) (cid:12) s(cid:13) (cid:6)
temperatureandtheenthalpyforfluidspeciesiisgivenby Theheattransferfromthesolidphasetothegasphaseisgivenby
h i¼ ZTr T ef C pi dt þ Δh f;i ð 72 Þ Sh¼(cid:3) ZZZ f (cid:5) ms (cid:12) θ ð !vf(cid:3) !vsÞ 2 (cid:3) Cv d d T t s (cid:13) (cid:3) d d m t s (cid:12) hsþ 1 2ð !vf(cid:3) !vsÞ 2 (cid:13)(cid:6) dmsd!vsd 8 T 3 s
ð Þ
whereC is the specific heat at constant pressure and Δh is the
p f whereh istheparticleenthalpy.
heat of formation of the species. The total fluid enthalpy is the s
massfractionweightedsumofthefluidspeciesenthalpies.
Prandtlnumbercorrelationisgivenby 5. Numericalsolution
C μ
Pr p t 73 In CPFD, the conservation equations are integrated over a
t¼ k t ð Þ control volume. The mixture fluid density, velocity and pressure
Theenthalpydiffusiontermisgivenby are coupled by semi-implicit pressure equation derived from the
gasmassconservationequationwhichisapplicabletoanarbitrary
q_ D¼ ∑
Ns
∇U ð h i α f ρ f DY f;iÞ ð 74 Þ Mach number. The fluid momentum, energy and pressure equa-
i 1 tionsaresolvedwithaconjugatedgradientsolver.Thechemistry
¼
Themixturepropertiesarebasedonthemassfractionofeachgas. of differential equations are calculated using a stiff, sparse ODE
The gas phase pressure, temperature and density are related solver.
throughidealgasequation.Foranidealgas,thepressureisgiven In the MP-PIC scheme, solids properties are mapped to and
bytheequationofstateas from the Eulerian grid to get grid properties for the solids. Fluid
properties,areinturn,mappedtodiscreteparticlelocations.The
N Y
p ρ RT ∑ f;i 75 interpolationoperatoristheproductofinterpolationoperatorsin
¼ f f i M i ð Þ thethreeorthogonaldirections.Foraparticlelocatedatx s ,where

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 707
Fig.13. Gasifierparametersatdifferentaxiallevelsinthereactor[149].
x
s¼ð
x s;y
s
;z
sÞ
, the x-directional component of the interpolation The y and z interpolation operators have a similar form. The
operator to grid cell i, is an even function, independent of the y particlevolumefractionatcellξfrommappingparticlevolumeto
andzcoordinates,andhastheproperties. thegridis
Sx ξð x sÞ¼( 1 0 ; ; x x ξ s (cid:3) ¼ 1 x Z ξ x s Zx ξ þ 1; ð 84 Þ α sξ¼V 1 ξ ∑ N k sm ρ sξ s k kn sk S sξk ð 85 Þ

708 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
Solid volume
fraction
0.0 s 0.5 s 1.0 s 1.5 s 2.0 s 2.5 s
Solid volume
fraction
0.0 s 0.5 s 1.0 s 1.5 s 2.0 s 2.5 s
Fig.14. (A)Discretesolidscoloredbyvolumefractionmappedfromthegridtoparticlelocationsand(B)solidsfieldcoloredbyvolumefraction[152].
where V is the grid volume, n is the number of particles in a Theparticlenormalstressisanapproximationofcollectiveeffects
ξ s
numerical particle each containing a cloud of particles with of neighbor particles on a particle. The particle stress is derived
identical particle velocity u, mass m, temperature T located at from particle volume fraction which is in turn calculated from
s s s
positionx andthesummationisoverallnumericalparticlesN . particle volume mapped to the grid. The particle normal stress
s s
Theinter-phasedragcoefficientisgivenby modelusedhereisfromHarrisandCrighton[147]asgivenbelow:
θ ¼ C d 3 8 ρ ρ f s(cid:7) v f r (cid:3) s v s (cid:7) α f(cid:3) 2:65 ð 86 Þ τ s¼max ½ð α CP(cid:3) P s α α s ζ s Þ ; ε ð 1 (cid:3) α sÞ(cid:5) ð 90 Þ
(cid:7) (cid:7)
where C d is the drag coefficient. The correlation for C d based on whereP s isapositiveconstantthathastheunitofpressure,α CP is
WenandYu[77]isgivenby the solid volume fraction at close packing limit, ε is a small
number on the order of 10(cid:3) 7 to remove the singularity and the
241 0:15Re0:687 ; Reo1000 constantζ isrecommendedas2rζr5.
C Reð þ Þ 87
d¼(0:44; ReZ1000 ð Þ The detailed equations and solution algorithm for Euler–
LagrangeCPFDmodelcanbefoundintheliterature[143].
and SniderandBanerjee[148]appliedCPFDnumericaltosimulate
2ρ v v r
theozonedecompositioninabubblingfluidizedbed.Simulations
Re f f(cid:3) s s 88 were run for the full three-dimensional bubbling bed of 0.229m
¼ μ ð Þ
(cid:7) (cid:7) f (cid:7) (cid:7) diameterand2mheight.Theozonedecompositionwasdescribed
wherer istheparticleradiusasgivenbelow. by a single stoichiometric equation with first order reaction rate
s
and isothermal simulation was run. The simulated ozone mass
r 3V s 1=3 89 fraction as function of inlet velocity was compared with the
s¼ 4π ð Þ analytical solution as well as the experimental result and agreed
(cid:2) (cid:3)

well with the both. Snider et al. [149] extended the Eulerian– wasinitiallyfilledwith47,000kgofsolids.Thesolidwasmodeled
Lagrangian CPFD methodology to include the heat transfer and as pure carbon with a particle size distribution. The gasification
chemistry with solid material pyrolysis. The model was used to chemistry was described with five homogeneous and heteroge-
simulate a large three-dimensional fluidized bed coal gasifier neouschemicalreactions.Thegas–solid chemistryconsumedthe
(4.57m diameter and 13.7m height) with internal cyclones, solidsandsolidshrinkfromchemistry.Thesimulationwasrunfor
internal heaters and as sparger to illustrate the complexity of 300s which took 6 days computational time on a single Intels
problem which can be solved by the CPFD method. The gasifier Core™ i7 computer. The results from the simulation provided
50
40
30
20
10
0
)%(
noitcarf
eloM
Simulation 50
Experiment
40
30
20
10
0
H CO CO CH N H CO CO CH N
2 2 4 2 2 2 4 2
)%(
noitcarf
eloM
Simulation
Experiment
50
40
30
20
10
0
)%(
noitcarf
eloM
60
Simulation 50
Experiment
40
30
20
10
0
H CO CO CH N H CO CO CH N
2 2 4 2 2 2 4 2
)%(
noitcarf
eloM
Simulation
Experiment
50
40
30
20
10
0
)%(
noitcarf
eloM
60
Simulation 50
Experiment
40
30
20
10
0
H CO CO CH N H CO CO CH N
2 2 4 2 2 2 4 2
)%(
noitcarf
eloM
C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 709
Simulation
Experiment
Fig.15. Comparisonbetweensimulatedandexperimentaldrygascompositions:(A)T 8001C,ER 0.35,S/B 0.5;(B)T 8501C,ER 0.35,S/B 0.5;(C)T 8001C,ER 0.35,
S/B 0.8;(D)T 8001C,ER 0.35,S/B 0.2;(E)T 8001C,ER 0.3,S/B 0.5;and(F)T ¼ 8001C,ER ¼ 0.4,S/B ¼ 0.5[152] ¼ . ¼ ¼ ¼ ¼
¼ ¼ ¼ ¼ ¼ ¼ ¼ ¼ ¼ ¼

710 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
insightintothegasifierasdiscussedbelow.Fig.13showsthatthe rates and consumption of carbon mass. Fig.16 shows the cumu-
gas–solid flow had regions of high and low volume fraction and lativenetconsumptionofcarbonmasswithtime.Itwasdescribed
largevoidstructures(bubbles)intothebed.Thebedsurprisingly that the cumulative consumption of carbon particle mass over
hasauniformtemperatureexceptatthefeed-spargerarmswhere 32.5s was about 0.0098kg/s, which resulted in the average
high sensible heat was generated from combustion. There were changeof0.268mmforsolidparticleradius.Thesimulatedoutlet
variations in gas species radially and axially in the bed such as gas composition also showed good agreement with the experi-
pockets of H above the sparger-distribution-pipe. Abbasi et al. mentwithminimumrelativeerroroflessthan3%,themaximum
2
[150] simulated the feeding section of a fast fluidized bed coal relative error of about 30% and the average relative error of less
gasifier by using CPFD methodology. The solid particles are than15%.
assumedtoremainunchangedinsizeandthesamesizedistribu- TheabovestudiesshowedthattheEuler–LagrangeCPFDmodel
tionwastakenforcarbonandashparticles.Distributionofparticle cansimulatethefluidizedbedgasificationprocessinlab-scaleas
velocities, particle volume fraction, gas compositions and tem- well as commercial-scale three dimensional gasifier geometry
peraturewereobtained.Theearlysingofchockinginthefeeding with reasonably less simulation time compared to the Euler–
sectionwaspredictedfromthesimulatedparticlevolumefraction Lagrange DEM/DPM model and also by keeping the Lagrangian
distribution. To compare the CPFD results, a simplified approach, description of particles but with the assumption of multiple
the plug flow reactor (PFR) model was simulated with the same particles in a cell. It can provide many details inside the gasifier
operatingconditions.Itwasfoundthatthetimeandcross-section likeparticleshrinkageduetoreaction,residencetimeofparticles,
averagevalue of temperature andgascompositions simulatedby particlesizedistribution,particleattrition,particleagglomeration
CPFDcloselyapproximatedtheoneforPFR.TheCPFDmodelwas etc. which cannot be obtained by Euler–Euler model. It also
also used to study the biomass gasification in three-dimensional provides the three dimensional gas–solid flow structure, gas
lab-scale fluidized bed gasifier [151,152] by considering different composition distribution, temperature distribution, reaction rate
particle size for sand and biomass particles. The gas–solid flow distribution etc. But, the Euler–Lagrange CPFD model cannot
pattern, gas composition distribution, parametricvariation ofgas provide the information about each and individual particle but
composition etc. were investigated in details. The bubble forma- can provide the information about each numerical particle (i.e.
tion, development and eruptionwith time was well captured by group of particles having similar property) and hence, it is a
complexthreedimensionalflowstructuresrevealedbythesimu- tradeoffbetweentheaccuracyandthecomputationalcost.Differ-
lation as shown in Fig. 14 [152] whereas only the growth was entmodelsusedtosimulatethefluidizedbedgasificationprocess
observedbutcoalescenceanderuptionwasnotidentifiedbecause aresummarizedinTable8.
of high velocity [151]. It was also observed that the overall
dynamics of the bed was strongly influenced by the biomass
injection through the side port where the instantaneous devola- 6. Conclusion
tization of biomass was assumed. The mode also captured the
inherentunsteadynatureofthefluidizedbed.Thecomparisonof An updated survey of published mathematical models for
simulatedoutletgascompositionwithexperimentaldatashowed fluidizedbedgasificationprocessispresented.Thepresentpaper
reasonable good agreement (Fig. 15). Nevertheless, the CPFD describesdifferentmodelingapproachesstartingfromthesimple
simulation slightly over-predicts H , CO and CH generation and modelslikeequilibriummodel,two-phaseflowmodeltothevery
2 4
under-predicts CO .Itwasconcluded thatthelittlediscrepancies complexEuler–EulermodelandEuler–Lagrangemodels.Thebasic
2
between experimental and simulated gas compositions may be principle of modeling is discussed in details. Different modeling
duetotheselectionofkineticparametersbasedonliterature.Xie approachesusedbydifferentresearchersarereviewedandmajor
et al. [153] also simulated the same lab-scale bubbling fluidized results obtained by them are also discussed. The following con-
bedcoalgasifierbyusingEuler–LagrangeCPFDmodelwhichwas clusionsmaybedrawnfromthepresentreview.
earlier simulated by using Euler–Euler model [89,91]. In the Theequilibriummodeliscomputationallyinexpensive.Itdoes
presentmodel,aparticlesizedistributionwasconsideredinstead notdependonthegasifiertype.But,itprovidesaquickideaabout
ofameanparticlediameter.Themodelconsideredthesolidmass thelimitingbehaviorofagasificationsystemandhenceitisuseful
consumedorproducedinreactionschangedthesize ofparticles. forpreliminarydesignofthegasifier.Itisobservedthattheresults
Themodelpredictedthegas–solidflowpattern,distributionofgas from the equilibrium model can be improved by modifying it
composition,heterogeneousandhomogeneouschemicalreaction kinetically. While, in kinetic model detailed gasification reaction
kinetic is considered with respective rate of reactions. Kinetic
modelsalsoconsiderthehydrodynamicsofthebed.Dependingon
the hydrodynamic consideration, the gasification model may be
classifiedasthetwo-phaseflowmodel,theEuler–Eulermodeland
the Euler–Lagrange model. The two-phase flow modeling is the
simplestamongsttheratebasedorkineticmodelbecauseitdoes
notsolveanymomentumequationforgasorsolid.Itconsidersthe
hydrodynamics of the fluidized bed gasifier which is based on
empirical correlations. In Euler–Euler model, both gas and solid
aretreatedasinterpenetratingcontinuumandseparategoverning
equationsaresolvedforeachphase.Couplingisachievedthrough
the inter-phase transfer coefficients. It is computationally less
expensive compared to the Euler–Lagrange model and also pro-
vides reasonably good details about the fluidized bed gasifier.
Euler–Lagrange model provides the maximum number of details
but computationally more expensive when compute individual
particle dynamics (DEM/DPM). Whereas, the Computational Par-
ticle Fluid Dynamics (CPFD) model, is a modified Euler–Lagrange
Q
Fi
a
g
¼
.
2
1
8
6
.
.
4
C
k
u
g
m
/h
u
,
l
Q
a
s
t
¼
iv
4
e
.6
c
k
o
g
n
/
s
h
um
[1
p
5
t
3
i
]
o
)
n
.
of carbon mass versus time (Qc¼ 8.0kg/h,
modelwhichassumesanumericalparticlebycombiningparticles

Table8
Differentmodelsforsimulatingthefluidizedbedgasificationprocess.
Authors Year Modeltype Keyfeatures Application Output
Lohaetal.[6] 2011 Equilibriummodel Stoichiometric,consideredonlygaseousspecies,modified BFB,lab-scale,biomassgasification,steam Parametricvariationofgascomposition,correlationforproductgas.
equilibriumconstants. asgasifyingagent.
Lohaetal.[7] 2011 Equilibriummodel Stoichiometric,consideredgaseousandsolidspecies. BFB,lab-scale,biomassgasification,steam Firstlawandsecondlawefficiencies,HHV,externalenergyinput,
asgasifyingagent. CBP.
Lietal.[10] 2001 Equilibriummodel Non-stoichiometric,RANDalgorithm,consideredgaseous CFB,lab-scale,coalgasification,airas Parametricvariationofgascomposition,HHV,carbonconversion,
andsolidspecies,modifiedwithexperimentalcarbon gasifyingagent. carbonformationboundary,roleofmoisture
conversion.
Lietal.[11] 2004 Equilibriummodel Non-stoichiometric,RANDalgorithm,consideredgaseous CFB,lab-scale,coalgasification,airas Parametricvariationofgascomposition,gasyield,HHV,coldgas
andsolidspecies,modifiedwithexperimentalcarbon gasifyingagent. efficiency,carbonformationboundary.
conversionandmethaneformation.
PetersenandWerther 2004 Equilibriummodel Stoichiometric,consideredonlygaseousspecies. CFB,pilot-scale,sewagesludge Parametricvariationofgascomposition.
[22] gasification,airasgasifyingagent.
Srinivasetal.[23] 2009 Equilibriummodel Stoichiometric,consideredonlygaseousspecies. CFB,pressurizedcondition,biomass Parametricvariationofgascomposition,heatingvalue,exergy,
gasification,air-steamasgasifyingagent. efficiency.
Frydaetal.[24] 2008 Equilibriummodel Non-stoichiometric,fixedamountofun-reactedcharand FB,lab-scale,biomassgasification,steam Parametricvariationofgascomposition,efficiency,integratedwith
CH4andtarwereintroducedbasedonliterature. asgasifyingagent. SOFC
Schusteretal.[25] 2001 Equilibriummodel Non-stoichiometric,consideredgaseousandsolidspecies. Dualfluidizedbed,commercial-scale, Parametricvariationofgascomposition,heatingvalue,efficiency,
biomassgasification,steamasgasifying carbonformationboundary.
agent.
PetersenandWerther 2005 Two-phaseflow 1.5-D,unsteady-state CFB,pilot-scale,sewagesludge Axialgascompositionvariation,comparisonwithownexperimental
[22] model gasification,airasgasifyingagent data,modifiedthereactionkinetics.
PetersenandWerther 2005 Two-phaseflow 3-D,unsteady-state CFB,pilot-scale,sewagesludge Threedimensionalvariationofproductgas,unevendistribution
[37] model gasification,airasgasifyingagent. nearfeedingpoint,bettermixingwithbyincreasingnumberof
feedingpoint.
JiangandMorey[33] 1992 Two-phaseflow 1-D,steady-state,non-isothermal BFB,lab-scale,biomassgasification,airas Fuelfeedrate,gascomposition,heatingvalue,temperatureetc.
model gasifyingagent. modelagreedwellwithexperimentathighertemperaturebutfailed
atlowertemperature.
Chatterjeeetal.[40] 1995 Two-phaseflow 1-D,steady-state,non-isothermal BFB,lab-scale,coalgasification,steamand Variationofgascomposition,temperature,calorificvalueand
model airasgasifyingagent. carbonconversionwithoxygenfeedandsteamfeed.
Yanetal.[41] 1998 Two-phaseflow 1-D,steady-state,isothermal,net-flowconsideration BFB,coalgasification. Bedvoidage,reactionrateandgascompositionalongtheheight,
model carbonconversion,significantdeviationwithoutconsideringthe
net-flow.
Jennenetal.[42] 1999 Two-phaseflow 1-D,non-isothermal,unsteady-state CFB,pilot-plant,biomassgasification,air Axialgascompositionandtemperatureprofile.
model asgasifyingagent.
HamelandKrumm 2001 Two-phaseflow 1-D,steady-state,non-isothermal BFB,lab-scaletocommercial-scale. Overallcarbonconversion,freeboardtemperature,gascomposition.
[43] model Gasificationofbrowncoal,peatand
sawdust.Air,air/steamandO2/steamas
gasifyingagent.
FiaschiandMichelini 2001 Two-phaseflow 1-D,non-isothermal BFB,biomassgasification,airasgasifying Gascompositionandtemperaturevariationalongtheaxis,
[44] model agent. optimizationwithrespecttoER,pressure,bedheightandgas
velocity.
Sadakaetal.[45–47] 2002 Two-phaseflow 1-D,unsteady-state,non-isothermal DualdistributortypeFB,lab-scale, Gascomposition,bedtemperature,heatingvalue,gasproduction
model Biomassgasification,Air-steamas rate.
gasifyingagent.
Chejneand 2002 Two-phaseflow 1-D,steady-state,non-isothermal. BFB,lab-scalecoalgasification. Temperature,gascomposition,volumefraction,velocityandother
Hernandez[48] model fluiddynamicparameters.Stronginfluenceoffeedpointposition
wasobservedintheresult.
Rossetal.[49] 2005 Two-phaseflow 1-D,steady-state,non-isothermal. BFB,commercial-scaleandpilot-scale, Gascomposition,temperatureandreactionratealongtheheight,
model coalgasification,air-steamasgasifying overallcarbonconversion.
agent.
Radmaneshetal.[50] 2006 Two-phaseflow 1-D,steady-state,Isothermal BFB,biomassgasification.air-steamas GascompositionvariationwithT,ER,S/B,feedlocationandmass
model gasifyingagent transferbetweencountercurrentregion.
Kaushaletal.[51] 2010 Two-phaseflow 1-D,steady-state,non-isothermal BFB,biomassgasification Temperature,solidholdupsandgasconcentrationvariationalong
model thereactor’smajoraxis.
C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
711

Table8(continued)
Authors Year Modeltype Keyfeatures Application Output
Pengmeietal.[52] 2008 Two-phaseflow 1-D,steady-state,Isothermal FB,biomassgasification,air-steamas Gascomposition,gasyield
model gasifyingagent
Goyaletal.[53] 2010 Two-phaseflow 1-D,non-isothermal BFB,gasificationofcoalandpetcoke Effectofcompositionandlocationoffeedpointandashcontenton
model mixture theperformance,Increaseinpetcokecontenttendstolowerthe
efficiencyandcarbonconversionbutincreasestheamountofsyngas
produced,increaseinashcontentofcoaldecreasesthecarbon
conversion.
Gungor[54] 2011 Two-phaseflow 1-D,steady-state,isothermal FB,biomassgasification,air-steamas HydrogenproductionvariationwithT,ER,S/B,velocity
model gasifyingagent. andparticlesize.
Douetal.[84] 2008 Euler–Eulermodel 2-D,singlesolidphaseandsingleparticlesize,unsteady- BFB,lab-scale,steamreformingof Gas–solidflowpattern,glycerolconsumption,hydrogen
state,non-isothermal. glycerol. andothergasproduction.
DouandSong[85] 2010 Euler–Eulermodel 2-D,singlesolidphaseandsingleparticlesize,unsteady- BFB,lab-scale,steamreformingof Gas–solidflowpattern,glycerolconsumption,hydrogen
state,non-isothermal. glycerol. andothergasproduction,detailedanalysisofrelationship
betweenhydrodynamicsandhydrogenproduction.
Papadikisetal. 2008 Euler–Eulermodel 2-Dand3-D,Euleriandescriptionofgasandsandparticle, BFB,Lab-scale,Fastpyrolysis Gas–solidflowpatternwithbiomassparticleposition,gas
[86,87] &2009 Lagrangiandescriptionofsinglebiomassparticle. compositionandtemperaturedistribution,tarevolution
Xueetal.[88] 2012 Euler–Eulermodel 2-Dand3-Dsimulation,twosolidphasesforsandand BFB,lab-scale,biomassfastpyrolysis Influenceofoperatingconditionsontheconversionprocessand
biomass,unsteady-state,isothermal. productyield,modelover-predictedtheun-reactedbiomass
elutriationforsmallerparticles.
Yuetal.[89] 2007 Euler–Eulermodel 2-D,k–ϵturbulencemodelforgasphase,Singlesolidand BFB,lab-scale,coalgasification,air-steam Gas–solidflowpattern,gascompositiondistribution,reactionrate
singleparticlesize,unsteady-state,non-isothermal. asgasifyingagent. distribution.
Wangetal.[90] 2009 Euler–Eulermodel 3-D,k–ϵturbulencemodelforgasphase,Singlesolidphase BFB,lab-scale,coalgasification,air-steam Flowpattern,gasvelocity,particlevelocity,gascomposition
andsingleparticlesize,unsteady-state,non-isothermal. asgasifyingagent. distribution,reactionratedistribution.
Armstrongetal.[91] 2011 Euler–Eulermodel 2-D,separatesolidphaseforcoal,limestoneandchar.Single BFB,lab-scale,coalgasification,air-steam Gas–solidflowpattern,distributionofgascomposition,reactionrate
particlesizeforeachsolidphase,unsteady-state,non- asgasifyingagent. andtemperature.Impactoflimestonecalcinationsongaseous
isothermal. composition.
Armstrongetal.[92] 2011 Euler–Eulermodel 2-D,twodifferentdevolatilizationmodel,separatesolid BFB,lab-scale,coalgasification,air-steam Gas–solidflowpattern,gascompositionvariationwithbedmaterial
phaseforcoal,limestoneandchar.singleparticlesizefor asgasifyingagent. composition,bedheight,temperatureofbedandinclusionofheat
eachsolidphase,unsteady-state,non-isothermal.extended transfercoefficient.
simulationtime(400s).
SilaenandWang 2010 Euler–Lagrange 3-D,fourdifferentdevolatizationmodelsareemployed Entrainedflowgasifier,coalgasification, Gascomposition,temperature,efficiency,effectofdifferent
[138] DEM/DPM oxygenblown. devolatizationmodel.
WatanabeandOtaka 2006 Euler–Lagrange 2-D,2t/day Entrainedflowgasifier,coalgasification. Influenceoftheairratiooncarbonconversionefficiency,amountof
[139] DEM/DPM productchar,heatingvalue,andcoldgasefficiency,temperatureand
productgascompositiondistribution.
Gräbneretal.[140] 2007 Euler–Lagrange 4800t/day,highpressure(33bar). Winklergasifier,coalgasification,steam/ Flowpattern,turbulence,productgascomposition,temperatureand
DEM/DPM oxygenasgasifyingagent. radialheattransfer.
Bruchmulleretal 2012 Euler–Lagrange 3-D,0.8millionindividualsandandbiomassparticle. BFB,lab-scale,biomassfastpyrolysis. Gas–solidflowpattern,particledegradation,particleentrainment,
[141] DEM/DPM gascompositiondistribution.
SniderandBanerjee 2010 Euler–Lagrange 3-D,constantparticlesize,onlysinglereaction,unsteady- BFB,lab-scale,ozonedecomposition. Particlevolumefractiondistribution,ozonemassfraction
[148] CPFD state. distribution,variationwithvelocity.
Snideretal.[149] 2011 Euler–Lagrange 3-D,47,000kgofparticleinitially,particlesizedistribution, InternalCFB,commercial-scaleexample Particlevolumefraction,gascomposition,temperatureandreaction
CPFD particleshrinkagefromchemistry,unsteady-state,non- gasifier,complexgeometrywithinternal ratedistribution.
isothermal. cyclones,coalgasification,air-steamas
gasifyingagent.
Abbasietal.[150] 2011 Euler–Lagrange 2-D,sameparticlesizedistributionforcoalandashparticle, FeedingsectionofaCFB,lab-scale,coal Particlevolumefraction,andsizedistribution,fluidvelocity,
CPFD sizedoesnotchangeduetoreaction,unsteady-state,non- gasification,air-steamasgasifyingagent. temperatureandpressuredropdistribution,gascomposition
isothermal. distribution.
Xieetal.[151] 2012 Euler–Lagrange 3-D,differentparticlespeciesforcarbon,ashandsand BFB,lab-scale,biomassgasification, Bubblegrowthwascapturedbutcollisionanderuptionwerenot
CPFD particle,unsteady-state,isothermal. air-steamasgasifyingagent. visible,gascompositionvariationwithT,S/B,ER.Gascomposition
distribution.
Lohaetal.[152] 2014 Euler–Lagrange 3-D,differentparticlespeciesforcarbon,ashandsand BFB,lab-scale,biomassgasification,steam Bubbleformation,developmentanderuptionwithtimeand
CPFD particle,particlesizedistribution,unsteady-state,isothermal. asgasifyingagent. interactionwith,influenceofbiomassinjectionthroughsideport,
gascompositionvariationwithT,S/B,ERandtime.
Xieetal.[153] 2013 Euler–Lagrange 3-D,differentparticlespeciesforcarbon,ashandsand BFB,lab-scale,coalgasification,air-steam Bubbleformation,developmentanderuptionwithtime,distribution
CPFD particle,particlesizedistribution,particlesizechangesdue asgasifyingagent. ofgascomposition,temperatureandreactionrate,carbon
toreaction,unsteady-state,non-isothermal. consumptionwithtime.
712
C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 713
ofsameproperties,cansimulatelarge-scalefluidizedbedgasifier [26] BadziochS,HawksleyPGW.Kineticsofthermaldecompositionofpulverized
with comparatively less time. But, the information about each coalparticles.IndEngChemProcessDesDev1970;9:521–30.
individual particle cannot be provided by the Euler–Lagrange [27] KobayashiH.Devolatilizationofpulverizedcoalathightemperatures.(Ph.D.
thesis).Cambridge,MA:DepartmentofMechanicalEngineering,Massachu-
CPFDmodel. settsInstituteofTechnology;1976.
From the present survey, it is observed that almost in all [28] Nunn TR, Howard JB, Longwell JP, Peters WA. Product compositions and
fluidizedbedgasificationmodelsonlytheoutletgascompositions kineticsintherapidpyrolysisofsweetgumhardwood.IndEngChemProc
DesDev1985;24:836–44.
are compared with experiment. There are few measurements [29] BorosonML,HowardJB,LongwellJP,PetersWA.Productyieldsandkinetics
available for comparison with detailed model results. Therefore, from the vapor phase cracking of wood pyrolysis tars. AIChE J
effortisstillrequiredtovalidatethetrulycomprehensivefluidized 1989;35:120–8.
[30] JandN,FoscoloPU.Decompositionofwoodparticlesinfluidizedbeds.Ind
bedmodels. EngChemRes2005;44:5079–89.
[31] NiksaS.Flashchaintheoryforrapidcoaldevolatilizationkinetics.2:impact
ofoperatingconditions.EnergyFuels1991;5:665–73.
[32] JiangH,MoreyRV.Pyrolysisofcorncobatfluidization.BiomassBioenergy
Acknowledgment 1992;3:81.
[33] JiangH,MoreyRV.Anumericalofafluidizedbedbiomassgasifier.Biomass
Bioenergy1992;3:431–47.
The authors express their sincere gratitude to The Director, [34] DavidsonJF,HarrisonD.Fluidisedparticles.Cambridge:CambridgeUniver-
CSIR-CMERI, Durgapur, India for his continuous support and sityPress;1963.
[35] KuniiD,LevenspielO.FluidizationEngineering.NewYork:JohnWiley;1969.
encouragement.Theauthorsarealsogratefulforthesupportfrom [36] KruseM,WertherJ.2Dgasandsolidsflowpredictionincirculatingfluidized
EUFP7iComFluidproject(GrantNo.312261). bedsbasedonsuctionprobeandpressureprofilemeasurements.ChemEng
Process1995;34:185–203.
[37] PetersenI,WertherJ.Threedimensionalmodelingofcirculatingfluidized
bedgasifierforsewagesludge.ChemEngSci2005;60:4469–84.
References
[38] Wen CY, Yu YH. A generalized method for predicting the minimum
fluidizationvelocity.AIChEJ1966;12:610–2.
[1] Basu P. Combustion and gasification in fluidized bed. Taylor and Francis [39] Grace JR. Contacting modes and behaviour classification of gas–solid and
Group:CRCPress;2006.
othertwo-phasesuspensions.CanJChemEng1986;64:353–63.
[2] BuragohainB,MahantaP,MoholkarVS.Biomassgasificationfordecentra- [40] ChatterjeePK,DattaAB,KunduKM.Fluidizedbedgasificationofcoal.CanJ
lizedpowergeneration:theIndianperspective.RenewSustainEnergyRev
ChemEng1995;73:204–10.
2010;14:73–92. [41] YanHM,HeidenreichC,ZhangDK.Mathematicalmodellingofabubbling
[3] Gomez-BareaA,LecknerB.Modelingofbiomassgasificationinfluidizedbed. fluidised-bed coal gasifier and the significance of ‘net flow’. Fuel
ProgEnergyCombustSci2010;36:444–509. 1998;77:1067–79.
[4] SinghRI,BrinkA,HupaM.CFDmodelingtostudyfluidizedbedcombustion [42] Jennen T, Hiller R, Koneke D, Weinspach PM. Modeling of gasification of
andgasification.ApplThermEng2013;52:585–614. woodinacirculatingfluidizedbed.ChemEngTechnol1999;22:822–6.
[5] SmithRW,MissenWR.Chemicalreactionequilibriumanalysis:theoryand [43] Hamel S, Krumm W. mathematical modeling and simulation of bubbling
algorithms.NewYork:WileyInterscience;1982.
fluidizedbedgasifiers.PowderTechnol2001;120:105–12.
[6] LohaC,ChatterjeePK,ChattopadhyayH.Performanceoffluidizedbedsteam [44] FiaschiD,MicheliniM.Atwo-phaseone-dimensionalbiomassgasification
gasificationofbiomass—modelingandexperiment.EnergyConversManag kineticsmodel.BiomassBioenergy2001;21:121–32.
2011;52:1583–8. [45] SadakaSS,GhalyAE,SabbahMA.Twophasebiomassair–steamgasi_cation
[7] LohaC,ChattopadhyayH,ChatterjeePK.Thermodynamicanalysisofhydro- model for fluidized bed reactors: Part I—model development. Biomass
genrichsyntheticgasgenerationfromfluidizedbedgasificationofricehusk. Bioenergy2002;22:439–62.
Energy2011;36:4063–71. [46] SadakaSS,GhalyAE,SabbahMA.Twophasebiomassair-steamgasi_cation
[8] JANAFthermochemicaltables,3rded.,Part1 2.NewYork;1986.
modelforfluidizedbedreactors:PartII—modelsensitivity.BiomassBioe-
[9] ProbsteinRF,HicksRE.Syntheticfuel.NewYo
þ
rk:McGraw-Hill;1982.
nergy2002;22:463–77.
[10] LiX,GraceJR,WatkinsonAP,LimCJ,ErgudenlerA.Equilibriummodelingof [47] SadakaSS,GhalyAE,SabbahMA.Twophasebiomassair–steamgasi_cation
gasification:afreeenergyminimizationapproachanditsapplicationtoa modelforfluidizedbedreactors:PartIII—modelvalidation.BiomassBioe-
circulatingfluidizedbedcoalgasifier.Fuel2001;80:195–207. nergy2002;22:479–87.
[11] LiX,GraceJR,LimCJ,WatkinsonAP,ChenHP,KimJR.Biomassgasificationin [48] ChejneF,HernandezJP.Modelingandsimulationofcoalgasificationprocess
acirculatingfluidizedbed.BiomassBioenergy2004;26:171–93. influidizedbed.Fuel2002;81:1687–702.
[12] White WB, Johnson SM, Dantzig GB. Chemical equilibrium in complex [49] RossDP,YanHM,ZhongZ,ZhangDK.Anon-isothermalmodelofabubbling
mixtures.JChemPhys1958;28:751–5. fluidized-bedcoalgasifier.Fuel2005;84:1469–81.
[13] Zeleznik FJ. Calculation of complex chemical equilibria. Ind Eng Chem [50] RadmaneshR,ChaoukiJ,GuyC.Biomassgasificationinabubblingfluidized
1968;60:27–57. bedreactor:experimentsandmodeling.AIChEJ2006;52:4258–72.
[14] SmithRW,MissenWR.Chemicalreactionequilibriumanalysis:theoryand [51] Kaushal P, Abedi J, Mahinpey N. A comprehensive mathematical model for
algorithms.NewYork:WileyInterscience;1982.
biomassgasificationinabubblingfluidizedbedreactor.Fuel2010:3650–61.
[15] Zainal ZA, Ali R, Lean CH, Seetharamu KN. Prediction of performance of [52] Pengmei L, Xiaoying K, Chuangzhi W, Zhenhong Y, Longlong M, Jie C.
downdraftgasifierusingequilibriummodelingfordifferentbiomassmate- Modeling and simulation of biomass air–steam gasification in a fluidized
rial.EnergyConversManag2001;42:1499–515. bed.FrontChemEngChina2008;2(2):209–13.
[16] Rao MS, Singh SP, Sodha MS, Dubey AK, Shyam M. Stoichiometric, mass, [53] Goyal A, Pushpavanam S, Voolapalli RK. Modeling and simulation of
energyandexergybalanceanalysisofcountercurrentfixed-bedgasification co-gasificationofcoalandpetcokeinabubblingfluidizedbedcoalgasifier.
ofpost-consumerresidues.BiomassBioenergy2004;27:155–71. FuelProcessTechnol2010;91(10):1296–307.
[17] PrinsMJ,PtasinskiKJ,JanssenFJJG.Thermodynamicsofgas–charreactions: [54] Gungor A. Modeling the effects of the operational parameters on H2
firstandsecondlawanalysis.ChemEngSci2003;58:1003–11. composition in a biomass fluidized bed gasifier. Int J Hydrogen Energy
[18] Prins MJ, Ptasinski KJ, Janssen FJJG. From coal to biomass gasification: 2011;36:6592–600.
comparisonofthermodynamicefficiency.Energy2007;32:1248–59. [55] Chapman S, Cowling TG. The mathematical theory of non-uniform gases.
[19] Jarungthammachote S, Dutta A. Thermodynamic equilibrium model and London:CambridgeUniversityPress;1961.
secondlawanalysisofadowndraftgasifier.Energy2007;32:1660–9. [56] LunCKK,SavageSB,JeffereyDJ,ChepurniyN.Kinetictheoriesforgranular
[20] PellegriniLF,deOliveiraS.Exergyanalysisofsugarcanebagassegasification. flow:inelasticparticlesincouetteflowandslightlyinelasticparticlesina
Energy2007;32:314–27. generalflowfield.JFluidMech1984;140:223.
[21] Abuadala A,DincerI,NatererGF.Exergyanalysisofhydrogenproduction [57] Sinclair JL, Jackson R. Gas–particle flow in a vertical pipe with particle–
frombiomassgasification.IntJHydrogenEnergy2010;35:4981–90. particleinteractions.AIChEJ1989;35:1473–86.
[22] PetersenI,WertherJ.Experimentalinvestigationandmodelingofgasifica- [58] DingJ,GidaspowD.Abubblingfluidizationmodelusingkinetictheoryof
tion of sewagesludgein the circulatingfluidizedbed. Chem EngProcess granularflow.AIChEJ1990;36:523–38.
2005;44:717–36. [59] GidaspowD.Multiphaseflowandfluidization.SanDiego:AcademicPress;
[23] SrinivasT,GuptaAVSSKS,ReddyBV.Thermodynamicequilibriummodeland 1994.
exergy analysis of a biomass gasifier. ASME J Energy Resour Technol [60] HuilinL,YurongH,GidaspowD.Hydrodynamicmodelingofbinarymixture
2009;131:031801-1–7. inagasbubblingfluidizedbedusingkinetictheoryofgranularflow.Chem
[24] FrydaL,PanopoulosKD,KarlJ,KakarasE.Exergeticanalysisofsolidoxide
EngSci2003;58:1197–205.
fuel cell and biomass gasification integration with heat pipes. Energy [61] Louge MY, Mastorakos E, Jenkins JT. The role of particle collisions in
2008;33:292–9. pneumatictransport.JFluidMech1991;231:345–59.
[25] SchusterG,LofflerG,WeiglK,HofbauerH.Biomasssteamgasification—an [62] Pita JA, Sundareasan S. Gas–solids flow in vertical tubes. AIChE
extensiveparametricmodellingstudy.BioresourTechnol2001;77:71–9. J1992;37:1009–18.

714 C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715
[63] Hrenya CM, Sinclair JL. Effects of particle-phase turbulence in gas–solid [97] LiJ,KuipersJAM.Effectofpressureongas–solidflowbehaviorindensegas-
flows.AIChEJ1997;43:853. fluidized beds: a discrete particle simulation study. Powder Technol
[64] SamuelsbergBJ,HjertagerH.Computationalmodelingofgas–particleflowin 2002;127(2):173–84.
ariser.AIChEJ1996;42:1536–47. [98] LiJ,KuipersJAM.Gas–particleinteractionsindensegas-fluidizedbeds.Chem
[65] Nieuwland JJ,Van Sint Annaland M,Kuipers AM, Van SwaaijPM. Hydro- EngSci2003;58(3–6):711–8.
dynamic modeling of gas–particle flows in riser reactors. AIChE J [99] HeY,VanSintAnnalandM.,DeenNG,KuipersJAM.Gas–solidtwo-phase
1996;42:1569–82. turbulent flow in a circulating fluidized bed riser: an experimental and
[66] BalzerG.,SimoninO.,BoelleA.,LavievilleJ.Aunifyingmodelingapproachfor numerical study. In: Proceedings of the fifth world congress on particle
thenumericalpredictionofdiluteanddensegas–solidflow.In:Proceedings technology,April23–27,2006,Orlando,FL,USA.
ofthecirculatingfluidizedbedV,Beijing,China,1996;MSD6. [100] LinkJ,ZeilstraC,DeenN,KuipersH.Validationofadiscreteparticlemodelin
[67] NeriA,GidaspowD.Riserhydrodynamics:simulationusingkinetictheory. a2Dspout-fluidbedusingnon-intrusiveopticalmeasuringtechniques.CanJ
AIChEJ2000;46:52–67. ChemEng2004;82(1):30–6.
[68] ArmstrongLM,GuS,LuoKH.Studyofwall-to-bedheattransferinabubbling [101] LinkJM,CuypersLA,DeenNG,KuipersJAM.Flowregimesinaspout-fluid
fluidizedbedusingthekinetictheoryofgranularflow.IntJHeatMassTransf bed:acombinedexperimentalandsimulationstudy.ChemEngSci2005;60
2010;53:467–76. (13):3425–42.
[69] Loha C, Chattopadhyay H, Chatterjee PK. Assessment of drag models in [102] VremanAW,Al-TaraziM,KuipersJAM,VanSintAnnalandM,BokhoveO.
simulating bubbling fluidized bed hydrodynamics. Chem Eng Sci Supercritical shallow granular and hydraulic flow through a contraction:
2012;75:400–7. experiment,theory,andsimulation.JFluidMech2007;578:233–69.
[70] Loha C, Chattopadhyay H, Chatterjee PK. Euler–Euler CFD modeling of [103] DahlSR,ClellandR,HrenyaCM.Theeffectsofcontinuoussizedistributions
fluidizedbed:influenceofspecularitycoefficientonhydrodynamicbehavior. ontherapidflowofinelasticparticles.PhysFluids2004;14(6):1972–84.
Particuology2013;11(6):673–80. [104] DahlSR,HrenyaCM.Sizesegregationinrapid,granularflowswithcontin-
[71] LohaC,ChattopadhyayH,ChatterjeePK.Effectofcoefficientofrestitutionin uoussizedistributions.PhysFluids2004;16(1):1–13.
Euler–Euler CFD simulation of fluidized bed hydrodynamics. Particuology [105] Dahl SR, Hrenya CM. Size segregation in gas–solid fluidized beds with
2014;15:170–7. continuoussizedistributions.ChemEngSci2005;60(23):6658–73.
[72] PapadikisK,GuS,FivgaA,BridgwaterAV.Numericalcomparisonofdrag [106] OuyangJ,LiJ.Particle-motion-resolveddiscretemodelforsimulatinggas–
modelsofgranularflowsappliedtothefastpyrolysisofbiomass.Energy solidfluidization.ChemEngSci1999;54(13–14):2077–83.
Fuels2010;24:2133–45. [107] OuyangJ,LiJ.Discretesimulationsofheterogeneousstructureanddynamic
[73] PapadikisK,GuS,BridgwaterAV.ACFDapproachontheeffectofparticle behavioringas–solidfluidization.ChemEngSci1999;54(22):5427–40.
size on char entrainment in bubbling fluidized bed reactor. Biomass [108] Helland E, Occelli R, Tadrist L. Numerical study of cohesivepowders in a
Bioenergy2010;34:21–9. densefluidizedbed.CRAcadSci—SerIIb:MecPhysChimAstron1999;327
[74] DeWildeJ,TrujilloWR.Fluidcatalyticcrackinginarotatingfluidizedbedin (14):1397–403.
a static geometry: a CFD analysis accounting for the distribution of the [109] HellandE,OccelliR,TadristL.Numericalstudyofclusterformationinagas–
catalystcokecontent.PowderTechnol2012;221:36–46. particlecirculatingfluidizedbed.PowderTechnol2000;110(3):210–21.
[75] Syamlal M, Rogers W, O’Brien TJ. Mfix documentation theory guide. U.S. [110] HellandE,OccelliR,TadristL.Computationalstudyoffluctuatingmotions
DepartmentofEnergy,OfficeofFossilEnergy.Technicalnote;1993. and cluster structures in gas–particle flows. Int J Multiph Flow 2002;28
[76] RichardsonJR,ZakiWN.Sedimentationandfluidization:partI.TransInst (2):199–223.
ChemEng1954;32(1):35–53. [111] HellandE,OccelliR,TadristL.Numericalstudyofclusterandparticlerebound
[77] Wen CY, Yu YH. Mechanics of fluidization. Chem Eng Prog Symp Ser effectsinacirculatingfluidisedbed.ChemEngSci2005;60(1):27–40.
1966;62:100. [112] IbsenCH,HellandE,HjertagerBH,SolbergT,TadristL,OccelliR.Comparison
[78] SyamlalM,O’BrienTJ.Computersimulationofbubblesinafluidizedbed. ofmultifluidanddiscreteparticlemodellinginnumericalpredictionsofgas
AIChESympSer1989;85:22–31. particle flow in circulating fluidised beds. Powder Technol 2004;149
[79] ErgunS.Fluidflowthroughpackedcolumns.ChemEngProg1952;48:89–94. (1):29–41.
[80] ArastoopourH,PakdelP,AdewumiM.Hydrodynamicanalysisofdilutegas– [113] Lun CCK. Numerical simulation of dilute turbulent gas–solid flows. Int J
solidsflowinaverticalpipe.PowderTechnol1990;62(2):163–70. MultiphFlow2000;26:1707–36.
[81] McKeen T, Pugsley T. Simulation and experimental validation of a freely [114] ZhouH,FlamantG,GauthierD,LuJ.Numericalsimulationoftheturbulent
bubblingbedofFCCcatalyst.PowderTechnol2003;129:139–52. gas–particleflowinafluidizedbedbyanLES-DPMmodel.ChemEngResDes
[82] GibilaroLG,DiFeliceR,WaldramSP.Generalizedfrictionfactoranddrag 2004;82(A7):918–26.
coefficientcorrelationsforfluid–particleinteractions.ChemEngSci1985;40 [115] CundallPA,StrackODL.Adiscretenumericalmodelforgranularassemblies.
(10):1817–23. Geotechnique1979;29(1):47–65.
[83] YangN,WangW,GeW,LiJ.CFDsimulationofconcurrent-upgas–solidflow [116] Schafer J, Dippel S, Wolf DE. Force schemes in simulations of granular
incirculatingfluidizedbedwithstructure-dependentdragcoefficient.Chem materials.JPhysI1996;6(1):5–20.
EngJ2003;96:71–80. [117] WaltonOR,BraunRL.Viscosityandtemperaturecalculationsforassemblies
[84] DouB,DupontV,WilliamsPT.Computationalfluiddynamicssimulationof ofinelasticfrictionaldisks.JRheol1986;30(5):949–80.
gas–solidflowduringsteamreformingofglycerolinafluidizedbedreactor. [118] Langston PA, Tüzün U, Heyes DM. Continuous potential discrete particle
EnergyFuels2008;22:4102–8. simulationsofstressandvelocityfieldsinhopperstransitionfromfluidto
[85] DouB,SongYA.CFDapproachonsimulationofhydrogenproductionfrom granularflow.ChemEngSci1994;49(8):1259–75.
steamreformingofglycerolinafluidizedbedreactor.IntJHydrogenEnergy [119] Tsuji Y, Kawaguchi T, Tanaka T. Discrete particle simulation of two-
2010;35:10271–84. dimensionalfluidizedbed.PowderTechnol1993;77(1):79–87.
[86] Papadikis K, Bridgwater AV, Gu S. CFD modelling of the fast pyrolysis of [120] KawaguchiT,TanakaT,TsujiY.Numericalsimulationoftwodimensional
biomassinfluidisedbedreactors,PartA:Euleriancomputationofmomen- fluidizedbedsusingthediscreteelementmethod(comparisonbetweenthe
tumtransportinbubblingfluidisedbeds.ChemEngSci2008;63:4218–27. two-andthree-dimensionalmodels).PowderTechnol1998;96(2):129–38.
[87] Papadikis K, Gu S, Bridgwater AV. CFD modelling of the fast pyrolysis of [121] Yu AB, Xu BH. Particle-scale modelling of gas–solid flow in fluidisation.
biomass in fluidised bed reactors. Part B: heat, momentum and mass JChemTechnolBiotechnol2003;78(2–3):111–21.
transportinbubblingfluidisedbeds.ChemEngSci2009;64:1036–45. [122] XuBH,YuAB,ChewSJ,ZulliP.Numericalsimulationofthegas–solidflowin
[88] XueQ,DallugeD,HeindelTJ,FoxRO,BrownRC.Experimentalvalidationand abedwithlateralgasblasting.PowderTechnol2000;109(1–3):13–26.
CFDmodelingstudyofbiomassfastpyrolysisinfluidized-bedreactors.Fuel [123] XuBH,YuAB.Numericalsimulationofthegas–solidflowinafluidizedbed
2012;97:757–69. bycombiningdiscreteparticlemethodwithcomputationalfluiddynamics.
[89] YuL,LuJ,ZhangX,ZhangS.Numericalsimulationofthebubblingfluidized ChemEngSci1997;52(16):2785–809.
bed coal gasification by the kinetic theory of granular flow (KTGF). Fuel [124] FengYQ,YuAB.Assessmentofmodelformulationsinthediscreteparticle
2007;86:722–34. simulationofgas–solidflow.IndEngChemRes2004;43(26):8378–90.
[90] WangX,JinB,ZhongW.Three-dimensionalsimulationoffluidizedbedcoal [125] FengYQ,XuBH,ZhangSJ,YuAB,ZulliP.Discreteparticlesimulationofgas
gasification.ChemEngPrecess2009;48:695–705. fluidizationofparticlemixtures.AIChEJ2004;50(8):1713–28.
[91] Armstrong LM, Luo K, Gu S. Effects of limestone calcinations on the [126] IwadateM,HorioM.AgglomeratingfluidizationofwetpowdersandgroupC
gasificationprocessesinaBFBcoalgasifier.ChemEngJ2011;168:848–60. powders:anumericalanalysis.In:FanLS,KnowltonT,editors.Fluidization
[92] ArmstrongLM,GuS,LuoK.ParametricstudyofgasificationprocessesinBFB IX.Durango,USA:EngineeringFoundation;1998.p.293.
coalgasifier.IndEngChemRes2011;50:5959–74. [127] Mikami T, Kamiya H, Horio M. Numerical simulation of cohesive powder
[93] DeenNG,VanSintAnnalandM,VanderHoefMA,KuipersJAM.Reviewof behaviorinafluidizedbed.ChemEngSci1998;53(10):1927–40.
discreteparticlemodelingoffluidizedbeds.ChemEngSci2007;62:28–44. [128] Ye M, Van der Hoef MA, Kuipers JAM. A numerical study of fluidization
[94] Campbell CS, Brennen CE. Computer simulations of granular shear flows. behavior of Geldart A particles using a discrete particle model. Powder
JFluidMech1985;151:167–88. Technol2004;139(2):129–39.
[95] HoomansBPB,KuipersJAM,BrielsWJ,VanSwaaijWPM.Discreteparticle [129] YeM,VanderHoefMA,KuipersJAM.Theeffectsofparticleandgasproperties
simulationofbubbleandslugformationinatwo-dimensionalgas–fluidised onthefluidizationofGeldartAparticles.ChemEngSci2005;60(16):4567–80.
bed:ahard-sphereapproach.ChemEngSci1996;51(1):99–118. [130] PanditJK,WangXS,RhodesMJ.StudyofGeldart’sgroupAbehaviourusing
[96] HoomansBPB,KuipersJAM,VanSwaaijWPM.Granulardynamicssimulation thediscreteelementmethodsimulation.PowderTechnol2005;160(1):7–14.
ofsegregationphenomenainbubblinggas–fluidisedbeds.PowderTechnol [131] KafuiKD,ThorntonC,AdamsMJ.Discreteparticle–continuumfluidmodel-
2000;109(1–3):41–8. lingofgas–solidfluidisedbeds.ChemEngSci2002;57(12):2395–410.

C.Lohaetal./RenewableandSustainableEnergyReviews40(2014)688–715 715
[132] LimtrakulS,BoonsriratA,VatanathamT.DEMmodelingandsimulationofa [143] SniderDM.Anincompressiblethreedimensionalmultiphaseparticle-in-cell
catalyticgas–solidfluidizedbedreactor:aspoutedbedasacasestudy.Chem modelfordenseparticleflows.JComputPhys2001;170:523–49.
EngSci2004;59(22–23):5225–31. [144] SniderDM.Threefundamentalgranularflowexperimentandexperiments
[133] Kuwagi K, Mikami T, Horio M. Numerical simulation of metallic solid andCPFDpredictions.PowderTechnol2007;176:36–46.
bridgingparticlesinafluidizedbedathightemperature.PowderTechnol [145] SmagorinskyJ.Generalcirculationexperimentswiththeprimitiveequations,
2000;109(1–3):27–40. patI:thebasicexperiment.MonWeatherRev1963;91:99–164.
[134] Oevermann M, Gerber S, Behrendt F. Euler–Lagrange/DEM simulation of [146] O’Rourke PJ, Snider DM. An improved collision damping time for MP-PIC
wood gasification in a bubbling fluidized bed reactor. Particuology calculations of dense particle flows with applications to polydisperse
2009;7:307–16. sedimentingbedsandcollidingparticlejets.ChemEngSci2010;65:6014–28.
[135] ZhouZY,YuAB,ZulliP.Particlescalestudyofheattransferinpackedand [147] HarrisSE,CrightonDG.Solitonssolitarywavesandvoidagedisturbancesin
bubblingfluidizedbeds.AIChEJ2009;55:868–84. gas-fluidizedbeds.JFluidMech1994;266:243–76.
[136] HouQF,ZhouZY,YuAB.Computationalstudyofheattransferinabubbling [148] SniderDM,BanerjeeS.HeterogeneousgaschemistryintheCPFDEulerian–
fluidizedbedwithahorizontaltube.AIChEJ2012;58:1422–34. Lagrangian numerical scheme (ozone decomposition). Powder Technol
[137] O’RourkePJ.Collectivedropeffectsonvaporizingliquidsprays.(Ph.D.thesis). 2010;199:100–6.
PrincetonUniversity;1981. [149] SniderDM,ClarkSM,O’RourkePJ.Eulerian–Lagrangianmethodforthree-
[138] SilaenA,WangT.Effectofturbulenceanddevolatilizationmodelsoncoal dimensionalthermalreactingflowwithapplicationtocoalgasifiers.Chem
gasificationsimulationinanentrained-flowgasifier.IntJHeatMassTransf EngSci2011;66:1285–95.
2010;53:2074–91. [150] AbbasiA,EgePE,deLasaHI.CPFDsimulationofafastfluidizedbedsteam
[139] WatanabeH,OtakaM.Numericalsimulationofcoalgasificationinentrained coalgasifierfeedingsection.ChemEngJ2011;174:341–50.
flowcoalgasifier.Fuel2006;85:1935–43. [151] XieJ,ZhongW,JinB,ShaoY,HaoL.Simulationongasificationofforestry
[140] GräbnerM,OgriseckS,MeyerB.Numericalsimulationofcoalgasificationat residues in fluidized beds by Eulerian–Lagrangian approach. Bioresour
circulatingfluidisedbedconditions.FuelProcessTechnol2007;88:948–58. Technol2012;121:36–46.
[141] BruchmullerJ,vanWachemBGM,GuS,LuoKH,BrownRC.Modelingthe [152] LohaC,ChattopadhyayH,ChatterjeePK.Threedimensionalkineticmodeling
thermochemicaldegradationofbiomassinsideafastpyrolysisfluidizedbed offluidizedbedbiomassgasification.ChemEngSci2014;109:53–64.
reactor.AIChEJ2012;58:3030–42. [153] XieJ,ZhongW,JinB,ShaoY,HaoL.Eulerian–Lagrangianmethodforthree-
[142] AndrewsMJ,O’RourkePJ.Themultiphaseparticle-in-cell(MP-PIC)method dimensional simulation of fluidized bed coal gasification. Adv Powder
fordenseparticleflow.IntJMultiphFlow1996;22:379–402. Technol2013;24:382–92.
