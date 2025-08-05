# Modeling_and_flowsheet_simulation_of_con

**Fonte**: Modeling_and_flowsheet_simulation_of_con.pdf  
**Data de conversão**: 2025-07-30 15:10:09  
**Origem**: base_relevantes

---

PowderTechnology238(2013)132–141
ContentslistsavailableatSciVerseScienceDirect
Powder Technology
journal homepage: www.elsevier.com/locate/powtec
Modeling and flowsheet simulation of continuous fluidized bed dryers
⁎
Ibrahim Alaathar , Ernst-Ulrich Hartge, Stefan Heinrich, Joachim Werther
HamburgUniversityofTechnology,InstituteofSolidsProcessEngineeringandParticleTechnology,Hamburg,D-21071,Germany
a r t i c l e i n f o a b s t r a c t
Availableonline5April2012 InthecurrentpaperasimulationtoolbasedonpreviousworkofBurgschweigerandTsotsas[1]isimplemented
within the framework of the flowsheet simulation program SolidSim [4]. The implementation within the
Keywords: flowsheetsimulationprogramallowsthesimulationofthedryingprocessformanydifferentliquidsandsolids.
Fluidizedbeddrying Itcanalsosimulatethedryingofmixturesofdifferentsolids.Themodulecomputesthevaporloadingand
Simulation temperatureoftheoutflowinggasandthemoistureandtemperaturedistributionofthesolidsattheoutlet
Moisturedistribution
takingintoaccounttheirresidencetimedistribution,theirparticlesizeandtheirmoisturedistributionatthe
Populationbalance
inlet.Furthermorethemodelhasbeenextendedbyasimpleapproachtosimulatethedryinginanelongated
fluidizedbeddryer.Aftervalidationthemodelhasbeenusedtostudytheinfluenceofresidencetime,particle
sizeandinletmoisturedistributioninadditiontodryingofmixtureofdifferenttypesofsolid.Forthemodeling
itisassumed,thatthereisnoclassificationoccurringwithinthebed.Thisassumptioniscommonlyfulfilledas
longastheparticlesizedistributionisnottoowideandthefluidizationvelocityissufficientlyhigh.Inthiscase
themixingactionofthebubblesisdominatingthesegregationtendencies.
©2012ElsevierB.V.Allrightsreserved.
1.Introduction mayhaveamajorimpactontheircolor,taste,andaroma.Itmayalso
significantlyimpactthepotencyandconsistencyofpharmaceuticals.
Fluidized bed drying is a technology which is widely applied in Thepresenceofproductmoisturedistributionbythecontinuous
industry for the drying of particulate solids. One of the major fluidizedbeddryingcannotbeavoided,butforcertainproductsitis
advantages of fluidized bed system results from the fact that the veryimportanttonarrowthemoisturedistributiontobewithinthe
high turbulence created in the bed provides high heat and mass safelimitoftheproduct.
transfer,aswellasagoodmixingofthesolidsinsidethebed.Another Kozanogluetal. [8] studiedexperimentally theeffectof particle
importantadvantageisthegoodtemperaturecontrol,whichallows sizeonthevacuum-fluidizedbeddryingusingpepperseedparticles
aneffectivedryingofheatsensitivematerialsasforexamplefoodor withtwodistinctdiameters.Intheconstantdryingrateperiod,the
pharmaceuticalproducts.Adisadvantageofthenearlyperfectsolids small particles demonstrated stronger drying rates resulting from
mixinginthefluidizedbedisthewideresidencetimedistributionof higher mass transfer coefficient values and larger contact area per
thesolids,i.e.someparticlewillleavethedryeralreadyafewseconds unitparticlehumidity.Theexperimentalresultsalsoshowedthatthe
after they have been fed to it, while other particles stay for very falling drying rate period was controlled in the beginning by the
long times inside the dryer, which may result in a wide moisture particlediameterandlaterbytheeffectiveporosityoftheparticle.A
distributionofthesolidsattheoutletofthedryerashasbeenshown schemeofacontinuousfluidizedbeddryerisdepictedinFig.2.The
experimentallybyKettneretal.[7]andbyPeglowetal.[10]. wetparticlesenterintothedryerataconstantflowrateandatthe
InAgricultural andfoodindustrythemaintargetofdryingisto sametimetheproductisdischargedthereforethemassofsolidinthe
decreasethemoisturecontentandthenthewateractivityw ,which dryerremainsconstant.Conventionalmodelingapproachesdescribe
a
depends directly on the moisture content, in order to enable their the solids in the fluidized bed as ideally mixed with average
storage at ambient temperature and to improve its shelf time. By properties, i.e. average particle size, average moisture and average
knowingthewateractivityFig.1[11],itispossibletopredictwhich residencetime.Suchamodelwillonlypredictanaveragemoisture
microorganismswillbepotentialsourcesofspoilage.Inadditionto contentforthesolidinthedryer.
influencingmicrobialspoilage,wateractivitymayplayasignificant Burgschweiger and Tsotsas [1] developed a model of the in
roleindeterminingtheactivityofenzymesandvitaminsinfoodsand stationary drying of solids in fluidized beds which takes the
distribution of residence times into account. It calculates the heat
andmasstransferfortheactualmoistureofeachindividualresidence
⁎ Correspondingauthor.Tel.:+4940428782765;fax:+4940428782678. timeclass.Fortheparticlesizethemeansurfacediameterwasusedas
E-mailaddress:i.alaathar@tu-harburg.de(I.Alaathar). thecharacteristicdiameter.
0032-5910/$–seefrontmatter©2012ElsevierB.V.Allrightsreserved.
doi:10.1016/j.powtec.2012.03.048

I.Alaatharetal./PowderTechnology238(2013)132–141 133
Table1
AcomparisonbetweentheBurgschweigermodel[1]andthenewlydevelopedmodel.
Considerationof Burgschweiger Newmodel
Energybalancesforgasphaseanddispersephase
Thesorptivebehaviorofthesolid
Transportresistanceinthe2nddryingperiod
Bubbleformation
Residencetimedistribution
Considerationofthetemperaturedependencyof –
gasproperties
Particlesizedistributionofthesolids –
Moisturedistributionoffeedmaterial –
Mixtureofseveralsolidcomponents –
Fig.1.Wateractivityandstabilitymapforfoodmaterial.
Forthemodelfollowingassumptionsweremade:
Based on the model by Burgschweiger and Tsotsas [1] (in the
• thebubblephaseisparticle-free,thegasinthebubblephaseflows
following named as ‘Burgschweiger model’) a generally applicable asplugflow
stationary model was implemented into SolidSim. In this work the • particlesinthesuspensionareperfectlymixed
modelwasgeneralizedtoallowitsapplicationtoarbitrarycombina-
• thegasinthesuspensionphaseflowsasplugflow
tionsofsolidsandliquidsandadjustedtoconsidertheparticlesize • solidparticlesareaddedandremovedataconstantrate
and moisture distribution of the feed material and to be able to • heat and mass are transferred between the particles and the
calculate a mixture of solids. Since SolidSim is a steady state surroundingsuspensiongas
simulation tool, the formulation had to be adjusted accordingly. A • the bubble fraction is dependent of bed height and calculated
comparison list between the current model and the model by accordingtoHilligardtandWerther[6]
BurgschweigerandTsotsasisshowninTable1. • thefallingdryingrateinthe2nddryingperiodcanbedescribedby
Finally the inclusion of the model as a unit into the flowsheet amodifiednormalizeddryingcurve
simulationprogramSolidSimallowstosimulatetheinterdependency • thereisnoentrainmentofsolids.
of the operation of a dryer with preceding or subsequent solids
processingunits. 2.1.Gasphasebalances
2.Model Suspension phase: the vapor loading Y of the gas in the
suspension phase is changed by the mass s flow M _ of vapor
ps
Fluidized bed drying involves processes on different scales, the transferredfromthe particlestothegas andby themassflow M _
sb
heatandmasstransferbetweenthegasandthesingleparticleonthe of vapor exchanged between the bubble phase and the suspension
micro scale and the more macroscopic heat and mass transfer gas:
betweenthebubbleandthesuspensionphaseinthe fluidizedbed.
Processesonbothscaleshavetobemodeledandtobecombinedina
fluid Th iz e ed flu b i e d d iz d ed ry b e e r d m m o o d d el e . lusedinthisworkisbasedonatwophase ð1−vÞ⋅M _ g⋅ ∂ ∂ Y ξ s¼ ∂ ∂ ξ M _ ps−M _ sb ð1Þ
model,whichdividesthefluidizedbedintoasolidfreebubblephase (cid:1) (cid:3)
andasuspensionphaseconsistingoftheparticlesandapartofthe
gas flowing through the suspension with the minimal fluidization Inthisequationvisthevolumefractionofthebedoccupiedbythe
velocityu . bubblephase, M _ g denotesthetotalgasmassflowthroughthebed
mf
AschematicrepresentationofthemodelisshowninFig.3. andξistheheightz abovethegasdistributornormalizedwiththe
bedheight.
Fig.2.Continuousfluidizedbeddryer. Fig.3.Thefluidizedbedmodel.

134 I.Alaatharetal./PowderTechnology238(2013)132–141
Similar to the vapor loading of the suspension gas the specific Bubblephase:thegasinthebubblephaseexchangesvapor,heat
enthalpyh ofthesuspensiongaschangeswithheight: andenthalpywithsuspensiongasonly.Thusthebalancesbecome
s
_
ð1−vÞM _
g
∂
∂
h
ξ
s¼
∂
∂
ξ
H _ ps−Q _
sp
þQ _ bs−H _
sp
ð2Þ vM _
g
∂
∂
Y
ξ
b¼ ∂M
∂ξ
sb ð3Þ
(cid:1) (cid:3)
withH _ denotingtheenthalpyflow,whichisduetothetransferof Forthevaporloading
vaporfr p o s mtheparticletothesuspensiongas,Q _ istheheatfluxfrom
_ _sp
the suspension gas to the particle, H and Q are the respective
sb bs
s
e
u
n
s
t
p
h
e
a
n
lp
s
y
ion
an
g
d
as.
heat flows exchanged between bubble phase and vM _
g
∂
∂
h
ξ
b¼
∂
∂
ξ
H _ sb−Q _
bs
ð4Þ
(cid:1) (cid:3)
Fig.4.ScreenshotoftheSolidSimprogramwiththefluidizedbeddryermodule.

I.Alaatharetal./PowderTechnology238(2013)132–141 135
2.2.Solidphasebalance with β being the mass transfer coefficient and Ac the solids
ps ps,k,f
surface of the specified class. υ_ ηc is the modified normalized
i;k;f
Populationbalanceshavetobesolvedforthesolidphaseinorder
drying rate after Burgschweiger(cid:1)and(cid:3)Tsotsas [1] as a function of
todescribethemoistureattheoutletofthedryerdependentonthe
normalizedparticlemoisturecontentaftervanMeel[12]
particlesizeandontheresidencetime.Itisassumed,thatthestate
variables of every particle, i.e. its moisture content X and tempera-
ture T ,aredeterminedbyitssize,itsinletmoisturecontentandits η¼
X−X
eq ð9Þ
residen
p
ce time in the dryer, that means, that the particles with a
X cr−X
eq
certain residence time having the same particle size and the same
This normalized drying function has to be determined experi-
inlet moisture content will have always the same temperature and
mentallyforeverycomponent.
the same moisture. Furthermore it is assumed, that there is no
classification occurring within the bed. This assumption is valid as
Theheattransferbetweengasandparticlesissimilarlydefinedby
long as the particle size distribution is not too wide and the
o d fl f i u r i t e d h c i e t za e b t x u io c b h n b a l v n e e s g lo e is c o it d f y o m i m s o i s i n s u a t f u t fi i r c n e i g e b n t e t h l t e y w h s e e i e g g n h re . t g h In a e t t i p h o a i n s rt c t i e a c n l s e e d s e th i n s e c n i m e e s g i . x l W e in c g h te i a d le c , t t t io h h n e e Q _c sp;i;k;f ¼∫ 1 0d d p ∫ ; p k ; − k 1 m m ∫ f− f 1τ ∫ τ i− i 1 ∂ξ∂ ∂ d 4 p Q _ ∂ s m p ∂τ ⋅dτ⋅dm⋅dd p⋅dξ ð10Þ
transportofheatbetweentheparticlesbelongingtodifferentclasses ¼∫ 1 0 N i⋅αc ps;k;f⋅Ac ps;k;f⋅ T s ðξÞ−Tc p;i;k;f dξ
istakenintoaccount.Finallyitisassumed,thatparticlesundergono h i
shrinking, fragmentation or abrasion, i.e. there is no transfer of wit T h h α e p e s n b t e h in al g p t y h fl e o m w a r s a s t t e ra fr n o s m fer th co e e p ffi ar c t i i e c n le t. tothesuspensionH _c
particlesbetweentheparticlesizeclasses. ps;i;k;f
resultingfromthetransferredvapormassfluxiscalculatedaccording
Forthecomputationaltreatmentthethree-dimensionaldistribu-
to
tion of particle size, residence time and inlet moisture content is
discretized into different size, inlet moisture and residence time
classes.Thesizeclassesareinthefollowingindexedby k,theinlet H _c ps;i;k;f ¼M _c ps;i;k;f⋅ c w;g⋅Tc p;i;k;f þΔh v ð11Þ
moistureby f,theresidencetimeclassesby i.
(cid:1) (cid:3)
With assumptions as stated above, the equations describing the
residencetimedistribution,moisturecontentandenthalpyinevery
Themassandheattransferbetweenbubblephaseandsuspension
size, inlet moisture content and residence time class under steady
gasaregivenby
stateconditionsforthecomponentcare:
_
M p⋅ d d N τ i¼−M _ p;in⋅N i ð5Þ
∂M
∂ξ sb¼ρ g⋅β sb⋅A sb⋅½Y s ðξÞ−Y b ðξÞ(cid:2) ð12Þ
_
ΔQC 3;k⋅ΔQC 3;f⋅N i⋅M p⋅ dX d c i τ ;k;f ¼−M _c ps;i;k;f ð6Þ
∂Q
∂ξ bs¼α sb⋅A sb⋅½T b ðξÞ−T s ðξÞ(cid:2) ð13Þ
withtheproductsofthemasstransfercoefficientandthetotalbubble
ΔQC 3;k⋅ΔQC 3;f⋅N i⋅M p⋅ dh d c p; τ i;k;f ¼ Q _c sp;i;k;f−H _c ps;i;k;f þQ _ pp ð7Þ s b u u r b f b ac le e s β u sb rf ⋅ a A c s e b a α n sb d ⋅A o s f b th ca e lc h u e la a t t ed tra a n c s c f o e r r d c in o g effi to cie a nt c a o n rr d el t a h ti e on tot b a y l
(cid:1) (cid:3) GroenewoldandTsotsas[4].
HereΔQC andΔQC arethemassfractionofparticlescomponent The enthalpy transfer between suspension and bubble phase is
3,k 3,f
c in size class k and moisture class f respectively, N the fraction of calculatedanalogoustoEq.(11)by
_ i
particlesin the residencetime class i, Q is the interparticle heat
pp
_ _
t
r
r
e
a
s
n
id
s
e
fe
n
r
c
,
e
i.
t
e
im
. t
e
h
a
e
n
e
d
x
/o
c
r
ha
s
n
iz
g
e
e
cl
o
a
f
ss
h
e
e
s
a
,
t
w
b
h
e
ic
t
h
we
d
e
if
n
fer
pa
in
rti
t
c
e
l
m
es
pe
in
rat
d
u
i
r
f
e
fe
.
r
T
e
h
n
e
t ∂
∂
H
ξ
sb¼ ∂M
∂ξ
sb c
w;g
ðT
sb
Þ⋅T
sb
þΔh
v
ðT
sb
Þ ð14Þ
enthalpyofenteringandleavingparticles H _ and H _ aretaken h i
p;in p;out
intoaccountbythetotalenergybalanceofthefluidizedbeddryer.
Finallytheheatexchangebetweenparticlesbelongingtodifferent
2.3.Kinetics residencetime,particlesize,orinletparticlemoisturecontentclasses
and having different temperatures is calculated according to
To solve the above described system of balance equations the BurgschweigerandTsotsas[1]by
dryingkinetics,i.e.theexchangeflows(Fig.3)areneeded.According
tothemodelassumptionoftheideallymixedsolidphase,plugflowin _
t r h es e id g e a n s c p e ha ti s m e e an a d n a d d p is a t r r t i i b cl u e tio si n ze of d t i h s e tri p b a u r t t i i o c n le s p t r h o e pe e r x ti c e h s a d n u g e e t fl o o t w he s Q _ pp;i;k;m ¼∫ d d p p ; ; k k−1 ∫ m m f f−1 ∫ τ τ i i−1∂d ∂ p Q ∂m pp ∂τ ⋅dτ⋅dm⋅dd p
_ (cid:2)
betweengasandsolidshavetobemodeledfour-dimensionallyalong ¼N i⋅α pp⋅A ps;k;m⋅ T p−T p;i;k;m ð15Þ
theheight-coordinateandthedistributionsofresidencetime,particle (cid:1) (cid:3)
sizeandinletmoisturecontent.
A istheparticlesurfaceofallparticlesbelongingtosizeclassk
ps,k,m
Themasstransferbetweenparticlesandgasphaseisgivenby and moistureclass m, α theheat transfer coefficient betweenthe
pp
particles. As a first approach the heat transfer coefficient α was
pp
M _c ps;i;k;f ¼∫ 1 0d d p ∫ ; p k ; − k 1 m m ∫ f− f 1τ ∫ τ i− i 1 ∂ξ∂ ∂ d 4 p M ∂ _ m ps f∂τ ⋅dτ⋅dm⋅dd p⋅dξ b c c o a e l n t c w t u a e l c a e t t n e a d r w e w a al i l o th f an t t w h d e o s c u d o s i r f p f r e e e r n l e a s n t i i o t o n n p . a b B r y t e i c c M a le u a s s r e t is in t v h [ e e 9 r ] y co f s o n m r ta a t c l h l t , e t t h h im e e a r e e t f a o t n r r a e d n , s t t f h h e e e r
¼∫ 1 0 N i⋅υ_ ηc i;k;f ⋅ρ g⋅βc ps;k;f⋅Ac ps;k;f⋅ Y eq Xc ps;i;k;f ;Tc ps;i;k;f −Y s dξ e e x q c u h a a ti n o g n e s o re f q m ui o re is d tu f r o e r b c e a t l w cu e l e a n tio d n iff o e f re h n e t at cla a s n s d es m i a s ss ne t g r l a e n c s t f e e d r . c A o l - l
(cid:1) (cid:3) h (cid:1) (cid:3) ið8Þ efficientsaresummarizedintheAppendixA.

136 I.Alaatharetal./PowderTechnology238(2013)132–141
Table2 Table4
Thenormalizeddryingcurveofγ-alumina[1]. OperatingparametersforthemeasurementsofBurgschweigerandTsotsas[1].
η 0 0.0086 0.2248 0.3721 0.6124 0.805 1 Parameter Exp.1 Exp.2 Exp.3 Exp.4 Exp.5
ν_ (η) 0 0.445 0.683 0.8 0.909 0. 1
M _bed,g 870 880 980 990 1020
Mp,g/s 0.48 0.85 1.21 1.45 1.69
X _in,kg/kg 0.614 0.663 0.611 0.635 0.635
Mg,g/s 39 38 38 38 38
Table3 Tg,in,°C 80 80.5 79.7 79.7 79.9
Thesorptionisothermofγ-alumina[1]. Yin,g/kg 5.32 5 3.07 6.33 6.33
φ[%] 0 5 10 65 75 80.5 93 100
Xeq 0 0.027 0.04 0.09 0.12 0.2 0.67 0.8
Table5
Itisworthmentioningthattheheatandmasstransfercoefficient
OperatingparametersforthemeasurementsofKettneretal.[7].
and the gas properties such as density, viscosity and thermal
Parameter Exp.1 Exp.2
conductivity are calculated as a function of the actual temperature
and pressure of the drying gas at each height. The new model M _bed,g 698 698
furthermoreconsiderschangesofthebedcrosssectionwithheight
M _p,g/s 1.45 1.45
(e.g.awideningofthebed)andthechangeofgasvelocityresulting
Mg,g/s 36.1 36.1
fromtheevaporatedvapormassfluxfromsolids.
Tg,in,°C 80 60
3.Modelapplication
3.1.Modelvalidation
Thesystemofdifferentialequationsasdescribedabovehasbeen Inafirststepthemodulehasbeenvalidatedwithmeasureddata
implementedasaunitmoduleintotheflowsheetsimulationprogram
by Burgschweiger and Tsotsas [1]. Burgschweiger and Tsotsas [1]
SolidSim[5],whichprovidestheuserinterfaceforthedefinitionof
carriedoutexperimentsinacontinuousfluidizedbeddryerwith150
the feeds, i.e. the gas and the solids feed and which especially
mm inner diameter with γ(cid:3)Al
2
O
3
spheres as bed material. The
providesthemodulewithallsolidsandgaspropertiesasfunctionof
particleshadameansurfacediameterd p¼1:8mmandanapparent
temperatureandpressure.Thisallowstoeasilyapplythesystemtoa densityρ ¼1040kg=m3.Thecriticalmoisturehadbeendetermined
wide range of solids, liquids and gases. Furthermore, it allows to p
connect the fluidized bed dryer with other unit modules to
withX cr¼0:2 kg=kg,thenormalizeddryingcurveandthesorptive
isothermasdeterminedbyBurgschweigerandTsotsas[1]aregiven
investigatetheinteractionofdifferentunitoperations.Ascreenshot
inTables2and3,respectively.
ofSolidSimwiththefluidizedbeddryermoduleisshowninFig.4.
The results of the simulation of the tests carried out by
The following strategy has been used to solve the system of
BurgschweigerandTsotsas[1]aregiveninFig.5togetherwiththe
equationsnumerically:
measurements. For the simulations the average values for the
operating parameters as given by Burgschweiger and Tsotsas [1]
• Theresidencetimecoordinateτhasbeendiscretizedgeometrically havebeenused;thevaluesfortheexperimentsaregiveninTable4.
intonclasses,andintegratedbytheEulermethod. In the diagram the averaged moisture content of the solids at the
• Forthecalculationofthegasmoistureandtemperatureprofilesthe outletisplottedvs.thethroughput.Thereisaverygoodagreement
dryer was divided into q finite height elements. Fourth-order betweenmeasurementsandsimulation.
Runge–Kutta algorithm has been used to solve the height For the module developed in this work the agreement even
integration. slightlybetterthanforthesimulationbyBurgschweigerandTsotsas
• l particle size classes have been usedto describethe particle size [1], even though both models are identical for the steady state
distribution. operationwithmono-sizedparticles.
• Theinletmoisturecontentcoordinatehasbeendiscretizedintor Thedifferencebetweenthetwomodelsresultsprobablyfromthe
classes. different calculation of the physical gas properties: while Burgsch-
weiger and Tsotsas [1] used the properties at average temperature
The user can change n,q,l and r depending on the desired and pressure as fixed values throughout the model, the physical
accuracyandcalculationtime. properties within the SolidSim module are always calculated
Fig.6.Influenceofthegastemperatureonthemoisturedistribution.
Fig.5.Averagemoisturecontent. MeasurementsbyKettneretal.[7].

I.Alaatharetal./PowderTechnology238(2013)132–141 137
Table6
OperatingparametersforthemeasurementsofPeglowetal.[10].
Symbol Exp.1 Exp.2 Exp.3
M _bed,g 982 820 976
M _p,g/s 1.7 1.3 1
Mg,g/s 125 125 125
Tg,in,°C 80 80 80
according to the actual local temperature. It has to be emphasized,
thattherewasnofurtherfittingofthemodeltothemeasurements.
Fig.8.Particlesizedistribution.
3.2.Moisturedistribution
flow of air was set to 20kg/s, corresponding to a superficial gas
velocityatthegasdistributorlevelof2m/s.
Inadditiontothemeasurementoftheaveragemoisturecontent
To study the influence of the particle size a particle size
Kettneretal.[7]andPeglowetal.[10]measuredalsothemoisture
distribution as shown in Fig. 8 has been assumed. In Fig. 9 the
distribution. They used the same experimental setup and a similar
resultingmoisturedistributionduetotheresidencetimedistribution
materialasBurgschweigerandTsotsas[1].
areshownforthreedifferentparticlesizes.
TheoperatingparametersfortheexperimentsbyKettneretal.[7]
As expected the particle size has a significant influence on the
aregiveninTable5.Themeasurementsandtherespectivesimulation
drying process. The remaining moisture content of coarse particles
results are shown in Fig. 6. It can be noted, that with the higher
afterdryingishigherthanforthefines.Theaveragemoistureofeach
temperature the moisture distribution is shifted to the left, i.e. the
classislistedinTable7.Duetothelargervolumespecificsurfacearea
producthas a lower moisture contentat the outlet. The agreement
ofthefinesthemoisturecontentofthefinesislowerthanthatofthe
betweenthesimulationandexperimentsforthelowertemperature
coarse particles even though the mass transfer coefficients are
of60°Cisverygood.Forthehighertemperatureof80°Cthereisa
smallerforthefines.
slightoverestimationofthemoisture,thiscanbeexplainedwiththe
fact that the temperature dependence of the sorption isotherm has
notbeentakeninaccount.
3.4.Influenceofinletmoisturecontent
SimilarmeasurementshavebeencarriedoutbyPeglowetal.[10],
whovariedthesolidsthroughputthroughthecontinuousdryer.The Another simulation run was made to study the influence of a
operating parameters are given in Table 6. The results of these
moisturedistributionattheinletofthedryer.Thiswillforexample
measurementsandthesimulationresultsaregiveninFig.7.Ascanbe
occurfortowdryersinseries.Theparticlesizewassetto1.8mmand
expected for higher solids throughput the moisture content of the
theinletmoisturedistributionasshowninFig.11.
solidsattheoutletincreases,i.e.themoisturedistributionisshiftedto Similar to the size distribution influence the inlet moisture
the right. The minimal moisture content is lower for the low
distributionplaysanimportantroleinthedryingprocessasshown
throughputs, since the outlet gas temperature and the solid
inFig.10.InFig.10atheactualvaluesofthemoisturedistributionare
temperature in the bed are higher and therefore the equivalence
plotted,inFig.10bforcomparisonthedistributionofthenormalized
moi
A
s
g
tu
a
r
in
e
,
c
t
o
h
n
e
te
a
n
g
t
r
i
e
s
e
l
m
ow
en
e
t
r.
between simulation and measurement is
moisture content, defined as X−X
eq
/X ini−X
eq
, is shown. It can be
noted, that with higher inlet moisture content the moisture
goodforallthreemassflows,eventhoughitslightlydecreaseswith
distributionisshiftedtotheright,i.e.theproducthashighermoisture
increasingsolidsthroughput.
contentattheoutlet.Theminimalmoisturecontentisthesameforall
classes of the inlet moisture content, because the gas temperature
3.3.Influenceofparticlesize andhumidityarethesameinthebed,andtheparticleswiththelong
residencetimewillinanycasedrydowntotheequilibriummoisture.
Afterthemodelhasthoroughlybeenvalidatedwiththemeasure- The maximal moisture content of each class is the inlet moisture
mentsavailableintheliteratureithasbeenappliedforthesimulation contents. These are particles which have a residence time close to
ofsolidswithparticlesizeandinletmoisturedistributions. zeroandwhichwillnotbedriedatall.
For all the following simulations a fluidized bed dryer with a Tostudytheinfluenceofamoisturedistributionattheinletofthe
cross-sectional area of 10 m2 has been assumed. Dry air with a dryer on the dryingprocess in Fig. 10 the results calculated of two
temperatureattheinletof80 wasusedasfluidizationgas.Themass differentcasesareshown.Forbothcasestheaveragemoistureofthe
Fig.7.Influenceofthesolidsthroughputonthemoisturedistribution.
MeasurementsbyPeglowetal.[10]. Fig.9.Influenceofparticlesizeandsolidsthroughputonmoisturedistribution.

138 I.Alaatharetal./PowderTechnology238(2013)132–141
Table7
Theaveragemoisturecontentofeachsizeclass.
dpmm0.625 0.875 1.125 1.375 1.625 1.875 2.125 2.375 2.625 2.875
Xav 0.358 0.37 0.378 0.384 0.39 0.395 0.4 0.404 0.408 0.412
feed is the same, but for case 1 the moisture at the inlet has a
distributionasshownasdottedlineinFig.11whileforcase2allthe
particles have the same moisture content. Fig. 11 shows the
calculatedproductmoisturedistributionwhichiscalculatedfortwo
different cases; case 1 is calculated regarding to a distributed
moisture content at the inlet (solid line) and case 2 is calculated
regarding to a constant mean moisture for the same inlet (dashed Fig.11.Influenceofaninletmoisturedistributionontheproductmoisturedistribution.
line).Itisnoticeablethatthereisnotonlyadifferencebetweenthe
productmoisturedisributionforthetwocases,butalsotheaverage
moisture with 0.29kg/kg for the first case and0.26kg/kg for the
secondcasediffers. aluminathedatabyBurgschweigerandTsotsas[1]areusedasinthe
simulationsbefore.
For the simulations a monosized mixture of 30% in mass
3.5.Simulationofmixtureoftwosolids
α-aluminaand70%inmassγ-aluminawasused.Forbothtypesthe
same particle size of 1.8mm and the same inlet moisture X of
Inordertocommencethissimulationamixtureoftwodifferent ini
0.3kg/kgwasset.
typesofaluminawasassumed.Inadditiontoγ-aluminaasusedfor
InFig.12themoisturecontentasfunctionofresidencetimefor
the previous simulations, α-alumina was used as a second type of
solid. The apparent density of α-alumina is with 2400 kg=m3
α-alumina and γ-alumina is shown. γ-Alumina is dried faster than
significantly higher than that of γ-alumina (1040 kg=m3). The α-aluminaatthebeginningofthedryingprocess.Thisisduetothe
lowerdensity,whichresultsinalargersurfaceareapermassunitof
differenceisduetothemicrocrystalstructureinbothtypes,α-type
solidsthanfortheα-alumina.But,duetothesmallerporosityofthe
hasacoarsecrystalstructurewithasmallamountofbigpores,while
α-alumina,onlyasmallamountofwaterhastobeevaporatedduring
theγ-typehasmanysmallporeswithalargerinternalsurfacearea.
theseconddryingperiod.Thereforeα-aluminahasalowermoisture
Thesedifferencesininternalstructureinadditiontothedeformation
contentthantheγ-aluminaafteraresidencetimeofmorethan300s.
of the crystals will lead to differences in their behavior during the
InFig.13thecorrespondingmoisturedistributionsareshown.Forthe
dryingprocess.
α-aluminaabout60%inmassofthematerialarenearlycompletely
Withrespecttothedryingresistanceintheseconddryingperiod
dried downto about 0.006kg/kg but on the other hand more than
it is assumed, that α-alumina has a negligible inner transport
resistance,thusthenormalizeddryingrateν_ issetto1.Thesorption 30%ofthematerialhasaremainingmoisturecontentofmorethan
0.1kg/kg.
isotherm after Greonewold [4] is used and listed in Table 8. For γ-
For γ-alumina there is no material with a moisture less than
0.006kg/kg,mostofthematerialhasamoistureof0.02to0.05kg/kg
andonly15%amoisturegreaterthan0.1kg/kg.Intotalthisgivesa
moisturecontentof0.079kg/kgfortheα-aluminaandof0.056kg/kg
fortheγ-alumina.
4.Simulationofanelongatedfluidizedbeddryer
To reduce the width of the residence time distribution and
thereforethewidthofthemoisturedistributionelongated,channel
shapedfluidizedbeddryersassketchedinFig.14areoftenusedin
industry.Herethesolidsareconvectivetransportedalongthelength
ofthefluidizedbedchannel.Thedispersivemixingcanbemodeled
usingthedispersiontheoryFyhretal.[3].Inthiscaseasuperposition
ofadispersivemixingwithaconvectivetransportissimulated.Such
a superposition of dispersion and convection may as a first
approximation be modeled as a cascade of stirred tanks [2]. This
approximationisalsomadeintheSolidSimmoduleofthefluidized
beddryertodescribetheinfluenceoftheconvectivetransportonthe
moisturedistributionoftheproduct.Theresidencetimedistribution
dependsforsuchacascadesolelyfromthenumberofstirredtanksK
in the cascade and the average residence time τ(cid:2). For K→∞ the
cascadeofstirredtankbecomespureplugflowwithoutanymixing.
Table8
Thesorptionisothermofα-aluminaafterGroenewold[4].
φ[%] 0 5 10 65 75 80 93 100
Fig.10.Influenceofaninletmoisturedistribution,a)actualmoisture;b)normalized
moisture.
Xeq 0 0.005 0.01 0.011 0.012 0.02 0.025 0.35

I.Alaatharetal./PowderTechnology238(2013)132–141 139
Fig.12.Themoisturecontentasafunctionofresidencetime.
In general the frequency distribution of the residence time for a
cascadeofstirredtankscanbecalculatedbyCunäusetal.[2]
Fig.14.Channelshapedfluidizedbeddryer.
nðτÞ¼ τ(cid:2) ⋅ðK 1 −1Þ!⋅ðτ=τ(cid:2)ÞK−1 ⋅expð−τ=τ(cid:2)Þ ð16Þ
themodelhasbeenextendedbyasimpleapproachtosimulatethe
Forthefluidizedbedchannelthenumberofstagesinthestirred drying in an elongated fluidized bed dryer. The model has been
tankcascadeisroughlyestimatedbytheaspectratiooflength/width includedintotheframeworkofthestationaryflowsheetsimulation
ofthechannel,i.e.thelongerandnarrowerthechannelis,themore system SolidSim which allows the application for a wide variety of
dominatestheconvectioncomparedtomixing. solids,gasesandliquids,sincethephysicalpropertiesareprovidedby
Forthesimulationofanexistingfluidizedbeddryerthenumberof theframework.
stirredtanksshouldbeadjustedbyfittingtomeasureddata.
To study the influence of the aspect ratio (AR) on the drying
processfivedifferentdryershavebeensimulated,allhavingacross- Listofsymbols
sectional area of 10m2, only the aspect ratio has been changed to A Surfacearea[m2]
valuesof1,2,3,4and5correspondingto1,2,3,4or5stagesinthe c Specificheatcapacity[J/kgK]
stirredtankcascade.Asfortheprevioussimulationthegasflowwas d Diameter[m]
20kg/sandtheinlettemperatureofthegas80°C. h Specificenthalpy[J/kg]
TheresultsofthesesimulationsareshowninFig.15.Foreachfive Δh Specificenthalpyofevaporation[J/kg]
aspectratiosthemoisturedistributionisshown.Clearlythepositive H _ v Enthalpyflowrate[J/s]
influenceofthesuperposedconvectivetransportofthesolidscanbe M Mass[kg]
recognized. Not only that the moisture distribution becomes M _ Massflowrate[kg/s]
narrowerwhentheaspectratioARisincreased,butalsotheaverage N Numberofdensity[−]
moisturecontentofthesolidsattheoutletisreduced. Q _ Heatflowrate[W]
While these simulations give already a good indication of the ΔQ
3,k
Massfractionofsolidsinparticleclasssizek[−]
influenceofthedryergeometry,theresultsstillhavetobevalidated ΔQ
3,f
Massfractionofsolidsinmoistureclasssizef[−]
bymeasurements. T Temperature[K]
v Ratioofbubbletototalgasflowrate[−]
5.Conclusions u Velocity[m/s]
X Particlemoisturecontent[kg /kg]
w s
Based on a model by Burgschweiger and Tsotsas [1] a SolidSim X Particleequilibriummoisturecontent[kg /kg]
eq w s
moduleforthesimulationoffluidizedbeddryershasbeendeveloped. X Criticalmoisturecontent[kg /kg]
cr w s
ThemodelbyBurgschweigerandTsotsas[1]hasbeenextendedby Y Gasmoisturecontent(drybasis)[kg /kg ]
w g
the consideration of particle size and solid inlet moisture content Y Gasequilibriummoisturecontent[kg /kg ]
eq w g
distributionsanddryingofmixturesofdifferentsolids.Furthermore z Bedheightcoordinate[m]
Fig. 15. Influence of aspect ratio AR of the fluidized bed dryer on the moisture
Fig.13.Themoisturedistributionofamixtureαandγ-alumina. distribution.

140 I.Alaatharetal./PowderTechnology238(2013)132–141
Greekletters Le¼ λ g
α Heattransfercoefficient[W/m2] c g ρ g δ g
β Masstransfercoefficient[m/s]
φ Relativehumidity[−]
1
η Normalizedparticlemoisturecontent[−] m¼
3
ρ Density[kg/m3]
ν _ Normalizedsingleparticledryingrate[−]
τ Residencetime[s]
A.3.Heattransferbetweentheparticlesandthewall
τ(cid:2) Meanresidencetime[s]
ξ Normalizedbedheight[−] Theheattransfercoefficientbetweentheparticlesandthewallis
calculatedafterMartin[9].
Subscripts
b Bubble Nu ¼ α pw d p
f Indexofdiscretizedinletmoisturecontentcoordinate pw λ g
i Indexofdiscretizedresidencetimecoordinate
k Indexofdiscretizedparticlesizecoordinate
g
mf
G
M
a
i
s
nimalfluidization
Nu
pw
¼ð1−εÞZ 1−e−N
p Particle (cid:1) (cid:3)
s Suspension
Withthecoefficients
A A. p 1 p .M en a d s i s x a A ndheattransferbetweenparticlesandsuspensiongas Z¼ 1 6 ρ p c λ p g ;wet v u u 5 ffiffiffiffiffi g ffi 1 ffiffi d ffi − ffi 3 p ffiffi(cid:1)ffi ε ffiffi ε ffi m ffiffi − ffi f ffiffiffi ε ffi ð ffiffi m 1 ffiffiffi f − ffi(cid:3)ffiffiffiffi ε ffiffi Þ ffiffi
u
t (cid:1) (cid:3)
Nu
MassandheattransferbetweenparticlesandsuspensiongasafterGnielinski[] N¼ p C wð Z maxÞ
forfixedbed K
Re¼R ε e m m f f Re¼R ε e m m f f C K ¼2:6
Sc¼ νg Pr¼νgcgρg
δw;g λg
Shlam¼0:664Re1 2Sc1 3 Nulam¼0:664Re1 2Pr1 3 ThemaximalNusselt-numbercanbecalculatedfrom
S
S
h
ht
p
ur
¼
¼
2
1
þ
þ2:4 0 4
S
: 3 0
h
R 3 e 7
2 la
− R
m
0 e :1 0:
þ(cid:7)
8S S c c
S
2 3
h
−
2 t
1
u (cid:8) r
N
N
u
u
t
p
ur
¼
¼
2
1
þ
þ2:4 0 4
N
: 3 0 R 3
u
e 7 −
2 l
R
a
0
m
e :1 0:
(cid:7)
8
þ
P P r r 2 3
N
−
u
1
2 t (cid:8) ur
Nu
pwðmaxÞ
¼4
(
1þ
d
2
p
l
!
ln
(cid:5)
1þ d
2
p
l (cid:6)
−1
)
qffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi qffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Shps=[1+1.5(1−εmf)]Shp Nups=[1+1.5(1−εmf)]Nup
with
BackmixingeffectafterGroenewoldandTsotsas[4]
S sh h 0 p 0 p s s ¼ ¼ R β A e p = δ 0 sd F S p cln (cid:1) 1þS R hp e s 0 A S = c F (cid:3) N N u u 0 p 0 p s s ¼ ¼ R α A e p λ = s 0 g d F P p rln (cid:1) 1þN R u e ps 0 A P = r F (cid:3) l¼2 (cid:5) γ 2 −1 (cid:6) rffi 2 ffiffi π ffiffiffiffi R e ffiffiffi T ffiffiffiffi M ffiffi e ffiffiffigffiffip 2c g− λ R g =M g
(cid:1) (cid:3)
e e
lg 1 −1 ¼0:6−
10
T
0
g
0Kþ1
γ C
Where Re Reynolds-Number, Sc Schmidt-Number,ε mf minimal (cid:5) (cid:6) A
fluidizationvelocity,PrPranntl-Number.
C ¼2:8
A
A.2.Massandheattransferbetweensuspensiongasandbubblephase
wherelisthemodifiedfreepathofthegasmolecules.
TheNumberofTransferUnit(NTU)isgivenas
References
ρ :β A [1] J. Burgschweiger, E. Tsotsas, Experimental investigation and modelling of
NTU sb ¼ g M _ sb g sb: C co h n e t m in i u ca o l u E s n fl gi u n i e d e iz r e in d g b S e c d ien d c r e yi 5 n 7 g ( u 2 n 00 d 2 er )5 s 0 te 2 a 1 d – y 5 - 0 st 3 a 8 t . e and dynamic conditions,
[2] U.Cunäus,M.Peglow,E.Tsotsas,Applicationofpopulationbalanceequationsfor
continuousfluidizedbeddrying,17thInternationalDryingSymposium—IDS
ItisassumedthatNTUincreaseslinearlywiththeheight,forabed 2010,Magdeburg,Germany,2010.
[3] C.Fyhr,I.C.Kemp,R.Wimmerstedt,Mathematical modelling offluidisedbed
height of 5cm a value of 1 was set Groenewold and Tsotsas [4],
dryers with horizontal dispersion, Chemical Engineering and Processing 38
therefore (1999)89–94.
[4] H. Groenewold, E. Tsotsas, A new model for fluidized bed drying, Drying
Technology15(1997)1687–1698.
NTU ¼NTU0: L bed [5] E.-U.Hartge,M.Pogodda,C.Reimers,D.Schwier,G.Gruhn,J.Werther,Flowsheet
sb sb 50mm simulationofsolidsprocesses,KONAPowderandParticle(24)(2006)146–158.
[6] K. Hilligardt, J. Werther, Local bubble gas-holdup and expansion of gas/solid
fluidizedbeds,GermanChemicalEngineering9(1986)215–221.
α sb A
_
sb¼ ρ g β
_
sb A sbLe1−m [7] C
fl
.
ui
K
d
e
iz
t
e
tn
d
er
b
,
ed
M.
dr
P
y
e
i
g
n
l
g
o
,
w
P
,
ro
T
c
.
ee
M
d
e
in
tz
g
g
s
er
o
,
f
E
th
.
e
Ts
1
o
5
t
t
s
h
as
I
,
n
D
te
i
r
s
n
tr
a
i
t
b
i
u
o
t
n
e
a
d
lD
p
r
r
y
o
i
d
n
u
g
ct
Sy
q
m
ua
p
l
o
it
s
y
ium
in
c M M
g g g 2006,Budapest,Hungary,2006.

I.Alaatharetal./PowderTechnology238(2013)132–141 141
[8] B. Kozanoglu, J. Martinez, S. Alvarez, J.A. Guerrero-Beltrán, J. Welti-Chanes, [11] E.Tsotsat,A.S.Mujumdar(Eds.),ModernDryingTechnology,ProductQualityand
Influenceofparticlesizeonvacuum-fluidizedBeddrying,DryingTechnology30 Formulation,Volume3,Wiley-VCH,Weinheim,2011.
(2)(2012)138–145. [12] D.A. van Meel, Adiabatic convection batch drying with recirculation of air,
[9] H.Martin,VDI-Wärmeatlas,7ed.,VDI-Verlag,1994,pp.Mf1–Mf8,ChapterMf. ChemicalEngineeringScience9(1958)36–44.
[10] M.Peglow,U.Cunäus,C.Kettner,T.Metzger,E.Tsotsas,Apopulationbalance
approachforcontinuousfluidizedbeddryers,6thEuropeanCongressofChemical
Engineering(ECCE-6),Copenhagen,Number2215,2007.
