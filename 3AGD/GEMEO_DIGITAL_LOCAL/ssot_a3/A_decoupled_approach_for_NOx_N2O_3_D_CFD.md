# A_decoupled_approach_for_NOx_N2O_3_D_CFD

**Fonte**: A_decoupled_approach_for_NOx_N2O_3_D_CFD.pdf  
**Data de conversão**: 2025-07-30 15:07:25  
**Origem**: base_relevantes

---

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
http://www.elsevier.com/authorsrights

Author's personal copy
A decoupled approach for NO –N O 3-D CFD modeling in CFB plants
x 2
⇑
A. Nikolopoulosa,b, , I. Malgarinosa, N. Nikolopoulosb, P. Grammelisb, S. Karrelasa, E. Kakarasa,b
aLaboratoryofSteamBoilersandThermalPlants,ThermalEngineeringSector,SchoolofMechanicalEngineering,NTUA,Athens,Greece
bCentreforResearchandTechnologyHellas,ChemicalProcess&EnergyResourcesInstitute,Athens,Greece
h i g h l i g h t s g r a p h i c a l a b s t r a c t
(cid:2)Adecoupled3-DNOx–N2OCFDmodel
forCFBCsisdevelopedandvalidated.
(cid:2)NOx–N2Oheterogeneousand 9
homogeneousreactionsare 8
considered. 7
(cid:2)Reactionratesareretrievedfrom
6
literature.
(cid:2)Thedecoupledapproachisvalidated 5
andprovedtobecomputational 4
efficient. 3
(cid:2)ThemodelcanbeusedforCFBC
2
optimizationwithrespectto
1
NOx–N2Oemissions.
0
600 400 200 0
NOx Conc. (mg/mN 3)
bed
height
- z
(m)
Fuel115(2014)401–415
ContentslistsavailableatScienceDirect
Fuel
journal homepage: www.elsevier.com/locate/fuel
experiment
Model2 Model2 minimun
Model2 maximum Model1
(a)
a r t i c l e i n f o a b s t r a c t
Articlehistory: Inthisstudy,a3DCFDmodelfortheformationofNOxandN2Oinalignitefired1.2MWthCFBpilotplant
Received26October2012 isdeveloped.Thedecoupledapproach(decoupledfromcombustionsimulation)istestedfortheminimi-
Receivedinrevisedform20June2013 zationofcomputationalcost.Ascombustionsimulationisprerequired,thiswasachievedthroughasim-
Accepted24June2013
Availableonline22July2013
plified3-DCFDcombustionmodel.Thedevelopedmodelisthenappliedtothepilot-scale1.2MWthCFB
plantandvalidatedagainstexperimentaldata.AsconcernstheNOx–N2Omodel,anextensiveliterature
reviewisalsocarriedoutfortheincorporationoftheappropriatereactionsnetworkandrespectivereac-
Keywords:
tionratesexpressions.Resultsshowthathomogenousreactionsarefavouredonthelowersectionofthe
NOx
bed,duetotheabundanceoffueldevolatilizationproducts.Ontheotherhand,ontheuppersection,het-
N2O
erogeneousreactionsgovernnitricoxideformation/reduction.Itisfoundthatfortheligniteexaminedin
Simulation
Combustion thiswork,HCNisreleasedinnegligibleamountsduringcharcombustion.Theproposedandvalidated
CFB CFDmodelforNOxandN2O,iscapableofexaminingtheeffectofdifferentoperationalparametersand
coalpropertiesontheoverallnitricoxidesemissionsfromaCFBcombustor,withlowcomputationalcost
andwithouttheadditionalexpensesforpilot-scaleexperiments.
(cid:2)2013ElsevierLtd.Allrightsreserved.
1.Introduction combustion.Today,circulatingfluidizedbed(CFB)boilersareused
inpowergenerationandaregrowinginnumberandsize.Thelarg-
Overthepasttwodecades,theurgentneedtofindnew,environ- estunitinoperationislocatedinLagisza,Polandandcontainsone
mentallyattractiveandmoreefficienttechnologiesforburningfos- 460MW supercriticalCFBboiler[1].Akeycharacteristicoffluid-
e
sil fuels, has led to the great development of fluidized bed ized bed combustion is low and uniform operating temperature,
usually in the range of 1025–1200K, in contrast to conventional
⇑ pulverized coal-fired boilers, which is approximately 1600K [2].
Corresponding author at: Laboratory of Steam Boilers and Thermal Plants,
UnderPF(PulverizedFuel)combustionconditions,thetemperature
Thermal Engineering Sector, School of Mechanical Engineering, NTUA, Athens,
Greece.Tel.:+302106501509;fax:+302106501598. distributionisfarfromuniform.Hotspotscanbespottedwithtem-
E-mailaddress:a.nikolopoulos@certh.gr(A.Nikolopoulos). peraturesupto2000K.Insuchconditions,airnitrogenisoxidized
0016-2361/$-seefrontmatter(cid:2)2013ElsevierLtd.Allrightsreserved.
http://dx.doi.org/10.1016/j.fuel.2013.06.036

Author's personal copy
402 A.Nikolopoulosetal./Fuel115(2014)401–415
Nomenclature
A pre-exponential reaction constant (varying i.e. s(cid:3)1, S sourceterm(varyingunits)
(mols)(cid:3)1) Sc Schmidtnumber(–)
A eddydissipationempiricalconstant(–) Sh Sherwoodnumber(–)
E
B eddydissipationempiricalconstant(–) t time(s)
E
c specificheatcapacityatconstantpressure(J/kgK) T temperature(K)
p
C gasconcentration(mol/m3) U unburntcarbonpercentage(%)
fc
d diameter(m) ~u actualvelocity(m/s)
d chardiameter(m) ~u interphasevelocity(m/s)
c lq
d initialdiameter(m) Y massfractionofanyproductspecies
o P
D Diffusivity(m2/s) Y massfractionofaparticularreactant
iff R
D o2 ðgÞ oxygendiffusivity(m2/s) Ysp speciesconcentration(mg species /kg gas )
g gravitationalacceleration(m/s2) Y mass percentage of volatiles in each particle (kg /
vol vol
h heattransfercoefficient(W/Km3) kg )
fuel
h diffusionratecoefficients(kg/(m2skPa)) b momentumexchangecoefficient(kg/(m3s))
m
H enthalpy(J/kg) C diffusionterm(kg/(ms))
k rateconstant(varying,e.g.1/s,mol/(m3s)) E activationenergy(J/kmol)
k charcombustionrate e volumefraction(–)
c v
K thermalconductivity(W/Km) stoichiometriccoefficientforreactantIinreactionr
kt turbulentkineticenergy(m2/s2)
vI,r
stoichiometriccoefficientforproductjinreactionr
I,r
L latentheatofwater(J/kg) q density(kg/m3)
w
m_ masstransferbetweenphases(kg/sm3) / charcombustionparameter(–)
c
m massoffuelinacell(kg)
f
m_w ps moistureevaporationrate(kg/s) Sub-,Super-scripts
M w molecularweight(kg/kmol) f fuelindex
N p numberofparticlesinacontrolvolume(#) g gas
Nu Nusseltnumber(–) i species(reactants)index
P 02ðgÞ partialpressureofoxygen(kPa) j species(products)index
Pr Prandtlnumber(–) l indexforanEulerianphase
~q heatflux(W/m2) p particle
Q _ rateofenergytransferbetweenphases(W/m3) PR productsindex
R reactionrate ps particlesurface
R c charcombustionreactionrate q indexforanEulerianphase
Re Reynolds(–) r reactionindex
R vol volatilereleaserate R reactantsindex
R u universalgasconstant(8314.47kJ/(molK)) vol volatilesordevolitilization
andleadstotheformationofthermal-NO [3,4].Alocalincreaseof ThemajorityoftherelevantCFDstudiesonCFBshavebeenfo-
x
just100KcanleadtoadoublingofthelocalthermalNO formation cused on isothermal modeling of CFBCs [10–13]. Such numerical
x
rate[2].Ontheotherhand,underfluidizedbedcombustioncondi- approachesconstitutedthebasisontowhichcombustionandpol-
tions(lowanduniformtemperature),theformationofthermal-NO lutantsformationmodelscanbeincorporated,inordertodevelop
x
isminimizedwhichresultsinlowNO emissions,asnitricoxides avalidatedandreliabletoolforthesimulationofCFBCs.However,
x
areformedalmostentirelyfromfuelnitrogen[3–5]. even for the CFD cold flow simulation, the uncertainty behind a
However,lowcombustiontemperatureenhancestheformation substantialnumberofparametersissignificant.Themostimpor-
of nitrous oxide (N O), emissions of which range from 15 to tantparameterasreportedbyWangetal.[14]isthemomentum
2
200ppm [6–8] in comparison to much lower levels observed in exchangecoefficientbetweengasandinertmaterial[15].
pulverizedcoalcombustionboilers(<20ppm[6–9]).Nitrousoxide RegardingthenumericalsimulationofCFBcombusting/react-
(N O)isknowntobeinvolvedin boththegreenhouse effectand ingflows,limitedliteratureisavailable,especiallyforcombustion
2
thedepletionoftheozonelayer[7].CFDmodelingoffersareliable mechanisms [16,17]. Moreover the majority of these studies, ap-
wayofinvestigatingthechemicalmechanismsthatgovernthefor- proachthecomplicatedphysics,whichdominatetheoperationof
mationofnitrogenoxidesandcontrolthefinalNO/N Oemissions. CFB combustor, in a two-dimensional way [16,17], overlooking
2
PredictionofgaseousemissionsfromaCFBplantcanbeachieved theirthreedimensionalcharacter.Inthisworkforthecalculation
with the assistance of CFD modeling, which may further lead in ofthecombustingfield,asimplified3-DpureEulerianCFDmodel
optimizeddesignofindustrialscaleunits. is developed taking into account fuel particle conversion mecha-
CFDmodelingisapowerfultoolcapableofaddressingpollutants nisms, i.e. drying, devolatilization and char combustion, in the
simulationincombustingflows.However,asCFBCmodelingiscon- CFBCriser.
cerned,thecomputationalcostisanimportantdrawbackofthese ThispaperdealswithpropersimulationofNO andN Oemis-
x 2
sophisticatedmodels.Nikolopoulosetal.,[10,11]pointedoutthat sionsfromCFBCs.Adecoupledapproachisfollowed.Howeverfor
thecomputationalcostishighevenforCFDsimulationoftheiso- suchmodelsthecombustionfieldshouldbeknown.Inthiswork
thermalflowinaCFBriser.Theadditionofcombustionandpollu- this information is retrieved through a simplified CFD modeling
tants formation mechanisms in such simulations severely of combustion mechanisms. Subsequently, a decoupled NO/N O
x 2
increasesboththecomplexityandthecomputationalcostofsuch modelisappliedusingthesolutionofthecombustionmodelasin-
models.Therefore,acombinationofacceptableaccuracywithhigh put and NO/N O spatial distribution is investigated. Reactions
x 2
computationalefficiencyisanobjective. kinetics are essential for the proper incorporation of reactions in

Author's personal copy
A.Nikolopoulosetal./Fuel115(2014)401–415 403
themodel.Areviewinliteratureconcerningreactionratesisalso @ ðe q~u Þþr(cid:4)ðe q~u~u Þ¼(cid:3)e rp (cid:3)rp þr(cid:4)s(cid:2)(cid:2) þe q~g
carriedout,inordertoconcludetoanetworkofchemicalreactions @t q q q q q q q q g q q q q
best describing the NO x /N 2 O formation/ destruction mechanisms n
in a fluidized bed. For the simulations, the commercial CFD plat- þ ½bð~u l (cid:3)~u q Þþm_ lq ~u lq (cid:3)m_ ql ~u ql (cid:5) ð3Þ
formofANSYS(Fluent12.1.4)isused. l¼1
X
Theaboveequationisappliedforthetwosolidphases,i.e.inert
2.Methodology materialandfuel.InEqs.(2)and(3)thetwolasttermsintheright
hand side describe the momentum transfer between qth and lth
2.1.SimplifiedcombustionmodelforCFBC phases due to mass transfer ðm_ Þ that is caused by reactions.~u
lq lq
istheinterphasevelocity,definedasfollows.Ifm_ >0(i.e.,phase
lq
ThesimulationofcombustingflowwithinFBswiththepureEu- p mass is being transferred to phase q),~u ¼~u ; if m_ < 0 (i.e.,
lq p lq
lerianTFM (Two-Fluid-Montel) formulation is difficult. The main phase q mass is being transferred to phase p),~u ¼~u . Likewise,
lq q
difficulties are the computational cost and the proper simulation ifm_ >0then=;ifm_ <0then~u ¼~u.
lp ql lq l
ofthemomentumandheatexchangecoefficients betweensolids Theenthalpyequationforeachphaseis:
(inert-material and fuel). Accurate modeling of momentum and
heatexchangecoefficientsisdifficultand littleinformation isre- @ ðe q H Þþr(cid:4)ðe q~u H Þ¼(cid:3)e @p qþs(cid:2)(cid:2) þr~u (cid:3)r~q
ported in the literature. Even in the simpler case of gas–solid @t q q q q q q q q @t q q q
momentum exchange, it is worth noticing that models based on n _
þS þ ðQ Þ ð4Þ
the assumption of homogeneous conditions for each computa- q lq
l¼1
tionalcell,failtopredictthegoverningphysicsofsuchprocesses, X
underspecificconditions[11,15,18–20].Thisfailurewasthedriv- Theheattransferbetweentheprimarygasphaseandthetwo
ing force for the development and implementation of the novel Euleriansolidphases(inert-materialandfuel),iscalculatedasfol-
EMMS schemes. However, EMMS implementation in combusting lows[24]:
flow is not straightforward because gas density and viscosity is _
Q ¼h (cid:4)ðT (cid:3)T Þ ð5Þ
not constant and the simulation of particulates clogging mecha- qg qg q g
nisms should take into account the different properties of fuel h ¼ 6(cid:4)K g (cid:4)e l (cid:4)e g (cid:4)Nu g ð6Þ
andinert-materialparticles.Thisishardtoachievesincethemech- qg d2
q
anismsofparticleclogginginpolydispersedgranularflowsarenot
known yet. Moreover, the gas properties are not constant but a
ForthecalculationofNunumber,Gunn[24]proposesthefol-
function of temperature, fact that increases the complexity of lowingequation.
EMMSimplementationinCFDcodes.
Nu ¼ð7(cid:3)10e þ5e2Þ 1þ0:7Re0:2Pr1=3
Currently, EMMS schemes cannot be applied to combusting g g g q
granularflowswithoutquestionablesimplifications: (cid:2) (cid:3)
þ 1:33(cid:3)2:4e þ1:2e2 Re0:7Pr1=3 ð7Þ
g g q
1. Gas properties that are a function of temperature should be (cid:2) (cid:3)
Thisequationisvalidforparticleloadingof0–65%,andReupto
considered constant. The assumption of isothermal conditions 105anditsapplicableforheattransferbetweenagasandagran-
inside CFB risers is reasonable enough due to the high heat
ularmaterial.PrandtlandReynoldsnumbersinEq.(7)arecalcu-
transfercoefficientexperiencedinsuchunits[21].
latedasfollows:
2. Fuel and inert-material particles should be either represented
bythemeandiameteroftheirbinarymixtureorbythemean Pr¼ c pg l g ð8Þ
diameter of the inert-material, which has the greater particle K g
loading.Thisisaroughsimplificationthatmayresultininaccu- j~u (cid:3)~u jq d
ratesimulationoftheFBhydrodynamics. Re q ¼ q l g g q ð9Þ
g
Therefore,theselectionof a conventionaldrag model,such as Forthecalculationofheattransferbetweengranularphases,i.e.
Gidaspow seems to be the only theoretically sound choice. The inert-materialandfuelacomprehensivemodelisnotavailablein
drawbacks of such models have been thoroughly discussed therespectiveliterature[25].However,Eqs.(7)–(9)thatcomprise
[11,15]butithasbeenstatedthatforindustrialpurposessuchcor- Gunn’s model [24] can be used for heat transfer between solid
relations may be utilized under proper grid density [15,22]. The phases,asproposedbyNikolopoulosetal.[26].InEqs.(10)–(13),
isothermalmodeladoptedinthisworkcanbefoundinRampidis q index refers to inert-material that is treated as a ‘‘pseudo’’ gas
etal.[23],andasfarasthedragmodelisconcernedtheconven- phase.
tionalmodelofGidaspowisapplied.
6(cid:4)K (cid:4)e (cid:4)e (cid:4)Nu
Thedescriptionofmultiphaseflowasinterpenetratingcontinua h ¼ q f q q ð10Þ
incorporatestheconceptofphasesvolumefraction,denotedbye . qf d2
q f
Thecontinuityequationforphaseqis: c l
Pr¼ pg q ð11Þ
@ ðe q Þþr(cid:4)ðe q~u Þ¼S ð1Þ K q
@t q q q q q q Re ¼ j~u q (cid:3)~u f jq q d f ð12Þ
q l
Asfarasgasesareconcerned,themomentumequationis: q
@ ðe q~u Þþr(cid:4)ðe q~u~u Þ¼(cid:3)e rp þr(cid:4)s(cid:2)(cid:2) þe q~g Nu q ¼ 7(cid:3)10e q þ5e2 q 1þ0:7Re0 q :2Pr1=3
@t q q q q q q q q g q q q (cid:2) (cid:3)(cid:2) (cid:3)
þ 1:33(cid:3)2:4e þ1:2e2 Re0:7Pr1=3 ð13Þ
q q q
n
þ ½bð~u (cid:3)~u Þþm_ ~u (cid:3)m_ ~u (cid:5) ð2Þ (cid:2) (cid:3)
l q lq lq ql ql Although this approximation may look oversimplified, the
X l¼1 numericalresultspresentedinthisworkagreequitewellwiththe
whilefortheqthsolidphasethefollowingequationisproposed: correspondingexperimentaldata.Additionallythesymmetricmod-

Author's personal copy
404 A.Nikolopoulosetal./Fuel115(2014)401–415
elofSyamlal[27]isusedforthesimulationofthemomentumex- Themodelisapplicablewhenthereisclearlyoneprimarycontinu-
changecoefficientbetweensolidphases(fuelandinert-material). ousphaseandtherestaredisperseddilutesecondaryphases.
As far as the effect of turbulence is concerned, albeit in bed The effect of particulates on gas turbulence is calculated
hydrodynamics seemed to have a small influence [13,23] it was through an algebraic sub-model. More information on k–e dis-
foundtobeimportantincombustingflows[25,26].Inordertosim- persedturbulencemodelcanbefoundinFLUENT[29].Thek–edis-
ulateinarealisticwaythehomogeneousreactionsrates,valuesof persedturbulencemodel isappropriatefor dilute granularflows.
ktandetareneededasinputsfortheFiniteRate/Eddydissipation However, in FBs the multiphase flow is rather denser. Theoreti-
concept. cally,inFBsthe‘‘perphase’’orthe‘‘Reynoldsstresses’’turbulence
Thefuelconversionissimulatedbythreeheterogeneousreac- models are more appropriate. The ‘‘per phase’’ turbulence model
tions. The first one is depicted in Eq. (14) and refers to moisture adds two more PDEs, pergranular phase, in the set of equations.
evaporation/boiling.Thesecondheterogeneousreaction,depicted These additional equations describe kt and et of granular phases.
in Eq. (15), describes the volatiles release (devolatilization). The The Reynolds stresses model adds six more PDEs per Eulerian
thirdoneisthecharcombustion. phase.Thecomputationalcost incrementdue tothose additional
equationsmakestheirapplicationdifficultespeciallyoncombust-
boiling
H 2 OðsÞ ! H 2 OðgÞ ð14Þ ingflow simulations ofCFBCs,becausethecomputationalcost of
such simulationsisvery highand any further increase shouldbe
v ol:ðsÞ devola ! tilizationv ol:ðgÞ ð15Þ avoided.Therefore,Nikolopoulosetal.andZhouetal.[25,26],have
usedthek–edispersedturbulencemodelinCFBCCFDsimulations.
Moreover,threehomogeneousreactionsareincorporatedinthe Theresultsofthesestudiesdepictedthatthissimplifiedturbulence
model, simulating the combustion of CH 4 [17], H 2 and CO [28]. modelcouldbeusedinFBsmodeling.
Homogeneous reactions are described via Eqs. (16)–(18) along Exceptforthehomogeneousreactionsdescribedaboveheteroge-
with reaction rates expressions. The constants of these reactions neousreactions,i.e.moistureevaporation,devolatilizationandchar
are summarized in Table 1. The Reaction rate (R) is expressed in combustion,takeplaceaswellinsideaCFBC.Themoistureevapora-
Kmol[m3
gas
s](cid:3)1andtheuniversalgasconstantR
u
inJ[KmolK](cid:3)1.
tion/boilingrateiscalculatedthroughEq.(21)asreportedbySofial-
CH
4
þ 3
2
O
2
!COþ2H
2
O;R¼Ae(cid:3)Ru E Tg½C
CH4
(cid:5)0:7½C
O2
(cid:5)0:8 ð16Þ i
l
d
on
is
g
e
a
t
s
a
t
l.
h
[
e
3
r
1
e
]
i
.
s
It
m
is
oi
e
s
n
tu
a
r
b
e
le
i
d
n
f
t
o
h
r
e
te
so
m
li
p
d
er
p
a
h
t
a
u
s
r
e
e
.
g
T
r
h
e
e
at
fi
e
r
r
s
t
t
h
t
a
e
n
rm
37
w
3
i
K
th
a
in
s
H
2
þ 1
2
O
2
!H
2
O;R¼Ae(cid:3)Ru E Tg½C
H2
(cid:5)½C
O2
(cid:5)0:5 ð17Þ b
cl
r
e
a
s
c
i
k
n
e
t
t
h
s
e
in
co
th
n
e
tr
r
o
i
l
g
v
h
o
t
l
h
u
a
m
n
e
d
.
s
T
i
h
d
e
e
s
r
e
e
c
p
o
r
n
e
d
se
t
n
e
t
r
s
m
th
re
e
p
n
r
u
e
m
se
b
n
e
ts
r
t
o
h
f
e
fu
m
e
o
l
i
p
s
a
tu
rt
r
i
e
-
COþ 1 2 O 2 !CO 2 ;R¼Ae(cid:3)Ru E Tg½C CO (cid:5)½C O2 (cid:5)0:25½C H2O (cid:5)0:5 ð18Þ e E v u a le p r o ia ra n ti f o o n rm ra u t l e a p ti e o r n p , a a r ll ti f c u l e e l .I p t a s r h t o ic u le ld s b w e it u h n in de a rl s i p n e e c d ifi th c a c t o d n u t e ro t l o v t o h l e -
umesharethesameproperties.Moreover,itshouldbeunderlined
ThereactionsratesdepictedinEqs.(16)–(18)refertothepure
thatthenecessaryheatforthisreactionisprovidedbythegasphase.
kinetics of the reactions and are accurate only if the respective
r l t e h e n a e c c e t C a F a n D n ts d m a t o r h e d e e f e l u f l f t l e h y c r t o m u o i g f x h m ed t i . x h i S e n p g E e d c o i d n e y s re d m a is c ix s t i i i p o n n a g ti r i o s a n t c e o s m n i o t s r d o i e n l l l c e o [ d 3 rp 0 b o ] y . ra I t n t u e r d t b h u i i n s - m_w f ¼ pq 6 f m (cid:4) f d3 p ! (cid:3)p(cid:4)d p (cid:4)Nu pc K p p p s s (cid:4)ln (cid:4) 1þ c pps (cid:4) 1 ðT (cid:3) g L (cid:3) w T ps Þ (cid:5)!
model, the rate of production of species i due to reaction r, (R ) ð21Þ
i,r
isgiven by thesmallerof thereactionrates providedby thetwo
InEq.(21),thethermalconductivity()andheatcapacity()for
expressions below (Eqs. (19) and (20)). The empirical constants
thewateratthesurfaceoftheparticlearecalculatedforatemper-
A andB , involvedin theseequations,are setequalto4and0.5
E E atureequaltoT =T+1/3(T (cid:3)T)[31]throughpropertemperature
ps f g f
respectively. The reaction rate introduced in the CFD model is
polynomials [32]. Nu number in Eq. (21) is calculated as
the minimum predicted by the finite rate and the eddy dissipa- Nu =2+0.5Re0.5.
p
tion-model.
Regardingreaction15,thechangeinmassofthesolidphasein
et Y eachcomputationalcell,duetodevolatilization,iscalculatedbya
R i;r ¼m0 i;r M w;i A E q gk g t g m R in m0 R;r M R w;R! ð19Þ s re im ac p t l i e on on co e n s s t t e a p n r t e s, a A ction (4 m 92 o , d 0 e 0 l 0 a s c (cid:3) c 1 o ) r i d s in th g e to pr E e q -e . x (3 p . o 7 n 5 e ). n A ti s al re fa g c a t r o d r s ,
vol
R i;r ¼m0 i;r M w;i A E B E q gk et g t Nv PR 00 Y M PR ð20Þ a e n rg d y E o v f ol t ( h 7 e .4 d (cid:6) ev 1 o 0 la 7 t J i / l k iz m at o i l o ) n [3 re 3 a ] c i t s io th n e . correspondingactivationen-
g Pj j;r w;j
tob
A
e
s
a
s
b
e
l
e
e
n
t
i
o
n
c
E
a
q
lc
s
u
.(
la
1
t
9
e
)
t
Pa
h
n
e
d
r
(
e
2
a
0
c
)
t
,
io
a
n
nd
ra
a
t
r
e
e
s
r
t
e
h
q
r
u
o
i
u
r
g
ed
h
a
th
s
e
in
E
p
d
u
d
t
y
si
d
n
is
o
s
r
i
d
p
e
a
r
-
m_ devol ¼
p
6
(cid:4)q
(cid:4)m
(cid:4)
f
d3 !
(cid:4)Avol (cid:4)e(cid:3)Evol=RuTf (cid:4)Yvol ð22Þ
f f
tionmodel.Therefore,anappropriateturbulencemodelshouldbe
incorporated in the CFD model in order to efficiently and accu- The most important reaction in CFBCs is the char combustion
ratelycalculatetheeffectofturbulentmixingonreactionrates. that incorporates the oxidation of char to carbon monoxide and
The k–e dispersed turbulence model is the appropriate model dioxide[34].The/ c parametercontrolsthecharconversiontocar-
whentheconcentrationsofthesecondaryphasesaredilute.Fluctu- bondioxideandcarbonmonoxide:
atingquantitiesofthesecondaryphasescanthereforebegivenin
1 2 2
termsofthemeancharacteristicsoftheprimaryphaseandtheratio CðsÞþ O ðgÞ! 2(cid:3) CO þ (cid:3)1 CO ð23Þ
/ 2 / 2 /
oftheparticlerelaxationtimeandeddy-particleinteractiontime. c (cid:4) c(cid:5) (cid:4) c (cid:5)
The/ parameterisreportedasafunctionofparticlesize[33]
Table1 c
andrangesfrom1to2.Incontrasttomoistureboilinganddevol-
Homogeneousreactionconstants[17,28,29].
atilization,charcombustionkineticsaremorecomplicated.Inthe
Reactions A(varyingunits) E(J/Kmol)
latter reaction, two controlling mechanisms exist. The first is the
Eq.3.67(CH4) 5.012(cid:6)1011 2(cid:6)108 reactionkineticsandthesecondisthediffusionofoxygenintopar-
Eq.3.68(H2) 9.87(cid:6)1015 3.1(cid:6)107 ticlessurfacerepresentedbyk andh respectively.Eqs.(24)and
Eq.3.69(CO) 2.239(cid:6)1012 1.7(cid:6)108 c m
(25)describethecharcombustionmechanismadopted[34].

Author's personal copy
A.Nikolopoulosetal./Fuel115(2014)401–415 405
m_ ¼ p(cid:4)d2 (cid:4) P O2ðgÞ ð24Þ considered a widely approved method for predicting nitrogen
char c 1 þ1 oxideemissions,buthasneverbeenappliedtoCFBCmodeling,in
(cid:2) (cid:3) hm kc
D thebestoftheauthors’knowledge.Inpreviouslypublishedpapers
h m ¼12u c Sh d O R 2ðg T Þ ð25Þ concerning CFB plants, NO x numerical investigation is performed
c u
coupled with combustion simulation [17,38–41]. In this work,
InEq.(25)thatdescribesthediffusionrateconstant,theuniver- thedecoupledapproachisselectedinordertominimizethecom-
salgasconstantunitsarekPam3[kgK](cid:3)1.Eq.(26)[34]depictsthe putationalcostanddetermineifitcanbeusedinCFBboilers.The
kineticrate.ThesetworatesarecombinedinEq.(24).Themecha- generictransportequationformultiphaseflowissolvedfor5spe-
nismsthattheyrepresent,oxygendiffusiononparticlesurfaceand cies,i.e.NO,HCN,CNO,N OandCO.
2
reactionkineticsareconsideredthatareactingsimultaneously(in
@e q Ysp
parallel). g g þr(cid:4)ðe q~u YspÞ(cid:3)r(cid:4)ðe CrYspÞ¼S ð30Þ
@t g g g g
k ¼0:0117expð(cid:3)2859=T Þ ð26Þ
c p ThediffusiontermCforturbulentflowsisgivenas:
Sh¼ R c ð D m O2 = ð s gÞ Þd c¼2e g þ0:69 " j~u g (cid:3) e g ~u l s j g q g d c # 0:5 Sc0:33 ð27Þ C¼q g D iff þ l Sc t ð31Þ
l
Sc¼ g ð28Þ where Sc = 0.7 [42] and the turbulent viscosity is calculated as
q g D O2ðgÞ shownbelow:
Regarding the change in fuel particle volume during combus- kt2
l ¼0:09q ð32Þ
tion, the shrinking core approximation is adopted. The shrinking t g et
diameter of char (d) is calculated through Eq. (29) that incorpo-
c InEqs.(30)–(32),q ;e ;~u ;ktandetare‘‘frozen’’variables,equal
ratesthetimeinstantcarbonburn-off(U ),asproposedbySmith g g g
fc to the respective combustion model results for each control vol-
[35].
ume.ThroughouttheNO–N O modelingprocedure,these values
x 2
d do notchange.VariableS(mg ofspeciesper cubicmeterper sec-
d c ¼ð1(cid:3)U fc Þ 1 3 ð29Þ ond) represents the source term that takes into account all reac-
o
tionsofthenetworkthateachspeciesparticipate.Forexample,if
The shrinking core model is enabled during char combustion
the intermediate gaseous species CNO is involved in 3 reactions,
and during this process the fuel density is considered constant.
I, II and III, with corresponding reaction rates, RI, RII and RIII
Inwaterevaporationanddevolatilizationthediameterofthefuel
respectively,andinreactionICNOisaproductwhileinIIandIII
phaseisconsideredconstantandfueldensityisdecreasingpropor-
is a reactant, the source term which will be incorporated in the
tionallytotherespectivemassloss.However,whenthesereactions
transportequationofCNOis:.
are finished and char combustionis enabled, the particle density
This modeling approach is not supported by Fluent platform
doesnotfurtherincreasebuttheparticlediameterisdecreasing.
and therefore NO/N O decoupled model is incorporated in the
x 2
The simplified combustion model presented in this work as-
commercialpackageviaUserDefinedScalars(UDS),whilereaction
sumeshomogeneousconditionsineachcontrolvolumeforallvari-
ratesforallspeciesareincludedinthesourcetermofeachequa-
ables. Nevertheless, more sophisticated models should be
tionusingUserDefinedFunctions(UDFs).
developedforaprecisenumericalrepresentationofthecombust-
The decoupled NO model comprises of 5 partial differential
x
ingflow,takingintoconsiderationflowheterogeneityineachcom-
equationandthecomputationalcostprovedtobearound1month
putationalcell.
inastandarddesktopdualcore2.4GHzPCwith4GbofRAM.The
Eventhissimplifiedcombustionmodelisrathercomputational
CPUcostishigherthantheoneexpectedbecauseofthenumerical
expensiveasitisasetof27partialdifferentialequations.Combus-
stiffness of the model. However, the decoupled model is by far
tionsimulationrununtilsolidsinventory,temperatureandspecies
moreefficientcomparedtotheapproachofthesimultaneoussim-
massfractionsreachedequilibrium.Thistimeperiodprovedtobe
ulationofhydrodynamic,combustionandNO mechanisms.
x
rather high, around 200s. After reaching this ‘‘steady’’ state an-
other20sweresolvedinordertoaveragescalarsandderiverep-
2.2.1.InvestigationofNO/N Oformation-destructionmechanisms
x 2
resentativemeanvalues.Therealtimeforthesecalculationswas
FortheNO/N Oformationmechanisms,combustionofcoalis
x 2
10monthsina standarddesktopdualcore2.4GHzPCwith4Gb
separated into two stages, the initial stage of devolatilization,
ofRAM.
and the subsequent burning of the char. During devolatilization,
hydrocarbonspecies(CH ),hydrogen(H ),watervapor(H O),car-
x y 2 2
2.2.NO/N Osimulationmethodology bon monoxide, carbon dioxide (CO, CO ) and tars are released,
x 2 2
while the ring structures containing nitrogen decompose, and as
ThedecoupledapproachisproposedforthecalculationofNO/ aresult,nitrogenisreleasedintheformofHCN,NH ,N andtar-
x 3 2
N Oconcentrations.Accordingtothistechnique,theconcentration boundednitrogen[9,43].
2
ofnitrogenoxidesproducedinacombustionsystem,isgenerally Devolatilizationtakesplaceonthelowerpartsofthebed,par-
verylow,thatthechemistryofnitricspeciesandtheirinteraction ticularly around fuel insertion area. Fuel particles, after entering
withothergasesinthecombustionchamberhasminimaleffecton the combustion chamber, are instantaneously heated with high
theconcentrationsofthemainproductsofcombustionandonthe ratesbythemuchhotterparticlesofthebed,duetogoodmixing
estimatedflowfieldandtemperaturedistribution[29].Thus,NO conditions and temperature uniformity. Devolatilization is then
x
calculationcanbedecoupledfromthecombustionmodeling.This followedbythestageofcharcombustion,whichlastsmuchlonger
assumption means that the simulation of NO/N O formation andconcernstheburningoftheresidualfuel.
x 2
mechanisms is achieved by using the prescribed initial fields of Fuelnitrogenfollowsthesamepath.Onepartisreleasedinvol-
velocity,fuel/solids,speciesdistributiontakenfromtheCFBcom- atiles,whiletherestremainsinthechar.AsproposedbyGoeletal.
bustionsimulation. [44],thedistributionoftheinitialfuelnitrogen(fuel-N)involatile
The NO decoupled approach has been adopted in previous nitrogen (volatile-N) and char nitrogen (char-N) strongly influ-
x
studies concerning NO modeling in PF boilers [2,36,37]. It is ences the final emissions of nitrogen oxides. This distribution
x

Author's personal copy
406 A.Nikolopoulosetal./Fuel115(2014)401–415
importance[46],asconcernsthefinalNO/N Oemissionsbecause
2
these species (HCN/ NH ) are considered the main precursors of
3
nitrogenoxides.Inmodelingstudies,asimplisticempiricalmeth-
odology is used for setting this ratio that defines the N-products
ofdevolatilization.Thissimplificationdependsgreatlyonthefuel
investigated. For example, species volatile ratio of HCN: NH for
3
bituminous coal is usually 9–1 [47], while for biomass, 1–9
[4,39].Fromtheliteratureviewpoint,therefore,itisproposedthat
forcoalcombustion,whichisthefuelofimportanceinthepresent
study, the main product of devolatilization is hydrogen cyanide
(HCN).Moreover,theammoniaconcentrationwhichwasobserved
duringtheexperimentsoftheunitinstudywastoolow[33].For
thesereasons,inthiswork,itisassumedthatvolatilenitrogenap-
pearsonlyintheformofhydrogencyanide.
Nitrogenoxidesareformedduringbothcharandvolatilescom-
bustion.Allreactionstakingplaceinsidethebedandconcernthe
Fig.1. MechanismofNO/N2Oformationinfluidizedbedcombustionofcoal.
nitrogenpath, are summarizedin Fig. 1 and consist of four main
mechanisms:
dependsgreatlyonfueltype.AccordingtoWójtowiczetal.[7],for
coal combustion, approximately60% oftheinitialfuel-Nremains (cid:2) NO/N 2 Oformationviahomogenousreactions.
inthechar.Duetolackofexperimentaldatafortheratioofvola- (cid:2) NO/N 2 Odestructionviahomogenousreactions.
tile-Ntochar-Nofthefuelinvestigated,itwasassumedthat43%of (cid:2) NO/N 2 Oformationviaheterogeneousreactions.
theinitialNisreleasedinvolatiles,avaluewhichisobtainedfrom (cid:2) NO/N 2 Odestructionviaheterogeneousreactions.
theworkofFineetal.[45],whoexaminedthisratioasafunctionof
operating temperature. This value is also in agreement with the 2.2.2.Reactionnetwork
workofWójtowiczetal.[7].Likewise,theratioofhydrogencya- InTable2themainreactionsoftheschemeshowninFig.1are
nide (HCN) to ammonia (NH 3 ) released in volatiles is of great presentedalongwithreactionrates,constantsandmodelparame-
Table2
ReactionnetworkforthemodelingofNOandN2Oformationfromcoalcombustion.Gasspeciesconcentrationinmolpercubicmeterofgasphaseandtheuniversalgasconstant
(Ru)iskJ[molK](cid:3)1.
No. Reaction Parameters Rateexpression(mol=m3 s) Refs. Usage
gas
Model1 Model2
Homogenousformation
I HCNþ1 2 O2!CNOþH kI=2.14(cid:6)105(cid:4)exp((cid:3)10,000/T) kI(cid:4)CO2 (cid:4)CHCN [17,38,39] Yes Yes
II CNOþ1 2 O2!NOþCO k k I 2I 1 I I ¼1:02 (cid:6) 109(cid:4)expð(cid:3)25;460=TÞ kI(cid:4)CO2 (cid:4)CHCN(cid:4) (cid:4) kI I Iþk k I 2 I I I I (cid:4)CNO(cid:5) [17,38,39] Yes Yes
III CNO+NO?N2O+CO kI(cid:4)CO2 (cid:4)CHCN(cid:4) (cid:4) kI I I k þ I 2 I k (cid:4)C I 2 I N (cid:4)C O NO(cid:5) [17,38,39] Yes Yes
IV NH3þ5 4 O2! NOþ3 2 H2O kIV=2.73(cid:6)1014(cid:4)exp((cid:3)38,160/T) kIV(cid:4)CNH3 (cid:4)CO2 [17,39,40] No No
Homogenousdestruction
V NH3+3/4O2 ?1/2N2+3/2H2O kV=3.38(cid:6)107exp((cid:3)10,000/T) kV(cid:4) CNH3(cid:4)CO2 [17,38] No No
CO2 þ0:054
VI NOþNH3þ1 2 O2!N2þ3 2 H2O kVI=1.11(cid:6)1012(cid:4)exp((cid:3)29,400/T) kVI(cid:4)ðCO2 (cid:4)CNH3 (cid:4)CNOÞ0;5 [17,38,39,48] No No
VII N2Oþ1
2
O2! N2þO2 kVII=1.75(cid:6)108(cid:4)exp((cid:3)23,800/T) kVII(cid:4)CN2O [6] Yes No
VIII N2O+CO?2N2CO2 k kV V I I I II = = 5 2 . . 7 51 (cid:6) (cid:6) 10 1 9 0 (cid:4) 1 e 1 x (cid:4) p ex ( p (cid:3)2 ((cid:3) 7, 2 0 3 0 , 0 1 / 8 T 0 ) /T) k k V VI I I I I (cid:4) (cid:4) C C N N 2 2 O O(cid:4)CCO [ N 3 o 9] N N o o Yes
kVIII=50.1(cid:6)1011(cid:4)exp((cid:3)5292/T) kVIII(cid:4)CN2O(cid:4)CCO [17] No Yes
Hetrogenousformation
IX char(cid:3)Nþ1
2
O2!ð(cid:3)CNOÞ Yes Yes
X ð(cid:3)CNOÞþ1 2 O2!NOþð(cid:3)COÞ k k X 2X 1 ¼4:86 (cid:6) 10(cid:3)5(cid:4)expð14;999=TÞ fc N C (cid:4)Rc(cid:4) (cid:4) kX 1þk k X 2 X 1 (cid:4)CNO(cid:5) [46] Yes Yes
XI ((cid:3)CNO)+NO?N2O+((cid:3)CO) fc N C (cid:4)Rc(cid:4) (cid:4) kX 1 k þ X 2 k (cid:4)C X 2 N (cid:4)C O NO(cid:5) [46] Yes Yes
Hetrogenousdestruction
XII NOþð(cid:3)CÞ!1 2 N2þCO kX a II¼1:3 (cid:6) 105(cid:4)expð17;111=TÞ kX a II(cid:4)Np(cid:4)p(cid:4)d2 c (cid:4)CNO(mol/s) [17] Yes No
kX
b
II¼1:17 (cid:6) 108(cid:4)expð(cid:3)13;221=TÞ kX
b
II(cid:4)CNO(mol/m3-fuels) [46] No Yes
XIII NOþð(cid:3)COÞ!1
2
N2þCO kXII=2.51(cid:6)1011(cid:4)exp((cid:3)10,000/T) kXIII(cid:4)CNO(cid:4)CCO [38] Yes Yes
XIV N2O+ ((cid:3)C)?N2+CO kXIV=2.9(cid:6)109(cid:4)exp((cid:3)16,983/T) kXIV(cid:4)Np(cid:4)p(cid:4)d2
c
(cid:4)CN2O(mol/s) [17] No No
kXIV(cid:4)CN2O(mol/m3-fuels) [38] No Yes
ThermalNOx
XV N2+O2 ?2NO BasedonZeldovichmechanism[29] [32] Yes Yes
Fuelnitrogen
XVI
N(cid:3)
v olatilesd!evolHCN Rvol Yes Yes
XVII N-char?HCN ð1(cid:3)fcÞN
C
(cid:4)Rc Yes No

Author's personal copy
A.Nikolopoulosetal./Fuel115(2014)401–415 407
ters. Two different reaction networks are tested, simply entitled and V are catalyzed by the presence of char particles and inert
model1andmodel2.Themaindifferencesbetweenthetwomod- bedmaterial.
elswillbediscussedlaterinthissection. The homogenous reactions concerning the reduction of nitric
For the fuel investigated in the 1.2MW CFBC plant, in a dry oxidearenotimportantunderfluidizedbedoperatingconditions,
th
ashfreebase,theNitrogentocarbonmolarratio(N/C)wasmea- asitisextractedfrompreviousworks[7,38,39,48].Theonlyreac-
suredequalto0.84584%.ThefractionofNitrogenwhichisreleased tion mentioned by Jensen et al. [48] and adopted by Desroches-
in volatiles was not experimentally measured. This important Ducarneet al.[38], Gungorand Eskin[17], Liu and Gibbs [39], is
parameter is calculated, as discussed above, through the work of the homogeneous destruction of NO in the presence of ammonia
Fineetal.[45]whomeasuredexperimentally,underpyrolysiscon- andoxygen(reactionVI).
ditions,thisfraction,forawiderangeoffossilfuels,andtheycon- The homogenous reduction of N O is temperature dependent
2
cludedthatitisafunctionofoperatingtemperature.Basedonthis [4].Atlowcombustiontemperatures((cid:7)1000–1200K),i.e.typical
workandtakingintoaccountthenumericallyinvestigated(822(cid:3)C) fluidized bed operating conditions, the homogenous destruction
operatingtemperatureoftheCFBCunit,thefractionofNitrogenre- mechanisms are not drastic. On the contrary, for temperatures
leasedinvolatilesisfoundequalto43%oftheinitialNitrogencon- higher than 1200K, N O is rapidly decomposed (almost immedi-
2
tentoftherawfuel.TherestoffuelNitrogenisconsideredaschar atelyafteritsgeneration)byO,OH,Hradicals.Themostimportant
bounded.Theremainingchar-boundednitrogencanundergotwo reactionsconcerningthehomogenousdestructionofN Oarepre-
2
different reaction paths as well. One part is released in the form sentedinTable2(reactionsVII,VIII).
ofgaseousspecies(mainlyHCN),whiletheresttakespartinhet- Referringtothefirstreaction(homogenousN Odecomposition
2
erogeneousreactionswhichleadtotheformationofnitricspecies. -reactionVII),alotofexpressionsforreactionrateswerefoundin
ThefractionofcharboundedNitrogenwhichisdirectlyoxidizedto literature[6,17,39,41].Thesereactionrateexpressionsareallinthe
NO andN Oisestimated,andnotmeasured,byLeithneretal.[33] sameorderofmagnitude,withtheonlyexceptionoftheexpression
x 2
tobeequalto30%.Therest(70%)isreleased,duringcharcombus- proposedbyGungorandEskin[17].Thereactionrateproposedby
tion, in the gas phase as HCN. These values are used in the pro- GungorandEskin,[17]wasfoundtobehigherthantheothersby4
posed model. In order to summarize the path that fuel nitrogen orders of magnitude. On the other hand, nitrous oxide reduction
is assumed to take in the present study, 43% is volatile-N, while afterreactionwithcarbonmonoxide(CO)wasreportedinthework
therest57%isdividedto30%char-N,and70%char-Nthattrans- ofMukadietal.[41],Chenetal.[6],GungorandEskin[17].
formstoHCN. Finally,concerningheterogeneousreactions,plentyofresearch
Inorderto calculatetherate ofmostheterogeneousreactions hasbeencarriedoutduetothecomplexityoftheirnature.Influ-
whichappearinthereactionsnetwork,thenumberoffuelparti- idizedbedcombustion,duetothepresenceofsolidinertandfuel
cles (N ) should be calculated, in order to calculate the effective particles, heterogeneous and catalytic reactions are of utmost
p
surfacearea(N pd2).InaLagrangianframe,thismeasureiseasily importance to the formation and destruction of nitrogen oxides.
p
calculated because particles or parcels of particles are tracked. According to literature, nitrogen oxides are heterogeneously
However,inanEulerianframe,astheoneusedinthisworkinor- formed following two different paths: (a) char-N oxidation and
der to simulate particulates, N cannot be calculated straightfor- (b)oxidationofHCN(ReactionXVII).
p
ward.Usually,theeffectivesurfaceareaiscalculatedastheratio
ofthevolumeoftheEulerianphaseineachcelltothevolumeof (cid:2) Asconcernspath(a),itisproposedbyChenetal.[6]andGoel
a single particle based on its initial diameter (d ). However, this et al., [44,51], and adopted by other researchers [39,46] that
o
treatmentover-predictsthesurfacearea.Therefore,analternative oxygen breaks the nitrogen containing aromatic rings bound
approachisadopted.Thenumberofparticlesiscalculatedforthe tothecharsurfaceandthenreactswiththefreenitrogenatoms
diameteroftheEulerianphase(d ),buttheactivesurfaceareais toformanactiveintermediate,suchas–CNO,stillboundedon
o
calculatedusingd. thecharsurface.Thisactiveintermediatedecomposestoform
c
NO,orreactswithNOtoformN O(reactionsIX,X,XI).Thisthe-
2
6eV ory which was proposed for the heterogeneous formation of
N pd2¼ f celld2 ð33Þ
p c d3 c nitrogen oxides by the oxidation of the active intermediate –
0 CNOissimilartothehomogenousdestructionofgaseousinter-
Table2presentsthereactionpaththatfuel-Nundergoesinside mediateCNO.Thereactionrateadoptedinthisworkforthese
aCFBboiler.Productsoffueldevolatilization,i.e.hydrogencyanide reactions was proposed by Kilpinen et al. [46] who estimated
(HCN)and ammonia(NH ),play animportantroleactingasgas- newexpressionsforthekineticconstantsandcomparedthem
3
phase precursors for both NO and N O and these homogeneous to the previous ones given by Goel et al. [44,51]. Tullin et al.
2
reactionpathwayshavebeenextensivelystudied.HCNisoxidized [52] proposed that the nitrogen (N) and carbon are oxidized
toformanintermediatespecies,NCO,whichcanyieldeitherNOor at relative rates that are in proportion to the nitrogen/carbon
N O[49](reactionsI,II,III).Asfarasthisschemeisconcerned,var- atomicratio(N/C)inthechar.Forthisreason,therateofheter-
2
ious authors [38,39,46] have reached to an agreement about the ogeneous formation of nitrogen oxides is multiplied by char
reactionrates. combustionrate,asshowninTable2.
Nitricoxide(NO)isalsoformedbytheoxidationofNH (reac- (cid:2) Asconcernspath(b),itisobservedthatHCNnotonlyisreleased
3
tionIV),whilehardlyanyN Oisformedfromammonia-basedfuel involatiles,butalsoduringcharcombustion[47,49].Thispro-
2
nitrogenradicals(NH).Thisconclusionwasmadebyexperiments cessiscalledsloworsecondarydevolatilization.Hydrogencya-
i
carriedoutbyKilpinenandHupa[49]andKramlichetal.[50],who nidecanthenundergohomogenousoxidationtoformeitherNO
injectedammoniaandhydrogencyanideinfuel-leanfluegasfrom orN Oasdiscussedabove.However,intheirwork,Goeletal.
2
burning coal and natural gas respectively. The researchers con- [51], showed,after seriesofexperiments,thatcyanidespecies
cluded that N O was preferentially formed from cyanide species, arenotreleasedinsignificantamountsduringcharcombustion
2
whereasverylittleN OwasreleasedduringNH injection. and that the formation of nitric and nitrous oxides derive
2 3
For reactions IV, V, VI containing ammonia, many researchers almost entirely from the oxidation of char-N. The fuel which
[38–40,48] agree on reaction rate expressions. Most authors use theyusedfortheexperimentswasNewlandcoal.Thecontribu-
the expressions derived from the work of Jensenet al. [48], with tion of HCN released during char combustion to the final NO/
slight modifications. It should be underlined that reactions IV N Oemissionsmaydependonthefuelused.
2

Author's personal copy
408 A.Nikolopoulosetal./Fuel115(2014)401–415
In this work, two different models are adopted (Table 2). In simulation. Transport equations are solved using the implicit
model 1, it is assumed that 30% of char-N is oxidized directly to
method,withtimestepofDt=10ls.
formNOorN 2 O,asestimatedbyLeithneretal.[33],whiletherest Diffusioncoefficient(D iff )isdifferentforeachgas.However,be-
isreleasedintheformofHCN.Thisvaluewasusedinaprevious causeoflimiteddatapublishedforthediffusionofchemicalspe-
simulationwhichwascarriedoutintheframeoftheexperimental cies during combustion in fluidized bed, D iff is set equal to
report [33]. In model 2, the assumption of Goel et al. [51] is
6.8(cid:6)10(cid:3)6m2s(cid:3)1forallspeciessolved,derivedfromtheworkof
adopted, according to which 100% of char-N is oxidized to form Kilpinen et al. [46]. However, for the purpose of this study other
NOandN O.Therefore,inordertosummarizethebasicdifferences
valuesforthiscoefficientwerealsotested.Avalueof10(cid:3)04,pro-
2
between these 2 Models, in Model 1, 43% of fuel-N is volatile-N, posedbyTullinetal.[52],wasapplied,butnodifferencewasob-
whiletherest57%isdividedto30%char-N,and70%whichisre- served in the results. This can be attributed to the high gas
leased in the form of HCN, whereas in Model 2 the remaining
velocityinthebed(approximately5–15ms(cid:3)1onthemainz-axis).
57%isassumedtobeallchar-N. Therefore, for the species transport equation it is concluded that
Heterogeneousreductionofnitrogenoxidesoncharsurface,as theconvectivetermisdominatingoverthediffusionterm.
authorssuggest[44,53],isoneofthemostimportantreactionsina Asthedecoupledapproachisadopted,profilesoftemperature
fluidizedbedreactor,whichinfactinfluencesthetotalamountof (T),charcombustionrate(R c ),volatilereleaserate(R vol ),chardiam-
NO x –N 2 Oemissions.Bonnetal.[54],proposedthatalmost60%of eter(d c )andO 2 concentrationinsidethebedareobtainedfromthe
the total N O formed in a fluidized bed is decomposed on char solutionofthecombustionsimulation.
2
surface.
Reaction XII, namely NO reduction on char surface, describes
theabsorptionofonemoleculeofnitricoxide(NO)fromanactive 3.1.2MWthCFBCUnitdescription
siteofthechar(–C)inordertoformmolecularnitrogen.Reaction
XIVissimilarwithreactionXIIandconcernsthereductionofni- Inthiswork,a1.2MW th pilotplantissimulated.Theunitsche-
trousoxide(N O)oncharsurface.However,afterthoroughexam- matic diagram is depicted in Fig. 2. The installation has 9.5m
2
inationofpreviousworks,ageneraldisagreementinreactionrate height and 0.4m2 mean cross section. The combustion chamber
expressionsforthesereactionsisobserved.Itissuggestedthatthe oftherigconsistsoftwosections.Thelowerpart(thefurnacehop-
differencebetweenrateexpressionscanbeattributedtothediffer- per) has a height of 3.15m. It is totally refractory lined and the
entfuelswhichwereusedfortheestimationofthekineticparam- crosssectionincreaseslinearfrom0.39(cid:6)0.45m2atthedistribu-
eters.ReactionratesforreactionsXII,XIVcanbefoundinalotof torplateto0.54(cid:6)0.81m2atthetopofthehopper.Theupperpart
previousworks[6,17,38,39,41,46]. (the rectangular freeboard) has a constant cross section of
In reaction XIII, one NO molecule binds to the surface of char 0.54(cid:6)0.81m2andaheightofabout6.35m.Threeoutofthefour
forming the intermediate active compound (–NO), which reacts freeboard walls are refractory lined. The temperature of the one
withtheintermediate(–CO)respectivelytoformmolecularnitro-
gen(N ).WheneverNOandCOmoleculesarepresentnearthesur-
2
face of char, reaction XIII is catalyzed. Jensen et al. [48], indicate
that this reaction is also catalyzed by solid particles of the bed.
ReactionsrateexpressionsforreactionXIIIarefoundinthework
of [6,17,38–40,46,48]. Actually, nitric oxides can be also formed
viaaseriesofcatalyticreactionsonthesurfaceofothersolidpar-
ticles present in the combustion chamber, except char particles.
However, these reactions exceed the purpose of this work and
thereforearenotincludedinthesimulationmodels.
AsshowninTable2,notallreactionsareusedinthetwomod-
elswhichweretested.Specifically,reactionsIV,VandVIcontain-
ingammonia(NH )werenotincludedbecauseasitwasdictated
3
fromtheexperimentaldata[33],thatthemainproductoffueldev-
olatilization was hydrogen cyanide (HCN) while ammonia (NH )
3
was produced in small negligible concentrations, as mentioned
before.
InModel1,reactionsVIIIandXIVarenotincorporated,dueto
theunderpredictionofnitrousoxideformationasitisdiscussed
intheresultssection.Finally,reactionXV(thermalNO),isincor-
x
poratedinthechemicalreactionnetworkinordertodemonstrate
itsexpectedlowcontributiontotheformationofNO.
x
2.2.3.NO/N Osimulationmethodology
x 2
Zero initial concentration is assumed for all five gases within
thebed,exceptforcarbonmonoxide(CO).Theinitialconcentration
ofCOisobtainedfromthesolutionofthecombustionmodel,be-
causeitisaproductofcombustionprocessandthereforeitsforma-
tion cannot be simulated with one reaction rate. Thus, it is
assumed that the amount of CO released during combustion is
independentoftheCOreleasedbychemicalreactionsinvolvedin
theNO–N OschemedepictedinTable2.InCOtransportequation,
x 2
the mass flux function (the convectional term) is set to zero, in
order to retain the CO concentration profile of the combustion Fig.2. Schematicdiagramofthe1.2MWthCFBCinstallation.

Author's personal copy
thatisnotrefractorylinedis610K.Thistemperaturereferstothe Table4
outersurfaceofthetubesthatisfacingthebed.Combustionairis Airstaging.
fed as primary air through the distributor plate, while additional Inlet Volumeflow(m3/ Portheight
primary air is fed into the bottom region of the furnace hopper h) (z)
with the fuel and the recirculated bed material. Secondary air is Distributer 828@501K 0
fedthroughfiveinletsalongtheheightofthecombustioncham- Solid(inert-materialandfuel)feed 202@501K 0.7
ber.Theratioofprimarytosecondaryaerationis86–14%[33]. port
Secondaryair1 199@501K 0.5
Inthiscomprehensivemodelgas,inert-materialandfuelareta-
Ignitionburner 121@501K 2.15
kenintoconsideration,asthreediscrete,pureEulerianphases,asit
Secondaryair2 32@501K 2.8
canbeseeninFig.3.Majorgaseouschemicalcomponentssuchas Secondaryair3 34@501K 5.6
O ,CO .H O,N ,volatiles,CO,CH andH aredefinedforcombus- Secondaryair4 36@501K 7.6
2 2 2 2 4 2
tionsimulationandHCNforNO/N Odecoupledsimulation.Spe-
x 2
ciesarealsodefinedwithinthefuelphase,i.eash,water,volatiles
andchar. throughthedistributerandthesecondaryairinlets.Therespective
Itisworthmentioningthatthecommercialsoftware(Fluent(cid:4)) flowsaredepictedinTable4.
used in this work does not support combusting or reacting flow
simulationundertheTFMpureEulerianframe.Therefore,thereac-
tionratesoftheinvolvedreactionsarecodedandincorporatedin 4.Resultsanddiscussion
Fluent(cid:4)platformthroughproperUDFs.
Thecomputationalgridconsistsof5724hexahedral,structured 4.1.Combustion
and uniform cells, with a mesh resolution of 9cm per computa-
tionalcell.Thereturningsystemhasbeenexcludedfromthesim- Asetof25partialdifferentialequationsgoverningthephenom-
ulation for simplicity. More information about this simplification enon,issolved.Thesetofequationspresentedaverystiffnumer-
andthenumericalgridcanbefoundinNikolopoulosetal.[10]. ical behavior. Therefore an efficient coupling among phases is
ParticleSizeDistributionintroductionforfuelphaseintheEule- foundcrucialintermsofnumericalstability.Ingeneral,thecom-
rianapproachisnoteasilyfeasibleintermsofcomputationalcost. prehensivecombustingmodelprovedtobemuchmorecomputa-
Therefore, fuel particles were considered and modeled as mono- tionalexpensivethantheisothermalflowmodel,butcertainlynot
sized, simplification which is expected to have an impact on the prohibitiveforapplicationinpilotscaleCFBCunits.
mostprecisedescriptionoftheinducedflowfieldandonheteroge- TheflowfieldinsidetheCFBriserwasinitializedfromthesolu-
neousreactionsthatareaffectedbyparticlesurface.Thefuelwhich tion of the corresponding isothermal case, in order to reduce the
wasusedfortheexperimentsisRhenishlignite.Proximateanalysis computationalcostforreachingsolidsinventoryandtemperature
conductedbyLeithneretal.[33],ispresentedinTable3.Itisworth stabilization.Unfortunately,thequantityofinertmaterialintheri-
mentioningthatthesamplingportsforthegasconcentrationmea- serstartedtodecreaserapidly,movingawayfromtheequilibrium
surementsarelocatedatfourlevelsalongtheheightoftheriser(at state. Reaching equilibrium again was proved to be time
1.15,2.15,5.2and8.3mrespectively).Theairfuelratio(lambda)is consuming.
1.15whilethefuelenterstheriserwithaflowrateof0.14kg/sata The numerical methodology is validated with experimental
temperatureof373K.Thecombustionairinthisunitisintroduced data from Leithner et al. [33]. In their experimental campaign,
meanCO andO concentrationweremeasuredinthefourdiffer-
2 2
entheightsmentionedabove.Thesemeasurements,alongwiththe
numericalpredictionsforthesespeciesprofilesalongtheheightof
the combustor, averaged at each height, are illustrated in Figs. 4
and5.
The minimum, maximum and mean experimental values are
presented. In each height there were 9 available experimental
measurements in different locations, across each slice. An excep-
tionisthemeasurementsconductedfortheheightof2.15mwhere
onlytwomeasurementsareavailable.Unfortunatelyitisnotclear
bythereportofLeithneretal.[33], atwhichexactpointofeach
Oxygen concentration
25
20
Fig.3. EulerianphasesandspeciesincorporatedintheCFDmodelofCFBC.
15
Table3
Rhenishligniteproperties. 10
Proximateanalysis Ultimateanalysis
5
Moisture 57.00w% C 27.1
Volatiles 21.63w% H 1.92
Char 19.07w% O 11.18 0
Ash 2.30w% N 0.33 0 2 4 6 8 10
Meanfueldiameter 1500lm S 0.17
Height (m)
Heatingvalue(a.r.) 8560MJ/kg ash 2.3
Density(a.r.) 2400kg/m3 Water 57
Solid(inert-material)diameter 260lm
)ria
yrd-%
.lov(
negyxO
A.Nikolopoulosetal./Fuel115(2014)401–415 409
Exper.
Sim. Ave
Sim. Min
Sim. Max
Fig.4. Timeaveragedvolumetric(%dry)O2concentrationalongthebed(simulated
andexperimentalvalues).

Author's personal copy
1150
1100
1050
1000
950
900
850
800
750
700
650
600
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
X (m)
abovementionedheightareonlytwo.Theexperimentallyobserved
increase of mean oxygen concentration from Z=1.1m to
Z=2.15m,shouldbefurtherinvestigated,sincethereisnosecond-
aryairopeningplacedbetweenthesetwocross-sections.Therefore
anincreaseofoxygenconcentrationbetweenthesetwocrosssec-
tionsishighlyunlikelytooccursinceallreactionsinvolvedinlig-
nitecombustiondonotproduceoxygen.Inthislight,itisbelieved
thateitherthetwoexperimentalvaluesarenotrepresentativefor
this height or the two aforementioned experimental measure-
mentswerenotproperlyconducted.
In general the developed model predicts that O is consumed
2
faster close to walls where fuel concentration is higher (in the
annulusregion),thaninthecoreregionofthebed(Fig.7).Addi-
tionally in the core region O values are generally higher, which
2
isconsistentwithliterature[55].
Themeantemperatureinsidetheriserisaccuratelysimulated.
Ameanvalueof1095Kispredicted,whiletheexperimentaldata
report1100K[33].Thepredictedtemperaturefieldclearlyshows
uniformity.Gas,inert-materialandfuelphasetemperaturevalues
Fig.6. TimeAverageddryvolumetric(%)concentrationofO2forheight2.15m. areveryclosetoeachother,indicatingtheefficientheattransferin
thebed.Fig.8presentstemperatureprofilesalongtheheightofthe
bedforinertandfuelphases.Fuelphasegenerallyisfoundtohave
slice(X,Ycoordinates)thesemeasurementswereconducted.Figs.4 a slightly higher temperaturethan the otherphases at 5K maxi-
and5depictthattheagreementwiththeexperimentaldataisvery mum,ingeneral.Nonetheless,atheightZ=1mwherethefuelen-
good,exceptforthepredictionsfortheheightof2.15.Concerning ters the bed, there is a temperature difference between fuel and
thiscross-sectiondepictedin Fig.6, thenumericalapproachpre- inert phase which takes a maximum value of 350K. This is ex-
sentedinthisstudypredictsO 2 andCO 2 concentrationswithval- pected, since the fuel has not yet been heated at that point and
uesclosetotheexperimentaldataatcertainregionsofthisarea. has high moisture content (57%). Additionally near the riser exit
Nevertheless, it should be noted that for this height, the area atemperaturedifferenceof80K ispredicted,whichisattributed
weighted averaging of these quantities disagree with the corre- tofurtherlocalcharcombustionandresultsinfueltemperaturein-
spondingexperimentalmeanvalue.Nonetheless,theexperimental crease.Theincreasedcharcombustioniscausedbythemixingof
measurementsthatwereusedforderivingthemeanvalueofthe oxygen rich core region gasses with the fuel rich annulus region
Fig.7. TimeAverageddryvolumetric(%)concentrationofO2forX=0.405m.
)K(
erutarepmeT
CO2 concentration
25
20
15
10
5
0
0 2 4 6 8 10
Height (m)
Temperature distribution
Z=1m, fuel
Z=1m, inert material
Z=5m, fuel
Z=5m, inert material
Z=8m, fuel
Z=8m, inert material
Fig.8. TemperatureprofilesalongX(Y=0.27)axis,forinert-materialandfuelfor
differentheights.
)ria
yrd-
%
lov(
2OC
410 A.Nikolopoulosetal./Fuel115(2014)401–415
Exper.
Sim. Ave
Sim. Min
Sim. Max
Fig. 5. Time averaged volumetric (% dry) CO2 concentration along the bed
(simulatedandexperimentalvalues).

Author's personal copy
experimeent
Moodel2
Moodel2 mminimuun
Moodel2 mmaximum
9
Moodel1
8
aa)
7
6
5
4
3
2
1
0
600 400 200 0
NO Connc. (mg/m3)
x N
solids that takes place in the exit area. At the same time, inert
material at this height of the riser has very low volume fraction
whichleadstoadecreasedheattransfercoefficientandhightem-
peraturedifferencewiththefuelphase.Theconsiderablereaction
rateofcharcombustionattheexitpipeisalsoverifiedexperimen-
tally[33].
4.2.NO–N Omodelresults x 2
Results of the simulation for both models against the experi-
mental data are presented in the following figures. Fig. 9 depicts
theconcentrationofNO,togetherwithfuelconcentrationacross
x
the height of the bed. In this figure, the mass-weighted average,
minimumandmaximumofNO concentration,aswellasfuelcon-
x
centrationarepresentedforselectedsurfacesalongbedheight.
Results for NO concentration (Fig. 9a) seem to be in good
x
agreementwiththeexperimentaldataforbothModels,especially
near thedistributorplate and theoutlet. However, thetransition I+II) is the most importantpathway on the lower section of the
fromthesecondtothethirdpoint(from2.25to5.2m)doesnotap- bed, where HCN is released in high rates during devolatilization.
pearassharpasmeasuredduringtheexperimentalprocedure.This Devolatilizationtakesplacearoundfuelinjectionarea.Fuelparti-
smallincreasewhichispredictedbythesimulationcanbeproba- cles, after entering the combustion chamber, are instantaneously
bly attributed to the addition of secondary air at the height of heatedbythemuchhotterparticlesofthebedduetogoodmixing
5.6m, which dilutes the flue-gas and therefore leads to the de- conditionsandtemperatureuniformity.
creaseofNO concentration.Model2resultsseemtoagreebetter The mean concentration of HCN along the riser is shown in
x
withtheexperimentaldata.Therefore,theresultsofModel2sim- Fig.11.Aspikeisobservedonthelowersectionduetolargequan-
ulationwillbepresentedinthissection.Concerningfuelconcen- tities of volatile-HCN, which is consumed at the upper part. The
tration (Fig. 9b), it is clear that on the lower part of the bed, outlet concentration of hydrogen cyanide is very small, as ex-
solids concentrationis higher– as expected– due to boththe S- pected, mainly due to the fact that a very large percent is con-
Shape solids concentration profile that characterize CFBs and the sumedinthefluidizedbed.
higherdiameteroffuelphasecomparedtoinertmaterialone. However,whenModel1isadopted,veryhighconcentrationof
Fig.10showstheroleofreactionsIIandXinthenetformation HCNisobservedonthebedoutletincombinationwithverylow
ofNO.ReactionXV,formationofthermal-NO,isprovedtobeneg- N O concentration. The extremely high concentration of HCN
2
ligible,withamaximumof2.45E(cid:3)19Kmol[m3s](cid:3)1andthereforeis whichisevengreaterthantheoneofnitrousoxidedictatedthat
notdepictedinFig.10.Thisresultagreeswellwiththeexpected the assumption for HCN release during char combustion is not
behaviorsincethecombustiontemperatureislow[6]. appropriatewithrespecttothefuelusedandreactionratesavail-
Throughthoroughexaminationofthenumericalmodelresults, able. Due to the relatively low rate at which hydrogen cyanide
it is clear that gas-phase formation of NO from HCN (Reactions formsNOandN O(RI–RIIIinTable2),alargeamountofHCNre-
2
bed
height
- z
(m)
(a) (b)
Fig.9. (a)ConcentrationofNOxplottedagainsttheheightofthebed;and(b)fuelconcentration(kg–fuel/m3-cell)alongbedheight.
1.00E-04
1.00E-05
1.00E-06
1.00E-07
0 1 2 3 4 5 6 7 8 9
z (m)
)s*3m
/
lomk(
etaR
noitcaeR
A.Nikolopoulosetal./Fuel115(2014)401–415 411
Reaction II
Reaction X
Net rate of NOx formation
Fig.10. ContributionofreactionsRIIandRXtotheNOnetformation(logscale).

Author's personal copy
200 ForreactionsIIIandXI,bothofwhichdestructNO x andleadto
180 theformationofnitrousoxide,itisworthmentioningthatthehet-
160 erogeneousdestructionofNO(ReactionXI)ismuchmoredrastic
140 thanthecorrespondinggas-phasereduction(ReactionIII).Therea-
120 sonisthatnitrousoxide,giventhereactionratesavailableinTa-
ble 2, is preferentially formed via the heterogeneous mechanism
100
(Reaction XI) rather than the homogenous mechanism (Reaction
80
III).Inordertoconceivethedifferencebetweenhomogenousand
60 heterogeneousN Oformation,inFigs.13and14,thedistribution
40 2
of NO and N O formation from the intermediates NCO (homoge-
20 2
nousformation)and–CNO(heterogeneousformation)respectively
0
ispresentedagainsttypicalvaluesofNOconcentrationinfluidized
0 1 2 3 4 5 6 7 8 9
bedreactors.
z (m)
ForeverymoleofN Owhichisformedfromtheheterogeneous
2
mechanism, approximately 6–14mol of NO are formed, whereas
for the homogenous mechanism, 4000 NO moles are generated.
Therefore, when Model 1 is adopted, 70% of char nitrogen is re-
leasedfromthechar,doesnotremainenoughtimeinthebedin
leased in the form of HCN during char combustion stage which
order to form nitrogen oxides and therefore is transferred to the
then leads to the low formation of nitrous oxide. On the other
outlet.
hand, when Model 2 is adopted, much more N O is produced. In
HeterogeneousNOformation(ReactionX)hasamorehomoge- 2
this light, model 2 simulates better the reaction network inside
noustrendalongtheheightofthebed.Thisisbecausethereaction
thebed.
ratedependsoncharcombustionrateR (Table2).Theinvestiga-
c
Nitrousoxide,asmentionedbefore,isonlyformedviaReactions
tion of the combustion model results depicted the uniformity of
IIIandXIanditsformationdependsonthelocalNOconcentration
combustionrate alongthe bed height. Higher R values were ob-
c
(Table 2, Figs. 13 and 14). In both N O formation reactions, one
served near the walls due to the higher concentration of inert 2
moleculeofNOisrequired.Nitricoxide’spresenceisthereforere-
bedmaterialandfuelparticles(fastfluidizationregime).Fuelpar-
quired for N O generation. In fact, Hayhurst and Lawrence [4]
ticles are, in general, evenly distributed inside the volume of the 2
foundthatthetotalnumberofmolesoffuelnitrogenthatcontrib-
bed due to the very good mixing conditions. However, they are
ute to the creation of nitrogen oxides is approximately constant.
not in the same combustion phase, due to internal and external
WhatreallychangesinrelationtotemperatureistheNO/N Ora-
recirculation. 2
tio.Thus,forhightemperature,themechanismsleadingtothefor-
Fig.12showstheratesofallreactionsinvolvedinthedestruc-
mation of nitric oxide (NO) are favored, and most of the nitrous
tionofNO aspredictedviamodel2.TherateofreactionIIIisnot
x
oxide(N O)whichiscreated,israpidlydecomposed.Atlowertem-
presentedinFig.12becauseitscontributionprovedtobenegligi- 2
peratures,however,thepathfortheformationofnitrousoxideis
blewhencomparedtothenetdestructionofNO (intherangeof
x
10(cid:3)10). As it is shown in Fig. 12, the reaction of NO with carbon relativelyfavored.
monoxidecomplex(–CO),i.e.reactionXIII,ispredictedasthemost
importantNO reductionreaction.Thepresenceofcarbonmonox-
x
ide,whichisaproductofbothcombustionprocessandreactionsII
andIII,atrelativelyhighconcentrations,enhancesthisreaction.
NOreductiononcharsurface(reactionXII)hasamorehomog-
enoustrendalongtheriser.Reactionratedependsonthelocalcon-
centrationoffuelparticlesinsidethebed(numberofparticlesin
the kinetic constant) and the local NO concentration. Since the
reactor operates in the fast fluidization regime, large amounts of
solidparticlesareconcentratedonthelowerpartofthebed,while
theupperpart(freeboard)ismoredilute.
)3
Nm/gm(
.cnoC
NCH
Fig.11. HCNconcentrationalongreactor(Model2).
1.00E-04
1.00E-05
1.00E-06
1.00E-07
0 1 2 3 4 5 6 7 8 9
z (m)
)s*3m/lomk(
etar
noitcaeR
7000
6000
5000
4000
3000
2000
1000
0
50 70 90 110 130 150
ΝΟ Conc. (mg/m3)
Reaction XII
Reaction XIII
Reaction XI
Net rate of NOx reduction
Fig.12. ContributionofreactionsXI,XIIandXIIItothenetreductionofNO(log
scale).
IIIR/IIR
Fig.13. NO/N2Omoleformationfromthehomogenousoxidationof–CNO.
16
14
12
10
8
6
4
2
0
50 70 90 110 130 150
ΝΟ Conc. (mg/m3)
IXR/XR
412 A.Nikolopoulosetal./Fuel115(2014)401–415
Fig.14. NO/N2Omoleformationfromtheheterogeneousoxidationofactive–CNO.

Author's personal copy
InFig.15,theresultsofN OconcentrationusingModels1and2 2
are presented. Model 1 simulation results seem to under predict
nitrousoxideformationinthefluidizedbed.Thiscanbeattributed
totheHCNreleaseresultingfromthechar-releaseassumption,as
discussedabove.
ResultsofModel2seemtoagreebetterwiththemeasureddata.
However, the simulated values do not coincide with the experi-
mental ones. It is worth mentioning that for the Height z=1.15,
the value measured during the experimental procedure was
350mg per normal cubic meter [33]. This value is not included
in Fig. 15sinceit isconsidered highlyunrealistic.Thisenormous
valueofN Oonthelowersectionofthebedcanbeattributedto
2
limitedsamplepointmeasurements.NOisneededfortheforma-
tion of N O, and NO formation rate is high on the lower section
2
(Fig.10).However,NOconcentrationislow(Fig.9),duetoconvec-
tion phenomena induced by the high gas velocity in the bottom
bed and thus N O formation rate is low. Moreover, Desroches-
2
Ducarneetal.[38]andMukadietal.[41]reportthatN Oconcen-
2
tration, in general, increases with height as CFD results and all
experimentaldataexcepttheoneforz=1.15indicate.
In Model 1, even though there is no N 2 O destruction reaction simulationresults(Fig.16).TherateofN 2 Odestructiononthesur-
incorporated, the N O concentration is still under predicted. On faceofthecharhasarelativelyhomogenoustrendalongtheheight
2
thecontrary,inModel2,threeN Odestructionreactionsareincor- ofthebed,asitdependsonfuelparticleconcentration.Thesimilar-
2
porated (reactions VII, VIII and XIV). The rate of homogenous itybetweenthisreactionandtheheterogeneousdestructionofNO
decompositionofN O(reactionVII),asshowninTable2,depends oncharsurfaceisobvious.
2
onlyonthelocalconcentrationofnitrousoxide.Thehomogeneous Finally,itisdeemednecessarytopresentthemgofNO x formed
destructionofnitrousoxideduetocarbonmonoxide(reactionVIII) ateachcomputationalcell,inordertocompletelygrasptheoverall
isstrongeronthelowersectionofthebed(Fig.16)duetothere- effectthatthesereactionshaveinnitricoxideemissions.Itisre-
leaseoflargequantitiesofcarbonmonoxidebyvolatilehydrocar- mindedthatthetotalamountofNO x added/reducedinacomputa-
bonscombustion. tional cell is represented by the source term in NO x – species
TheheterogeneousdestructionofN 2 Ooncharsurface(reaction transportequation.Fig.17adepictstheprofileofNO x sourceterm
XIV) ispresented inliteratureasthemostsignificantN Oreduc- plottedagainsttheheightofthebed, whilein Fig. 17bthemean
2
tionreaction.Thesignificanceofthisreactionisconfirmedbythe oxygenconcentrationispresented.FromFig.17a,intenseNO x for-
mationisobservedonthelowerpartofthebed,mainlyduetothe
presence of gaseous volatiles that are released instantaneously
after fuel insertion at z=0.7m, and due to oxidizing conditions.
Then, a sharp decrease in NO formation is observed, which is
x
attributedtothesharpdecreaseinoxygenlevels.Oxygeniscon-
sumedintheoxidationofvolatilespecies.Abovetheinsertionof
9 secondary air at 2.15m and especially at 2.8m, there is enough
oxygentoenhancetheformationofNO fromhomogenous(vola-
x
8 tilesthatarenotconsumedandtheyaretransferredfromthelow-
er part) and heterogeneous mechanisms (char oxidation). This
increase in NO formation is observed in Fig. 17a. However, the
x
7 oxygen level drops once more due to combustion. At 5.6m and
above, NOformation mechanisms are favored due to the new
x
6 insertionofsecondaryair.NO x isnowformedalmostentirelyfrom
char oxidation (as seen in Fig. 10). The same trend is observed
alongtheriser.Betweensecondaryairinlets,NO areformedata x
5 high rate. When oxygen decreases, destruction reactions are en-
hanced,thusNO formationratesdecrease.Thereforeitcanbecon-
x
4 cludedthatairstagingports,separatethecombustionchamberin
differentzonesinwhichthesamepatterninNO formationisob-
x
served,atfirstahighrateofformationwhichisfollowedbyasig-
3 nificantreduction.
TherespectivesourcetermofN OisplottedinFig.17cagainst
2
2 thebedheight.ThroughcomparisonofFig.17candadepictingthe
NOformationrate,thesametrendsareobserved.Thisisattributed
to the fact that the air staging influences N O formation in the
2
1 samewayasitaffectsNO formation.However,onthelowersec-
x
tionofthebed,wherehighNO formationratesareobserved,N O
x 2
formationratesarenotsimilarlyhighfortworeasons.Firstly,the
0
250 200 150 100 50 0 formation of nitrous oxide from volatile HCN is a rather ‘‘slow’’
reaction, as already discussed before, and secondly, the creation
ofN O depends on theconcentrationof NO,whichis low on the
2
lowersection(Fig.9).
bed
height
-z
(m)
1.00E-06
1.00E-07
1.00E-08
1.00E-09
0 1 2 3 4 5 6 7 8 9
z (m)
experiment
Model2
Model2 minimum
Model2 maximum
Model1
NO Conc. (mg/m3 )
2 N
Fig.15. ConcentrationofN2Oplottedagainsttheheightofthebed.
)s*3m/lomk(
etar
noitcaeR
A.Nikolopoulosetal./Fuel115(2014)401–415 413
Reaction VII
Reaction VIII
Reaction XIV
Net rate of N2O reduction
Fig.16. ContributionofreactionsVII,VIIIandXIVtothenetN2Oreduction(log.
Scale)

Author's personal copy
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
200 150 100 50 0 -50 -100
5.Conclusions computationally inexpensive, allowing the efficient simulation of
NO andN Oevenoflargescaleunits.However,forsuchsimula-
x 2
Adecoupled3-DsimulationfortheformationofNO–N Oina tions the combusting flow field is a prerequisite. These data can
x 2
1.2MW CFB plant is performed. This model pre-requires the be either obtained by CFD, which is computationally expensive
th
knowledgeofthecombustionfield.Inordertoobtainthatfield,a or by semi-empirical models that are computational inexpensive
simplifiedthreedimensionalCFDcombustingflowmodelisused. butrelyonempiricalcorrelations.
Despite the numerous assumptions of the model and the uncer-
tainties that may entail, good agreement between experimental Acknowledgments
dataandnumericalresultsisachieved.
Gettingafurtherinsightintothedecoupledmodel,theresults TheauthorswouldliketothankPr.LeithnerR.forhisprecious
of the simulation suggest that nitric oxides are formed homoge- support and his help with the experimental data. This paper in-
nously on the lower section of the bed from the oxidation of cludes results from work carried out with a financial grant from
HCN, while on the upper stages, heterogeneous formation is the theResearchFundforCoalandSteeloftheEuropeanCommunity
dominantmechanism.N 2 Oisformedmainlythroughtheheteroge- (ContractNo.RFCR-CT-2005-00009).
neousmechanism.Themainreactionforthereductionofnitrous
oxide was found to be the heterogeneous reduction on char sur-
References
face, fact that agrees with literature. It was found that the main
productoffueldevolatilizationthatledtotheformationofnitric
[1] HämäläinenJ.VTT’sexpertiseinFluidizedBedCombustionofFossilFuelsand
oxideswasHCN.WiththeassumptionofHCNreleaseduringboth Biomass,BIOCLUSEUproject;2011.
devolatilization and char combustion (Model 1), HCN concentra- [2] Nikolopoulos N, Nikolopoulos A, Karampinis E, Grammelis P, Kakaras E.
Numerical investigation of the oxy-fuel combustion in large scale boilers
tion on the outlet was too high. Therefore, Model 2 which does
adoptingtheECO-Scrubtechnology.Fuel2011;90:198–214.
notassumeHCNreleaseduringcharcombustion,butdirectoxida- [3] ThomasKM.Thereleaseofnitrogenoxidesduringcharcombustion.Fuel76,
tion of char-bounded nitrogen seems to be more accurate. How- 457-473. Tsuo, Y.P., Gidaspow, D., 1990. Computation of flow patterns in
circulatingfluidizedbeds.AIChEJ1997;36:885–96.
ever, such a behavior may be fuel specific and more
[4] HayhurstAN,LawrenceAD.TheamountsofNOxandN2Oformedinafluidized
experimentalandsimulationworkisneededbeforedrawingfinal bedcombustorduringtheburningofcoalvolatilesandalsoofchar.Combust
anduniversalconclusions. Flame1996;105:341–57.
Thedecoupledapproachadoptedinthisworkdecreasessignif-
[5] ArmestoL,BoerrigterH,BahilloA,OteroJ.N2Oemissionsfromfluidisedbed
combustion.Theeffectoffuelcharacteristicsandoperatingconditions.Fuel
icantlytheCPUcostincomparisonwiththeapproachofsimulta- 2003;82:1845–50.
neously simulating hydrodynamics, combustion and NO [6] ChenZ,LinM,IgnowskiJ,KellyB,LinjewileTM,AgarwalPK.Mathematical
x
mechanismsasfollowedby[16,17,25].Ifthelatterapproachhad modelingoffluidizedbedcombustion.4:N2OandNOXemissionsfromthe
combustionofchar.Fuel2001;80:1259–72.
been adoptedin the case of the 1.2MW th CFBC, for 220s of flow [7] WójtowiczMA,PelsJR,MoulijnJA.CombustionofcoalasasourceofN2O
simulationexceptforthe27p.d.e.describingthecombustingflow emission.FuelProcessTechnol1993;34:1–71.
the 5 species transportation equations of the NO sub-model [8] MannMD,CollingsME,BotrosPE.Nitrousoxideemissionsinfluidized-bed
x combustion: fundamental chemistry and combustion testing. Progr Energy
shouldhavebeenalsosolved.Thiswouldresultinasevereincre-
CombustSci1992;18:447–61.
mentofthecomputationalcost. [9] BlairDW,WendtJOL,BartokW.Evolutionofnitrogenandotherspeciesduring
ThedevelopedmodelachievedinpredictingNO andN Owith controlled pyrolysis of coal. In: 16th Symposium (international) on
x 2 combustion;1977.p.475–89.
goodaccuracy,especiallyclosetofurnaceexitandcanbeusedfor
[10] NikolopoulosA,PapafotiouD,NikolopoulosN, GrammelisP,Kakaras E.An
CFBC design optimization. The decoupled approach followed is advanced EMMS scheme for the prediction of drag coefficient under a 1.2
z
(m)
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
60 50 40 30 20 10 0 -10
NO source term (mg/m3s) x
z
(m)
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
0 5 10 15
Oxygen Conc. (O 2 % dry vol.) N 2 O source term (mg/m3s)
(a)
)m(
z
414 A.Nikolopoulosetal./Fuel115(2014)401–415
(b) (c)
Fig.17. (a)NOxSourcetermplottedagainsttheheightofthebed;(b)averageoxygenconcentrationplottedagainsttheheightofthebed,and(c)N2OSourcetermplotted
againsttheheightofthebed.

Author's personal copy
A.Nikolopoulosetal./Fuel115(2014)401–415 415
MWthCFBCisothermalflow–partI:numericalformulation.ChemEngSci [32] FLUENT.UserGuide;2006.
2010;65:4080–8. [33] LeithnerR,MüllerH,MüllerJ,SchlutzA,VorckrodtS,WangJ,etal.1993.
[11] Nikolopoulos A, Atsonios K, Nikolopoulos N, Grammelis P, Kakaras E. An Minimization of the formation of air pollutants in the CAFBC by using
advanced EMMS scheme for the prediction of drag coefficient under a 1.2 Europeanfuelsandadditives.
MWthCFBCisothermalflow–partII:numericalimplementation.ChemEngSci [34] BasuP.Combustionofcoalincirculatingfluidized-bedboilers:areview.Chem
2010;65:4089–99. EngSci1999;54:5547–57.
[12] Abbasi E, Arastoopour H. CFD simulation of CO2 sorption in a circulating [35] Smith W. The combustion of coal chars: a review in 19th symposium on
fluidizedbedusingdeactivationkineticmodel.In:KnowltonTM,editor.Tenth combustion.TheCombustionInstitute.;1982.p.1045–65.
international conference on circulating fluidized beds and fluidization [36] LiK,ThompsonS,PengJ.ModellingandpredictionofNOxemissioninacoal-
technology.Sunriver,Oregon;2011.p.736–43. firedpowergenerationplant.ControlEngPract2004;12:707–23.
[13] WangW,LiJ.Simulationofgas–solidtwo-phaseflowbyamulti-scaleCFD [37] LeBrisT,CadavidF,CaillatS,PietrzykS,BlondinJ,BaudoinB.Coalcombustion
approach—of the EMMS model to the sub-grid level. Chem Eng Sci modellingoflargepowerplant,forNOxabatement.Fuel2007;86:2213–20.
2007;62:208–31. [38] Desroches-DucarneE,DolignierJC,MartyE,MartinG,DelfosseL.Modellingof
[14] WangJ,GeW,LiJ.Euleriansimulationofheterogeneousgas-solidflowsinCFB gaseous pollutants emissions in circulating fluidized bed combustion of
risers:EMMS-basedsub-gridscalemodelwitharevisedclusterdescription. municipalrefuse.Fuel1998;77:1399–410.
ChemEngSci2008;63:1553–71. [39] Liu H, Gibbs BM. Modelling of NO and N2O emissions from biomass-fired
[15] GeW,WangW,DongW,WangJ,LuB,XiongQ,etal.Meso-scalestructure—a circulatingfluidizedbedcombustors.Fuel2002;81:271–80.
challengeofcomputationalfluiddynamicsforcirculatingfluidizedbedrisers. [40] AfacanO,GogebakanY,SelÇUk*N.ModelingofNOxemissionsfromFluidized
In:Proceedingsofthe9thInternationalConferenceonCirculatingFluidized Bed Combustion of high volatile lignites. Combust Sci Technol
BedsHamburg;2008.p.19–37. 2007;179:227–47.
[16] Gungor A. Two-dimensional biomass combustion modeling of CFB. Fuel [41] Mukadi L, Guy C, Legros R. Prediction of gas emissions in an internally
2008;87:1453–68. circulatingfluidizedbedcombustorfortreatmentofindustrialsolidwastes.
[17] GungorA,EskinN.Two-dimensionalcoalcombustionmodelingofCFB.IntJ Fuel2000;79:1125–36.
ThermSci2008;47:157–74. [42] Versteeg HK, Malalasekera W. An introduction to computational fluid
[18] GeW,WangW,YangN,LiJ,KwaukM,ChenF,etal.Meso-scaleoriented dynamics,thefinitevolumemethod.PearsonEducatiomLimited;2007.
simulationtowardsvirtualprocessengineering(VPE)—theEMMSparadigm. [43] NelsonPF,BuckleyAN,KellyMD.Functionalformsofnitrogenincoalsandthe
ChemEngSci2011;66:4426–58. releaseofcoalnitrogen asNOxprecursors(HCNandNH3).In:Symposium
[19] Hartge E-U, Ratschow L, Wischnewski R, Werther J. CFD-simulation of a (International)oncombustion,vol.24;1992.p.1259-67.
circulatingfluidizedbedriser.Particuology2009;7:283–96. [44] Goel S, Sarofim A, Kilpinen P, Hupa M. Emissions of nitrogen oxides from
[20] ZhangY,GeW,WangX,YangC.ValidationofEMMS-baseddragmodelusing circulating fluidized-bed combustors: modeling results using detailed
latticeBoltzmannsimulationsonGPUs.Particuology2011;9:365–73. chemistry. In: Symposium (International) on combustion, vol. 26; 1996. p.
[21] KuniiD,LevenspielO.Fluidizationengineering.2nded.Boston:Butterworth- 3317–24.
Heinemann;1991. [45] FineDH,SlaterSM,SarofimAF,WilliamsGC.Nitrogenincoalasasourceof
[22] ZhangDZ,VanderHeydenWB.High-resolutionthree-dimensionalnumerical nitrogenoxideemissionfromfurnaces.Fuel1974;53:120–5.
simulationofacirculatingfluidizedbed.PowderTechnol2001;116:133–41. [46] Kilpinen P, Kallio S, Konttinen J, Barišic´ V. Char-nitrogen oxidation under
[23] Rampidis I, Nikolopoulos A, Koukouzas N, Grammelis P, Kakaras E. fluidised bed combustion conditions: single particle studies. Fuel
Optimization of computational performance and accuracy in 3-D transient 2002;81:2349–62.
CFDmodelforCFBhydrodynamicspredictions2007;452–5. [47] Winter F, Wartha C, Löffler G, Hofbauer H. The NO and N2O formation
[24] GunnDJ.Transferofheatormasstoparticlesinfixedandfluidisedbeds.IntJ mechanismduringdevolatilizationandcharcombustionunderfluidized-bed
HeatMassTrans1978;21:467–76. conditions.In:Symposium.
[25] ZhouW,ZhaoCS,DuanLB,ChenXP,LiangC.Two-dimensionalcomputational [48] JensenA,JohnssonJE,AndriesJ,LaughlinK,ReadG,MayerM,etal.pressurized
fluid dynamics simulation of nitrogen and sulfur oxides emissions in a fluidizedbedcombustionofcoal.Fuel1995;74:1555–69.
circulatingfluidizedbedcombustor.ChemEngJ2011;173:564–73. [49] KilpinenP,HupaM.HomogeneousN2Ochemistryatfluidizedbedcombustion
[26] Nikolopoulos A, Rampidis I, Nikolopoulos N, Grammelis P, Kakaras E. conditions:akineticmodelingstudy.CombustFlame1991;85:94–104.
Numericalinvestigationof3-Dtransientcombustingflowina1.2MWthpilot [50] KramlichJC,ColeJA,McCarthyJM,LanierWS,McSorleyJA.Mechanismsof
powerplant.2009;839–44. nitrousoxideformationincoalflames.CombustFlame1989;77:375–84.
[27] Syamlal M. A review of granular stress constitutive relations. National [51] GoelS,ZhangB,SarofimAF.NOandN2OformationduringCharcombustion:is
technicalinformationservice.VA:Springfield;1987. itHCNorsurfaceattachednitrogen?CombustFlame1996;104:213–7.
[28] ZhaoY,KimHY,YoonSS.Transientgroupcombustionofthepulverizedcoal [52] TullinCJ,GoelS,MoriharaA,SarofimAF,BeerJM.NOandN2Oformationfor
particlesinsphericalcloud.Fuel2007;86:1102–11. coal combustion in a fluidized bed: effect of carbon conversion and bed
[29] FLUENT.Theoryguide;2010. temperature.EnergyFuels1993;7:796–802.
[30] Magnussen BF, Hjertager BH. On mathematical models of turbulent [53] Gulyurtlu I, Esparteiro H, Cabrita I. N2O formation during fluidized bed
combustion with special emphasis on soot formation and combustion. In: combustionofchars.Fuel1994;73:1098–102.
16th Symposium (International) on combustion. The Combustion Institute; [54] BonnB,PelzG,BaumannH.FormationanddecompositionofN2Oinfluidized
1976. bedboilers.Fuel1995;74:165–71.
[31] SofialidisD,FaltsiO,SardiK,SkevisG,SkodrasG,KaldisSP,etal.Modelling [55] ZhaoJ,BreretonC,GraceJR,JimLimC,LegrosR.Gasconcentrationprofilesand
low-temperaturecarbonisationofsolidfuelsinaheatedrotarykilnforclean NOxformationincirculatingfluidizedbedcombustion.Fuel1997;76:853–60.
fuelproduction.Fuel2005;84:2211–21.
