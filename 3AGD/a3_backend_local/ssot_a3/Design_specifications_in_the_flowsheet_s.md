# Design_specifications_in_the_flowsheet_s

**Fonte**: Design_specifications_in_the_flowsheet_s.pdf  
**Data de conversão**: 2025-07-30 15:10:24  
**Origem**: base_relevantes

---

PowderTechnology191(2009)260–271
ContentslistsavailableatScienceDirect
Powder Technology
journal homepage: www.elsevier.com/locate/powtec
Design specifications in the flowsheet simulation of complex solids processes
⁎
Claus Reimers, Joachim Werther , Guenter Gruhn
HamburgUnivesityofTechnology,Germany
a r t i c l e i n f o a b s t r a c t
Articlehistory: Inthepresentworkamethodforthetreatmentofdesignspecificationsinthesimulationofcomplexsolids
Received27August2007 processeshasbeendeveloped.
Receivedinrevisedform16September2008 Addingadesignspecificationtotheflowsheetofagivensolidsprocessmeansthatthesolidproductshould
Accepted21October2008 fulfillacertainrequirement.Forexample,itsSautermeandiametershouldbekeptwithinacertaininterval
Availableonline31October2008
orthemassfractionofparticlesaboveacertainthresholdshouldbekeptbelowacertainlimit.Themethod
developed hereis notonlyable tohandle product specifications but also otherstream properties of the
Keywords:
process.Thesepropertiescanbeeitherdistributedorconcentrated.Evendependentlydistributedproperties
Solidsprocesses
Designspecification e.g.aparticlesize-dependentcontaminationcanbehandled.Thetreatmentofdesignspecificationshasbeen
Coalpreparation implementedasanextensionoftheflowsheetsimulationsystemSolidSim.
Dressing Practicalapplicationsoftheimplementedextensionareillustratedwiththreeexamples:(i)asimpleprocess
forthepreparationofbrowncoal,(ii)aprocessforthetreatmentofgravelandsandand(iii)acomplex
processforthemechanicalseparationanddewateringofharborsedimentscontaminatedwithheavymetals.
©2008ElsevierB.V.Allrightsreserved.
1.Introduction behavior of a system with reasonable accuracy. In solids process
engineeringontheotherhand,thepropertiesof thesolids,suchas
Flowsheetsimulationiscommonlyusedinchemicalengineering size, composition or moisture content have to be described by
during process design, optimization and flexibility or sensitivity distributions, with potential dependences between the distributed
analysis [1]. Flowsheet simulation means the numerical solution of attributes—e.g.moisturecontentasafunctionofparticlesize,which
materialandenergybalancesandthedeterminationoftheintensive makesthedescriptionofasolidsprocessmoredifficult[6].
propertiesforvaryingprocessstructuresandsubstancesonthebasis Thestreamstructureofthepresentlyavailablesimulationtools
of coupled mathematical models for the different process steps[1]. for fluid processing is insufficient to handle such distributed
Theuseofsoftwaretoolsforflowsheetsimulationisstateoftheartfor properties [7,8]. In recent years the software tool “SolidSim” has
processesinvolvingjustfluids[2].Inthedesignphaseofachemical been developed especially for solids processes by a group of
process it is often necessary to consider well-defined conditions German”researchinstitutes(see[6,5]).Thistoolcontainsastream
regardingprocessvariables,forexampleproductspecifications.Inthe structure which permits the handling of distributed and depen-
block-orientatedflowsheetsimulationoffluidprocessessuchrequire- dentlydistributedproperties.Thiswasachievedbyusingamatrix
mentscanbeincludedintothesimulationbyusingso-calleddesign structureinwhichthedistributedpropertiescanbestored.Inthis
specifications(see[2,3]). way the interdependence between the properties is considered
There are various commercial software tools for the flowsheet without implying any hierarchy [9]. With the package SolidSim, a
simulationoffluidprocessesavailable(e.g.AspenPlus[3],Pro/II[4]). system has been developed that allows the user to model and to
Thesimulationofprocesseswhichinvolvesolidsisnotasadvanced.It simulatecompletesolidsprocesseslikeitisalreadycommonprac-
is rather common practice to simulate, design and optimize each ticeinfluidprocessengineering.
apparatusseparately[5].Thereasonforthisisthesubstantiallymore Consequently, besides concentrated properties the treatment of
complexstructureofthestreaminformationnecessarytodescribethe designspecificationsinthesimulationofsolidprocessesrequiresthe
propertiesofsolids.Influidprocessengineering,onlyafewvariables considerationofdistributedanddependentlydistributedproperties.
(pressure, temperature, composition) are necessary to describe the Forinstance,therequirementofacertainmassfractionaboveagiven
particlesizeinthecoarsefractioncouldbesuchadesignspecification.
For this task a method for the treatment of design specifications
⁎ Corresponding author. Institute of Solids Process Engineering and Particle
withinthesimulationofcomplexsolidprocesseshasbeendeveloped
Technology, Hamburg University of Technology, Denickestr.15, D-21071 Hamburg,
inthepresentworkandimplementedasanextensiontotheflowsheet
Germany.Tel.:+4940428783239;fax:+4940428782678.
E-mailaddress:werther@tu-harburg.de(J.Werther). simulationsystemSolidSim.
0032-5910/$–seefrontmatter©2008ElsevierB.V.Allrightsreserved.
doi:10.1016/j.powtec.2008.10.012

C.Reimersetal./PowderTechnology191(2009)260–271 261
2.Theory
2.1.Flowsheetsimulation
In the flowsheet of a process handling solids, models of the
processing units (crusher, screen etc.) or process groups (classifier
mill, fluidized bed dryer etc.) are linked by means of material and
energy streams to form a network [6]. Every specific process unit
model of the flowsheet transfers the information at its inlet into a
Fig.2.Mixerexample.
completesetofinformationatitsoutlet.Forthecomputationofthe
specific unit models different types of parameters have to be
distinguished,namely
tionisthatthecalculatedvaluey ofastreampropertyiequalsthe
i,calc
• product properties (y → ): They are stream properties (e.g. mass specifiedvaluey i,spec withinagiventolerance(cid:2).Thiscanbewrittenas
flow)whichcharacterizetheproductstream(s). jy −y jV(cid:2): ð2Þ
• feedproperties( → x):Theyaredefinedliketheproductproperties, i;calc i;spec
butarevalidforthestream(s)whichentertheunit. Thespecificationismetbymanipulationofatleastonedesignor
→
• design parameters (d): They specify the design of the system controlparameter.Forinstance,arequiredreactortemperatureforthe
(e.g.meandiameterofahydrocyclone). combustionofcoalcanbeachievedbychangingthefeedrateofair.In
• controlvariables( → c): Theyspecify theoperation of thesystem terms of the flowsheet the design specification is a recirculation of
(e.g.heatingrateofaheater). information within the flowsheet. Fig. 1 shows the integration of a
• modelparameters(p → ):Theyarepartofthemodeldefinitionsfor designspecificationintotheflowsheetstructure.Theflowsheetconsists
thedifferentprocessunits. oftwoprocessunits.Theoutputy oftheunit1isidenticaltotheinput
1
x ofunit2.Theoutputofunit2issampledandusedtomanipulatethe
2
Themathematicalmodelofaprocessunitjcanbeformulatedas designpropertyd ofunit1.Thesolutionoftheresultingsimulation
1
follows: systemisperformed,likeamaterialrecirculation,iteratively.
Y M Y y; Y x; Y d; Y c; Y p =0 ð1Þ 2.2.1.Treatmentofconcentratedpropertiesindesignspecifications
j(cid:1) (cid:3)
Theuseofdesignspecificationsisalreadystateoftheartforfluid
→
withM asthevectorofmodelequationsfortheprocessunitj. processes. For the definition of the specifications onlyconcentrated
j
Forthecalculationoftheflowsheeteitherthesequential-modular streampropertiesliketemperature,pressureorenthalpyareused.By
methodortheequation-orientedmethodcanbeapplied[2].Byusing wayofexample,theuseofadesignspecificationinafluidprocesscan
the sequential-modular method the flowsheet is computed from beexplainedeasilyassumingthattwowaterstreamswithdifferent
processunittoprocessunit,i.e.oneprocessstageiscomputedonthe temperaturesaretobemixed(Fig.2).ForagivenstreamS,at1kg/s
1
basis of the upstream elements in the flowsheet. The calculation and350Ktheflowrateṁ ofstreamS ,at300Kisadjustedtoachieve
2 2
sequencecorrespondsapproximatelytothedirectionof the flow in adesiredtemperatureofthemixereffluent(e.g.325K).Sotheflow
theplant. Recirculation requires the iterative solution ofunit loops. rate of water in stream S is the manipulated variable, while the
2
Withtheequation-orientedmethod,theentireprocessisdescribedby temperatureoftheprocessoutputstreamS isthesampledvariable.
3
asetofequations.Thedataforthestreampropertiesofallstreamsof Inaddition,itisnecessarytodefinealowerandanupperlimitforthe
thesystemcanbeobtainedfromthesolutionoftheseequations[10]. manipulated variable (e.g. lower limit 0 kg/s, upper limit 10 kg/s).
In cases of solids processes the population balance modeling itself After the calculation of the mixer unit is completed, the design
leads to a model formulation consisting of (partial) integro-differ- specificationmodulesamplestheeffluenttemperatureT .Itreadjusts
3
ential equations. Therefore, an accurate solution of such systems the flow rate of stream S when the specified temperature is not
2
requiressophisticatednumericaltechniquesandhighcomputational achievedandthecalculationstartsagain.Thisiterativeprocedureis
effort.Duetothisfact,theapplicationofpopulationbalancemodelsis repeateduntilthespecificationfromEq.(2)isfulfilled.Fig.3shows
uptonowlimitedtothesimulationofsingleprocessunits[11]andan thetemperatureofstreamS asfunctionoftheflowrateofstreamS
3 2
equation-orientedsimulationoftotalprocessesisnotyetpossible.For inprinciple.Foreachiterationstepthedesignspecificationmodule
this reasons SolidSim uses the sequential-modular method for the
solutionofthemassandenergybalances.
2.2.Designspecifications
By using design specifications it is possible to specify certain
stream properties or some function of stream properties (sampled
variables)withintheflowsheet.Theobjectiveofthedesignspecifica-
Fig.1.Integrationofadesignspecification. Fig.3.TemperatureofstreamS3asafunctionoftheflowrateṁ2ofstreamS2.

262 C.Reimersetal./PowderTechnology191(2009)260–271
hastoadjustthemanipulatedvariable.Thereforemathematicalroot Tohandlethemassfractionsofdependentlydefineddistributedprop-
findingalgorithms(e.g.secantmethod)orone-dimensionaloptimiza- erties(e.g.size-dependentcontamination)the“@-operator”isdefined:
tionmethods(e.g.Brent'sMethod[12])canbeused.
massfractionoftheparticlesthatbelongstoclassiofdistributionA
A@B =
i j andtoclassjoftheA(cid:2)dependentdistributionB:
2.2.2.Treatmentofdistributedpropertiesindesignspecifications
With this @-operator user-defined parameters that refer to depen-
Inparticle technology distributions like for example the particle
dently defined parameters (e.g. particle size-dependent solids
sizedistributionsareusuallycomposedofseveraldiscretevalues.Since
moisture content) can be defined and used for the definition of
in solids processes these parameters are usually important for the
descriptionoftheprocess,designspecificationshavetobeapplicable design specifications.Forinstance the entryshown in Fig. 4 can be
accessedbythefollowingexpression:
todistributedandeventodependentlydistributedparameters.
Thetreatmentofdistributedpropertiesindesignspecificationsis
basedonthedescriptionofthesolidphaseinSolidSim(fordetailssee Particlesize½1(cid:2)2μm(cid:3)@Density h 2000(cid:2)2200kg=m3 i @Moisture h 0(cid:2)1g=kg dryi:
[5]):
Obviously,thefollowingarithmeticrulesarevalidfortheuseofthe
• The solid phase is described by distributions (e.g. particle size @-operator:
distribution)andpossiblydependentdistributions(e.g.particle
A@B =B@A ð3Þ
sizedependentdensitydistribution). i j j i
• All distributions of the solid phase are described by a single m
matrixofmassfractions.Thedimensionofthismatrixisequalto A ðn;mÞ @B j = ∑ A i @B j ð4Þ
thenumberofdefineddistributions.Eachelementofthematrix i=n
m k
describes the mass fraction of a certain particle type (e.g. A ðn;mÞ @B ðl;kÞ = ∑ ∑ A i @B j : ð5Þ
particles that belong to the particle size class 1–2 µm, to the i=n j=l
densityclass1600–1800kg/m3andtothemoistureclass5–7.5g/ FortheexampleshowninFig.4themassfractionoftheparticles
kg )ofthesolidphase.Thesumofallelementsofthematrixis belongingtotheparticlesizeinterval0–32µmandthesolidsmoisture
dry
equaltoone. contentinterval2.5–10.0g/kg canbedescribedby
dry
this
Fi
e
g
x
.
a
4
m
s
p
h
l
o
e
w
t
s
h
a
e
p
s
o
o
s
li
s
d
ibl
p
e
h
d
a
e
se
fin
i
i
s
tio
d
n
es
o
c
f
ri
a
be
s
d
oli
fi
d
rs
p
t
ha
b
s
y
e
a
in
p
S
a
o
r
l
t
i
i
d
c
S
le
im
s
.
iz
In
e
PSD
ð0;5Þ
@Moisture
ð2;4Þ
: ð6Þ
distribution.Inaddition,aparticlesizedependentdensitydistribution This latter expression could be helpful for describing a design
andaparticlesizedependentmoisturedistributionaredefinedforthe specification for a drying process if certain limits regarding the
solidphase. producthavetobefulfilled.
Fig.4.ExampleofasolidphasedefinitioninSolidSim.

C.Reimersetal./PowderTechnology191(2009)260–271 263
Beside these mass fraction related design specifications also beenimplementedasaprototypicalextensionofSolidSim.Themod-
differentuser-definedparameterscanbeusedforthesamepurpose. ule consists of a graphical user interface and a so called design
For the definition of such parameters nearly all available stream specificationunit.Byuseofthegraphicaluserinterfacetheusercan
parameters can be combined using mathematical expressions. For easilydefinedesignspecificationsbythefollowingsteps:
instance,asshowninEq.(7)afinesfractionxfines canbeexpressedas
thesumofthemassfractionswithinthethreesmallestparticlesize 1. Define the variables that will be used for the formulation of the
intervals. designspecification.Ascreenshotofthedialogforthedefinitionof
thestreamvariablesusedforformulationofthedesignspecifica-
3 tionisgiveninFig.5.Thedialogisdividedintotwosections:
x fines = ∑ ΔQ 3(cid:4) d p;i(cid:5) : ð7Þ
i=1
• selectionofstreamproperties
Furthermore parameters describing the position and shape of
Thesection“selectionofvariables”allowstoselectthestream
distributions can be introduced. In the case of a particle size dis-
properties usedas variablesfor thedefinition of the design
tributionitsposition,forexample,canbecharacterizedbyuseofthe
specification.Itconsistsoftwolistboxes:Thelistboxonthe
median value (d ), where d denotes the 50% value of the
p,50 p,50 left contains not only the available concentrated stream
cumulativemassdistributionof theparticlesizesd .Similarly,d
p p,25 properties(e.g.temperature,totalflow,enthalpyetc.)thatcan
and d denote the 25% and 75% values, respectively, of the cum-
p,75 beusedforthedefinitionofavariable,butalsocharacteristic
ulativemassdistributionoftheparticlesizes.Usingthesevaluesthe
valuesdescribingthedefineddistributions(e.g.medianvalue,
shapeofadistributioncanbeexpressedbythesteepnessψ,whichcan
Sautermeandiameteroraveragecontamination).Thelistbox
bedefinedbytheratioofd tod as:
p,25 p,75 on the right contains the defined intervals of a selected
d
distributionthatmaybeusedforthedefinitionofacertain
ψ= p;25: ð8Þ variable.Fortheselectionofadistributionthecomboboxon
d
p;75
thetopofthedialogcanbeused.
Inaddition,parametersliketheSautermeandiametercanbeused.In Additionally,itispossibletodefinecustomstreamproperties,
caseofacontaminationdistribution,forexample,themassaverage that can than be used in all parts of SolidSim (e.g. design
contaminationcanbeusedtocharacterizethisdistributionbyasingle specification, optimization sensitivity analysis etc.). The
value. corresponding input dialog can be opened by clicking the
button‘definecustom’intheupperrightcornerofthedialog.
2.2.3.Implementedextension InFig.5theparametertotalflowofstream8wasselected.
A generallyapplicable module for the treatmentof design spec- • definedstreamproperties
ificationsintheflowsheetsimulationofcomplexsolidsprocesseshas In the section “defined variables” the name of a selected
Fig.5.Dialogforthedefinitionofthevariablesthatareusedfortheformulationofthedesignspecification.

264 C.Reimersetal./PowderTechnology191(2009)260–271
streampropertyisdisplayedintheeditboxontheupperleft showsthedefinedvariables(seeStep1)thatareavailableforthe
corner.Theeditboxintheupperrightcornerallowstheuser definitionofthedesignspecification.
to enter the name of the defined variable. In the example 3. Select the design or control variable that should be adjusted to
showninFig.5“totalFlow8”wasenteredasvariablename.By meetthespecificationandenteralowerandanupperlimitforthe
clicking the greenarrow, the defined variablewill be taken selectedparameter.Oncethedesignspecificationitselfisdefined,
over and can then be used for the definition of a design theuserhastoselectthedesignorcontrolparameterthatshould
specification.Allthedefinedvariablesarelistedinthelistbox beadjustedinordertomeetthespecification.Besidethisalower
on thebottomof thesection.Inthepresent caseavariable andanupperlimithastobedefinedfortheselectedparameter.
named“coarseFraction8”isalreadydefined.Itisshowninthe 4. Selectasolverthatisusedduringthecalculationoftheflowsheet
list box, that thedefined variable refers tothe user-defined in order to solve the design specification.Right now either the
streamproperty“coarseFraction”ofstream8. bisectionmethodorthesecantmethodcanbechosen.
Analogtothedefinitionofstreamvariablesitisalsopossible
todefineunitparametersasvariablesfortheformulationof For each defined specification a design specification unit is
thedesignspecification. integratedintotheflowsheetasshowninFig.1.Insteadofmaterial
streams entering and leaving a process unit information streams
2. Enterthedesignspecificationintheformofanequationanddefine entering and leaving the design specification unit have been
thetargetvalueandthetolerance. introduced. Since SolidSim is a block-oriented flowsheet simulation
Byuseoftheselectedvariablesthedesignspecificationcanbe systemalsothedesignspecificationunitshavetobeintegratedinto
enteredintheformofanequation.Ascreenshotofthedialogfor the calculation sequence. Therefore it was necessary to extend the
the definition of the specification is given in Fig. 6. The section existing implementation of the algorithm for the determination of
“designspecification”allowstodefinethedesignspecificationby thecalculationsequence(LoopFinder[13])andthetearing(ItFinder
use of a mathematical expression. Nearly all mathematical [13]). For the determination of the calculation sequence and the
operators (+, −, ⁎ ,/…) as well as many mathematical functions tear streams the design specification units are treated like normal
(e.g. sine or cosine) may be used for the formulation of the process units and the information streams are considered like
expression.Theeditboxonthetopofthedialogallowstoenterthe materialstreams.
name of the design specification. The target value and the During the calculation of the flowsheet the design specification
corresponding tolerance have to be defined. In the example unitsamplesthevaluesofthevariablesusedfortheformulationofthe
shown in Fig. 6 a design specification called “coarse flow” is design specification (see Fig.1). Withthese values the resultof the
defined as product of the user-defined variable “coarse fraction” user-definedequationforthedesignspecificationiscomputed.Based
andthemassflowofstream8.Thetargetvalueissetto3kg/swith on this result a new value of the adjustable design or control
a tolerance of 1%. The list box in the section “defined variables” parameterisobtainedbyuseoftheselectedrootfindingalgorithm.
Fig.6.Dialogforthedefinitionofthedesignspecification,thetargetvalueandthetolerance.

C.Reimersetal./PowderTechnology191(2009)260–271 265
Subsequently, the new parameter value is set in the corresponding Table1
processunit. Parameterization of the process unit models for the simulation of the brown coal
preparationprocess
3.Applications Processunit Model Parameter Value Dimension
1stscreen Plitt[14] Numberofsievetrays 1 –
The use of design specifications in the flowsheet simulation of Cutsize 6 mm
complexsolidsprocesseswillbeillustratedbyexamplesofprocesses Separationsharpness 4 –
Offsetoffines 0 –
forthepreparationofbrowncoal,forthetreatmentofgravelandsand Sievehammermill Vogelbreakage Adjustableparameterc −0.0065 s/m
and for the mechanical separation and dewatering of harbor function[21,22] Adjustableparameterd 0.532 –
sediments. Minimumfragmentsize 36 μm
Numberofstressevents 2 –
Internal Cutsize 11.53 mm
3.1.Processforthepreparationofbrowncoal
classification Rotorspeed 4000 1/min
Rotordiameter 0.124 m
RWEPowerAGisoperatinglargeopen-pitminesforbrowncoalin 2ndscreen Plitt[14] Numberofsievetrays 1 –
thevicinityofCologneinthewestofGermany.Thecoalisusedmostly Cutsize 6 mm
forelectricitygenerationbydirectcombustioninlargepowerstations Separationsharpness 4 –
Offsetoffines 0 –
butalsofortheproductionofbriquette,cokeandpulverizedcoalfor
variousapplications.Thecoalispreprocessedinadressingprocess.
Thisdressingprocesscanbedividedintothreemajorprocesssteps.
Thefirststageisthepreparationwherethebrowncoalismilledand
classified in order to adjust the particle size of the coal. A certain ThescreeningprocessesaremodeledaccordingtoPlitt[14].Since
amountofthiscoalisthendirectlyfedtoapowerplantthatproduces themeshwidthofboththefirstandthesecondscreenisgivenwith
energyandsteamfortheprocess.Themajorpartofthecoalisinthe 6mmthesamefigurehasbeenadoptedforthecutsizesofthetwo
secondstagedriedbyuseofrotarytubedryerstoacertainmoisture screens. The model parameter α describing the sharpness of the
content.Thedryers areheatedbythelowpressuresteam fromthe separationisassumedtobe4.0,whichindicatesatechnicallysharp
power plant. Subsequently, in the third stage the coal is used to classification.Thedesignandmodelparametersdescribingthesieve
generatedifferentproducts,i.e.briquette,cokeandpulverizedcoal. hammer mill are taken from [15]. Table 1 gives an overview of the
In the following the SolidSim module for the definition of user- modelparameters.
definedpropertiesaswellasthemoduleforthetreatmentofdesign OnthebasisoftheparametervaluesgiveninTable1asimulation
specificationswithintheflowsheetwillbeappliedtothepreparation of the process has beenperformed.The particle size distribution of
stepoftheprocess.TheSolidSimflowsheetisgiveninFig.7. therawcoal(stream1)hasbeenmeasured.Itisshowntogetherwith
Therawcoalisfirstclassifiedinascreeningstep(“1stscreen”).The thecalculatedparticlesizedistributionoftheproduct(stream8)in
coarse fraction from the screen is then milled by use of a sieve Fig.8.
hammer mill (“sieve hammer mill”). The particles generated in the Atypicalproductspecificationregardingtheproductcoalparticle
hammermillarefedtoasecondscreen(“2ndscreen”).Thenthefines sizedistributionisthedefinitionofacertainmassfractionaboveor
fractionfromthefirstandthesecondscreenaremixed.Thismixtureis belowacertainparticlesize.Inthepresentcasetherequirementis
the educt for the drying step. The coarse fraction from the second that the mass fraction of particles above 5.0 mm should be less or
screenisrecycledtothesievehammermill. equal to 3 wt.%. With the actual design of the preparation stepthe
mass fraction of the particles bigger than 5.0 mm turns out to be
7.6wt.%.Theamountofparticleswithsizeslagerthan5.0mmcanbe
influencedeitherbytheenergyinputtothesievehammermillorby
thecutsizeof thesecondscreen.Ingeneral,hammermills usedin
industry are not RPM-regulated, because this is too costly. So the
change of the sieve tray may be the best possibility to achieve the
productspecification.Basedonthisideatheproductspecificationcan
Fig.7.SolidSimflowsheetofthepreparationstep.Thedottedlineindicatesthedesign Fig.8.Measuredparticlesizedistributionofthefeed(stream1)andcalculatedparticle
specification. sizedistributionoftheproductstream8(product)forthecoalpreparationprocess.

266 C.Reimersetal./PowderTechnology191(2009)260–271
The design specification can be easily integrated into the sim-
ulation flowsheet by using the graphical user interface of the
design specification module. Fig. 7 shows the defined design
specification pictured as a dotted line in the flowsheet. The line
connects the stream for which the specification is defined, with
the process unit, whose design parameter is varied to meet the
specification.
Thecomputationwiththisdesignspecificationnotonlyyieldsthe
streamdatabutalsothecutsizeofthesecondscreenthatmeetsthe
specification.Anumericalvalueof3.25mmisobtainedforthiscut
size.FromFig.9itcanbeseenthatthemassfractionofparticlesbigger
than5.0mmisreducedfromaround7.6wt.%to3.0wt.%.
3.2.Processforthetreatmentofgravelandsand
In industrialized countries granular soils are dressed on a large
Fig.9.Comparisonoftheparticlesizedistributionoftheproduct(stream8)forthe scale.Theproductionofgravelandsand,ascomponentsofconcrete
originallayoutwithcalculateddatafortheoptimizedlayout. has a great economic significance. Particles larger than 2 mm are
calledgravelwhiletheparticlessmallerthan2mmarecalledsand
easilybeintegratedintotheflowsheetbyadesignspecification.For [16]. Depending on the use of the different products, different
this purpose in the first step a user-defined parameter x coarse is requirements regarding the purity and particle size distribution
introducedwhichdefinesthemassfractionofparticlesgreaterthan have to be fulfilled. A process for the treatment of gravel and sand
5mmas consiststypicallyofthreedifferentprocesssteps:
10 • adjustmentoftheparticlesizedistribution
x
coarse
=
i
∑
=3
ΔQ
3(cid:4)
d
p;i(cid:5)
ð9Þ
Theparticlesizedistributionisadjustedbyclassificationandsize
wheretheparticlesizedistributionhasbeendescribedby10intervals reduction.
as shown in Fig. 8 (the dots and squares of the distribution curves • purification
indicatetheendofeachinterval).i=3meansthethirdintervalwhich
Unwantedsubstances(e.g.coal,wood,humus)areremovedby
rangesfrom5to6.3mm.
With the parameter x the design specification can then be useofdifferentseparationtechniques.
coarse
definedasfollows:
• dewatering
• specification:
Ingeneral,thesandfractiononlyisdrainedbyuseofdewatering
mass fraction of particles bigger than 5.0 mm of the product screens. Sometimes the water from the dewatering step is
(stream8)equaltoorbelow3wt.%(x =3wt.%) recycled.
coarse,product
• manipulatedvariable:
Inmostcasestherawmaterialisfirstclassifiedinawetscreening
stepinordertoseparategravelandsand.Thereafterthegravelandthe
cutsizeofthesecondscreen(d t,sieve ) sand are treated separately. The arrangementof the following clas-
(3.0mm≤d ≤7mm). sificationandpurificationstepsforthetreatmentofthegravelfraction
t,sieve
Fig.10.SolidSimflowsheetofthepurificationofsand.Thedottedlineindicatesthedesignspecification.

C.Reimersetal./PowderTechnology191(2009)260–271 267
Table2
Parameterizationoftheprocessunitmodelsforthesimulationofthepurificationof
sand
Processunit Model Parameter Value Dimension
Pump Definedoutlet Outletpressure 4.0 bar
pressure[23]
Hydrocyclone Plitt[24,25] Accommodation 1.0 –
designmode factorsF1toF4
Geometricconcept Rietema[26]
Pressuredrop 1.0 bar
Elutriator In-house Diameter 1.0 m
model[23] Separationsharpness 4.0 –
Offsetoffines 0.00 –
Dewatering Plitt[14] Numberofsievetrays 1 –
Sievespacing 0.15 mm
Separationsharpness 4.0 –
Offsetoffines 0.00 –
Feed2 – Watermassflow 0.1 kg/s
Fig.12.Particlesizedistributionofthesand(stream“sand”inFig.10,overflowof
dewateringscreen).
dependsonthewidthoftheparticlesizedistributioninthefeed.In
contrast,thesandfractionisinmanycasesclassifiedandpurifiedby
useofelutriatorsinonesinglestep.Fig.10showsapurificationplant
forthesandfractionwhichiscontaminatedbythepresenceofcoal consistsofalmostcleansand,isdrainedbyuseofadewateringsieve.
particles.Inthisexampletheobjectiveofthispurificationstepisto TheparameterconfigurationoftheunitoperationsisgiveninTable2,
removecoal particlesfromthesand.Thereforethe mixture ofsand whilethedefinitionofthefeedstreamusedinthefollowingexample
andcoalisfedtoahydrocyclonefirst.Theunderflowof thehydro- isshowninFig.11.BesidestheparticlesizedistributionFig.11also
cycloneisthensubjectedtoasortingprocessinanelutriator.Subse- showsthemassfractionofcoalinthedifferentparticlesizeclasses.
quently, in the third stage the underflow of the elutriator, which Theaveragemassfractionofcoalis30g /kg .
coal total
OnthebasisoftheparametervaluesgiveninTable2andthefeed
definitiongiveninFig.11asimulationwasperformed.Fig.12shows
theobtainedparticlesizedistribution,thephaseflowsandthecoal
massfractionforthesand(“product2”).
Atypicalproductspecificationwithregardtothepuritymaybethe
definitionofamaximumallowedmassfractionofacertainsubstance
intheproduct.Hereitisassumedthatthemassfractionofcoalinthe
productshouldbelessorequalto2.0g /kg .Theamountofcoal
coal total
intheproductstreamcanbeinfluencedbychangingtheflowrateof
theclassificationwaterfedtotheelutriator.Theflowratethatfulfills
theproductspecificationcanbedeterminedbyuseofthefollowing
designspecification:
• specification:
massfractionofcoalintheproductlessorequalto2.0g /kg
coal total
(x =2.0g /kg )
coal,product coal total
• manipulatedvariable:
flowrateofupstreamwater(ṁ )
water
(0.1kg/s≤ṁ ≤2.0kg/s).
water
Fig.13.Particlesizedistributionoftheproductsandforthesimulationwithdesign
Fig.11.Definitionofthefeedstreamenteringthepurificationprocess. specification.

268 C.Reimersetal./PowderTechnology191(2009)260–271
Fig.14.Flowsheetofthemechanicaldewateringandseparationofharborsediments.
Thedesignspecification isindicatedinFig.10byadottedline. expense of a slightly decreased production rate from 0.63 kg/s to
Resultingfromthecomputationoftheflowsheetbyusingthedesign 0.56kg/s.
specification module the flow rate of upstream water that fulfills
the product specification is obtained as ṁ =1.23 kg/s. The 3.3.Mechanicaldewateringandseparationofharborsediments
water
corresponding particle size distribution of the product stream is
shown in Fig.13. Comparing with Fig.12 we see that indeed the This example shows the application of the design specification
average coal mass fraction has decreased to 2.0 g /kg at the moduletoasomewhatmorecomplexprocess,namelythemechanical
coal total
Fig.15.SolidSimflowsheetforthemechanicaldewateringandseparationofharborsediments.Thedottedlinesindicatethetwodesignspecifications.

C.Reimersetal./PowderTechnology191(2009)260–271 269
Table3 stage hydrocyclone classification. The underflow of these latter
Parameterizationoftheprocessunitmodelsforthesimulationoftheprocessforthe hydrocyclonesisundergoingasortingprocessinaspiralconcentrator
mechanicalseparationanddewateringofharborsludge[9] which yields after dewatering the third product, namely the “fine
Processunit Model Parameter Value Dimension sand”. The overflow of the second stage hydrocyclones is finally
Coarse Plitt[14] Numberofsievetrays 1 – drained in a sequence of a thickener, a wire belt press and a high
screening Sievespacing 1.0 mm pressure press to yield the sludge which is highly concentrated in
Separationsharpness 2.0 – heavymetalsandwhichhastobekeptonaspecialdisposalsite.
Pump1 Defineoutlet O O f u f t s l e e t t o p f re fi s n s e u s re 0 5 . . 0 0 – bar The simulation flowsheet used for the SolidSim simulation is
pressure[23] showninFig.15.Theonlychangeisthereplacementofthewirebelt
1st Plitt[24,25] Accommodationsfactor 1.0 – pressandthehighpressurepressbyadecantersincemodelsforthe
hydrocyclone designmode F1toF4 pressesarecurrentlynotyetavailable.Theparameterconfigurationof
Geometricconcept Rietema the unit operations is given in Table 3. The definition of the feed
[26]
streamwhich has been taken frommeasurements [18] is shownin
Pressuredrop 1.0 bar
Elutriator In-house Cutsize 0.1 mm Fig.16.Thecontaminationinthisexampleislead.FromFig.16itis
model[23] Cutdensity 2600 kg/m3 obviousthatthebulkofcontaminationislocatedinthefinesfraction
Dewatering Plitt[14] Numberofsievetrays 1 – below45µm.However,thereisalsoacharacteristicpeakinthecoarse
Sievespacing 0.15 mm
fractionsabove500µm.Detailedinvestigationshaveshownthatthis
Separationsharpness 1.65 –
Offsetoffines 0.10 – is due to the presence of ore particles which originate from the
Pump2 Defineoutlet Outletpressure 5.0 bar shipping to the Norddeutsche Affinerie AG which is a large copper
pressure[23] smelterlocatedintheHamburgharborarea.Thiscoarsefractioniscut
2nd Plitt[24,25] Accommodationsfactor 1.0 –
ofbyscreeningwitha700µmscreen.Modelingthisprocesswiththe
hydrocyclone designmode F1toF4
Plitt model [14] yields a coarse product flow of 0.06 kg/s with an
Geometricconcept Rietema
[26] averageleadcontaminationof22ppm.Thismaterialisalsosenttothe
Pressuredrop 2.0 bar disposalsite.
Spiral Plitt[14] Cutsize 20 μm Thegoalofthepresentprocessisofcoursetoobtainasmuchas
concentrator Flowsplit 0.9 –
possibleusefulmaterialforroadbuildingandtoproduceaslittleas
Separationsharpness 2.0 –
Vacuum Plitt[14] Numberofsievetrays 1 – possible highly contaminated sludge for the disposal. Since the
dewatering Sievespacing 0.10 mm practicaluseofsandforconcretemakingandroadbuildingrequires
Separationsharpness 1.65 – that the levels of contaminations are below prescribed levels the
Offsetoffines 0.10 – ultimate goal of the process is to minimize the mass flow of the
Thickener In-house Variableconcentration
model[23] Marginofsafety 1.2 – product “sludge” while keeping the contaminations in the useful
Underflow 90.0 kg/m3 products below the prescribed levels. The maximum allowed
concentration contamination levels in soils and building materials are depending
Settlingvelocity0.001 150.0 mm/min on the heavy metal species and the intended use of the material.
atkg/m3
FurthermoretheselevelsvaryamongthefederalstatesinGermany.
Settlingvelocity5.000 50.0 mm/min
atkg/m3
Withthedesignspecificationtoolitisnowpossibletoassignmean
Settlingvelocity100.0 35.0 mm/min levelstothedifferentproducts“sand”and“finesand”andmanipulate
atkg/m3 acorrespondingnumberofdesignorcontrolparameterssuchthatthe
Settlingvelocity200.0 30.0 mm/min setlevelofcontaminationismet.Alevelof15ppmleadshallnotbe
atkg/m3
exceededinausefulproduct.
Decanter Sedimentation Idealseparation
model[23] In the first step those design or control parameters have to be
Deliquoring Definedresidual 20.0 % identifiedwhicharemostinfluentialwithregardtothisspecification.
model[23] moisture In general, these parameters can be identified by a systematic
Splitter1 ṁ27/ṁ19 0.3 –
sensitivityanalysis[10,19].
Splitter2 ṁ27/ṁ23 0.067 –
dewatering and separation of harbor sediments which is currently
practiced by the port authority of Hamburg [17]. The simulation of
this process has been described in detail by Pogodda [9]. The
harbor sediments are contaminated with heavy metals which are
concentratedmainlyinthefinesfraction.Therefore,theobjectiveof
theprocessistoseparatethehighlycontaminatedfinesfractionfrom
sandfractionswithlowcontamination[20].Thesandcanthenbeused
for example in road building if the contamination is below a given
limitandonlythehighlycontaminatedfractionhastobedepositedon
aspecialdisposalsite.TheflowsheetoftheprocessisshowninFig.14
showingalotofdifferentunitoperationswithalotofrecycles.After
passinganonboardcoarsescreentheharborsedimentishydraulically
conveyed from the dredger into a storage pond. From this storage
pondacuttertakesthesuspensionandpumpsitonthecoarsescreen.
The overflow of the coarse screen is a first product, the “coarse
fraction”. The underflow is pumped into the first hydrocyclone
classification.Theunderflowofthehydrocyclonesisfurtherclassified
inanelutriatortheunderflowofwhichafterdewateringbecomesthe
secondproduct,namelythe“coarsesand”.Theoverflowofboththe
Fig.16.Definitionoffeedstreamenteringtheharborsedimentprocessingplant,from
first stage hydrocyclones and the elutriator is sent into the second measurements[18].

270 C.Reimersetal./PowderTechnology191(2009)260–271
Fig. 17. Particle size distribution and contamination of the sand (stream “sand”, Fig.19.Particlesizedistributionandcontaminationofthesludge(stream“sludge”in
overflowofthe“dewateringscreen”)forthesimulationwithdesignspecifications. Fig.15)forthesimulationwithdesignspecifications.
The product “sand” is strongly influenced by the cut size of the Comparing the contamination distributions in the different
elutriatorwhiletheproductfinesand“ismostlyinfluencedbythecut product flows with that of the sludge in Fig.19 on the one hand
sizeofthespiralconcentrator.” and that of the feed on the other hand we see that the con-
Therefore,twodesignspecificationsaredefined: tamination is now indeed concentrated in the sludge stream,
whereas the two product streams have a comparatively low level
• DesignspecificationI ofcontamination.Thecumulativesolidsmassflowofbothproduct
streams is 0.53 kg/s which means that over 50% of the sediment
– specification:averagecontaminationof“streamsand”15ppm massareobtainedforusefulpurposes.Itisclearthattheflowsheet
– manipulated variable: cut size of the elutriator (d ) simulationwithdesignspecificationssuggestedhereisofgreathelp
t,elu
(70µm≤d ≤200µm) for the practical operation of such a complicated solids process
t,elu
plant.
• DesignspecificationII
4.Summaryandconclusions
– specification: average contamination of stream “fine sand”
15ppm In the present work a method for the treatment of design
– manipulatedvariable:cutsizeofthespiralconcentrator(d ) specifications in the simulation of complex solids processes has
t,spiral
(20µm≤d ≤100µm). been developed. Besides concentrated properties the method con-
t,spiral
siders distributed and dependently distributed properties. The
With these definitions the flowsheet has been computed again developed method has been implemented as an extension of the
usingthedesignspecificationmodule.Thestreamdataobtainedare flowsheet simulation system SolidSim. The developed approach as
showninFigs.17–19togetherwiththedistributionsofparticlesizes well as the developed extension of SolidSim was tested by three
andleadcontaminations.Thedesignparameterswhicharekeeping examples,namelythepreparationofcoalwithacrusher/sievecycle,a
thespecificationsare: processforthedressingofsandandfinallyaprocessforthetreatment
of harbor sediments which were contaminated with heavy metals.
• cutsizeoftheelutriator:d =88µm
t,elu According to the results obtained, the practical applicability of the
• cutsizeofthespiralconcentrator:d =33µm.
t,spiral developedmethodhasbeendemonstratedsuccessfully.
Acknowledgements
TheauthorswouldliketothankErnst-UlrichHartgeandMatthias
Pogoddaformanyhelpfuldiscussions.Thanksarealsotothecompanies
BayerTechnologyServices,BASFOutotec,Dow,WackerandPuracfor
theirsupportoftheSolidSimdevelopmentintheframeworkoftheIK
SolidSim Consortium. Finally, supply of the measurements by RWE
PowerAGisgreatlyacknowledged.
References
[1] H.Schuler,Prozeßsimulation,VCH,Weinheim,1995.
[2] W.Seider,J.Seader,D.Lewin,ProcessDesignPrinciples:Synthesis,Analysisand
Evaluation,JohnWiley&Sons,NewYork,1999.
[3] AspenTech,onlineresource,lastchecked:22.Aug.2007.URLwww.aspentech.com.
[4] SimSci-EssorInc.,onlineresource,lastchecked:22.Aug.2007.URLhttp://www.
simsci-esscor.com.
[5] E.-U.Hartge,M.Pogodda,C.Reimers,D.Schwier,G.Gruhn,J.Werther,Flowsheet
simulationofsolidsprocesses,KONA(24)(2006)146–158.
[6] E.-U.Hartge,M.Pogodda,C.Reimers,D.Schwier,G.Gruhn,J.Werther,Atoolforthe
Fig.18.Particlesizedistributionandcontaminationofthefinesand(stream“finesand”, flowsheet simulation of solids processes, Aufbereitungs-Technik 47 (1) (2006)
solidproductof“vacuumdewatering”)forthesimulationwithdesignspecifications. 42–51.

C.Reimersetal./PowderTechnology191(2009)260–271 271
[7] J.-C. Töbermann, J. Rosenkranz, J. Werther, G. Gruhn, Block-oriented process [23] Institute of Solids Process Engineering and Particle Technology, Hamburg
simulationofsolidsprocesses,ComputersandChemicalEngineering23(2000) UniversityofTechnology,Hamburg,Germany,SolidSimUserGuide.
1773–1782. [24] L.R.Plitt,Amathematicalmodelofthehydrocycloneclassifier,CIMBulletin80
[8] G.Gruhn,J.Rosenkranz,J.Werther,J.-C.Töbermann,Developmentofanobject- (1976)39–50.
orientedsimulationsystemforcomplexsolidsprocesses,ComputersandChemical [25] L.R.Plitt,A.Broussaud,C.Conil,Animprovedmethodofcalculatingthewater-split
Engineering68(1996)509–517. inhydrocyclone,MineralsEngineering3(5)(1990)533–535.
[9] M.Pogodda,Developmentofanadvancedsystemforthemodelingandsimulation [26] K.Rietema,PerformanceanddesignofhydrocyclonesI–IV,ChemicalEngineering
ofsolidsprocesses,Ph.D.thesis,HamburgUniversityofTechnology(2007). Science15(3–4)(1960)298–325.
[10] G. Gruhn, Verfahrenstechnische Berechnungsmethoden, Teil 6: Verfahren und
Anlagen,VCH,Weinheim,1988.
[11] S.Motz,S.Mannal,E.-D.Gilles,Integralapproximation—anapproachtoreduced Glossary
[12] m 9 R 8 . o 7 B d – r e 1 e l 0 s n 0 t, 0 fo . A r lg p o a r r it t h ic m ul s at f e or p M ro i c n e i s m se iz s a , ti C o h n em W ic it a h l ou E t ng D in er e i e v r a i t n e g s, S P c r i e e n n t c i e ce- 5 H 9 all ( , 20 N 0 e 4 w ) → B c A i i c c v l l e a a c s s t s s o j i r o o c f f o d n d i i t s s a t t i r r n i i b i b n u u g t t i i t o o h n n e B A controlparametersofacertainprocessunitmodel
Jersey,2002. d → vectorcontainingthedesignparametersofacertainprocessunitmodel
[ [ [ 1 1 1 4 5 3 ] ] ] ( L C E G 1 . n . . R 9 J R g . . 7 i e P F n 1 i l o m ) e it r e 4 t d e , r 2 e r i T n s – r h , , g 4 e J 7 H . S a . W . c n i H e a e n l r u y t c t s h e c i e h s 2 r i o , s 4 f G o s ( n . o 4 , G l ) i T r d ( u h 1 – h 9 e s n 6 o a , 9 li n F ) d a l 7 o s ly 7 e w s 1 p s i – a s h r 7 e a o 8 e t f 5 i t o . c s n h im s e i m u n l i c a c l t a a i l o ss n p ifi l o a e f n r s t s o , fl l C i o d IM w s s p B h r u o e l e c le e ts t s i , s n e C 6 s h 4 — e ( m 7 d i 0 a c 8 t a a ) l d d d d t p p p , , [ 2 5 [ m 5 0 m [ [ ] ] m m ] ] c p 2 m p u 5 a a e t r % r d t t s i i i v i c c a z a l l n e e e lu v s d e i a i z a l o e u m f s e t e d h ( t p 5 e e ) 0 r c % um va u lu la e ti o v f e t m he as c s um di u st l r a i t b iv u e tio m n a o ss f d th is e tr p i a b r u t t i i c o le n s o i f ze th s e dp
r P e r c o o c n es c s il i i n a g tio 4 n 7( a 2 n 0 d 08 a ) dj 1 u 3 s 8 tm –1 e 5 n 8 t . ofmodelparameters,ChemicalEngineeringand m dp ̇ ,7 [k 5 g [ / m s] ] 7 m 5 a % ss va fl l o u w eofthecumulativemassdistributionoftheparticlesizesdp
[16] Dineniso14688-1:Geotechnicalinvestigationandtesting—identificationand →
classificationofsoil—part1:identificationanddescription(2003).
p
M →j v
v
e
e
c
c
t
t
o
o
r
r
o
c
f
on
m
t
o
ai
d
n
e
i
l
n
e
g
q
t
u
h
a
e
ti
m
on
o
s
d
f
e
o
l
r
p
p
a
r
r
o
am
ce
e
s
t
s
e
u
rs
ni
o
t
f
j
acertainprocessunitmodel
[17] H.D.Detzner,W.Schramm,U.Döring,W.Bode,Newtechnologyofmechanical
treatment of dredged material from Hamburg harbour, Water Science and
Q3(dp) cumulativemassdistributionofparticlesized
[18] T J o . e f W c d h r e e n r d t o h g lo e e r g d , y R m . 3 H a 7 t i e l ( l r 6 i i g – a a l 7 , r ) d in t ( , : 1 U K 9 . 9 . K W 8 a ) l o c 3 l k f 3 , , 7 W J – .W . 3 v 4 e a 3 b n . e d r, e I n nv B e r s in ti k g , a F ti . o C n ol o o n n t ( h E e d m s.) e , c C h o a n n t i a c m al i t n r a e t a e t d m S e o n i t l → T x y→ [K] t v v e e e m c c t t p o o e r r r c c a o o tu n n r t t e a a i i n n i i n n g g t t h h e e i i n n l l e e t t s s t t r r e e a a m m p p r r o o p p e e r r t t i i e e s s
'88,KluwerAcademicPublishers,Dordrecht,1988,pp.1285–1294. yi,calc calculatedvalueofastreampropertyi
[19] D. Schwier, Zum Einfluss von Parameter- und Modellungenauigkeiten bei der yi,spec specifiedvalueofthestreampropertyi
Simulation komplexer Feststoffprozesse, Ph.D. thesis, Hamburg University of
Technology,inpreparation(2007). Greekletters
[20] D.Detzner,TheHamburgProjectMETHA:largescaleseparation,dewateringand (cid:2) toleranceofthespecificationwhichhastobefulfilled
reuseofpollutedsediments,EuropeanWaterPollutionControl5(1995)38–42.
ψ steepnessofadistribution
[21] L.Vogel,W.Peukert,Breakagebehaviourofdifferentmaterials—constructionofa xfines finesfraction
mastercurve for the breakage probability, Powder Technology (129) (2003)
101–110.
[22] L.Vogel,W.Peukert,Modellingofgrindinginanairclassifiermillbasedona
fundamentalmaterialfunction,KONA(21)(2003)109–120.
