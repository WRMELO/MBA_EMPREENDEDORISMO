# CFD_simulation_of_a_circulating_fluidize

**Fonte**: CFD_simulation_of_a_circulating_fluidize.pdf  
**Data de conversão**: 2025-07-30 15:10:27  
**Origem**: base_relevantes

---

Particuology7(2009)283–296
ContentslistsavailableatScienceDirect
Particuology
journal homepage: www.elsevier.com/locate/partic
CFD-simulation of a circulating fluidized bed riser
Ernst-UlrichHartge ,LarsRatschow,ReinerWischnewski,JoachimWerther
∗
Hamburg-UniversityofTechnology,InstituteofSolidsProcessEngineeringandParticleTechnology,D-21071Hamburg,Germany
a r t i c l e i n f o a b s t r a c t
Articlehistory: Inthecurrentwork,amodelofthefluidmechanicsintheriserofacirculatingfluidizedbed(CFB)has
Received3April2009 beenimplementedusingcomputationalfluiddynamics(CFD).Themodeldevelopedshallbeusedin
Accepted11April2009 futureasthebasisof3D-reactormodelforthesimulationoflargescaleCFBcombustors.Thetwo-fluid
model(TFM)approachisusedtorepresentthefluidmechanicsinvolvedintheflow.Thecomputational
Keywords: implementationisaccomplishedbythecommercialsoftwareFLUENT.Differentclosureformulationsare
Circulatingfluidizedbed testedonasimplifiedgeometry.Twodifferentturbulenceformulations,namelytheswirlmodifiedRNG
Two-fluidmodel
k–εmodelandtheRealizablek–εmodel,aretestedincombinationwithtwodifferentapproachestosolid
EMMSmodel
phaseturbulence,namelythedispersionandperphaseapproach.Onefocusofthecurrentworkisputon
Dragcorrelations
thestudyofdifferentdragcorrelations.BesidesthedragcorrelationsbySyamlaletal.[Syamlal,M.,Rogers,
W.,&O’Brien,T.J.(1993).MFIXdocumentationtheoryguide.TechnicalReportDOE/METC-94/1004,U.S.
DepartmentofEnergy(DOE).MorgantownEnergyTechnologyCenter:Morgantown,WV]andGidaspow
[Gidaspow,D.(1994).Multiphaseflowandfluidization.NewYork:AcademicPress]theEMMSmodelhas
beenusedtodeterminethemomentumexchangebetweenthetwophases.Theresultingformulationis
thenusedtosimulatea1-m 0.3-mcoldCFBsetupandisvalidatedbyexperimentalresults[Schlichthärle,
×
P.(2000).Fluiddynamicsandmixingofsolidsandgasinthebottomzoneofcirculatingfluidizedbeds.
Unpublisheddoctoraldissertation,TechnischeUniversitaetHamburg-Harburg,ShakerVerlag:Aachen].
©2009ChineseSocietyofParticuologyandInstituteofProcessEngineering,ChineseAcademyof
Sciences.PublishedbyElsevierB.V.Allrightsreserved.
1. Introduction vidually, is often applied to dilute systems using the trajectory
method (e.g. Crowe, Sommerfeld, & Tsuji, 1997). By this method
Today circulating fluidized beds (CFBs) are widely applied in thetrajectoriesofindividualparticlesorofparticlesrepresenting
industryfordifferentprocesses,e.g.ascombustorsorforhetero- a large number of individual particles are computed, neglecting
geneouslycatalyzedreactions.Theaimofthecurrentworkisto particle–particlecollisions.Forhighersolidsconcentrationsasthey
implementandtovalidateacomputationalfluidmechanics(CFD) existinaCFBparticle–particlecollisionsdominatethetransport
model,whichshallbeapplicabletolargeCFBs.Thefinalaimistouse anddispersionofmomentumandhavethereforetobetakeninto
thisCFD-modelasthebasisforthefull3D-simulationoflargescale account.Thismaybedonebythediscreteparticlemodeling(DPM)
CFBcombustors.TodaysuchCFBcombustorshavedimensionsofup (e.g.Deen,vanSintAnnaland,vanderHoef,&Kuipers,2007).By
to10m 20m 40mandevenlargeroneswillbebuiltinthenear DPMthetrackofeachindividualparticleiscomputed,collisions
× ×
future.Theselargedimensionstogetherwiththeadditionalsimu- betweenindividualparticlesarepredictedandtheirinfluenceon
lationofthecombustionprocessandtheheattransportrequireto theparticletracksistakenintoaccount.Thesecalculationsneeda
useaCFD-modelwhichisassimpleaspossibleandwhichcanbe lotofcomputingresourcesandarethereforelimitedtoanumber
solvedwithsufficientaccuracyonaverycoarsegrid.Thepresent ofabout106particlestoday.ThereforeDPMcannotbeusedyetfor
workisafirststeptodevelopsuchaCFB-modelandtovalidateit the simulation of large scale CFBs with more than 1012 particles
withdatafromapilot-scalecoldCFB-testrig. inside.
Ingeneraltwodifferentapproachesmightbeusedforthesimu- NowadayscommonlytheEulerianapproachisusedforthesim-
lation of gas–solid flows, namely the Lagrangian or the Eulerian ulationoflargescaleCFBs.IntheEulerianapproachortwo-fluid
approach. The Lagrangian approach, which treats particles indi- model both the gas and the granular phases are treated as fully
interpenetrating continua. The equations used are a generaliza-
tionoftheNavier–Stokesequationsforinteractingmediums(e.g.
Goldschmidt,2001).Thesolidparticleswithinthesolidphaseare
∗ Correspondingauthor.
E-mailaddress:Hartge@tuhh.de(E.-U.Hartge). generallyconsideredtobeidenticalhavingarepresentativediam-
1674-2001/$–seefrontmatter©2009ChineseSocietyofParticuologyandInstituteofProcessEngineering,ChineseAcademyofSciences.PublishedbyElsevierB.V.Allrightsreserved.
doi:10.1016/j.partic.2009.04.005

284 E.-U.Hartgeetal./Particuology7(2009)283–296
to describe the momentum exchange between the two phases.
Nomenclature Agrawal,Loezos,Syamlal,andSundaresan(2001)reportedthatthe
solidstresspredictedbyKGTFposednoimportantcontributionto
C dragcoefficient
D theoverallstructureoftheflow,whereastheclusteringeffectof
ds particlediameter,m
theparticles–andhencetheassociateddrag–hadthedominant
ess particle–particlerestitutioncoefficient
roleintheoutcomeoftheirsimulation.
ew particle–wallrestitutioncoefficient
Theinterphasemomentumtransferbetweenthephasesisone
g gravitationalaccelerationvector,m/s2
ofthemostsignificanttermsinthegasandsolidphasemomen-
g radialdistributionfunction
0 tumequations.Thismomentumexchangeisrepresentedbyadrag
Js fluctuatingvelocity-forcecorrelation,kg/m3s
force.Thedragforceonasinglesphericalparticleiswellcorrelated
k diffusioncoefficientofgranulartemperature,kg/ms
 forawiderangeofReynoldsnumbers(Bird,Stewart,&Lightfoot,
Gs externalsolidsreflux,kg/m2s
2001).However,thesecorrelationslosetheirvalidityinasolid–gas
p Pressure,Pa
suspensionsincethedragforceononeparticleisaffectedbythe
ps solidspressure,Pa
presenceofothers(Taghipour,Ellis,&Wong,2005).
Res particleReynoldsnumber
To cover a broad range of solids concentrations for CFD-
t time,s
simulationsacombinationofthecorrelationsbyErgun(1952)and
u superficialgasvelocity,m/s
0 WenandYu(1966)isquiteoftenused.Thesecorrelationswereorig-
u minimumfluidizationvelocity,m/s
mf inallydevelopedonthebasisofexperimentswithhomogeneous
systems. However the distribution in fluidized beds is heteroge-
Greeksymbols
neous.
˛i volumefractionofphasei
CFD-simulations with these or similar drag correlations are
˛s,max maximumpackinglimit
generally in good agreement with the experimental findings for
ˇ interphasemomentumexchangecoefficient,
the upper dilute region of the riser of CFBs. However, in most
kg/m3s
cases the simulations fail to describe the lower part of the riser,
εs solidsvoidfraction
where a region with high solids concentrations is observed in
collisionaldissipationofenergy,kg/m3s
 mostexperiments.TheCFD-simulationsgenerallyunderestimate
s solidsbulkviscosity,Pas
thesolidconcentrationinthisregion.ForexampleQi,You,Boemer,
i viscosityofphasei,Pas
andRenz(2000)reportedthatthedragcorrelationsderivedfrom
i densityofphasei,kg/m3
Ergunequationcausedarapidcarryoverofsolidsandasaresult,
 granulartemperature,m2/s2
the simulated flow became rather dilute as a whole. The reason
 velocityvectorofphasei,m/s
i for this behavior is the monotonous increase of the drag with
stresstensorforphasei,N/m2
i increasingsolidsconcentrationwhichisincontrasttotheexper-
imentallyobservedreductionofthedragduetotheformationof
Subscripts
clusters.
col collisional
Beetstra,vanderHoef,andKuipers(2006)haveshownbyLat-
dil dilute
tice/Boltzmannsimulationsthatthedragofsuspensionsdepends
fr frictional
strongly on the arrangement of the particles and therefore the
g gasphase
structure of the suspension should be taken into account in the
kin kinetic
calculationofthemomentumexchange.Somerecentstudiestake
max maximum
thelocalheterogeneityofthegas–solidsflowinaCFBintoaccount
mf minimumfluidization
forthecomputationofthedragforce.Firstapproachestotakethe
s solidsphase
structureoftheflowonasub-gridscaleintoaccounthavebeen
w wall
madebyKallio(2006),Yang,Wang,Ge,andLi(2003)andQi,Li,
Xi,andYou(2007).Thelattertwocomputedthedragbasedonthe
EMMStheory(Li&Kwauk,1994).TheworksofYangetal.(2003)
eteranddensity.Tosimulateparticlesizedistributionsmorethan andQietal.(2007)showpromisingagreementwiththeexperi-
onepseudofluidhastobeusedforthesimulationofthesolidphase, mentalresults,whereasthesuccessoftheworkbyKallio(2006)
eachofthesepseudofluidsrepresentingoneparticlesizeclass.In isvalidatedonlytrend-wise,sinceanexperimentalcomparisonis
thecurrentworkonlyonepseudofluidhasbeenused. lacking.
Amongthevariousattemptstoformulatetheparticulateflow,
thekinetictheoryofgranularflow(KTGF)hasfoundthewidestuse.
2. Modeling
Thistheoryisbasicallyanextensionoftheclassicalkinetictheoryof
gasesdescribedbyChapmanandCowling(1970)todenseparticu-
The simulations were performed using FLUENT 6.3. All simu-
lateflows,describingtheparticle–particlecollisions(Goldschmidt,
lations have been done in three-dimensions. In the following a
2001). The random movements and the nearly elastic collisions
shortoverviewonthegoverningequationsisgiven.Thecontinu-
of the solid particles make the kinetic theory ideally suited to
ityequationforthegasandsolidphasesaregiveninthefollowing
describegranularflows.Theapproachusesaoneequationmodelto
equations:
describetheturbulentkineticenergyoftheparticle–introduced
with the concept of granular temperature – and assumes either ∂
aMaxwellianoranon-Maxwelliandistributionfortheparticles, ∂t
(˛gg)
+∇·
(˛gg g)
=
0, (1)
considering both dilute and dense cases (Benyahia, Arastoopour,
Knowlton,&Massah,2000).
∂
∂
t
(˛ss)
+∇·
(˛ss v s)
=
0. (2)
Interparticlecollisionsandthesolidphasestressisapparently
nottheonlychallengethegas–solidflowmodelsarefacing.Another Intheseequationsparameters˛i ,i and
i
representthevolume
modeling challenge is the use of appropriate drag correlations fraction,densityandvelocityofphasei,respectively.

E.-U.Hartgeetal./Particuology7(2009)283–296 285
Following are the momentum conservation equations for gas The RNG formulation with swirl correction is chosen as another
andsolidphases: candidatetobetestedhere.Thoughaswirldominatedflowisnot
observed within the CFB riser, the applied swirl modification is
∂ ∂ t (˛gg v g) +∇· (˛gg v g v g) knowntoyieldabetteraccuracyinthecurvedstreamlineswhich
areobservedattheinletandexitgeometriesoftheriser.Thetrans-
=− ˛g∇ p +∇· (cid:2) g+ ˛ggg + ˇ(v s− v g), (3) portequationsassociatedtotheturbulenceparameterskandεare
verysimilartothoseinthestandardmodel,asshownbelow:
∂ ∂ t
=
(˛
−
s
˛
s
s
v
∇
s)
p
+
−
∇
∇
·
p
(
s
˛
+
s
∇
s v
·
s
(cid:2)
v s
s
)
+ ˛ssg + ˇ(v g− v s). (4) ∂
∂
t
(mk)
+∇·
(m v mk)
=∇·
(˛
k
t,m∇ k)
+
G
k,m−
mε, (13)
e
In
xch
th
a
e
n
s
g
e
ec
e
o
q
e
u
ffi
at
c
i
i
o
e
n
n
s
t,w
ˇ
hi
r
c
e
h
pr
h
e
a
s
s
e
t
n
h
t
e
s
s
t
a
h
m
e
e
i
v
n
a
t
l
e
u
r
e
p
i
h
n
as
b
e
oth
m
e
o
q
m
ua
e
t
n
i
t
o
u
n
m
s. ∂
∂
t
(mε)
+∇·
(m v mε)
Whenmultipliedbytheslipvelocitybetweenthetwophases,it
ε
yields the interaction force between the phases. In addition, the =∇· (˛εt,m∇ ε) +k (C1ε G k,m− C2ε mε) − Rε. (14)
term(cid:2) standsforthestresstensorsforthegasandsolidsphases.
i
Thesetermsaredefinedasfollows:
The terms ˛
k
and ˛ε are the inverse effective Prandtl numbers,
whichareobtainedby
g = ˛gg( ∇ v g+∇ vT g ) −3 2 ˛gg( ∇· v g)I, (5) ˛ε= ˛ k , (15)
(cid:2) s= ˛ss( ∇ v s+∇ vT s ) − ˛s(s−3 2 s)( ∇· v s)I. (6) ˛ ˛  0− − 1 1 . . 3 3 9 9 2 2 9 9 0.6321 ˛ ˛  0+ + 2 2 . . 3 3 9 9 2 2 9 9 0.3679 =   t, m m , (16)
It should be mentioned here that, a strict formulation of the (cid:4) (cid:4) (cid:4) (cid:4)
momentumconservationequationswouldalsoincludeliftandvir-
(cid:4)
(cid:4)
˛0= 1. (cid:4)
(cid:4)
(cid:4)
(cid:4)
(cid:4)
(cid:4)
(17)
tualmassforcesasinterfacialforcesinadditiontothedragforce. Theconstantsusedintheprecedingequationsareasfollows:
Theinteractionbetweenthetwophasesishoweverknowntobe
dominatedbythedragforceandthecontributionsoftheliftand
C1ε= 1.42, C2ε= 1.68. (18)
virtualmassforceshavebeenneglectedbymostoftheresearchers. Another alternative turbulence formulation that is tested in this
Thesameapproachisusedinthiswork. workistheRealizablemodel.Thetransportequationforthetur-
Tosolvetheseflowequationsfurtherclosuresarerequired.The bulencekineticenergyisthesameasinthestandardmodel(Eq.
first submodel is related to the description of the turbulence. In (7)),whereasthetransportequationforthedissipationtermdiffers
this work, different versions of the k–ε model, namely the swirl significantly:
modifiedRNGk–εmodelandtheRealizablek–εmodelhavebeen
u
an
se
d
d
p
.
e
F
r
o
p
r
h
th
a
e
se
d
a
e
p
s
p
cr
r
i
o
p
a
t
c
io
h
n
h
o
a
f
ve
so
b
l
e
id
en
ph
a
a
p
s
p
e
li
t
e
u
d
r
.
bulencethedispersion
∂
∂
t
(mε)
+∇·
(m v mε)
2.1. Turbulencemodeling =∇·


t,
ε
m
∇
ε
+
mC1Sε
−
mC2
k
ε
√
2
ε
. (19)
(cid:2) (cid:3) +
The basic equations describing the standard k–ε model with
The eddy viscosity t,m is defined as in the standard k–ε model
mixture approach are given below. Here k represents the turbu-
byEq.(11).However,thecoefficientCinEq.(11)hasnolongera
constantvalueandisevaluatedby
lentkineticenergyandthetermεrepresentsthedissipationrate
o tr f a t n u s r p b o u r l t e e n q t u k a i t n io et n i s c a e s n s e o r c g ia y t . e T d h w e i f t o h ll t o h w e i s n e g p t a w ra o m e e q t u er a s t : ions are the C= A0+ As kU
ε
∗ − 1 , (20)
∂
∂
t
(mk)
+∇·
(m v mk)
=∇·


t,m
∇
k
+
G
k,m−
mε, (7) where (cid:2) (cid:3)
k
(cid:2) (cid:3) U∗ = S ij S ij+  ij  ij , (21)
∂
∂
t
(mε)
+∇·
(m v mε)
=∇·


t,
ε
m
∇
ε
+k
ε (C1ε G
k,m−
C2ε mε),
C1= m
(cid:5)
ax 0.43, 

5 , (22)
(cid:2) (cid:3) (8) (cid:6) + (cid:7)
wherethemixturepropertiesaredescribedas ˝¯ 1 ∂ v m,i ∂ v m,j , (23)
ij= 2 ∂x − ∂x
(cid:8) j i (cid:9)
v  m m = = ˛ ˛ g g ˛   g g g  v + g g + ˛ + s ˛ ˛  s s s   , s s v s . (1 (9 0) ) A0 = = 1 3 4. c 0 o 4 s , − 1 A √ s 6 = W √6 , cos W , = S ij S jk S ki 3 , ( ( 2 24 5 ) )
Theeddyviscosityforthemixturephaseiscalculatedas S ij S jk
(cid:10) (cid:11)
t,m= mC k ε 2 . (11) S ij= 2 1 ı ı v x m,i + ı ı v x m,j . (cid:10)(cid:5) (cid:11) (26)
(cid:8) j i (cid:9)
TheproductionoftheturbulentkineticenergyG iscalculated
k,m
usingthefollowingrelation: Theconstantsinvolvedintheformulationareprovidedbelow:
G k,m= t,m[ ∇ v m+∇ (v m)T]: ∇ v m. (12) C1ε= 1.44, C2= 1.9, = 1.0, ε= 1.2. (27)
Theconstantsinvolvedintheaboveequationsare: Theaveragingprocedureinvolvedinthemixturemodelissuitable
onlyforphaseshavingsimilarproperties.Inaddition,thetransport
C1ε= 1.44, C2ε= 1.92, C= 0.09, = 1.0, ε= 1.0. equationsforkandεdonotaccountfortheinterphaseturbulence

286 E.-U.Hartgeetal./Particuology7(2009)283–296
momentumtransfer,whichlimitstheapplicationareaofthismodel where
tophasesthatarenotinterpenetrating.Thesubstantialdifference v
betweenthegasandsolidphasesandtheirfullinterpenetration  | sg| t,g , (36)
= Lt,g
disqualifythemixtureapproachforanaccuratemodelinginthis
work. C 1.8 1.35cos2. (37)
ˇ= −
Analternativeapproachformodelingmultiphaseturbulenceis
Intheseequations,thetermistheanglebetweenthemeanparti-
calledthedispersedmodel.ThisformulationisbasedontheTchen
clevelocityandthemeanrelativevelocity.Furthermore,theterms
theoryofdispersionofdiscreteparticlesbyhomogeneousturbu-
lence (Hinze, 1975). The turbulence equations are solved for the
t,gandLt,garethecharacteristictimeandlengthscaleofthetur-
bulenteddiesinthegaseousphase,respectively.Thesearedefined
gasphaseandtheturbulenceparametersforthesolidsphaseare
bythefollowingequations:
deducedusingdispersionrules.Theturbulencetransportequations
o
th
b
e
ta
d
i
i
n
s
e
p
d
er
u
s
s
e
i
d
n
m
gt
o
h
d
e
el
d
i
i
s
s
p
p
r
e
e
r
s
s
e
e
n
d
t
f
e
o
d
rm
us
u
in
la
g
t
t
io
h
n
es
a
t
r
a
e
n
s
d
h
a
o
rd
w
k
n
–
b
ε
e
m
lo
o
w
d
.
e
H
l.T
er
h
e
e
,
t,g = 2
3
Cε
kg
g , (38)
implementationfortheotherturbulencemodelscanbeobtained
e ∂ ∂ a t s ( i ˛ ly g in gk a g s ) im + i ∇ la · r ( w ˛g a  y. g v gkg) L T t h ,g e = ra (cid:12) tio 3 2 o C f  th k e ε g 3 g / c 2 h . aracteristictimesisrepresentedbysgas (39)
=∇· ˛g   t k ,g ∇ kg + ˛gG k,g− ˛ggεg+ ˛gg˘ kg , (28) sg = F t, , s s g g . (40)
(cid:2) (cid:3)
∂
∂
t
(˛ggεg)
+∇·
(˛gg v gεg) T
ca
h
l
e
cu
tu
la
r
t
b
e
u
d
le
u
n
s
c
i
e
ng
qu
th
an
e
ti
f
t
o
i
l
e
l
s
ow
as
i
s
n
o
g
ci
e
a
q
te
u
d
at
w
io
i
n
th
s
t
a
h
c
e
co
d
r
i
d
s
i
p
n
e
g
rs
t
e
o
d
t
p
h
h
e
a
T
se
ch
a
e
r
n
e
theory:
=∇· (cid:2)
˛g 

t
ε
,g
∇
εg
(cid:3) +
˛g ε
kg
g(C1ε G
k,g−
C2ε gεg)
+
˛gg˘εg .
(29) k s 2 = kg (cid:8) b 1 2 + +   s s g g (cid:9) , (41)
Intheseequations,thetermG iscalculatedbyEq.(12).Allthe
o
ga
th
s
e
p
r
h
p
a
a
s
r
e
am
ve
e
r
t
s
e
io
rs
ns
in
o
v
f
o
t
l
h
ve
e
d
m
in
ixt
t k
u
h ,g
r
e
e
se
fo
e
r
q
m
u
u
a
l
t
a
io
ti
n
o
s
ns
co
d
r
e
r
s
e
c
s
r
p
ib
on
ed
d
a
to
bo
t
v
h
e
e
.
ksg
=
2kg
(cid:8) 1
b +
+


s
s
g
g (cid:9)
, (42)
T p h ar e ti t c e l r e m so s n ˘ th kg eg a a n s d p ˘ ha ε s g e. r F e o p l r l e o s w en in t g t e h q e u i a n t fl io u n e s n a c r e e o u f se th d e to d c i a sp lc e u r l s a e t d e Dt,sg = 1 3 ksg t,sg, (43)
theseterms:
2 1
˘ kg = ˛g ˇ g [ksg− 2kg+ (v s− v g) · v dr ], (30) D
w
s
h
=
er
D
e
t,sg+ (cid:2) 3 ks− b 3 ksg (cid:3) F,sg, (44)
˘εg = C3ε ε kg g ˘ kg . (31) b (1 Cv) s Cv − 1 (45)
= + g +
(cid:8) (cid:9)
Thetermksgisthecovarianceofthevelocitiesofthegasanddis-
and
persed phases. The equation used to calculate this term will be
b
p
e
ro
c
v
a
i
l
d
c
e
u
d
la
l
t
a
e
t
d
er
u
.T
si
h
n
e
g
t
t
e
h
r
e
m
e
v
q
d
u
r
a
r
t
e
i
p
o
r
n
e
b
se
e
n
lo
t
w
st
:
hedriftvelocitywhichcan C3ε= 1.2, C= 0.09, sg
=
0.75. (46)
TheassumptionsinvolvedinTchentheoryarelimitedtosystems
v
dr =− s
D
g
s
˛s∇
˛s−s D
g
g
˛g∇
˛g . (32) w
do
h
m
ere
flu
th
ct
e
ua
in
ti
t
o
e
n
rp
s
a
o
r
f
tic
th
le
e
c
d
o
i
l
s
l
p
is
e
i
r
o
s
n
e
s
d
h
p
a
h
v
a
e
se
n
.
o
U
m
nd
aj
e
o
r
r
s
r
u
o
c
l
h
e i
c
n
on
th
di
e
ti
r
o
a
n
n
s
-
,
(cid:8) (cid:9)
theturbulenceofthedispersedphaseiscontrolledmainlybythe
IntheequationaboveDsandDgarethediffusivities.Accordingto randommotionsinthegaseousphaseandthedispersedphasetur-
Tchentheorythefollowingequalityisassumed. bulence can be estimated using characteristic ratios. Apparently,
suchaformulationrequiresthesuspensiontobedilute.Sincethe
Ds= Dg (33)
solidsconcentrationwithintheriserofaCFBcanbequitehigh,the
validityofthisapproachisquestionable.
The turbulence formulation for the solid phases is drawn from
Amoregeneralapproachtosolidphaseturbulenceistousesep-
thegaseousphase,usingsomealgebraicrelations.Twoimportant
arateturbulenceequationsforeachphase.Thisapproachiscalled
parametersincharacterizingtheturbulenceofthedispersedphase
theperphasemodel(Fluent,2005).Themaintransportequations
arethecharacteristicparticlerelaxationtime,
F,sg
,relatedtothe
forthetwophasesaredemonstratedusingthestandardk–εmodel
inertialeffectsactingonthedispersedphase,andtheLagrangian
below.Allthetermsinvolvedintheseequationsarecalculatedin
integral time scale, t,sg, based on the particle trajectories and
thesamewayasdescribedinthepreviousapproaches.
their crossing in space. These two parameters are calculated as
follows:
∂
∂
t
(˛ggkg)
+∇·
(˛gg v gkg)
F,sg = ˛g ˇ g (cid:8)   g s + Cv (cid:9) , (34) =∇· ˛g   t,g ∇ kg + (˛gG k,g− ˛ggεg) + ˇ(Csgks− Cgskg)
k
t,sg = 1 + t,g C ˇ 2 , (35) − ˇ(
(cid:2)
v s− v g) ·˛  s t  ,
(cid:3)
s s∇ ˛s+ ˇ(v s− v g) ·˛  g t  ,g g∇ ˛g, (47)
(cid:5)

E.-U.Hartgeetal./Particuology7(2009)283–296 287
∂
∂
t
(˛ggεg)
+∇·
(˛gg v gεg) c ti o o n n c i e s n c t o ra r t r i e o la n te a d pp u r s o in ac g h t e h s e p S a c c h k a i e n f g fe l r im (1 i 9 t 8 . 7 T ) h f is or f m ric u t l i a o t n io a n l c b o e n lo t w rib : u-
=∇· ˛g   t ε ,g ∇ εg + ε kg g(C1ε ˛gG k,g− C2ε ˛ggεg) + C3ε  s,fr = p 2 ssin l2D . (56)
(cid:2) (cid:3)
× ˇ(Csgks− Cgkg) − ˇ(v s− v g) ·˛  s t  ,s s∇ ˛s+ ˇ(v s− v g) ·˛  g t  ,g g∇ ˛g . c T o h m eb p u re lk ss (cid:5)v io is n co a s n i d ty e  x s p f a o n r s m io u n la . t T e h s e th fo e ll r o e w si i s n ta g n e c q e u o a f ti s o o n lid gi p ve a n rti b c y le L s u t n o
(cid:13) (cid:14)
etal.(1984)isusedinthiswork:
(48)
P
le
e
n
r
c
p
e
h
i
a
n
se
bo
m
th
od
p
e
h
l
a
d
s
o
e
e
s
s
a
n
re
ot
c
i
o
n
n
v
s
o
i
l
d
v
e
e
re
a
d
ny
se
li
p
m
ar
it
a
a
t
t
e
i
l
o
y
n
a
s
n
in
d
c
w
e
i
t
t
h
h
e
ou
tu
t
r
a
b
n
u
y
- s= 4
3
˛ssdsg0 (1
+
ess)
(cid:12)


. (57)
assumption.However,amorebasicproblemisassociatedwiththis
2.3. Dragmodel
approach.Itisquestionabletouseturbulencemodelsformodeling
thesolidphaseturbulencedirectlysincethesemodelswereorig-
Aspecialfocuswasputonthedescriptionofthedragbetween
inallydevelopedformodelingfluids.Ifusedwithoutanyfurther
the gas and the solids phase. In the momentum transport equa-
assumptionormodification,thepropertiesofthesolidphaseare
tionsoftheindividualphases,thedragforceisrepresentedbythe
usedintheturbulenceequationswhichhasnojustificationasfar
asitsreliabilityisconcerned.
termˇ(v s–v g),theproductoftheinterphasemomentumexchange
coefficientˇandtheslipvelocity.
2.2. Kinetictheoryofgranularflow ThecorrelationsasgivenbyGidaspow(1994)andSyamlaland
O’Brien(1989)areoftenused.ThecorrelationbyGidaspow(1994)is
Forthedescriptionofthesolidphasestress,thekinetictheory acombinationoftheworksofErgun(1952)andWenandYu(1966);
ofgranularflow(KTGF)asdescribedbyLun,Savage,Jeffrey,and theformulationpresentedbyErgun(1952)isusedwherethesus-
Chepurniy(1984)hasbeenapplied.Fortheconductivityofgranular pensionisdense,whereastheformulationbyWenandYu(1966)
energyk thecorrelationbySyamlal,Rogers,andO’Brien(1993) isusedwherethesuspensionisdilute.Thegoverningequationsfor

hasbeenused: thiscorrelationaregivenbelowasastepfunctiondependingon
k  = 15 4 d (4 s 1 s − ˛ 1 s 3 2 √ 3  )  16 ˇ th = eg 3 4 as CD vo ˛ l s u ˛ m g e g d f | r s v a s c − tio v n g| ˛ ˛ g g : − 2.65, for ˛g >0.8, (58)
where
×
(cid:6)
1 + 5 2(4 − 3)˛sg0+15 (41 − 33)˛sg0
(cid:7)
, (49) ˇ
=
150 ˛
˛
2 s
g

d s 2
g
+
1.75 ˛sg|
d
v s
s
− v g|, for ˛g
≤
0.8 (59)
1 with

= 2
(1
+
ess), (50)
24
isthegranulartemperature,givenas
CD=
˛gRes
[1
+
0.15(˛gRes)0.687]. (60)
 = 1 3(cid:5) v ′s(cid:7) 2. (51) m Th e e n c ts or o r f e t la h t e io t n er o m f i S n y a a l m ve l l a o l c e it t ie a s l. o (1 f 9 p 9 a 3 rt ) ic is le b s a i s n e a d s o o n lid th s e u m sp e e a n s s u io re n - .
Intheaboveequation, v representstheensembleaveragedmag- Thecorrelationisrepresentedbythefollowingequations:
(cid:5) ′s(cid:7)
a n l i . tu ( T 1 d h 9 e e 8 o s 4 o f ): l t i h d e s r p a r n e d ss o u m re ly p fl s u in ct E u q a . t ( i 4 n ) g is ve c l a o lc c u it l y at o e f d th a e cc s o o r l d id in p g a t r o ti L c u le n s. et ˇ = 3 4 ˛  s r 2 ˛ ,s g d  s g CD (cid:2) R v r e ,s s (cid:3) | v s− v g| , (61)
where
ps= ˛ss
+
2s(1
+
ess)˛s 2g0. (52)
2
F
b
u
u
r
lk
th
v
e
i
r
s
m
co
o
s
r
i
e
ty
th

e
s.
E
T
q
h
.
e
(
s
6
h
)
e
i
a
n
r
vo
v
l
i
v
sc
e
o
s
s
t
i
h
ty
e
c
t
a
e
n
rm
b
s
e
s
e
h
x
e
p
a
r
r
es
v
s
i
e
sc
d
o
a
s
s
it
t
y
h

es
s
u
a
m
nd
-
CD=
(cid:15)
0.63
+ R
4
e
.
s
8
/r,s(cid:16)
, (62)
mationofthethreecontributingcomponents:
and (cid:5)

Th
s
e
=
te

r
s
m
,co

l+  s
r
,
e
ki
p
n
r
+
es

en
s,
t
fr
s
.
thecollisionalcontributiontothesh
(5
e
3
ar
) r,s= 0.5 A
−
0.06Res+ (0.06Res)2
+
0.12Res(2B
−
A)
+
A2 .
s,col
resistance,anditisformulatedasfollows: (cid:6) (cid:5) (cid:7)
(63)
4  Thecoefficientsinvolvedintheequationsabovearedefinedas:

s,col= 5
˛ssdsg0 (1
+
ess)

. (54)
Althoughthecollisionalvis
(cid:12)
cosityformulationgivenaboveisagen-
A
=
˛4
g
.14, B
=
0.8˛1
g
.28, for ˛g
≤
0.85,
erallyagreedone,thesamethingisnotvalidforthekinetictermof
theshearviscosity .ThecorrelationintroducedbyGidaspow
A
=
˛4
g
.14, B
=
˛2
g
.65, for ˛g >0.85.
s,kin
(1994)isusedthroughoutthiswork: Fig.1showsaplotofthemomentumexchangecoefficientˇvs.

s,kin= 96
1
˛
0
s(
s
1
d
+
s √
e

ss

)g0
1
+
4
5
g0˛s(1
+
ess) . (55) t t
c
h i
o
e e
e
s
f
s
fi
a o n
c
l
i
d i
e
d
n
f s o
t
r v
a
o a
n
l
d
u g m i
t
v
h
e e
u
n c
s
p o
a
n a
ls
r c t
o
e i n c
t
l t
h
e r
e
a s t
d
i i z o
r
e
a
n .
g
I ˛ t
is
s ca
c
fo n
o
r
n
b
t
a e
in
g s
u
i e v
o
e e
u
n n
sl
t
y
s h y a
i
s
n
t t
c
e t
r
h m
e
e
a
o
s
e
i
f x
n
c v
g
h e a
w
lo n
i
c g
t
i
h
e -
(cid:6) (cid:7)
The last term  in Eq. (53) accounts for the real mechanical increasingsolidsconcentration.Thisbehaviorisinagreementwith
s,fr
frictionbetweenthesolidparticles,whichbecomestheeffective measurementsinhomogeneoussuspensionsbutincontradiction
mechanismofmomentumtransferindensebedswherethesolid to the experimentally experienced behavior of segregating flows

288 E.-U.Hartgeetal./Particuology7(2009)283–296
Fig.1. Momentumexchangecoefficientvs.solidsvolumefraction. Fig.2. Momentumexchangecoefficientvs.solidsvolumefractionaccordingtothe
EMMSmodelincomparisonwiththeGidaspowformulation.
(e.g.Mueller&Reh,1994).Intheseflowsclustersorstrandswill
suspensionthefactorωhadbeenpre-computedwithforthecur-
formwhenthesolidsconcentrationisincreasedfromaverylean
rentapplicationandwerestoredinalook-uptable,whichhasbeen
suspension. This segregation causes an increase of the settling
usedwithintheFluentsimulations.
velocityandthusadecreaseofthedragcoefficient.Furtherincreas-
InFig.2,themomentumexchangecoefficientscomputedbythe
ingsolidsconcentrationwillreducethisinhomogeneityoftheflow
Gidaspowmodel,thecorrelationsofYangetal.(2003)forFCCand
andthusresultinanagainincreasingdragforce.
computed for the material used in this work are shown vs. the
SinceforsimulationsoflargescaleCFBunitsthegridcellswill
solids concentration. The EMMS yields a significant reduction of
alwaysbesignificantlylargerascomparedwithsizeoftheaggre-
themomentumexchangeforlowsolidsconcentrations,whichis
gatesformedintheflow,thecomputedconcentrationinacellis
inagreementwiththeexperimentallyobservedbehavior.Further-
alwaysanaverageoverdifferent,leananddense,flowstructures
moreitcanbeseen,thatthereductionofthedragissignificantly
andthereforethedragforcewillbeoverestimatedbythecorre-
influencedbythebedmaterialandtheoperatingconditions.Forthe
lationsofGidaspow(1994)andSyamlaletal.(1993).Atheoretical
coarsersandusedinthisworkthedecreaseofmomentumtransfer
solutionwouldbetochooseagridwithcellsizeswellbelowthesize
duetoclusterformationismuchlessthanforthefineandlightFCC
ofthestructureelements,butthiscannotbedoneforthesimulation
particles.
oflargeCFBrisersduetothelimitationsincomputingresources.
An alternative approach is to consider the sub-grid structure
withineachcell.FollowinganapproachofYangetal.(2003)the 3. Experimentalfacility
EMMS(energyminimizationmultiscale)modelofLiandKwauk
(1994)hasbeenusedduringthisworktotaketheheterogeneityof Theevaluationoftheperformanceofthesimulationsrequires
flowintoaccount. comparison of the results with experimental data. For this rea-
The EMMS assumes that the flow consists of a dense cluster son,simulationsinthisworkarebasedonapilot-scalecoldCFB
phaseandaleansurroundingphase.Theclustersareassumedto setup with a rectangular riser cross-section having the dimen-
bespherical;theminimumvoidageoftheclustersisequaltothe sions1.0m 0.3m.Theriserhasaheightof8.5mandanabrupt
×
voidageatminimumfluidizationvelocity.Onlydragforceandgrav- (L-type)exitconfiguration(seeFig.3).Therectangularductcon-
ityareconsideredintheformulation.Furthermoreitisassumed nectingtherisertothecyclonestartsataheightof7.57mandhas
thatparticleswithintheclustersandtheclustersinacontrolvol- a0.86m 0.16mcross-section.
×
ume are homogeneously dispersed. With these assumptions the For the separation of solids, the setup employs a two-stage
model can be formulated as a non-linear optimization problem cyclone system where the separated solids are returned back to
with 8 independent equations for totally 10 unknown variables the bottom section of the riser at a height of approximately 1m
(Yangetal.,2003). abovethedistributorplate,viaadowncomerpipeandasiphon.The
Sinceitistootimeconsumingtosolvethisoptimizationprob- solidsreturntotheriseratanangleof45 ◦ throughacircularduct
lem for each iteration and each cell, the problem is solved once of20cmdiameter.Inordertobeusedduringexperimentation,the
fortheoperatingconditionsunderconsiderationandthemomen- setupisequippedwithobservationwindowsforviewingtheflow
tumexchangecoefficientˇiscomputeddependingonthesolids phenomena,aswellasaweighingsectioninthedowncomerpipe
volumefraction.FollowingtheapproachofYangetal.(2003)the tomonitortheexternalrecirculation.Theriserandthedowncomer
momentumexchangecoefficientˇiscalculatedduringthiswork areequippedwithseveralpressuretransducersformeasuringthe
asfollows: pressureprofile.
ˇ
=
3
4
CD ˛s˛gg
d
|
s
v s− v g|ω, for ˛g >0.74, (64) d
ve
e
r
s T
i
c
fi
h r
c
i e b
a
e
ti
d r
o
e
n
a s b u
o
o l
f
t v s
t
e
h
,
e
p of r
s
e
im
s p e r
u
n e
l
t v
a
e i
t
d o
io
u b
n
s y
r
S
e
e c
s
x h
u
p l
l
i e
t
c
s
r h
.
i t m
I
h
n
e ä
t
n r
h
l t e
e
a
s
( t 2
e
io 0
e
n 0
x
0
p
w )
e
,
r
a i
i
t r
m
h e
e
u
n
t s h
t
e
s
e d
,
f
q
o s
u
e r
a
t t
r
u h
t
p e
z
where ω is a correction factor calculated from the results of the sandwasusedasthebedmaterial.Thepropertiesofthematerial
EMMSmodel.Fordensesuspensions,whentheexchangecoeffi- aregiveninTable1.
cientˇcalculatedbyEq.(64)islargerthantheoneresultingfrom Measurements were carried out at superficial gas velocities
theGidaspow(1994)model,thecorrelationsbyGidaspow(1994) between2and4m/s.Duringtheexperimentation,thesolidsload-
havebeenusedtocomputethemomentumexchange.Forthelean ingiskeptconstantataround300kginthewholesystemincluding

E.-U.Hartgeetal./Particuology7(2009)283–296 289
Fig.3. Experimentalsetup(Schlichthärle,2000).
Table1 lackofagenerallyacceptedformulationforhandlingthemodeling
Propertiesofbedmaterial. isthemainchallengehere.
Solidsdensity 2600kg/m3 ThemostdominantparameterintheoperationofaCFBisclearly
Meanparticlesize,d50,3 190(cid:2)m thesuperficialgasvelocity.Auniformvelocityboundarycondition
Surfacemeandiameter 140(cid:2)m atthebottomoftheriserisusedtosetthesuperficialgasvelocity.
Minimumfluidizationvelocity 0.03m/s
Oncethesuperficialvelocityisset,thereremainmainlytwovari-
Terminalsettlingvelocity 0.93m/s
ablesthatcanbecontrolled.Thesearethepressuredropsoverthe
totallengthoftheriserandtheexternalsolidsreflux.Thesetwo
the external recirculation components, and the variation of the variablesarehowevernotindependent,thereforeonlyoneofthem
externalsolidsrefluxratewithrespecttothechanginggasvelocity canbecontrolledatatime.
isobserved. While in experimental operation usually the solids inventory
TherelevantdataavailableinSchlichthärle(2000)isquitelim- andthusthepressuredropoftheriserisset,inthecurrentsimu-
ited. Only the axial variation of the average solids concentration lation,thesolidsrecirculationrateisset.Tosetthepressuredrop
canbeextractedfromwhatispresented.Nomatchingdatainvolv- duringthesimulation,itrequiresanexternalloop,whichwould
ing velocities or horizontal variation of solids concentration can significantlyincreasethecomputingtime.
be used from the source. Furthermore, the data concerning the Instudiesfoundintheliterature,timestepsofordersranging
axial variation of the solids concentration are obtained via pres- between10 5and10 3sareusedforsimilarsystems.Inthiswork,
− −
suredropmeasurements,whichinvolvessomeinaccuracydueto afewtimestepsfallinginthisrangearetriedandavalueof0.005s
accelerationeffects. isselectedtobeusedinthesimulations.Thisisavaluewhichleads
toconvergenceinreasonableamountofiterationsandalsosuffi-
4. Formulationstudy cientlyaccurate.Furthermore,itisobservedthattheuseofvery
smallstepsizesmayalsoleadtodivergenceasintheuseofvery
Aimofthisworkistosearchforanappropriateformulationfor largestepsizes.
modelinggas–solidflowsinsidelargeCFBs.Asmentionedbefore, AnapproachsimilartothatusedbyKallio(2006)isfollowed
thevarietyoftheformulationspublishedintheliteratureandthe inthisstudyinordertodetermineanappropriategridsizeforthe

290 E.-U.Hartgeetal./Particuology7(2009)283–296
Table2
Gridcharacteristics.
ID Typicalmeshdimensions Numberofcells
Coarsegrid 50mm 30mm 62.5mm 25,104
× ×
Mediumgrid 35mm 22.5mm 55mm 45,365
× ×
Finegrid 25mm 15mm 50mm 93,264
× ×
simulation.Forthispurpose,asimplifiedgeometryiscreatedby
considering only the first 5m of the riser from the bottom, and
thusneglectingtheexitgeometry.
Threedifferentgridswereappliedtothissimplifiedgeometry,
i.e.acoarsegrid,amediumgridandafinegrid.Thecharacteristics
ofthesegridsarepresentedinTable2.Inthesetrials,itisintended
todetermineameshingresolutionbeyondwhichthechangesin
themajorparametersarenomoresignificant.Althoughitisalways
possibletoresolvethelocalflowparametersfurtherbyrefiningthe
gridsize,thetimeand/orspaceaveragedoperationalparameters
suchastheaxialsolidsconcentrationdistributionorthetotalsolids
hold-upareexpectedtoremainalmostunaffectedonceasufficient
resolutionisreached.
Forcomparison,thevariationsoftheaveragedsolidsconcen-
trationalongtheheightoftheriserforthethreemeshingschemes
are shown in Fig. 4. The plotted values are obtained by spatially
averagingthesolidconcentrationsoverthecross-sectionandover Fig.5. Schematicsofthesimplifiedsimulationgeometry.
time. The analysis of the axial solids concentration graph shows
thatthechangeintheresultsbetweenthemediumandfinegrids Table3
ismuchlowercomparedtothatbetweenthecoarseandmedium Turbulenceformulationswhichhavebeentested.
grids.Actually,thedataofthemediumandfinegridsoverlapforthe Case k–εmodel Multiphaseapproach
mostdatarangeinthegraph.Goingonestepfurtherandputting
1 Swirl-modifiedRNG Dispersed
asidethecomparisonapproachwhichisofrelativenature,theabso-
2 Swirl-modifiedRNG Perphase
lutevariationinthesolidsconcentrationbetweenthemediumand 3 Realizable Perphase
finegridshasamaximumvalueof0.3%,whichisquitesmallwhen
thetwofoldchangeinthevolumeelementsisconsidered.There-
foremostofthefurthersimulationrunshavebeendonewiththe As a result of this comparison time averaged solids concen-
mediumgrid. trations in a vertical plane in the mid of the unit are shown in
Further tests have been performed with respect to the tur- Fig.6.Allthreesimulationsshowverylowconcentrationscloseto
bulence model. To reduce computing requirements a simplified thegasdistributor,whicharenotinagreementwithexperimental
geometryisusedhere.Ageometrythatisone-thirdoftheorigi- observations. The Realizable k–ε model shows high concentra-
nalcross-sectionand4mhighisconstructed,asshowninFig.5. tions quite far above the distributor, which are not typical for
Duetoitslowvolume,thegeometryrequiresmuchlowernum- thesolidsandoperatingconditionsusedforthesimulations.Fur-
berofcellsandthereforespeedsupthesimulationssubstantially. thermore instantaneous plots show very large dense zones with
Threedifferentapproaches(cf.Table3)havebeentested. solidsconcentrationsofnearly20vol%alongthewholeriserheight,
whichagainarequiteunreasonable.Thebestqualitativeagreement
withthepictureknownfrommeasurementsisobtainedwiththe
SwirlmodifiedRNGmodelandthedispersedmultiphaseapproach
exceptforthebottomzone.
Onthesamegridastheturbulencemodelsalsothedragformu-
lationsweretested.FivecasesasgiveninTable4havebeentested.
Inadditiontothedragmodelalsothecoefficientofrestitutionhas
beenvaried.
InFig.7,thetimeaveragedconcentrationsontheverticalmiddle
planeoftheriserareplotted.ForthemodelsbySyamlaletal.(1993)
andGidaspow(1994)againaleanzonedirectlyabovethegasdis-
tributorcanbeseen,onlytheEMMSmodelaccordingtoYangetal.
(2003)predictsadensebottomzone,asitisobservedinreality.
Table4
Dragcorrelationstested.
Case Dragcorrelation Coefficientofrestitution,ess
1 Syamlaletal.(1993) 0.99
2 Gidaspow(1994) 0.90
3 Gidaspow(1994) 0.99
4 Yangetal.(2003) 0.90
Fig.4. Timeaveragedaxialsolidsconcentrationvs.heightcomputedwithdifferent
5 Yangetal.(2003) 0.99
gridresolutions.

E.-U.Hartgeetal./Particuology7(2009)283–296 291
Fig.6. Timeaverageddistributionofsolidsinsidetheriser(Gidaspowdragmodel,coefficientofrestitutioness=0.99,u=3m/s,Gs=20kg/m2s).
Fig.7. Timeaverageddistributionofsolidsinsidetheriser(turbulencemodelRNGdispersed,u=3m/s,Gs=20kg/m2s).

292 E.-U.Hartgeetal./Particuology7(2009)283–296
Fig.8. Timeaveragedaxialsolidsdistribution(turbulencemodelRNGdispersed,
u=3m/s,Gs=20kg/m2s).
InFig.8,theaxialprofileofthesolidsconcentrationaveraged
overthecross-sectionalareaisplotted.Inthisfigurealsoexperi- Fig.9. Schematicofthesimulationgeometrywithdimensionsgiveninmm.
mentalvaluesmeasuredbySchlichthärle(2000)areaddedintothe
graph,eventhoughtheyhavebeenmeasuredinadifferentgeom-
etrybutundersimilaroperatingconditions.Itcanbeseen,thatthe velocity,u 0 andthesolidsexternalreflux,Gs,arecontrolleddirectly
simulationresultswiththeEMMSdragmodelfitquitewelltothe bytheboundaryconditions,whereastheremainingonesarethe
measurements,whiletheotherdragcorrelationsshowfartoolow outcomesofthesimulation.
solidsconcentrations. Fig. 10 shows the time averaged solids concentrations in the
middleplaneoftheCFBriser.Adensebottomzoneofabout1m
heighthasbeenrecognized.Intherescaledplotoftheuppersection
5. Simulationresultsofapilot-scaleCFB
acore/annulusstructurecanberecognizeduptoaheightofabout
4–5mabovethegasdistributor.Abovethisheightsolidsseemto
Asinthesimulationsperformedpreviously,thesimulationof
movetowardthecenter.
theexperimentalsetuprequiresbuildingamodelgeometry.The
The observations made up to now are more of a qualitative
onlydifferenceinthecreationofsuchgeometryhereistheneces-
nature. However, a scientific study necessitates the quantitative
sity to achieve an accurate representation of the real physical
descriptionoftheinvolvedparameters.Amoreconcreteideaabout
system.
the solids phase inside the riser can be obtained by considering
Adeviationfromtheoriginalgeometryispresentforthesolids
theaxialsolidsconcentrationdistributionplottedinFig.11.Inthis
refluxpipe.The20cmdiameterpipeofcircularcross-sectioninthe
figure,theexperimentalresultsproducedinSchlichthärle(2000)
experimentalsetupisreplacedwithaductofsquarecross-section
corresponding to each of the cases simulated are also plotted.
havinganequalcross-sectionalarea.Suchanactionistakentomake
Comparisonofthesecurvesisamainindicatorinevaluatingthe
iteasiertostructurethegrids.Sincealltheboundariesoftheriser
performanceoftheperformedsimulations.
arerectangularinshape,itisquiteeasytoobtainastructuredgrid
Theaxialplotsshowthatthegeneraltendenciesintheexperi-
inthemodeledgeometry.Theuseofacircularsolidsrefluxgeome-
mentalresultsarereproducedquitesuccessfullyinthesimulations.
trywouldnormallycreatealocaldistortioninthegeneralmeshing
Theexperimentaldataforasuperficialvelocityof3m/sshowthat
patternoftheriservolumearoundtheconnectionpoint.Thiscom-
a dense bed of approximately 80cm height and 30–35% solids
plication is prevented by using the square duct. Since the exact
concentration is followed by a very steep decrease in the solids
shapeofthisducthasnoexpectedcriticalroleinthegeneralflow
concentration,representingthetransitionzone.Ataheightaround
patterninsidetheriser,thesimplificationmadehereisveryreason-
1.5mthelargeslopeceasesoutandarelativelyconstantvalueof
able.Withallthesepointsuptonow,thedetailedschematicofthe
thesolidsconcentrationisattained,althoughacontinuousdropof
modeledgeometryispresentedinFig.9.Followingtheresultsof
theconcentrationisobservedthroughouttheriser.
theformulationsstudytheschemesummarizedinTable5isused
Somediscrepanciesareobservedinthesteepnessofthegradient
forthesimulation.
betweenthedensebottomzoneandtheleanupperzone.Thesim-
Two cases of different superficial gas velocities and external
ulationspredictamuchsmoothertransitionbetweenthesezones
massrefluxratesaresimulatedinthispartofthework.Theopera-
thantheexperiments.Atthispoint,itisnecessarytonotethatthe
tionalparametersforthesecases,whichareselectedbasedonthe
experimentaldataadaptedfromSchlichthärle(2000)arebasedon
experimental work of Schlichthärle (2000), are listed in Table 6.
pressuredropmeasurements.Althoughthisisquiteacommonway
Theparametersinthefirsttwocolumns,namelythesuperficialgas
ofestimatingthesolidsconcentration,itinvolvessomeinaccuracy
Table5
Usedmodelsandparametersforthesimulationofthepilotplant. Table6
Simulatedoperationalconditions.
Granulartemperaturemodel PDEformulation
Turbulencemodel RNGk–ε,dispersed
Case u0(m/s) Gs(kg/m2s) (cid:21)Priser(mbar) Solidshold-up(kg)
Dragmodel EMMS 1 3 7.8 94 298
Coefficientofrestitution,ess 0.99 2 4 20.0 79 245

E.-U.Hartgeetal./Particuology7(2009)283–296 293
Fig.10. Timeaverageddistributionofsolids(case1:u0=3m/s,Gs=7.8kg/m2s).
duetotheaccelerationeffectofsolidparticleswhichisreflected forthesolidsphase,giveninFigs.12and13,respectively.Thecon-
in the pressure drop. In principle, the acceleration effect causes centration profiles in Fig. 12 show that a core-annular regime is
largerpressuredropstobemeasuredalongtherisercomparedto observedthroughouttheriser,withsolidsconcentratingmoreat
theweightoftheparticlesintherelevantsection.Therefore,the thenear-wallregion.Thisfactisalsoobservedinthedensebottom
solidsconcentrationcalculatedfromthepressuremeasurements zone,asnotedpreviously.Theeffectisobservedtodisappearonly
arehigherthantherealvalues,meaningthattheerrorsmentioned towardstheendoftheriser,wheretheexitgeometryiseffective.
throughouttheanalysishereareslightlyoverestimated.Neverthe- Inthedensebottomzone,theshapesoftheconcentrationpro-
less,thesedifferenceshavetobeinvestigatedinmoredetailina filesarequitesimilarforbothsimulations.Thesolidconcentrations
futurework. forthefirstsimulation(case1)arelargeratthebottomzone,com-
Amoredetaileddescriptionoftheflowfieldisprovidednext pared to the second simulation (case 2) with a larger superficial
withthehorizontalprofilesofconcentrationandverticalvelocity gasvelocity.Onthecontrary,theprofilesforthefistsimulationfall
belowthesecondonefortheupperdilutezone.Bothobservations
arequitestraightforwardandmatchtheexpectations.
Theseparationofsolidsphaseinthenear-wallregionatmoder-
ateheightsoftheriser,whichwaspreviouslynotedintheanalysis
inmoredetail,isalsoobservedintheconcentrationprofilesshown
here.Atheightsof4and6m,itisclearlyobservedthatthepro-
filesattainalocalminimumvaluejustinthevicinityofnear-wall
region where the maximum values of the solids concentrations
occur,confirmingthegapthatwasmentionedpreviously.Asimilar
observationintheconcentrationprofilesobservedataheightof
0.75misthoughttoresultfromtheeffectsofsolidsinlet.
A further fact concerning the solids concentration profiles is
that the accumulation of solids in the near-wall region is very
intense.Formostoftheheightsconsideredinthegivenprofiles,
theobservedsolidsconcentrationsinthenear-wallregionaresev-
eralmultiplesoftheconcentrationsinthecore;theratioreaching
avalueof5forcertaincases.
TheverticalvelocityprofilesofthesolidsphasegiveninFig.13
arealsoreasonable.Forallprofilesplottedatdifferentheights,a
Fig.11. Timeaveragedaxialsolidsprofilesinsidetheriserincomparisonwithmea-
surementsfromSchlichthärle(2000). downwardmovementofsolidsisobservedinthenear-wallregion,

294 E.-U.Hartgeetal./Particuology7(2009)283–296
Fig.12. Horizontalprofilesofaveragesolidsconcentrationinsidetheriser.
which matches the general expectation. Though the downward ties.Forthefirstsimulation,thesolidsvelocityseldomexceedsthe
velocityofthesolidsattaindifferentlevelsatdifferentheightsof superficialgasvelocityof3m/s.Forthesecondsimulationveloc-
theriser,theyallshowadownwardmovingbehavior,exceptthe itiesexceedingthesuperficialgasvelocitiesinthecoreregionis
particular observation at 8m, where the wall disappears on one morecommon,especiallyatmoderateheights.Thisisqualitatively
sideduetotheexitconfiguration.Atthisparticularlocation,the ingoodagreementwithexperimentalfindings(e.g.Hartge,Li,&
solidspossessvelocitiessimilartothevelocitiesinthecore. Werther,1986).Forthehigherregions,itisalsopossibletoobserve
Verysimilarprofilesareobservedforbothsimulationsconcern- verticalsolidsvelocitiesexceedingthesuperficialvelocity.Thisis
ingtheverticalsolidsvelocitiesinthebottomzone.Atthehigher howeveranormaloutcomeoftheaccelerationthattakesplacenear
regions of the riser, the solids are accelerated to higher veloci- theexitgeometry.

E.-U.Hartgeetal./Particuology7(2009)283–296 295
Fig.13. Horizontalprofilesofaverageverticalsolidsvelocityinsidetheriser.
6. Conclusions correlationswithanincreasingdragwithincreasingsolidsconcen-
trationfailtopredictadensebottomzoneintheCFBriser,asis
Theworkpresentedhereconsistsoftwomajorparts.Thefirst observedinreality.Takingthesub-gridheterogeneityoftheflow
partinvolvesaformulationstudy,whereseveralcombinationsof into account, as is done here with the help of the EMMS model,
granulartemperatureformulation,turbulencemodels,approaches allowspredictingthedensebottomzone.
tosolidsphaseturbulence,dragcorrelationsandsolid–solidresti- Inthesecondpartoftheworkapilot-scalecoldCFBsetupissim-
tutioncoefficientsaretested.Asresultofthisstudy,aformulation ulated.Thisisdonetoevaluatetheperformanceoftheformulation
isestablishedfromthevarietyofavailablemodels.Asamajorfind- that is established. A general comparison of the results with the
ingofthispartithasbeenshown,thatthecommonlyuseddrag availableexperimentaldatashowsgoodagreement.However,the

296 E.-U.Hartgeetal./Particuology7(2009)283–296
extentofcomparisontoexperimentaldataremainsratherlimited. Kallio,S.(2006).CharacteristicsofgasandsolidsmixinginaCFBdeterminedfrom
Moredetailedmeasurementsarenecessarytogetamorecomplete 3DCFDsimulations.InProceedingsof19thInternationalConferenceonFluidized
BedCombustionVienna,Austria.
validation.
Li,J.,&Kwauk,M.(1994).Particle-fluidtwo-phaseflow,theenergy-minimizationmul-
tiscalemethod.Beijing:MetallurgicalIndustryPress.
References Lun,C.K.K.,Savage,S.B.,Jeffrey,D.J.,&Chepurniy,N.(1984).Kinetictheoriesfor
granularflow:Inelasticparticlesincouetteflowandslightlyinelasticparticles
inageneralflowfield.JournalofFluidMechanics,140,223–256.
Agrawal,K.,Loezos,P.N.,Syamlal,M.,&Sundaresan,S.(2001).Theroleofmeso-scale
Mueller,P.,&Reh,L.(1994).Particledragandpressuredropinacceleratedgas–solid
structuresinrapidgas–solidflows.JournalofFluidMechanics,445,151–185.
flow.InA.A.Avidan(Ed.),CirculatingfluidizedbedtechnologyIV(pp.193–198).
Beetstra,R.,vanderHoef,M.A.,&Kuipers,J.A.M.(2006).ALattice–Boltzmann
NewYork:AIChE.
simulationstudyofthedragcoefficientofclustersofspheres.Computers&Fluids,
Qi,H.,Li,F.,Xi,B.,&You,C.(2007).ModelingofdragwiththeEulerianapproach
35,966–970.
andEMMStheoryforheterogeneousdensegas–solidtwo-phaseflow.Chemical
Benyahia,S.,Arastoopour,H.,Knowlton,T.M.,&Massah,H.(2000).Simulationof
EngineeringScience,62,1670–1681.
particlesandgasflowbehaviorintherisersectionofacirculatingfluidizedbed
Qi,H.,You,C.,Boemer,A.,&Renz,U.(2000).Euleriansimulationofgas–solidtwo-
usingthekinetictheoryapproachfortheparticulatephase.PowderTechnology,
phaseflowinaCFB-riserunderconsiderationofclustereffects.InD.Xu,&S.
112,24–33.
Mori(Eds.),Fluidization2000:scienceandtechnology(pp.231–237).Xi’an:Xi’an
Bird,R.B.,Stewart,W.E.,&Lightfoot,E.N.(2001).Transportphenomena(2nded.).
PublishingHouse.
NewYork:Wiley.
Schaeffer,D.G.(1987).Instabilityintheevolutionequationsdescribingincompress-
Chapman,S.,&Cowling,T.G.(1970).Themathematicaltheoryofnon-uniformgases:
iblegranularflow.JournalofDifferentialEquations,66,19–50.
Anaccountofthekinetictheoryofviscosity,thermalconductionanddiffusionin
Schlichthärle,P.(2000).Fluiddynamicsandmixingofsolidsandgasinthebottom
gases.Cambridge:CambridgeUniversityPress.
zoneofcirculatingfluidizedbeds.Unpublisheddoctoraldissertation,Technische
Crowe,C.T.,Sommerfeld,M.,&Tsuji,Y.(1997).Multiphaseflowswithdropletsand
UniversitaetHamburg-Harburg,Aachen:ShakerVerlag.
particles.BocaRaton:CRCPress.
Syamlal,M.,&O’Brien,T.J.(1989).Computersimulationofbubblesinafluidized
Deen,N.G.,vanSintAnnaland,M.,vanderHoef,M.A.,&Kuipers,J.A.M.(2007).
bed.AIChESymposiumSeries,85,22–31.
Reviewofdiscreteparticlemodelingoffluidizedbeds.ChemicalEngineering
Syamlal,M.,Rogers,W.,&O’Brien,T.J.(1993).MFIXdocumentationtheoryguide.
Science,62,28–44.
TechnicalReportDOE/METC-94/1004,U.S.DepartmentofEnergy(DOE).Mor-
Fluent.(2005).FLUENT6.2user’sguide.Lebanon:FluentInc.
gantownEnergyTechnologyCenter,Morgantown,WV.
Ergun,S.(1952).Fluidflowthroughpackedcolumns.ChemicalEngineeringProgress,
Taghipour,F.,Ellis,N.,&Wong,C.(2005).Experimentalandcomputationalstudy
48,89–94.
of gas–solid fluidized bed hydrodynamics. Chemical Engineering Science, 60,
Gidaspow,D.(1994).Multiphaseflowandfluidization.NewYork:AcademicPress.
6857–6867.
Goldschmidt,M.(2001).Hydrodynamicmodellingoffluidisedbedspraygranulation.
Wen,C.-Y.,&Yu,Y.H.(1966).Mechanicsoffluidization.ChemicalEngineeringProgress
Unpublisheddoctoraldissertation,TheNetherlands:TwenteUniversity.
SymposiumSeries,62,100–111.
Hartge,E.-U.,Li,Y.,&Werther,J.(1986).Flowstructuresinfastfluidizedbeds.In
Yang,N.,Wang,W.,Ge,W.,&Li,J.(2003).CFDsimulationofconcurrent-upgas–solid
L.K.Østergaard,&A.Sørensen(Eds.),FluidizationV(pp.345–352).NewYork:
flowincirculatingfluidizedbedswithstructure-dependentdragcoefficient.
EngineeringFoundation.
ChemicalEngineeringJournal,96,71–80.
Hinze,J.O.(1975).Turbulence.NewYork:McGraw-Hill.
