# Industrial_Boilers_and_Heat_Recovery_Ste

**Fonte**: Industrial_Boilers_and_Heat_Recovery_Ste.pdf  
**Data de conversão**: 2025-07-30 15:13:30  
**Origem**: base_relevantes

---

Industrial Boilers
and Heat Recovery
Steam Generators
Design, Applications,
and Calculations
V. Ganapathy
ABCO Industries
Abilene, Texas, U.S.A.
Marcel Dekker, Inc. New York Basel
•
TM
Copyright © 2003 Marcel Dekker, Inc.

ISBN: 0-8247-0814-8
Thisbookisprinted onacid-free paper.
Headquarters
Marcel Dekker, Inc.
270Madison Avenue, NewYork,NY10016
tel:212-696-9000; fax:212-685-4540
EasternHemisphereDistribution
Marcel Dekker, AG
Hutgasse 4,Postfach 812, CH-4001Basel, Switzerland
tel:41-61-260-6300; fax: 41-61-260-6333
WorldWideWeb
http:==www.dekker.com
Thepublisheroffersdiscountsonthisbookwhenorderedinbulkquantities.Formoreinfor-
mation,writetoSpecialSales=ProfessionalMarketingattheheadquartersaddressabove.
Copyright#2003by Marcel Dekker,Inc.All Rights Reserved.
Neither this book nor any part may be reproduced or transmitted in any form or by any
means,electronicormechanical,includingphotocopying,microfilming,andrecording,or
by any information storage and retrieval system, without permission in writing from the
publisher.
Current printing(last digit):
10 9 8 7 6 5 4 3 2 1
PRINTED INTHE UNITEDSTATES OFAMERICA
Copyright © 2003 Marcel Dekker, Inc.

To all professionals involved in steam generation
and energy conservation.
Copyright © 2003 Marcel Dekker, Inc.

Preface
Theroleofboilersandheatrecoverysteamgenerators(HRSGs)intheindustrial
economy has been profound. Boilers form the backbone of power plants,
cogeneration systems, and combined cycle plants. There are few process
plants, refineries, chemical plants, or electric utilities that do not have a steam
plant. Steam is the most convenient working fluid for industrial processing,
heating, chilling,andpowergenerationapplications.Fossilfuelswillcontinueto
be the dominant energy providers for years to come.
This book is about steam generators, HRSGs, and related systems. There
are several excellent books on steam generation and boilers, and each has been
successful in emphasizing certain aspects of boilers and related topics such as
mechanical design details, metallurgy, corrosion, constructional aspects, main-
tenance, or operational issues. This book is aimed at providing a different
perspective on steam generators and is biased toward thermal and process
design aspects of package boilers and HRSGs. (The terms ‘‘waste heat boiler’’
and‘‘HRSG’’areusedinthesamecontext.)Myemphasisonthermalengineering
aspects of steam generators reinforced by hundreds of worked-out real-life
examples pertaining to boilers, HRSGs, and related systems will be of interest
toengineersinvolvedinabroadfieldofsteamgenerator–relatedactivitiessuchas
consulting, design, performance evaluation, and operation.
Copyright © 2003 Marcel Dekker, Inc.

DuringthelastthreedecadesIhavehadtheopportunitytodesignhundreds
ofpackageboilersandseveralhundredwasteheatboilersthatareinoperationin
the U.S. and abroad. Based on my experience in reviewing numerous specifica-
tions of boilers and HRSGs, I feel that consultants, plant engineers, contractors,
and decision makers involved in planning and developing steam plants often do
not appreciate some of the important and subtle aspects of design and perfor-
mance of steam generators.
Many engineers still feel that by raising the exit gas temperature in boilers
(cid:1)
witheconomizers,onecanavoidaciddewpointconcerns.Itisthefeedwater
temperature—not the gas temperature—that determines the tube wall
temperature (and hence the corrosion potential).
Softened water is sometimes suggested for attemperation for steam tempera-
(cid:1)
ture control, even though it will add solids to steam that can cause problems
such as deposition of solids in superheaters and steam turbines.
To operate steam plants more efficiently, plant engineers should be able to
(cid:1)
understandandappreciatethepartloadcharacteristicsofboilersandHRSGs.
HoweverwhilespecifyingboilersandHRSGs,oftenonlytheperformanceat
100% load is stressed.
HRSGsteamgenerationandtemperatureprofilescannotbearbitrarilyarrived
(cid:1)
at, as pinch and approach points determine this. For example, I have seen
several specifications call for a 300 F exit gas temperature from a single
(cid:2)
pressure unfired gas turbine HRSG generating saturated steam at 600psig
using feedwater at about 230 F. A simple analysis reveals that only about
(cid:2)
340–350 F is thermodynamically feasible.
(cid:2)
Supplementary firing in gas turbine HRSGs is an efficient way to generate
(cid:1)
steamcomparedwithsteamgenerationinapackagedboiler.Thebookexplains
whythisisso,withexamplesinChapters1and8.Cogenerationengineerscan
make use of this information to minimize fuel costs in their plants.
Afewwasteheatboilerspecificationsprovidethefluegasflowinvolumetric
(cid:1)
units instead of mass units, leading to confusion. Lack of information on
molecular weight or gas pressure can lead to incorrect evaluation of density
andhencethemassflow.Also,volumeoffluegasisoftengivenincfm(cubic
feet per minute) and one is not sure whether it is acfm (actual cubic feet per
minute)orscfm(standardcubicfeetperminute).Thedifferenceinmassflow
can be significant depending on the basis.
Althoughfluegasanalysisaffectsgasspecificheat,heattransfer,boilerduty,
(cid:1)
and temperature profiles, these data are often not given in specifications for
waste heat boilers. Forexample,theratioofspecificheats offluegases from
combustion of natural gas and fuel oil is about 3.5%, which is not insignif-
icant.Thisisduetothe18%volumeofwatervaporinnaturalgasproductsof
combustion versus 12% in fuel oil combustion products.
Copyright © 2003 Marcel Dekker, Inc.

A few consultants select boilers and HRSGs based on surface area, although
(cid:1)
it can vary significantly based on tube geometry or fin configuration. With
finnedtubes,ascanbeseenfromseveralexamplesinthisbook,thevariation
in surface areas could be in the range of 200–300% for the same duty.
Operating cost due to fuel consumption or gas pressure drop across heating
(cid:1)
surfaces is often ignored by many consultants in their evaluation and only
initial costs are compared while purchasing steam generators or HRSGs,
resulting in a poor selection for the end user. A few plants are now realizing
thattheitemsofsteamplantequipmenttheypurchasedyearsagobasedonlow
initialcostsaredrainingtheircashreservesthroughcostlyfuelandelectricity
bills and hence are scrambling to improve their design and performance.
Many engineers are not aware of recent developments in oil- and gas-fired
(cid:1)
packagedboilersandarestillspecifyingboilersusingrefractorylinedfurnace
walls and floors!
Plantengineersoftenassumethataboilerdesignedfor600psig,forexample,
(cid:1)
canbeoperatedat200psig and atthesame capacity.The potential problems
associated with significant changes in steam pressure and specific volume in
boiler operation are discussed in Chapters 1 and 3.
Condensing exchangersarebeing considered in boilers andHRSGsnotonly
(cid:1)
forimprovementinefficiencybutalsotorecoverandrecyclethewaterinthe
flue gases, which is a precious commodity in some places.
Emission control methods such as flue gas recirculation increase the mass
(cid:1)
flowof flue gases through the boiler; yet standard boilers are being selected
thatcanbeexpensivetooperateintermsoffanpowerconsumption.Manyare
not aware of the advantages of custom-designed boilers, which can cost less
to own and operate.
Afewsteamplantprofessionalsdonotappreciatetherelationbetweenboiler
(cid:1)
efficienciesandhigherandlowerheatingvalues,andthusspecifyvaluesthat
are either impossible to accomplish or too inefficient.
As a result of this ‘‘knowledge=information gap’’ in process engineering
aspects of boilers or HRSG, the end user may need to settle for a product with
substandardperformanceandhighcosts.Thisbookelaboratesonvariousdesign
and performance aspects of steam generators and heat recovery boilers so that
anyone involved with them will become more informed and ask the right
questions during the early stages of development of any steam plant project.
This will give the best chance of selecting the steam generator with the right
design and parameters. Even a tiny improvement in design, efficiency, operating
costs, or performance goes a long way in easing the ‘‘energy crunch.’’
The first four chapters describe some of the recent trends in power
generation systems, a few aspects of steam generator and HRSG design and
performance, and the impact of emissions on boilers in general. The remaining
Copyright © 2003 Marcel Dekker, Inc.

chaptersdealwithcalculationsthatshouldbeof interesttosteamplantengineers.
I authored the Steam Plant Calculations Manual (Marcel Dekker, Inc.) several
yearsago andhad beenthinking ofadding more examplestothisworkforquite
some time. This book builds on that foundation.
Chapter1isanintroductorydiscussionofpowerplantsanddescribessome
of the recent developments in power systems such as the supercritical Rankine
cycle,theKalinacycle,theChengcycle,andtheintegratedcoalgasificationand
combined cycle (IGCC) plant that is fast becoming a reality.
The second chapter describes heat recovery systems in various industries.
The role of the HRSG in sulfur recovery plants, sulfuric acid plants, gas turbine
plants, hydrogen plants, and incineration systems is elaborated.
Chapter 3, on steam generators, describes the latest trends in custom-
designed package boilers and the limitations of standard boilers developed
decades ago. Emission regulations have resulted in changes in boiler operating
parameters such as higher excess air and FGR rates that impact boiler perfor-
mance significantly. It should be noted that there can be several designs for a
boiler simply because the emission levels are different, although the steam
parameters may be identical. If an SCR system is required, it necessitates the
addition of a gas bypass system, adding to the cost and complexity of boiler
design. These are explained through quantitative and practical examples.
Chapter4,onemissions,describesthevariousmethodsusedinboilersand
HRSGs to limit NOx and CO and how their designs are impacted. For example,
the HRSG evaporator may have to be split up to accommodate the selective
catalytic reduction (SCR) system; gas bypass dampers may have to be used in
packaged steam generators toachievetheoptimalgastemperatureatthecatalyst
forNOxconversionatvariousloads.Fluegasrecirculation(FGR)addstothefan
powerconsumptionifthestandardboilerisnotredesigned.Itmayalsoaffectthe
boiler efficiencythroughhigher exitgas temperature due tothe larger mass flow
of flue gases. Other methods for emission control, such as steam injection and
burner modifications, are also addressed.
Chapters 4–8, which present calculations pertaining to various aspects of
boilers and HRSGs and their auxiliaries, elaborate on the second edition of the
SteamPlantCalculationsbook.Severalexampleshavealsobeenadded.Chapter
5 deals with calculations such as conversion of mass to volumetric flowrates,
energy utilization from boiler blowdown, general ASME code calculations, and
lifecyclecostingmethods.(ASMEhasbeenupdatingtheallowablestressvalues
forseveralboilermaterialsandoneshouldusethelatestdata.)Alsoprovidedare
ABMA and ASME guidelines on boiler water, for evaluating the blowdown or
estimatingthesteamfordeaeration.Lifecyclecostingisexplainedthroughafew
examples.
Chapter 6 deals with combustion calculations, boiler efficiency, and
emission conversion calculations. Simplified combustion calculation procedures
Copyright © 2003 Marcel Dekker, Inc.

such as the MM Btu method are explained. Often boiler efficiency is cited on a
Higher Heating Value basis, while a fewengineers use the Lower Heating Value
basis.Therelationbetweenthetwoisillustrated.TheASMEPTC4.1methodof
calculating heat losses for estimating boiler efficiency is elaborated, and simpli-
fiedequationsforboilerefficiencyarepresented.Examplesillustratetherelation
between oxygen in turbine exhaust gases and fuel input. Correlations for dew
point of various acid vapors are given with examples.
Chapter7explainsboilercirculationcalculationsinbothfiretubeandwater
tubeboilers.Fluidflowinblowoffandblowdownlines,whichinvolvetwo-phase
flowcalculations,canbeestimatedbyusingtheproceduresshown.Theproblem
of flow instability in boiling circuits is explained, along with measures to
minimize this concern, such as use of orifices at the inlet to the tubes.
Calculations involving orifices and safety valves should also be of interest to
plant engineers.
Chapter 8 on heat transfer has over 65 examples of sizing, off-design
performance calculations pertaining to boilers, superheaters, economizers,
HRSGs, and air heaters. Tube wall temperature calculations and calculations
with finned tubes for insulation performance will help engineers understand the
design concepts better and even question the boiler supplier. HRSG temperature
profiles are also explained, with methods described for evaluating off-design
HRSG performance.
The last chapter deals with pumps, fans, and turbines and examples show
the effect of a few important variables on their performance. The impact of air
density on boiler fan operation is illustrated, and the effect of elevation and
temperature on flow and head are explained. With flue gas recirculation being
used in almost all boilers, the effect of density on the volume is important to
understand.Theeffectof inletairtemperatureonBraytoncycleefficiencyisalso
explained and plant engineers will appreciate the need for inlet air-cooling in
summer months in large gas turbine plants. The efficiency of cogeneration is
explained, as are also power output calculations using steam turbines.
Asimplequizisgivenattheendofthebook.Itspurposeistorecapitulate
important aspects of boiler and HRSG performance discussed in the book.
In sum, the book will be a valuable addition to anyone involved in steam
plants,cogenerationsystems,orcombinedcycleplants.Manyexamplesarebased
on my personal experience and hence, the conclusions drawn do not reflect the
viewsofanyorganization.Itispossible,duetolackof informationonmypartor
totherapiddevelopmentsinsteamplantengineeringandtechnology,thatIhave
expressedsomeviewsthatmaynotbecurrentormaybeagainstthegrain;ifso,I
expressmyregrets.Iwouldappreciatereadersbringingthesetomyattention.The
calculations have been checked to the best of my ability; however if there are
errors,Iapologizeandwouldappreciateyourfeedback.Itismyferventhopethat
Copyright © 2003 Marcel Dekker, Inc.

this book will be the constant companion of professionals involved in the steam
generation industry.
I would like to thank ABCO Industries for allowing me to reproduce
severalofthedrawingsandphotographsofboilersandHRSGs.Ialsothankother
sources that have provided me with information on recent developments on
various technologies.
V. Ganapathy
Copyright © 2003 Marcel Dekker, Inc.

Contents
Preface
1 Steam and Power Systems
2 Heat Recovery Boilers
3 Steam Generators
4 Emission Control in Boilers and HRSGs
5 Basic Steam Plant Calculations
6 Fuels, Combustion, and Efficiency of Boilers and Heaters
7 Fluid Flow, Valve Sizing, and Pressure Drop Calculations
8 Heat Transfer Equipment Design and Performance
9 Fans, Pumps, and Steam Turbines
Copyright © 2003 Marcel Dekker, Inc.

Appendix 1: AQuiz on Boilers and HRSGs
Appendix 2: Conversion Factors
Appendix 3: Tables
Glossary
Bibliography
Copyright © 2003 Marcel Dekker, Inc.

1
Steam and Power Systems
INTRODUCTION
Basichumanneedscanbemetonlythroughindustrialgrowth,whichdependsto
a great extent on energy supply. The large increase in population during the last
fewdecadesandthespurtinindustrialgrowthhaveplacedtremendousburdenon
the electrical utility industry and process plants producing chemicals, fertilizers,
petrochemicals, and other essential commodities, resulting in the need for
additional capacity in the areas of power and steam generation throughout the
world. Steam is used in nearly every industry, and it is well known that steam
generatorsandheatrecoveryboilersarevitaltopowerandprocessplants.Itisno
wonderthatwithrisingfuelandenergycostsengineersinthesefieldsareworking
oninnovativemethods togenerateelectricity,improveenergyutilizationinthese
plants, recover energy efficiently from various waste gas sources, and simulta-
neously minimize the impact these processes have on environmental pollution
and the emission of harmful gases to the atmosphere. This chapter briefly
addresses the status of various power generation systems and the role played
by steam generators and heat recovery equipment.
Severaltechnologiesareavailablefor powergenerationsuchasgasturbine
basedcombinedcycles,nuclearpower,windenergy,tidalwaves,andfuelcells,to
mention a few. Figure 1.1 shows the efficiencyof a few types of power systems.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.1 Efficiencyoftypicalpowersystems.
Copyright © 2003 Marcel Dekker, Inc.

About40%oftheworld’spoweris,however,generatedbyusingboilersfiredwith
pulverized coal and steam turbines operating on the Rankine cycle. Large
pulverized coal fired and circulating fluidized bed supercritical pressure units
are being considered as candidates for power plant capacity addition, though
several issues such as solid particle erosion, metallurgy of pressure parts,
maintenance costs, and start-up concerns remain. It may be noted that in
Europe and Japan supercritical units are more widespread than in the United
States.
In spite of escalation in natural gas prices, gas turbine capacity has
increased by leaps and bounds during the last decade. Today’s combined cycle
plants are rated in thousands of megawatts, unlike similar plants decades ago
when 100MW was considered a very high rating. Steam pressure and tempera-
tureratingsforheatrecoverysteamgenerators(HRSGs)incombinedcycleplants
have also increased, from 1000psig a decade or so ago to about 2400psig.
Reheaters,whichimprovetheRankinecycleefficiencyandaregenerallyusedin
utility boilers, are also finding a place in HRSGs. Complex multipressure,
multimodule HRSGs are being engineered and built to maximize energy
recovery.
Repowering existing steam power plants typically 30 years or older with
modern gas turbines brings new useful life in addition to offering a few
advantages such as improved efficiency and lower emissions. A few variations
of this concept are shown in Fig. 1.2. In boiler repowering, the gas turbine
exhaustisusedascombustionairfortheboiler.Owingtothesizeofsuchplants,
solid fuel firing may be feasible and perhaps economical. Another option is to
increase the power output of the steam turbine by not using the extraction steam
for feedwater heating, which is performed by the turbine exhaust gases in the
HRSG.TheexhaustgasescanalsogeneratesteamwithparametersintheHRSG
similar to these of the original coal-fired boiler plant, which can be taken out of
service.Becausegasturbinestypicallyusepremiumfuels,theemissionsofNOx,
CO ,andSOxarealsoreducedintheserepoweringprojects.Itmaybenotedthat
2
the various HRSG options discussed above are challenging to design and build,
becausenumerousparameters aresite-specific andcostfactorsvaryfromcaseto
case.
Significant advances have been made in research and development of
alternative methods of coal utilization such as fluidized bed combustion and
gasification; integrated coal gasification and combined cycle (IGCC) plants are
not research projects any longer. A few commercial plants are in operation
throughout the world. Figure 1.3 shows a typical plant layout.
Research into working fluids for power generation have also led to new
concepts and efficient power generation systems such as the Kalina cycle (Fig.
1.4),whichusesamixtureofammoniaandwaterastheworkingfluidinRankine
cyclemode.Theuseoforganicvaporcyclesinlowtemperatureenergyrecovery
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.2 Repowering conceptsto salvage agingpowerplants.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.3 Wabash integrated coalgasificationandcombined cycle plant.
applications is also widespread. Gas turbine technology is being continuously
improved to develop advanced cycles such as the intercooled aero derivative
(ICAD), humid air turbine (HAT), and Cheng cycle. We have come a long way
fromthe35%efficiencyleveloftheRankinecycletothe60%levelincombined
cycle plants.
Heat sources in industrial processes can be at very high temperatures,
1000–2500 F,orverylow,ontheorderof250–500 F,andapplicationshavebeen
(cid:2) (cid:2)
developedtorecoverasmuchenergyfromthese effluentsaspossibleinorder to
improve the overall energy utilization. Heat recovery steam generators form an
importantpartofthesesystems.(Note:Thetermswasteheatboiler,heatrecovery
boiler, and heat recovery steam generator are used synonymously). Waste gas
streams sometimes heat industrial heat transfer fluids, but in nearly 90% of the
applicationssteamisgenerated,thatisusedforeitherprocessorpowergeneration
via steam turbines.
Condensing heat exchangers are used in boilers and in HRSGs when
economicallyviabletorecoverasignificantamountofenergyfromfluegasesthat
are often below the acid and water dew points. The condensing water removes
acid vapors present in the gas stream along with particulates if any. In certain
process plants, energy recovery and pollution control go hand in hand for
economic and environmental reasons. Though expensive, condensing economi-
zers, in addition to improving the efficiency of the plant, help conservewater, a
preciouscommodityinsomeareas.SeeChapter3foradiscussiononcondensing
exchangers.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.4 Kalina cycle scheme at Canoga Park, CA. 1, HRVG; 2, turbine; 3,
flashtank;4,finalpreheater;5,HPpreheater;6,secondrecuperator;7,vaporizer;
8,HPpreheater;9,firstrecuperator;10,LPpreheater;11,HPcondenser;12,LP
condenser; 13, coolingwater;t, throttlingdevice; p, pump.
Today if we walk into any chemical plant, refinery, cogeneration plant,
combined cycle plant, or conventional power plant, we can see the ubiquitous
steam generators and heat recovery boilers, because steam is needed virtually
everywhere for process and power generation. Boiler and HRSG designs are
being continuously improved to meet the challenges of higher efficiency and
lower emissions and to handle special requirements if any. For example, one of
the requirements for auxiliary boilers in large combined cycle plants is quick
start-up;packagedboilersgeneratingsaturatedorsuperheatedsteamarerequired
tocomeupfrom hotstandbyconditionto100%capacityinafewminutesifthe
gas turbine trips. Packaged boilers with completely water-cooled furnaces (Fig.
1.5)arebettersuitedforthisapplicationthanrefractory-linedboilers.Inaddition
to generating power or steam efficiently, today’s plants must also meet strict
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.5 Packaged steam generator with completely water-cooled furnace.
(Courtesyof ABCOIndustries, Abilene, TX.)
environmental regulations relating to emissions of NOx, SOx, CO, and CO ,
2
which adds to the complexity of their designs.
RANKINE CYCLE
A discussion on boilers would be incomplete without mentioning the Rankine
cycle. The steam-based Rankine cycle has been synonymous with power
generation for more than a century. In the United States, utility boilers typically
use subcritical parameters (2400 psi, 1050=1050 F), whereas in Europe and
(cid:2)
Japan, supercritical plants are in vogue (4300psi, 1120=1120 F). The net
(cid:2)
efficiency of power plants has increased steadily from 36% in the 1960s for
subcritical coal-fired plants to 45% for supercritical units commissioned in the
1990s. Severaltechnological improvements in areas such as metallurgyof boiler
tubing,reductioninauxiliarypowerconsumption,improvementsinsteamturbine
blade design and metallurgy, pump design, burner design, variable pressure
condenser design, and multistage feedwater heating coupled withlow boiler exit
gastemperatureshaveallcontributedtoimprovementsinefficiency.Animmedi-
ateadvantageofhigherefficiencyisloweremissionsofCO andotherpollutants.
2
Currentstate-of-the-artcoal-firedsupercriticalsteampowersystemsoperateatup
to 300 bar and 600 C with net efficiencies of 45%. These plants have good
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

efficienciesevenatpartialloadcomparedtosubcriticalunits,andplantcostsare
comparabletothoseofsubcriticalunits.At75%load,forexample,theefficiency
reductioninasupercriticalunitisabout2%comparedto4%forsubcriticalunits.
At 50% load, the reduction is 5.5–8% for supercritical versus 10–11% for
subcritical. These units are of once-through design. Cycle efficiencies of 36%
inthe1960s(160bar,540=540 C)rosetoabout40%in1985andto43–45%in
(cid:2)
1990. These gains have been made through [1–3]
Increases in the main and reheat steam temperatures and main steam
pressure, including transitions to supercritical conditions
Changesincycleconfiguration,includingincreasesinthenumberofreheat
stages and the number of feedwater heaters
Changes in condenser pressure and lowering of the exit gas temperature
from the boiler (105–115 C)
(cid:2)
Reductions in auxiliary power consumption through design and develop-
ment
Improvements in the performance of various types of equipment such as
turbines and pumps, as mentioned above
One of the concerns with the steam-based Rankine cycle is that a higher
steam temperature is required with higher steam pressure to minimize the
moistureinthesteamafterexpansion.Moistureimpactstheturbineperformance
negatively through wear, deposit formation, and possible blockage of the steam
path.AscanbeseeninFig.1.6,ahighersteampressureforthesametemperature
FIGURE 1.6 T–S diagramshowing expansionofsteam.
Copyright © 2003 Marcel Dekker, Inc.

results in higher moisture after expansion. Hence steam temperatures have been
increasingalongwithpressures,addingtometallurgicalconcerns.Thisimpliesa
needforhigherboilertubewallthicknessandmaterialswithhigherstressvalues
at high temperatures. Multistage reheating minimizes the moisture concern after
expansion;however, thisaddstothecomplexityoftheboiler andHRSG design.
AlsowithHRSGs,thesteam-basedRankinecyclelimitstheeffectivenessofheat
recovery, because steam boils at constant temperature and significant energy is
lost, which brings us to the Kalina cycle.
KALINA CYCLE
ArecentdevelopmentinpowergenerationtechnologyistheKalinacycle,which
basicallyfollowstheRankinecycleconceptexceptthattheworkingfluidis70%
ammonia–watermixture.Ithasthepotentialtobe10–15%moreefficientthanthe
Rankine cycle and uses conventional materials of construction, making the
technology viable. Figure 1.4 shows the scheme of the demonstration plant at
Canoga Park, CA, which has been in operation since 1995 [4–6]. In the typical
steam–water-based Rankine cycle, the loss associated with the working fluid in
the condensing system is large; also, the heat is added for the most part at
constant temperature; hence there are large energy losses, resulting in low cycle
efficiency.
In the Kalina cycle, heat is added and rejected at varying temperatures
(Fig. 1.7a), which reduces these losses. The steam–water mixture boils or
condenses at constant temperature, whereas the ammonia–water mixture has
varying boiling and condensing temperatures and thus closely matches the
temperatureprofilesoftheheatsources.Thedistillation condensationsubsystem
(DCSS)changestheconcentrationoftheworkingfluid,enablingcondensationof
the vapor from the turbine to occur at a lower pressure. The DCSS brings the
mixture concentration back to the 70% level at the desired high inlet pressure
beforeenteringtheheatrecoveryvaporgenerator(HRVG).TheHRVGissimilar
in design to an HRSG.
The ammonia–water mixtures have many basic features unlike those of
either ammonia or water, which can be used to advantage:
1. The ammonia–water mixture has a varying boiling and condensing
temperature, which enables the fluid to extract more energy from the
hot stream by matching the hot source better than a system with a
constantboilingandcondensingtemperature.Thisresultsinsignificant
energy recovery from hot gas streams, particularly those at low
temperatures, such as the geothermal heat source of Fig. 1.7b. By
changing the working fluid concentration from 70% to about 45%,
condensation of the vapor is enabled at a lower pressure, thus
Copyright © 2003 Marcel Dekker, Inc.

FIGURE1.7 (a)Cyclediagram:Kalinavs.steamRankinesystems.(b)Tempera-
tureprofilesof (left) Kalinaand (right)steam heatrecoverysystems.
recovering additional energy from the vapor in the turbine with lower
energylossesatthecondensersystem.AscanbeseeninFig.1.7b,the
energy recovered with a steam system is very low, whereas the
ammonia–water mixture is able to recover a large fraction of the
availableenergyfromthehotexhaustgases.Asteamplantwouldhave
to use a multiple-pressure system to recover the same fraction of
energy, but this increases the complexity and cost of the steam plant.
The lower the temperature of the gas entering the boiler, the better is
the Kalina system compared to the steam system.
2. The thermophysical properties of an ammonia–water mixture can be
altered by changing the ammonia concentration. Thus, even at high
ambient temperatures, the cooling system can be effective, unlike in a
steamRankinesystem,wherethecondenserefficiencydropsoffasthe
cooling water temperature or ambient temperature increases. The
Kalina cycle can also generate more power at lower cooling water
temperatures than a steam Rankine cycle.
Copyright © 2003 Marcel Dekker, Inc.

3. The ammonia–water mixture has thermophysical properties that cause
mixed fluid temperatures to change without a change in heat content.
The temperature of water or ammonia does not change without a
change in energy.
4. Water freezes at 32 F, whereas pure ammonia freezes at 108 F.
(cid:2) (cid:2)
(cid:3)
Ammonia–watersolutionshaveverylowfreezingtemperatures.Hence
atlowambienttemperatures,theKalinaplantcangeneratemorepower
without raising concerns about freezing.
5. Thecondensingpressureofanammonia–watermixtureishigh,onthe
orderof2barcomparedto0.1barinasteamRankinesystem,resulting
in lower specific volumes of the mixture at the turbine exhaust and
consequentlysmallerturbineblades.Theexpansionratiointheturbine
is about 10 times smaller. This reduces the cost of the turbine
condenser system. With steam systems, the condenser pressure is
already at a low value, on the order of 1psia; hence further lowering
would be expensive and not worth the cost.
6. The losses associated with the cooling system are smaller due to the
lowercondensingduty, andhencethecoolingsystemcomponents can
be smaller and the environmental impact less.
Example of a Kalina System
A3MWplanthasbeeninoperationinCaliforniaformorethanadecade.Inthis
plant, 31,450lb=h of ammonia vapor enters the turbine at 1600psia, 960 Fand
(cid:2)
exhausts at 21psia. The ammonia concentration varies throughout the system.
The main working fluid in the HRVG is at 70% concentration, whereas at the
condenseritisat42%.Theleanerfluidhasalowervaporpressure,whichallows
foradditionalturbineexpansionandgreaterworkoutput.Theabilitytovarythis
concentration enables the performance to bevaried and improvedirrespectiveof
the cooling water temperature.
Followingtheexpansionintheturbine,thevaporisattoolowapressureto
be completely condensed at the available coolant temperature. Increasing the
pressurewouldincreasethetemperatureandhencereducethepoweroutput.Here
is where the DCSS comes in. The DCSS enables condensing to be achieved in
twostages,firstforminganintermediatemixtureleanerthan70%andcondensing
it, then pumping the intermediate mixture to higher pressure, reforming the
working mixture, and condensing it as shown in Fig. 1.4. In the process of
reforming the mixture (back to 70%), additional energy is recovered from the
exhaust stream, which increases the power output. Calculations show that the
poweroutputcanbeincreasedby10–15%intheDCSScomparedtotheRankine
system based on a steam–water mixture.
Copyright © 2003 Marcel Dekker, Inc.

The HRVG for the Kalina cycle is a simple once-through steam generator
withaninletforthe70%ammonialiquidmixture,whichisconvertedintovapor
at the other end. Thevapor-side pressure drop is large, on the order of hundreds
of pounds per square inch due to the two-phase boiling process. Conventional
materialssuchascarbonandalloysteelsareadequatefortheHRVGcomponents.
Studies have been made on large combined cycle plants using the Kalina
cycle concept. Using an ABB 13E gas turbine, 227MW can be generated at a
heat rate of 6460Btu=kWh (52.8%). This system produces an additional
12.1MW compared to a two-pressure steam bottoming cycle. Though the cost
details are not made available, it is felt that they are comparable on the basis of
dollars per kilowatt.
SeveralvariationsoftheKalinacyclehavebeenstudied.Oneoftheoptions
for power generation cycles is shown in Fig. 1.8. It employs a reheat turbine. A
cooling stage is included between the high pressure and intermediate turbines.
First the vapor is superheated in the HRVG and expanded in the high pressure
stage.ThenitisreheatedintheHRVGandexpandedintheintermediatestageto
generate more power. At this point the superheat remaining in the vapor is
removedtovaporize a portion of theworking fluid, which has been preheated in
the economizer section. This additional vapor is then combined with the vapor
generatedintheHRVGandthensuperheated.Thecooledvaporisthenexpanded
in the low pressure stage. These heat exchanges enable the working fluid to
recovermoreenergyfromtheexhaustgasstream.A4.5MWKalinasystemisin
operationinJapanthatusesenergyrecoveredfromamunicipalincinerationheat
recovery system, and a 2MW plant using geothermal energy is in operation in
FIGURE1.8 Kalinasystemtoimproveenergyrecoveryinacombinedcycleplant.
Copyright © 2003 Marcel Dekker, Inc.

Iceland.Itmaybenotedthatasthetemperatureoftheheatsourceisreduced,the
Kalina system offers more efficiency than a steam or organic vapor system.
ORGANIC RANKINE CYCLE
TheRankinecycleisathermodynamiccycleusedtogenerateelectricityinmany
power stations and is the practical approach to the Carnot cycle. Superheated
steam is generated in a boiler, then expanded in a steam turbine. The turbine
drives a generator to convert the work into electricity. The remaining steam is
then condensed and recycled as feedwater tothe boiler. A disadvantage of using
thewater–steammixtureisthatsuperheatedsteamhastobegenerated;otherwise
the moisture content after expansion might be too high, which would erode the
turbineblades.Organicsubstancesthatcanbeusedbelowatemperatureof400 C
(cid:2)
do not have to be overheated. For many organic compounds superheating is not
necessary,resultinginamoreefficientcycle.Inaheatrecoverysystem,itmaybe
shownthatifthedegreeofsuperheatingisreduced,moresteamcanbegenerated
and hence more energy can be recovered from the heat source as shown in
Q8.36.* The working fluid superheats as the pressure is reduced, unlike steam,
which becomes wet during the expansion process. Organic fluids also have low
freezingpointsandhenceevenatlowtemperaturesthereisnofreezing.Theratio
of latent heat to sensible heat allows for greater heat recovery than in steam
systems.
AnOrganicRankineCycle(ORC)canmakeuseoflowtemperaturewaste
heat such as geothermal heat togenerate electricity. At these low temperatures a
steam cycle would be inefficient, because of the enormous volume of low
pressuresteam,whichwouldrequireveryvoluminousandcostlypipingresulting
in inefficient plants. Small-scale ORCs have been used commercially or as pilot
plants in the last two decades. Several organic compounds have been used in
ORCs (e.g., CFCs, Freon, isopentane, or ammonia) to match the temperature of
theavailablewasteheat.Wasteheattemperaturescanbeaslowas70–80 C.The
(cid:2)
efficiency of an ORC is estimated to be between 10% and 20%, depending on
temperature levels. To minimize costs and energylosses it is necessary to locate
anORCneartheheatsource.Itisalsonecessarytocondensetheworkingvapor;
therefore,acoolingmediumshouldbeavailableonsite.Thesesitecharacteristics
will limit the potential application. Condensing pressure is higher than atmo-
spheric,sothereisnoneedforvacuumequipment.ORCisexpensiveonthebasis
of cost per kilowatt-hour compared to other systems, but the main advantage is
that it can generate power from low temperature heat sources. ORC plants can
alsobeoflargecapacity.A14MWpowerplantusingFlurinol85astheworking
*Q8.36referstotheQandAsectioninChapter8.Thisnomenclaturewillbeusedthroughout.
Copyright © 2003 Marcel Dekker, Inc.

fluid is in operation in Japan, using the energy recovered from the effluents of
asinteringplant.Thelowboilingpointandlowlatentheatofthisfluidcompared
to steam help recover a significantly greater amount of energy from the hot
gases.
COMBINED CYCLE AND COGENERATION PLANTS
Gas turbine plants operate in both combined cycle and cogeneration mode (Fig.
1.9).Figure1.10showsthearrangementofanunfiredHRSGusedinsuchplants.
Large combined cycle plants with thousands of megawatts in capacity are being
built today. Chemical plants, refineries, and process plants use HRSGs in
cogeneration mode to supply steam for various purposes. The combined cycle
plantwithagasturbineexhaustingintoanHRSGthatsuppliessteamtoasteam
turbineisthemostefficientelectricgeneratingsystemavailabletoday.Itexhibits
lowercapitalcoststhanfossilpowerplants.Table1.1showstheaveragecostofa
gas turbine. The HRSG price ranges from about $80 to $130 per kilowatt.
Combining the Brayton and Rankine cycles results in efficiencies significantly
above the 40% level, which was an upper limit of large coal-fired utility plants
built30–50yearsago.Distillateoilsandnaturalgasaretypicallyfiredinthegas
turbines. Combined cycle plants have a number of advantages:
Modular designs enable increases in plant capacity as time passes.
Theseplantshaveshortstart-up periods. Theycome on-line inacouple of
hours from the cold.
Combined cycle plants can be built within 12–20 months, unlike a large
utility plant, which takes 3–4 years.
FIGURE 1.9a Combinedcycle system showingthe Brayton–Rankine cycle.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.9b Cogeneration systems.
Advances in gas turbine technology and cooling systems can be made use
of to improve the overall system efficiency. We are close to 60% LHV
efficiency with recent developments such as high pressure, multiple-
pressure steam systems and reheat steam cycles.
EmissionsofNOxandCOforplantsburningnaturalgasareinsingle-digit
plants per million (ppm).
Cooling water requirements are low due to higher efficiencyand the small
ratio of Rankine cycle power to total power output. The Brayton cycle
portion does not require cooling water.
Large-capacityadditionsarefeasible.Today’scombinedcycleplantisrated
in thousands of megawatts, which is otherwise feasible only with coal-
fired power plants.
Recent developments in gas turbine technology such as closed steam
cooling of blades enable firing temperatures to be increased, thus increasing
the simple cycle efficiency. Every 100 F increase in firing temperature increases
(cid:2)
theturbinepoweroutputby10%andgivesa4%gaininsimplecycleefficiency.
In large systems, an HRSG with three pressure levels and reheat is used,
Copyright © 2003 Marcel Dekker, Inc.

FIGURE1.10 UnfiredHRSG inagas turbine plant.
Copyright © 2003 Marcel Dekker, Inc.

TABLE1.1 Gas TurbinePricing
Machinesize (MW) Cost($=kW)
1–2 600–650
5 400–450
50 275–300
150 180–190
250 175–185
260–340 175–180
Note: A host of factors affect pricing, and the
abovenumbersgiveanidea onlyand shouldbe
usedwithcaution.
Source:Ref.14.
increasing the plant efficiency to 55% LHV. Table 1.2 presents data for a few
systems that are being commercially offered. The data are typical only.
Inspite ofall the advantages mentioned, it should be noted that theoutput
ofagasturbinedecreasessignificantlyastheambienttemperatureincreases.The
lower density of warm air reduces the mass flow through the turbine and the
exhaust gas flow through the HRSG, which in turn reduces its steam generation
and hence the steam turbine power output. Unfortunately, hot weather also
corresponds to peak electrical loads in many areas of the world. Hence a few
methods are used to improvethegas turbine power output in summer. The three
most common methods of increasing the gas turbine (GT) output are [7]
Injection of steam into the gas turbine
Precooling of the inlet air
Supplementary firing in the HRSG
Steam Injection
Injecting steam into thegas turbine has been a strategy adopted by turbine users
for a long time to increase its power output. The increased mass flow coupled
withthehigherthermalconductivityandspecificheatoftheexhaustgases(dueto
the higher percent by volume of water vapor) generates more power in the gas
turbine and higher steam output inthe HRSG. The Chengcycle,discussed later,
is a good example of this technique. Besides increasing the power output, it
reduces the turbine NOx levels.
Precooling of the Inlet Air
Evaporativecoolingbooststheoutputofthegasturbinebyincreasingthedensity
and mass flowof the air. Water sprayed into the inlet air stream cools the air to
Copyright © 2003 Marcel Dekker, Inc.

TABLE1.2 Typical Combined CyclePlants
System
Simplecycle data 7FA 9FA 6FA W501F
Simplecycle output,kW 159,000 226,500 70,140 187,000
Simplecycle heatrate (LHV) 9500 9570 9980 9235
Simplecycle efficiency, %LHV 35.9 35.7 34.2 36.9
Pressureratio 14.7 14.7 14.6 15
Firingtemperature, F 2350 2350 2350 —
(cid:2)
Exhaustgas flow,lb=h 3,387,000 4,877,000 1,591,000 1,645,200
Exhaustgas temperature, F 1093 1093 1107 1008
(cid:2)
HRSG system 3press,reheat 3press,reheat 3press, reheat Multipress,reheat
1 GT netoutput, MW 241.4 348.5 108.4 274
(cid:4)
Netheatrate(LHV), Btu=kWh 6260 6220 6455 6150
1 GT netefficiency, % 54.5 54.8 52.8 55.5
(cid:4)
2 GT netoutput, MW 483.2 700.8 219.3 550
(cid:4)
2 GT netheat rate,Btu=kWh 6250 6190 6385 6120
(cid:4)
2 GT netefficiency, % 54.6 55.1 53.4 55.8
(cid:4)
Source:Ref.9.
Copyright © 2003 Marcel Dekker, Inc.

near its wet bulb temperature. The effectiveness of the evaporative cooling
systems is limited by the relative humidity of the air. At 95 F dry bulb
(cid:2)
temperature and 60% relative humidity, an 85% effective evaporative cooler
canaltertheairinlettemperatureandmoisturecontentto85 Fdrybulband92%
(cid:2)
humidity, respectively. This boosts the gas turbine output and the HRSG steam
generation(duetothelargergasmassflow).Theincrementalcostofthissystem
is about $180=kW. The cost of treated water, which is lost to the atmosphere,
must also be considered in evaluating this system.The effectivenessof the same
system in less humid conditions, say 95 F and 40% relative humidity, is much
(cid:2)
higher. The same evaporativecooler canreduce theinletair temperature to75 F
(cid:2)
dry bulb and 88% humidity. The combined cycle plant output increases by 7%,
and the heat rate by about 1.9%. With evaporative coolers, the air cannot be
cooled below the wet bulb temperature, so chillers are used for this purpose.
Chillers canbe mechanical or absorption systems.Water isthe refrigerant,
and lithium bromide (LiBr) is the absorber in single-effect LiBr absorption
systems. A low grade heat source such as low pressure steam drives the
absorptionprocess,whichproduceschilledwater.Absorbersdrawlittleelectrical
powerandarewellsuitedtocogenerationplantswheresteamisreadilyavailable.
SometimestheHRSGgeneratesthelowpressuresteamrequiredforchilling,orit
can be taken from some low pressure steam header. Unlike mechanical chillers,
theefficiencyofanabsorberisunchangedasitsloadisdecreased.Chilledwater
output is limited to around 44 F, yielding inlet air at 52 F.
(cid:2) (cid:2)
AmechanicalchillercaneasilyreducethetemperatureofGTinletairfrom
95 F to 60 F dry bulb and achieve 100% humidity. This increases the plant
(cid:2) (cid:2)
output by 8.9% but also degrades the net combined cycle heat rate by 0.8% and
resultsina1.5in.WCinletairpressuredropduetotheheatexchangerlocatedat
thechillingsection.Costscouldbeabout$165=kW.Absorptionsystemsaremore
complex than mechanical chillers.
Off-peak thermal storage is another method of chilling inlet air. A portion
oftheplant’selectricalorthermaloutputisusedtomakeiceorcoolwaterduring
leanperiods.Duringpeakperiods,thechillingsystemisturnedoffandthestored
ice is used to chill the inlet air.
The performance of HRSGs with varying ambient temperatures is
discussed later. One can appreciate from the example why inlet air cooling is
necessary, particularly in locations where ambient temperatures are very high.
Improvements in Gas Turbines
Inordertohandlethehighfiringtemperatures,intherangeof2500–2600 F,gas
(cid:2)
turbinesuppliersaredoing researchanddevelopmentworkonturbinebladesfor
protection against corrosion and thermal stresses. Thermal barrier coatings have
been used on turbine blades for several years. The base high alloy material
Copyright © 2003 Marcel Dekker, Inc.

ensuresthemechanicalintegrity,whilethecoatingsprotectagainstoxidationand
corrosion as well as reducing the blade surface temperature. The rotating blades
are manufactured by using single-crystal casting technology, which allows the
chemical composition of the alloys to be modified to improve their resistance to
fatigue and creep. Thermal barrier coatings comprise two layers: the outer
ceramic layer, which prevents flowof heat into the turbine blade, and a metallic
bond coating, which is a nickel- or cobalt-based material.
General Electric uses closed loop steam cooling for the blades in its quest
for higher firing temperatures. This unique cooling system allows the turbine to
fireahighertemperature,around2600 F,forhigherperformance.Earlierdesigns
(cid:2)
were cooled by compressor dischargeair, whichcauses a largetemperature drop
in the first-stage nozzle. Cooling with steam systems has been found to be more
effectivebecauseitpicksupheatforuseinthesteamturbine,transformingwhat
waswasteheattousableheat.Inconventionalgasturbines,compressorairisalso
used to cool rotational and stationary components downstream of the stage 1
nozzle.Thisiscalledchargeableairbecauseitreducesperformance.Inadvanced
systems, this air is replaced by steam, which enhances performance by 2% and
increases thegas turbine output because all the compressor air can be channeled
throughtheturbinepathtodousefulworkintheturbineaswellasintheHRSG
[9]. The high pressure steam from the HRSG is expanded through the steam
turbine’s high pressure section. The exhaust steam from this turbine section is
thensplit.OnepartisreturnedtotheHRSGwhiletheotheriscombinedwiththe
intermediatepressuresteamandusedforcoolinginthegasturbine.Steamisused
to cool the stationary and rotational parts of the turbine. In turn, the heat
transferredfromthegasturbineincreasesthesteamtemperaturetoapproximately
reheattemperature.Thegasturbinecoolingsteamismixedwiththereheatsteam
from the HRSG and introduced into the intermediate pressure steam turbine
section [8].
COAL-BASED SYSTEMS
Though combined cycle plants based on natural gas (Fig. 1.9a) arewidely used,
with the increasing cost of natural gas several coal gasification technologies are
gaining acceptance. The technology is proven, and there are several plants in
operation throughout the world. The advantages of integrated coal gasification
combined cycle (IGCC) are
Ability to use of low grade fuels such as coal and biomass.
Highefficiency,about7–8%higherthanconventionalcoal-basedplants.A
net efficiency of 45% is not impossible.With improvements in gasifica-
tionandgasturbinetechnologies,theefficiencycanreach50%by2010.
Copyright © 2003 Marcel Dekker, Inc.

Fuel flexibility. The combined cycle portion of the plant can be fueled by
natural gas, oil, or coal. A plant can switch from gas to coal as gas
becomes unavailable or very expensive. Most gasifiers can handle
different grades of coal. Gas turbine combustors can also handle
different fuels with different heating values and gas analysis from low
to high Btu.
LowSO ,NOx,andCO emissions.InanIGCC,90%ofthecoal’ssulfuris
2 2
removedbeforecombustion.NOxisreducedby90%,asisalsotheCO
2
onlb=kWhbasis.Thecoalgasispurifiedbeforecombustion,unlikeina
conventionalcoal-firedplant,wherethefluegasesarecleaned.Hencethe
quantity of effluent to be handled is much smaller. The composition of
the fuel gas also allows for better chemistry while cleaning.
Low water consumption due to higher efficiency and lower heat losses.
Marketable by-products such as sulfur, sulfuric acid, and carbon dioxide.
Awiderangeoftechnologiessuchasfixedbed,fluidizedbed,andentrained
bed gasification.
Ability to make use of advances in gas turbine technology.
Availability of IGCC plants, which has been in excess of 90% and is
improving.
Higher gas turbine power output possible due to about 14% larger mass
flow of flue gases at the same combustion temperature compared to
natural gas.
Decreasing installation costs due to advances in technology. $1000=kW
will be achievable in the near future. Unit sizes range from 100 to
500MW.
In an IGCC, coal is gasified in a gasifier by using steam and either air or
oxygen to generate a low or high Btu gas, which is cleaned and fired in a gas
turbine combustor. There are three processes for gasifying coal: fixed bed,
fluidized bed, and entrained bed. Figure 1.3 shows an IGCC plant. Typically,
coalisgasifiedinthegasifieratpressureusingsteam,oxygenorair,andcoal.The
coal gas is cooled in a synthesis gas cooler, which also generates steam or
superheats the steam generated elsewhere. It is then cleaned in a gas cleaning
system,wheretheparticulatesandsulfurareremoved.Hotgascleaningmethods
are also being developed, which can improve the efficiency of the system even
more.Thecleancoalgasisfiredinthegasturbinecombustor.Theexhaustgases
generate high pressure steam for the steam turbine and also for gasification. A
portion of the air from the gas turbine compressor is also sent to the gasifier.
There are several plants in operation throughout the world. In the United States
the Wabash River plant, which began operation in 1995 (Fig. 1.3) generates
262MWusing the Destec process for gasification, which uses an entrained flow
Copyright © 2003 Marcel Dekker, Inc.

oxygen-blown gasifier. Coal is slurried, combined with 95% pure oxygen, and
injectedintothefirststageofthegasifier,whichoperatesat400psigand2600 F.
(cid:2)
The coal slurry undergoes a partial oxidation reaction at temperatures that bring
the coal’s ash above its melting point. From the gasifier the fluidized ash falls
through a tap hole at the bottom. The synthesis gas flows into the second stage,
where additional coal slurry is injected. At this stage the coal is pyrolyzed in an
endothermicreactionwiththehotsynthesisgas.Thisenhancestheheatingvalue
of the synthesis gas.
After leaving the second stage the synthesis gas flows into a gas cooler,
which is a waste heat boiler that generates high pressure saturated steam at
1600psia. After cooling, any remaining particulates are removed in a hot=dry
filter.Furthercoolingofgastakesplaceinaseriesofexchangers.Itisscrubbedto
remove chlorides and passed through a catalyst that hydrolyzes the carbonyl
sulfideintohydrogensulfide.TheH Sisremovedbyanacidgasremovalsystem.
2
Amarketableelementalsulfurisproducedasaby-product.Finallythesweetgas
is moisturized and preheated before being sent to the gas turbine. The power
block consists of a GE 192 MW MS7001A gas turbine, The exhaust gases
generatesteam intheHRSG,which generatespower viaasteam turbine.Thisis
presently the largest gasification repowering project. The heat rate is around
8910Btu=kWh (HHV) with SO emissions around 0.1lb=MM Btu, NOx 0.15,
2
and particulates below detectable limits [10].
Coal will remain a major fuel, more so with the significant run-up in the
priceofgas,andIGCCplantshaveearnedapermanentplaceinpowergeneration
technology. The heat exchanger and the HRSG are designed to meet the special
requirementsofthisprocess.Oxygen-blowngasificationhasdominatedcommer-
cial gasification processes, because these plants produce chemicals based on
synthesis gas (H and CO) and premium fuels. Air-blown gasifiers, which
2
generatelowBtugas,arealsowidelyusedintheindustry.Air-blowngasification
produces a gas in which the desirable chemical reactants are diluted by massive
amountsofnitrogen.Thegasifiercapacityiscutinhalfwhenitisair-blown.The
efficiency of conversion of feed to fuel gas is higher with oxygen-blown
gasification. The air-blown gasification produces over twice as much gas as is
generated by oxygen-blown operation; hence investment costs for air-blown
systems and cleanup systems are higher. Cleanup costs are also higher because
the partial pressures of the pollutants are higher in air-blown system raw gas.
Compressioncostsarelowerbecausethemassflowofanoxygen-blownsystemis
smaller by 20–40%.
The Sierra Pacific Power Company’s Pinon-Pine project employs an air-
blown system and a fluidized bed gasification process that uses low sulfur coal,
most of which is captured in the bed itself by the use of limestone injection
methods. A low Btu gas is generated, on the order of 130Btu=scf.
Copyright © 2003 Marcel Dekker, Inc.

EFFECT OF AMBIENT TEMPERATURE ON HRSG
PERFORMANCE
The power output of a gas turbine without inlet air temperature cooling or
conditioning suffers at highambienttemperature owing tothe effect of lower air
density,whichinturnreducesthemassflowofair.Thepoweroutputcoulddrop
byasmuchas15–25%betweenthecoldestandhottesttemperatures.Theexhaust
gasflow,temperature,andgasanalysisalsovarywithambienttemperature,which
affects the HRSG performance. Table 1.3 shows the data for a typical LM 5000
gas turbine.
Naturally, the performance of an unfired HRSG behind the gas turbine
wouldbeaffectedbythechangesinexhaustgasflowandtemperature.Usingthe
‘‘HRSGS’’ program (see Chap. 2), one can evaluate the HRSG performance
undervaryingambientconditions;theresultsareshowninFig.1.11.Onecansee
the large variation in the HRSG performance between summer and winter
months. In order to minimize the effect of ambient temperature on power
output, several methods are resorted to, such as the use of evaporative coolers,
mechanicalchillers,absorptionchillers,andthermalstoragesystemsasdiscussed
above.
EFFECT OF GAS TURBINE LOAD ON HRSG
PERFORMANCE
Generally gas turbines perform poorly at low loads, which affect not only their
[11,12]performancebutalsothatoftheHRSGlocatedbehindthem.Becauseof
the lowexit gas temperature at lower loads, the HRSG generates less steam and
alsohasthepotentialforsteamingintheeconomizer.Table1.4showstheexhaust
flow and temperature of a small gas turbine as a function of load. It should be
noted that the data are typical, presented to illustrate the point that at low gas
TABLE1.3 Gas TurbinePerformance atSelectedAmbient Temperatures
20 F 40 F 60 F 80 F 100 F 120 F
(cid:2) (cid:2) (cid:2) (cid:2) (cid:2) (cid:2)
Power, kW 38,150 38,600 35,020 30,820 27,360 24,040
Heatrate,Btu=kWh 9,384 9,442 9,649 9,960 10,257 10,598
Exhaust temp, F 734 780 797 820 843 870
(cid:2)
Exhaust flow,lb=h 1,123,200 1,094,400 1,029,600 950,400 878,400 810,000
Vol% CO 2.7 2.9 2.8 2.8 2.7 2.7
2
H O 7.6 8.2 8.5 9.2 10.5 12.8
2
O 14.6 14.3 14.3 14.2 14.0 13.7
2
N 75.1 74.7 74.4 73.8 72.8 70.8
2
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.11 HRSG performance versus ambient temperature. Gas flow shown has a multiplication
factorof 0.1.
Copyright © 2003 Marcel Dekker, Inc.

TABLE1.4 Typical GasTurbine Performanceat LowLoads
Load(%)
10 20 30 40 100
Generator kW 415 830 1244 1659 4147
Heatrate,Btu=kWh 48,605 28,595 21,960 18,649 12,882
Efficiency,% 7 12 15.54 18.3 26.5
Exhaust gas,lb=h 147,960 148,068 148,170 148,320 148,768
Exhaust temp, F 562 612 662 712 1019
(cid:2)
Vol% CO 1.18 1.38 1.59 1.79 3.04
2
H O 3.76 4.14 4.53 4.93 7.33
2
O 18.18 17.78 17.28 16.88 14.13
2
N 76.9 76.7 76.6 76.4 75.5
2
turbine loads the HRSG performance will be poor. Note that at low loads the
exhaust temperature is lower but the mass flow changes little.
TheHRSGperformanceat100%and40%loadsisgiveninFigs.1.12aand
1.12b. The HRSG was designed for the 100% case, and its performance was
checked at 40% load using the ‘‘HRSGS’’ program. It may be seen that the
economizergeneratessomesteam.Also,theexitgastemperaturefromtheHRSG
atlowloadisveryhighcomparedtothenormalcase.Thisisduetothefactthat
less steam is generated in the evaporator and hence the flow through the
economizer is also small, resulting in only a small gas temperature drop; the
heat sink at the economizer is not large enough to cool the gases to a low
temperature.ThusitisrecommendedthattheHRSGnotbeoperatedatlowloads
ofthegasturbineforlongdurations.If itisabsolutelyrequired,thenagasbypass
dampershouldbeused,ormethodssuggestedinQ8.41,maybetriedtominimize
economizer steaming.
EFFECT OF STEAM PRESSURE ON HRSG PERFORMANCE
Combinedcycleplantstodayoperateinslidingpressuremode;ifextractionsteam
isdesiredatagivenpressureforprocessreasons,thenaconstantpressuremaybe
requiredatthesteamturbineinlet.Typicallythesteampressureisallowedtofloat
by keeping the turbine throttling valves fully open and ensuring full arc
admission. The load range over which sliding operation is allowed varies from
about40%or50%to100%.Largevariationsinsteampressureaffectthespecific
volume of steam, which in turn affects the velocity and pressure drop through
superheater tubes and pipes, valves, etc. Large variations in steam pressure also
affect the saturation temperature at the drum and hence thermal stresses across
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.12a HRSGperformance at100% loadofgas turbine.
thickcomponentssuchasdrumandsuperheaterheaders,whichinturnlimitsthe
rate of load changes. Sliding pressure operation increases the efficiency of the
turbine at low loads due to lower throttling losses and also lowers the cost of
pumping if variable-speed pumps are used.
The steam pressure at turbine inlet increases linearly as the load increases;
however, the unfired HRSG steam output decreases as the steam pressure
increases. By matching the steam turbine and HRSG characteristics, one can
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.12b HRSG performance at40%load ofgasturbine.
arriveattheoperatingpointsatvariousloads.Becauseofthelargevariationsthat
occurindrumpressureduringslidingpressureoperation,thedrumlevelcontrols
should be pressure-compensated.
As an example, using the HRSG simulation program, the effect of steam
pressureonasingle-pressureunfiredHRSGwasevaluated;theresultsareshown
in Table 1.5. Note that when multiple-pressure HRSGs are involved, the
Copyright © 2003 Marcel Dekker, Inc.

TABLE1.5 Effect ofSteamPressure onHRSG Performancea
Pressure (psia)
400 600 800 1000
Steamflow,lb=h 69,900 68,225 67,320 66,800
Steamtemp, F 799 802 800 800
(cid:2)
Exitgas temp, F 354 373 388 401
(cid:2)
Duty, MMBtu=h 85.2 82.9 81.0 79.6
aFeedwatertemperature 230 F,heatloss 1%,blowdown 1%.
¼ (cid:2) ¼ ¼
performance of agivenmoduleis affectedbythe module precedingit, sounless
the configuration is known it is difficult to make generalized observations.
InthecaseforwhichdataaregiveninTable1.5,theHRSGwasdesignedto
generate steam at 1000psia and 800 F and the off-design performance was
(cid:2)
evaluated at selected pressures.
The steam flow decreases as the pressure increases due to the higher
saturation temperature, which limits the temperature profiles.
The exit gas temperature increases as the pressure increases, again due to
the higher saturation temperature.
The steam temperature does not vary by much.
The dutyor energy absorbed by steam decreases as pressure increases due
to the higher exit gas temperature.
AUXILIARY FIRING IN HRSGs
Supplementary firing is an efficient way to increase the steam generation in
HRSGs. Additional steam in the HRSG is generated at an efficiency of nearly
100%asshowninQ8.38.Typically,HRSGsincombinedcycleplantsareunfired
and those in cogeneration plants are fired. The merits of auxiliary firing in
HRSGs are discussed in Q8.38. Figure 1.13 shows the arrangement of a
supplementary-fired HRSG, which can handle a firing temperature of about
1600 F.Typically,oilornaturalgasisthefuelused.Figure1.14showsafurnace-
(cid:2)
fired HRSG, which can be fired up to 3000 F. The superheater is shielded from
(cid:2)
theflamebyascreensection.Thefurnaceshouldbelargeenoughtoenclosethe
flame. In furnace-fired HRSGs even a solid fuel can be fired and the HRSG
design approaches that of a conventional steam generator. Water-cooled
membrane walls ensure that the casing is kept cool. A large amount of steam
can be generated in this system. Table 1.6 compares the features of unfired,
supplementary-fired, and furnace-fired HRSGs.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE1.13 Multipressuresupplementary-fired HRSG.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.14a Furnace-firedHRSG arrangement.
Combined Cycle Plants and Fired HRSGs
It is generally believed that combined cycle plant efficiencies with fired HRSGs
arelowerthanthosewithunfiredHRSGs.Thereasonisnotthepoorperformance
oftheHRSG.Infact,afiredHRSGbyitselfisefficient.However,thelargelosses
associatedwiththeRankinecycle,particularlywhenthesteamturbinepowerisa
large fraction of the overall power output, distorts the results slightly as the
following example shows.
FIGURE 1.14b Photograph of a furnace-fired ABCO HRSG in a cogeneration
plant.
Copyright © 2003 Marcel Dekker, Inc.

TABLE1.6 General FeaturesofFired and UnfiredHRSGs
Unfired Supplementary-fired Furnace-fired
Gasinlet temp toHRSG, F 800–1000 1000–1700 1700–3200
(cid:2)
Gas=steamratio 5.5–7.0 2.5–5.5 1.2–2.5
Burnertype No burner Ductburner Ductor register
Fuel None Oilor gas Oil, gas,solid
Casing Internally insulated, Insulatedor membrane wall Membranewall,
4in.ceramic fiber external insulation
Circulation Natural, forced, Natural,forced,once-through Natural
once-through
Backpressure,in. WC 6–10 8–14 10–20
Configuration Single- or multiple- Single- ormultiple-pressure steam Single-pressure
pressuresteam
Other Convective design, Convectivedesign,finnedtubes Radiantfurnace,
finnedtubes generallybaretubes
Copyright © 2003 Marcel Dekker, Inc.

Example 1
AcombinedcycleplantusesafiredHRSG.ThegasturbineusedisLM5000.At
59 F,
(cid:2)
Exhaust gas flow 1,030,000lb=h at 800 F.
(cid:2)
¼
Gas analysis, vol%: CO 2.8, H O 8.5, N 74.4, O 14.3
2¼ 2 ¼ 2¼ 2¼
Power output 35MW; heat rate 9649Btu=kWh
¼ ¼
Steam turbine data:
Inlet pressure 650psia at 750 F
(cid:2)
¼
Exhaust pressure 1psia
¼
Efficiency 80%, dropping off by 2–3% at 40% load.
¼
HRSG data:
230 F feedwater, 2% blowdown, 1% heat loss
(cid:2)
Steam is generated at 665psia and 750 F.
(cid:2)
The HRSG generates 84,400lb=h in the unfired mode and a maximum of
186,500lb=hwhenfiredupto1200 F.TheHRSGperformancewassimulatedby
(cid:2)
using the HRSGS program. The system efficiency in both cogeneration and
combined cycle mode are calculated as follows:
Gas turbine fuel input 35;000 9649 337:71 MM Btu/h,
¼ (cid:4) ¼
lower heating value (LHV) basis.
Cogeneration mode efficiency at 900 F, from first principles (or
(cid:2)
fundamentals)
¼
35 3:413 129:9
ð (cid:4) þ Þ 100 67:9%
337:71 29:6 (cid:4) ¼
þ
where 129.9MM Btu=h is the HRSG output and 29.6MM Btu=h is the HRSG
burner input in LHV (lower heating value basis).
Combined cycle mode efficiency:
35 12:1 3:413
ð þ Þ(cid:4) 100 43:8%
337:71 29:6 (cid:4) ¼
þ
where 12.1 MW is the power output from the steam turbine.
Table 1.7 shows the results at various HRSG firing temperatures.
Cogeneration plant efficiency improves with firing in the HRSG as
discussed earlier. The combined cycle plant efficiency drops only because of
the lower efficiency of the Rankine system as the proportion of power from the
Rankinecycleincreases.TheHRSG,ascanbeseen,isefficientinthefiredmode
with a slightly lower stack gas temperature.
Copyright © 2003 Marcel Dekker, Inc.

TABLE1.7 Cogeneration andCombinedCycle Efficiencywith FiredHRSG
HRSG exit Turbine Cogen. Comb.
Gas inlet gas temp Boiler Burner power effic. cycle effic. Steam
temp( F) ( F) dutya dutyb (MW) (%) (%) (lb=h)
(cid:2) (cid:2)
800 435 99.8 0 9.2 64.9 44.7 84,400
900 427 129.9 29.6 12.1 67.9 43.8 109,700
1000 423 160.0 59.1 15.3 70.4 43.2 135,200
1100 420 190.4 90.7 18.2 72.3 42.4 160,960
1200 418 221.0 121.0 21.1 74.2 41.75 186,500
aBoilerdutyistheenergyabsorbedbysteam,MMBtu=h.
bBurnerdutyisthefuelinputtoHRSG,MMBtu=h,LHVbasis.
Generating Steam Efficiently in Cogeneration Plants
Today’scogenerationplantshavebothHRSGsandpackagedsteamgenerators.To
generate a desired quantityof steam efficiently, the load vs. efficiencycharacter-
istics of both the HRSG and steam generator should be known. Although the
generationofsteamwiththeleastfuelinputistheobjective,itmaynotalwaysbe
feasible, for reasons of plant loading, availability or maintenance, However the
information is helpful for planning purposes [13].
To explain the concept, an HRSG and a packaged boiler both capable of
generating up to 100,000lb=h of 400psig saturated steam on natural gas are
considered. In order to understand how the cogeneration system performs, one
should know how the HRSG and the steam generator perform as a function of
load. Figure1.15shows theload vs. efficiencycharacteristics ofboth theHRSG
and packaged boiler. The following points may be noted.
1. The exit gas temperature from the HRSG decreases as the steam
generationisincreased.Thisisduetothefactthatthegasflowremains
the same while the steam flow increases, thus providing a larger heat
sinkattheeconomizerasdiscussedearlier.Ontheotherhand,theexit
gas temperature from the steam generator increases as the load
increases because a larger quantity of flue gas is handled by a given
heat transfer surface.
2. TheASMEHRSGefficiencyincreasesasfiringincreasesasexplained
inQ8.38.Therangebetweenthelowestandhighestloadissignificant.
The steam generator efficiency increases slightly with load, peaks
around 60–75%, anddrops off. Thevariation between 25%and 100%
loadsismarginal.Thisisduetothecombinationofexitgaslossesand
casing heat losses. The casing loss is nearly unchanged with load in
Btu=h but increases as a percentage of total loss at lower loads. The
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.15 Load versus efficiency characteristics of HRSG and steam
generator.
flue gas heat loss is lower at lower loads due to the lower exit gas
temperature and mass flow.
Performancecalculationsweredoneatloadsrangingfrom25%to100%for
boththesteam generator andtheHRSG. Results arepresentedinTables1.8 and
TABLE1.8 SteamGenerator PerformanceatVarious Loadsa
Load(%)
25 50 75 100
Steamflow,lb=h 25,000 50,000 75,000 100,000
Excess air,% 30 10 10 10
Duty, MMBtu=h 25.4 50.8 76.3 101.6
Fluegas,lb=h 30,140 50,600 76,150 101,750
Exitgas temp, F 265 280 300 320
(cid:2)
Drygasloss, % 3.93 3.56 3.91 4.27
Airmoisture, % 0.1 0.09 0.1 0.11
Fuelmoisture, % 10.43 10.49 10.58 10.66
Casing loss,% 2.00 1.0 0.7 0.5
Efficiency,HHV % 83.54 84.86 84.7 84.46
Efficiency,LHV % 92.58 94.05 93.87 93.60
Fuel,MM Btu=h(LHV) 27.5 54.0 81.3 108.6
aSteampressure 400psig;feedwater 230 F,blowdown 5%.
¼ ¼ (cid:2) ¼
Fuel:naturalgas.C 97;C 2;C 1vol%
1¼ 2¼ 3¼
Copyright © 2003 Marcel Dekker, Inc.

TABLE1.9 HRSG Performanceat VariousLoadsa
Load
25 50 75 100
Steamgeneration,lb=h 25,000 50,000 75,000 100,000
Duty, MMBtu=h 25.4 50.8 76.3 101.6
Exhaust gasflow,lb=h 152,000 153,140 154,330 155,570
Exitgas temp F 319 285 273 269
(cid:2)
Fuelfired, MMBtu=h(L) 0 24.5 50.0 76.5
ASME efficiency,% 70.8 83.79 88.0 89.53
aSteampressure 400psig;feedwater 230 F;5%blowdown.
¼ ¼ (cid:2)
FuelinputisonLHVbasis.
1.9.Additionalperformancecalculationsmayalsobedoneforintermediatesteam
generation values. Table 1.10 presents the total fuel required for a given total
steamoutputandshowsthesplitbetweentheboilerandHRSGsteamgeneration.
It is obvious that the HRSG should be used first to make any additional
steam, because its fuel utilization is the best. However, if for some reason we
cannot operate the HRSG, then information on how the total fuel consumption
varies with the loading of each type of boiler helps in planning. For example, if
100,000lb=hofsteamisrequired,thesteamgeneratorcanbeshutoffcompletely
and the HRSG can be fully fired; the next best mode is to run the HRSG at
TABLE1.10 FuelConsumption at VariousLoads
Totalsteam HRSG Boiler HRSG fuel Boiler fuel Totalfuel
(lb=h) steam steam (MMBtu=h) (MMBtu=h) (MMBtu=h)
200,000 100,000 100,000 76.5 108.5 185
150,000 50,000 100,000 24.5 108.5 133.0
150,000 75,000 75,000 50.0 81.3 131.3
150,000 100,000 50,000 76.5 54.0 130.5
100,000 0 100,000 0 108.5 108.5
100,000 25,000 75,000 0 81.3 81.3
100,000 50,000 50,000 24.5 54.0 78.5
100,000 75,000 25,000 50.0 27.4 77.4
100,000 100,000 0 76.5 0 76.5
50,000 0 50,000 0 54.0 54.0
50,000 25,000 25,000 0 27.4 27.4
50,000 50,000 0 24.5 0 24.5
Copyright © 2003 Marcel Dekker, Inc.

75,000lb=handtheboilerat25,000lb=horinthatrange.Asimilartablemaybe
prepared if there are multiple units in the plant, and by studying the various
combinations a plan for efficient fuel utilization can be developed. Note that a
typical packaged boiler generates steam at about 92% efficiency on LHV basis,
whereas it is nearly 100% if the same amount of fuel (gas or oil) is fired in an
HRSG.
Cogeneration Plant Applications
The steam parameters of combined cycle and cogeneration plants differ signifi-
cantly.
CombinedcycleplantstypicallyuseunfiredHRSGsandgeneratemultiple-
pressure-level steam with a complex arrangement of heating surfaces to
maximize energy recovery. Fired HRSGs in combined cycle plants are
often the exception to the rule owing to their impact on cycle efficiency
as discussed above.
In cogeneration plants, a large amount of steam is required and hence
supplementary or furnace-fired HRSGs are common. With a high gas
inlet temperature, a single-pressure HRSG can often cool the gases to a
reasonablylowtemperature,sosingle-pressuresteamgenerationisoften
adequate.
Incogenerationplants,saturatedsteamisoftenimportedfromotherboilers
to the HRSG to be superheated; steam may also be exported from the
HRSG to other plants.
Combined cycle plant HRSGs often operate at steady loads, cogeneration
plant steam demand often fluctuates and is a function of the process.
Given below is an example of an HRSG simulation in a cogeneration
plant. Note the effect on steam temperaturewith and without the export
steam.
Example 2
Exhaust gas flow from a gas turbine is 250,000lb=h at 1000 F. Gas analysis in
(cid:2)
percent by volume (vol %) is CO 3, H O 7, N 75, and O 15. Super-
2¼ 2 ¼ 2¼ 2¼
heatedsteamisgeneratedat600psiaat875 F,andabout20,000lb=hofsaturated
(cid:2)
steam is required for process, which is taken off the steam drum. Predict the
HRSGgas=steamprofiles.Use20 Fpinchandapproachpoints,230 Ffeedwater,
(cid:2) (cid:2)
and 1% blowdown and heat loss.
In the off-design mode, process steam is not required. Steam pressure is
650psia. Determine the HRSG performance. Steam temperature is uncontrolled.
Copyright © 2003 Marcel Dekker, Inc.

Solution. The design mode run is shown in Fig. 1.16a. The evaporator
generates 37,883lb=h, and 17,883lb=h is sent through the superheater as
20,000lb=h is taken off for process from the drum.
Intheoff-designmode,almostallofthesteam,35,270lb=h,issentthrough
thesuperheater.Asaresultthesteamtemperatureislower,only749 F,asshown
(cid:2)
in Fig. 1.16b. Note that without the program it would be tedious to perform this
FIGURE 1.16a PerformanceofaHRSG with process steamuse.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.16b Performance ofthe HRSG whenprocess steamis not required.
calculation, because we have no idea of the exit gas temperature in the design
mode.
COMBINED CYCLE PLANT HRSG SIMULATION
The HRSG simulation concept is helpful in predicting the performance of an
HRSG at various modes of operation. The HRSG need not be designed to
perform this study. Figure 1.17a shows a multiple-pressure HRSG used in a
combinedcycleplantwithninemodules.Module1superheaterisfedbymodule
3, which consists of a superheater, evaporator, and economizer. Module 2 is a
reheater.Module7evaporatorfeedsmodule4superheater.Module5economizer
Copyright © 2003 Marcel Dekker, Inc.

FIGURE1.17a HRSGschemeinacombinedcycleplant.Modules1,3,and5are
HP sections. Modules 6, 8, and 9 are LP sections. Modules 4 and 7 are IP
sections.Module 2isareheater.
FIGURE 1.17b Temperature profilesandperformance ofthe HRSG.
Copyright © 2003 Marcel Dekker, Inc.

feedsmodule2,andmodule9evaporatorfeeds module6superheater.Module8
economizer feeds both modules 5 and 7.
TheHRSGSprogramcanbeusedtoarriveatthedesigncaseperformance
asshowninFig1.17b.TheUSvalue(productofoverallheattransfercoefficient
and surface area) for each surface is also shown. One may also use this
information to predict the HRSG performance at other off-design cases and
study, for example, the effect of steam pressure or the feedwater temperature on
the HRSG performance.
IMPROVING HRSG PERFORMANCE
By nature, HRSGs are inefficient, particularly the unfired units, because of the
large gas mass flow associated with the low exit gas temperature from the gas
turbine.Thelargemassflowforcesonetouseaboilerwithalargecrosssection,
though the steam generation may not be compatible with the size of the HRSG.
The low ratio of steam togas flow (15–18%) also results in a small heat sink at
the economizer leading to higher stack gas temperature. Hence single-pressure
units are inefficient. In addition,
1 Gas=steam temperature profiles are dictated by the steam pressure and
steam temperature, unlike in a steam generator, where one can easily
attain about 300 Fstack gastemperatureinasingle-pressureuniteven
(cid:2)
with high steam pressures on the order of 2000–2500psi. In a single-
pressure HRSG, the exit gas temperature is a function of the steam
pressureandtemperature.With600psigsteamsuperheatedto700 F,it
(cid:2)
isdifficulttogettheeconomizerexitgastemperaturebelow380 Finan
(cid:2)
unfired HRSG.
2 The higher the steam pressure, the lower the exit gas temperature
(single-pressureunit).Thispointisexplainedunder HRSG simulation:
see Q8.36.
3 The higher the steam temperature, the lower the steam generation and
thehighertheexitgastemperature.Thisisduetothesmalleramountof
steam generated with higher steam temperature and hence a smaller
heat sink at the economizer.
4 Partial load operation of a gas turbine also results in poor HRSG
performance, as shown above.
SohowcanweimprovetheHRSGperformance?Thereareseveraloptions.
Designs with Low Pinch and Approach Points
Pinch and approach points determine HRSG temperature profiles. If we have to
work with only a single-pressure HRSG and there is no additional heat recovery
Copyright © 2003 Marcel Dekker, Inc.

equipment such as a deaerator coil or condensate heater, we can use low pinch
and approach points to maximize steam generation. However, the surface area
requirementsincreaseduetothelowlog-meantemperaturesintheevaporatorand
economizer, which adds to the cost of the HRSG slightly and increases the gas
pressure drop. The major components of the HRSG such as controls and
instrumentation, drum size, casing, and insulation do not change in a big way,
and theadditional cost of heating surfacesmaynot be that significant ifwe look
attheoverallpicture.However,aneconomicevaluationmaybedoneasshownin
Q8.40.
Fired HRSGs
TheadvantagesoffiredHRSGswerediscussedearlier.Firingincreasesthesteam
generation and lowers the HRSG exit gas temperature with a fuel utilization of
nearly 100%. The additional fuel fired increases the HRSG duty by the same
amount compared to, say, 92% in a steam generator.
Using Secondary Surfaces
Because single-pressure HRSGs are not very efficient, one may consider adding
secondary surfaces such as as a deaerator coil or condensate heater or a heat
exchanger as shown in Fig. 1.18 to lower the stack gas temperature.
Multiple-Pressure HRSGs
Before going into this option, one should clearly understand when multiple-
pressureoptionsarejustified.FromthediscussiononHRSGsimulation,itcanbe
seenthattheexitgastemperatureinanHRSGdependsonthesteampressureand
temperature. The higher the steam pressure, the higher the exit gas temperature.
Hencewhen high pressure steam is generated, it will not be possible to cool the
exhaust gases to an economically justifiable levelwith a single-pressure HRSG.
Hence multiple-pressure steam generation iswarranted. Also, one can maximize
energy recovery by doing several things such as rearranging heat transfer
surfaces, splitting up economizers, superheaters, and evaporators so that the
gas temperature profiles match the steam and water temperatures and no large
imbalance exists between the gas and steam temperatures. This can be done by
using a program such as the HRSGS program (see Q8.37). In small HRSGs,
multiple-pressuresteamgenerationmaynotoftenbeviableduetothecomplexity
of the HRSG design and cost.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.18a Secondary surfaces to improve HRSG efficiency. 1, turbine; 2, deaerator; 3, HRSG; 4,
mixingtank; 5,pump; 6,deaerator coil; 7,condenser; 8,heatexchange; 9,condensate heater.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.18b Continued
Copyright © 2003 Marcel Dekker, Inc.

HIPPS
SeveralteamsoflargecompaniesintheUnitedStatesaredevelopingacoal-fired
highperformancesystem,alsocalledHIPPS.Inthiscombinedcycleplant,afluid
bedair-blownpyrolyzerconvertscoalintofuelgasandchar.Thecharisfiredina
hightemperatureadvancedfurnace,whichheatsupbothairforagasturbineand
steamforasteamturbine.Theairisheatedto1400 F.Thegasturbinecombustor
(cid:2)
raisestheairtemperatureto2350 Fandgeneratespowerinthegasturbine.High
(cid:2)
pressure steam is also generated in the HRSG [11].
CHENG CYCLE
One of the variations in cogeneration systems using gas turbines is the Cheng
cycle. This system is ideal for plants with varying electrical and steam loads. It
consistsofagasturbinewithanHRSG,whichhasasuperheater,evaporator,and
economizer (Fig. 1.19). A duct burner is located between the superheater and
evaporator. The HRSG generates saturated steam, which is superheated in the
superheaterandinjectedintothegasturbine,whichincreasesitselectricalpower
outputsignificantly.ThefigureshowsanAllison501Kmachine,whichnormally
generates 3.5MW, in injection mode about 6MW. The superheater is capable of
running dry, that is, without steam. When only process steam is required,
saturated steam from the evaporator is used. When additional process steam is
required, the duct burner is fired. Hence the HRSG can operate in a variety of
modes and at various points as shown in the figure by varying the amount of
steaminjectedintothegasturbineandbyvaryingtheamountoffuelfiredinthe
duct burner. Thus the plant can vary the ratio of power to process steam
significantly according to the cost of fuel or electricity and thus optimize the
overallefficiency.Cogenerationplantswithfluctuatingsteamandpowerdemands
are ideal candidates for the Cheng cycle. The system’s proven success in small-
scale plants is now being applied to midsized gas turbines ranging from
50 to 125MW. Cheng cycle systems are in operation in over 50 installations
worldwide.
HAT CYCLE
Another concept that is being studied is the humidified air turbine (HAT) cycle.
Thisisanintercooled,regeneratedcyclewithasaturatorthataddsaconsiderable
amount of moisture to the compressor discharge as shown in Fig. 1.20. The
combustor inlet contains 20–40% water vapor, depending on whether the fuel is
natural gas or gasified coal gas. The intercooling reduces the compressor work,
while the water vapor in the exhaust gases increases the turbine output. Capital
cost is lowered by the absence of steam turbine and condenser system. The gas
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.19 Cheng cyclescheme.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 1.20 HAT cycle scheme.A, intercooler;B, aftercooler; C,recuperator.
turbine combustor design is modified to handle the large amount of water vapor
intheincoming air.Cycle efficiencyisexpectedtobeintherange of55%LHV
with a significant increase in power output.
DIESEL ENGINE HEAT RECOVERY
Diesel engines are widely used as sources of power when an electrical utility
supply is not available. They may be fired on gaseous or liquid fuels. They are
mostly employed in lowand medium power cogeneration units, typically 50kW
to10MWfornaturalgasfiring,50kWto50MWfordiesel,and2.5–50MWfor
heavyfuel oils.Theyarewidelyused incountrieswheretheelectricity supplyis
not reliable. Diesel plants have several advantages and features:
Medium-sized reciprocating engines have substantially higher electrical
efficiencies than gas turbines of similar size (34–40% vs. 25–30%).
Partial load efficiencies are also higher.
They require lower fuel gas pressure for operation—20–40psig compared
to 180–400psig for gas turbines.
Electrical power output is less sensitive to ambient air temperature. The
output of a gas turbine drops off at higher ambient temperatures as
discussed above.
Capital costs are higher than these for gas turbines by 10–25%. Operating
andmaintenancecostsarealsohigher,butdieselenginescanbeusedon
heavy fuel oils, so fuel costs are lower. Developing countries use diesel
engine sets for on-site power needs because the power supply is not
dependable in many locations.
In applications calling for high power to heat recovery, hot water or low-
pressure steam, reciprocating engines are preferred to gas turbines. A
lowerexhaustgastemperature(650–800 F)makesthemlesssuitablefor
(cid:2)
high pressure heat recovery systems than gas turbines; also, the exhaust
Copyright © 2003 Marcel Dekker, Inc.

gascontainslessoxygen,ontheorder of10–12% comparedto14–15%
for turbine exhaust, making supplementary firing difficult, though not
impossible.
There are two main sources of heat available in diesel engines. One is the
enginecoolingwater,andtheotheristheexhaustgas(Fig.1.21).Theexhaustgas
temperature is often below 750 F, hence only low pressure saturated or super-
(cid:2)
heatedsteamisgenerated.Dependingonthecleanlinessofthegasstream,water
tube boilerswith extendedsurfacescould beusedfor heat recovery,though bare
tubeboilerswithsootblowerprovisionsareoftenused.Firetubeboilersareused
if the gas flow is small, less than 50,000lb=h. In many plants several diesel
enginesareusedatthesametime;hencebycombiningtheexhaustgasflowintoa
single large duct, a single waste heat boiler could be built. The gas is often
pulsating, so the boiler and casing design has to be rugged. Work is also being
done to supplementary fire the diesel engine exhaust by using solid fuels to
generate high pressure steam for combined cycle operation.
FIGURE 1.21 Diesel engine heat recovery system. Top: Combined cycle plant.
Bottom: Dieselcogeneration.
Copyright © 2003 Marcel Dekker, Inc.

REFERENCES
1. JB Kitto. Developments in pulverized coal-fired boiler technology. Presented to
Missouri Valley Electric Association Engineering Conference, Apr 10–12, 1996,
KansasCity.
2. SupercriticalSteamPowerCyclesforPowerGenerationApplications.Report,Deptof
Trade&Industry,London,UK,Jan1999.
3. IStambler.Kalinabottomingcycle3.2MWdemoplantrated26.9%efficiency.Gas
TurbineWorld,March-April1992.
4. J Corman. Kalina cycle looks good for combined cycle generation. Modern Power
SystemsReview,July1995.
5. AKalina.Kalinacyclepromisesimprovedefficiency.MPSReview,January1987.
6. Editor.Enhancinggasturbineperformance.Power,September1995.
7. Boswell.Choosebestoptionsforenhancingcombinedcycleoutput.Power,Septem-
ber1993.
8. GEReport.AdvancedTechnologyCombinedCycles.GeneralElectricCorp,October
2000.
9. Editor. Advanced gas turbines provide high efficiency and low emission. Power
Engineering,March1994.
10. USDeptofEnergy.CleanCoalTechnologyReport—WabashRiverCoalGasification
RepoweringProject,November1996.
11. VGanapathy. Understand boiler performance characteristics. Hydrocarbon Proces-
sing,August1994.
12. V Ganapathy. Heat-recovery steam generators: understand the basics. Chemical
EngineeringProgress,August1996.
13. VGanapathy. Efficiently generate steam from cogeneration plants. Chemical Engi-
neering,May1997.
14. D Franus. Thegas turbine powered electrical power generation market 2001–2010.
CogenerationandOn-SitePowerProduction,July–August2001.
Copyright © 2003 Marcel Dekker, Inc.

2
Heat Recovery Boilers
INTRODUCTION
Heatrecoveryboilers,alsoknownaswasteheatrecoveryboilersorheatrecovery
steamgenerators(HRSGs),formaninevitablepartofchemicalplants,refineries,
power plants,andprocesssystems.Theyareclassifiedinseveralways,ascanbe
seeninFig.2.1,accordingtotheapplication,thetypeofboilerused,whetherthe
fluegasisusedfor processormainlyforenergyrecovery,cleanlinessofthegas,
and boiler configuration, to mention a few. The main classification is based on
whether the boiler is used for process purposes or for energy recovery. Process
waste heat boilers are used to cool waste gas streams from a given inlet
temperature to a desired exit temperature for further processing purposes. An
example can be found in the chemical industry in a sulfuric acid or hydrogen
plant where the gas stream is cooled to a particular gas temperature and then
takentoareactorforfurtherprocessing.Theexitgastemperaturefromtheboiler
is an important parameter affecting the downstream process reactions and hence
is controlled by using a gas bypass system. Steam generation is of secondary
importanceinsuchplants.Inenergyrecoveryapplications,ontheotherhand,the
gas is cooled as much as possible while avoiding low temperature corrosion.
Examples can be found in gas turbine exhaust heat recovery or flue gas heat
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.1 Classification of wasteheatboilers.
Copyright © 2003 Marcel Dekker, Inc.

recoveryfromincinerators,furnaces,andkilns.Theobjectivehereistomaximize
energy recovery.
Ifthegasstreamisclean,watertubeboilerswithextendedsurfacesmaybe
used. In solid or liquid waste incineration applications, thegas is generally dirty
and may contain corrosive compounds, acid vapors, ash, and particulates. If the
ashcontainscompoundsofsodium,potassium,ornonferrousmetals,slaggingis
likely on heat transfer surfaces if these compounds become molten. In these
cases,baretubeboilerswithprovisionforcleaningthetubeswithsootblowersor
a rapping mechanism are used. A water-cooled furnace, which cools the gas
stream toatemperature belowtheashmelting temperatureand henceminimizes
slagging on the convective surfaces, may also be necessary.
Generally if the gas inlet temperature is high, say above 1400 F, a single-
(cid:2)
pressure heat recovery system is adequate to cool thegases to about 300–350 F.
(cid:2)
Ingasturbineexhaustheatrecoveryapplicationswithalowinletgastemperature
totheHRSGof900–1000 F,asingle-pressureheat recoverysystemcannotcool
(cid:2)
the gases adequately and a multipressure steam system is often required.
In the United States HRSGs are generally of natural circulation design,
whereasinEuropeitisverycommon toseeonce-through andforced circulation
designs. The features of these boilers are discussed later.
Fluegasanalysisisimportanttothedesignoftheboiler.Alargeamountof
water vapor or hydrogen increases the specific heat and thermal conductivity of
thegasandhencetheboilerdutyandheatflux.Forexample,thereformedgasin
hydrogenplantshasalargevolumeofhydrogenandwatervapor,whichincreases
theheattransfercoefficient by500–800%comparedtotypical fluegases. Hence
heatfluxisofconcerninthesetypesofboilers.Hydrogenchloride(HCl)vaporin
thefluegasesindicatescorrosivepotential,particularlyifasuperheateroperating
at high metal temperatures, say exceeding 900 F, is present. The presence of
(cid:2)
sulfur trioxide (SO ) vapor and HCl also suggests low temperature corrosion
3
problemsduetotheirlowaciddewpoints.Fluegaspressureinwasteheatboilers
istypicallyatmosphericorafewinchesofwatercolumn(in.WC)aboveorbelow
atmospheric pressure; however, there are applications such as the use of a
reformed gas boiler or synthesis gas boiler in hydrogen or ammonia plants
where the gas pressure could be as high as 300–1500psig (see Chap. 8, Table
8.46). Fire tube boilers are generally preferred for these applications, though
special water tube boiler designed with heat transfer surfaces located inside
pressure vessels have been built.
A common classification of boilers is based on whether the gas flows
insideoroutsidethetubes.Infiretubeboilers,thefluegasesflowinsidethetubes
(Fig. 2.2), whereas in water tube boilers, the gas flows outside the tubes as
shown in Fig. 2.3. The features of each type are discussed in the following
section.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE2.2 Firetubewasteheatboilerwithsuperheaterandeconomizer.(CourtesyofABCOIndustries,Abilene,
TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE2.3 Watertubewasteheatboilerwithsuperheaterandeconomizer.(CourtesyofABCOIndustries,Abilene,TX.)
Copyright © 2003 Marcel Dekker, Inc.

WATER TUBE VERSUS FIRE TUBE BOILERS
Table 2.1 shows a few aspects of fire tube and water tube waste heat boilers.
Generallywatertubeboilersaresuitableforlargegasflowsexceedingmillionsof
poundsperhourandcanhandlehighsteampressuresandtemperatures.Firetube
boilers are suitable for low steam pressures, generally below 500psig. Table 2.2
shows the effect of pressure on tube thickness in both types of boilers, and one
can see why fire tube boilers are not suggested for high steam pressure
applications.
Inwatertubeboilers,extendedsurfacescanbeusedtomakethemcompact
ifthegasstreamisclean,asdiscussedinQ8.21.Fluegaspressuredropwillalso
be lower than for an equivalent fire tube boiler owing to the compactness of the
design. Water tube boilers can be smaller and weigh less, particularly if the gas
flowislarge,exceeding100,000lb=h.Superheaterscanbeusedinbothtypes.In
a water tube boiler they can be located in an optimum gas temperature zone. A
shield screen section or a large convectionsection precedes the superheater. In a
fire tube boiler, the superheater has to be located at either the gas inlet or exit,
making the design less flexible and vulnerable to slagging or corrosion. If the
wastegasisslagginginnature,awatertubeboilerisdesiredbecausethesurfaces
canbecleanedbyusingretractablesootblowers.Ingeneral,thetypeofboiler to
TABLE2.1 AComparison of FireTube and WaterTube Boilers
Variable Firetubeboiler Watertubeboiler
Gas flow Small—less than 50,000 tomillions of
50,000lb=h lb=h
Gas inlet temperature Lowto adiabatic Lowto adiabatic
combustion combustion
Gas pressure High—even ashigh Generally lessthan
as2000psig 2psig
Firing Possible Possible
Typeof heatingsurface Bare tube Bare andfinnedtubes
Superheaterlocation At inlet orexit ofboiler Anywhere inthe gas
pathusing screen
section
Waterinventory High Low
Heatflux-steam side Generally low Canbehigh withfinned
tubes
Multiple steampressure No Yes
Sootblower location Inlet or exitofboiler Anywhere inside boiler
surfaces
Multiple modules No Yes
Copyright © 2003 Marcel Dekker, Inc.

TABLE2.2 Tube Thicknessvs. SteamPressure—ASMESec 1
Tube thicknessa External pressure Internalpressure
(in.) (psig) (psig)
0.105 575 1147
0.120 686 1339
0.135 800 1533
0.150 921 1730
0.180 1172 2137
a2in.OD,SA178aandSA192carbonsteeltubesat700 F.
(cid:2)
beusedforaparticularcaseisdeterminedbytheexperienceofthemanufacturer.
Sometimes a combination of fire and water tube boilers is used to suit special
needs.
HEAT RECOVERY IN SULFUR PLANTS
A sulfur plant forms an important part of a gas processing system in a refinery.
Sulfur ispresent innaturalgas ashydrogen sulfide (H S);it is theby-product of
2
processing natural gas and refining high sulfur crude oils. For process and
combustion applications, the sulfur in the natural gas has to be removed. Sulfur
recovery refers to the conversion of hydrogen sulfide to elemental sulfur. The
most common process for sulfur removal is the Claus process, which recovers
about 95–97% of the hydrogen sulfide in the feedstream. Waste heat boilers are
an important part of this process (Fig. 2.4).
The Claus process used today is a modification of a process first used in
1883,inwhichH Swasreactedoveracatalystwithair toformelemental sulfur
2
and water. The reaction is expressed as
H S 1=2O S H O
2 þ 2 (cid:3)! þ 2
Control of this exothermic reaction was difficult, and sulfur recovery efficiency
was low. Modifications later included burning one third of the H S to produce
2
sulfur dioxide, SO , which is reacted with the remaining H S to produce
2 2
elemental sulfur. This process consists of multistage catalytic oxidation of
hydrogen sulfide according to the reactions
2H S 3O 2SO 2H O heat
2 þ 2 ! 2þ 2 þ
2H S O 2S 2H O
2 þ 2 ! þ 2
Each catalytic stage consists of a gas reheater, a catalyst chamber, and a
condenser as shown in Fig. 2.4.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.4 Claus processforsulfurrecovery.
Copyright © 2003 Marcel Dekker, Inc.

In addition to the oxidation of H S to SO and the reaction of SO with
2 2 2
H S in the reaction furnace, many other side reactions occur, such as
2
CO H S COS H O
2þ 2 ! þ 2
COS H S CS H O
þ 2 ! 2þ 2
2COS CO CS
! 2þ 2
The gas stream contains CO ;H S;SO ;H ;CH , and water vapor in
2 2 2 2 4
addition to various species of sulfur. The duty of the boiler behind the sulfur
combustor includes both sensible heat from cooling of the gas stream from
2600 Ftoabout650 Fandthedutyassociatedwiththetransformationofvarious
(cid:2) (cid:2)
speciesofsulfur.Thereactionfurnacenormallyoperatesat1800–2800 F,andthe
(cid:2)
fluegasesarecooledinawasteheatboiler(Fig.2.5),inwhichsaturatedsteamat
about 600psig is generated. This is typically of two-gas-pass design, though
single-passdesignshavebeenused.Thegasiscooledtoabout1200 Finthefirst
(cid:2)
pass and finally to about 650 F in the two-pass boiler.
(cid:2)
Figure2.6showstheboilerforalargesulfurrecoveryplant,whichconsists
of two separate shells for each pass connected to a common steam drum. The
steam drum is external to the boiler. The external downcomer and riser system
ensures adequate cooling of the tubes and the tube sheet, which is refractory-
lined; ferrules are also used for further protection of the tube sheet. Ferrules are
generallymadeofceramicmaterialandareusedtotransfertheheatfromthehot
flue gases (at about 2800 F) to the tubes, which are cooled by water. The
(cid:2)
refractoryonthetubesheet,whichisabout4in.thickandmadeofahighgrade,
high density castable, lowers the tube sheet temperature at the hot end and thus
limits the thermal stress across it. The inlet gas chamber is also refractory-lined.
The casing is kept above 350–400 F through a combination of internal and
(cid:2)
externalinsulationtominimizeconcernsregardingaciddewpointcorrosion.This
is often referred to as ‘‘hot casing.’’ Q8.56 discusses this concept. The exit gas
chamberisexternallyinsulated,asarealsothedrum,downcomer,riserpipes,and
exchanger. The high pressure saturated steam, which is generated at about 600–
650psig, is purified by using steam drum internals and sent for process use.
About 65–70% of the sulfur is removed in the boiler as liquid sulfur by using
heated drains.
Though the boiler generally operates above the sulfur dew point, some
sulfur may condense at partial loads and during transient start-up or shutdown
mode.Thecooledgasesexitingtheexchangerarereheatedtomaintainacceptable
reactionratesandtoensurethatprocessgasesremainabovethesulfurdewpoint
andaresent tothecatalystbedsforfurtherconversionasshowninFig.2.4.The
catalytic reactors using alumina or bauxite catalysts operate at lower tempera-
tures,rangingfrom200to315 C.Becausethisreactionrepresentsanequilibrium
(cid:2)
chemical reaction, it is not possible for a Claus plant to convert all of the
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.5 Waste heatboilerforsulfur recoveryplant.(Courtesyof ABCO Industries,Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.6 Multiple boilerpassesconnectedtoa commonsteamdrum. (CourtesyofABCO Industries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.7 Sulfurcondenser. (Courtesy ofABCO Industries,Abilene, TX.)
incomingsulfurtoelementalsulfur.Thereforetwoormorestagesareused.Each
catalyticstagecanrecoveronehalftotwo-thirdsoftheincomingsulfur.Acidgas
isalsointroducedateachcatalyststageasshown.Thegasstreamfromeachstage
is cooled in another low pressure boiler, called the sulfur condenser, which
condenses some of the sulfur. These gas streams generate low pressure steam at
about 50–70psig in the sulfur condenser.
Ifthefluegasquantityissmall,asingle-shellfiretubeboilerhandlesallthe
streams from the reactors (Fig. 2.7). Each stage has its own gas inlet and exit
connections. The outlet gas temperatures of these exchangers are around 330–
360 F. From the condenser of the final catalytic stage the process stream passes
(cid:2)
on to some form of tail gas treatment process. The tail gas contains H S;SO ,
2 2
sulfur vapor, and traces of other sulfur compounds and is further treated
downstream and vented.
SULFURIC ACID PLANT HEAT RECOVERY
Sulfuric acid is an important chemical that is manufactured using the contact
process. Heat recovery plays a significant role in this system, whose main
objective,istocoolthegasstreamtoadesiredtemperatureforfurtherprocessing.
Copyright © 2003 Marcel Dekker, Inc.

Raw sulfur is burned with air in a combustion chamber, generating sulfur
dioxide, oxygen, and nitrogen. The gases, at about 1900 F and at a pressure of
(cid:2)
about 50in. WC, pass through a waste heat boiler generating saturated or
superheated steam. The boiler could be of fire tube or water tube design. The
gases are cooled to about 800 F, which is the optimum temperature for conver-
(cid:2)
sionofSO toSO .Theexitgastemperaturefromtheboilerdecreasesastheload
2 3
decreases.
In order to maintain the exit gas temperature at 800 Fat varying loads, a
(cid:2)
gas bypass system is incorporated into the boiler, either internally or externally
(Fig. 2.8). The gases then pass through a converter where SO gets converted to
2
SO inafewstagesinthepresenceofcatalystbeds.Thereactionsareexothermic,
3
and the gas temperature increases by 40–100 F. Air heating or superheating of
(cid:2)
steam is necessary to cool the gases back to 800 F. After the last stage of
(cid:2)
conversion, most of the SO has been converted to SO . The gas stream
2 3
containing SO gases at about 900 F is cooled in an economizer before being
3 (cid:2)
senttoanabsorptiontower.Thefluegasstreamisabsorbedindilutesulfuricacid
to form concentrated sulfuric acid. The scheme is shown in Fig. 2.9. The steam
thusgeneratedinthesewasteheatboilersisusedforprocessaswellasforpower
generation.
Themainboilerbehindthesulfurcombustorcouldbeoffiretubeorwater
tubedesign,dependingongasflow.Extendedsurfacesmayalsobeusedifthegas
stream has no dust. Sometimes, owing to inadequate air filtration and poor
FIGURE 2.8 Gas bypasssystems forHRSG exitgas temperaturecontrol.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.9 Scheme of a sulfuric acid plant. 1, sulfur combustion furnace; 2,
waste heat boiler; 3, contact apparatus; 4, superheater; 5, economizer; 6,
absorptiontower.
combustion, particulates are present in the flue gases, which could preclude the
useoffinnedtubes.Onehastobeconcernedaboutthecasingdesignbecause of
the possibility of sulfur condensation and corrosion. Soot blowing is not
recommended, because it affects the gas analysis and adds moisture to the flue
gases and may cause acid condensation.
Water-cooledfurnacedesignshaveanadvantageinthatthecasingoperates
atthesaturationtemperatureofsteam,henceacidcorrosionisunlikely.Themain
concern in sulfuric acid plants is corrosion due to acid condensation from
moisture reacting with SO . This is minimized by starting up and shutting
3
down the plants on clean fuels if possible and avoiding frequent start-ups and
shutdowns, which induce a cooler environment for possible acid condensation
over the exchanger or economizer tubes. The boiler and exchanger casings must
also be maintained above the dew point by using a ‘‘hot casing’’design, which
reduces the heat loss to the surroundings while at the same time keeping the
casing hot, above 350–400 F, as required. Boilers may be kept in hot standby if
(cid:2)
frequent shutdowns and start-ups are likely.
Thefeedwatertemperatureasitenterstheeconomizerhastobehigh,often
above320 F,tominimizeaciddewpointcorrosionbecausethegascontainsSO .
(cid:2) 3
Carbonsteeltubeswithcontinuouslyweldedsolidfinshavebeenusedinseveral
plants in the United States, whereas in Europe and Asia cast iron gilled tubes
shrunk over carbon steel tubes are widely used. In a few projects, the sulfur
deposits found their way between the gilled iron rings and the tubes and caused
corrosion problems. The choice of tube materials is based on the preference and
experience of the end user and the boiler supplier.
Copyright © 2003 Marcel Dekker, Inc.

Theinternalgasbypasssystemincreasestheshelldiametercomparedtothe
external bypass system. The bypass pipe also cools the gases to some extent, so
thedamperisnotexposedtothehightemperaturegasesasintheexternalbypass
system,wherethedamperislocatedinarefractory-linedpipeandhandlesthehot
inlet gases. Operability and maintenance of the damper are important aspects of
boileroperation.Bothinternalandexternalgasbypasssystemshavebeenusedin
the industry.
In fire tube boilers, ferrules and the refractory lining on the tube sheet
protect the tube sheet from the hot gases. An external steam drum with down-
comersandrisersensuresadequatecirculationofthesteam–watermixtureinside
the shell.
HEAT RECOVERY IN HYDROGEN PLANTS
Hydrogen and ammonia are valuable chemicals invarious processes. The steam
reforming process is widely used to produce hydrogen from fossil fuels such as
naturalgas,oil,orevencoalasshowninFig.2.10.Thereareseveralvariationsof
the process, but basically the steam reforming process converts a mixture of
hydrocarbons and steam into hydrogen, methane, and carbon dioxide in the
presenceofnickelcatalystinsidetubes.Beforeenteringthereformer,thenatural
gas has to be desulfurized in order to protect the reformer tubes and catalysts
from sulfur poisoning. The desulfurized gas is mixed with process steam,
preheated to about 500 C in the flue gas boiler, then sent through the tubes of
(cid:2)
the reformer. Reactions occur inside the tubes of the reformer at 800–950 C.
(cid:2)
FIGURE 2.10 Steam reforming process in hydrogen plants. 1, natural gas; 2,
sulfur removal; 3, reformer; 4, reformed gas boiler; 5, flue gas boiler; 6, shift
converter;7,airpreheater;8,air;9,CO removalandmethanation;10,Pressure
2
Swing Adsorption(PSA); 11, H product; 12,stack; 13,CO by-product.
2 2
Copyright © 2003 Marcel Dekker, Inc.

Reforming pressures range from 20 to 40atm, depending on the process
equipment supplier.
C H nH O nCO m=2 n H
n mþ 2 ! þð þ Þ 2
CH H O CO 3H
4þ 2 Ð þ 2
CO H O CO H
þ 2 Ð 2þ 2
Theoverallreactionishighlyendothermic,sothereactionheathastobeprovided
fromoutsidebyfiringfuelsuchasnaturalgasornaphthaoutsidethetubes.This
generates fluegases, typically at 1800 Fand atmospheric pressure, that are used
(cid:2)
to generate high pressure superheated steam in a water tube waste heat boiler,
generally referred to as a flue gas boiler. The flue gases also preheat the steam–
fuel mixture and air.
In some processes the effluents of the primary reformer are led to the
secondaryreformer,wheretheyaremixedwithpreheatedair.Chemicalreactions
occur,andthecatalystsconvertthemethanepartlytohydrogen.Theeffluentfrom
the reformer, called reformed gas, is at a high gas pressure, typically 20–40atm,
and contains hydrogen, water vapor, methane, carbon dioxide, and carbon
monoxide. This gas stream is then cooled from about 1600 F to 600 F in a
(cid:2) (cid:2)
reformed gas boiler, which is generally an elevated drum fire tube boiler (Fig.
2.11) with provision for gas bypass control to maintain the exit gas temperature
constant at all loads. The exit gas temperature from the boiler decreases as the
duty of the boiler decreases, and the bypass valve adjusts the flow between the
incoming hot gases and the cool exit gases to maintain a constant exit gas
temperatureatallloads.Thecooledgasesthenenterashiftconverter,whereCO
isconvertedtoCO inthepresenceofcatalystandsteam.Additionalhydrogenis
2
alsoproduced.Theexothermicreactionraisesthegastemperaturetoabout800 F.
(cid:2)
TheCOcontentisreducedfromabout13%to3%.Awasteheatboilerreferredto
as a converted gas boiler cools the gas stream before it enters the next stage of
conversion, where CO is reduced to less than 0.3%. The next stage is the
methanator, in which catalysts convert traces of CO and CO to methane and
2
water vapor. The H ;CO, and unreacted methane are then separated. This
2
producesagasstreamthatcanberecycledtoprocessfeedandproducehydrogen
of 98–99% purity that is further purified by the pressure swing adsorption
method. In older plants carbon dioxideis removedin a liquid absorption system
and finally the gas goes through a methanation step to remove residual traces of
carbon oxides.
Inlargeplants,thefluegasandreformed gasboilers areseparateunitsbut
haveacommonsteamsystem,whereasinsmallhydrogenplantstheseboilerscan
be combined into a single module. The flue gas boiler is a water tube unit; the
reformed and converted gas boilers are fire tube units connected to the same
steamdrum.Thefluegasboilercontainsvariousheatingsurfacessuchasthefeed
Copyright © 2003 Marcel Dekker, Inc.

FIGURE2.11 Reformedgasboilerwithinternalgasbypasssystem.(Courtesyof
ABCO Industries,Abilene, TX.)
preheat coil, evaporator, superheater, economizer, and air heater. The casing is
refractory-lined, and extended surfaces are used where feasible because the gas
streamisgenerallyclean.Thesteamgeneratedinthereformedgasboilerisoften
combined with the saturated steam generated in the flue gas boiler and then
superheatedinthesuperheaterofthefluegasboiler.Thisisasubstantialquantity
of steam (often referred to as import steam), so the performance of the super-
heatermustbecheckedforcaseswhentheimportsteamquantitydiminishesoris
reduced to zero for various reasons.
Thereformedgasboiler,whichhandlesgasescontainingalargevolumeof
hydrogen andwater athigh pressure,operates athigh heat flux;the heat transfer
coefficient with reformed gases is about 6–8 times higher than those of typical
fluegases from combustion ofnaturalgas; seeQ8.64.Hence theheat flux atthe
inlet to the reformed gas boiler is limited to less than 100,000Btu=ft2h to
minimize concerns about vapor formation over the tubes and possible departure
fromnucleateboilingconditions(DNB).Thegaspropertiesfor typicalreformed
gas and flue gases are listed in Table 8.45 (Chap. 8). The higher thermal
conductivity and specific heat and lower viscosity coupled with higher mass
Copyright © 2003 Marcel Dekker, Inc.

flow per tube leads to higher heat transfer rates and hence higher heat flux in
reformed gas boilers. Note that the heat transfer coefficient is proportional to
specificheat 0:4
thermal conductivity 0:6
viscosity (cid:4)ð Þ
(cid:1) (cid:2)
as discussed in Q8.02.
Generally fire tube boilers are ideal for high gas pressures, though a few
European suppliers have built water tube designs for this application.
GAS TURBINE HRSGs
Gas turbine–based combined cycle and cogeneration plants are springing up
throughout the world. The advantages of gas turbine plants are discussed in
Chapter 1. Though gas turbine exhaust is used to heat industrial heat transfer
fluids and gases, the emphasis here will be on steam generation. Gas turbine
exhaust is clean; therefore water tube boilers with extended surfaces are the
natural choice for heat recovery applications. It is also relevant here to mention
brieflyafewpeculiaraspectsofgasturbineexhaustgasesinorder tounderstand
the design features of HRSGs better.
AsdiscussedinChapter1,gasturbinecombustor temperatureislimitedto
about 2400–2500 F for metallurgical reasons. Therefore a large amount of
(cid:2)
compressed air is used to cool the flame, which in turn increases the exhaust
gas flow from the turbine. After expansion in the turbine, the gas exits at about
1000 F and at a few inches of water column above atmospheric pressure. The
(cid:2)
exhaustgascontainsabout6–10%byvolume(vol%)ofwatervaporandabout14
vol%ofoxygen.Gasturbinesthatareheavilyinjectedwithsteamhaveadifferent
exhaustgasanalysis,whichisdiscussedlater.Thelargeamountofoxygeninthe
exhaustgasesenablesfueltobefiredintheexhaustgaseswithouttheadditionof
air;thehighergasinlettemperaturetotheHRSGinturngeneratesmoresteamin
the HRSG. Because of these large ratio of gas to steam flow compared to steam
generators,HRSGsarehugeincomparison.Forexample,thecrosssectionofan
unfired HRSG generating, say, 100,000lb=h of steam will be about 6 times as
large as that of a packaged boiler generating the same amount of steam.
AnotherimportantaspectofgasturbineHRSGsisthattheexhaustgasflow
remains nearly constant, and increasing the gas inlet temperature through
auxiliary fuel firing increases the steam generation. Unlike in a conventional
steam generator, the ratio of gas to steam flow in an HRSG varies significantly
withsteamgeneration.Thisinturnaffectsthegasandsteamtemperatureprofiles
in the HRSG.
A water–steam mixture boils at a constant temperature at a given steam
pressure; hence the gas temperature distribution across the HRSG surfaces is
influenced by the saturation temperature of steam. Generally, the lower the gas
Copyright © 2003 Marcel Dekker, Inc.

inlet temperature to the HRSG, the lower will be the steam generation and the
highertheexitgastemperature.Thisisduetofactthattheheatsinkintheformof
aneconomizerdoesnothavetheabilitytobringtheexhaustgasstreamtoalower
temperature. In order to cool thegas stream to a reasonably low temperature, on
the order of 250–300 F, multiple-pressure steam generation is usually required.
(cid:2)
Heat recovery stream generators are generally of the water tube type with
extended surfaces. This makes their design compact. Because of the large duty
and low log-mean temperature differences at the various heating surfaces, plain
tubescannotservethepurposeeffectively.TheresultingHRSGdesignwouldbe
huge and uneconomical; the gas pressure drop also would be very high. One
exception is the furnace-fired HRSG, which is very close in design to a
conventional steam generator operating at much higher log-mean temperature
differences; bare tubes may be used in this case. Fire tube boilers are rare in gas
turbine heat recovery applications because they use plain tubes, which makes
them large and unwieldy. They are sometimes used behind small gas turbines,
oftenlessthan3MWinsize,forgeneratinglowpressuresaturatedsteamforuse
in chillers.
HRSGs AND CIRCULATION
Heatrecoverysteamgeneratorsaregenerallycategorizedaccordingtothetypeof
circulation system used, which could be natural, forced, or once-through as
illustratedinFig.2.12.Naturalcirculationunitshaveverticaltubesandhorizontal
gas floworientation, whereas the forced circulation HRSG uses horizontal tubes
and gases flow in the vertical direction. Once-through units can have either a
horizontal or vertical gas flow path. In natural circulation units, the difference in
density between water and steam drives the steam–water mixture through the
evaporator tubes and risers and back to the steam drum. In forced circulation
units, a pump is used to drive the steam–water mixture through the horizontal
evaporator tubes. At the steam drum, steam separates from the steam–water
mixture and dry saturated steam flows through the superheater. In once-through
designs, there is no circulation system. Water enters at one end and leaves as
steam at the other end of the tube bundle.
In Europe, vertical gas flow forced circulation units are common. These
require a circulation pump for maintaining flow through the evaporator tubes. A
recent design in Belgium has natural circulation with vertical gas flow. The
pressure drop through the evaporator tubes is limited by using an adequate
number of streams or parallel paths.
Once-Through Units
A once-through HRSG (called an OTSG) does not have a steam drum like a
natural or forced circulation unit (Fig. 2.12). An OTSG is simply made up of
serpentine coils like an economizer. Because water is converted to steam inside
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.12 HRSGs with different type of circulation systems: (a) Natural
circulation,(b) forced circulation.(c)Once-through.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.12 Continued.
thetubes,thewatershouldhavenearlyzerosolids.Otherwisedepositionofsolids
canoccur insidethetubes tothecomplete evaporation process.Thisinturncan
lead to overheating of the tubes and consequent tube failure, particularly if the
heat flux inside the tubes is high. Like natural or forced circulation units, these
units generate single- or multiple-pressure saturated or superheated steam.
The concept of once-through steam generation is not new. Supercritical
boilersinEuropehavebeenusingonce-throughdesignsforoverhalfacentury.A
once-through unit does not have a defined economizer, evaporator, and super-
heatersection.Thelocationatwhichboilingstartskeepsmovingdependingupon
the gas flow, inlet gas temperature, and duty. The single-point control for the
OTSG is the feedwater control valve; valve actuation depends on predefined
operating conditions that are set through the distributed control system (DCS).
The DCS is connected to a feedforward and feedback control loop, which
monitorsthetransientsinthegasturbineloadandsteamconditions.Ifatransient
in the gas turbine load is monitored, the feedforward control sets the feedwater
flow to a predicted value based on the turbine exhaust temperature, producing
steady-state superheated steam conditions.
Because there is no steam drum, the water holdup is much less than in
drum-typeunits.OftenAlloy800or825tubesareusedtoensuredryrunningand
also to limit the sensitivity to oxygen in the water, avoiding the need for active
chemical treatment. A gas bypass diverter system is not required, because of the
dryoperability.Theuseofhighgradealloytubesminimizesexfoliationconcerns,
which are likely with carbon steel or low grade alloy superheater tubes. When
boilertubesareheated,theyformanoxidelayerinsidethetubes,andwhencooler
steam flows through them the oxide particles are dislodged and carried off to be
deposited inside the steam turbine. This process, called exfoliation, occurs when
the tubes are cycled frequently between hot and cold conditions.
Copyright © 2003 Marcel Dekker, Inc.

Once-throughunitscanalsobestarteduporshutdownveryfastcompared
tonaturalorforcedcirculationboilers,becausetheweightofsteelandholdupof
water are much smaller. On the flip side, the steam pressure decay when the gas
turbinetripsislikelytobefasterthanindesignsthathavemuchlargermetalheat
and a large water inventory. It must be kept in mind that a typical gas turbine
HRSG can generally be started up in 80–100min from cold, so the saving in
start-uptimemaynotbeasignificantissueunlesstheunitisdesignedforfrequent
cycling.Therearealsoafewadvantagesofonce-throughunitssuchasabsenceof
downcomer and riser piping and drum and related material costs and fabrication
concerns. From the heat transfer viewpoint there should not be much of a
differencebetweenonce-throughunitsandthenaturalorforcedcirculationunits;
hence the cross section and size of the HRSG or the areas of various heating
surfaces should all be nearly the same. The flow configuration of the heating
surfaces is generally counterflow except for the evaporator, which could be in
parallel flow as in forced circulation units.
The two-phase steam-side pressure drop in the evaporator tubes is,
however, quite large and could be in the range of a few hundred psi, which is
anoperatingcostandmustbeconsideredinevaluating thedesign.Inthenatural
andforcedcirculationunit,thereisnoadditionalpressurelossassociatedwiththe
evaporatorcircuit,becausethecirculationsystemhandlesthelossesandthestatic
headavailableorthecirculatingpumpbalancesthisloss,consideringotherlosses
associated with the downcomer, evaporator tubes, and riser piping.
Another type of once-through unit is used in oil fields for secondary oil
recoveryoperations(Fig.2.13).Thesegeneratehighpressuresteamrangingfrom
1500 to 3000psig at 80% quality for injection into used oil fields in order to
recover additional oil. The steam pressure depends on the depth at which oil is
available. The hot, wet steam dislodges the viscous layers of oil in the ground
beneath, and thus more oil is recovered. This HRSG is also of once-through
design,withwaterenteringatoneendofthecoilandleavingaswetsteamatthe
FIGURE 2.13 HRSG used inoil fieldapplications.
Copyright © 2003 Marcel Dekker, Inc.

other.Becauseofconcernswithdeparturefromnucleateboiling(DNB),thefinal
portions of the coil are in parallel flow and not in counterflow and are located
behindtubeshavinglowersteamquality.Thisfeaturehelpstolowertheheatflux
inside the tubes where the quality of steam is high. The allowable heat flux to
avoid DNB decreases as the steam quality increases, hence this measure. The
feedwater in these generators is generally of poor quality and has high solids
content,exceedingthousandsofppmofsalts,becausethewateristakenfromthe
fields nearby and basic, inexpensivesoftening methods are used in its treatment.
Becausesodiumsaltsaresolubleinwater,the80%qualitysteam,whichstillhas
20% water, is often adequate to ensure that the salts are disolved and are not
depositedinsidethetubesduringtheevaporationprocess.Single-streamdesigns,
in which a single tube handles the entire steam flow, are used for up to
100,000lb=h capacity, whereas with higher steam flows, multiple streams are
employed.Duetoinstabilityproblemsassociatedwithtwo-phaseboilingoffluids
withmultiplestreams,aflowresistanceattheinlettoeachstreamintheformof
orifices or control valves, as explained in Q7.36, is used. Because water at
ambient temperature is often used as feedwater, a heat exchanger is used to
preheat the incoming water, using the hotter water at the exit of the economizer
portion to minimize acid dew point concerns.
Natural and Forced Circulation HRSGs
Figures 2.12b and 2.12c show the arrangement of natural and forced circulation
HRSGs. In the natural circulation unit the differential head between the cold
water in the downcomer circuit and the hotter, less dense mixture in the riser
tubes drives the steam–water mixture through the evaporator tubes. The circula-
tion ratio (CR), which is discussed in Q7.29, is typically on the order of 8–20
depending on the system, the layout, and the size of downcomers, evaporator
tubes, and risers. The forced circulation units are sized for a particular CR,
typically 3–6. The circulation pumps provide the additional differential head to
ensureflowthroughtheevaporatortubes.Thefollowingaresomeofthefeatures
of these types of HRSGs.
1. Natural circulation units do not require a pump for maintaining
circulation through the evaporator tubes. The circulation is ensured
through natural gravity principles. The use of circulating pumps in
forced circulation units involves an operational and maintenance cost,
andtheirfailureforsomereasonsuchaspoweroutageorpumpfailure
could shut down the HRSG.
2. Thewaterboilsinsideverticaltubesinnaturalcirculationunits,andthe
steam bubbles formed move upward, which is the natural path for
them;hencethetubewallsarecompletelywettedbywater.Asaresult,
tube failures are rare, whereas with horizontal tubes there is a
Copyright © 2003 Marcel Dekker, Inc.

difference in temperature between the top and bottom portions of the
tubes, which could cause thermal fatigue. Also, if the steam–water
mixture velocity is not high enough, the vapor can separate from the
water inside the horizontal tubes, leading to steam blanketing and
possiblyoverheatingthetubes.Thisisapossibilitywhentheheatflux
inside the evaporator tubes is high, for example, in fired conditions,
particularly when a high fin density is used for the evaporator tubes.
3. Natural circulation units can tolerate higher heat flux, generally 50–
80% more than horizontal tube designs due to the vertical configura-
tion of the tubes. Also, in the event of nonuniform gas temperature or
heat flux across the cross section (which is often likely due to
maldistribution of gas flow), the tube receiving the higher heat flux
in a natural circulation unit has a higher circulation ratio or higher
steam–watermixtureflow.Thisisduetothegreaterdifferentialinfluid
densities between the more dense fluid in the downcomer circuit and
the less dense fluid inside the evaporator tubes, which is helpful and
evens out flow imbalances. In a forced circulation unit, all the
evaporator tubes receive the same steam–water flow, irrespective of
their location, unless special efforts are taken to design the orifice in
each tube as in controlled circulation utility boilers. Therefore severe
gas-side flow and temperature maldistributions can lead to the possi-
bility of tube failures or overheating in some tubes.
4. Naturalcirculationunitsrequiremorerealestatethanforcedcirculation
units, because heating surfaces are laid out one behind the other. The
floor space occupied often runs into a few hundred square feet,
particularly with multipressure units with catalysts for NOx and CO
reduction. In forced circulation units the floor space may be small but
the height of the HRSG will be large, requiring a large amount of
supporting structural steel, ladders, and platforms.
5. Duringwarmstarts,thevertical,readilydrainablesuperheater–reheater
arrangement in natural circulation designs eliminates concerns over
condensate carryover and impingement on hot headers and piping,
which would result in thermal stresses at the headers.
6. The horizontal gas flow configuration of natural circulation HRSG
provides an easy way to water wash the highly soluble ammonia
compounds formed downstream of the SCR when operating with a
sulfur-bearing fuel. A major deficiency of forced circulation or once-
through units with their vertical gas path arrangement is the lack of a
procedure to water wash deposits from heat transfer surfaces down-
stream of the SCR without damage to the SCR catalysts.
7. During start-up and low load periods, steam bubbles generated in the
economizer section have to flow down in the counterflow direction in
Copyright © 2003 Marcel Dekker, Inc.

once-through and forced circulation units, which is not their natural
path. To overcome steaming concerns, the feedwater control is some-
times located between the economizer and the evaporator. This
increases the design pressure of the economizer. A safety valve is
also required at the economizer.
8. Thecasingdesignforforcedcirculationunitsistypically‘‘hot,’’thatis,
it is insulated on the outside. Hence the designer is required to use
alloysteelmaterialforthecasing,andonehastoevaluatetheimpactof
thermal expansion.
Despite their differences and the pros and cons, all three types of HRSGs
are used throughout theworld. Selection is generally based on the experience of
the plant managers, their consultants, and the end users.
INCINERATION APPLICATIONS
In chemical and industrial plants, several by-products are generated in solid,
liquid, and gaseous forms that have to be safely destroyed to prevent potential
environmental damage. These by-products come from petroleum refining and
petrochemical, pharmaceutical, paper and pulp, and plastics production. Small
quantitiesofby-productsarestoredindrumsandplacedinlandfills,butthemost
effective method of rapidly destroying a high percentage of hydrocarbon
contaminants is to oxidize the organic materials at elevated temperatures
(1500–1800 C). For some vapor streams, effective destruction of contaminants
(cid:2)
canbeachievedatlowertemperatures.Thecarbonandhydrogeninthewasteare
convertedtoCO andH O.Ifthegasstreamcontainssulfurorchlorineorsimilar
2 2
substancestheymustberecoveredorremovedbeforeventingthefluegasestothe
atmosphere according to local air quality regulations. Particulates are also
generated that have to be removed.
The process of thermal oxidation of fumes, liquids, and gaseous wastes is
often carried out in thermal oxidizers or incinerators. If the waste stream has a
lowheatingvalueorlowconcentration,oftennaturalgasorliquidfuelsarefired
alongside to improve the combustion process. In order to destroy most of the
pollutants, incineration is carried out at temperatures ranging from 1500 to
1800 F with proper residence times, typically 1–2s. The exhaust gas stream
(cid:2)
contains a significant amount of energy and is recoveredin the form of steam in
waste heat boilers.
If the gas stream is greater than 100,000lb=h and clean, then awater tube
boilerwithextendedsurfacesistheidealchoice.Firetubeboilersarealsousedin
incineration plants if the gas is not likely to cause slagging. A superheater and
economizermayalsobeusedinfiretubeboilersasshowninFig.2.2.Becauseof
Copyright © 2003 Marcel Dekker, Inc.

the high gas temperature at the inlet to the boiler, 1500–2000 F, the superheater
(cid:2)
is often located downstream of the boiler as shown. The superheater steam
temperature cannot be very high, obviously, with such an arrangement; it is
typically 500–550 F depending on the steam pressure. The disadvantage of the
(cid:2)
firetubedesignisthatitisdifficulttohavetwofiretubeboilerswithasuperheater
in between such as can be done with water tube designs. Hence we have to live
withasteamtemperaturethatisslightlylowerthanthosefeasiblewithwatertube
designs.Locatingthesuperheateratthegasinletcanleadtocorrosionduetothe
presence of corrosive gases in the gas stream.
Bare and finned tubes are used in the design of water tube boilers,
depending upon the cleanliness of the gas, its fouling tendencies, and the gas
temperature.Simpletwo-drumdesigns,suchasthoseshowninChapter8inFig.
8.3, in which the steam drum and mud drum are connected by plain or finned
tubes rolled into the steam and mud drums, are common. This design can have
eitherarefractory-linedcasingorawater-cooledcasing.Withtherefractory-lined
design, casing corrosion is a possibility if thegas stream contains corrosiveacid
vapors that can seep through the refractory. Access doors or lanes can be easily
incorporated into this design. The water-cooled casing operates at the saturation
temperatureofsteam andensuresthat corrosionconcernsareminimal. The two-
drum crossflow design is suitable for small capacities, generally about 50,000–
75,000lb=h of steam. When the amount of steam generated is much greater say
above100,000lb=h,anelevatedsteamdrumwithexternaldowncomersandrisers
may be justified. The steam drum should havethevolumeor holdup to handle a
few minutes of residence time from normal level to empty. Some plants require
this residence time to be 3–4min, and a few plants require 10–12min. In large
plants, multiple evaporators are connected to a common steam drum and
circulation system.
Figure 2.3 shows a water tube boiler consisting of a screen section,
followedbyatwo-stagesuperheaterwithinterstageattemperation,anevaporator,
and an economizer that is used in large incineration projects handling clean
effluents.Thescreensectionissimilartotheshieldsectionusedinafiredheater
andprotectsthesuperheaterfromthehotgasesandfromexternalradiationfrom
theincineratorflame.Aminimumoffourrowsarerequiredtoabsorbtheexternal
radiationfromthecavityorflame,asdiscussedinQ8.09.Theevaporatorandthe
screen sections are in parallel and are connected to the same steam drum by
external downcomers and risers. If the gas enters at a temperature in excess of
1500 F,thescreensectionisoftendesignedwithbaretubes.Thesuperheatermay
(cid:2)
or may not have fins, depending on the steam and tube wall temperatures. The
evaporator has finned surfaces, which canvary from a low fin density section at
theinlet(twofinsperinch)toahighfindensitysection(fourtofivefinsperinch)
as the gas is cooled. This is done to minimize the heat flux inside the tubes and
also to minimize fin tip temperatures.
Copyright © 2003 Marcel Dekker, Inc.

Theeconomizerusesafindensityoffourtosixfinsperinch.Thetubesof
all the sections are generally vertical with horizontal gas flow, as in gas turbine
HRSG plants. Superheaters are of T11, T22, or T91 material if the tube wall
temperatures are close to 1000–1100 F.
(cid:2)
In plantswith large steam requirements, energy from thewastegas stream
is augmented by firing natural gas or fuel oil. In these designs, a D-type boiler
(Fig. 2.14) is an ideal choice. The burner is fitted at the front wall of the boiler
and fires into awater-cooled furnace; thewastegas stream enters the convection
bank, mixes with the furnace flue gases, then flows through the convection and
economizersections.Asuperheatercanbelocatedintheconvectionbankbehind
screen tubes. If the flue gases are clean, extended surfaces may be used in the
cooler sections of the convection bank.
Various modes of operation have to be considered in these boilers,
particularly if a superheater is used. If the waste gas stream supply is cut off,
the steam generation is reduced. Hence the total steam flow is reduced which
affectsthesteamtemperatureandthesuperheatertubewalltemperatures.Insome
casesonlythewastegasstreamisused,andinsomeothermodesonlytheburner
isfiredforgeneratingsteam.Allthesedifferentcasesgeneratedifferentquantities
ofsteamandfluegasesatdifferenttemperaturesthatentertheconvectionsection;
hence the superheater performance has to be evaluated carefully in all these
modes. The furnace pressure is maintained at nearly zero, and an induced draft
fan handles the flowof the flue gases from the burner and thewaste gas stream.
The forced draft fan just handles the combustion air to the burner.
Figure 2.15 is the schematic of a waste heat boiler for a dirty gas from a
carbon black incineration system. A D-type boiler was also used for this
application. The hot gas coming in at about 2100 F is cooled in the furnace
(cid:2)
and then enters the convection bank. A screen section with widely spaced bare
tubes helps to minimize slagging concerns with ash particulates that have low
melting temperatures. A retractable blower also helps to clean the front end. As
the gas cools, the tube spacing can be closer.
Slagging is a serious concern when flue gases containing ash particulates
with lowmelting point salts areused inheatrecoveryapplications. The slag is a
rocklike deposit that forms on cool surfaces such as tubes and solidifies as soon
as it is formed. Retractable blowers can help minimize this problem but cannot
eliminateitcompletely.Thewidetubespacingensuresthattubesarenotbridged
bythemoltenmassofdeposits,thuspreventingtheflowofgases.Ashparticles,if
any, are collected in hoppers located beneath the convection bank.
FOULING IN WASTE HEAT BOILERS
Fouling isa serious concern inboth firetube andwater tube boilers, particularly
with dirty gas streams. It affects not only the waste heat boiler performance but
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.14 D-type waste heat boiler for operation with burner and waste heat. (Courtesy of ABCO
Industries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.15 Waste heat boiler in carbon black plant. (Courtesy of ABCO
Industries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

alsoequipmentsuchasscrubbersdownstreamoftheboiler.Whenfoulingsetsin,
thesteam generationdecreasesandthegaspressuredropincreasesoveraperiod
of time. There are a few ways to infer if the fouling has become severe:
1. Theexitgastemperaturefromtheboilerwillincreaseoveraperiodof
time;if,say,thenormalexitgastemperaturefromtheconvectionbank
is 550 F and we observe 570–600 F for the same load, then we can
(cid:2) (cid:2)
inferthatfoulinghassetin.Foulingdepositsbuildupoverheattransfer
surfaces (whether inside or outside), and the fouling factor increases
exponentially and then tapersoff asshowninFig.2.16. With periodic
cleaningsomeofthedepositsareremoved,whichdecreasesthefouling
factor,butabaselayerbuildsupandincreasestheexitgastemperature
anddecreasestheboilerduty.Acompleteshutdownandcleaningmay
help restore the original boiler performance or close to it.
2. The gas pressure drop across the convection section increases. If the
fan power consumption increases over a period of time, then one can
inferthatthereissomeblockageofthegaspathandthatfoulinghasset
in.
3. Steam generation naturally decreases with fouling.
4. Superheated steam temperature, if a superheater is present, has to be
looked at carefully, because fouling in different sections may be
different, and one cannot conclude that there is fouling at a given
surfacewithout having data on thegas inletand exittemperatures and
steam inlet and exit temperatures and flows. Sometimes steam-side
foulingiscausedbydepositionofsaltsfromsteam.Steam-sidefouling
can increase the tube wall temperatures and cause overheating as
discussed in Q8.13. Steam-side fouling is more critical in finned
water tube boilers, as discussed in Q8.24.
One has to shut down the boiler and perform an investigation iffouling is
severe.Normalfoulingmaybeacceptablebetweenmaintenanceshutdowns.Heat
transfer calculations backed up with field data and tube wall temperature
FIGURE 2.16 Foulingin waste heatboilersversustime.
Copyright © 2003 Marcel Dekker, Inc.

measurements can also show if the fouling is on the gas side or steam side or
both.Withgas-sidefoulingthetubewalltemperatureswillnotincrease,whereas
with steam-side fouling the tube wall temperatures can increase significantly.
Withacombinationofgas-andsteam-sidefouling,themeasurementofoperating
data on each side, followed by elaborate calculations, can reveal the extent of
fouling.
Because both fire tube and water tube boilers are used in HRSGs, a few
guidelines on their sizing are in order.
FIRE TUBE BOILER DESIGN CONSIDERATIONS
ThesizingproceduresforfiretubeboilersarediscussedinQ8.10.Itmaybenoted
that the tube size plays a significant role in minimizing the length of the boiler.
Withsmallgasflows,onemayconsidermulti-gas-passdesign,whichcanreduce
theoveralllength.Tubesizesvaryfrom1.5to2.5in.OD;smallertubesgenerally
have lower tube wall temperatures and also require less surface area and shorter
tube length.Henceacomparisonofsurfaceareasoftwoor moredesignsshould
bemadewithcaution.Heatfluxesarequitelowinfiretubeboilersowingtolow
gas-side heat transfer coefficients, an exception being gas streams in hydrogen
plants, as discussed earlier. SA 178a carbon steel tubes are typically used for
evaporators handling common flue gases. In reformed gas applications, T11 or
T22 tubes are preferred. Gas pressure drop can range from 3 to 6in. WC in flue
gasheatrecoveryboilersandabout1psiinhighgaspressureapplicationssuchas
reformed gas boilers.
BoilercirculationmaybecheckedusingmethodsdiscussedinQ7.32.With
poor water quality, fouling and scale formation are of concern, and tube wall
temperatures can increase significantly with scale thickness as discussed in
Q8.13.
Elevatedsteam drumdesign isgenerally used ifthesteam purity hasto be
less than 1ppm. External downcomers and risers help cool the tubes and tube
sheet by circulating the water–steam mixture over them. If the flue gas
temperature is below 1500 F, then an elevated drum design may be dispensed
(cid:2)
with and a single-shell fire tube boiler may be used. The steam purity without
internals is low, on the order of 5–15ppm, which may be adequate for low
pressure process heating applications.
Owing to the large inventory of water, fire tube boilers respond slowly to
load changes compared with water tube units. However, the pressure decay on
loss of heat input will also be smaller.
WATER TUBE BOILER DESIGN CONSIDERATIONS
Thedesignprocedureforwasteheatboilersisquiteinvolved.Withagivensetof
inletgasconditionssuchasflowandtemperature,wehavetoseehowthevarious
Copyright © 2003 Marcel Dekker, Inc.

heatingsurfacesrespond.Thesurfacescouldconsistofbareorfinnedtubes.The
superheater could have one or more stages; a screen section may or may not be
used. Import steam could come from another boiler to be superheated in the
boiler in question, or saturated steam may be drawn off the steam drum for
deaeration or process purposes. The feedwater temperature or steam pressure
could vary depending on plant facilities.
Before attempting to evaluate the performance of a complete waste heat
boiler, one must first know how to obtain the performance of individual
components such as the superheater, evaporator, and economizer by using the
number of transfer units (NTU) method or through trial and error. This is
discussed in Q8.29 and Q8.30. Once we know how to evaluate the performance
of each surface, evaluating the overall performance of a waste heat boiler is
simple.Figure2.17showsthelogicforasimplewasteheatboilerconsistingofa
superheater, evaporator, and economizer. A few iterations may be required,
because we have to first assume a steam flow and completely solve all the
other sections and then check on whether the assumed steam flow was fine. A
FIGURE 2.17 Logicused forevaluating HRSG performance.
Copyright © 2003 Marcel Dekker, Inc.

computer program is required, because these calculations become tedious with
two-stage superheaters with attemperation, a combination of bare and finned
tubes in evaporators, and the use of import or export steam, to mention a few
variables.Alsotheincineratormayoperateatdifferentcombinationsofgasflows,
temperatures, and gas analysis. The performance has to be checked at different
operating points before finalizing it.
Figure 2.18showstheprintout ofresultsforawater tubewaste heatboiler
foragasturbineexhaustconsistingofafurnacesection, ascreensection, atwo-
stagesuperheater,anevaporatorconsistingofbareandfinnedtubes,andafinned
tube economizer. In the unfired mode this HRSG makes about 45,000lb=h of
steam.TheturbineexhaustenterstheHRSGat980 F,whichisraisedto2175 F
(cid:2) (cid:2)
by the burner located at the HRSG inlet to generate 150,000lb=h of steam at
620psig and 750 F. The oxygen content has decreased from 15% to 8.39% by
(cid:2)
volume and the burner duty is 123MM Btu=h on LHV basis. The gas
temperature drops to 2063 F in the furnace section and is cooled to 1852 F in
(cid:2) (cid:2)
the screen section before entering the superheater. The gas pressure drop in the
HRSG is about 6in. WC. To this must be added the burner, selective catalytic
reduction (SCR), and duct losses. The printout also shows the tube wall
temperatures, fin tip temperatures, heat transfer coefficients at various sections
both inside and outside the tubes, and the gas- and steam=water-side pressure
drops. The amount of spray water used for attemperation is also computed.
Several variables can be changed to check the effect on performance. The
evaporator uses different fin configurations. This is done to minimize the heat
flux inside the evaporator tubes and also the tube wall and fin tip temperatures.
The boiler duty is 177MM Btu=h. The fuel used is typically natural gas.
Boilertubesizestypicallyrangefrom1.5to2.5in.andfindensitycanvary
from2to6fins=in.dependinguponthedesign.Baretubeboilersareusedindirty
gas applications. Sometimes multipass designs offer a compact design. Whereas
with finned tubes, both in-line and staggered arrangements are used, an in-line
arrangement is generally used with bare tubes because it is inefficient to use a
staggeredarrangement,as discussed inQ8.22. Tube spacing canvary depending
on gas velocity, dirtiness of the gas stream, and heat transfer considerations. A
radiant furnace is also used if the incoming gas is at a high temperature and has
the potential to cause slagging problems. Superheaters can be of bare tube or
finned tube design, depending upon the gas temperature and cleanliness.
Generally a low fin density is preferred for superheaters owing to the low heat
transfer coefficient inside tubes, as discussed in Q8.22 and Q8.27. Superheater
tubes can be vertical or horizontal depending on size or layout considerations.
Economizersareofbaretubedesignindirtygasapplicationsandusefinnedtubes
in clean gas applications. In sulfuric acid plants, a few suppliers use cast iron
gilled tubes.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 2.18 Printoutof HRSG performance.
Copyright © 2003 Marcel Dekker, Inc.

PREDICTING HRSG DESIGN AND OFF-DESIGN
PERFORMANCE USING HRSG SIMULATION
It is possible to predict the performance of water tube HRSGs in clean gas
applications by using a simulation process instead of physically designing the
unit. Thus anyone familiar with heat balances such as consultants and those
planning cogeneration or combined cycle plants can obtain a good idea of the
performance of the HRSG under various modes of operation. This information
may be used to arrive at the HRSG configuration and optimize the major
parameters for the steam system. Several ‘‘what if’’ scenarios may be looked
at. The performance of an existing HRSG may also be evaluated to see if its
performance is reasonable, as discussed in Q8.45. Though simulation may be
used for any clean gas convective type of HRSG, it is particularly useful in gas
turbine applications, because the HRSG designs involving multiple-pressure,
multiple-module designs are more complex as discussed in Chapter 1.
Because of the large amount of exhaust gases and the low inlet gas
temperature of an HRSG, one cannot arbitrarily assume an exit gas temperature
and compute the steam generation. The problem of evaluating steam generation
and temperature profiles gets complicated further as it is not often possible to
recover a substantial amount of energy from the exhaust gases with steam at a
single pressure level. Multiple-pressure steam generation with split modules
alonecanoptimizeenergyrecovery,makesthetaskofperformingenergybalance
calculations very tedious. Gas and steam temperature profiles and hence energy
balance in an HRSG aregoverned by whatare called pinch and approach points
(Fig. 2.17) Q8.34 and Q8.37 explain this in greater detail.
Basically,we estimatetheterm UA,the product oftheoverallheat transfer
coefficientandthesurfacearea, foreach heating surface inthe designmode and
then correct it for the effect of gas flow, temperature, and analysis. Using this
corrected UA, one can use the NTU method to evaluate the performance of any
exchanger and then the overall performance.
The HRSGS Program
Ihavedevelopedasimulation programcalledHRSGStoperformthesecomplex
design and off-design performance calculations. Basically the desired HRSG
configuration is built up by using the six basic modules shown in Fig. 2.19. By
using the common economizer or common superheater concept, one can config-
ure complex multiple-pressure HRSGs, as shown in the examples in the figure.
Up to 10 modules or nine pressure levels can be evaluated. The program
automatically arrives at the firing temperature and the fuel requirement if the
desired steam quantity isknownwith bothturbineexhaustand fresh air cases. It
checks for steaming in the economizer and handles import or export steam from
evaporators as illustrated by a fewexamples in Chapter 1 (See p. 26 and 36). It
Copyright © 2003 Marcel Dekker, Inc.

FIGURE2.19 HowbasicmodulesmaybecombinedtoarriveatcomplexHRSGconfigurations.
Copyright © 2003 Marcel Dekker, Inc.

computes the ASME efficiency and prints out the US values for each surface in
the design and off-design modes as shown in several examples in Chap. 1.
The simulation program is generally used for convective-type HRSGs and
waste heat boilers, which operate on clean gas streams. If a radiant furnace is
used, there will be some variation between the actual and predicted values.
Because of the large fouling factors involved in dirty gas applications, the heat
transfer coefficients cannot be corrected for off-design conditions accurately;
hence there will be some deviation between predicted and actual performance if
thisisusedin,say,municipalwasteapplications.Formoreinformationaboutthe
program, please contact the author at v_ganapathy@yahoo.com or visit the web
site http://vganapathy.tripod.com/boilers.html.
SPECIFYING WASTE HEAT BOILERS
Thefollowingpointsmaybeconsideredwhiledevelopingspecificationsforheat
recovery applications.
1. Becausetherearenumerousapplicationsofheatrecovery,itisalways
good practice to start off the specifications by describing the process
that generates the fluegases, because that givesan idea of the nature
ofthegasstream.Withacleangasstream,finnedtubescouldbeused
tomaketheboilerdesigncompact,whereasadirtygaswithslagging
potential must have bare tubes, with provision for cleaning the
surfaces.Processgasapplicationssuchashydrogenplantsorsulfuric
acid plant boilers require exit gas temperature control systems.
2. Desired steam purity should be mentioned, particularly if the steam
generated is used in a gas or steam turbine. Also, based on load
swings, one could arrive at the proper size for the steam drum.
3. The extent of optimization required and the cost of fuel, electricity,
and steam should be indicated. For example, simply stating the inlet
gas conditions and steam parameters may not be adequate. If design
Acoolsthegasto,say,450 FanddesignBcoolsitto,say,400 Fby
(cid:2) (cid:2)
usingalargerboilerathighercost,howisthistobeevaluated?Also,
if for the same steam parameters, one design has 6in. WC pressure
dropandanotherhas4in.WC,isthereanywaytoevaluateoperating
costs? Such an indication in the specifications will help the designer
to review the design and balance the installed and operating costs.
4. Space availability and layout considerations should be indicated.
Sometimes a boiler is built before the builder finds out that it has
to be located inside a building that has already been constructed.
5. Thesteamsystemshouldbeclearlydescribed.Oftenonlythemakeup
waterconditionsaregivenwithoutanindicationofwherethesteamto
Copyright © 2003 Marcel Dekker, Inc.

thedeaeratorcomesfrom.Ifthesteam istakenfromtheboiler itself,
thenthedesignislikelytobeaffected,particularlyifasuperheateris
present. Hence a scheme showing the complete steam–water system
for theplant will be helpful. In waste heat boilers, sometimes import
steam from another source is superheated in the boiler. This affects
thesuperheater and boiler performance, particularly whenthe import
steam supply is reduced or cut off.
6. Often feedwater is used for desuperheating steam to control its
temperature.Thiswatershouldhavezerosolidsandshouldpreferably
bedemineralized. Softenedwater willaddsolidstothesteam ifused
directly as spray, so one may have problems with solid deposits,
fouling,andoverheatingofsuperheatertubesandpossibledeposition
of solids in the steam turbine blades. If demineralized water is not
available and that is so stated up front, the designer could come up
with a sweet water condensing system to obtain the desired spray
water for steam temperature control (see Chap. 3). The feedwater
analysis is also important because it affects blowdown rates.
7. Gas flow should be stated in mass units. Often volumetric units are
given and the writer of the specifications has no idea if it is actual
cubicfeet per minuteorstandardcubic feetper minute;then without
thegasanalysis,itisdifficulttoevaluatethedensityorthemassflow.
The ratio between standard and actual cubic feet per minute of flue
gascouldbenearly4dependingonthegastemperature.Theproblem
is resolved if the flue gas mass flow is given in pounds per hour or
kilograms per hour.
8. Flue gas analysis is important. We have seen that the presence of
water vapor or hydrogen in flue gases increases the heat transfer
coefficient and also affects the specific heat and temperature profiles
ofthegas.Thepresenceofcorrosivegasessuchashydrogenchloride,
sulfurtrioxide,andchlorinesuggeststhepossibilityofcorrosion.The
boilerdutyforthesamegastemperaturedropandmassflowcouldbe
different if one designer assumes a particular flue gas analysis and
another designer assumes another. Hence flue gas analysis should be
stated as well as the gas pressure. High gas pressure, on the order of
even 1–2psi, affects the casing design and cost.
9. With HRSGs, one should perform a temperature profile analysis
before arriving at the steam generation values. As shown in Q8.36,
assuming an exit gas temperature and computing HRSG duty or
steam generation on that basis can lead to errors.
10. EmissionlevelsofNOx;CO,andother pollutantsrequiredattheexit
of the HRSG or waste heat boiler should be stated. In such cases,
informationonpollutantsintheincominggasesshouldalsobegiven.
Copyright © 2003 Marcel Dekker, Inc.

11. FuelanalysisshouldbeprovidedforafiredHRSGorboiler.Also,the
costoffuelhelpstodetermineifadesigncanbeoptimizedbyusinga
larger boiler and smaller fuel consumption or vice versa.
12. Iftheboilerislikelytooperateforashortperiodonlyorweeklyoris
being cycled, then this information should also be given. Frequent
cycling requires some considerations in the design to minimize
fatigue stresses. Provisions for keeping the boiler warm during shut-
down may also be necessary.
In addition, local code requirements, site ambient conditions, and constructional
features, if any, should be mentioned.
REFERENCES
1. V Ganapathy. Simulation aids cogeneration system analysis. Chemical Engineering
Progress,October1993.
2. VGanapathy.Evaluatinggasturbineheatrecoveryboilers.ChemicalEngineering,Dec
7,1987.
3. VGanapathy.Evaluatingwasteheatboilersystems.PlantEngineering,Nov22,1990.
4. V Ganapathy. HRSG features and applications. Heating, Piping, Air-Conditioning,
January1989.
5. VGanapathy.SimplifyHRSGevaluation.HydrocarbonProcessing,March1990.
6. VGanapathy.Fouling—thesilentheattransferthief.HydrocarbonProcessing,October
1992.
Copyright © 2003 Marcel Dekker, Inc.

3
Steam Generators
INTRODUCTION
Steamgenerators,orboilersastheyareoftencalled,formanessentialpartofany
power plant or cogeneration system. The steam-based Rankine cycle has been
synonymouswithpowergenerationforcenturies.Thoughsteamparameterssuch
as pressure and temperature havebeen steadily increasing during the last several
decades,thefunctionoftheboilerremainsthesame,namely,togeneratesteamat
the desired conditions efficiently and with low operating costs. Low pressure
steamisusedincogenerationplantsforheatingorprocessapplications,andhigh
pressure superheated steam is used for generating power via steam turbines.
Steam is used in a variety of ways in process industries, so boilers form an
important part ofthe plant utilities. In addition toefficiencyand operatingcosts,
another factor that has introduced several changes in the design of boilers and
associated systems is the stringent emission regulations in various parts of the
world.AsdiscussedinChapter5,thelimitsonemissionsofNOx;CO;SOx,and
particulateshaveimpactedthedesignandfeaturesofsteamgeneratorsandsteam
plants,nottomentiontheircosts.Today’scogenerationsystemsandpowerplants
resemble chemical plants with NOx; SOx, and particulate control systems
forming a major portion of the plant equipment. Oil- and gas-fired packaged
boilers used in cogeneration and combined cycle plants have also undergone
significant changes during the last few decades. Selective catalytic reduction
Copyright © 2003 Marcel Dekker, Inc.

systems (SCRs) are used even in packaged boilers for NOx control, adding to
their complexity and costs.
Steam pressure and temperature ratings of large utility boilers have been
increasinginordertoimproveoverallplantefficiency.Severalsupercriticalplants
have been built during the last decade. There have been improvements in the
design of packaged boilers too. Figure 3.1 shows the general arrangement of a
packaged steam generator. The standard refractory-lined packaged boilers of the
last century are being slowly replaced by custom-designed boilers with comple-
telywater-cooledfurnaces(Fig.3.2).Theairheaterthatwasonceanintegralpart
of oil- and gas-fired boilers is now replaced by the economizer, which helps to
FIGURE 3.1 Package water tube boiler. (Courtesy of ABCO Industries, Abilene,
TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE3.2 Completelywater-cooledfurnacedesign.(CourtesyofABCOIndus-
tries,Abilene, TX.)
lower NOx levels. To improve efficiency, a few plants are even considering the
use of condensing economizers.
Though pulverized coal–fired boilers form the backbone of utility plants,
fluidizedbedboilersarefindingincreasingapplicationwhenitcomestohandling
solid fuels with varying moisture, ash, and heating values; they also generate
lower emissions of NOx and SOx. Oil- and gas-fired fire tube boilers (Fig. 3.3)
are widely used in small process plants for generating low pressure saturated
steam. Though different types of boilers are mentioned in this chapter, the
emphasisisontheoil-andgas-firedpackagedwatertubesteamgenerator,which
isfastbecomingacommonsightineverycogenerationandcombinedcycleplant.
BOILER CLASSIFICATION
Thetermsboilerandsteamgeneratorareoftenusedinthesamecontext.Boilers
may be classified into several categories as follows:
By Application: Utility, marine, or industrial boiler. Utility boilers are the
largesteamgeneratorsusedinpowerplantsgenerating500–1000MWof
Copyright © 2003 Marcel Dekker, Inc.

FIGURE3.3a Firetubeboiler—wetback design.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.3b Firetubeboiler—dryback design.
Copyright © 2003 Marcel Dekker, Inc.

electricity.Theyaregenerallyfiredwithpulverizedcoal,thoughfluidized
bed boilers are popping up in some plants. Utility boilers generate high
pressure, high temperature superheated and reheat steam; typical para-
meters are 2400psig, 1000=1000 F. A few utility boilers generate
(cid:2)
supercritical steam at pressures in excess of 3500psig, 1100=1100=
1100 F. Double reheat cycles are also in operation. Industrial boilers
(cid:2)
used in cogeneration plants generate low pressure steam at 150psig to
superheated steam at 1500psig at temperatures ranging from 700 to
1000 F.
(cid:2)
By Pressure: Low to medium pressure, high pressure, and supercritical
pressure.Processplantsneedlowtomediumpressuresteamintherange
of 150–1500psig, which is generated by field-erected or packaged
boilers, whereas large utility boilers generate high pressure (above
2000psig) and supercritical pressure steam.
By Circulation Method: Natural, controlled, once-through, or combined
circulation. Figure 3.4 illustrates these concepts. Natural circulation is
widely used for up to 2400psig steam pressure. There is no operating
costincurredforensuringcirculationthroughthefurnacetubes,because
gravityaidsthecirculationprocess.Controlledandcombinedcirculation
boilers use pumps to ensure circulation of a steam–water mixture
through the evaporator tubes. Supercritical boilers are of the once-
through type. It may be noted that once-through designs can be
employed at any pressure, whereas supercritical pressure boilers must
be of a once-through design.
By Firing Method: Stoker, cyclone furnace, fluidized bed, register burner,
fixed or moving grate.
By Construction: Field-erected or shop-assembled. Large industrial and
utility boilers are field-erected, whereas small packaged fire tube boilers
upto90,000lb=hcapacityandwatertubeboilersupto250,000lb=hare
generally assembled in the shop. Depending on shipping dimensions,
these capacities could vary slightly.
BySlagRemovalMethod:Dryorwetbottom,applicabletosolid-fuel-fired
boilers.
By Heat Source and Fuel: Solid, gaseous, or liquid fuels, waste fuel or
waste heat. Waste heat boilers are discussed in Chapter 2. The type of
fuel usedhasasignificantimpactonboiler size.Forexample,coal-fired
boiler furnaces are large, because a long residence time is required for
coal combustion, whereas oil- and gas-fired boilers can be smaller, as
shown in Fig. 3.5.
According to Whether Steam is Generated Inside or Outside the Boiler
Tubes: Fire tube boilers (Fig. 3.3), in which steam is generated outside
the tubes, are used in small plants up to a capacityof about 60,000lb=h
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.4 Boiler circulation methods. (a) Natural; (b) forced circulation; (c)
once-through; (d) once-through with superimposed circulation. 1, Economizer; 2,
furnace; 3,superheater;4, drum;5, orifice;6,circulating pumps;7, separator.
FIGURE 3.5 Theimpact offuelon furnacesize.
Copyright © 2003 Marcel Dekker, Inc.

of saturated steam at 300psig or less; they typically fire oil or gaseous
fuels. Water tube boilers, in which steam is generated inside the tubes,
can burn any fuel, be of any size, and operate at any pressure but are
generally economical above 50,000lb=h capacity. See Chap. 2 for a
comparison between fire tube and water tube waste heat boilers.
STEAM PRESSURE AND BOILER DESIGN
The energy absorbed by steam is distributed among feedwater heating (sensible
heat),boiling(latentheat),superheating,andreheatingfunctions.Thedistribution
ratios areafunctionofsteam pressure, ascanbeseenfromsteam tablesorfrom
Fig. 3.6. If the latent heat is large as in low pressure steam, a large furnace is
requiredfor theboiler; asthe pressure ofsteam increases, thelatentheat portion
decreases and the superheat and reheat energy absorption increases. The boiler
design accordingly varies with large surface areas required for the superheaters
and reheaters and a small furnacewith little or no convective evaporator surface
inparticular.Thesensibleheat,whichisabsorbedintheeconomizer,isalsohigh
at high pressure. The distribution of energy among the various surfaces—the
furnace,evaporator,superheater,reheater,andeconomizer—issomewhatflexible,
as will be shown later, but it must be emphasized that steam pressure plays a
significant role in determining the sizes of these surfaces.
FIGURE 3.6 Distribution ofenergy in boilersasafunction ofsteam pressure.
Copyright © 2003 Marcel Dekker, Inc.

Innaturalcirculationunitsthedensitydifferentialbetweenthecoolerwater
in the downcomers and the less dense steam–water mixture in the riser tubes of
the furnace provides the hydraulic head for circulation of the steam–water
mixture through the evaporator tubes. The circulation ratio, CR, which is the
ratio of the mixture flow to steam flow, could be in the range of 6–8 in high
pressure boilers. In packaged boilers operating at low steam pressure, say 150–
1000psig, the CR could be higher, ranging from 10 to 20. Note that we are
referring to an average value. The circulation ratio will differ for each parallel
circuit, depending on itslength,tube size, heat flux,and static head available,as
discussed in Q7.29. The controlled circulation boiler is operated at a slightly
higher steam pressure, around 2500–2600psig, and flow is ensured through the
furnace tubes by a circulating pump; which forces the boiler water through each
circuit.Thecirculationratioispreselectedintherangeofabout2–4.Thisisdone
to reduce the operating cost associated with the circulating pumps; also, the use
ofcarefullyselectedorificesensurestheflowofthesteam–watermixturethrough
each circuit. Hence a low CR is used in these systems. The once-through unit
with superimposed circulation requires the circulating pump during start-up and
at low loads when flow through the circuits is not high and later switches to the
once-through mode at higher loads.
PACKAGED STEAM GENERATORS
Packaged boilers are widely used in cogeneration and even in combined cycle
plants as auxiliary boilers providing steam for turbine sealing and steam for
other uses when the gas turbine trips and the HRSG is not in operation.
These boilers are generally shop-assembled and custom-designed. Typically,
boilers of up to 250,000lb=h capacity can be shop-assembled and larger units
are field-erected. Steam parameters vary from 150psig saturated to 1500psig,
1000 F. They typically burn natural gas, distillate fuel oils, and even heavy
(cid:2)
residual oils. Widely used methods for NOx control are low-NOx burners, flue
gas recirculation, and selective catalytic reduction systems (SCRs). Carbon
monoxide catalysts are also used if required. Emission control methods are
discussed in Chapter 4.
Packaged boilers could be further classified as D, A, or O-type depending
ontheirconstruction,asshowninFig.3.7.IntheA-andO-typeboilers,theflue
gasesexitthefurnaceandthenmakea180 turn,splitupintotwoparallelpaths,
(cid:2)
and flow through the convection section, then recombine to flow through the
economizer. Using a convective superheater in this type of boiler is tricky,
because ithastobesplit intotwohalves.Aradiantdesignmaybelocated atthe
furnace exit, but it operates in a harsh environment as discussed later.
D-type boilers arewidely used in industry. The fluegases generated in the
furnace travel though the furnace, make a turn, and go through the convection
Copyright © 2003 Marcel Dekker, Inc.

FIGURE3.7 A-, D-,and O-typeboilerconfigurations. 1,Burner; 2, steamdrum;3, muddrum.
Copyright © 2003 Marcel Dekker, Inc.

bankandthenthroughtheeconomizer tothestack.Thegasflowisnotsplitinto
two parallel paths as in the A- or O-type designs. If a superheater has to be
locatedintheconvectionbank,theD-typedesignisthemostconvenient,because
thereisnoconcernwithmaldistributioningasflowbetweenparallelpathsaswith
the O- and A-type boilers, which may lead to thermal performance issues.
However, the O- and A-type boilers are more suitable as mobile units, because
theyhavebalancedweightdistribution;rentalboilers,whichmovefromlocation
to location, are generally of A- and O-type designs.
The gas-fired O-type boiler shown in Fig. 3.8 is another variation of
packaged boiler design. In this boiler the flue gases do not make a turn at the
furnace end; the gases flow straight beyond the furnace to a convection section
consistingofbareandfinnedtubes;thefinnedtubesmaketheconvectionsection
compact, thus reducing the overall length of the boiler. The advantage of this
design is that the width required is not large, because the width of the furnace
determines the width of the unit, whereas in a typical O- or A-type boiler the
widthofthefurnaceisaddedtothatoftheconvectionbank,makingitdifficultto
shiptheboilertocertainareasofthecountryortheworld.Also,aconvectivetype
of superheater can be easily located behind a screen section. The advantages of
the convective superheater over a radiant design are discussed later.
A recent application for packaged boilers has been in combined cycle
plants. These plants require steam for turbine sealing purposes when the HRSG
trips,andtheyneeditatshortnotice,say,within5–15min.Packagedboilerswith
completely water-cooled furnace designs are well suited for fast start-ups, as
discussed later.
Very high steam purity as in utility plants can be obtained in packaged
boilers through proper design of steam drum internals. Depending on the
application, steam purity in the range of 30–100 parts per billion (ppb) can be
FIGURE3.8 Agas-firedO-typepackageboilerwithextendedsurfaces.(Courtesy
ofABCO Industries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

achieved.Packagedboiler designshaveevolvedovertheyearsandhaveadapted
well to the needs of the industry.
Standard Boilers
Standard boilers, which are pre-engineered packages, are inexpensive and are
usedinapplicationsthatarenotverydemandingintermsofprocessoremission
limits. Decades ago, various manufacturers had developed so-called standard
designs for boilers of 40,000–200,000lb=h capacity with fixed dimensions of
furnace, tubes, tube spacing, lengths, and surface areas. If someone wanted a
boiler for a particular capacity that was not listed, the next or closest standard
modelwouldbeoffered.Standardmodelsarelessexpensivethancustomdesigns
becausenoengineeringisrequiredtodesignandbuildthem.Itmustbebornein
mindthatthesedesignsweredeveloped30–50yearsagowhentheconceptofflue
gas recirculation and low-NOx burners were unheard of. They also had a lot of
refractory in their design—on the floor, front walls, and rear walls—because
completely water-cooled furnace designs had not yet been developed. The
concerns with refractory-lined boilers are discussed later. However, emission
regulations are forcing suppliers to custom design the boilers.
As discussed in Chapter 4, the effect of flue gas recirculation and changes
inexcessairlevelshavetobereviewedonacase-to-casebasisdependingonthe
NOxandCOlevelsdesired.Hencestandardfurnacedimensionsmayormaynot
besuitableforagivenheatinput,becausetheflameshapevariesaccordingtothe
NOxcontrolmethodused.Flamelengthswithlow-NOxburnerscanbewideror
evenlongerthanwithregularburners.Hencetheuseoflow-NOxburnersmakes
it difficult to select a standard boiler that meets the same need and is also an
economicaloption.Thefurnacesizecouldbecompromised,whichmayresultin
flame impingement concerns with the burners used, or the gas pressure drop
acrosstheconvectionsurfacescouldbeverylargeduetothefluegasrecirculation
rates used; the efficiency also could be lower due to the higher exit gas
temperature associated with the larger flue gas flow. The operating cost due to
a higher gas pressure drop is discussed below and in Chapter 4.
Often gaseous and oil fuels are fired at excess air ranging from 10% to
20%; flue gas recirculation could be in the range of 10–35%, depending on the
NOx level desired. In a few boilers, 9ppmv NOx has been achieved with the
burneroperatingat15%excessairand35%fluegasrecirculationrateonnatural
gas firing. Thus it is possible to have a ‘‘standard’’ steam generator handling
nearly 30–40% more flue gases than it was designed for in the good old days
when 5–10% excess air was used without gas recirculation: A 100,000lb=h
standardboilercouldbeoperatingatgasflowconditionsequivalenttothoseofa
140,000lb=h boiler if it is not custom-designed. Of course, one could select a
largerstandardboiler,butitmayormaynotmeetalltherequirementsoffurnace
Copyright © 2003 Marcel Dekker, Inc.

dimensions, because developers of standard boilers generally increase furnace
lengths for higher capacity but not the width or height, due to shipping
constraints, particularly when the capacity is large. However, standard boilers
areusefulwhereoneisnotconcernedaboutoptimizingalltheparameterssuchas
efficiency,gaspressuredrop,andemissionlevelsandlowinitialcostisaprimary
objective.
Packaged steam generators of today are custom-designed with an eye on
operating costs and emissions. The furnace design also has undergone major
design innovations, the completely water-cooled furnace (Fig. 3.2) being one of
them. This design offers several advantages over the refractory-lined boilers
designed decades ago.
Advantages of Water-Cooled Furnaces
Water-cooled furnaces have a number of advantages over other types:
1. The front, rear, and side walls are completely water-cooled and are of
membrane construction, resulting in a leakproof enclosure for the
flame, as shown in Fig. 3.2. The entire furnace expands and contracts
uniformly, thus avoiding casing expansion problems. When refractory
is used on the front, side, or rear walls, the sealing between the hotter
membranewallsandthecooleroutercasingisaconcernandhotgases
can sometimes leak from the furnace to the outside. This can cause
corrosion of the casing, particularly if oil fuels are fired.
2. Problemsassociatedwithrefractorymaintenanceareeliminated.Also,
there is no need for annual shutdown of the boiler plant to inspect the
refractory or repair it, thus lowering the cost of owning the boiler.
3. Fast boiler start-up rates are difficult with refractory-lined boilers
becauseofthepossibilityofcausingcracksintherefractory.However,
with completely water-cooled furnaces, start-up rates are limited only
by thermal stresses in the drums and are generally quicker. The tubes
maybeweldedtothedrumsinsteadofbeing rolledifthestart-upsare
frequent. With boilers maintained in hot standby conditions using
steam-heated coils located in the muddrum, even10–15min start-ups
are feasible. With a separate small burner whose capacity is 6–8% of
the total heat input in operation during boiler standby conditions, the
boilercanbemaintainedatpressureandcanberampeduptogenerate
100% steam within 3–5min.
4. Heatreleaserateonanareabasisislowerforthewater-cooledfurnace
by about 7–15% compared to the refractory-lined boiler. Some gas-
fired boilers designed decades ago still use refractory on the floor;
replacing this with a water-cooled floor will increase the effective
heating surface of the furnace and lower the heat flux inside the tubes
Copyright © 2003 Marcel Dekker, Inc.

even further. The furnace exit gas temperature also decrease slightly
due to the increased effective cooling surface of the furnace. A lower
furnaceexitgastemperaturedecreasestheradiantenergytransferredto
asuperheaterlocatedatthefurnaceexitandthusreduces thepotential
for superheater tube failures. A lower area heat release also helps
reduce NOx, as can be seen from the correlations developed by a few
burner suppliers.
5. Reradiationfromtherefractoryonthefrontwall,sidewalls,andafloor
increases the flame temperatures locally, which results in higher NOx
formation. Of the total NOx generated by the burner, a significant
amount of NOx is formed at the burner flame base, so providing a
coolerenvironmentfor theflamenear theburnerhelpsminimizeNOx
to some extent.
6. Circulationwas oneof theconcernsabout the useof refractoryon the
floor of even gas-fired boilers because the D tubes are longer than
partitiontubesofthedividingwall.Heatfluxesinpackagedboilersare
generally low compared to those of utility boilers. To further protect
the floor and roof tubes, a small inclination to the horizontal is used;
also,consideringthelowsteampressure,tube-sidevelocities,heatflux,
and steam quality, departure from nucleate boiling (DNB) has never
been an issue, as evidenced by the operation of hundreds of boilers at
pressures as high as 1000–1500psig. The tube-sidevelocities are also
adequate to ensure that steam bubbles do not separate from thewater.
Hence refractory is not required on the floor or front or rear walls for
oil and gas firing.
7. Packaged boilers use economizers as the heat recovery equipment
instead of air heaters, whichonly serveto increase the flame tempera-
ture,thusincreasingtheNOxformation.Thegas-andair-sidepressure
drops are also higher with air heaters, thus adding to the fan size and
power consumption. The heat flux inside the furnace tubes is also
reduced owing to the smaller furnace duty.
Custom-Designed Boilers
Custom-designed boilers, as the term implies, are designed from scratch. Based
ondiscussionswiththeburnersupplierandthelevelofNOxandCOdesired,one
firstselectsthetypeofburnertobeusedandtheemissioncontrolstrategy.Afew
options could be considered:
Use a large amount of flue gas recirculation (FGR) and a low cost burner,
whichresultsinhigheroperatingcosts;onemayusealargeboilerwitha
wide convection bank to minimize gas pressure drop.
Use an expensive burner, which uses fuel or air staging methods and
requires little or no flue gas recirculation. A few burners can guarantee
Copyright © 2003 Marcel Dekker, Inc.

about 20–30ppmv NOx (at 3% oxygen dry) on gas firing. Installation
and operating costs associated with FGR are minimized.
Onecanalsoconsiderthepossibilityofusingaselectivecatalyticreduction
(SCR)systemalongwithalessexpensiveburner,whichhasalowtonil
FGR rate.
Steaminjectionmayalsobelookedinto,andthecostofsteamversusFGR
may be compared.
Depending on the NOx and CO levels desired and the fuel analysis, the
solution may vary from case to case, and no obvious solution exists for every
situation.Thusonearrivesatthebestoptionfromanemissioncontrolviewpoint
andthenstartsdevelopingtheboilerdesignusingtheexcessairandFGRratesfor
the fuels in consideration; the furnace dimensions to avoid flame impingement
onthefurnacewallsarethenarrivedat.Assumingaspecificexitgastemperature,
the boiler efficiency calculations are done to arrive at the air and flue gas flow
ratesandtheamountoffluegasrecirculated.Thisisfollowedbyanevaluationof
furnaceperformanceanddesignoftheheatingsurfaces.Theexitgastemperature
from the economizer is arrived at and compared with the assumed value;
efficiency is recalculated using the computed exit gas temperature, and revised
air and flue gas flows are obtained. (Air and flue gas quantities depend on the
amount of fuel fired, which in turn depends on efficiency.) Another iteration
starting from the furnace is done to fine-tune the performance. The superheater
performance isevaluatedatvariousloads todeterminewhether thesurfaceareas
are adequate.
Ifdifferentfuelsarefired,thesecalculationsarecarriedoutforallthefuels.
Efforts are then made to reduce the fuel consumption and also lower the fan
power consumption, which are recurring expenses, by fine-tuning the design
of the evaporator and economizer. A large economizer may be used to improve
theboilerefficiencyifthedurationofoperationwarrantsit.Thedesigneralsohas
theabilitytochangethedimensionsoftheconvectionsection—forexample,the
number of tubes wide, length, tube spacing, or even tube diameter—to come up
with low gas pressure drop and hence low fan operating cost as shown below.
Basedonpartialload performance andgastemperature profiles,bypass dampers
may be required if an SCR system is used. Hence it is likely that the steam
parameters of several boilers could be the same but the designs different due to
the emission control strategy used and degree of custom designing. A computer
program is used to perform these tedious calculations.
Example 1
A 150,000lb=h boiler firing standard natural gas and generating saturated steam
at 285psig with 230 F feedwater uses 15% excess air and 15% flue gas
(cid:2)
recirculation. The exit gas temperature is 323 F. Compare the performance of a
(cid:2)
standardboilerwiththatofacustom-designedunit.Thefluegasflowthroughthe
Copyright © 2003 Marcel Dekker, Inc.

boiler is 184,300lb=h. With 80 Fambient temperature, the efficiency is 83.38%
(cid:2)
HHV.
TheresultsofthecalculationsareshowninTable3.1.Thefollowingpoints
may be noted from this table:
1. The efficiency is the same in both designs because the exit gas
temperatureandexcessairarethesame.Also,thefurnacedimensions
are the same. Hence the furnace exit gas temperature is the same in
both designs.
2. Theconvectionsectionsaredifferent.Inthestandardboiler,weuseda
standardtubespacingof4in.Inthecustom-designedunit,wereduced
the surface area significantly by using fewer rows and also made the
convection bank tube transverse spacing 5in. This reduces the gas
pressure drop in the convection bank by 4in. WC. It also reduces the
duty of the evaporator section, as can be seen by the higher exit gas
temperature of 683 F versus 550 F.
(cid:2) (cid:2)
3. We added a few more rows to the economizer in the custom-designed
unitandmadeitstubeslonger toobtainthesameexitgastemperature
and also to handle the additional duty. Economizer steaming is not a
TABLE3.1 Reducing BoilerGas PressureDrop ThroughCustomDesigning
Item Standard boiler Customboiler
Furnace length width 32ft 7ft 11ft 32ft 7ft 11ft
(cid:4) (cid:4) (cid:4) (cid:4) (cid:4)
height
(cid:4)
Furnace exitgastemp, 2167 2167
F
(cid:2)
Gas templeaving 550 683
evaporator, F
(cid:2)
Exitgas temperature, 323 323
F
(cid:2)
Boiler surfacearea, ft2 8,920 6,710
Economizerarea, ft2 10,076 14,107
Geometry Evaporator Economizer Evaporator Economizer
Tubes=row 16 18 12 18
No.of rowsdeep 96 12 96 14
Effective length,ft 10 10 10 12
Gas pressuredrop, 11.0 1.7 7.0 1.6
in.WC
Transverse pitch, in. 4 4 5 4
Copyright © 2003 Marcel Dekker, Inc.

concerninpackaged boilersduetothesmallratiooffluegastosteam
flows(thisaspectisdiscussedlater).Hencewecanabsorbmoreenergy
in the economizer, which is a less expensive heating surface than the
evaporator.Theoverallgaspressuredropsavingof4in.WCresultsin
a saving of 31kW in fan power consumption (see Example 9.06b for
fan power calculation). If energy costs 7cents=kWh, for 8000h of
operation per year the annual saving is
31 0:07 8000 $17;360:
(cid:4) (cid:4) ¼
This is not an insignificant amount. Simply by manipulating the tube
spacing of the convection bank, we have dramatically reduced the fan
powerconsumptionandthesizeofthefan.Alsotheboilercostforthe
two designs should be nearly the same because the increase in
economizer cost is offset by the smaller number of evaporator tubes,
whichreducesthematerialcostsaswellaslaborcosts.Toimprovethe
energy transfer in evaporators one can also use finned tubes if the
boiler is fired with natural gas or distillate fuels. For example, if we
desiregood efficiencybutdonot wantan economizer because of, say,
shorter duration of operation or corrosion concerns, we may consider
usingextendedsurfacesintheconvectionbanktolowertheevaporator
exitgastemperaturebyabout40–100 F,whichimprovestheefficiency
(cid:2)
by 1–2.5% compared to a standard boiler.
4. Another important pointisthat surfaceareas should belooked atwith
caution.Oneshouldnotpurchaseboilersbasedonsurfaceareas,which
is still unfortunately being done. It is possible to distribute energy
among the furnace, evaporator, and economizer in several ways and
come up with the same overall efficiency and fan power consumption
andyethavesignificantlydifferentsurfaceareasasshowninTables3.1
and 3.2.
Comparing Surface Areas
Example 2
This example illustrates the point that surface areas can be misleading. A boiler
generates100,000lb=hofsaturatedsteamat300psig.Feedwaterisat230 F,and
(cid:2)
blowdown is 2%. Standard natural gas at 10% excess air is fired. Boiler
duty 100.8MM Btu=h, efficiency 84.3% HHV, furnace backpressure
¼ ¼
7in. WC
¼
ItisseenfromTable3.2thatboiler2hasabout10%moresurfaceareathan
boiler 1 but the overall performance is the same for both boilers in terms of
operating costs such as fuel consumption and fan power consumption. Also the
Copyright © 2003 Marcel Dekker, Inc.

TABLE3.2 Comparison of Boilerswith Same EfficiencyandBackpressure
Itema Boiler 1 Boiler 2
Heatrelease rate,Btu=ft3h 90,500 68,700
Heatrelease rate,Btu=ft2h 148,900 116,500
Furnace length,ft 22 29
Furnace width,ft 6 6
Furnace height,ft 10 10
Furnace exitgastemp, F 2364 2255
(cid:2)
Evaporator exitgastemp, F 683 611
(cid:2)
Economizer exitgastemp, F 315 315
(cid:2)
Furnace proj area,ft2 (duty) 802(36.6) 1026(40.4)
Evaporator surface,ft2 3972(53.7) 4760(52.1)
Economizer surface,ft2 8384(10.5) 8550(8.3)
Geometry Evaporator Economizer Evaporator Economizer
Tubes=row 11 15 10 15
Number deep 66 14 87 10
Length,ft 9.5 11 9.5 10
Economizer, fins=in. ht 3 0.75 0.05 0.157 5 0.75 0.05 0.157
(cid:4) (cid:4) (cid:4) (cid:4) (cid:4) (cid:4) (cid:4)
thickness (serration)
(cid:4) (cid:4)
Transverse pitch, in. 4 4 4.375 4
Overall heattransfercoeff 18 7.35 17.0 6.25
aDutyisinMMBtu=h,findimensionsininches,heattransfercoefficientinBtu=ft2h F.
(cid:2)
energy absorbed in different sections is different, hence comparing surface areas
is difficult unless one can do the heat transfer calculations for each surface.
Ithasbecomeacommonpractice(withtheplethoraofspreadsheetusers)to
compare surface areas of boilers and generally select the design that has the
higher surface area. Surface areas should not be used for comparing two boiler
designs for the following reasons:
1. Surface area is only a part of the simple equation Q UADT, where
¼
U overall heat transfer coefficient, A surface area, DT log-mean
¼ ¼ ¼
temperature difference, and Q energy transferred. However, the Q
¼
and DT could be different for the two designs at different sections as
shownintheaboveexample.Henceunlessoneknowshowtocompute
U;A values should not be compared.
2. Even if DT remains the same for a surface, U is a function of several
variables such as the tube size, spacing, and gas velocity. With finned
tubes, the heat transfer coefficient decreases as fin surface area
increases, as discussed in Q8.19. Hence unless one is familiar with
Copyright © 2003 Marcel Dekker, Inc.

all these issues, a simplistic tabulation of surface areas can be
misleading.
EFFECT OF STEAM PRESSURE ON BOILER DESIGN AND
PERFORMANCE
Another example of custom designing is shown in Example 3. In this example,
weareaskedtodesignaboilerforalower pressureofoperationfor thefirstfew
years with the idea of operating at a higher steam pressure after that.
Example 3
Aninterestingrequirementwasplacedonthedesignofaboiler.The175,000lb=h
boilerwastogeneratesteamat150psigand680 Fforthefirstfewyearsandthen
(cid:2)
operate at 650psig and 760 F. The piping and superheater changes had to be
(cid:2)
minimal when the time came for modifications.
Operatingasteamgeneratorattwodifferentpressuresisachallengingtask,
particularlywhenasuperheaterispresent.Thereasonisthatthelargedifference
inspecificvolumeofsteamaffectsthesteamvelocityinsidethesuperheatertubes
andthesteam-sidepressuredrop,whichinturnaffecttheflowdistributioninside
the tubes. The ratio of specific volume between the 150 and 650psig steam is
about4.Henceforthesamesteamoutput,wecouldhavea4timeshighersteam
velocity at the lower pressure if the flow per tube were the same. Also, if the
pressuredropat650psigwere,say,30psi,itwouldbeabout120psiatthelower
operating pressure if flow per tube were the same. Hence it was decided to
manipulate the streams and steam flows as shown in Fig. 3.9.
In the low pressure operation, therewould be two inlets to the superheater
from opposite ends of the headers as shown in Fig. 3.9a. This would make the
velocity and pressure drop inside the tubes more reasonable. The total length of
tubing traveled by steam in the low pressure option would be nearly half that of
thehighpressurecase,whichalsoreducesthepressuredrop.Partofthesteamis
inparallelflowandpartincounterflow.Athighgastemperatures,asinthiscase,
the difference in performance between parallel and counterflow superheaters is
marginal.
Inthehighpressurecase,allthesteamflowsthroughthesuperheatertubes
incounterflow.Becausethespecificvolumeissmall,thesteamcanflowasshown
with a reasonable steam velocity and without increasing the pressure drop. The
performanceinboth,casesisshowninTable3.3.Thuswithaminimalamountof
reworking, the piping could be changed when high pressure operation is begun.
The superheater per se was untouched, and only the nozzle connections were
redone. This boiler will be in operation for several years. If custom designing
were not done, the capacity at low pressure mode would have to be limited to
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.9 Superheater piping arrangement for (a) low and (b) high pressure
operation.
about 50–60% of the boiler capacity in order to avoid unreasonable steam
velocity or pressure drop values. The main steam line has two parallel valves
in the low pressure mode and will be converted to single-valve operation in the
high pressure mode.
BOILER FURNACE DESIGN
The furnace is considered the heart of the boiler. Both combustion and heat
transfertotheboilingwateroccurhere,soitshouldbecarefullydesigned.Ifnot,
several problems may result, such as lower or higher steam temperature if a
TABLE3.3 Boiler Performanceat Lowand High SteamPressurea
Lowpressure High pressure
Steamflow,lb=h 175,000 175,000
Steamtemperature, F 680 760
(cid:2)
Steampressure,psig 150 650
Pressure drop,psi 23 46
aFeedwater 230 F;excessair 15%;FGR 17%;naturalgas.
¼ (cid:2) ¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

superheaterisused;theheatfluxshouldbesuchastoavoidfromDNBconcerns.
Circulation inside the tubes should be good. There could be incomplete
combustion, which leads to lower efficiency and, coupled with a poor burner
design,higheremissionsofNOxandCO.Also,theflameshouldnotimpingeon
the walls of the furnace enclosure. Hence it is always good practice to discuss
emission control needs with potential burner suppliers who can model the flame
shapeandensurethatthefurnacedimensionsusedcanavoidflameimpingement
issues while ensuring the desired emission levels.
In boilers fired with fuels that produce ash, the furnace is sized so that the
furnace exit gas temperature is below the ash softening temperature. This is to
avoid potential slagging problems at the turnaround section. Slag or molten
deposits from various salts and compounds in the ash can cause corrosion
damage and also affect heat transfer to the surfaces. The gas pressure drop
across the convection section is also increased when the flow path is blocked by
slag deposits.
One of the parameters used in furnace sizing is the area heat release rate.
Thisisthenetheatinputtotheboilerdividedbytheeffectiveprojectedarea.This
factordetermines thefurnaceabsorption and hencethe dutyand heat fluxinside
the tubes. Typically it varies from 100,000 to 200,000Btu=ft2 h for oil- and gas-
fired boilers and from 70,000 to 120,000Btu=ft2 h for coal-fired units.
Thevolumetricheatreleaserateisanotherparameter,whichisobtainedby
dividing the net heat input by the furnace volume. This is indicative of the
residence time of the flue gases in the furnace and varies from 15,000 to
30,000Btu=ft3h for coal-fired boilers. For oil and gaseous fuels it is not as
significant a parameter as for fuels that are difficult to burn such as solid fuels.
However, this parameter ranges from 60,000 to 130,000Btu=ft3h for typical
packaged oil- and gas-fired boilers.
Fromthesteamside,thecirculationofthesteam-watermixtureinthetubes
should be good. As discussed in Q7.30, several variables affect circulation,
including static head available, steam pressure, tube size, and steam generation.
The circulation is said to be adequate when the heat flux does not cause DNB
conditions for the steam quality in consideration. Packaged boilers have a low
static head, unlike field-erected industrial boilers, and also have longer furnace
tubes. However, packaged boilers operate at low pressures, on the order of 200–
1200psig, unlike large utility boilers, which operate at 2400–2600psig, and
circulation is better at lower pressures.
Today’s boilers use completely welded membrane walls for the furnace
enclosure (Fig. 3.2). Earlier designs were of tangent tube construction or had
refractory behind the tubes (Fig. 3.10). With the refractory-lined casing, it is
difficult to maintain a leakproof enclosure between the refractory walls and the
water-cooled tubes, as a result flue gases can leak to the atmosphere, leading to
corrosion, at the casing interfaces, particularly on oil firing. Balanced draft
Copyright © 2003 Marcel Dekker, Inc.

FIGURE3.10 Furnaceconstruction—membranewall,tangenttube,andrefractory
wall.
furnace design is used to minimize this concern, where the furnace pressure is
maintained near zero by using a combination of forced draft and induced draft
fans.
Thetangenttubedesignisanimprovementovertherefractory-linedcasing.
However, it has the potential for leakage across the partition wall. During
operation the tubes in the partition wall are likely to flex or bend due to thermal
expansion, paving the way for leakage of combustion gases from the furnace to
the convection bank, resulting in higher CO emissions and also higher exit gas
temperature from the evaporator and lower efficiency. Present-day boiler designs
useforced draftfans,andthefurnaceispressurizedto20–30in.WC,depending
onthebackpressure.IfSCRandCOcatalystsareused,theback-pressureislikely
tobeevenhigher.Withsuchalargedifferentialpressurebetweenthefurnaceand
the convection bank, a leakproof combustion chamber is desired to ensure
completecombustion.Ifgasbypassingoccursfromthefurnacetotheconvection
side,theresidencetimeofthefluegasesinthefurnaceisreduced,thusincreasing
theformationofCO.Anotherconcernwithleakageofhotfurnacegasesfromthe
furnace to the convection bank is the impact on superheater performance; the
steam temperature is likely to be lower.
The present practice is to use membrane walls. These consist of tubes
weldedtoeachotherbyfinsasshowninFigs.3.2and3.10.Agastightenclosure
is thus formed for the combustion products. The partition wall is also leakproof,
hencegasbypassingisavoidedbetweenthefurnaceandconvectionsections.This
ensures complete combustion in the furnace enclosure. Typical designs at low
pressuresuse2in.ODtubesatintervalsof3.5–4in.dependingonmembranetip
temperature. Three-inch tubes have also been swaged to 2in. and used at 4in.
Copyright © 2003 Marcel Dekker, Inc.

pitch.Thisensuresalowermembranetemperatureaswellasreasonableligament
efficiency in the steam and mud drums. At pressures up to 700–750psig,
membranes using 2in. tubes on 4in. pitch have been found to be adequate due
tothecombinationoflowheatfluxinthefurnaceandlowsaturationtemperature,
as evidenced by the operation of several hundred boilers. The 1in. long
membrane with appropriate thickness does not result in excessive fin tip
temperatures or thermal stress concerns. At higher pressures, one may use
0.5in. 0.75in. long membranes. Figure 3.11 shows how fin tip temperatures
(cid:4)
vary with heat flux and membrane length.
Thefurnaceprocessisextremelycomplicated,becausetoday’sburnershave
to deal with various aspects of burner designs such as staged fuel or staged air
combustion, flue gas recirculation, and other NOx control methods; hence
furnace performance should be arrived at on the basis of experience, field data,
andcalculations.Thefurnaceexitgastemperatureisthemostimportantvariable
in this evaluation and is a function of heat input, fluegas recirculation rate, type
offuel used, effective cooling surface available, and excess air used. A gas-fired
flame has less luminosity than an oil flame, so the furnace exit temperature is
higher,asshowninFig.3.12.Acoal-firedflamehasanevenhigherfurnaceexit
gas temperature. An oil flame is more luminous and the furnace absorbs more
energy, resulting in higher heat flux in the furnace tubes.
Energy Absorbed by the Furnace
The energy transferred to the furnace is obtained from the equation
Q A e e s T4 T4 W LHV W h
¼ p 1 2 ð g (cid:3) wÞ¼ f (cid:3) g e
FIGURE3.11 Relatingfintiptemperaturetoheatfluxinmembranewall furnace.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.12 Furnace outlettemperature forgasand oilfiring.
where
Q energy transferred to the furnace, Btu=h
¼
T average gas temperature in the furnace, R
g¼ (cid:2)
h enthalpy of flue gases corresponding to the furnace exit gas
e¼
temperature T , Btu=lb
e
T average furnace wall temperature, R
A
w¼
effective projected area of the furn
(cid:2)
ace, ft2
p¼
s radiation constant
¼
e ;e emissivity of flame and wall, respectively
1 2¼
LHV lower heating value of the fuel, Btu=lb
¼
W ;W fuel and flue gas quantity, lb=h
f g¼
Theemissivityoftheflamemaybedeterminedbyusingmethodsdiscussed
inQ8.08.Theeffectiveprojectedareaincludesthewater-cooledsurfacesandthe
opening to the furnace exit plane. If refractory is used on part of the surfaces, a
correctionfactorof0.3–0.5hastobeusedforitseffectiveness.Oncethefurnace
dutyisarrivedat,theheatfluxinsidethetubemaybeestimated.Heatfluxinside
the tubes is a very important parameter because it affects the boiling process.
Example 4
Determine theenergyabsorbedbythepackaged boilerfurnace firing naturalgas
for which data are given in Table 3.4. At 100% load, boiler duty or energy
absorbed by steam 118.71MM Btu=h. Flue gas flow 125,246lb=h at 100%
¼ ¼
load.
Copyright © 2003 Marcel Dekker, Inc.

TABLE3.4 Boiler Performance—GasFiringa
Load(%)
25 50 75 100
Boiler duty,MMBtu=h 29.14 50.09 89.03 118.71
Excess air,% 30 15 15 15
Fuelinput,MMBtu=h 34.68 69.79 105.69 141.89
Heatrel rate,Btu=ft3h 16,055 32,310 48,931 65,691
Heatrel rate,Btu=ft2h 29,646 59,660 90,349 121,297
Steamflow,lb=h 25,000 50,000 75,000 100,000
Steamtemperature, F 711 740 750 750
(cid:2)
Economizerexit water 328 334 356 374
temp, F
(cid:2)
Boiler exitgastemp, F 525 587 666 739
(cid:2)
Economizerexit gas 254 271 298 327
temp, F
(cid:2)
Airflow, lb=h 32,954 58,665 88,843 119,275
Fluegas,lb=h 34,413 61,602 93,290 125,246
Drygasloss, % 3.71 3.58 4.08 4.62
Airmoisture loss,% 0.1 0.1 0.1 0.12
Fuelmoistureloss,% 10.48 10.55 10.67 10.79
Casing loss,% 1.2 0.6 0.4 0.3
Margin,% 0.5 0.5 0.5 0.5
Efficiency,% HHV 84.01 84.67 84.24 83.66
Efficiency,% LHV 93.12 93.85 93.37 92.73
Furnace backpressure, 0.8 2.61 6.21 11.49
in.WC
aSteampressure500psig;feedwater230 F,blowdown1%,ambtemp80 F;RH60%,fuel-
(cid:2) (cid:2)
standard natural gas. Flue gas analysis (vol%): CO 8:29, H O 18:17, N 71,
0:07;O 2:46.Boilerfurnaceprojectedarea 1169ft2,fu 2 r ¼ nacewidth 2 7 ¼ .5ft,length 2¼ 32ft,
2¼ ¼ ¼ ¼
height 9ft.
¼
The net heat input to the furnace is
0:992
118:71 127MMBtu=h
(cid:4)0:9273¼
where0.992 17heatlosses,and0.9273istheboilerefficiencyonLHVbasis.
¼
Net heat input 127 106
(cid:4) 108;900Btu=ft2 h
Effective furnace area¼ 1169 ¼
Copyright © 2003 Marcel Dekker, Inc.

Thefurnaceexitgastemperature fromFig.3.12is2235 F.Itmaybeshownthat
(cid:2)
the enthalpy of the flue gases at 2235 F is 661.4Btu=lb based on the flue gas
(cid:2)
analysis. (See Appendix, Table A8.)
The furnace duty from (5) 127 106 125;246 661:4 44:2MM
¼ (cid:4) (cid:3) (cid:4) ¼
Btu=h.
The average heat flux based on projected area is
44:2 106
(cid:4) 37;810Btu=ft2 h
1169 ¼
However, what is of significance is the heat flux inside the boiler tubes, not the
heatfluxonaprojectedareabasis.Wecanrelatethesetwoparametersasfollows:
q S q pd=2 2h
p t ¼ cð þ Þ
where
q heat flux on projected area basis
p¼
S transverse pitch of membrane walls, in.
q
t¼
heat flux on circumferential area basis, Btu=ft2 h
c¼
d OD of furnace tubes
¼
h membrane height, in.
¼
Once q is obtained, we can relate it to q, the heat flux inside the tubes, as
c i
follows:
q d qd
c ¼ i i
where d tube inner diameter, in. Simplifying
i¼
q S d=d
q p tð iÞ
i ¼pd=2 2h
þ
In our example, q 37;810Btu=ft2 h, S 4in:; h 1in:; d 2,
p ¼ t ¼ ¼ ¼
d 1:706in. Then
i ¼
37;810 2=1:706 4
q (cid:4)ð Þ(cid:4) 34;500Btu=ft2 h
i ¼ 3:14 2=2 2 1 ¼
(cid:4) þ (cid:4)
Note that if we did the same calculation for oil firing, the heat flux would be
higher,becausethefurnaceexitgastemperatureislower.Heatfluxinsidetubesis
an important parameter, because allowable heat fluxes are limited by circulation
rates. Large heat flux inside tubes can lead to departure from nucleate boiling
conditions.
Estimating Fin Tip Temperatures
Fintiptemperaturesinboilersofmembranewalldesigndependonseveralfactors
suchascleanlinessofthewateror tube-sidefouling,fingeometry,andheatflux,
Copyright © 2003 Marcel Dekker, Inc.

which is a function of the load and gas temperature. Assuming that membranes
arelongitudinalfinsheatedfromoneside,thefollowingequationmaybeusedto
determine the fin tip temperature:
t t
g(cid:3) b t t
cosh mh ¼ g(cid:3) t
ð Þ
where
t gas temperature, F
g¼ (cid:2)
t fin base temperature, F
b¼ (cid:2)
Duetothehighboilingheattransfercoefficients,ontheorderof3000–
10,000Btu=ft2h F,finbasetemperatureswillbeafewdegrees higher
(cid:2)
than saturation temperature, assuming that tube-side fouling is mini-
mal.
t fin tip temperature, F
t¼ (cid:2)
h membrane height, in. (see Fig. 3.11)
m ¼ h C=KA 0:5
¼ð g Þ
where
h gas-side heat transfer coefficient, Btu=ft2 h F
g¼ (cid:2)
C perimeteroffincrosssection 2b Lin.(forheatingfromoneside)
¼ ¼ þ
where b fin thickness and L fin length or furnace length
¼ ¼
K fin thermal conductivity, Btu=ft h F
(cid:2)
¼
A cross-section of fin bL
¼ ¼
C=Aforlongfins 2b L =bL L=bL 1=b
¼ð þ Þ ¼ ¼
Example 5
In a boiler furnace, gas temperature at one location is 2200 F. The gas-side heat
(cid:2)
transfer coefficient is estimated to be 30Btu=ft2 h F. Fin height 0.5in. fin
(cid:2)
¼
thickness 0.375in. Fin base temperature is 600 F. Thermal conductivity of fin
(cid:2)
¼
is 20Btu=ft h F. Determine the fin tip temperature.
(cid:2)
Solution: Using the above equation, we have
T 2200 F; t 600 F; h 30; h 0:5in:; b 0:375in:;
g ¼ (cid:2) b ¼ (cid:2) g ¼ ¼ ¼
K 20
¼
0:5 30 12 0:5
mh (cid:4) 0:3536 or cosh 0:3536 1:063
¼ 12 20 0:25 ¼ ð Þ¼
(cid:1) (cid:4) (cid:2)
2200 600
T t ¼ 2200 (cid:3) 1:0 (cid:3) 63 ¼ 695 (cid:2) F
Copyright © 2003 Marcel Dekker, Inc.

THE BOILING PROCESS
When thermal energy is applied to furnace tubes, the process of boiling is
initiated.However,thefluidleavingthefurnacetubesandgoingbacktothesteam
drum is not 100% steam but is a mixture of water and steam. The ratio of the
mixture flow to steam generated is known as the circulation ratio, CR. Typically
the steam quality in the furnace tubes is 5–8%, which means that it is mostly
water, which translates into a CR in the range from about 20 to 12. CR is the
inverse of steam quality. Circulation calculations and the importance of heat
fluxes are discussed in Q7.29.
Nucleate boiling is the process generally preferred in boilers. In this
process, the steam bubbles generated by the thermal energy are removed by
the flow of the mixture inside the tubes at the same rate, so the tubes are kept
cool. Boiling heat transfer coefficients are very high, on the order of 5000–
8000Btu=ft2h FasdiscussedinQ8.46.Whentheintensityofthermalenergyor
(cid:2)
heat flux exceeds a value known as the critical heat flux, then the process of
nucleate boiling is disrupted. The bubbles formed inside the tubes are not
removed adequately by the cooler water; the bubbles interfere with the flow of
water and form a film of superheated steam inside the tubes, which has a lower
heat transfer coefficient and can therefore increase the tube wall temperatures
significantlyasillustratedinFig.3.13.Itisthedesigner’sjobtoensurethatweare
FIGURE 3.13 Boiling process andDNB inboiler tubes.
Copyright © 2003 Marcel Dekker, Inc.

neverclosetocriticalheatfluxconditions.Generally,packagedboilersoperateat
low pressures compared to utility boilers and therefore DNB is generally not a
concern. The actual heat fluxes range from 40,000 to 70,000Btu=ft2 h, while
critical heat flux could be in excess of 250,000Btu=ft2 h. However, one has to
perform circulation calculations on all the parallel circuits in the boiler, particu-
larlythefrontwall,whichisexposedtotheflame,toensurethatthereisadequate
flowineachtube.IntheABCOD-typeboiler,carefullysizedorificesareusedto
limit the flowof mixture through the D headers while ensuring flow through all
the tubes in the front wall. Ribbed or rifled tubes are sometimes used as
evaporator tubes. These tubes ensure that the wetting of the tube periphery is
better than in plain tubes. They have spiral grooves cut into their inner wall
surface. The swirl flow induced by the ribbed tubes not only forces more water
outwardontothetubewallsbutalsopromotesgeneralmixingbetweenthephases
to counteract the gravitational stratification effects in a nonvertical tube. Ribbed
ortwistedtubescanhandleamuchhigherheatflux,often50%higherthanplain
tubes.Theyareexpensivetousebutofferasafetynetinregionsofhighheatflux,
particularly in very high pressure boilers.
In fire tube boilers, the critical heat flux may be estimated as shown in
Q8.47.Againowing tothelowpressureofsteam,theallowableheatfluxtoavoid
DNB is much higher than the actual values; hence tube failures are rare unless
tube deposits or scale formation is severe. As discussed later in this chapter,
maintaininggoodboilerwaterchemistry,ensuringproperblowdown,andadding
chemicals to maintain proper alkalinity and pH in the boiler should minimize
scale formation and thus prevent tube failures.
BOILER EFFICIENCY CALCULATIONS
Theboilerefficiencyisanimportantvariablethatisimpactedbythetypeoffuel,
its analysis, the exit gas temperature, excess air used, and ambient reference
conditions. The major losses due to flue gases and the method of computing
efficiency are discussed in Q6.19. With rising fuel costs, plant engineers should
try to aim for higher efficiency if the plant is base-loaded and operates
continuously. Often less efficient and less expensive units are purchased owing
to lack of funds, and this practice should be reviewed. One should look at the
long-term benefits to the end user. Similarly, the fan operating costs should also
be evaluated. A design with high gas pressure drop in the boiler may be less
expensive, but if one considers the long-term operating costs, it may not be the
better choice.
Table3.5showstheeffectofexcessairandexitgastemperaturesonboiler
efficiencyand cost of operation. Itis important to operate at as lowan excessof
air as possible; however, as discussed in Chapter 4, limits on NOx and CO may
force the burners to use higher values of excess air.
Copyright © 2003 Marcel Dekker, Inc.

TABLE3.5 Effect ofExcess Air andExitGas Temperatureon Efficiencya
Excess air(%)
5 20 5 20
Exitgas temp, F 300 300 400 400
(cid:2)
Vol% CO 9 7.97 9 7.97
2
H O 19.57 17.56 19.57 17.56
2
N 70.53 71.31 70.53 71.31
2
O 0.89 3.16 0.89 3.16
2
Efficiency,% HHV 84.81 84.22 82.64 81.79
% LHV 94.11 93.46 91.71 90.70
Fluegas,lb=h 96,160 110,000 98,680 113,210
Annual fuelcost,MM$=yr 2.854 2.873 2.928 2.959
aSteamflow 100,000lb=h,300psigsat,feedwatertemp 230 F,2%blowdown,ambient
¼ ¼ (cid:2)
temp 80 F,relativehumidity 60%,boilerduty 100.8MMBtu=h,fuelcost $3=MMBtu.
¼ (cid:2) ¼ ¼ ¼
As shown in Tables 3.4 and 3.7, the efficiency of packaged boilers varies
with load. This information may be used as a planning tool as discussed,
particularly when the plant has HRSGs in addition to steam generators.
Combination Firing
BoilerefficiencycalculationsaredoneusingASMEPTC4.1methods,asshown
inQ6.19.Whenacombinationoffuelsisfired,thecalculationscanbeinvolved.
The results from a program developed are shown in Fig. 3.14. They show the
performance of a boiler firing two different fuels at the same time. Based on the
exitgas temperature and measured or predicted oxygenfor the fluegas mixture,
one cansimulate theexcessair and obtain theperformancewith individual fuels
first and then obtain the combined effect on air and gas flows, flue gas analysis,
combustion temperatures, heat losses, and efficiency.
BURNERS
The fuel burner is an important component of any boiler. Burner designs have
undergone several iterations during the last decade. Burner suppliers such as
CoenandToddareofferingburnersthatresultinsingle-digitNOxemissionsand
very low CO levels, competing with the SCR system presently used in the
industry for single-digit NOx emissions. However, these burners use a large
amount of flue gas recirculation, and flame stability at low loads is a concern.
Developmentworkisgoingontoimproveontheseresults.Fuelorairstagingand
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.14 Efficiencycalculations forsimultaneous firing offuels.
steam injection are the other methods used by burner suppliers to control NOx.
Todaysingleburnersareusedforcapacitiesupto300–350MMBtu=hongasor
oil firing.
Often more than one fuel is fired in the burner. When different gaseous
fuels are fired in a burner, the fuel gas pressure has to be adjusted at the burner
inlet to ensure proper fuel flow.
Example 6
Letussaythataburnerisfiring5MMBtu=honLHVbasisusingafueloflower
heating value, 1400Btu=ft3, and molecular weight 25.8 at a pressure of 30psig.
Assuming the nozzles remain the same, what should be done when a fuel of
Copyright © 2003 Marcel Dekker, Inc.

heatingvalue700Btu=ft3whosemolecularweightis11.6isfired,thedutybeing
the same?
Solution: The gas pressure should be adjusted; otherwise it would be
difficulttocontroltheheat input.The pressure drop acrossthe nozzlesisrelated
to the flow of fuel as follows (Subscripts 1 and 2 refer to fuels 1 and 2):
DP KW2=MW KQ2MW
1 ¼ ¼
where Q volumetric flow
¼
W mass flow
¼
MW molecular weight
¼
K is a constant 30=Q2 MW
¼ 1
Basically we are converting the pressure drop equation from mass to
volumetric flow.
Because the heat input by both fuels is the same,
Q LHV Q LHV
1 1 ¼ 2 2
where LHV is the lower heating value of the fuel, Btu=ft3.
30
DP Q2MW
2 ¼Q2MW 2 2
1 1
Rewriting Q in terms of Q and simplifying, we have
2 1
700 2 25:8
DP 30 17psi
2 ¼ (cid:4) 1400 (cid:4)11:6¼
(cid:1) (cid:2)
Thus we should have a lower fuel gas pressure to ensure the same heat input.
COMBUSTION CONTROLS
The function of a combustion control system is to ensure that the steam
generation matches the steam demand. When the demand exceeds the supply,
the steam pressure will decrease and vice versa. Although a few utility boilers
generate steam at sliding pressures, packaged boilers typically generate steam at
fixedpressure.Thecontrolsystemimmediatelyadjuststhefuelinputtomaintain
the steam pressure. The following methods are typically used for combustion
control.
Single-Point Positioning: This is a simple and safe system for combustion
control. A common jackshaft is modulated by a power unit based on
variations in drum pressure and is mechanically linked to both the fuel
controlvalueandtheaircontroldamper.Thissystem islimitedtosmall
boilers, typically below 100,000lb=h, that have an integral fan mounted
Copyright © 2003 Marcel Dekker, Inc.

on top of the wind-box and are fired by a single fuel of nearly constant
heatingvalue.Fuelheatingvaluesshouldnotvary,andonlyonefuelcan
be fired at a time. When low CO values are desired such as less than
70ppmv, an oxygen trim is added.
Parallel Positioning System: This system is used on large boilers where a
remotefansuppliesairtothewind-box.Ithasseparatepneumaticpower
units for controlling air and fuel.
Full Metering with Cross Limiting: This system is expensive but is
recommended for accurate air=fuel ratios, for keeping oxygen levels
optimized, and for its firing precision. Fuel and air flows are measured
continuouslyandareadjustedasrequiredtomaintainthedesiredair=fuel
ratio.Airleadsonloadincreases,andfuelleadsonloaddecreases.This
system allows simultaneous firing of two or more fuels. When emission
levels are stringent and a large flue gas recirculation rate is used, this
method is used and offers better control over the combustion process.
As far as the boiler is concerned, a three-element-level control system is
generally used to control the drum water level. Other controls would include
steam temperature and master pressure control. Figure 3.15a and 3.15b show
typical schemes ofgas-side andsteam-sideinstrumentationandcontrols,respec-
tively, used in packaged boilers.
FAN SELECTION
Packaged steam generators of today use a single fan for up to 250,000lb=h of
steam. The furnaces of oil- and gas-fired boilers are pressurized, hence the fan
parametersshouldbeselectedwithcare.Estimatingthefloworheadinaccurately
canforcethefantooperateinanunstableregionorresultinthehorsepowerbeing
too high and the operation inefficient. The density of air should be accurately
estimated,soelevationandambienttemperatureconditionsshouldbeconsidered.
Insomecoldlocations,asteam–airpreheatcoilisusedtopreheattheairbeforeit
enters the fan, and this adds to the pressure drop. When flue gas recirculation is
required, usually the flue gases from the boiler exit are sucked in by the fan,
whichhandlestheresistanceoftheentiresystem.Thedensityofthemixedairis
lower, owing to the higher temperature of the air mixed with the flue gases. The
fanshouldbeselectedforthelowestdensitycase,asexplainedinQ9.06,because
themassflowofairisimportantforcombustionandnotthevolumetricflow.The
effect of gas density on fan performance is shown in Fig. 3.16a.
Largemarginsonflowandheadshouldnotbespecified,becausethisleads
tooversizingofthefanandcanforcethefanoperatingpointtotheextremeright
of the curvein Fig. 3.16b, wherethe horsepower can be extremely high; a lot of
energyisalsowasted.Inletvanecontrolistypicallyusedforcontrollingtheflow
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.15a Scheme ofboiler controls—gas side.(Courtesy ofABCO Industries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE3.15b Scheme ofboiler controls—steamside. (Courtesyof ABCOIndustries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.16 (a) Fan performance and range of operation. (b) Effect of system
resistanceonfanhorsepower.(c)Effectofvanepositiononflowreductioninfans.
ofair;thissystemtypicallyoperatesstablybetween20%and100%vaneopening,
which does not translate into a large flow difference, as can be seen from Fig.
3.16c. Hence a small margin on flowand head is preferred—about 15% margin
on flow and 20–25% on head is adequate; otherwise one may have to use a
variable-speed drive or frequency modulation for control, which is expensive.
Underestimating the fan head can also cause the fan to operate in the unstable
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.16 Continued.
region as shown in Fig. 3.16a. Curve 2 in Fig. 3.16b is the estimated curve, and
theactualcurve1istotheleft,closetotheunstableregionwithpositiveslope.It
also delivers less flow than required. The fan operating point must preferably be
inthenegativelyslopingportionoftheheadversusflowcurve;otherwisethefan
could operate in the unstable region, causing surges and vibration. The flue gas
recirculation lines must be properly sized; typical air and flue gas velocity in
ducts is about 40ft=s.
The flue gas recirculation line is usually connected to the fan inlet in gas
anddistillateoil–firedboilers.Thisincreasesthesizeoftheforceddraftfan.The
highergaspressuredropintheboilerduetotheincreasedmassflowshouldalso
be considered when selecting the fan. A separate recirculation fan is used
occasionally when heavy fuel oils containing sulfur are fired and the flue gases
areadmittedintotheburnerwind-box.Ifthefluegaseswereallowedtomixwith
thecoldairatthefaninlet,themixturetemperaturecouldfallbelowtheaciddew
point, possibly leading to corrosion.
The fan inlet duct and downstream ductwork must have proper flow
distribution. Pulsations and duct vibrations are likely if the inlet airflow to the
fanbladesisnotsmoothandthemaldistributioninvelocityislarge.Similarly,the
ductwork between the fan and wind-box should be designed to minimize flow
maldistribution to ensure proper airflow to the burner.
SUPERHEATERS
The superheater is an important component of a packaged boiler. The degree of
superheatcouldbeveryhigh,withsteamtemperaturesupto1000 F,oraslowas
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

50 F.Withaverylowdegreeofsuperheat,onecanlocatethesuperheaterbehind
(cid:2)
the evaporator and ahead of the economizer. In this case, the superheater may
require a large surface area due to the low log-mean temperature difference, but
extended surfaces may be used (if distillate oils and gaseous fuels are fired) to
make it compact.
Radiantsuperheaters,whicharetypicallylocatedinthefurnaceexitregion,
arewidelyusedbyseveralboilermanufacturers.Radiantsuperheatershavetobe
designedverycarefullybecausetheyoperateinamuchharsherenvironmentthan
convective superheaters, which are located in the convective zone behind screen
tubesasshowninFig.3.17a.Radiantsuperheatersarelocatedatthefurnaceexit
or in the turning section (Fig. 3.17b). The furnace exit gas temperature is a
difficult parameter to estimate. Variations in excess air, flue gas recirculation
rates, and burner flame patterns can affect this value and the temperature
distribution across the furnace exit plane. The gas temperature in operation
could be off by 100–150 F from the predicted value. The turning section is also
(cid:2)
subject to nonuniformity in gas flow and turbulence, which can affect the
superheater performance. Thus its duty can be either underestimated or over-
estimated by a large margin.
TheconvectivesuperheaterisshieldedbehindscreentubesasshowninFig.
3.17a and often operates at 1800–1900 F in comparison with the 2200–2300 F
(cid:2) (cid:2)
for radiant designs. Because it operates at lower tube wall temperatures, its life
canbelonger,butitrequiresagreatersurfaceareabecauseofthelowerlog-mean
temperature difference. However, owing to the lower operating temperatures, a
convectivesuperheatercanusealowergradematerialthantheradiantdesign,and
this helps balance thecost to some extent.Also, its locationbehind screen tubes
helps reduce the gas flow nonuniformity to a great extent; hence predicting its
performance is easier and more reliable than predicting the performance of the
single-stage radiant superheater.
FIGURE3.17 Locationofconvectiveandradiantsuperheater.1,Superheater;2,
burner; 3,screen evaporator.
Copyright © 2003 Marcel Dekker, Inc.

Several boilers operate at partial loads of less than 60% for large periods.
The radiant superheater, by its nature, absorbs more enthalpy at lower loads,
hence the steam temperature increases at lower loads. Convective heat transfer
depends on mass flow of flue gases, so as the load decreases, the gas flow and
temperaturedecrease atthesuperheater region,and therefore thesteam tempera-
ture and the tube wall temperatures drop with load. Also if at 100% load the
steam-sidepressuredropinaradiantsuperheateris50psi,thenat30%,itwillbe
about5psi,whichcanleadtoconcernsaboutsteamflowdistributionthroughthe
tubes when it is receiving more radiant energy per unit mass of steam. Coupled
with nonuniform gas flow distribution at low loads and low gas velocities, the
radiant superheater poses several concerns about its tube wall temperatures and
hence its life.
The convective superheater is located behind several rows of screen tubes
that shield it from furnace radiation. Gas flow entering the superheater is well
mixed;henceitiseasiertopredictitsperformanceandtubewalltemperatures.As
mentionedearlier,itssurfacearearequirementmaybemore,butoneisassuredof
low tube wall temperatures and hence longer life.
The steam temperature in a convective superheater generally decreases as
theloadfallsoff,whereasinaradiantdesignitremainswithinasmallrangeover
alargerloadrange.Hencetheconvectivedesignhastobesizedtoensurethatthe
requiredsteam temperatureis achievedatthe lowest load, whichcan increaseits
size and cost.
Thechoiceofwhethertousearadiantoraconvectivesuperheaterisbased
on the experience of the supplier. Because the surface area requirements are
significantly different due to the different log-mean temperature differences, this
is yet another reason that a comparison of surface areas can be misleading.
Ifheavyoilisfiredintheboiler,theproblemsassociatedwithslaggingand
high temperature corrosion pose concerns for the longevity and operability of
radiant superheaters as discussed below, so convective superheater designs are
preferredinsuchcases.Packagedboilersuselimitedspacecomparedtoutilityor
field-erectedboilers;withhighgasvelocitiesandslaggingpotentialinthefurnace
exit region, the radiant design is vulnerable. Even with a convective superheater
design, care should be taken to use retractable soot blowers, and there should be
adequate space provided for cleaning and maintenance.
Steam Temperature Control
Thesteamtemperatureinpackagedboilersisoftencontrolledfrom60%to100%
load by using a two-stage superheater design with interstage attemperation as
shown in Fig. 3.18. Steam temperature can also be maintained from 10% to
100%; however, this calls for a much larger superheater surface area. Deminer-
alized water should be used for attemperation, because it does not add solids to
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.18 Steamtemperature controlmethods.
the steam. The solids in the feedwater used for attemperation should be in the
same range as the final steam purity desired, which could be as low as
30–100ppb. If solids are deposited inside the superheater, the tubes can
become overheated, particularly if operated at high loads and high heat flux
conditions. The convective superheaters are generally oversized at 100% load as
explained earlier. The quantity of water spray is larger at higher load. In the
radiant design, the steam temperature remains nearly flat over the load range
becausetheradiantcomponentofenergyincreasesatlowerloadsanddecreasesat
higher loads. Thus many radiant superheaters do not use a two-stage design.
However, reviewing other concerns such as possible overheating of tubes and
higher tube wall temperatures, the choice is left to the user.
Whendemineralizedwaterisnotavailable,aportionofthesaturatedsteam
fromthedrumistaken andcooled inaheatexchanger,preheatingthefeedwater
asshowninFig.3.18.Thecondensedwateristhensprayedintotheattemperator
betweenthetwostagesofthesuperheater.Often,inordertobalancethepressure
drops in the two parallel paths, a resistance is introduced into each path or the
exchanger is located vertically up, say 30–40ft above the boiler, to provide
additional head for the spray water control valve operation.
Spraying downstream of the superheater for steam temperature control is
notrecommended,becausethesteamtemperatureatthesuperheaterexitincreases
with load, thus increasing the superheater tubewall temperature, which can lead
totubefailures.Forexample,if800 Fisthefinalsteam temperaturedesired,the
(cid:2)
steam temperature at the superheater exit may run as high as 875–925 F, which
(cid:2)
will diminish the life of the tubes overa period of time. Also, thewater droplets
Copyright © 2003 Marcel Dekker, Inc.

may not evaporate completely in the piping and the steam turbine could end up
with water droplets and the solids present in the water, leading to deposits on
turbine blades.
Design Aspects
Figures 3.19a and 3.19b show an inverted loop superheater commonly used in
packaged boilers, and Fig. 3.19c shows a horizontal tube design with vertical
headers. Superheaters operate at high tube wall temperatures; hence their design
should be carefully evaluated. The convective superheater design located behind
several rows of screen section operates at lower tube wall temperatures than the
radiant design, though the steam temperatures may be the same. Figure 3.20
showstheresultsfromacomputerprogramforasuperheaterlocatedverycloseto
the furnace section and beyond several rows of screen tubes.
Optionashowstheresultsforapackagedboilergenerating150,000lb=hof
steam at 650psig when a 14-row screen section is used. The gas temperature
entering the superheater is 1628 F. For the steam temperature of 758 F, the
(cid:2) (cid:2)
superheater tube wall temperature is 856 F. The surface area used is 1833ft2.
(cid:2)
Inoptionb,anine-rowscreensectionisused.Thegastemperatureentering
the superheater is 1801 F. The superheater tube wall temperature is 882 F.
(cid:2) (cid:2)
However, owing to the higher log-mean temperature difference, the surface
area required is smaller, namely 1466ft2. It can be shown, as discussed under
life estimation below, that the difference in the life of the superheater for a 26 F
(cid:2)
difference for alloy steel tubes such as T11 can be several years. By the same
token, one may wonder about the life of the radiant design with a gas inlet
temperatureof 2187 F.Tubesizes aretypically 1.5–2in.OD, and materials used
(cid:2)
rangefromT11,T22,andT91tostainlesssteels,dependinguponsteamandtube
walltemperatures.Generally,baretubesareused;however,Ihavedesignedafew
packaged boilers, which are in operation in gas-fired boilers, using finned
superheaters to make the design compact.
Steam velocity inside the tubes ranges from about 50ft=s at high steam
pressure (say 1000–1500psig) to about 150ft=s at low pressure (150–200psig).
The turndown conditions and maximum tube wall temperatures determine the
number of streams used and hence the steam pressure drop. In inverted loop
superheaters, the headers are inside the gas path and are therefore protected by
refractory. A few evaporator tubes are provided in the superheater region to
ensure that steam blanketing does not occur at the mud drum and that steam
bubbles can escape from the mud drum to the steam drum.
Flowdistributionthroughtubesisanotherconcernwithsuperheaterdesign.
If long headers are used, multiple inlets can reduce the nonuniformity in steam
flow distribution through the tubes as shown in Fig. 3.21. Inlet and exit
connections from the ends of headers should be avoided because they can
Copyright © 2003 Marcel Dekker, Inc.

FIGURE3.19a Inverted loopsuperheater arrangement. (Courtesyof ABCOIndustries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.19b An inverted loop superheater. (Courtesy of ABCO Industries,
Abilene, TX.)
result in flow distribution problems. In arrangement 1, the inlet and exit
connections are on opposite ends, causing the greatest difference in static
pressure at the ends of the headers, and should be avoided. Arrangement 2 is
better than 1 because the flow distribution is more uniform. However, arrange-
ment3ispreferred,becausethecentralinletandexitreducethedifferentialstatic
pressure values by one-fourth, so the flow maldistribution is minimal.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.19c Horizontal tube superheater arrangement. (Courtesy of ABCO
Industries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.20 Results from boiler program showing effect of screen section on superheater
performance. Optiona:More screen rows; optionb: fewerscreen rows.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.21 Flow nonuniformitydueto headerarrangements.
Two temperatures are of significance in the design of superheater tubes.
Oneisthetubemidwalltemperature,whichisusedtoevaluatethetubethickness
per ASME code. (The published ASME stress values have increased during the
lastfewyearsandthereforethelatestinformationonstressvaluesshouldbeused
in calculating the tube thickness.) The outer wall temperature determines the
maximum allowable operating temperature, sometimes known as the oxidation
limit. Table 3.6 gives typical maximum allowable temperatures for a few
materials.
One can vary the tube thickness to handle the design pressure, but if the
outermost tube temperature gets close to the oxidation limit, we have to review
TABLE3.6 MaximumAllowable Temperatures
Material Composition Temp( F)
(cid:2)
SA178A (erw) Carbonsteel 950
SA178C (erw) Carbonsteel 950
SA192 (seamless) Carbonsteel 950
SA210A1 Carbonsteel 950
SA210C Carbonsteel 950
SA213-T11 1.25Cr-0.5Mo-Si 1050
SA213-T22 2.25Cr-1Mo 1125
SA213-T91 9Cr-1Mo-V 1200
SA213-TP304H 18Cr-8Ni 1400
SA213-TP347H 18Cr-10Ni-Cb 1400
SA213-TP321H 18Cr-10Ni-Ti 1400
SB407-800H 33Ni-21Cr-42Fe 1500
Copyright © 2003 Marcel Dekker, Inc.

the design. In large superheaters, different materials and tubes of different sizes
may be used at different sections, depending on the tube midwall and outer wall
temperatures. In all these calculations one has to consider the nonuniformity in
gas flow, gas temperature across the cross section, and steam flow distribution
throughthetubes.Becauseoftheirshorterlengths,afewtubescouldhavehigher
flow and starve the longer tubes.
Life Estimation
Highalloysteeltubesusedinsuperheatersandreheaters,unlikecarbonsteel,fail
by creep rupture. Creep refers to the permanent deformation of tubes that are
operated at high temperatures. Carbon steel tubes operate in the elastic range
whereallowablestresses arebased onyield stresses, whereas alloy tubes operate
inthecreep-rupturerange,whereallowablestressesarebasedonrupturestrength.
Thelifeofsuperheatertubesisanimportantdatumthathelpsplantengineersplan
tube replacements or schedule maintenancework. When a new superheater tube
is placed in service, it starts forming a layer of oxide scale on the inside. This
layer gradually increases in thickness and also increases the tube wall tempera-
ture.Therefore,topredictthelifeofthetubes,informationonthecorrosionorthe
formation of the oxide layer is necessary. The corrosion of oxide formation also
reduces the actual thickness of the tubes and increases the stresses in the tubes
over time even if the pressure and temperature are the same. The data on oxide
formation were once obtained by cutting tube samples and examining them but
are now obtained through nondestructive methods. There are also methods to
relatetheoxidelayerthicknesswithtubemeanwalltemperaturesoveraperiodof
time.
Creep data are available for different materials in the form of the Larson
Miller parameter,LMP.ThisrelatestherupturestressvaluetotemperatureT and
the remaining lifetime t, in hours.
LMP T 460 20 logt
¼ð þ Þð þ Þ
Every tube inoperation hasanLMPvalue that increaseswith time. LMPcan be
related to stress values and the relationship then used to predict remaining life.
However, there are charts that givewhat is called the minimum and the average
rupture stress versus LMP, and one can compute different life times with the
differentvalues.Also,itcanbeseenthatevenafewdegreesdifference,say10 F
(cid:2)
in metal temperatures, can change the lifetime by a large amount, which shows
how complex and difficult it is to interpret the results. Figure 3.22 shows the
relationships between LMP and minimum rupture stress values for T11 and T22
materials.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.22 Larson–Miller parameters forT11and T22materials.
Example 7
AssumethatasuperheaterofT11materialoperatesat1000 Fandatahoopstress
(cid:2)
of 6000psi. What is the predicted time to failure? From Fig. 3.22, the LMP at
6000 is 36,800.
Solution: From the above equation, we can see that
36;800 1460 20 logt ; or t 160;500h
¼ð Þð þ Þ ¼
Ifatubehadoperatedatthistemperaturefor50,000h,itslifeconsumedwouldbe
50,000=160,500 0.31, or 0.69 of its life would remain. If after this period of
¼
50,000h, it operated at, say, 1020 Fand at the same stress level, then
(cid:2)
36;800 1480 20 logt ; or t 73;250h
¼ð Þð þ Þ ¼
andthenumberofoperatinghoursatthistemperaturewouldbe0.69 73,250
(cid:4) ¼
50,728h.
One can see from the above how sensitive these numbers are to tempera-
turesandstressvalues.Hencewehavetointerprettheresultswithcautionbacked
up by operational experience. Simplistic approaches to replacement of tube
bundlesarenotrecommended.Itshouldalsobenotedthatiftheaveragerupture
stress is used instead of the minimum value, the lifetimewould be much higher,
casting more uncertainty in these calculations.
Copyright © 2003 Marcel Dekker, Inc.

ECONOMIZERS
Economizers areusedasheat recoveryequipment inpackaged boilers insteadof
airheatersbecauseofNOxconcernsasdiscussedinChapter4.Theyarealsoless
expensive and have lower gas pressure drops across them. Economizers for gas
firing typically use serrated fins at four to five fins per inch. For distillate fuel,
about 4fins=in, solid fins are preferred. For heavy oil, bare tubes or a maximum
of 2–3fins=in.are used,depending upon thedirtiness ofthe fluegasand the ash
content of the fuel.
Economizers are generally of vertical gas flowand counterflow configura-
tion with horizontal tubes as shown in Fig. 3.23. The water-side velocity ranges
from3to7ft=s.Smallpackagedboilers,below40,000lb=hcapacity,usecircular
economizers that can be fitted into the stack. Another variation is the horizontal
gas flow configuration with vertical headers and horizontal tubes.
Generally,steamingintheeconomizerisnotaconcern,asdiscussedearlier.
Feedwatertemperaturesof230–320 Farecommon,dependingonaciddewpoint
(cid:2)
concerns. The feedwater is sometimes preheated in a steam–water exchanger if
the deaerator delivers a lower feedwater temperature than that desired to avoid
acid corrosion in the case of oil-fired boilers.
BOILER PERFORMANCE ASPECTS
Plantengineersareinterestedinknowinghowagivenboiler performsatvarious
loads. Thevariables affecting its performance are the fuel, amount of excess air,
FGRrate,andsteamparameters.Tables3.4and3.7showhowboilerperformance
varieswithloadongasandoilfiring.Figure3.24showstheresultsingraphform.
The following observations can be made:
1. Astheloadincreases,theboilerexitgastemperatureincreases.Thisis
due to the larger flue gas mass flow transferring energy to a given
heating surface. The water temperature leaving the economizer is
higher at loads owing to the higher gas temperature entering the
economizer. The approach point (difference between saturation and
water temperature entering evaporator) is lower at higher loads.
Steaming in the economizer is not a concern in steam generators
because the approach point is quite large at full load and increases at
lowerloads.Theratioofgasflowtosteamgenerationismaintainedat
1.2–1.3 at various loads. Hence the economizer does not absorb more
energy at low loads as in the case of HRSGs.
2. Theboilerefficiencyincreasesastheloadincreases,peaksatabout50–
70%ofload,thendropsoff.Thetwomajorvariablesaffectingtheheat
lossesarethecasingheatlossesandheatlossduetofluegases.Q6.24
discussesthiscalculation.Astheloadincreases,thefluegasheatlosses
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.23a Economizerin apackaged boiler. (Courtesy ofABCO Industries, Abilene, TX.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.23b Photo of an economizer. (Courtesy of ABCO Industries, Abilene,
TX.)
increase due to the higher exit gas temperature. The casing loss
decreases as a percentage but, as explained in Q6.24, in terms of
Btu=hitremainsthesamebecausetheevaporatoroperatesatsaturation
temperature, so heat losses in Btu=h are unaffected by boiler load
except if ambient temperature or wind velocity changes. Thus the
combination of these losses results in a parabolic shape for efficiency
as a function of load.
3. The steam temperature generally increases with load owing to the
convective nature of the superheater. If a radiant design were used, it
would decrease slightly at higher loads.
4. It may also be seen that the gas temperature leaving the evaporator
decreases as the load decreases. If an SCR is used between the
evaporator and the economizer, the gas temperature should be main-
tainedintherangeoftypically650–780 F;henceonemayhavetouse
(cid:2)
a gas bypass system to obtain a higher gas temperature at low loads.
Chapter 4 shows the arrangement of dampers to achieve this purpose.
5. Thesteamtemperatureonoilfiringislowerthanthatingasfiring.This
is due to the better absorption of energy from the oil flames in the
Copyright © 2003 Marcel Dekker, Inc.

TABLE3.7 Boiler Performance—Oil Firing
Load(%)
25 50 75 100
Boiler duty,MMBtu=h 28.94 58.26 89.03 118.71
Excess air,% 30 15 15 15
Fuelinput,MMBtu=h 32.98 65.95 101.25 135.9
Heatrel rate,Btu=ft3h 15,266 30,531 46,875 62,918
Heatrel rate,Btu=ft2h 28,188 56,376 86,554 116,176
Steamflow,lb=h 25,000 50,000 75,000 100,000
Steamtemp, F 694 710 750 750
(cid:2)
Economizerexit water 324 329 350 368
temp, F
(cid:2)
Boiler exitgastemp, F 526 588 671 748
(cid:2)
Economizerexit gas 254 269 296 325
temp, F
(cid:2)
Airflow, lb=h 32,064 56,728 87,096 116,903
Fluegas,lb=h 33,731 60,061 92,212 123,771
Drygasloss, % 3.95 3.83 4.36 4.95
Airmoisture loss,% 0.1 0.1 0.11 0.13
Fuelmoistureloss,% 6.58 6.62 6.69 6.77
Casing loss,% 1.2 0.6 0.4 0.3
Margin,% 0.5 0.5 0.5 0.5
Efficiency,% HHV 87.67 88.35 87.93 87.35
Efficiency,% LHV 93.67 94.39 93.95 93.33
Furnace backpressure, 0.8 2.45 5.81 10.76
in.WC
Steampressure 500psig,oilfiring.HHV 19,727;LHV 18,463Btu=lb.Fluegasanalysis
¼ ¼ ¼
(vol%):CO 10:76,H O 11:57,N 73:63,O 2:51.
2¼ 2 ¼ 2¼ 2¼
FIGURE 3.24 Boiler performanceversusload.
Copyright © 2003 Marcel Dekker, Inc.

furnace, which results in a lower furnace exit gas temperature and
lowergas temperatureatthesuperheater inoilfiring. Hencethesteam
temperature is lower. However, if we wanted to maintain the same
steamtemperatureonbothoilandgasfiring,wewouldhavetosizethe
superheatersothatitmakesthesteamtemperatureintheoil-firingcase
and then control it in gas firing by attemperation.
Performance Without an Economizer
IfwelookatTable3.4forperformanceofaboilerat,say,100%load,weseethat
thegastemperatureleavingtheevaporatoris739 Fandleavingtheeconomizerit
(cid:2)
is327 F.Nowiftheeconomizerisremovedfromservice,canweassumethatthe
(cid:2)
exit gas temperature will still be 739 F? The answer is No, for the following
(cid:2)
reasons:
1. Theboilerefficiencydrops significantly,by atleast(7397327)=40
¼
10.3%. Hence the efficiency will be at best 83.66710.3 73.36%
¼
HHV.
2. The boiler fuel input increases by this ratio. The new heat input is
(118.71=0.7336) 161.8MM Btu=h versus (118.71=0.8366)
¼ ¼
141.9MM Btu=h. Hence the flue gas flow, which is proportional to
heat input, will be higher by 161.8=141.9 1.14 or 14%, or about
¼
1.14 125,246 142,800lb=h.
(cid:4) ¼
3. The furnace heat input and heat release ratewill also be higher due to
thelowerefficiencyandhencehigherfurnaceexitgastemperature.The
combination of higher gas flow and higher gas inlet temperature to
the convection bank will increase the exit gas temperature from the
evaporator from 739 F to a slightly higher value. Therefore another
(cid:2)
iterationwillhavetobeperformedtoarriveattheexitgastemperature
basedontherevisedefficiencyandfuelinput.Theexitgastemperature
could be close to 770–780 F.
(cid:2)
4. Becauseofthelargerfluegasflowandhigheroperatingtemperaturein
theevaporatorbank,thegaspressuredropwillalsobehigher;itcould
beasmuchasintheearliercaseorevenmore.Hence,theassumption
thatremovingtheeconomizerwillreducethetotalgaspressuredropis
incorrect. One has to do the performance calculations before arriving
at any conclusion.
Why the Economizer Does Not Steam in Packaged Boilers
Unlike HRSGs, packaged boilers, fortunately, do not have to dealwith the issue
of steaming. The reason is illustrated in Fig. 3.25, which shows the temperature
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.25 Economizer temperaturepick-upin boiler versusHRSG.
profilesoftheeconomizeroftheboilerwhoseperformanceisgivenaboveandan
HRSG.
Because of the small ratio of gas to water flow in packaged boilers, the
temperature drop of the flue gas has to be large for a given water temperature
increase. If the water temperature increases by, say, 145 F, the gas temperature
(cid:2)
drop is given by
1:23 0:286 T T 145
(cid:4) (cid:4)ð 1(cid:3) 2Þ¼
or
T T 412 F
1(cid:3) 2 ¼ (cid:2)
whereas in an unfired HRSG, the gas temperature drop of only 105 F accom-
(cid:2)
plishes a water temperature increase of 248 F! Thus it is easy for the water to
(cid:2)
reach saturation temperature in HRSGs. Thus in spite of the fact that the gas
entering temperature is quite large in packaged boilers (due to the high furnace
exit gas temperature), the water temperature does not increase significantly.
If the water temperature approach is large at 100% load, it will be even
larger at partial loads, because the gas temperature entering the economizer
decreases.
Performance with Oil Firing
Steam generators have been fired with both distillate fuel oils and residual oils.
Thedesignoftheboilerdoesnotchangemuchfordistillateoilfiringcomparedto
gasfiring.Thefoulingfactorusedismoderatelyhigher,0.003–0.005ft2h F=Btu,
(cid:2)
comparedto0.001ft2h F=Btuforgasfiring;rotarysootblowerslocatedateither
(cid:2)
endof theconvectionsectionareadequate forcleaning the surfaces for distillate
oilfiring.Withheavyfueloils,retractablesootblowersarerequired.Economizers
Copyright © 2003 Marcel Dekker, Inc.

alsouserotaryblowersinoil-firedapplications.Solidfintubesofafindensityof
three or four per inch may be used if distillate fuels are used, but if heavy oil is
fired it is preferable to use bare tubes or at best 2–3 fins=in. The emissions of
NOxwillbehigheronthebasisoffuel-boundnitrogen,becauseitcancontribute
to nearly 50% of the total NOx. Fluegas recirculation has less effect on NOx in
oil firing than in gas firing.
With residual fuel oil firing, there are several aspects to be considered.
1. Hightemperaturecorrosionduetotheformationofsaltsofsodiumand
vanadium in the ash has been a serious problem in with heavy oil
boilersfired.Thefurnaceexitregionisapotentiallydirtyzoneproneto
deposition of molten ash on heating surfaces. The use of superheaters
in such regions presents serious performance concerns. Retractable
steam soot blowers are required, with access lanes for cleaning. Tubes
should preferentially be widely spaced at the gas inlet region to avoid
bridging of tubes by slag. Vanadium content in fuel oil ash should be
restricted to about 100ppm to minimize corrosion potential.
2. Superheater materials used in heavy oil firing applications should
consider the high temperature corrosion problems associated with
sodium and vanadium salts. The metallurgy of the tubes should be
T22 or even higher if the tube wall temperature exceeds 1000 F. A
(cid:2)
large corrosion allowance on tube thickness is also preferred. This is
yet another reason for preferring a convective superheater design to a
radiant superheater.
3. Steam temperatures with oil firing will be lower than on gas firing as
discussed above.
4. Furnace heat flux will be higher in oil firing than in gas firing.
Therefore one has to check the circulation and the furnace design.
5. One of the problems with firing a fuel containing sulfur is the
formation of sulfur dioxide and its conversion to sulfur trioxide in
thepresenceofcatalystssuchasvanadium,whichispresentinfueloil
ash. Sulfur trioxide combines with water vapor to form sulfuric acid
vapor, which can condense on surfaceswhosetemperature falls below
the acid dew point. Q6.25 illustrates the estimation of dew points of
various acid vapors. Sulfuric acid dew points can vary from 200 to
270 F depending on the amount of sulfur in the fuel. If the tube wall
(cid:2)
temperature of the economizer or air heater falls below the acid dew
point, condensation and hence corrosion due to the acid vapor are
likely. I have seen a few specifications where a parallel flow arrange-
ment was suggested for the economizer to minimize acid dew point
corrosion. Because the feedwater temperature governs the tube wall
temperature and not the flue gas temperature, only maintaining a high
Copyright © 2003 Marcel Dekker, Inc.

watertemperatureavoidsthisproblem,asshowninQ6.25c.Onecould
usesteamtopreheatthefeedwaterorusethewaterfromtheexitofthe
economizer to preheat the incoming water in a heat exchanger.
Experience and research show that acid corrosion potential is maxi-
mum notat the dewpoint but at slightly lower values, about 15–20 C
(cid:2)
belowthedewpoint.Henceonemayuseafeedwatertemperatureeven
slightly lower than the dew point of the acid vapor in order to recover
more energy from the waste gas stream. In waste heat boiler econo-
mizers, other acid vapors such as hydrochloric acid or hydrobromic
acidmaybepresent.Thedewpointsofthesearemuchlowerthanthat
of sulfuric acid, as discussed in Q6.25, so care must be taken in the
design of economizers or air heaters in heat recovery applications.
Table 3.7 shows the boiler performance with distillate oil firing. The
efficiency on LHV basis is nearly the same as for gas firing, but on HHV basis
thereisadifference.Thefluegasanalysiswith15%excessairisshown.Theflue
gaseshavelesswatervaporbutmorecarbondioxidethanfluegasesfromnatural
gas combustion.
Effect of FGR on Boiler Performance
Flue gas recirculation is widely used as a method of NOx control because it
reduces the flame temperature and thus lowers NOx formation as discussed in
Chapter4.TheeffectofFGRonboilerperformanceisquitesignificant.Notonly
is the gas temperature profile across the boiler different, but the steam tempera-
ture and gas pressure drop are also affected.
Table3.8showstheperformanceofa150,000lb=hboilerwithandwithout
FGR. The following points may be noted:
1. The flue gas quantity increases with FGR; hence the backpressure
increases at all loads.
2. ThesteamtemperatureishigherwithFGRinboth100%and50%load
cases, but the difference is greater at low loads.
3. The furnace exit gas temperature is lower with FGR, and the gas
temperatureacrossthesuperheaterishigherat50%loadthanat100%.
Thus load plays a big role in the temperature profiles.
4. The efficiencynaturally drops due to the higher stack gas temperature
at both 100% and 50% loads.
Relating FGR and Oxygen in the Wind-Box
Fluegasrecirculationaffectstheoxygeninthewind-boxbydilutingit.Onemay
measure the oxygenvalues to evaluate the FGR rate used.
Copyright © 2003 Marcel Dekker, Inc.

TABLE3.8 Effect ofFGR onBoilerPerformance
Load(%)
100 100 50 50
Excess air,% 15 15 15 15
FGR,% 0 15 0 15
Combustion,temp, F 3,230 2,880 3,230 2,880
(cid:2)
Furnace exittemp, F 2,350 2,188 2,007 1,956
(cid:2)
Gas tempto superheater, F 1,695 1,630 1,323 1,334
(cid:2)
Gas tempto evaporator, F 1,250 1,240 944 973
(cid:2)
Gas tempto economizer, F 630 645 543 555
(cid:2)
Gas templeaving 300 315 263 270
economizer, F
(cid:2)
Fluegasflow, lb=h 185,500 215,000 88,900 104,000
Efficiency,% HHV 84.26 83.9 85.1 84.9
Steamflow,lb=h 150,000 150,000 75,000 75,000
Steamtemp, F 748 756 686 711
(cid:2)
Economizerexit water 338 355 318 333
temp, F
(cid:2)
Boiler backpressure, 6.2 7.8 2.0 2.5
in.WC
Feedwatertemp, F 228 228 228 228
(cid:2)
Fuel:standardnaturalgas;1%blowdown;steampressure 650psig.
¼
Example 8
Aboilerfiringnaturalgasat15%excessairuses119,275lb=hofcombustionair,
and about 14,000lb=h of flue gases is recirculated. Determine the oxygen levels
inthewind-box.Letusassumethattheairisdryandis77%byweightnitrogen
and 23% oxygen. Then the amount of nitrogen in air 0.77 119,275
¼ (cid:4) ¼
91,842lb=h, and that of oxygen 27,433lb=h.
¼
The flue gas analysis (vol%) is CO 8:29;H O 18:17;N 71:07,
2 ¼ 2 ¼ 2 ¼
and O 2:47.
2 ¼
To convert to percent by weight (wt%) basis, first obtain the molecular
weight:
MW 8:29 44 18:17 18 71:07 28 2:47 32 =100 27:61
¼ð (cid:4) þ (cid:4) þ (cid:4) þ (cid:4) Þ ¼
%CO 8:29 44=27:61 13:21
2 ¼ (cid:4) ¼
Similarly, H O 11:84wt%;N 72:07, and O 2:88.
2 ¼ 2 ¼ 2 ¼
Copyright © 2003 Marcel Dekker, Inc.

The individual constituents in the mixture of 14,000 119,275
þ ¼
133,275lb=h of gases are
CO 0:1321 14;000 1849:4lb=h
2 ¼ (cid:4) ¼
H O 0:1184 14;000 1658lb=h
2 ¼ (cid:4) ¼
N 91;843 0:7207 14;000 101;922lb=h
2 ¼ þ (cid:4) ¼
O 27;433 0:0288 14;000 27;836lb=h
2 ¼ þ (cid:4) ¼
Converting this to percent by volume basis as we did earlier, we have
CO 0:9vol%;H O 1:98;N 78:37;andO 18:75
2 ¼ 2 ¼ 2 ¼ 2 ¼
SOOT BLOWING
Soot blowing is often resorted to in coal-fired or heavy oil–fired boilers. In
packaged boilers, both steam and air have been used as the blowing media, and
bothhavebeeneffectivewithheavyoilfiring.Rotaryblowersaresometimesused
with distillate oil firing. Steam-blowing systems must have a minimum blowing
pressure of 170–200psig to be effective. The steam system must be warmed up
priortoblowingtominimizecondensation.Thesteammustbedry.Increasingthe
capacityofasteamsystemiseasierthanincreasingthatofanairsystem.Withan
air system, the additional capacity of the compressor must be considered. Also,
because steam hasahigherheat transfer coefficientthan air,moreair isrequired
for cooling the lances in high gas temperature regions compared to steam.
Moisturedropletsinsteamcancauseerosionoftubes,andoftentubeshieldsare
required to protect the tubes. The intensity of the retractable blower jet is more
than that of the rotary blower jet, and its blowing radius is larger, thus cleaning
moresurfacearea.However,onemustbeconcernedabouttheerosionorwearon
the tubes.
Sonic cleaning has been tried on a few boilers. In this system, low
frequency high energy sound waves are produced when compressed air enters
a sound generator and forces a diaphragm to flex. The resulting sound waves
cause particulate deposits to resonate and dislodge from the surfaces. Once
dislodged, they are removed by gravity or by the flowing gases. Typical
frequencies range from 75 to 33Hz. Sticky particles are difficult to clean. The
nondirectional nature of the sound wavesminimizes accumulation in blindspots
wheresootblowersareineffective.Pipingworkisminimal.Sonicblowersoperate
on plant air at 40–90psi and sound off for 10s every 10–20min.
Copyright © 2003 Marcel Dekker, Inc.

WATER CHEMISTRY, CARRY OVER, AND STEAM PURITY
Goodwaterchemistryisimportantforminimizingcorrosionandtheformationof
scaleinboilers.Steam-sidecleanlinessshouldbemaintainedinwatertubeaswell
as fire tube boilers. Plant engineers should do the following on a regular basis:
1. Maintain proper boiler water chemistry in the drum according to
ABMA or ASME guidelines by using proper continuous blowdown
rates. The calculation procedure for the blowdown rate based on
feedwater and boiler water analysis is given in Q5.17.
2. Ensure that the feedwater analysis is fine and that there are no sudden
changes in its conductivity or solids content.
3. Check steam purity to ensure that there are no sudden changes in its
value. A sudden change may indicate carryover.
4. Watch superheated steam temperatures, particularly in boilers with
large load swings. If slugs of water get carried into the steam during
large load swings, the deposits are left behind after evaporation,
potentially leading to tube failure. An indication of slugging, which
is likely in boilers with small drums, is a sudden decrease in steam
temperatures due to entrainment of water in the steam.
Intheprocessofevaporatingwatertoformsteam,scaleandsludgedeposits
formontheheatedsurfacesofaboilertube.Thechemicalsubstancesinthewater
concentrate in a film atthe evaporation surface;thewater displacing the bubbles
ofsteamreadilydissolvesthesolublesolidsatthepointofevaporation.Insoluble
substancessettleonthetubesurfaces,formingascaleandleadingtoanincrease
in tubewall temperatures. Calcium bicarbonate, for example, decomposes in the
boiler water to form calcium carbonate, carbon dioxide, and water. Calcium
carbonate has limited solubility and will agglomerate at the heated surface to
form a scale. Blowdown helps remove some of the deposits. Calcium sulfate is
more soluble than calcium carbonate and will deposit as a heat-deterrent scale.
Most scale-forming substances have a decreasing solubility in water with an
increase in temperature.
In boilers that receive some hardness in the makeup water, deposits are
generally compounds of calcium, sulfate, silica, magnesium, and phosphate.
Depending on tube temperatures and heat flux and the solubility of these
compounds as a function of temperature, these compounds can form deposits
inside the boiler tubes. These scales, along with sludge and oils, form an
insulatinglayerinsidetubesatlocationswheretheheatfluxisintense.Alkalinity
andpHofthewateralsoaffectthescaleformation.Saltssuchascalciumsulfate
and calcium phosphate deposit preferentially in hot regions. Boilers are consid-
eredgenerallycleanifthedepositsarelessthan15mg=cm2.Boilershavingmore
than 40mg=cm2 are considered very dirty. The least soluble compounds deposit
Copyright © 2003 Marcel Dekker, Inc.

first when boiling starts. Calcium carbonate deposits quickly, forming a white
friable deposit. Magnesium phosphate is a binder that can produce very hard,
adherentdeposits.Insolublesilicatesarepresentinmanyboilers.Thepresenceof
sodium hydroxide, phosphate, or sulfate may be considered proof that complete
evaporation has occurred in the tubes, because these are easily soluble salts.
Sludge or easily removable deposits accumulate at the bottom of the tubes
in the mud drum and should be removed by intermittent blowdown, generally
oncepershift.Basedonconductivityreadings,thefrequencymaybeincreasedor
decreased. Continuous blowdown is usually taken from the steam drum a few
inchesfromabovethewaterline,wheretheconcentrationofsolidsisthehighest.
Any boiler water treatment program should be reviewed with a water
chemistry consultant, because this program can vary on a case-to-case basis.
Generally theobjectiveistoadd chemicals topreventscale formation caused by
feedwaterhardnessconstituentssuchascalciumandmagnesiumcompoundsand
toprovide pHcontrol intheboiler to enhance maintenance ofa protectiveoxide
film on boiler water surfaces. There are methods such a phosphate-hydroxide,
coordinated phosphate, chelant treatment, and polymer treatment methods. In
medium and low pressure boilers, all these methods have been used.
Carryover of impurities with steam is a major concern in boilers having
superheaters and also if steam is used in a steam turbine. Carryover results from
bothineffectivemechanicalseparationmethodsandvaporouscarryoverofcertain
salts. Vaporous carryover is a function of steam density and can be controlled
only by controlling the boiler water solids, whereas mechanical carryover is
governedbytheefficiencyofthesteamseparatorsused.Totalsolidscarryoverin
steam is the sum of mechanical and vaporous carryover of impurities.
The steam purity requirements for saturated steam turbines are not
stringent. Because the saturated steam begins to condense on the first stage of
the turbine, water-soluble contaminants carried with the steam do not form
deposits.Unlessthesteamiscontaminatedwithsolidparticlesoracidicgases,its
purity does not significantly affect the turbine performance. However, there can
be erosion concerns due towater droplets moving at high speeds.
Withsuperheatedsteam,steampurityiscriticaltotheturbine.Saltsthatare
solubleinsuperheatedsteammaycondenseorprecipitateandadheretothemetal
surfacesasthesteamiscooledwhenitexpands.Depositionfromsteamcancause
turbine valves to stick. Reduced efficiency and turbine imbalance are the other
concerns. Deposition and corrosion occur in the ‘‘salt zone’’ just above the
saturation line and on surfaces in the wet steam zone. The solubility of all low
volatility impurities such as salts, hydroxides, silicon dioxide, and metal oxides
decreasesassteamexpandsintheturbineandislowestatthesaturationline.The
moisture formed has the ability to dissolve most of the salts and carry them
downstream. The critical region for deposition in turbines operating on super-
heated steam is the blade row located just upward of the Wilson line.
Copyright © 2003 Marcel Dekker, Inc.

Mechanical carryover results from entrainment of small droplets of boiler
water in the separated steam. Because the entrained water droplets contain the
sameconcentrationandproportionsofsolidsasintheboilerwater,thesteamwill
also contain these solids as a function of its moisture content.
Foaming in the boiler water will also result in carryover. Common causes
are excessive boiler water solids, excessive alkalinity, or the presence of organic
matter such as oil. Continuous blowdown should be done to maintain the boiler
water concentration below the ASME=ABMA levels.
Unlike mechanical carryover, vaporous carryover is selective because it
depends on the solubility of the salts in steam. Silica is an example of a
contaminant that has this tendency, particularly at high steam pressures, above
700psig. Boiler water of a higher pH helps minimize the carryover. Drum
internals (Fig. 3.26) serve to remove moisture from the steam as it leaves the
drumandentersthesuperheater.Generallythebellypancollectsthesteam–water
mixture from the riser tubes and directs it inside the drum, where a chevron
separator consistingof multiplevaneswith tortuous paths separates the moisture
from the steam. The mass flow of the mixture is the circulation ratio times the
steam generation. Hencethebelly panwidth must besized tohandle the flowof
this mixture. The steam purity required depends on the application. Saturated
steamusedinprocessheatingapplicationscanhavealargecarryoverofsolids,as
much as 3–5ppm. Drum internals need not be elaborate in these cases. A few
steam turbine suppliers demand steam purity in the range of parts per billion for
superheated steam, whereas some accept even 100ppb total dissolved solids.
FIGURE 3.26 Arrangement ofsteam drum internals.
Copyright © 2003 Marcel Dekker, Inc.

Restrictionsarealsoplacedonsodiumandsilicainsteam.Typicalsilicalevelsare
20ppb.BymaintainingproperboilerwaterchemistryassuggestedinQ5.17,per
ABMA and ASME, one can ensure that the steam purity is acceptable. Main-
taining an alkaline condition (pH about 10–11.5) in the boiler water minimizes
corrosion in the boiler; however, the alkalinity should also not exceed 700ppm
CaCO . Above this level chemical reactions liberate CO into steam, which
3 2
results in the corrosion of steam and return lines.
As far asthefeedwater isconcerned, proper deaerationand theremovalof
oxygenbychemicalmethodshelps. Demineralized water isrequiredif it isused
for attemperation to control the steam temperature. Once-through steam genera-
tors and HRSGs need zero solids because complete evaporation of water occurs
insidethetubes.Dissolvedoxygenisthefactormostresponsibleforthecorrosion
of steel surfaces in contact with water. Oxygen should be less than 5–7ppb to
minimize these concerns. Chemicals such as hydrazine or sodium sulfite are
added to minimize oxygen corrosion.
Scaleformationcanaffectthetubewalltemperaturesinfiretubeaswellas
water tube boilers; as discussed above.
A few plants do not spend sufficient money on water treatment facilities.
Table3.9showshowalargeamountofblowdownincreasesthecostofoperation
andwhyitpaystoinvestinagoodwatertreatmentsystem.Corrosionandsteam
purity problems result in additional costs, which cannot be quantified because
they lead to unscheduled maintenance. The additional amount of fuel fired to
generate the same amount of steam is significant over a period of time. I have
seen blowdown on the order of 15–20% in a few refineries.
TABLE3.9 Costof Blowdowna
Steamflow,lb=h 100,000 100,000
Steampressure,psig 300 850
Steamtemperature, F Sat 850
(cid:2)
Feedwatertemperature, F 230 230
(cid:2)
Blowdown, % 2 10 2 10
Boiler duty,MMBtu=h 100.8 102.4 123.1 125.7
Heatinput, MMBtu=h 121.5 123.4 148.4 151.5
Flashsteam recovery,% 20 33
Additional cost,$=y 36,480 49,850
aBoilerefficiency 83%HHV;fuelcost $3=MMBtu.Operatingfor8000h=y.
¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

FIRE TUBE BOILERS
Packaged fire tube boilers (Fig. 3.3) generate low pressure saturated steam,
generally below 300psig. Above this pressure, the thickness of the corrugated
centralfurnace(referredtoasMorrisonpipe)becomeslargeranditisdifficultto
make the corrugations. The corrugations help to reduce the thickness of the
furnace,whichoperatesatahighmetaltemperaturebecauseitcontainstheflame.
The corrugations also help to handle the thermal expansion differences between
thefurnaceandthesmallertubesinthesecondandthirdpasses,whichoperateat
lowertubewalltemperatures.Notethatthetubesheetsarefixedattheendsofthe
tubes,andwithoutthisflexibilitylargestresseswouldbeintroducedintothetube
sheets and the tubes. The thickness of a tube subjected to external pressure is
higher than that subjected to internal pressure, as shown in Table 2.2. Fire tube
boilersaretypicallyratedinboilerhorsepower(BHP);Q5.08showshowonecan
relate BHP to steam generation. Often these boilers do not need an economizer,
becausetheexitgastemperature,duetothelowpressureofsteam,isaround400–
450 F. However, an economizer is used when high efficiency is desired.
(cid:2)
Thenumberofpassesonthetubesidedependsuponthesupplier.Typically
three to four passes are used. In the wetback design the turnaround section is
immersed in the water, so the hot gases leaving the furnace do not contact the
refractoryasinthedrybackdesign,whichislessexpensivetobuild.However,the
wetbackdesignhasfewerproblemswithrefractorymaintenancethanthedryback
design.Wetorwater-cooledreardoorsarealsoavailablethatminimizerefractory
maintenance concerns in dryback boilers. The typical gas temperature at the
furnace exit is about 2000–2200 F, hence the turnaround section with refractory
(cid:2)
often requires maintenance.
Oilandgaseousfuelsaregenerallyfiredinpackagedfiretubeboilers.Solid
fuels such as wood shavings have also been fired. The boiler capacity has been
limited to about 80,000lb=h, because it becomes more expensive to build these
boilers as shop-assembled units as the capacity increases. The heat transfer
coefficient with gas flowing inside the tubes is generally less than when it flows
outside the tubes; hence fire tube boilers are large compared to water tube
designs. They are considered economical below 50,000lb=h of steam. It is
generallydifficulttoinstall asuperheaterinthese designs.NOxcontrol methods
suchasfluegasrecirculationortheuseoflow-NOxburnershavealsobeenused
with these boilers. Due to the large amount of water inventory compared to
equivalent water tubedesigns,these boilers takealittlelonger tostartup.Steam
purityisgenerallypoor,becausethesteamismainlyusedinheatingapplications
where steam purity is not a concern and therefore no drum internals are used.
Oftensingle-shellfiretubeboilerssuchasthoseshowninFig.3.3generatesteam
with 3–15ppm purity. Elevated drums have been used on fire tube boilers to
Copyright © 2003 Marcel Dekker, Inc.

obtain steam with avery high purity if required. The design would be similar to
the elevated drum waste heat boiler discussed in Chapter 2.
When it comes to generating superheated steam, a water tube boiler has
moreoptions,becausethesuperheatercanbeplacedwithinabankoftubesorin
theradiantsectionorbeyondtheconvectionsectionasdiscussedabove.However,
in the case of a fire tube boiler, the options are limited; a possible location is
betweenthetubepasses,butthegastemperaturesthereareeithertoohighortoo
low, making it difficult to design a reasonable superheater. Therefore, packaged
fire tube boilers generally generate saturated steam.
Thewaterinventoryinafiretubeboilerisgenerallylarger,thusrequiringa
longer start-up period. Heating surfaces can be cleaned by using retractable or
rotaryblowersatanylocationinawatertubeboiler,whereasinafiretube,access
forcleaningisavailableeitherattheturnaroundsectionoratthetubesheetends.
AIR HEATERS
Air heaters are used in a few waste heat boilers for preheating combustion air.
Incineration plants and reformer furnaces also use preheated air. Decades ago
theywereusedinboilersthatfiredsolid,liquid,andgaseousfuels.However,with
NOxlimitationsforallkindsoffuels,theyarenowusedonlyifthecombustionof
thefuelwarrantsit.Ifthegaseousfuelhasalowheatingvalueorifthesolidfuel
has a significant amount of moisture, then hot air is required for drying the fuel
and also to ensure combustion with a stable flame. A gas togas heater, whichis
similar to an air heater, is also used in incineration heat recovery plants where
waste fuel is heated by the flue gases from the incinerator before entering the
thermalorcatalyticincinerator.Ingas-firedorliquidfuel–firedpackagedboilers,
air heaters are not generally used. An economizer is the main heat recovery
equipment.Thereareseveraltypesofairheaters,includingtubular,regenerative,
andheatpipes,thelatterbeingarecentdevelopment.Inalltheseheatexchangers,
air is preheated by using hot flue gases from the boiler or heater. The flue gases
could flow outside or inside the tubes. If the flue gases contain dust or ash
particles, it is preferable to make them flow inside the tubes so that the shell or
casingisnotfouled,becauseitismoredifficulttocleantheexteriorsurfaces.The
air takes a multipassroute outsidethetubes asshowninFig. 3.27.Q8.28 shows
the sizing procedures.
One of the concerns with air heaters is low temperature corrosion at the
coldend.Thetubewalltemperatureortheplatetemperatureatthecoldendfalls
belowtheaciddewpointofthefluegasesiftheincomingairtemperatureislow.
Also, tube wall and plate temperatures are lower at lower loads because of their
low heat transfer coefficients. Steam is often used to increase the incoming air
temperature and thus mitigate this concern.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 3.27 (a) Rotaryregenerativeair heater.(b) Tubularairheater.
There are two types of regenerative air heaters, one in which the heater
matrixrotates,andoneinwhichtheconnectingairandfluegasductworkrotate.
The first type is called the Ljungstrom air heater. The energy from the hot flue
gases is transferred to a slowly rotating matrix made of enamel or alloy=carbon
steel material, which absorbs the heat and then transfers it to the cold air as it
rotates. The elements are contained in baskets, which makes cleaning or
replacement easier. Regenerative air heaters are more compact than tubular air
heaters,whichareheavyandoccupyalotofspace.Thegas-andair-sidepressure
drops are high in both these types of air heaters, adding to the fan power
consumption.Duetothelowheattransfercoefficientsofairandfluegasesanda
low log-mean temperature difference (LMTD), surface area requirements are
largeforairheaters.However,alotofsurfaceareacanbepackedintoeachbasket
of a regenerative air heater, so they are more compact than the tubular heater.
Oneoftheproblemswithregenerativeairheatersistheleakageofairfrom
the flue gas side that affects the power consumption and efficiency of the fan.
Thoughtheleakagemaybelow,ontheorderof5–10%dependingupontheseal
design,itissignificantinlargeplants.Intubularairheaters,failureofthetubesor
expansionjointscouldresultinleakagefromtheairsidetothegasside,butthis
is minimal.
Copyright © 2003 Marcel Dekker, Inc.

In regenerative air heaters, corrosion concerns are addressed by using
enamel or corten materials at the cold end. In the case of tubular air heaters, the
entire section of tubes may haveto be replaced. In some designs of regenerative
air heaters, a selective coating of catalytic materials is given to the heating
elementstopromotethereactionofNOxwithammoniaorurea,whichisinjected
upstreamoftheairheater.NOxisthusreduced.Theammoniumbisulfateformed
is removed periodically by online soot blowing.
Both tubular and regenerative air heaters are widely used in pulverized
coal–fired or fluid bed coal-fired boiler plants.
HEAT PIPES
Heat pipes (Fig. 3.28) were introduced into the heat recovery market about 40
years ago. A heat pipe consists of a bundle of pipes filled with a working fluid
such as toluene, naphthalene, or water and sealed. Heat from the flue gas
evaporates the working fluid collected in the lower end of the slightly inclined
pipes (6–10 from horizontal), and the vapor flows to the condensing section,
(cid:2)
where it gives up heat to the incoming combustion air.
Condensedfluidreturnsbygravitytotheevaporativesectionassistedbyan
internalcapillarywick,whichisessentiallyaporoussurfacesorcircumferentially
spiraled grove of proprietary design. The process of evaporation and condensa-
FIGURE 3.28 Arrangement ofaheatpipe.
Copyright © 2003 Marcel Dekker, Inc.

tioncontinuesaslongasthereisatemperaturedifferencebetweentheairandflue
gases.
In a typical design, there is a divider plate at the middle of the tube that
supports the tube and also maintains a seal between the hot flue gases and the
cold air. Pipe surfaces are finned to make the heat transfer surfaces compact.
Finned surfaces are used because the heat transfer coefficient inside the tubes is
very high due to the condensation and evaporation. Fin density is based on
cleanliness of the gas stream.
Heat pipes offer several advantages over conventional air heaters:
1. They are compact and weigh less than other air heaters due to the use
of extended surfaces.
2. Theyhavezeroleakagebecausethepipesarestationaryandthedivider
plate is welded to the tubes.
3. Noauxiliarypowerisneeded,becauseheatpipesdonotneedapower
source to operate.
4. Maintenance is low because there are no rotating parts.
5. They have low corrosion potential. Owing to the isothermal behavior
of the pipes, the minimum tube metal temperature is higher than in
other types of exchangers. By selecting proper working fluids, it is
possibleto maintain the cold end abovethe acid dew point. The tubes
also operate at constant temperature along their entire length because
of the phase transfer process.
6. They undergo only low stresses because the tubes are fixed at the
midpoint and are allowed to expand at either end.
7. Individual pipe failure does not appreciably affect the overall perfor-
mance of the unit.
8. Gas- and air-sidepressure drops aregenerally lower than intubular or
regenerative air heaters owing to the compactness of the design.
CONDENSING HEAT EXCHANGERS
The conventional design of economizers and air heaters ensures that cold end
corrosionduetocondensingsulfuric acidorwater vapordoesnotoccur because
the minimum tube wall temperature is maintained above the dew points.
However, owing to this design philosophy, a significant amount of energy is
lost or not recovered in boilers and HRSGs. The condensing heat exchanger is
designed to allow for the condensation of acid and water vapor over the heat
transfer surfaces, thusrecoveringasignificantamountofsensibleandlatentheat
from the flue gases. The efficiency of a boiler plant with a condensing heat
recoverysystemcanbecloseto99%.Withnaturalgasfiring,thepartialpressure
of water vapor is about 18%, whereas with oil fuels it is about 12%. With the
Copyright © 2003 Marcel Dekker, Inc.

condensation of this water vapor, significant improvement in efficiency can be
obtainedbyusingoil-firedboilersasshowninFig.3.29.Duetotheimprovement
in the overall efficiencyof the boiler or HRSG, the emissions of CO , NOx and
2
CO are also reduced.
Unlikeconventionaleconomizersandairheaters,whichmaintaintempera-
tures above 270–300 F to prevent condensation, the condensing exchanger can
(cid:2)
operatewith water or air at ambient temperatures. Hence condensate or makeup
water at 60–80 F or so can be directly used to be heated up by the flue gases,
(cid:2)
whereas in a noncondensing exchanger the lowest feedwater temperature would
varyfrom230to270 F.Hencetheexitfluegastemperaturecanbearound100–
(cid:2)
130 F versus 270–300 F. Because the exchanger tube surface and the exhaust
(cid:2) (cid:2)
section of the exchanger are below the dew point of water vapor, a rain of
condensate is produced through dropwise condensation of the water vapor. This
condensatepassesaroundthetubearray,carryingparticulatesandacidsthathave
been scrubbed and washed from thetubes.A fewdesignshandle the problemof
heat recovery and scrubbing at the same time to remove particulates and acid
gases from the waste gas stream from incineration plants.
Thecondensingexchangerconsistsofspeciallydesignedtubescoatedwith
a 0.015in. extruded layer of FEP Teflon. The inside surfaces of the heat
exchanger are covered with a 0.06in. thick sheet of PTFE Teflon. During
fabrication, the tubes are pushed through extruded tube seals in the Teflon-
covered tube sheet to form a resilient Teflon-to-Teflon seal. This ensures that all
heat exchanger surfaces exposed to the flue gases are protected against acid
corrosion. To protect the Teflon, the inlet gas temperature is limited to about
500 F. The tubes are generally made of Alloy C70600, which protects them
(cid:2)
FIGURE 3.29 Efficiency improvement in oil and gas firing using a condensing
exchanger.
Copyright © 2003 Marcel Dekker, Inc.

against acid corrosion. The tube sheet and casing are coated with Teflon to
preventcorrosion.Thesubdewpoint condensingexchanger uses baretubes due
tothecoatingrequiredandhenceislargerthanafinnedtubebundleforthesame
duty.
Potential applications also include recovery of water from the gas turbine
exhaust for recycle, reducing the amount of fresh makeup water required. The
water could be redirected with proper treatment into the steam–water injection
system for reducing NOx emissions. Cheng cycle systems, in which a large
amountofsteamisinjectedintoagasturbine,arealsocandidatesforcondensing
exchangers.
GLASS EXCHANGERS
Borosilicate glass (Pyrex) tubing has been used in heat recovery applications
because it is most resistant to chemical attack and presents no corrosion
problems. Fouling is minimal due to the smoothness of the surfaces. These
tubesalsohavealowcoefficientofexpansionandareresistanttothermalshock,
which makes them suitable as heat exchanger tubes. However, the temperature
limitisabout500 F,andthepressurelimitisalsolow,ontheorderof60psigor
(cid:2)
less. The thermal conductivity is lower than that of carbon steel, by about one-
third; however,because thetubewallthickness islow,thewallresistancetoheat
transferisalsolow.Thus,comparedtocarbonsteeltubestheoverallheattransfer
coefficient is lower by only a small margin. Flue gas towater heat recovery has
been accomplished by using glass exchangers.
SPECIFYING PACKAGED BOILERS
The following process data should be specified as a minimum.
1. Steam parameters such as flow, pressure, temperature, and feedwater
temperature. If saturated steam is taken from the boiler for deaeration
or for NOx control, fuel oil heating, etc., it should be so stated. If the
makeupwaterflowis100%,thedeaerationsteamcouldbeintherange
of 15% of the steam generation and therefore not an insignificant
amount.
2. If superheated steam is required, the steam temperature control range
should be specified. Generally the steam temperature can be main-
tained from 50 to 100%. A larger range requires a larger superheater.
Also, if several fuels were fired, the steam temperature would vary as
discussed above.
3. Analysisoffeedwaterenteringtheeconomizershouldbestatedsothat
the blowdown requirements can be evaluated. An example is given in
Copyright © 2003 Marcel Dekker, Inc.

Q5.17. In some refinery projects, I have seen very poor feedwater
being used, which results in 10% to even 20% blowdown, which is a
tremendous waste of energy; it also affects the boiler duty and heat
inputsignificantly.Heatinput,inturn,affectsthefluegasquantityand
gas pressure drop.
4. EmissionlimitsofNOxandCOshouldbestatedupfrontbecausethey
affect the burner design as well as the furnace design, the flue gas
recirculation rates, and therefore the entire boiler design and perfor-
mance. The use of SCR may also haveto be looked into, and the cost
implications are significant.
5. Fuels usedandtheiranalysis shouldbestated. Standardnaturalgasor
fuel oil may not have significant variations in analysis within the
United States, but for projects overseas the fuel analysis is important.
Somenaturalgasfuelsoverseascontainalargepercentageofhydrogen
sulfide, which can cause acid dew point problems. Gaseous fuels
should have the analysis in percent by volume and not in percent by
weight, whereas liquid and solid fuels should have the analysis in
percent by weight.
6. Surface areas should not be specified, for reasons discussed earlier.
7. Operatingcostssuchasthecostoffuelandelectricityshouldbestated
as well as the norm for evaluating operating costs. Ignoring operating
costs and selecting boilers based on initial costs alone (which is
unfortunately being done even today!) is doing a disservice to the
end user.
8. Furnaceareaheatreleaseratesaremoreimportantthanvolumetricheat
release rates for clean fuels, as mentioned earlier, therefore specifying
volumetricheatreleaseratesisnotrecommendedforgasandoilfuels.
9. Large fan margins should not be used, and efforts must be made to
estimatethegaspressuredropaccurately.Largemarginsonflow(such
as20%)andonheat(40%)notonlyincreasetheoperatinghorsepower,
whichisawasteofenergy,butalsomakeitdifficulttooperatethefan
at low loads. In boilers with single fans, the margins should be small,
say 10–12% on flowand 20–25% on head. Those familiar with utility
boiler practice where multiple fans are used try to apply the same
normstopackagedboilers,whichcanleadtooperatingconcernsatlow
loads unless variable-speed drives or variable-frequency drives are
used. The ambient temperature variations and elevation at which the
boilerislikelytobeusedareimportantbecausethisinformationhelps
in the selection of appropriate fans.
These points along with information on mechanical requirements such as
materials,corrosionallowances,andfutureoperationalconsiderations,ifany,are
Copyright © 2003 Marcel Dekker, Inc.

important to the boiler designer. The proposal should also clearly state the
required performance aspects.
REFERENCES
1. V Ganapathy. Understand the basics of packaged steam generators. Hydrocarbon
Processing,July1997.
2. V Ganapathy. Heat recovery steam generators: understand the basics. Chemical
EngineeringProgress,August1996.
3. V Ganapathy, Customizing pays off in steam generators. Chemical Engineering,
January1995.
4. APIRecommendedPractice530,2nd.ed.RecommendedPracticeforCalculationof
HeaterTubeThicknessinPetroleumRefineries.May1978.
5. V Ganapathy. Understand the basics of packaged steam generators. Hydrocarbon
Processing,July1997.
6. VGanapathy.Superheaters:designandperformance.HydrocarbonProcessing,July
2001.
7. VGanapathy.21stcenturypackagedboilerswillbelargerandmoreenvironmentally
friendly.PowerEngineering,August2001.
8. OJones.Developingsteampuritylimitsforindustrialturbines.Power,May1989.
9. J Robinson. A practical guide to avoiding steam purity problems in the industrial
plant.InternationalWaterConference,October1992.
10. NalcoCorp.TheNalcoGuidetoBoilerFailureAnalysis.NewYork:McGraw-Hill,
1991.
11. Editor.Attractiongrowsforheatpipeairheatersinfluegasstreams.Power,February
1989.
12. V Ganapathy. How important is surface area? Chemical Engineering Progress,
October1992.
13. V Ganapathy. Understand steam generator performance. Chemical Engineering
Progress,December1994.
Copyright © 2003 Marcel Dekker, Inc.

4
Emission Control in Boilers and HRSGs
INTRODUCTION
BoilerandHRSGdesignshaveundergonesignificantchangesduringthelastfew
decades with the enforcement of emission regulations in various parts of the
world. Decades ago boiler and HRSG users were concerned about two issues
only:theinitialcostoftheboilerorHRSGandthecostofoperation.Lowboiler
efficiency, for example, meant higher fuel cost, and a large pressure drop across
boiler heating surfaces resulted in increased fan power consumption. Each
additional 1in. WC pressure drop in a boiler of 100,000lb=h capacity results
in about 5kWof additional fan power consumption. In a gas turbine HRSG, an
additional 4in. WC of gas pressure drop decreases the gas turbine power output
by about 1.0%. At 320 F stack gas temperature, the difference in efficiency
(cid:2)
between 5% and 15% excess air operation on natural gas is about 0.4%.
Therefore, steam generators were operated at the lowest possible excess air,
about 5% or so, to maintain good efficiency. With strict emission regulations in
voguethroughouttheworld,present-daysteamgeneratorsorHRSGs,inaddition
tohavinglowoperatingcosts,mustlimittheemissionsofCO ;CO;NOx; SOx,
2
and particulates. The expression ‘‘low NOx, no SOx, and no rocks’’ aptly
describes the direction in which we are headed. However, several of the
techniques used for emission control increase the cost of owning and operating
Copyright © 2003 Marcel Dekker, Inc.

theboilersandHRSGs.Forexample,inordertomeetthestringentlevelsofNOx
andCO,today’sboilershavetooperateathigherexcessairandusesomefluegas
recirculation(FGR),whichaffectstheirefficiencyaswellastheiroperatingcosts
significantly, as we discuss later.
One of the important changes is in the use of an economizer instead of an
air heater for heat recovery in packaged boilers. Air heaters were used in
industrial boilers several decades ago even if the fuel fired was natural gas.
However, as the combustion air temperature to the boiler increases, the NOx
formation increases, because it is a function of flame temperature, as shown in
Fig. 4.1. With natural gas at 15% excess air, each 100 F increase in combustion
(cid:2)
air temperature increases the flame temperature by about 65 F. Hence today’s
(cid:2)
packaged oil- and gas-fired boilers do not use air heaters. Economizers are used
to improve their efficiency. In addition to increasing NOx, an air heater adds
about 3–5in. WC to the gas- and air-side pressure drop, while the typical gas
pressuredrop across theeconomizer is1in.WC.Therefore, with aneconomizer
as the heat recoveryequipment, substantial savings in operating costcan also be
realized.
Owing tothe useof low-NOxburners, the furnace dimensions ofstandard
boilers may have to be reviewed to avoid flame impingement concerns. The
completely water-cooled furnace (Fig. 4.2) is another innovation that helps in
loweringemissions.Ifthedesiredemissionlevelsareinsingledigits,HRSGsand
packaged boilers use catalysts to minimize NOx and CO, which influences their
design significantly. For example, a gas bypass system has to be provided in
boilers, and the evaporator may have to be split up in the case of HRSGs to
accommodate the selective catalytic reduction (SCR) system.
Thus,thereareseveralvariablesthataffectemissionsandnumerousoptions
to minimize them, as indicated in Fig. 4.3, which will be addressed in this
FIGURE 4.1 Typical NOxformation versusflametemperature fornaturalgas.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 4.2 Water-cooled furnace.(Courtesy ofABCO Industries, Abilene, TX.)
chapter. These emission control strategies naturally add to the initial and
operating costs of boilers and HRSGs and impact their design as well, a price
we must pay for cleaner air.
HOW POLLUTANTS ARE GENERATED
Before going into further details of how the boiler or HRSG is impacted by
emission regulations, one should first understand what thevarious pollutants are
FIGURE 4.3 OptionsforNOxremoval in boilersand HRSGs.
Copyright © 2003 Marcel Dekker, Inc.

and how they are formed. In the process of combustion of fossil fuels, be it in
steam generators, gas turbines, or engines, several pollutants are released to the
environment. These include carbon dioxide (CO ), oxides of nitrogen (NOx),
2
carbon monoxide (CO), oxides of sulfur (SOx), and volatile organic compounds
(VOCs).
Carbon dioxide is considered to be responsible for the greenhouse
effect and global warming. Concentrations of 3–6% can cause headaches;
larger concentrations can lead to unconsciousness and possibly death. Coal
generates about 200lb CO =MM Btu fired; oil generates 150lb and natural
2
gasabout100lbperMMBtu.Henceonecanseewhynaturalgasisthepreferred
fuel in any fired equipment. CO molecules retain infrared heat energy,
2
preventing normal radiation from the earth and leading to warming of the
atmosphere. There are several processes, such as amine-based systems that
can remove CO from flue gas streams, but these can be justified only in large
2
plants.
The presence of carbon monoxide (CO) in flue gases is indicative of
inefficient combustion and may be due to poor burner operation, improper
settings, or even poor boiler design. CO is dangerous to the health of humans
and other living creatures. It passes through the lungs directly into the blood-
stream, where itreduces theabilityofthe redbloodcellstocarryoxygen.Itcan
cause fainting and even death. At an exposure of only 0.1% by volume
(1000ppm) in air, a human being will be comatose in less than 2h. A few
regulationsestablishamaximumexposureofCOof9ppmforan8haverageand
13ppm for any 1h period.
Oxidesofnitrogen,NOx,arepredominantlyNOandNO .Themajorityof
2
NOx produced during combustion is NO (95%). NOx is responsible for the
formation of ground-level ozone or smog. Oxides of sulfur, SOx, are formed
when fuels containing sulfur are fired. Sulfur dioxide (SO ) and sulfur trioxide
2
(SO ) are responsible for acid rain and can damage plant life and materials of
3
construction. The Taj Mahal in India is a good example of what acid formation
fromnearbyrefineriesemittingoxidesofsulfurcandotothelusterandbeautyof
marbleoveraperiodoftime.Particulatesarealsoformedduringcombustionthat
disperseintheair toformhazeandsmog,affectingvisibility.Dangerousdriving
conditions are created in some places due to smog formation. Inhalation of
particulates affects the lungs and the digestive system.
Volatile organic compounds (VOCs), which are generated in industrial
processessuchasthoseofchemicalandpetrochemicalplants,alsocauseharmful
ozone.
Tremendouseffortsarebeingmadetoreducethesepollutantsinpowerand
process plants, refinery heaters, and combustion equipment.
Copyright © 2003 Marcel Dekker, Inc.

NOx FORMATION
Nitrogenoxidesareofenvironmentalconcernbecausetheyinitiatereactionsthat
result in theformationofozone andacid rain, whichcan cause healthproblems,
damage buildings, and reduce visibility. The allowable NOx emissions from
boilersandHRSGsvarydependingonlocalregulationsbutaregraduallyedging
towardsingle-digitvaluesinpartspermillionvolume(ppmv)duetoadvancesin
combustion and pollution control technology. The principal nitrogen pollutants
generated by boilers, gas turbines, and engines and other combustion equipment
arenitricoxide(NO)andnitrogendioxide(NO ),collectivelyreferredtoasNOx
2
andreportedasNO .Oncereleasedintotheatmosphere,NOreactstoformNO ,
2 2
which reacts with other pollutants to form ozone (O ). Oxides of nitrogen are
3
produced during the combustion of fossil fuels through the oxidation of atmo-
spheric nitrogen and fuel-bound nitrogen. These sources produce three kinds of
NOx: fuel NOx, prompt NOx, and thermal NOx.
Fuel NOx is generated when nitrogen in fuel combines with oxygen in
combustion air. Gaseous fuels have little fuel-bound nitrogen, whereas
coal and oil contain significant amounts. Fuel-bound nitrogen can
account for about 50% of total NOx emissions from coal and oil
combustion. Most NOx control technologies for industrial boilers
reduce thermal NOx and have little impact on fuel NOx, which is
economically reduced by fuel treatment methods or by switching to
cleanerfuels.FuelNOxisrelativelyinsensitivetoflametemperaturebut
is influenced by oxygen availability.
Prompt NOx results when fuel hydrocarbons break down and recombine
withnitrogeninair.PromptNOxischemicallyproducedbythereactions
that occur during burning; specifically, it forms when intermediate
hydrocarbon species react with nitrogen in air instead of oxygen.
Prompt NOx, so called because the reaction takes place ahead of the
flame tip, accounts for about 15–20ppm of the NOx formed in the
combustionprocessandisaconcernonlyinlowtemperature situations.
Thermal NOx forms when atmospheric nitrogen combines with oxygen
underintenseheat.Thisrateofformationincreasesexponentiallywithan
increase in temperature and is directly proportional to oxygen concen-
tration. Its formation is well understood and straightforward to control.
Keeping the flame temperature low reduces it. Belowa certain tempera-
ture, thermal NOx is nonexistent, as indicated in Fig. 4.1. Combustion
temperature, residence time, turbulence, and excess air are the other
factorsthataffecttheformationofthermalNOx.MostNOxisformedin
this manner in gas turbines, industrial boilers, and heaters fueled by
natural gas, propane, butane, and light fuel oils.
Copyright © 2003 Marcel Dekker, Inc.

Common boiler fuels in the order of increasing NOx potential are
methanol, ethanol, natural gas, propane, butanes, distillate fuel oil, heavy fuel
oils, and coal.
NOx CONTROL METHODS
Methods for NOx control can be classified into two broad categories:
1. Postcombustion methods: methods that are deployed after flue gases
are generated.
2. Combustion control methods: methods that are deployed during the
combustion process.
Postcombustion Methods
As the name implies, postcombustion methods dealwith the flue gases obtained
after combustion. They are more expensive than combustion control methods,
because they handle large quantities of flue gases generated in the process of
combustion.Theratiooffluegastofuelonaweightbasisisabout21fornatural
gas and 18 for fuel oils in steam generators. In gas turbines, the exhaust gas
quantity generated is very large because on the order of 200–300% excess air is
used. The two commonly used methods of control are
1. Selective noncatalytic reduction (SNCR) methods
2. Selective catalytic reduction (SCR) methods
SNCR
In selective noncatalytic reduction a NOx reduction agent such as ammonia or
urea is injected into the boiler exhaust gases at a temperature of approximately
1400–1650 F. The ammonia or urea breaks down the NOx in the exhaust gases
(cid:2)
into water and atmospheric nitrogen, plus CO if urea is injected. This reaction
2
takes place in a narrow range of temperatures; as shown in Fig. 4.4, ammonia is
formed below a certain temperature, and above this temperature the NOx level
increases.SNCRreducesNOxbyabout70%.TheSNCRmethodisusedinlarge
industrial and utility boilers, which have adequate residence times for the
reduction reactions. In packaged boilers it is difficult to apply this method
becausetheammoniaorureamustbeinjectedintothefluegasesataspecificflue
gastemperature;however,thegastemperatureprofilevarieswithload,excessair,
and fuel fired as shown in Fig. 4.5 and residence times in oil- and gas-fired
packaged boilers are generally very small.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 4.4 Rangeof temperatures forSNCR operation.
FIGURE4.5 Boilertemperatureprofilesasafunctionofload.Furn,furnace;scrn,
screen;SH,superheater evap,evaporators;econ,economizer.
Copyright © 2003 Marcel Dekker, Inc.

Typical reactions, that take place with ammonia injection are:
NO NH 1=4 O N 3=2 H O
þ 3þð Þ 2(cid:3)! 2þð Þ 2
NH 5=4 O NO 3=2 H O
3þð Þ 2 ! þð Þ 2
Both oxidation and reduction take place. Ammonia oxidizes to form NO.
Because reduction and oxidation reactions are temperature-sensitive, there is a
narrowrangeoftemperaturesinwhichtheconversionsareefficient.Anincrease
in ammonia increases the efficiencyof conversion; however, excessive ammonia
can slip through the reactions and cause plugging of components downstream.
SNCR has a low cost of operation and may be used in conjunction with other
methods such as a low-NOx burner to improvethe efficiencyof NOx reduction.
In large field-erected boilers, wall injectors are located at several locations
toinjecttheammoniaorureausingspeciallydesignedlances.Thismethodisnot
usedinHRSGsbecauseitisdifficulttofindsuchatemperaturewindowandalso
have a suitable residence time.
Benefits of SNCR include
Medium to high NOx reduction.
(cid:1)
No by-products for disposal—minimizes waste management concerns,
(cid:1)
Easy to retrofit—little downtime required.
(cid:1)
Minimum space required.
(cid:1)
Can be used along with other NOx reduction methods.
(cid:1)
Lowenergy consumption. Additional gas pressure drop of flue gases is
(cid:1)
zero,unlikeinSCRmethod,wherethecatalystcouldaddabout3to4in.
WC to the gas pressure drop, adding to the operating cost.
SCR
If the desired CO and NOx levels are very low, on the order of single digits, a
selective catalytic reduction (SCR) system may have to be used in boilers and
HRSGs,Becausemostcatalystsoperateefficientlywithinatemperaturewindow,
generally650–780 F,theboilershouldhaveagasbypasssystemtoaccommodate
(cid:2)
the gas temperaturewindowat all loads. One can see from Fig. 4.5 how the gas
temperature profile across a packaged boiler varies with load. As the load
decreases,thegastemperatureatthevarioussurfacesdecreasesbecauseasmaller
amount of flue gases is generated at lower load. Hence a gas bypass system, as
shown in Fig. 4.6, that mixes the hot flue gases taken from the convection bank
withthecoolergasesattheevaporatorexitensuresahighergastemperatureatthe
SCR at low loads. Heat recovery steam generators (HRSGs) also use the SCR
system to limit NOx, and, again, to match the gas temperature window of 650–
780 FtheevaporatorisoftensplitupasshowninFig.4.7.Ifwedidnotsplitup
(cid:2)
the evaporator, we would have a very low gas temperature at its exit; also we
cannot locate the SCR system ahead of the evaporator, because the gas
Copyright © 2003 Marcel Dekker, Inc.

FIGURE4.6 Gasbypasssysteminboilerusing(a)FGRand(b)SCRmethodsfor
NOxcontrol.
temperature there is very high. As shown in Fig.4.7, the two evaporator circuits
are in parallel. External downcomers and risers are used to ensure adequate
circulation through both the evaporator modules. Figure 4.8 shows the gas
temperaturesenteringvarioussectionsofafiredHRSG—superheater,evaporator,
economizer, and stack—at various steam flows. The gas temperature at the
entranceofthesecond-stageevaporatorsectionmaybeseentobeintherangeof
650–800 F.The SCRsystem addsabout3–4in.WCtotheboilerorHRSG gas-
(cid:2)
side pressure drop, which is an operating expense as discussed earlier.
The selective catalytic reduction (SCR) method uses the same reaction
process as SNCR except that a catalyst is employed to lower the temperature of
operationandalsoincreasetheefficiencyofconversion.Ammoniaorureaisused
inthesereactionsasthereagent.Figure4.9showshowammoniaisaddedinthree
differentsystems.Themostcommonmethodusesanhydrousammonia,whichis
pure ammonia. Anhydrous ammonia is toxic and hazardous, particularly if the
neighborhood has a large population. It has a high vapor pressure at ordinary
temperaturesandthusrequiresthickshellsforthestoragetanks.Itsreleasetothe
atmospherecancauseenvironmentalproblems,andextremecautionisrequiredto
handlesuchasituation.However,thisistheleastexpensivewaytofeedammonia
into the HRSG.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 4.7 HRSG showinglocation ofNOx(SCR) and COcatalysts.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 4.8 HRSG gas temperature profiles as a function of steam generation.
sh,superheater; econ,economizer; evap,evaporator.
FIGURE 4.9 Ammonia injection methods. (Courtesy of Peerless Manufacturing,
Dallas, TX.)
Copyright © 2003 Marcel Dekker, Inc.

AqueousNH NH OH ,whichisamixtureofammoniaandwater,issafer
3ð 4 Þ
to handle. A typical grade contains 30% ammonia and 70% water. It has nearly
atmospheric vapor pressure at ordinary temperatures. The liquid ammonia is
pumpedtoavaporizerandmixedwithheatedairbeforebeingsenttothemixing
grid.Ureasystems,whichgenerateammoniaon-site,arealsosaferandhavebeen
recently introduced. Dry urea is dissolvedto form an aqueous solution, whichis
fed to an in-line reactor to generate ammonia by hydrolysis. Heat is applied to
carry out the reactions under controlled conditions. The ammonia is mixed with
air and then injected through a grid into the gas stream.
Computationalfluiddynamics(CFD)analysisisdonetoensurethatthegas
velocity distribution across the boiler or HRSG cross section is uniform, with
variationswithin15%.Theammoniavaporismixedwithairandsprayedintothe
flue gas stream at the desired location before coming into contact with the
catalyst. A heat transfer surface located immediately behind the ammonia
injection grid ensures good mixing of ammonia vapor with the flue gases. The
optimum gas temperature for the NOx reduction reactions with most catalysts is
600–780 F as mentioned earlier. Below this temperature, chemical reactivity is
(cid:2)
impaired, and above it physical damage can occur to the catalyst through
sintering. From the boiler or HRSG design viewpoint, a suitable location has
to be found for the SCR so that at the wide range of loads, the temperature
window is maintained, to ensure that undesirable oxidation of ammonia to NO
doesnottakeplace.Thisisaccomplishedinaboilerbyusingagasbypasssystem
as discussed earlier. The ammonia injection system is located upstream of the
SCR and should have sufficient mixing length that the flue gases can react with
ammonia. SCR efficiency ratings are in excess of 90%. A gas pressure drop
across the catalyst of about 3–4in. WC adds to the fan power consumption in a
steamgeneratorandcouldbeasignificantpowerdecrementinagasturbineplant.
Catalysts are typically platinum, vanadium, tungsten, and noble metals and
zeolites, which are used at higher temperatures.
Typical reactions are
catalyst
4NH 4NO O 4N 6H O
3þ þ 2 (cid:3)! 2þ 2
catalyst
4NH 2NO 3N 6H O
3þ 2 (cid:3)! 2þ 2
Tocompletethesereactions,slightlymoreNH thanrequiredisinjectedintothe
3
gas stream. This excess ammonia, which is called slip, is generally limited to a
single-digit value (less than 5ppm), through a control and emission monitoring
system. The slip value increases gradually over a period of time as the catalyst
nears the end of its service life.
Sulfur-containing flue gas streams present problems for boilers and
HRSGs. The presence of vanadium in the SCR converts SO to SO , which
2 3
Copyright © 2003 Marcel Dekker, Inc.

canreactwithexcessammoniatoformammoniumsulfateorwithwatervaporto
form sulfuric acid, causing problems such as fouling and plugging of tubes
downstream of the boiler or HRSG. Distillate oil contains a small amount of
sulfur,hencetheonlywaytominimizethisconcernistolimittheoperatinghours
on oil fuels. Lowering the ammonia slip also helps, but this can lower the NOx
reduction efficiency.
Environmentally ammonium sulfate and bisulfate are particulates that
contribute to visible haze and acidify lakes and ground areas when they settle
out of the air.
Sulfates are formed according to the equations
SO NH H O NH HSO
3þ 3þ 2 ! 4 4
SO 2NH H O NH SO
2þ 3þ 2 !ð 4Þ2 4
Ammonium sulfate is a sticky substance that can be deposited on heat transfer
surfacesandcausefouling.Thegaspressuredropacrosstheheatingsurfacesalso
increases over a period of time. If the ammonia slip is less than 10ppm and the
SO concentration is less than 5ppm, expert opinion is that the probability of
3
ammonium sulfate formation is practically nil unless the gas temperature is low,
on the order of 200 C. Hence low gas temperatures should be avoided,
(cid:2)
particularly at the catalysts, because salt formation and deposits there would be
detrimentaltothelifeofthecatalyst.Somesuppliersrequireaminimumof450–
500 F at the catalyst to minimize these reactions. Either ammonium sulfate or
(cid:2)
ammoniumbisulfatewillbeformed bythereactionofSO andexcessammonia
3
downstream of the SCR catalyst. In general, ammonium sulfate is considerably
less corrosive than ammonium bisulfate.
One should keep the boiler or HRSG warm in standby conditions during
brief shutdowns iffuel oils are fired. Shutdown and isolation of the HRSG after
oil firing should be avoided because the SO can condense during the cooling
3
phase.ForboilersorHRSGsfiringnaturalgasfuels,fortunately,therearenosuch
concernsasthosejustdiscussed.Itmaybenotedthatthepresenceofwatervapor
in the flue gases has an adverse effect on NOx reduction efficiency.
Selective catalytic reduction systems have efficiencies of 90–95%.
However, they are expensive and may cost from $3000 to $5000=MM Btu=h
in gas or oil-fired packaged boilers. For gas turbines the cost could range from
$40to100=kW.Insomecoal-firedplantswhereregenerativeairheatersareused,
thehotendheatingelementsarecoatedwithacatalystmaterialtoconvertNOxto
N and H O.
2 2
SCONOx
TheSCONOxsystemisarecentdevelopmentthatisclaimedtoreduceNOxand
COlevelsto2–5ppmvwithasinglecatalyst.Itdoesnotuseammoniaorureaand
Copyright © 2003 Marcel Dekker, Inc.

hence avoids the concerns associated with handling ammonia. The system can
operate efficiently at 300–700 F, which is an advantage because the HRSG
(cid:2)
evaporator need not be split up. Typically the gas temperature between the
evaporatorandeconomizerofanHRSGisinthisrange.Dampersarenotneeded
tocontrolthegastemperature insteam generatorsatlowloads.Thismethodhas
been used in a few HRSGs but not in packaged boilers.
The SCONOx catalyst works by simultaneously oxidizing CO to CO ,
2
hydrocarbonstoCO H O,andNOxtoNO andthenabsorbingNO ontoits
2þ 2 2 2
platinum surface through the use of a potassium carbonate absorber coating.
These reactions, shown below, are referred to as the ‘‘oxidation=absorption
cycle.’’
CO 1O CO
þ2 2 ! 2
NO 1O NO
þ2 2 ! 2
CH O O CO H O
2 þ 2 ! 2þ 2
2NO K CO CO KNO KNO
2þ 2 3 ! 2þ 2þ 3
The CO produced by these reactions is exhausted up the stack. The potassium
2
carbonatecoatingreactstoformpotassiumnitratesandnitrites,whichremainon
the surface of the catalyst.
The SCONOx catalyst can be compared to a sponge absorbing water. It
becomessaturatedwithNOxandmustberegenerated.Whenallofthecarbonate
absorbercoatingonthecatalystsurfacehasreactedtoformnitrogencompounds,
NOx will no longer be absorbed, and the catalyst must enter the regeneration
cycle.
The unique regeneration cycle is accomplished by passing a dilute hydro-
genreducinggasacrossthesurfaceofthecatalystintheabsenceofoxygen.The
hydrogen reacts with nitrites and nitrates to form water and elemental nitrogen.
Carbondioxideintheregenerationgasreactswithpotassiumnitritesandnitrates
to form potassium carbonate, which is the absorber coating that was on the
catalystsurfacebeforetheoxidation=absorptioncyclebegan.Thiscycleiscalled
the ‘‘regeneration cycle.’’
KNO KNO 4H CO K CO 4H O N
2þ 3þ 2þ 2 ! 2 3þ 2 þ 2
Water and elemental nitrogen are exhausted up the stack instead of NOx, and
potassium carbonate is once again present on the catalyst surface, allowing the
entire cycle to begin again.
Because the regenerationcyclemusttake place inanoxygen-free environ-
ment, a section of catalyst undergoing regeneration must be isolated from the
exhaust gases, usually by a set of louvers, one upstream of the section being
regenerated and one downstream. During the regeneration cycle, these louvers
Copyright © 2003 Marcel Dekker, Inc.

closeandavalveallowstheregenerationgasintothesection.Stainlesssteelstrips
on the louvers minimize leaks during operation. A SCONOx system has five to
15 sections of catalyst, depending on gas flow, design, etc. At any given time,
80% of the sections are in the oxidation=absorption cycle and 20% are in the
regeneration mode. Because the same number of sections are always in the
regenerationmode,theproductionofregenerationgasproceedsataconstantrate.
Aregenerationcyclelastsfor3–5min,soeachsectionisinoxidation=absorption
mode for 9–15min.
The SCONOx technology is still being developed and have yet to
accumulate significant operational experience compared to the SCR system. It
isalsoveryexpensiveandissensitivetosulfur,eventhesmallamountinnatural
gas. For a 2.5ppmv NOx limit from a 501 F Westinghouse gas turbine, studies
(cid:2)
show that the cost of SCONOx is more than that of the SCR system. However,
with technological improvements, it could become an economically viable
option.
Combustion Control Methods
The formation of NOx has been well understood by burner manufacturers, who
are able to offer several methods to reduce the formation of NOx in steam
generators. Gas turbine manufacturers also have come up with design improve-
ments to lower NOx emissions.
During the combustion process, several complex reactions occur within
the flame, and NOx formation is a function of temperature, oxygen, and time
of residence in the high temperature zones. Figure 4.1 shows the effect of
temperature on NOx formation. As the combustion temperature is reduced from
2700 F to 2300 F, NOx is reduced by a factor of 10.
(cid:2) (cid:2)
As the excess air increases, the NOx increases and drops off as shown in
Fig. 4.10 Because CO is another pollutant, its emissions should also be limited.
Astheexcessair increases, COdecreases.Hencethereisabandofexcessairin
which one can operate the burner to minimize both NOx and CO.
Gas turbine manufacturers have come up with dry low-NOx (DLN)
combustors,whichlimittheNOxtosingle-digitlevels.MostoftheNOxemitted
by a gas turbine firing natural gas is generated by the fixation of atmospheric
nitrogen in the flame, and the amount of this ‘‘thermal NOx’’ is an exponential
functionofflametemperature.TheDLNcombustorlowerstheflametemperature
by burning a leaner mixture of fuel and air in premixed mode. To reduce NOx
emissionsintraditionalcombustors,steamorwaterisinjectedtoreducetheflame
temperature;benefitsincludeadditionalpoweroutput.However,thereisalossin
engine life and shortening of combustor life. CO formation also increases as the
amount of water or steam increases, as shown in Fig. 4.11.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 4.10 Typical NOxand COlevels versusexcess air.
Oxygen Control
In steam generators, oxygen trim can be added to control the excess oxygen
levels. Too little oxygenincreases CO formation, and too much can increase the
NOx.Also,theboilerefficiencyisimpactedbytheexcessairlevelsasdiscussed
in Chapter 3. The higher mass flow also affects the gas temperature distribution
throughout the boiler and can affect the superheated steam temperature.
Steam–Water Injection
Boiler and burner suppliers sometimes use steam injection to reduce the flame
temperatureandthusdecreaseNOx.Steamgeneratorsaswellasgasturbinesuse
this method. In boilers the steam consumption could vary by 1–3% of the total
steam generated, thus reducing the boiler output; however, the significant
reduction in NOx may offset the need for FGR or other methods. The NOx
reduction is more significant with gas firing than with oil firing. A side effect of
water or steam injection is the increase in CO content. Hence there should be a
compromise between the efforts to reduce NOx and CO.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 4.11 Effectof steam–waterinjectionon NOxandCO.
Copyright © 2003 Marcel Dekker, Inc.

InHRSGs,steamorwaterinjectionintothegasturbinecombustorisused
along with catalysts located in the HRSG to limit NOx to single digits. The
increase in water vapor content on SCR performance has to be reviewed. Steam
injection also increases the gas turbine power output due to the increased mass
flow and higher specific heat of the gases with increased water vapor content.
This concept is used in the Cheng cycle power system discussed in Chapter 1.
Water or steam injected into gas turbines has to be treated to give high
steampurity.Steampurityshouldbepreferablyinthepartsperbillionrange.The
treatedwaterislosttotheatmosphereandhastobeevaluatedasanoperatingcost
in such systems.
Burner Modifications
Staged combustion is widely used by burner suppliers to reduce NOx. In this
method,thefuelorairisaddedinincrements(Fig.4.12)sothatatnopointinthe
flame is an exceptionally high temperature obtained. In air staging, a fuel-rich
mixtureisinitiallycreated,followedbytheadditionofairattheburnertiptoburn
theremainingfuel.Aslittleas60%ofthetotalcombustionairisintroducedinto
the primary combustion zone. The substoichiometric operation generates a high
levelofpartialpressuresofhydrogenandCO,andthesereducingagentslimitthe
NOx formation. The second-stage air is introduced downstream to complete the
combustion process after some heat has been transferred to the process, thereby
limiting the formation of thermal NOx. The staging of air does provide some
control over both thermal and fuel NOx.
A concept that is a little more effective for reducing thermal NOx is fuel
staging. Staged fuel burners arewidely used.A portion ofthefuel andall of the
combustionairareintroducedintotheprimarycombustionzone.Rapidcombus-
FIGURE 4.12 Staging offueland airin burners.
Copyright © 2003 Marcel Dekker, Inc.

tionisachievedinthefuel-richatmospherewithahighlevelofexcessair,which
reduces thepeakflame temperature,therebyreducingthermalNOx.Thefuel for
the second stage is introduced through a series of nozzles positioned around the
burner perimeter. This fuel is introduced in such a manner that the final
combustion occurs after heat has been transferred to the process, lowering the
final combustion temperature. In addition, the secondary fuel is injected at a
relatively high pressure, which, because of the position of the secondary tips,
entrains flue gases; this simulates flue gas recirculation, which helps lower the
combustiontemperature.AlthoughfuelstaginghelpslowerthermalNOxbyupto
75%, it does not reduce the amount of fuel NOx generated. However, this is a
smallportionoftheoverallNOxingas-firedboilers.Fuelstagingisdifficultwith
liquidfuels.Fuelstagingalsohelpsoperationatlowerexcessairthanairstaging.
A few burner suppliers are able to promise less than 30ppmvd NOx using this
technique.
Furnace Modifications
Thecompletelywater-cooledfurnace(Fig.4.2)providesacoolerenvelopeforthe
flame than a refractory-lined front wall or floor and hence produces less NOx.
Most NOx is generated at the flame front when combustion is initiated, and a
water-cooled furnace absorbs some of the radiation from the flame, which helps
cool it, whereas a refractory-lined boiler reradiates energy back to the flame,
keeping it locally hotter, thus increasing its potential for forming thermal NOx.
The effective projected radiant surface for this design is greater than that of a
refractory-lined boiler by 7–15%. Hence the net heat input per unit effective
radiantareaortheheatreleaserateonareabasisislower,whichalsohelpslower
NOx.
Burner Emissions
DuctburnersusedinHRSGsalsogenerateNOxandCO,addingtotheemissions
fromtheturbineexhaustgases.ThecalculationprocedureforestimatingtheNOx
and CO in ppmv after combustion is shown in Q6.26e. It may be noted that the
values ofNOx and COin lb=h arealways higher after combustion; however, the
valuesinppmvmayormaynotbe,dependingontheinitialppmvvaluesofNOx
andCOandthecontributionbytheburner.TypicalNOxandCOemissionsfrom
duct burners are listed in Table 4.1.
With distillate oils containing fuel-bound nitrogen in the range of 0.05%,
nearly80–90%of itisconvertedtoNOx,whereaswithheavyfueloilswith0.3%
nitrogen, about 50% of it is converted to NOx. In the case of packaged boiler
burners,theemissionsdependonburnerdesign,onwhetherfuelispremixedwith
air, on whether fuel or air is staged, and on the combustion temperature as
discussed below. NOx emission ranges from 0.04 to 0.1lb=Mm Btu for natural
gasfiringandincreasesifhydrogenorafuelwithahighcombustiontemperature
Copyright © 2003 Marcel Dekker, Inc.

TABLE4.1 Typical Emissions fromVariousFuels
Gas Nox (lb=MM Btu) CO (lb=MMBtu)
Natural gas 0.1 0.08
Hydrogen gas 0.15 0
Refinerygas 0.1–0.15 0.03–0.08
Blastfurnace gas 0.03–0.05 0.12
Producer gas 0.05–0.1 0.08
is fired. Typical CO emissions range from 30 to 100ppmv. Combustion
technologyisimprovingdaybyday.Readersshouldnotethatsignificantchanges
in burner design or combustion techniques could be made available to the
industry before this book is even published!
Flue Gas Recirculation and Excess Air
Present-daypackagedsteamgeneratorsoperateathighexcessair(15–20%)with
fluegasrecirculation(FGR)ratesrangingfrom0%to30%tolimitCOandNOx.
Flue gas recirculation refers to the admission of flue gases from the boiler exit
back into the burner region in order to lower the combustion temperature, as
showninFig.4.6,whichinturnlowersNOx.SeeTable4.2fortheeffectofFGR
on combustion temperature.
ThereasonfortheuseofhighexcessaircanbeseenfromFig.4.10,which
shows that as theexcessair isincreased,theNOxlevelincreases andthen drops
off.Atsubstoichiometricconditions,thecombustiontemperatureisnothighand
hence the NOx formation is less; however, as the excess air increases, the
combustiontemperatureincreases,whichresultsinhigherNOx.Furtherincrease
in excess air (or FGR) lowers the flame temperature and hence NOx decreases.
Also, at a low excess air rate, the CO generation is high due to poor mixing
betweenfuelandair.HencetomeetbothCOandNOxlevels,15%excessairand
15% FGR rates are not unusual today in oil- and gas-fired steam generators.
Some burner suppliers recommend 15% excess air and 30% FGR rates to limit
theNOxtolessthan9ppmvonnaturalgasfiring.TheFGRsystemnaturallyadds
TABLE4.2 Effect ofFGR onCombustion Temperatureswith 15%Excess Air
Natural gas No.2oil
FGR,% 0 15 30 0 15 30
Combustion temp, F 3227 2892 2619 3354 2994 2713
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

toboththeinitialandoperatingcostsoftheboiler.Henceexcessairontheorder
of 5%, which was typical decades ago, is not adequate to limit CO, though
efficiencywiseit makes sense. The combination of high FGR rate and excessair
factor increases the mass flowof fluegases through the boiler, though the steam
generation may be unchanged, making it necessary to use a larger boiler for the
same duty. If the same boiler (designed several decades ago) were used, the flue
gasmassflowthroughtheboilercouldbe20–25%higher,resultinginsignificant
pressure drop across the heating surfaces and consequently higher fan power
consumption.
Table 4.3 shows the effect of different excess air and FGR rates on the
performance of a boiler of 100,000lb=h capacity generating steam at 300 psig
usingfeedwaterat230 F.Cases1and2useaneconomizer.Cases3and4show
(cid:2)
theresultswithouttheeconomizer.Inallthesecalculationstheboilerisassumed
tobethesameandtheburnerischangedtohandlethehigherexcessairandFGR
rate.Thenewburnerisassumedtohavethesamepressuredropastheearlierone.
Thepressuredropdifferencesshownareduetothedifferenceinthefluegasflow
rates through the boiler.
Using an electricity cost of 7cents=kWh and fuel cost of $3=MM Btu, the
additional fuel and electricity costs due to the lower efficiency and higher gas
pressure drop were computed and are shown below in Table 4.3. Due to the
higherexcessairandFGRrate,theannualoperatingcostincreasesby$43,400in
case 2 overcase 1. This does notinclude thecost of thebypass system,damper,
and controls. When the economizer is not present, the differential operating cost
is evenmore, $69,000 per year. Two conclusions may be drawn from this study:
TABLE4.3 EffectofExcessAirandFlueGasRecirculationonBoilerOperating
Costs
Item Case 1a Case2a Case3b Case4b
Duty, MMBtu=h 101.4 101.4 101.4 101.4
Exitgas temp, F 295 311 553 579
(cid:2)
Excess air,% 10 15 10 15
FGR,% 0 15 0 15
Fluegas,lb=h 96,349 117,416 103,498 126,923
Fuelinput,MMBtu=h 119.83 120.68 128.72 130.45
Gas drop,in.WC 16 21 17.6 21.5
Fanpower, kW 60 101 71 120
Efficiency,% HHV 84.6 84.0 78.78 77.74
Fancost, $=yr 0 23,000 0 27,500
Fuelcost,$=yr 0 20,400 0 41,500
aWithaneconomizer.
bWithoutaneconomizer.
Copyright © 2003 Marcel Dekker, Inc.

1. Modifying an existing boiler to handle new emission levels will be
expensive in terms of operating costs.
2. Operating a boiler without the economizer results in a higher gas
pressuredropevenforthesameexcessair.Case3showsanincreaseof
1.6in.WCovercase1.Thisisduetothelargerfluegasflowincase3
arising out of lower boiler efficiency.
As shown in Fig. 4.13, the effect of FGR on NOx reduction gradually
decreases as the FGR rate increases; that is, NOx reduction is very high at low
FGRratesandastheFGRrateincreasestheincrementalNOxreductionbecomes
smaller. On oil firing, the effect of FGR is less significant. Operators must
consider the risk of operating a boiler near the limits of inflammability when
usinghighamountsofFGR.Figure4.14showsthenarrowingbetweentheupper
flammability limit and the lower ignition limit as FGR increases. Integrating
control systems to maintain fuel=air ratios at high FGR rates is difficult because
FGR dampens the combustion process to the ragged edges of flammability—
flame-outs and flame instability. Full metering combustion control systems with
good safety measures are necessary in such cases.
AstheFGRrateincreases,thegaspressuredropacrosstheboilerincreases,
and the boiler must be made larger with wider tube spacing or the fan power
consumptioncanbesignificantasshowninTable4.3.Aboilerusing20%FGRis
equivalenttoa20%increaseinitssizecomparedtoaboilerofthesamecapacity
not using FGR. One has to be concerned about the flame stability at low loads
and also the excess CO formed. Generally, in packaged boilers the FGR duct is
connected to the fan inlet duct and a separate FGR fan is not required. Large
FIGURE 4.13 NOxversusflue gasrecirculation.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 4.14 Flue gas recirculation and limits of inflammability. (Adapted from
newsletter ofCoen Co.,Spring1996, Burlingame, CA.)
industrialboilersuseseparateFGRfans.Ifthefluegasescontainoxidesofsulfur,
then mixing the flue gases at the fan inlet may lower the temperature below the
acidvaporpointandriskpotentialcorrosionatthefanandinletductwork;insuch
cases,aseparatefanmaybeusedtoadmitthefluegasesdirectlyneartheburner
throat. With induced FGR, the inlet temperature to the fan increases. With 80 F
(cid:2)
ambient temperature and 15% FGR at 320 F fluegas temperature, the mixed air
(cid:2)
temperature at the fan inlet is about 112 F. The air density decreases, which
(cid:2)
resultsinaslightlylargervolumeofairtobehandledbythefan.FGRalsoaffects
theperformanceofsteamgeneratorsbecauseitaffectsthegastemperatureprofile
throughout the boiler. This is illustrated in Chapter 3.
Gas Reburn
One of the methods to reduce NOx in large industrial boilers is natural gas
reburning, which is capable of providing a 50–70% reduction in NOx. In this
method, natural gas is injected into the upper furnace region to convert the NOx
formedintheprimaryfuel’scombustiongasestomolecularnitrogen.Theoverall
process occurs within three zones of the boiler as shown in Fig. 4.15.
Primary Combustion Zone: Burners fueled by coal, oil, or gas are turned
down by 10–20%. Lowexcess air is used to minimize NOx.
Gas Reburning Zone: Natural gas between 10% and 20% of boiler heat
inputisinjectedabovetheprimarycombustionzone.Thiscreatesafuel-
rich region where hydrocarbon radicals react with NOx to form mole-
cular nitrogen. Recirculated flue gases may be mixed in with the gas
before it is injected into the boiler.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 4.15 Reburning andNOxreduction.
BurnoutZone:Aseparateoverfireairsystemredirectsairfromtheprimary
combustion zone to a location above the gas reburning reaction zone to
ensurecompletecombustionofanyunreactedfuel.Allcoal-,oil-,orgas-
fired utility boilers are suitable for reburning. There must be enough
room above the main firing zone for reburning and burnout. As the
naturalgasreplacestheprimaryfuel(coaloroil),theemissionsofSOx,
CO , and particulates are also reduced.
2
CARBON MONOXIDE REDUCTION
From Figs. 4.10 and 4.11 it can be seen that any effort to reduce NOx such as
reducingflametemperatureorwater=steaminjectionresultsinanincreaseinCO;
thereforeabalancemustbestruckbetweentheeffortstoreduceNOxandCO.In
packaged boilers, in addition to using proper excess air and FGR, ensuring that
the combustion products do not leak to the convection pass from the furnace
helpstolowerCO.Someboilersthatusethetangenttubeconstructioninsteadof
the membrane wall design for the partition between the furnace and the
convection section have experienced leakage of hot furnace gases from the
furnacesidetotheconvectionsection;thetangenttubesarelikelytowarpdueto
thermal expansion during operation and allow gas to leak. The difference in gas
Copyright © 2003 Marcel Dekker, Inc.

pressure between the furnace and the convection section can be on the order of
10–30in.WCdependingontheboilerdesign,sotheleakagecouldbesignificant.
Inthatcasethefluegasesdonothavetheresidencetimeneededtocompletethe
combustionprocessinthefurnace,whichcanresultinhigherCOformation.The
presenceofwatervaporalsoincreasesCO.Increasingtheboilersizereducesboth
COandNOxbecausethefurnacetemperaturesandheatreleaseratesarereduced
andtheresidencetimeforCOconversiontoCO isincreased;however,thisadds
2
to the boiler cost.
Generally30–100ppmvofCOcanbeachievedwithmostpackagedboiler
burners in operation today and about 25–50ppmv in gas turbines. If single-digit
COemissionsarerequired,anoxidationcatalystissuggestedinpackagedboilers
and HRSGs, which can add to their cost and operating gas-side pressure drop.
CO 1O CO
þ2 2 ! 2
H C O CO H O
x yþ 2 ! 2þ 2
An oxidation catalyst increases the conversion of SO to SO , which can react
2 3
with ammoniatoformammoniumsulfate.However,withnaturalgasfuelwith a
low sulfur content, this is not a serious concern. This conversion is higher at
highertemperatures,sayat1100 F,anddecreasestoabout10%at600 Fwithout
(cid:2) (cid:2)
significantly affecting the efficiency of CO or formaldehyde removal. Good
combustion controls can also help reduce CO formation. VOCs are also some-
what reduced by oxidation catalysts.
The dry low-NOx (DLN) combustors used in gas turbines have demon-
strated CO levels of less than 5ppm.
Figure 4.7 shows the use of a CO catalyst in an HRSG. Generally, higher
temperatures on the order of 600–1000 Fare acceptable for CO catalysts, so the
(cid:2)
catalyst can be placed at the inlet of the unfired gas turbine HRSG. However,
when a burner is used in the HRSG, it is advisable to have another heat transfer
surfaceprecede it sothat the burnerflame doesnotimpinge on thecatalyst. The
COcatalystshouldalsoprecedetheNOxcatalysttokeepitawayfromammonia.
Typical CO conversion efficiency can range from 60% to 85%, though higher
values may be obtained. Depending on its size, the gas pressure drop across the
CO catalyst can range from 2 to 3in. WC. The cost of a typical CO catalyst is
about 50% of that of a SCR catalyst.
SOx REMOVAL
SulfurpresentinfuelsgetsconvertedtoSO ,andinthepresenceofacatalystthe
2
SO is converted to SO , which reacts with water vapor to form sulfuric acid
2 3
vapor. Sulfuric acid causes environmental damage through corrosion. SO and
2
SO aretogether referredtoasSOx.ThelevelofSOxdependsontheamountof
3
Copyright © 2003 Marcel Dekker, Inc.

sulfur presentinthefuel.Typically,95%ofthesulfurconvertstoSO and1–3%
2
converts to SO . Historically SOx pollution has been controlled through disper-
3
sion through theuseof tall stacks. However,in caseswherethis isnotadequate,
reductionmethodssuchasfluegasdesulfurization(FGD)areused.FGDinvolves
the use of scrubbers to remove SOx emissions from the flue gases. These are
classified as either regenerable or nonregenerable, depending on how the by-
products are disposed of. In regenerable systems, the sulfur or sulfuric acid is
recovered.However,these areexpensiveprocesses andarejustified onlyinlarge
high-sulfur coal-fired plants. Wet scrubbers using chemicals such as lime soda,
magnesium oxide, and limestone arewidely used in large utility plants. Because
manyofthesechemicalprocessesoccurbeyondtheboilerboundary,theyarenot
discussed here.
PARTICULATES
Emission particulates from combustion sources consist of compounds such as
sulfates, nitrates, and unburned compounds. Particulate matter emissions are
classifiedintotwocategories,PMandPM10,whichrefertoparticulates10mmor
more and less than 10mm in diameter, respectively. All particulates pose health
problems, but small particulates can be inhaled and can cause more damage to
humans than larger ones. PM levels from natural gas are lower than those from
oilsandcoals.HighashinfueloilsandcoalscanalsoincreasethePM.Inutility
boilers, electrostatic precipitators, scrubbers, or bag houses are used to remove
particulates.Thesesystemsincreasetheinstallationcostoftheplantandmaynot
be justified in small plants. Switching to low ash, low sulfur fuels also helps
reduce PM but adds to the cost of fuel.
VOLATILE ORGANIC COMPOUNDS
Volatile organic compounds (VOCs) are unburned hydrocarbons of higher
molecular weight than methane. Sources of VOCs include combustion products,
automobileexhaustsolvents,andpaints,tomentionafew.Whenreleasedintothe
atmosphere, VOCs contribute to the formation of harmful ozone and are health
hazards, particularly because of their high molecular weights. [Unburned hydro-
carbons (UHCs) are similar to VOCs but are of lower molecular weight and
characterized as methane.]
Good combustion techniques and the maintenance of high combustion
temperatures minimize VOC formation; however, they also increase NOx. In
chemical plants, incineration is generally adopted to minimize the emission of
VOCs. There are two types of oxidizers. Thermal oxidizers combust the VOCs
along with natural gas and maintain a gas temperature of 1500–1800 F with a
(cid:2)
few seconds of residence time, which destroys the VOCs. Catalytic oxidation
Copyright © 2003 Marcel Dekker, Inc.

requires a lower temperature, 500–700 F, and therefore consumes less natural
(cid:2)
gas.Heatrecoveryboilersmaybeusedbehindincineratorsforrecoveringenergy
from the flue gases, as discussed in Chapter 2. VOCs in packaged boilers are
reduced by using good combustion techniques. Oxidation catalysts also reduce
VOCs but are expensive.
CONCLUSION
ItiseasiertodesignforagivenNOxorCOlevelinanewboilerorHRSGthanin
an older one, because we can design around the various options and size the
boilerorHRSGaccordingly.ModifyinganexistingboilerorHRSGtomeetnew
emission levels presents more challenges. For example, the existing boiler
furnace dimensions may not be adequate if a low-NOx burner is retrofitted,
owingtopossibleflameimpingementconcerns.Theexistingfanmaynotbeable
to handle the increase in pressure drop if FGR is used. If an air heater is used it
must be replaced by an economizer. If a catalyst is required, an existing HRSG
may haveto operate in a gas temperature regime that may not be optimum for it
unless the heating surfaces are split. A different catalyst material capable of
operation at the gas temperature window available between the evaporator and
economizerorcapableofoperatingaheadoftheevaporatormayhavetobeused.
If there are space limitations, the designer may even have to reduce the boiler
capacity. Steam injection in the burner may be examined.
It is possible to improve the emissions of existing boilers through options
such as replacing the refractory-lined boilers with water-cooled furnaces, using
membrane walls where possible to minimize flue gas bypassing between the
furnace and convection bank, and using a low-NOx burner. With HRSGs, if
steam injection is introduced to minimize NOx, the effects of gas flow and
temperaturehavetobereviewedbecausetheymayaffecttheHRSGperformance.
In a new boiler or HRSG project, there are fewer constraints.
There are several ways to control NOx and CO in packaged boilers and
HRSGs, some of which affect the quantity of flue gases flowing through the
boiler, thus affecting the temperature profile, efficiency, and gas pressure drop.
Catalystsrequireaspecificgastemperaturewindowforefficientoperation,which
is achieved by modifying the boiler or HRSG design as discussed above. These
factors must be evaluated on a case-by-case basis, because no two boilers are
identical.InthecaseofgasturbineHRSGs,optimumlocationsmustbefoundfor
the SCR and the CO catalyst by considering the various loads and gas
temperature profiles. The cost of meeting the emission limits is quite large,
because boiler and HRSG designs have to be modified to incorporate catalysts,
dampers, and low-NOx burners. Operating costs are also increased due to the
highergaspressuredropacrosstheheatingsurfacesandducts.Thefanmayhave
to be replaced.
Copyright © 2003 Marcel Dekker, Inc.

TABLE4.4 Typical Allowable Emission Rates for a Combined Cycle Project in
California
Allowableemission rate
Unit Pollutant lb=h lb=MMBtu or pmvd
CTG=HRSG with ductfiring PM 28.2 0.012
SOx 5.7 0.0023
NOx 28.6 3ppmvdat 15%O
2
VOCs 35.2 0.015
CO 98.5 20ppmvdat 15%O
2
Formaldehyde 5.0 0.002
Auxiliaryboiler PM 0.19 0.005
SOx 0.09 0.0024
NOx 3.5 0.092
VOCs 0.49 0.013
CO 2.1 0.055
New plants evaluate the best available control technology (BACT) for
emissionsonthebasisofcost andenvironmental conditions.The costper tonof
pollutantremovedisestimated,andthebesttechnologytoachievethiswithinthe
maximum cost allowable ischosen. Emission limits vary depending on location.
TypicallimitsforacombinedcycleplantinCaliforniathatwerebothgasturbines
and auxiliary boilers are listed in Table 4.4.
As the technology improves, it is hoped that the cost of emission control
will also be reduced. For example, research work is going on to lower NOx and
COtosingle-digitpercentagesingas-firedburnersbyusinginternalrecirculation
ofpartialcombustionproductswithouttheuseoffluegasrecirculationandwhile
using lowexcessair. Thiswill lower operating costs and also improvethe boiler
efficiency.
REFERENCES
1. Catalogues.CoenCompany,Burlingame,CA.
2. V Burd. Squeezing clean energy from boilers and heaters. Chemical Engineering,
March1992.
3. P Bancel et al. Gas turbine NOx controlled with steam and water injection. Power
Engineering,June1986.
4. NalcoFuelTechBrochureonNOxoutprocess,1992.
5. D Lambert and TF McGowan. Nox control techniques for the CPI. Chemical
Engineering,June1996.
Copyright © 2003 Marcel Dekker, Inc.

6. S Drennen, V Lifshits. Developmental issues of ultra low NOx burners for steam
generation.PaperpresentedattheFallMeetingoftheWesternStatesSectionofthe
CombustionInstitute,DiamondBar,CA,Oct23–24,1997.
7. TWebster.BurnertechnologyforsingledigitNOxemissionsinboilerapplications,
CIBONOxControlConference,SanDiego,CA,Mar13,2001.
8. UseofSCRforcontrolofNOxemissionsfrompowerplantsintheUS.Preparedby
Synapse Energy Economics, Inc., Cambridge, MA, for the Ontario Clean Air
Program,Canada(ONTAIR),campaign,February2000.
9. SNaroozi.UreaenhancessafetyinSCRapplications.PowerEngineering,December
1993.
10. L Czarnecki. SCONOx—ammonia-free NOx removal technology for gas turbines.
InternationalJointPowerGenerationConference(IJPGC)-2000-15032,Florida,July
2000.
Copyright © 2003 Marcel Dekker, Inc.

5
Basic Steam Plant Calculations
5.01 Converting liquid flow in lb=h to gpm, and vice versa; relating density,
specific gravity, and specific volume
5.02 Relatingheadofliquidorgascolumntopressure;convertingfeetofliquid
topsi;relatinginchesofwatercolumnofgastopsiandfeetofgascolumn
5.03 Estimating density of gases; relating molecular weight and density; effect
of elevation on gas density; simplified formula for density of air and flue
gases at sea level
5.04 Relating actual and standard cubic feet of gas per minute to lb=h
5.05 Computing density of gas mixture; relating mass to volumetric flow;
computing velocity of gas in duct or pipe
5.06 Relating mass and linear velocities
5.07 Calculating velocity of wet and superheated steam in pipes; computing
specific volume of wet steam; use of steam tables
5.08 Relating boiler horsepower to steam output
5.09 Calculating amount of moisture in air; relative humidity and saturation
vapor pressure
5.10 Water dew point of air and flue gases; partial pressure of water vapor
5.11 Energyabsorbedbywetandsuperheatedsteaminboilers;enthalpyofwet
anddrysteam;useofsteamtables;convertingMMBtu=h(millionBtu=h)
to kilowatts
Copyright © 2003 Marcel Dekker, Inc.

5.12 Relating steam by volume, steam by weight, and steam quality; relating
circulation ratio and quality
5.13a Determining steam quality using throttling calorimeter
5.13b Relating steam quality to steam purity
5.14 Waterrequiredfordesuperheatingsteam;energybalanceinattemperators,
desuperheaters
5.15 Water required for cooling gas streams
5.16 Calculating steam volume after throttling process; use of steam tables
5.17 Determining blowdown and steam for deaeration
5.18 Calculating flash steam from boiler blowdown; economics of flash steam
recovery
5.19a Estimating leakage ofsteam through openings; effect of wetness ofsteam
on leakage
5.19b Estimating air flow through openings
5.20 Estimating leakage of gas across dampers; calculating energy loss of
leakage flow; sealing efficiency of dampers on area and flow basis
5.21 Economics of waste heat recovery; annual cost of energy loss; simple
payback period calculation
5.22 Life-cycle costing applied to equipment selection; interest and escalation
factors; capitalized and life-cycle cost
5.23 Life-cycle costing applied to evaluation of heat recovery systems
5.24 Calculating thickness of boiler tubes to ASME Code; allowable stresses
for various materials
5.25 Calculating maximum allowable working pressures for pipes
5.26 Sizing tubes subject to external pressure
5.27 On sound levels: OSHA permissible exposure levels
5.28 Adding decibels
5.29 Relating sound pressure and power levels
5.30 Effect of distance on noise level
5.31 Computing noise levels from engine exhaust
5.32 Holdup time in steam drum
5.01
Q:
Convert 50,000lb=h of hot water at a pressure of 1000psia and 390 F to gpm.
(cid:2)
A:
To convert from lb=h to gpm, or vice versa, for any liquid, we can use the
following expressions:
q
W 8 1
¼ v ð Þ
1
r 62:4s 2
¼ ¼ v ð Þ
Copyright © 2003 Marcel Dekker, Inc.

where
W flow, lb=h
¼
q flow, gpm (gallons per minute)
¼
r density of liquid, lb=cu ft
¼
s specific gravity of liquid
¼
v specific volume of liquid, cu ft=lb
¼
For hot water we can obtain the specific volume from the steam tables (see the
Appendix). v at 1000psia and 390 F is 0.0185cu ft=lb. Then, from Eq. (1),
(cid:2)
0:0185
q 50;000 115:6gpm
¼ (cid:4) 8 ¼
Forwaterattemperaturesof40–100 F,forquickestimateswedividelb=hby500
(cid:2)
to obtain gpm. For example, 50,000lb=h of water at 70 F would be 100gpm.
(cid:2)
5.02A
Q:
Estimate the head in feet developed by a pump when it is pumping oil with a
specific gravity of 0.8 through a differential pressure of 150psi.
A:
Conversion from feet of liquid to psi, or vice versa, is needed in pump
calculations. The expression relating the variables is
DP
H 144DPv 2:3 3
1 ¼ ¼ s ð Þ
where
DP differential pressure, psi
¼
H head, ft of liquid
1¼
Substituting for DP and s, we have
150
H 2:3 431:2ft
l ¼ (cid:4) 0:8 ¼
5.02B
Q:
If a fan develops 8in. WC (inches of water column) with a flue gas density of
0.05lb=cu ft, what is the head in feet of gas and in psi?
Copyright © 2003 Marcel Dekker, Inc.

A:
Use the expressions
DP
H 144 4
g ¼ r ð Þ
g
H 27:7DP 5
w ¼ ð Þ
where
H head, ft of gas
g¼
H head, in. WC
w¼
r gas density, lb=cu ft
g¼
Combining Eqs. (4) and (5), we have
8
H 144 835ft
g ¼ (cid:4)27:7 0:05¼
(cid:4)
8
DP 0:29psi
¼27:7¼
5.03
Q:
Estimate the density of air at 5000ft elevation and 200 F.
(cid:2)
A:
The density of any gas can be estimated from
P
r 492 MW 6
g ¼ (cid:4) (cid:4)359 460 t 14:7 ð Þ
(cid:4)ð þ Þ(cid:4)
where
P gas pressure, psia
¼
MW gas molecular weight (Table 5.1)
¼
t gas temperature, F
(cid:2)
¼
r gas density, lb=cu ft
g¼
The pressure of air decreases as the elevation increases, as shown in Table 5.2,
whichgivestheterm P=14:7 MWofair 29.Substitutingthevariousterms,
ð Þ(cid:4) ¼
we have
0:832
r 29 492 0:05lb=cuft
g ¼ (cid:4) (cid:4)359 660¼
(cid:4)
Copyright © 2003 Marcel Dekker, Inc.

TABLE5.1 GasMolecularWeights
Gas MW
Hydrogen 2.016
Oxygen 32.0
Nitrogen 28.016
Air 29.2
Methane 16.04
Ethane 30.07
Propane 44.09
n-Butane 58.12
Ammonia 17.03
Carbondioxide 44.01
Carbonmonoxide 28.01
Nitrous oxide 44.02
Nitric oxide 30.01
Nitrogendioxide 46.01
Sulfurdioxide 64.06
Sulfurtrioxide 80.06
Water 18.02
A simplified expression for air at atmospheric pressure and temperature t at sea
level is
40
r 7
g ¼460 t ð Þ
þ
Foragasmixturesuchasfluegas,themolecularweight(MW)canbeobtainedas
discussedinQ5.05.Intheabsenceofdataonfluegasanalysis,Eq.(7)alsogives
a good estimate of density.
TABLE5.2 Density Correction
forAltitude
Altitude (ft) Factor
0 1.0
1000 0.964
2000 0.930
3000 0.896
4000 0.864
5000 0.832
6000 0.801
7000 0.772
8000 0.743
Copyright © 2003 Marcel Dekker, Inc.

When sizing fans, it is the usual practice to refer to 70 Fand sea level as
(cid:2)
standard conditions for air or flue gas density calculations.
5.04A
Q:
Howisacfm(actualcubicfeetperminute)computed,andhowdoesitdifferfrom
scfm (standard cubic feet per minute)?
A:
acfmiscomputedusingthedensityofthegasatgivenconditionsofpressureand
temperature, and scfm is computed using the gas density at 70 F and sea level
(cid:2)
(standard conditions).
W
q 8
¼60r ð Þ
g
where
q gasflowinacfm(at70 Fandsealevel,scfmandacfmareequal;then
(cid:2)
¼
q W=4:5)
¼
r gas density in lb=cu ft (at standard conditions r 0:075lb=cuft
g¼ g ¼ Þ
W gas flow in lb=h 4:5q at standard conditions
¼ ¼
5.04B
Q:
Convert 10,000lb=h of air to scfm.
A:
Using Eq. (6), it can be shown that at P 14:7 and t 70, for air
¼ ¼
r 0:075lb=cuft.
g ¼
Hence, from Eq. (8),
10;000
q 2222scfm
¼60 0:075¼
(cid:4)
5.04C
Q:
Convert 3000scfm to acfm at 35 psia and 275 F. What is the flow in lb=h? The
(cid:2)
fluid is air.
Copyright © 2003 Marcel Dekker, Inc.

A:
Calculate the density at the actual conditions.
35
r 29 492 0:129lb=cuft
g ¼ (cid:4) (cid:4)359 735 14:7¼
(cid:4) (cid:4)
From the above,
W 4:5 3000 13;500lb=h
¼ (cid:4) ¼
Hence
13;500
acfm 1744cfm
¼60 0:129¼
(cid:4)
5.05
Q:
In a process plant, 35,000lb=h of flue gas having a composition N 75%,
2 ¼
O 2%,CO 15%,andH O 8%,allbyvolume,flowsthroughaductof
cr 2 os ¼ s section 2 3 ¼ ft2 at a tempe 2 ratu ¼ re of 350 F. Estimate the gas density and
(cid:2)
velocity.Becausethegaspressureisonlyafewinchesofwatercolumn,forquick
estimates the gas pressure may be taken as atmospheric.
A:
Tocomputethedensityofagas,weneeditsmolecularweight.Foragasmixture,
molecular weight is calculated as follows:
MW MW y
¼ ð i(cid:4) iÞ
where P
y volume fraction of gas i
i¼
MW molecular weight of gas i
i¼
Hence
MW 0:75 28 0:02 32 0:15 44
¼ (cid:4) þ (cid:4) þ (cid:4)
0:08 18 29:68
þ (cid:4) ¼
From Eq. (6),
492
r 29:68 0:05lb/cu ft
g ¼ (cid:4)359 810¼
(cid:4)
The gas velocity V can be obtained as
g
W
V 9
g ¼60r A ð Þ
g
Copyright © 2003 Marcel Dekker, Inc.

where
V velocity, fpm (feet per minute)
A
g¼
cross section, ft2
¼
Hence
35;000
V 3888fpm
g ¼60 0:05 3¼
(cid:4) (cid:4)
The normal range of air or flue gas velocities in ducts is 2000–4000fpm.
Equation (9) can also be used in estimating the duct size.
Inthe absence offluegas analysis,we could haveused Eq. (7)to estimate
the gas density.
5.06
Q:
A term that is frequently used by engineers to describe the gas flow rate across
heating surfaces is gasmass velocity. How dowe convert this to linear velocity?
Convert 5000lb=ft2 h of hot air flow at 130 Fand atmospheric pressure to fpm.
(cid:2)
A:
Use the expression
G
V 10
g ¼60r ð Þ
g
where G is the gas mass velocity in lb=ft2 h. Use Eq. (7) to calculate r .
g
40
r 0:0678lb/cu ft
g ¼460 130¼
þ
Hence
5000
V 1230fpm
g ¼60 0:0678¼
(cid:4)
5.07A
Q:
What is the velocity when 25,000lb=h of superheated steam at 800 psia and
900 F flows through a pipe of inner diameter 2.9in.?
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

A:
Use expression (11) to determine thevelocityof any fluid inside tubes, pipes, or
cylindrical ducts.
v
V 0:05 W 11
¼ (cid:4) (cid:4)d2 ð Þ
i
where
V velocity, fps
¼
v specific volume of the fluid, cu ft=lb
¼
d inner diameter of pipe, in.
i¼
For steam, v can be obtained from the steam tables in the Appendix.
v 0:9633cu ft/lb
¼
Hence
0:9633
V 0:05 25;000 143fps
¼ (cid:4) (cid:4) 2:92 ¼
The normal ranges of fluid velocities are
Water: 3–12fps
Steam: 100–200fps
5.07B
Q:
Estimate thevelocity of 70% quality steam in a 3in. schedule 80 pipewhen the
flow is 45,000lb=h and steam pressure is 1000psia.
A:
We need to estimate the specific volume of wet steam.
v xv 1 x v
¼ gþð (cid:3) Þ f
wherev andv arespecificvolumesofsaturatedvaporandliquidatthepressure
g f
inquestion,obtainedfromthesteamtables,andxisthesteamquality(seeQ5.12
for a discussion of x). From the steam tables, at 1000psia, v 0.4456 and
g¼
v 0.0216cu ft=lb. Hence the specific volume of wet steam is
f ¼
v 0:7 0:4456 0:3 0:0216 0:318cuft=lb
¼ (cid:4) þ (cid:4) ¼
The pipe inner diameter d from Table 5.3 is 2.9 in. Hence, from Eq. (11),
i
0:318
V 0:05 45;000 85fps
¼ (cid:4) (cid:4) 2:92 ¼
Copyright © 2003 Marcel Dekker, Inc.

5.08
Q:
What is meant by boiler horsepower? How is it related to steam generation at
different steam parameters?
A:
Packagedfiretubeboilersaretraditionallyratedandpurchasedintermsofboiler
horsepower (BHP). BHP refers to a steam capacity of 34.5lb=h of steam at
atmosphericpressurewithfeedwaterat212 F.However,aboilerplantoperatesat
(cid:2)
different pressures and with different feedwater temperatures. Hence conversion
between BHP and steam generation becomes necessary.
33;475 BHP
W (cid:4) 12
¼ Dh ð Þ
where
W steam flow, lb=h
¼
Dh enthalpy absorbed by steam and water h h BD h h
¼ ¼ð g(cid:3) fwÞþ ð f (cid:3) fwÞ
where
h enthalpy of saturated steam at operating steam pressure, Btu=lb
g¼
h enthalpy of saturated liquid, Btu=lb
f ¼
h enthalpy of feedwater, Btu=lb
fw¼
BD blowdown fraction
¼
For example, if a 500BHP boiler generates saturated steam at 125psig with 5%
blowdown and with feedwater at 230 F, the steam generation at 125psig will be
(cid:2)
500 33;475
W (cid:4)
¼ 1193 198 0:05 325 198
ð (cid:3) Þþ (cid:4)ð (cid:3) Þ
16;714lb=h
¼
where 1193, 198, and 325 are the enthalpies of saturated steam, feedwater, and
saturated liquid, respectively, obtained from steam tables. (See Appendix.)
5.09A
Q:
Why do we need to know the amount of moisture in air?
A:
Incombustioncalculations(Chap.6)weestimatethequantityofdryair required
toburnagivenamountoffuel.Inreality,atmosphericairisneverdry;itconsists
of some moisture, depending on the relativehumidity and dry bulb temperature.
To compute the partial pressure of water vapor in the fluegas, which is required
Copyright © 2003 Marcel Dekker, Inc.

TABLE5.3 Dimensions ofIron SteelPipe (IPS)
Surfaceper
linearft
Nominal Flowarea (ft2=ft) Weight
pipesize, Schedule perpipe perlinft
IPS (in.) OD (in.) no. ID (in.) (in.2) Outside Inside (lbsteel)
1 0.405 40a 0.269 0.058 0.106 0.070 0.25
3
80b 0.215 0.036 0.056 0.32
1 0.540 40a 0.364 0.104 0.141 0.095 0.43
4
80b 0.302 0.072 0.079 0.54
2 0.675 40a 0.493 0.192 0.177 0.129 0.57
3
80b 0.423 0.141 0.111 0.74
1 0.840 40a 0.622 0.304 0.220 0.163 0.85
2
80b 0.546 0.235 0.143 1.09
3 1.05 40a 0.824 0.534 0.275 0.216 1.13
4
80b 0.742 0.432 0.194 1.48
1 1.32 40a 1.049 0.864 0.344 0.274 1.68
80b 0.957 0.718 0.250 2.17
11 1.66 40a 1.380 1.50 0.435 0.362 2.28
4
80b 1.278 1.28 0.335 3.00
11 1.90 40a 1.610 2.04 0.498 0.422 2.72
2
80b 1.500 1.76 0.393 3.64
2 2.38 40a 2.067 3.35 0.622 0.542 3.66
80b 1.939 2.95 0.508 5.03
21 2.88 40a 2.469 4.79 0.753 0.647 5.80
2
80b 2.323 4.23 0.609 7.67
3 3.50 40a 3.068 7.38 0.917 0.804 7.58
80b 2.900 6.61 0.760 10.3
4 4.50 40a 4.026 12.7 1.178 1.055 10.8
80b 3.826 11.5 1.002 15.0
6 6.625 40a 6.065 28.9 1.734 1.590 19.0
80b 5.761 26.1 1.510 28.6
8 8.625 40a 7.981 50.0 2.258 2.090 28.6
80b 7.625 45.7 2.000 43.4
10 10.75 40a 10.02 78.8 2.814 2.62 40.5
60 9.75 74.6 2.55 54.8
12 12.75 30 12.09 115 3.338 3.17 43.8
14 14.0 30 13.25 138 3.665 3.47 54.5
16 16.0 30 15.25 183 4.189 4.00 62.6
18 18.0 20c 17.25 234 4.712 4.52 72.7
20 20.0 20 19.25 291 5.236 5.05 78.6
22 22.0 20c 21.25 355 5.747 5.56 84.0
24 24.0 20 23.25 425 6.283 6.09 94.7
aCommonlyknownasstandard.
bCommonlyknownasextraheavy.
cApproximately.
Copyright © 2003 Marcel Dekker, Inc.

for calculating nonluminous heat transfer, we need to know the total quantity of
water vapor in flue gases, a part of which comes from combustion air.
Also, when atmospheric air is compressed, the saturated vapor pressure
(SVP) of water increases, and if the air is cooled below the corresponding water
dewpointtemperature,watercancondense.Theamountofmoistureinairorgas
fixesthewaterdewpoint,soitisimportanttoknowtheamountofwatervaporin
air or flue gas.
5.09B
Q:
Estimate the pounds of water vapor to pounds of dry air when the dry bulb
temperature is 80 Fand the relative humidity is 65%.
(cid:2)
A:
Use the equation
p
M 0:622 w 13
¼ (cid:4)14:7 p ð Þ
(cid:3) w
where
M lb water vapor=lb dry air
¼
p partial pressure of water vapor in air, psia
w¼
This may be estimated as the vol% of water vapor total air pressure or as the
(cid:4)
product of relative humidity and the saturated vapor pressure (SVP). From the
steamtableswenotethatat80 F,SVP 0.5069psia(at212 F,SVP 14.7psia).
(cid:2) (cid:2)
¼ ¼
Hence p 0.65 0.5069.
w¼ (cid:4)
0:5069
M 0:622 0:65 0:0142
¼ (cid:4) (cid:4)14:7 0:65 0:5069¼
(cid:3) (cid:4)
Hence, if we needed 1000lb of dry air for combustion, wewould size the fan to
deliver 1000 1.0142 1014.2lb of atmospheric air.
(cid:4) ¼
5.10A
Q:
What is the water dew point of the flue gases discussed in Q5.05?
A:
Thepartialpressureofwater vaporwhenthevol%is8andtotalpressureis14.7
psia will be
p 0:08 14:7 1:19psia
w ¼ (cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

From the steam tables, we note that the saturation temperature corresponding to
1.19psiais107 F.Thisisalsothewaterdewpoint.Ifthegasesarecooledbelow
(cid:2)
this temperature, water can condense, causing problems.
5.10B
Q:
What is the water dew point of compressed air when ambient air at 80 F,
(cid:2)
14.7psia, and a relative humidity of 65% is compressed to 35psia?
A:
Use the following expression to get the partial pressure of water vapor after
compression:
P
p p 2 14
w2 ¼ w1(cid:4)P ð Þ
1
where
p partial pressure, psia
w¼
P total pressure, psia
¼
The subscripts 1 and 2 stand for initial and final conditions. From Q5.09b,
p 0.65 0.5069.
w1¼ (cid:4)
35
p 0:65 0:5069 0:784psia
w2 ¼ (cid:4) (cid:4)14:7¼
From the steam tables, we note that corresponding to 0.784psia, the saturation
temperatureis93 F.Thisisalsothedewpointaftercompression.Coolingtheair
(cid:2)
to below 93 F would result in its condensation.
(cid:2)
5.11A
Q:
Calculatetheenergyabsorbedbysteaminaboilerif400,000 lb=hofsuperheated
steam at 1600psia and 900 F is generated with feedwater at 250 F. What is the
(cid:2) (cid:2)
energy absorbed, in megawatts?
A:
The energy absorbed is given by
Q W h h (neglecting blowdown) 15
¼ (cid:4)ð 2(cid:3) 1Þ ð Þ
where
W steam flow, lb=h
¼
h ;h steam enthalpy and water enthalpy, Btu=lb
2 1¼
Q duty, Btu=h
¼
Copyright © 2003 Marcel Dekker, Inc.

From the steam tables, h 1425.3Btu=lb and h 224Btu=lb.
2¼ 1¼
Q 400;000 1425:3 224
¼ (cid:4)ð (cid:3) Þ
480:5 106 Btu=h
¼ (cid:4)
480:5million Btu/h(MM Btu/h)
¼
Using the fact that 3413Btu=h 1kW, we have
¼
106
Q 480:5 141MW
¼ (cid:4)3413 103 ¼
(cid:4)
5.11B
Q:
Estimatetheenergyabsorbedbywetsteamat80%qualityinaboilerat1600psia
when the feedwater temperature is 250 F.
(cid:2)
A:
The enthalpy of wet steam can be computed as
h xh 1 x h 16
¼ gþð (cid:3) Þ f ð Þ
wherehistheenthalpyinBtu=lb.Thesubscriptsgandf standforsaturatedvapor
andliquidatthereferencedpressure,obtainedfromsaturatedsteamproperties.x
is the steam quality fraction.
From the steam tables,h 1163Btu=lbandh 624Btu=lbat 1600psia.
g¼ f ¼
The enthalpy of feedwater at 250 F is 226Btu=lb.
(cid:2)
h 0:8 1163 0:2 624 1054Btu=lb
2 ¼ (cid:4) þ (cid:4) ¼
h 226Btu=lb
1 ¼
Q 1054 226 828Btu=lb
¼ (cid:3) ¼
If steam flow were 400,000lb=h, then
Q 400;000 828 331 106 331MMBtu=h
¼ (cid:4) ¼ (cid:4) ¼
5.12
Q:
How is the wetness in steam specified? How do we convert steam by volume
(SBV) to steam by weight?
Copyright © 2003 Marcel Dekker, Inc.

A:
A steam–water mixture is described by the term quality, x, or dryness fraction.
x 80% means that in 1lb of wet steam, 0.8lb is steam and 0.2lb is water. To
¼
relate these two terms, we use the expression
100
SBV 17
¼1 100 x =x v =v ð Þ
þ½ð (cid:3) Þ (cid:5)(cid:4) f g
where
v ;v specific volumes of saturated liquid and vapor, cu ft=lb
f g¼
x quality or dryness fraction
¼
From the steam tables at 1000psia, v 0:0216 and v 0.4456 cu ft=lb.
f ¼ g¼
100
SBV 98:8%
¼1 100 80 =80 0:0216=0:4456¼
þ½ð (cid:3) Þ (cid:5)(cid:4)
Circulationratio(CR)isanothertermusedbyboilerengineerstodescribe
the steam quality generated.
1
CR 18
¼ x ð Þ
A CR of 4 means that the steam quality is 0.25 or 25%; in other words, 1lb of
mixture would have 0.25lb of steam and the remainder would be water.
5.13A
Q:
How is the quality of steam determined using a throttling calorimeter?
A:
Throttling calorimeters (Fig. 5.1) are widely used in low pressure steam boilers
fordeterminingthemoistureorwetness(quality)ofsteam.Asamplingnozzleis
locatedpreferablyintheverticalsectionofthesaturatedsteamlinefarfrombends
or fittings. Steam enters the calorimeter through a throttling orifice and passes
intoawell-insulatedexpansionchamber.Knowingthatthrottlingisanisoenthal-
pic process, we can rewrite Eq. (16) for enthalpy balance as
h h xh 1 x h
s ¼ m ¼ gþð (cid:3) Þ f
where
h ;h ;h ;h enthalpiesofsteam,mixture,saturatedliquid,andsaturated
s m f g¼
steam, respectively
x steam quality fraction
¼
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 5.1 Throttling calorimeter.
The steam temperature after throttling is measured at atmospheric pressure, and
thentheenthalpyisobtainedwiththehelpofsteamtables.Thesteamisusuallyin
superheated condition after throttling.
Example
Athrottlingcalorimeter measuresasteamtemperatureof250 Fwhenconnected
(cid:2)
to a boiler operating at 100psia. Determine the steam quality.
Solution. h at atmospheric pressure and at 250 F 1168.8 Btu=lb from
s (cid:2) ¼
steam tables; h 1187.2 and h 298.5Btu=lb, also from steam tables. Hence
g¼ f ¼
1168:8 1187:2x 1 x 298:5
¼ þð (cid:3) Þ
or
x 0:979or97:9%quality
¼
5.13B
Q:
How is steam quality related to steam purity?
Copyright © 2003 Marcel Dekker, Inc.

A:
Steampurityreferstotheimpuritiesinwetsteam,inppm.Atypicalvalueinlow
pressureboilerswouldbe1ppmofsolids.However,qualityreferstothemoisture
in steam.
The boiler drum maintains a certain concentration of solids depending on
ABMAorASMErecommendationsasdiscussedinQ5.17.Ifat500psigpressure
the boiler water concentration is 2500ppm, and if steam should have 0.5ppm
solids, then the quality can be estimated as follows:
0:5
% Moisture in steam 100 0:02%
¼2500(cid:4) ¼
or
Steam quality 100 0:02 99:98%
¼ (cid:3) ¼
5.14
Q:
How do we estimate the water required for desuperheating steam? Superheated
steamat700psiaand800 Fmustbecooledto700 Fbyusingasprayofwaterat
(cid:2) (cid:2)
300 F. Estimate the quantity of water needed to do this.
(cid:2)
A:
From an energy balance across the desuperheater, we get
W h Wh W h 19a
1 1þ f ¼ 2 2 ð Þ
where
W ;W steam flows before and after desuperheating
1 2¼
W water required
¼
h ;h steam enthalpies before and after the process
1 2¼
h enthalpy of water
f ¼
Also, from mass balance,
W W W
2 ¼ 1þ
Hence we can show that
h h
W W 1(cid:3) 2 19b
¼ 2(cid:4)h h ð Þ
1(cid:3) f
Neglecting the pressure drop across the desuperheater, we have from the steam
tables h 1403, h 1346, and h 271, all in Btu=lb. Hence W=W 0.05.
1¼ 2¼ f ¼ 2¼
That is, 5% of the final steam flow is required for injection purposes.
Copyright © 2003 Marcel Dekker, Inc.

5.15
Q:
How is the water requirement for cooling a gas stream estimated? Estimate the
water quantity required to cool 100,000lb=h of flue gas from 900 F to 400 F.
(cid:2) (cid:2)
What is the final volume of the gas?
A:
From an energy balance it can be shown [1] that
q 5:39 10 4 t t
¼ (cid:4) (cid:3) (cid:4)ð1(cid:3) 2Þ
W 20
ð Þ
(cid:4)1090 0:45 t 150
þ (cid:4)ð2(cid:3) Þ
where
q water required, gpm
¼
t ;t initial and final gas temperatures, F
1 2¼ (cid:2)
W gas flow entering the cooler, lb=h
¼
Substitution yields
q 5:39 10 4 900 400
(cid:3)
¼ (cid:4) (cid:4)ð (cid:3) Þ
100;000
(cid:4)1090 0:45 400 150
þ (cid:4)ð (cid:3) Þ
23gpm
¼
The final gas volume is given by the expression
W
460 t 0:341
ð þ 2Þ(cid:4) 2361þ
(cid:1) (cid:2)
The final volume is 43,000acfm.
5.16
Q:
In selecting silencers for vents or safety valves, we need to figure thevolume of
steamafterthethrottlingprocess.Estimatethevolumeofsteamwhen60,000lb=h
ofsuperheatedsteamat650 psiaand800 Fisblowntotheatmospherethrougha
(cid:2)
safety valve.
A:
We have to find the final temperature of steam after throttling, which may be
considered an isoenthalpic process; that is, the steam enthalpy remains the same
at 650 and 15psia.
Copyright © 2003 Marcel Dekker, Inc.

From the steam tables, at 650psia and 800 F, h 1402Btu=lb. At 15psia
(cid:2)
¼
(atmospheric conditions), the temperature corresponding to an enthalpy of
1402Btu=lb is 745 F. Again from the steam tables, at a pressure of 15psia and
(cid:2)
a temperature of 745 F, the specific volume of steam is 48cu ft=lb. The total
(cid:2)
volume of steam is 60,000 48 2,880,000cu ft=h.
(cid:4) ¼
5.17
Q:
How do we determine the steam required for deaeration and boiler blowdown
water requirements?
A:
Steam plant engineers have to frequently perform energy and mass balance
calculationsaroundthedeaeratorandboilertoobtainthevaluesofmakeupwater,
blowdown, or deaeration steam flows. Boiler blowdownquantity depends on the
total dissolved solids (TDS) of boiler water and the incoming makeup water.
Figure5.2showstheschemearoundasimpledeaerator.Notethattherecouldbe
severalcondensatereturns.Thisanalysisdoesnotconsiderventingofsteamfrom
the deaerator or the heating of makeup using the blowdown water. These
refinements can be done later to fine-tune the results.
The American Boiler Manufacturers Association (ABMA) and ASME
provide guidelines on the TDS of boiler water as a function of pressure (see
Tables5.4and5.5.Thedrumsolidsconcentrationcanbeatorlessthanthevalue
shown in these tables. Plant water chemists usually set these values after
reviewing the complete plant chemistry.
FIGURE 5.2 Scheme ofdeaeration system.
Copyright © 2003 Marcel Dekker, Inc.

TABLE5.4 Suggested Water QualityLimitsa
Boiler type:Industrial watertube,high duty,primaryfuelfired, drum type
Makeup waterpercentage:Up to 100%of feedwater
Conditions: Includessuperheater,turbine drives,or processrestriction onsteam purity
Drumoperatingpressureb, 0–2.07 2.08–3.10 3.11–4.14 4.15–5.17 5.18–6.21 6.22–6.89 6.90–10.34 10.35–13.79
MPa(psig) (0–300) (301–450) (451–600) (601–750) (751–900) (901–1000) (1001–1500) (1501–2000)
Feedwaterc
Dissolved oxygen(mg=LO ) <0.04 <0.04 <0.007 <0.007 <0.007 <0.007 <0.007 <0.007
2
measured beforeoxygen
scavengeradditiond
Total iron(mg=LFe) 0.100 0.050 0.030 0.025 0.020 0.020 0.010 0.010
(cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6)
Total copper (mg=LCu) 0.050 0.025 0.020 0.020 0.015 0.015 0.010 0.010
(cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6)
Totalhardness(mg=LCaCO ) 0.300 0.300 0.200 0.200 0.100 0.050 n.d. n.d.
3 (cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6)
pH range@25 C 7.5–10.0 7.5–10.0 7.5–10.0 7.5–10.0 7.5–10.0 8.5–9.5 9.0–9.6 9.0–9.6
(cid:2)
Chemicalsforpreboiler Use onlyvolatilealkaline materials
system protection
Nonvolatile TOCs <1 <1 <0.5 <0.5 <0.5 —Aslowaspossible, <0.2—
(mg=LC)e
Oily matter(mg=L) <1 <1 <0.5 <0.5 <0.5 —Aslowaspossible, <0.2—
Boiler water
Silica(mg=LSiO ) 150 90 40 30 20 8 2 1
Total alkalinity(m 2 g=LCaCO ) < (cid:6) 350f < (cid:6) 300f < (cid:6) 250f < (cid:6) 200f < (cid:6) 150f < (cid:6) 100f n (cid:6) .s.g n (cid:6) .s.g
3
Freehydroxide alkalinity n.s. n.s. n.s. n.s. n.d.g n.d.g n.d.g n.dg
(mg=LCaCO )h
3
Specificconductance <3500i <3000i 2500i <2000i <1500i <1000i 150 100
(cid:6) (cid:6)
(mmho=cm)@25 Cwithout
(cid:2)
neutralization
Copyright © 2003 Marcel Dekker, Inc.

n.d. notdetectable;n.s. notspecified.
aNo ¼ valuesaregivenforsa ¼ turatedsteampuritytargetbecausesteampurityachievabledependsuponmanyvariables,includingboilerwatertotal
alkalinityandspecificconductanceaswellasdesignofboiler,steamdruminternals,andoperatingconditions(seefootnotei).Becauseboilersin
thiscategoryrequirearelativelyhighdegreeofsteampurity,otheroperatingparametersmustbesetaslowasnecessarytoachievethishigh
purityforprotectionofthesuperheatersandturbinesand=ortoavoidprocesscontamination.
bWithlocalheatfluxes >473.2kW=m2(>150,000Btu=hft2),usevaluesforthenexthigherpressurerange.
cBoilersbelow6.21MPa(900psig)withlargefurnaces,largesteamreleasespace,andinternalchelant,polymer,and=orantifoamtreatmentcan
sometimestoleratehigherlevelsoffeedwaterimpuritiesthanthoseinthetableandstillachieveadequatedepositioncontrolandsteampurity.
Removaloftheseimpuritiesbyexternalpretreatmentisalwaysamorepositivesolution.Alternativesmustbeevaluatedastopracticalityand
economicsineachcase.
dValuesintableassumetheexistenceofadeaerator.
eNonvolatileTOCsaretheorganiccarbonnotintentionallyaddedaspartofthewatertreatmentregime.
fMaximumtotalalkalinityconsistentwithacceptablesteampurity.Ifnecessary,shouldoverrideconductanceasblowdowncontrolparameter.If
makeup is demineralized water at 4.14–6.89MPa (600–1000psig), boiler water alkalinity and conductance should be that in table for 6.90–
10.34MPa(1001–1500psig)range.
g‘‘Notdetectable’’inthesecasesreferstofreesodiumorpotassiumhydroxidealkalinity.Somesmallvariableamountoftotalalkalinitywillbe
presentandmeasurablewiththeassumedcongruentorcoordinatedphosphatepHcontrolorvolatiletreatmentemployedatthesehighpressure
ranges.
hMinimum levelof OH(cid:3) alkalinityin boilers below6.21MPa(900psig) mustbeindividuallyspecified withregard tosilicasolubility andother
componentsofinternaltreatment.
iMaximumvaluesareoftennotachievablewithoutexceedingsuggestedmaximumtotalalkalinityvalues,especiallyinboilersbelow6.21MPa
(900psig)with >20%makeupofwaterwhosetotalalkalinityis >20%ofTDSnaturallyorafterpretreatmentwithsodalimeorsodiumcycleion-
exchangesoftening.Actualpermissibleconductancevaluestoachieveanydesiredsteampuritymustbeestablishedforeachcasebycareful
steampuritymeasurements.Relationshipbetweenconductanceandsteampurityisaffectedbytoomanyvariablestoallowitsreductiontoa
simplelistoftabulatedvalues.
Source:AdaptedfromASME1979Consensus.
Copyright © 2003 Marcel Dekker, Inc.

Example
A boiler generates 50,000lb=h of saturated steam at 300psia, out of which
10,000lb=h is taken for process and returns to the deaerator as condensate at
180 F. The rest is consumed. Makeup water enters the deaerator at 70 F, and
(cid:2) (cid:2)
steamisavailableat300psiafordeaeration.Thedeaeratoroperatesatapressure
of25psia.Theblowdownhasatotaldissolvedsolids(TDS)of1500ppm,andthe
makeup has 100ppm TDS.
Evaluate the water requirements for deaeration steam and blowdown.
Solution. From mass balance around the deaerator,
10;000 D M F 50;000 B 21
þ þ ¼ ¼ þ ð Þ
TABLE5.5 RecommendedBoilerWaterLimitsandAssociatedSteamPurityat
Steady-StateFull LoadOperation—Water Tube Drum-TypeBoilers
Suspended TDS range,b,c
Drum TDS range,a Rangetotal solids steam (ppm)
pressure boiler water alkalinity,bboiler boiler water (maxexpected
(psig) (ppm)(max) water(ppm) (ppm)(max) value)
0–300 700–3500 140–700 15 0.2–1.0
301–450 600–3000 120–600 10 0.2–1.0
451–600 500–2500 100–500 8 0.2–1.0
601–750 200–1000 40–200 3 0.1–0.5
751–900 150–750 30–150 2 0.1–0.5
901–1000 125–625 25–125 1 0.1–0.5
1001–1800 100 —d 1 0.1
1801–2350 50 n.a. 0.1
2351–2600 25 n.a. 0.05
2601–2900 15 n.a. 0.05
Once-throughboilers
1400andabove 0.05 n.a. n.a. 0.05
n.a. notavailable.
aAct ¼ ualvalueswithintherangereflecttheTDSinthefeedwater.Highervaluesareforhigh
solidsinthefeedwater,lowervaluesforlowsolids.
bActualvalueswithintherangearedirectlyproportionaltotheactualvalueofTDSofboiler
water.Highervaluesareforthehighsolidsintheboilerwater,lowervaluesforlowsolids.
cThesevaluesareexclusiveofsilica.
dDictatedbyboilerwatertreatment.
Source:AmericanBoilerManufacturersAssociation,1982.
Copyright © 2003 Marcel Dekker, Inc.

From an energy balance around the deaerator,
10;000 148 1202:8 D M 38 209 F 209 50;000 B
(cid:4) þ (cid:4) þ (cid:4) ¼ (cid:4) ¼ (cid:4)ð þ Þ
22
ð Þ
From a balance of solids concentration,
100 M 1500 B 23
(cid:4) ¼ (cid:4) ð Þ
InEq.(22),1202.8istheenthalpyofthesteamusedfordeaeration,209the
enthalpy of boiler feedwater, 148 the enthalpy of the condensate return, and 38
thatofthemakeup,allinBtu=lb.Theequationassumesthattheamountofsolids
inreturningcondensateandsteamisnegligible,whichistrue.Steamusuallyhas
aTDSof1ppmorless,andsodoesthecondensate.Hence,forpracticalpurposes
we can neglect it. The net solids enter the system in the form of makeup water
and leave as blowdown. There are three unknowns—D, M, and B—and three
equations. From Eq. (21),
D M 40;000 B 24
þ ¼ þ ð Þ
Substituting (23) into (24),
D 15B 40;000 B2
þ ¼ þ
or
D 14B 40;000 25
þ ¼ ð Þ
From (22),
1;480;000 1202:8D 38 15B
þ þ (cid:4)
209 50;000 209B
¼ (cid:4) þ
Solving this equation, we have B 2375lb=h, D 6750lb=h, M 35,625lb=h,
¼ ¼ ¼
and F 52,375lb=h. Considering venting of steam from the deaerator to expel
¼
dissolved gases and the heat losses, 1–3% more steam may be consumed.
5.18
Q:
How can the boiler blowdown be utilized? A 600psia boiler operates for 6000h
annually and discharges 4000lb=h of blowdown. If this is flashed to steam at
100psia, how much steam is generated? If the cost of the blowdown system is
$8000,howlongdoespaybacktake?Assumethatthecostofsteamis$2=1000lb.
Copyright © 2003 Marcel Dekker, Inc.

A:
To estimate the flash steam produced we may use the expression
h xh 1 x h 26
¼ gþð (cid:3) Þ f ð Þ
where
h enthalpy of blowdown water at high pressure, Btu=lb
¼
h ;h enthalpies of saturated steam and water at the flash pressure,
g f ¼
Btu=lb
x fraction of steam that is generated at the lower pressure
¼
From the steam tables, at 600psia, h 471:6, and at 100psia, h 1187 and
¼ g ¼
h 298, all in Btu=lb. Using Eq. (26), we have
f ¼
471:6 1187x 1 x 298
¼ þð (cid:3) Þ(cid:4)
or
x 0:195
¼
About20%oftheinitialblowdownisconvertedtoflashsteam,thequantity
being 0.2 4000 800lb=h. This 800lb=h of 100psia steam can be used for
(cid:4) ¼
process. The resulting savings annually will be
6000
800 2 $9600
(cid:4) (cid:4)1000¼
Simple payback will be 8000=9600 0.8 year or about 10 months.
¼
Tablesareavailablethatgivetheflashsteamproducediftheinitialandflash
pressures are known. Table 5.6 is one such table.
5.19A
Q:
Estimate the leakage of steam through a hole 1=8in. in diameter in a pressure
vessel at 100psia, the steam being in a saturated condition.
A:
The hourly loss of steam in lb=h is given by [2]
AP
W 50 27
¼ 1 0:00065 t t ð Þ
þ ð (cid:3) satÞ
where
W steam leakage, lb=h
A ¼ hole area, in.2
¼
P steam pressure, psia
¼
t;t steam temperature and saturated steam temperature, F
sat¼ (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

TABLE5.6 SteamFlashand HeatContent atDifferential Temperatures
Initial Temp. of Percentofflash atreducedpressures
pressure liquid Atm.
(psig) F pressure 5lb 10lb 15lb 20lb 25lb 30lb 35lb 40lb
(cid:2)
ð Þ
100 338 13 11.5 10.3 9.3 8.4 7.6 6.9 6.3 5.5
125 353 14.5 13.3 11.8 10.9 10 9.2 8.5 7.9 7.2
150 366 16 14.6 13.2 12.3 11.4 10.6 9.9 9.3 8.5
175 377 17 15.8 14.4 13.4 12.5 11.6 11.1 10.4 9.7
200 388 18 16.9 15.5 14.6 13.7 12.9 12.2 11.6 10.9
225 397 19 17.8 16.5 15.5 14.7 13.9 13.2 12.6 11.9
250 406 20 18.8 17.4 16.5 15.6 14.9 14.2 13.6 12.9
300 421 21.5 20.3 19 18 17.2 16.5 15.8 15.2 14.5
350 435 23 21.8 20.5 19.5 18.7 18 17.3 16.7 16
400 448 24 23 21.8 21 20 19.3 18.7 18.1 17.5
450 459 25 24.3 23 22 21.3 20 19.9 19.3 18.7
500 470 26.5 25.4 24.1 23.2 22.4 21.7 21.1 20.5 19.9
550 480 27.5 26.5 25.2 24.3 23.5 22.8 22.2 21.6 20.9
600 488 28 27.3 26 25 24.3 23.6 23 22.4 21.8
Btu inflash perlb 1150 1155 1160 1164 1167 1169 1172 1174 1176
Temp. ofliquid, F 212 225 240 250 259 267 274 280 287
(cid:2)
Steamvolume, 26.8 21 16.3 13.7 11.9 10.5 9.4 8.5 7.8
cuft=lb
Source:MaddenCorp.catalog.
Ifthesteamissaturated,t t .Ifthesteamiswetwithasteamqualityofx,then
¼ sat
the leakage flow is obtained from Eq. (27) divided by px: Because the steam is
saturated x 1,
ð ¼ Þ ffiffiffiffi
1 2 1
W 50 3:14 100 61lb=h
¼ (cid:4) (cid:4) 8 (cid:4)4(cid:4) ¼
(cid:1) (cid:2)
If the steam were superheated and at 900 F, then
(cid:2)
61
W 50lb=h
¼1 0:00065 900 544 ¼
þ (cid:4)ð (cid:3) Þ
544 F is the saturation temperature at 1000psia. If the steam were wet with a
(cid:2)
quality of 80%, then
61
W 68lb=h
¼p0:8¼
ffiffiffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

5.19B
Q:
How is the discharge flow of air from high pressure to atmospheric pressure
determined?
A:
Criticalflowconditionsforairarefoundinseveralindustrialapplicationssuchas
flow through soot blower nozzles, spray guns, and safety valves and leakage
through holes in pressurevessels. The expression that relates thevariables is [8]
MW 0:5
W 356 AP 28
¼ (cid:4) (cid:4) T ð Þ
(cid:1) (cid:2)
where
W flow, lb=h
A ¼ area of opening, in.2
¼
MW molecular weight of air, 28.9
¼
T absolute temperature, R
(cid:2)
¼
P relief or discharge pressure, psia
¼
Whatistheleakageairflowfromapressurevesselat40psiaiftheholeis0.25in.
in diameter? Air is at 60 F.
(cid:2)
0:25
A 3:14 0:25 0:049in:2
¼ (cid:4) (cid:4) 4 ¼
Hence,
28:9 0:5
W 356 0:049 40 164lb=h
¼ (cid:4) (cid:4) (cid:4) 520 ¼
(cid:1) (cid:2)
5.20A
Q:
Derive an expression for the leakage of gas across a damper, stating the
assumptions made.
A:
Most of the dampers used for isolation of gas or air in ducts are not 100%
leakproof.Theyhaveacertainpercentageofleakagearea,whichcausesaflowof
Copyright © 2003 Marcel Dekker, Inc.

gas across the area. Considering the conditions to be similar to those of flow
across an orifice, we have
r
V C 2gH w 29
g ¼ d w2r ð Þ
sffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffigffiffi
where
V gas velocity through the leakage area, fps
g¼
H differential pressure across the damper, in. WC
w¼
r ;r density of gas and water, lb=cu ft
g
g
w¼
acceleration due to gravity, ft=s2
¼
C coefficient of discharge, 0.61
d¼
The gas flow W in lb=h can be obtained from
V
W 3600r A 100 E g 30
¼ g ð (cid:3) Þ 100 ð Þ
(cid:1) (cid:2)
where E is the sealing efficiencyon an area basis (%). Most dampers have an E
value of 95–99%. This figure is provided by the damper manufacturer. A is the
duct cross section, ft2. Substituting C 0:61 and r 40= 460 t into Eqs.
d ¼ g ¼ ð þ Þ
(29) and (30) and simplifying, we have
H
W 2484A 100 E w 31
¼ ð (cid:3) Þ 460 t ð Þ
rffiffiffiffiffiffiffiffiffiþffiffiffiffiffiffi
where t is the gas or air temperature, F.
(cid:2)
5.20B
Q:
A boiler flue gas duct with a diameter of 5ft has a damper whose sealing
efficiency is 99.5%. It operates under a differential pressure of 7in. WC when
closed. Gas temperature is 540 F. Estimate the leakage across the damper. If
(cid:2)
energy costs $3=MM Btu, what is the hourly heat loss and the cost of leakage?
A:
Substitute A 3:14 52=4;H 7;t 540, and E 99:5 into Eq. (31). Then
¼ (cid:4) w ¼ ¼ ¼
52 7
W 2484 3:14 100 99:5
¼ (cid:4) (cid:4) 4 (cid:4)ð (cid:3) Þ(cid:4)p1000
2040lb=h
¼ ffiffiffiffiffiffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

The hourly heat loss can be obtained from
Q WC t t 2040 0:26 540 80
¼ pð (cid:3) aÞ¼ (cid:4) (cid:4)ð (cid:3) Þ
240;000Btu=h 0:24MMBtu=h
¼ ¼
whereC isthegasspecificheat,Btu=lb F.Valuesof0.25–0.28canbeusedfor
p (cid:2)
quick estimates, depending on gas temperature. t is the ambient temperature in
a
F.80 Fwasassumedinthiscase.Thecostofthisleakage 0.24 3 $0.72=h.
(cid:2) (cid:2)
¼ (cid:4) ¼
5.20C
Q:
How is the sealing efficiency of a damper defined?
A:
The sealing efficiency of a damper is defined on the basis of the area of cross
section of the damper and also as a percentage of flow. The latter method of
definition is a function of the actual gas flow condition.
InQ5.20b,thedamperhadanefficiencyof99.5%onanareabasis.Assume
that the actual gas flow was 230,000lb=h. Then, on a flow basis, the efficiency
would be
2040
100 99:12%
(cid:3)230;000¼
If the flow were 115,000lb=h and the differential pressure were maintained, the
efficiencyonanareabasiswouldstillbe99.5%,whereasonaflowbasisitwould
be
2040
100 98:24%
(cid:3)115;000¼
Plant engineers should be aware of these two methods of stating the
efficiency of dampers.
5.21
Q:
50,000lb=h of flue gas flows from a boiler at 800 F. If a waste heat recovery
(cid:2)
systemisaddedtoreduceitstemperatureto350 F,howmuchenergyissaved?If
(cid:2)
energy costs $3=MM Btu and the plant operates for 6000h=year, what is the
annual savings? If the cost of the heat recovery system is $115,000, what is the
simple payback?
Copyright © 2003 Marcel Dekker, Inc.

A:
The energy savings Q WC t t ; where t and t are gas temperatures
¼ pð1(cid:3) 2Þ 1 2
beforeandafterinstallationoftheheatrecoverysystem, F.C isthegasspecific
(cid:2) p
heat,Btu=lb F.Useavalueof0.265whenthegastemperatureisintherangeof
(cid:2)
400–600 F.
(cid:2)
Q 50;000 0:265 800 350 5:85 106
¼ (cid:4) (cid:4)ð (cid:3) Þ¼ (cid:4)
5:85MMBtu=h
¼
Annualsavings 5:85 6000 3 $105;000
¼ (cid:4) (cid:4) ¼
Hence
115;000
Simplepayback 1:1years, or 13 months
¼105;000¼
5.22
Q:
What is life-cycle costing? Two bids are received for a fan as shown below.
Which bid is better?
Bid1 Bid2
Flow, acfm 10,000 10,000
Head, in.WC 8 8
Efficiency, % 60 75
Total cost,fanand motor, $ 17,000 21,000
A:
Life-cycle costing is a methodology the computes the total cost of owning and
operating the equipment over its life. Several financing methods and tax factors
wouldmakethisacomplicatedevaluation.However,letususeasimpleapproach
to illustrate the concept. To begin with, the following data should be obtained.
Cost of electricity, C $0.25=kWh
e¼
Annual period of operation, N 8000h
¼
Life of equipment, T 15 years
¼
Interest rate, i 0.13 (13%)
¼
Escalation rate, e 0.08 (8%)
¼
If the annual cost of operation is C , the life-cycle cost (LCC) is
a
LCC C C F 32
¼ cþ a ð Þ
Copyright © 2003 Marcel Dekker, Inc.

whereC isthecostofequipmentandF isafactor thatcapitalizestheoperating
c
cost over the life of the equipment. It can be shown [4,5] that
1 e T
1 þ
1 e (cid:3) 1 i
F þ (cid:1) þ (cid:2) 33
¼ 1 i (cid:4) 1 e ð Þ
þ 1 þ
(cid:3) 1 i
þ
The annual cost of operation is given by
C PC N 34
a ¼ e ð Þ
where P is the electric power consumed, kW.
qH
P 1:17 10 4 w 35
(cid:3)
¼ (cid:4) (cid:4) Z ð Þ
f
where
H head, in. WC
w¼
Z efficiency, fraction
f ¼
q flow, acfm
¼
Let us use the subscripts 1 and 2 for bids 1 and 2.
8
P 1:17 10 4 10;000 15:6kW
1 ¼ (cid:4) (cid:3) (cid:4) (cid:4)0:60¼
8
P 1:17 10 4 10;000 12:48kW
2 ¼ (cid:4) (cid:3) (cid:4) (cid:4)0:75¼
From Eq. (33), substituting e 0.08, i 0.13, and T 15, we get F 10.64.
¼ ¼ ¼ ¼
Calculate C from Eq. (34):
a
C 15:6 8000 0:025 $3120
a1 ¼ (cid:4) (cid:4) ¼
C 12:48 8000 0:025 $2500
a2 ¼ (cid:4) (cid:4) ¼
Using Eq. (32), calculate the life-cycle cost.
LCC 17;000 3120 10:64 $50;196
1 ¼ þ (cid:4) ¼
LCC 21;000 2500 10:64 $47;600
2 ¼ þ (cid:4) ¼
Wenotethatbid2hasalowerLCCandthusmaybechosen.However,wehaveto
analyzeotherfactorssuchasperiodofoperation,futurecostofenergy,andsoon,
before deciding. If N were lower, it is likely that bid 1 would be better.
Hence, the choice of equipment should not be based only on the initial
investment but on an evaluation of the life-cycle cost, especially as the cost of
energy is continually increasing.
Copyright © 2003 Marcel Dekker, Inc.

5.23
Q:
Aprocesskilnomits50,000lb=hoffluegasat800 F.Twobidswerereceivedfor
(cid:2)
heat recovery systems, as follows:
Bid1 Bid2
Gas temperatureleavingsystem, F 450 300
(cid:2)
Investment, $ 215,000 450,000
If the plant operates for 6000h=year and interest, escalation rates, and life
of plant are as in Q5.22, evaluate the two bids if energy costs $4=MM Btu.
A:
Let us calculate the capitalized savings and compare them with the investments.
For bid 1:
Energy recovered 50;000 0:25 800 450
¼ (cid:4) (cid:4)ð (cid:3) Þ
4:375MMBtu=h
¼
This energy is worth
4:375 4 $17:5=h
(cid:4) ¼
Annual savings 6000 17:5 $105;000
¼ (cid:4) ¼
ThecapitalizationfactorfromQ5.22is10.64.Hencecapitalizedsavings(savings
throughout the life of the plant) 105,000 10.64 $1.12 106. A similar
calculation for bid 2 shows that the ¼ capitalize (cid:4) d saving ¼ s will be (cid:4) $1.6 106. The
difference in capitalized savings of $0.48 106, or $480,000, ex (cid:4) ceeds the
(cid:4)
difference in the investment of $235,000. Hence bid 2 is more attractive.
If,however,energycosts$3=MMBtuandtheplantworksfor2500h=year,
capitalized savings on bid 1 will be $465,000 and that of bid 2 $665,000. The
difference of $200,000 is less than the difference in investment of $235,000.
Hence under these conditions, bid 1 is better.
Thecostofenergyandperiodofoperationareimportantfactorsinarriving
at the best choice.
5.24
Q:
Determine the thickness of the tubes required for a boiler super-heater. The
material is SA 213 T11; the metal temperature is 900 F (see Q8.16a for a
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

discussion of metal temperature calculation), and the tube outer diameter is
1.75in. The design pressure is 1000psig.
A:
Per ASME Boiler and Pressure Vessel Code, Sec. 1, 1980, p. 27, the following
equation can be used to obtain the thickness or the allowable pressure for tubes.
(Atubeisspecifiedbytheouterdiameterandminimumwallthickness,whereas
a pipe is specified by the nominal diameter and averagewall thickness.) Typical
pipe and tube materials used in boiler applications are shown in Tables 5.3 and
5.7.
Pd
t 0:005d e 36
w ¼2S Pþ þ ð Þ
aþ
2t 0:01d 2e
P S w(cid:3) (cid:3) 37
¼ a(cid:4)d t 0:005d e ð Þ
(cid:3)ðw(cid:3) (cid:3) Þ
where
t minimum wall thickness, in.
w¼
P design pressure, psig
¼
d tube outer diameter, in.
¼
e factorthataccountsforcompensationinscrewedtubes,generallyzero
¼
S allowable stress, psi
a¼
TABLE5.7 Allowable Stress Values,FerrousTubing,1000psi
Temperaturesnot exceeding( F):
(cid:2)
Material specifications 20–650 700 750 800 850 900 950 1000 1200 1400
SA178 gr A 10.0 9.7 9.0 7.8 6.7 5.5 3.8 2.1 — —
12.8 12.2 11.0 9.2 7.4 5.5 3.8 2.1 — —
SA192 gr C 11.8 11.5 10.6 9.2 7.9 6.5 4.5 2.5 — —
SA210 gr A-1SA53 B 15 14.4 13.0 10.8 8.7 6.5 4.5 2.5 — —
gr C 17.5 16.6 14.8 12.0 7.8 5.0 3.0 1.5 — —
SA213 T11,P11 15.0 15.0 15.0 15.0 14.4 13.1 11.0 7.8 1.2 —
T22,P22 15.0 15.0 15.0 15.0 14.4 13.1 11.0 7.8 1.6 —
T9 — 13.4 13.1 12.5 12.5 12.0 10.8 8.5 — —
SA213 TP304 H — 15.9 15.5 15.2 14.9 14.7 14.4 13.8 6.1 2.3
TP316 H — 16.3 16.1 15.9 15.7 15.5 15.4 15.3 7.4 2.3
TP321 H — 15.8 15.7 15.5 15.4 15.3 15.2 14.0 5.9 1.9
TP347 H — 14.7 14.7 14.7 14.7 14.7 14.6 14.4 7.9 2.5
Source:ASME,BoilerandPressureVesselCode,Sec.1,Powerboilers,1980.
Copyright © 2003 Marcel Dekker, Inc.

From Table 5.7, S is 13,100. Substituting into Eq. (36) yields
a
1000 1:75
t (cid:4) 0:005 1:75 0:073in:
w ¼2 13;100 1000þ (cid:4) ¼
(cid:4) þ
Thetubewiththenexthigherthicknesswouldbechosen.Acorrosionallowance,
if required, may be added to t .
w
5.25
Q:
DeterminethemaximumpressurethatanSA53Bcarbonsteelpipeofsize3in.
schedule80canbesubjectedtoatametaltemperatureof550 F.Useacorrosion
(cid:2)
allowance of 0.02in.
A:
By the ASME Code, Sec. 1, 1980, p. 27, the formula for determining allowable
pressures or thickness of pipes, drums, and headers is
Pd
t c 38
w ¼2S E 0:8Pþ ð Þ
a þ
where
E ligament efficiency, 1 for seamless pipes
¼
c corrosion allowance
¼
From Table 5.3, a 3in. schedule 80 pipe has an outer diameter of 3.5in. and a
nominal wall thickness of 0.3in. Considering the manufacturing tolerance of
12.5%, the minimum thickness available is 0.875 0.3 0.2625in.
(cid:4) ¼
Substituting S 15,000psi (Table 5.7) and c 0:02 into Eq. (38), we
a¼ ¼
have
3:5P
0:2625 0:02
¼2 15;000 0:8Pþ
(cid:4) þ
Solving for P, we have P 2200psig.
¼
For alloy steels, the factor 0.8 in the denominator would be different. The
ASME Code may be referred to for details [6]. Table 5.8 gives the maximum
allowable pressures for carbon steel pipes up to a temperature of 650 F [7].
(cid:2)
5.26
Q:
How is the maximum allowable external pressure for boiler tubes determined?
Copyright © 2003 Marcel Dekker, Inc.

TABLE5.8 MaximumAllowable Pressurea
Nominalpipesize (in.) Schedule40 Schedule 80 Schedule 160
1=4 4830 6833 —
1=2 3750 5235 6928
1 2857 3947 5769
11 2112 3000 4329
2
2 1782 2575 4225
21 1948 2702 3749
2
3 1693 2394 3601
4 1435 2074 3370
5 1258 1857 3191
6 1145 1796 3076
8 1006 1587 2970
aBasedonallowablestressof15,000psi;corrosionallowanceiszero.
Source:Ref.7.
A:
According to ASME Code [9], the external pressures of tubes or pipes can be
determined as follows.
For cylinders having d =t >10,
o
4B
P 39
a ¼3 d =t ð Þ
ð o Þ
where
P maximum allowable external pressure, psi
a¼
A;B factors obtained from ASME Code, Sec. 1, depending onvalues of
¼
d =t and L=d , where L;d , and t refer to tube length, external
o o o
diameter, and thickness.
Whend =t <10; AandBaredeterminedfromtablesorchartsasinQ5.25.
o
For d =t <4; A 1:1= d =t 2. Two values of allowable pressures are then
o ¼ ð o Þ
computed, namely, P and P .
a1 a2
2:167
P 0:0833 B
a1 ¼ d =t (cid:3) (cid:4)
(cid:1) o (cid:2)
and
1 t=d
P 2S (cid:3) o
a2 ¼ b(cid:4) d =t
o
Copyright © 2003 Marcel Dekker, Inc.

where S is the lesser of 2 times the maximum allowable stress values at design
b
metaltemperaturefromthecodestresstablesor1.8timestheyieldstrengthofthe
material at design metal temperature. Then the smaller of the P or P is used
a1 a2
for P .
a
Example
Determinethemaximumallowableexternalpressureat600 Ffor120in.SA192
(cid:2)
tubes of outer diameter 2in. and length 15ft used in fire tube boilers.
Solution.
d 15 12
o (cid:4) 90
L ¼ 2:0 ¼
and
d 2
o 16:7
t ¼0:120¼
From Fig. 5.3 factor A 0.004. From Fig. 5.4, B 9500. Since d =t >10,
¼ ¼ o
4B 9500
P 4 758psi
a ¼3 d =t ¼ (cid:4)3=16:7¼
ð o Þ
5.27
Q:
What is a decibel? How is it expressed?
A:
Thedecibel(dB)istheunitofmeasureusedinnoiseevaluation.Itisaratio(not
an absolute value) of a sound level to a reference level and is stated as a sound
pressurelevel(SPL)orasoundpowerlevel(PWL).ThereferencelevelforSPLis
0.0002mbar. A human ear can detect from about 20dB to sound pressures
100,000 times higher, 120dB.
Audible frequencies are divided into octave bands for analysis. The center
frequencies in hertz (Hz) of the octave bands are 31.5, 63, 125, 250, 500, 1000,
2000,4000,and8000Hz.Thehumanearissensitivetofrequenciesbetween500
and3000Hzandlesssensitivetoveryhighandlowfrequencies.At1000Hz,for
example, 90dB is louder than it is at 500Hz.
The sound meter used in noise evaluation has three scales, A, B, and C,
which selectively discriminate against low and high frequencies. The A scale
(dBA) is the most heavily weighted scale and approximates the human ear’s
response to noise (500–6000Hz). It is used in industry and in regulations
regarding the evaluation of noise. Table 5.9 gives typical dBA levels of various
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 5.3 Factor Aforusein external pressurecalculation [9].
noise sources, and Table 5.10 gives the permissible Occupational Safety and
Health Act (OSHA) noise exposure values.
5.28
Q:
How are decibels added? A noise source has the following dB values at center
frequencies:
Hz 31.5 63 125 250 500 1000 2000 4000 8000
dB 97 97 95 91 84 82 80 85 85
What is the overall noise level?
Copyright © 2003 Marcel Dekker, Inc.

FIGURE5.4 FactorB forusein external pressurecalculation (SA178A,SA 192tubes) [9].
Copyright © 2003 Marcel Dekker, Inc.

TABLE5.9 Typical A-WeightedSoundLevels
dBA Source Perception=hearing
140 Jet engine at25ft Unbearable
130 High pressuresafety ventat25ft Threshold ofpain
120 Large forced draftfan plenumarea Uncomfortably loud
110 8000hpengine exhaust at25ft
100 Compressor building Veryloud
90 Boiler room
80 Pneumatic drill Loud
70 Commercial area
60 Normal conversation
50 Averagehome Comfortable
40 Nighttime residentialarea
30 Broadcast studio
20 Whisper Barelyaudible
10
0 Threshold ofhearing
A:
Decibelsareaddedlogarithmicallyandnotalgebraically.97dBplus97dBisnot
194dB but 100dB.
P 10 log 10P 1 =10 10P 2 =10 10P 3 =10
¼ ð þ þ þ(cid:7)(cid:7)(cid:7)Þ
10 log 109:7 109:7 109:5 109:1 108:4 108:2 108
¼ ð þ þ þ þ þ þ
108:5 108:5
þ þ Þ
102dB
¼
TABLE5.10 Permissible Noise Exposures
(OSHA)
Soundlevel (dBA)
Durationperday (h) (slow response)
8 90
6 92
4 95
3 97
2 100
11 102
2
1 105
1 110
2
1orless 115
4
Copyright © 2003 Marcel Dekker, Inc.

5.29
Q:
What are SPL and PWL?
A:
SPLissoundpressurelevel,whichisdependentonthedistanceandenvironment
andiseasilymeasuredwithasoundlevelmeter.SPLvaluesshouldbereferredto
distance. PWLissoundpowerlevelandisameasureofthetotalacoustic power
radiated by a given source. It is defined as
W
PWL 10log dB 40
¼ 10 12 ð Þ
(cid:1) (cid:3) (cid:2)
PWL is a constant for a given source and is independent of the environment. It
cannot be measured directly but must be calculated. PWL can be roughly
described as being equal to the wattage rating of a bulb. Manufacturers of fans
and gas turbines publish the values of PWL of their machines. When selecting
silencers for these equipment, PWL may be converted to SPL depending on
distance, and the attenuation desired at various frequencies may be obtained. A
silencer that gives the desired attenuation can then be chosen.
5.30
Q:
Asoundlevelof120dBismeasuredatadistanceof3ftfromasource.Findthe
value at 100ft.
A:
The following formula relates the PWL and SPL with distance:
SPL PWL 20logL 2:5dB 41
¼ (cid:3) þ ð Þ
where L distance, ft.
¼
PWL is a constant for a given source. Hence
SPL 20logL a constant
þ ¼
120 20log3 SPL 20 log100
þ ¼ 2þ
Hence
SPL 89:5dB
2 ¼
Thus we see that SPL has decreased by 30dB with a change from 3ft to 100ft.
When selecting silencers, one should be aware of the desired SPL at the desired
distance. Neglecting the effect of distance can lead to specifying a larger and
more costly silencer than necessary.
Copyright © 2003 Marcel Dekker, Inc.

5.31
Q:
How is the noise level from the exhaust of engines computed?
A:
A gas turbine exhaust has the noise spectrum given in Table 5.11 at various
octavebands. The exhaustgases flowthrougha heat recoveryboiler into astack
that is 100ft high. Determine the noise level 150ft from the top of the stack (of
diameter 60in.) and in front of the boiler.
Assume that the boiler attenuation is20dBat all octavebands. In order to
arrive at the noise levels at the boiler front, three corrections are required: (1)
boilerattenuation,(2)effectofdirectivity,and(3)divergenceat150ft.Theeffect
of directivity is shown in Table 5.12. The divergence effect is given by 20 log
L 2:5; where L is the distance from the noise source.
(cid:3)
Row 8 values are converted to dBA by adding the dB at various
frequencies. The final value is 71 dBA.
5.32
Q:
How is the holdup or volume of water in boiler drums estimated? A boiler
generating10,000lb=hofsteamat400psighasa42in.drum10ftlongwith2:1
ellipsoidalends. Findthe time between normalwater level(NWL)andlow level
cutoff(LLCO)ifNWLisat2in.belowdrumcenterlineandLLCOis4in.below
NWL.
TABLE5.11 Table ofNoise Levels
1.Frequency, Hz 63 125 250 500 1000 2000 4000 8000
2.PWL, 10(cid:3) 12W dB 130 134 136 136 132 130 131 133
(cid:4)
(gasturbine)
3.Boiler attenuation,dB 20 20 20 20 20 20 20 20
(cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3)
4.Directivity, dB 0 1 2 5 8 10 13 16
(cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3)
5.Divergence, dB 41 41 41 41 41 41 41 41
(cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3)
6.Resultant 69 72 73 70 63 59 57 56
7.A scale,dB 25 16 9 3 0 1 1 1
(cid:3) (cid:3) (cid:3) (cid:3) (cid:3)
8.Net 44 56 64 67 63 60 58 55
56 69 65 60
69 66.5
71
Copyright © 2003 Marcel Dekker, Inc.

TABLE5.12 EffectofDirectivityBasedonAngletoDirectionofFlowandSizeof
Silencer Outlet
Octave bandcenter frequency(Hz)
Angle todirection Silencer outlet
offlow diameter (in.) 63 125 250 500 1000 2000 3000 4000
0 72–96 4 5 5 6 6 7 7 7
(cid:2)
þ þ þ þ þ þ þ þ
54–66 3 4 4 5 5 5 5 5
þ þ þ þ þ þ þ þ
36–48 2 3 3 4 4 4 4 4
þ þ þ þ þ þ þ þ
26–32 1 1 2 2 2 2 2 2
þ þ þ þ þ þ þ þ
16–24 0 0 1 1 1 1 1 1
þ þ þ þ þ þ
8–14 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0
45 72–96 2 3 3 4 4 5 5 5
(cid:2)
þ þ þ þ þ þ þ þ
54–66 1 2 2 3 3 3 3 3
þ þ þ þ þ þ þ þ
36–48 0 1 1 2 2 2 2 2
þ þ þ þ þ þ þ
26–32 0 0 0 1 1 1 1 1
þ þ þ þ þ
16–24 0 0 0 0 0 0 0 0
8–14 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0
90and 135 72–96 1 2 5 7 10 12 15 17
(cid:2)
(cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3)
54–66 0 1 2 5 8 10 13 16
(cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3)
36–48 0 0 1 3 6 7 11 15
(cid:3) (cid:3) (cid:3) (cid:3) (cid:3) (cid:3)
26–32 0 0 0 1 3 5 9 14
(cid:3) (cid:3) (cid:3) (cid:3) (cid:3)
16–24 0 0 0 0 1 3 7 13
(cid:3) (cid:3) (cid:3) (cid:3)
8–14 0 0 0 0 1 2 5 11
(cid:3) (cid:3) (cid:3) (cid:3)
5–6 0 0 0 0 0 1 3 6
(cid:3) (cid:3) (cid:3)
4 0 0 0 0 0 0 1 3
(cid:3) (cid:3)
Source:BurgessManning.
A:
The volume of water in the drum must include the volume due to the straight
section plus the dished ends.
Volume in the straight section, V , is given by
s
a
V L R2 sina cosa
s ¼ (cid:4) (cid:4) 57:3(cid:3) (cid:4)
(cid:4) (cid:5)
whereaistheangleshowninFig.5.5.Thevolumeofliquidineachendisgiven
by
V 0:261 H2 3R H
e ¼ (cid:4) (cid:4)ð (cid:3) Þ
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 5.5 Partial volumeof waterinboiler drum.
where
H straight length of drum
¼
R drum radius
¼
In this case, H 120in. and R 21in.
¼ ¼
LetuscomputeV andV ,thevolumeofthestraightsectionandeachend
s1 e1
corresponding to the 19in. level from the bottom of the drum.
2
cosa 0:09523
¼21¼
Hence
a 84:5 andsina 0:9954
(cid:2)
¼ ¼
84:53
v 120 21 21 0:0953 0:9954
s1 ¼ (cid:4) (cid:4) (cid:4) 57:3 (cid:3) (cid:4)
(cid:1) (cid:2)
73;051cuin:
¼
V 0:261 19 19 3 21 19 4146cuin:
e1 ¼ (cid:4) (cid:4) (cid:4)ð (cid:4) (cid:3) Þ¼
Hencetotalvolumeofliquid upto19in.level 73,051 2 4146 81,343cu
¼ þ (cid:4) ¼
in. 47.08cu ft.
¼
Similarly, we can show that total volume of water up to the 15in.
level 34.1cu ft. Hence the difference is 13cu ft.
¼
Specific volume of water at 400psig 0.0193cu ft=lb.
¼
0:0193
Normal evaporation rate 10;000
¼ (cid:4) 60
3:2cuft=min
¼
Hence the length of time between the levels assuming that the water supply has
been discontinued 13=3.21 4.05min.
¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

NOMENCLATURE
A Area of opening, in.2, or duct cross section, ft2
A;B Factors used in Q5.26
BD Blowdown, fraction
BHP Boiler horsepower
c Corrosion allowance, in.
C Initial investment, $
c
C Coefficient of discharge
d
C Cost of electricity, $=kWh
e
C Specific heat, Btu=lb F
p (cid:2)
d Tube or outer diameter, in.
d Tube or pipe inner diameter, in.
i
e Escalation factor
E Sealing efficiency, %; ligament efficiency, fraction
F Factor defined in Eq. (33)
G Gas mass velocity, lb=ft2 h
h Enthalpy, Btu=lb
H Height of liquid column, in.
h ;h Enthalpy of saturated vapor and liquid, Btu=lb
g f
H Head of gas column, ft
g
H Head of liquid, ft
l
H Differential pressure across damper, in. WC
w
i Interest rate
L Distance, ft
LCC Life-cycle cost, $
M Moisture in air, lb=lb
MW Molecular weight
N Annual period of operation, h
P Partial pressure of water vapor, psia
w
P Gas pressure, psia; design pressure, psig
DP Differential pressure, psi
PWL Sound power level
q Volumetric flow, gpm or cfm
Q Energy, Btu=h
R Radius of drum, in.
RH Relative humidity
s Specific gravity
S Allowable stress, psi
a
SBV Steam by volume
SPL Sound pressure level, dB
SVP Saturated vapor pressure, psia
Copyright © 2003 Marcel Dekker, Inc.

t Fluid temperature, F
(cid:2)
t Minimum wall thickness of pipe or tube, in.
w
T Life of plant, years
v Specific volume, cu ft; subscripts g and f stand for saturated vapor and
liquid
V ;V Volume of drum ends, straight section, cu in.
e s
V Velocity of gas
g
W Mass flow, lb=h
x Steam quality
y Volume fraction
r Density, lb=cu ft; subscript g stands for gas
REFERENCES
1. VGanapathy.Determiningoperatingparametersforhotexhaustgascoolingsystems.
PlantEngineering,Mar3,1983,p182.
2. VGanapathy.Nomographestimatessteamleakageandcost.HeatingPipingandAir-
Conditioning,Nov1982,p101.
3. VGanapathy. Quickestimates of damper leakage andcost energyloss. Oil andGas
Journal,Sept21,1981,p124.
4. VGanapathy.AppliedHeatTransfer,Tulsa,OK:PennWellBooks,1982,p186.
5. RJBrownandRRYanuck.LifeCycleCosting.Atlanta,GA:FairmontPress,1980,p
188.
6. ASME.BoilerandPressureVesselCode,Sec.1.NewYork,1980,p119.
7. V Ganapathy. Estimate maximum allowable pressures for steel piping, Chemical
Engineering,July25,1983,p99.
8. ASME.BoilerandPressureVesselCode,Sec.8,Div.1,ParaUG131,1980.
9. ASME.BoilerandPressureVesselCode,Sec.1,ParaPFT51,1989.
Copyright © 2003 Marcel Dekker, Inc.

6
Fuels, Combustion, and Efficiency of Boilers
and Heaters
6.01 EstimatingHHV(higherheatingvalue)andLHV(lowerheatingvalue)of
fuelsfromultimateanalysis;relatingheatinputsbasedonHHVandLHV;
relating boiler efficiencies based on HHVand LHV
6.02 Estimating HHVand LHVof fuel oils if API is known
(cid:2)
6.03 Calculating cost of fuels on MM Btu (million Btu) basis; comparing
electricity cost with cost of fuels
6.04 Estimating annual fuel cost for power plants; relating heat rates with
efficiency of power plants
6.05 Determining gas regulator settings for different fuels
6.06 Correcting fuel flow meter readings for operating fuel gas pressures and
temperatures
6.07 Determining energy, steam quantity, and electric heater capacity required
for heating air
6.08 Determining energy, steam quantity, and electric heater capacity required
for heating fuel oils
6.09 Combustion calculations from ultimate analysis offuels; determining wet
and dry air and fluegas quantities; volumetric analysis of fluegas on wet
and dry basis; partial pressures of water vapor and carbon dioxide in flue
gas; molecular weight and density of flue gas
6.10 Combustion calculations on MM Btu basis; determining air and flue gas
quantities in the absence of fuel data
Copyright © 2003 Marcel Dekker, Inc.

6.11 Estimating excess air from flue gas CO readings
2
6.12 Estimating excess air from CO and O readings; estimating excess air
2 2
from O readings alone
2
6.13 Effect of reducing oxygen in flue gas; calculating flue gas produced;
calculating energy saved and reduction in fuel cost
6.14 Effect of fuel heating values on air and flue gas produced in boilers
6.15 Determiningcombustiontemperatureofdifferentfuelsintheabsenceof
fuel analysis
6.16a Calculating ash concentration in flue gases
6.16b Relating ash concentration between mass and volumetric units
6.17 Determining melting point of ash knowing ash analysis
6.18 Determining SO and SO in flue gases in lb=MM Btu and in ppm
2 3
(volume)
6.19 Determining efficiencyofboilers and heaters; efficiencyon HHVbasis;
drygasloss;lossduetomoistureandcombustionofhydrogen;lossdue
to moisture in air; radiation loss; efficiency on LHV basis; wet flue gas
loss; relating efficiencies on HHVand LHV basis
6.20 Determining efficiency of boilers and heaters on HHVand LHV basis
from flue gas analysis
6.21 Loss due to CO formation
6.22 Simple formula for efficiency determination
6.23 Determiningradiationlossesinboilersandheatersifcasingtemperature
and wind velocity are known
6.24 Variation of heat losses and efficiency with boiler load
6.25a Sulfur dew point of flue gases
6.25b Computing acid dew points for various acid vapors
6.25c Effect of gas temperature on corrosion potential
6.25d Another correlation for sulfuric acid dew point
6.26a Converting NOx and CO from lb=h to ppm for turbine exhaust
gases
6.26b Converting NOx and CO from lb=h to ppm for fired boilers
6.26c Converting UHC from lb=MM Btu to ppm
6.26d Converting SOx from lb=MM Btu to ppm
6.26e Converting NOx and CO from lb=h to ppm before and after auxiliary
firing in an HRSG
6.26f Relating steam generator emission from measured oxygen value to 3%
basis
6.27a Oxygen consumption versus fuel input for gas turbine exhaust gases
6.27b Determining gas turbine exhaust gas analysis after auxiliary firing
6.27c Determining turbine exhaust gas temperature after auxiliary firing
6.28 Relating heat rates of engines to fuel consumption
Copyright © 2003 Marcel Dekker, Inc.

6.01
Q:
HowaretheHHV(higherheatingvalue)andLHV(lowerheatingvalue)offuels
estimated when the ultimate analysis is known?
A:
We can use the expressions [1]
O
HHV 14,500 C 62,000 H 2 4000 S 1
¼ (cid:4) þ (cid:4) 2(cid:3) 8 þ (cid:4) ð Þ
(cid:1) (cid:2)
LHV HHV 9720 H 1110W 2
¼ (cid:3) (cid:4) 2(cid:3) ð Þ
where W is the fraction by weight of moisture in fuel, and C;H ;O , and S are
2 2
fractions by weight of carbon, hydrogen, oxygen, and sulfur in the fuel.
If a coal has C 0:80;H 0:003;O 0:005;W 0:073;S 0:006,
¼ 2 ¼ 2 ¼ ¼ ¼
and the rest ash, find its HHV and LHV. Substituting into Eqs. (1) and (2), we
have
0:005
HHV 14,500 0:80 62,000 0:003
¼ (cid:4) þ (cid:4) (cid:3) 8
(cid:1) (cid:2)
4000 0:006 11,771Btu=lb
þ (cid:4) ¼
LHV 11,771 9720 0:003 1110 0:073
¼ (cid:3) (cid:4) (cid:3) (cid:4)
11,668Btu=lb
¼
Fuel inputs to furnaces and boilers and efficiencies are often specified without
reference to the heating values, whether HHV or LHV, which is misleading.
Ifa burner has a capacityof QMM Btu=h (million Btu=h)on HHVbasis,
its capacity on LHV basis would be
LHV
Q Q 3a
LHV ¼ HHV(cid:4)HHV ð Þ
Similarly, if Z and Z are the efficiencies of a boiler on HHV and LHV
HHV LHV
basis, respectively, they are related as follows:
Z HHV Z LHV 3b
HHV(cid:4) ¼ LHV(cid:4) ð Þ
6.02a
Q:
How can we estimate the HHV and LHV of a fuel oil in the absence of its
ultimate analysis?
Copyright © 2003 Marcel Dekker, Inc.

A:
Generally,the APIofafueloilwillbeknown,andthefollowingexpressionscan
(cid:2)
be used:
HHV 17,887 57:5 API 102:2 %S 4a
(cid:2)
¼ þ (cid:4) (cid:3) (cid:4) ð Þ
LHV HHV 91:23 %H 4b
¼ (cid:3) (cid:4) 2 ð Þ
where %H is the percent hydrogen by weight.
2
2122:5
%H F 5
2 ¼ (cid:3) API 131:5 ð Þ
(cid:2) þ
where
F 24:50for0 API 9
(cid:2)
¼ (cid:6) (cid:6)
F 25:00for9 API 20
(cid:2)
¼ (cid:6) (cid:6)
F 25:20for20 API 30
(cid:2)
¼ (cid:6) (cid:6)
F 25:45for30 API 40
(cid:2)
¼ (cid:6) (cid:6)
HHV and LHV are in Btu=lb.
6.02b
Q:
Determine the HHV and LHV of 30 API fuel oil in Btu=gal and in Btu=lb.
(cid:2)
Assume that %S is 0.5.
A:
From Eq. (4a),
HHV 17,887 57:5 30 102:2 0:5
¼ þ (cid:4) (cid:3) (cid:4)
19,651Btu=lb
¼
Tocalculatethedensityorspecificgravityoffuel oilswecanusetheexpression
141:5 141:5
s 0:876 6
¼131:5 API¼131:5 30¼ ð Þ
þ(cid:2) þ
Hence
Density 0:876 8:335 7:3lb=gal
¼ (cid:4) ¼
8.335 is the density of liquids in lb=gal when s 1.
¼
HHV in Btu/gal 19,561 7:3 142,795
¼ (cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

From Eq. (5),
2122:5
%H 25:2 12:05
2 ¼ (cid:3)131:5 30¼
þ
LHV 19,561 91:23 12:05 18,460Btu=lb
¼ (cid:3) (cid:4) ¼
18,460 7:3 134,758Btu=gal
¼ (cid:4) ¼
6.03a
Q:
A good way to compare fuel costs is to check their values per MM Btu fired. If
coal having HHV 9500Btu=lb costs $25=long ton, what is the cost in $=MM
¼
Btu?
A:
1 long ton 2240lb. 1MM Btu has 106=9500 105lb of coal. Hence 105lb
¼ ¼
would cost
25
105 $1:17=MMBtu
(cid:4)2240¼
6.03b
Q:
If No. 6 fuel oil costs 30 cents=gal, is it cheaper than the coal in Q6.03a?
A:
Table 6.1 gives the HHV of fuel oils. It is 152,400Btu=gal. Hence 1MM Btu
would cost
106
0:30 $1:96=MMBtu
152,400(cid:4) ¼
6.03c
Q:
Which is less expensive, electricity at 1.5cents=kWh or gas at $3=MM Btu?
A:
3413Btu 1kWh. At 1.5cents=kWh, 1MM Btu of electricity costs
(106=3413 ¼ ) 1.5=100 $4.4. Hence in this case, electricity is costlier than
(cid:4) ¼
gas. This example serves to illustrate the conversion of units and does not
imply that this situation will prevail in all regions.
Copyright © 2003 Marcel Dekker, Inc.

TABLE6.1 Typical HeatContents ofVariousOils
Sp.gr. Sp. Temp. Air
Typical 60 F Gross Gross Wt% Net Net Sp.heat heatat corr. 60 F Ult.
(cid:2) (cid:2)
oil (cid:2) API (15.6 (cid:2) C) lb=gal kg=m3 Btu=gal kcal=L H Btu=gal kcal=L at40 (cid:2) F 300 (cid:2) F ( (cid:2) API/ (cid:2) F) (ft3=gal) %CO 2
0 1.076 8.969 1,075 160,426 10,681 8.359 153,664 10,231 0.391 0.504 0.045 1581 —
2 1.060 8.834 1,059 159,038 10,589 8.601 152,183 10,133 0.394 0.508 — — —
4 1.044 8.704 1,043 157,692 10,499 8.836 150,752 10,037 0.397 0.512 — — 18.0
6 1.029 8.577 1,0028 156,384 10,412 9.064 149,368 9,945 0.400 0.516 0.048 1529 17.6
8 1.014 8.454 1,013 155,115 10,328 9.285 148,028 9,856 0.403 0.519 0.050 1513 17.1
10 1.000 8.335 1,000 153,881 10,246 10.00 146,351 9,744 0.406 0.523 0.051 1509 16.7
12 0.986 8.219 985.0 152,681 10,166 10.21 145,100 9,661 0.409 0.527 0.052 1494 16.4
No.6oil 14 0.973 8.106 971.5 151,515 10,088 10.41 143,888 9,580 0.412 0.530 0.054 1478 16.1
16 0.959 7.996 958.3 150,380 10,013 10.61 142,712 9,502 0.415 0.534 0.056 1463 15.8
18 0.946 7.889 945.5 149,275 9,939 10.80 141,572 9,426 0.417 0.538 0.058 1448 15.5
No.5oil 20 0.934 7.785 933.0 148,200 9,867 10.99 140,466 9,353 0.420 0.541 0.060 1433 15.2
22 0.922 7.683 920.9 147,153 9,798 11.37 139,251 9,272 0.423 0.545 0.061 1423 14.9
24 0.910 7.585 909.9 146,132 9,730 11.55 138,210 9,202 0.426 0.548 0.063 1409 14.7
No.4oil 26 0.898 7.488 897.5 145,138 9,664 11.72 137,198 9,135 0.428 0.552 0.065 1395 14.5
28 0.887 7.394 886.2 144,168 9,599 11.89 136,214 9,069 0.431 0.555 0.067 1381 14.3
No.2oil 30 0.876 7.303 875.2 143,223 9,536 12.06 135,258 9,006 0.434 0.559 0.089 1368 14.0
32 0.865 7.213 864.5 142,300 9,475 12.47 134,163 8,933 0.436 0.562 0.072 1360 13.8
34 0.855 7.126 854.1 141,400 9,415 12.63 133,259 8,873 0.439 0.566 0.074 1347 13.6
36 0.845 7.041 843.9 140,521 9,356 12.78 132,380 8,814 0.442 0.569 0.076 1334 13.4
38 0.835 6.958 833.9 139,664 9,299 12.93 131,524 8,757 0.444 0.572 0.079 1321 13.3
No.1oil 40 0.825 6.877 824.2 138,826 9,243 13.07 130,689 8,702 0.447 0.576 0.082 1309 13.1
42 0.816 6.798 814.7 138,007 9,189 — — — 0.450 0.579 0.085 — 13.0
44 0.806 6.720 805.4 137,207 9,136 — — — 0.452 0.582 0.088 — 12.8
Copyright © 2003 Marcel Dekker, Inc.

6.04
Q:
Estimate the annual fuel cost for a 300MW coal-fired power plant if the overall
efficiency is 40% and the fuel cost is $1.1=MM Btu. The plant operates for
6000h=yr.
A:
Power plants have efficiencies in the range of 35–42%. Another way of
expressing this is to use the term heat rate, defined as
3413
Heatrate Btu=kWh
¼efficiency
In this case it is 3413=0.4 8530Btu=kWh.
¼
Annual fuel cost 1000 megawatt heatrate h=yr cost of fuel
¼ (cid:4) (cid:4) (cid:4)ð Þ(cid:4)
in $=MM Btu
1:1
1000 300 8530 6000
¼ (cid:4) (cid:4) (cid:4) (cid:4)106
$16:9 106
¼ (cid:4)
The fuel cost for any other type of power plant could be found in a similar
fashion. Heat rates are provided by power plant suppliers.
6.05
Q:
A 20MM Btu=h burner was firing natural gas of HHV 1050Btu=scf with a
¼
specific gravity of 0.6. If it is now required to burn propane having
HHV 2300Btu=scf with a specific gravity of 1.5, and if the gas pressure to
¼
the burner was set at 4psig earlier for the same duty, estimate the new gas
pressure. Assume that the gas temperature in both cases is 60 F.
(cid:2)
A:
TheheatinputtotheburnerisspecifiedonHHVbasis.Thefuelflowratewould
beQ=HHV,whereQisthedutyinBtu=h.Thegaspressuredifferential between
thegaspressureregulatorandthefurnaceisusedtoovercometheflowresistance
according to the equation
KW2
DP f 7
¼ r ð Þ
where
DP pressure differential, psi
¼
Copyright © 2003 Marcel Dekker, Inc.

K a constant
¼
r gas density 0.075s (s is the gas specific gravity; s 1 for air)
¼ ¼ ¼
W fuel flow rate in lb=h flow in scfh 0.075s
f ¼ ¼ (cid:4)
Let the subscripts 1 and 2 denote natural gas and propane, respectively.
20 106
W (cid:4) 0:075 0:6
f1 ¼ 1050 (cid:4) (cid:4)
20 106
W (cid:4) 0:075 1:5
f2 ¼ 2300 (cid:4) (cid:4)
DP 4;r 0:075 0:6, and r 0:075 1:5. Hence, from Eq. (7),
1 ¼ 1 ¼ (cid:4) 2 ¼ (cid:4)
DP W2r 4 0:6 2300 2
1 f1 2 ð Þ
DP ¼W2r ¼DP ¼ 1050 2(cid:4) 1:5
2 f2 1 2
ð Þ
or
DP 2:08psig
2 ¼
Hence,ifthegaspressureissetatabout2psig,wecanobtainthesameduty.The
calculation assumes that the backpressure has not changed.
6.06
Q:
Gas flow measurement using displacement meters indicates actual cubic feet of
gas consumed. However, gas is billed, generally, at reference conditions of 60 F
(cid:2)
and14.65psia (4oz). Hencegasflowhastobe corrected foractual pressure and
temperature. Plant engineers should be aware of this conversion.
In a gas-fired boiler plant, 1000cu ft of gas per hour was measured, gas
conditions being 60psig and 80 F. If the gas has a higher calorific value of
(cid:2)
1050Btu=scf, what is the cost of fuel consumed if energy costs $4=MM Btu?
A:
The fuel consumption at standard conditions is found as follows.
T
V V P s 8
s ¼ a a P T ð Þ
s a
Copyright © 2003 Marcel Dekker, Inc.

where
V ;V fuel consumption, standard and actual, cu ft/h
s a ¼
T reference temperature of 520 R
s ¼ (cid:2)
T actual temperature, R
a ¼ (cid:2)
P ;P standard and actual pressures, psia
s a ¼
520
V 100 30 14:22
s ¼ (cid:4)ð þ Þ(cid:4)14:65 540
(cid:4)
2900scfh
¼
Hence
Energy used 2900 1050 3.05MM Btu=h
¼ (cid:4) ¼
Cost of fuel 3.05 4 $12.2=h.
¼ (cid:4) ¼
If pressure and temperature corrections are not used, the displacement
meter reading can lead to incorrect fuel consumption data.
6.07
Q:
EstimatetheenergyinBtu=handinkilowatts(kW)forheating75,000lb=hofair
from 90 F to 225 F. What is the steam quantity required if 200psia saturated
(cid:2) (cid:2)
steam is used to accomplish the duty noted above? What size of electric heater
would be used?
A:
The energy required to heat the air can be expressed as
Q W C DT 9
¼ a p ð Þ
where
Q duty, Btu/h
¼
W air flow, lb/h
a ¼
C specific heat of air, Btu/lb F
p ¼ (cid:2)
DT temperature rise, F
(cid:2)
¼
C may be taken as 0.25 for the specified temperature range.
p
Q 75,000 0:25 225 90 2:53 106 Btu=h
¼ (cid:4) (cid:4)ð (cid:3) Þ¼ (cid:4)
Copyright © 2003 Marcel Dekker, Inc.

Using the conversion factor 3413Btu 1kWh, we have
¼
106
Q 2:53 741kW
¼ (cid:4)3413¼
A 750kW heater or the next higher size could be chosen.
If steam is used, the quantity can be estimated by dividing Q in Btu=h by
thelatentheatobtainedfromthesteamtables(seetheAppendix).At200psia,the
latent heat is 843Btu=lb. Hence
106
Steam required 2:55 3046lb=h
¼ (cid:4)843¼
6.08
Q:
Estimate the steam required at 25psig to heat 20gpm of 15 API fuel oil from
(cid:2)
40 F to 180 F. If an electric heater is used, what should be its capacity?
(cid:2) (cid:2)
A:
Table6.2givestheheat contentoffueloils inBtu=gal[2].At 180 F,enthalpyis
(cid:2)
529Btu=gal,andat40 Fitis26Btu=gal.Hencetheenergyabsorbedbythefuel
(cid:2)
oil is
Q 20 60 529 26 0:6 106 Btu=h
¼ (cid:4) (cid:4)ð (cid:3) Þ¼ (cid:4)
106
0:6 175kW
¼ (cid:4)3413¼
The latent heat of steam (from the steam tables) is 934Btu=lb at 25psig or
40psia. Hence
106
Steam required 0:6 646lb=h
¼ (cid:4)934¼
If an electric heater is used, its capacity will be a minimum of 175kW.
Allowing for radiation losses, we may choose a 200kW heater.
Intheabsenceof informationonfueloilenthalpy,useaspecificgravityof
0.9 and a specific heat of 0.5Btu=lb F. Hence the duty will be
(cid:2)
0:9
Q 20 60 62:40 0:5 180 40
¼ (cid:4) (cid:4) (cid:4)7:48(cid:4) (cid:4)ð (cid:3) Þ
0:63 106 Btu=h
¼ (cid:4)
(7.48 is the conversion factor from cubic feet to gallons.)
Copyright © 2003 Marcel Dekker, Inc.

TABLE6.2 HeatContent (Btu=gal) ofVariousOilsa
Gravity, API at60 F(15.6 C)
(cid:2) (cid:2) (cid:2)
10 15 20 25 30 35 40 45
Specific gravity,60 F=60 F
(cid:2) (cid:2)
Temp.
( F) 1.0000 0.9659 0.9340 0.9042 0.8762 0.8498 0.8251 0.8017
(cid:2)
32 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
60 95 93 92 90 89 87 86 85
965
100 237 233 229 226 222 219 215
1065 1062
120 310 305 300 295 290 286 281
1116 1112
140 384 378 371 366 360 355 349
1169 1164
160 460 453 445 438 431 425 418
1236 1223 1217
180 538 529 520 511 503 496 488
1293 1278 1272
200 617 607 596 587 577 569 560
1371 1352 1335 1327
220 697 686 674 663 652 643 633
1434 1412 1393 1384
240 779 766 753 741 729 718 707
1498 1474 1452 1442
260 862 848 833 820 807 795 783
1563 1537 1513 1502
300 1034 1017 999 984 968 954 939
1699 1668 1639 1626
400 1489 1463 1439 1416 1393 1372 1352 1333
2088 2064 2041 2018 1997 1977 1958
500 1981 1947 1914 1884 1854 1826 1799 1774
2497 2464 2434 2404 2376 2349 2324
600 2511 2467 2426 2387 2350 2314 2281 2248
2942 2901 2862 2825 2789 2756 2723
700 3078 3025 2974 2927 2881 2837 2796 2756
3478 3425 3374 3327 3281 3237 3196 3156
800 3683 3619 3559 3502 3447 3395 3345 3297
4008 3944 3884 3827 3772 3720 3670 3622
aValuesinregulartypeareforliquid;boldvaluesareforvapor.
Copyright © 2003 Marcel Dekker, Inc.

TABLE6.3 Combustion Constants
Heatofcombusionc
Spgr Btu=cuft Btu=lb
Mol. Lbper Cuft air
No.Substance Formula wta cuftb perlbb 1,00 ¼ 0b Gross Netd Gross Netd
1 Carbon C 12.01 — — — — — 14,093g 14,093
2 Hydrogen H2 2.016 0.005327 187.723 0.06959 325.0 275.0 61,100 51,623
3 Oxygen O2 32.000 0.08461 11.819 1.1053 — — — —
4 Nitrogen(atm) N2 28.016 0.07439c 13.443c 0.9718e — — — —
5 Carbonmonxide CO 28.01 0.07404 13.506 0.9672 321.8 321.8 4,347 4,347
6 Carbondioxide CO 44.01 0.1170 8.548 1.5282 — — — —
2
ParaffinseriesCnH2n 2
7 Methane þ CH4 16.041 0.04243 23.565 0.5543 1013.2 913.1 23,879 21,520
8 Ethane C H 30.067 0.08029c 12.455c 1.04882e 1792 1641 22,320 20,432
2 6
9 Propane C3H8 44.092 0.1196c 8.365c 1.5617c 2590 2385 21,661 19,944
10n-Butane C4H10 58.118 0.1582c 6.321c 2.06654e 3370 3113 21,308 19,680
11Isobutane C4H10 58.118 0.1582e 6.321e 2.06654e 3363 3105 21,257 19,629
12n-Pentane C5H12 72.144 0.1904e 5.252e 2.4872c 4016 3709 21,091 19,517
13Isopentane C H 72.144 0.1904e 5.252e 2.4g72e 4008 3716 21,052 19,47g
5 12
14Neopentane C5H12 72.144 0.1904e 5.252e 2.4872e 3993 3693 20,970 19,396
15n-Hexane C H 86.169 0.2274e 4.39ge 2.9704c 4762 4412 20,940 19,403
6 14
OlefinseriesC H
n 2n
16Ethylene C2H4 28.051 0.07456 13.412 0.9740 1613.8 1513.2 21,644 20,295
17Propylene C3H6 42.077 0.1110e 9.007e 1.4504e 2336 2186 21,041 19,691
18n-Butene(butylene) C4H8 56.102 0.1480e 6.756e 1.9336e 3084 2gg5 20,840 19,496
19Isobutene C4H8 56.102 0.1480e 6.756e 1.9336e 3068 2g69 20,730 19,382
20n-Pentene C H 70.128 0.1852e 5.400e 2.4190e 3836 3586 20,712 19,363
5 10
AromaticseriesCnH2n 6
21Benzene (cid:3) C6H6 76.107 0.2060c 4.852c 2.6920e 3751 3601 1g,210 17,480
22Toluene C H 92.132 0.2431c 4.113e 3.1760e 4484 4284 18,440 17,620
7 8
23Xylene C8H10 106.158 0.2803e 3.567e 3.6618e 5230 4980 18,650 17,760
Miscellaneousgases
24Acetylene C H 26.036 0.06971 14.344 0.9107 1499 1448 21,500 20,776
2 2
25Naphthalene C10H8 128.162 0.3384e 2.955e 4.4208e 5854f 5654f 17,298f 16,708f
26Methylalcohol CH3OH 32.041 0.0846e 11.820e 1.1052e g67.9 768.0 10,259 9,078
27Ethylalcohol C2H5OH 46.067 0.1216e 8.221e 1.5890e 1600.3 1450.5 13,161 11,929
2gAmmonia NH3 17.031 0.0456e 21.914e 0.5961e 441.1 365.1 9,668 8,001
29Sulfur S 32.06 — — — — — 3,983 3,983
30Hydrogensulfide H2S 34.076 0.09109e 10.979e 1.1g98e 647 596 7,100 6,545
31Sulfurdioxide SO2 64.06 0.1733 5.770 2.264 — — — —
32Watervapor H O 18.016 0.04758e 21.017e 0.6215e — — — —
2
33Air — 26.9 0.07655 13.063 1.0000 — — — —
Allgasvolumescorrectedto60(cid:2)Fand30in.Hgdry.Forgasessaturatedwithwaterat60(cid:2)F,1.73%oftheBtuvaluemustbe
deducted.
aCalculatedfromatomicweightsgiveninJournaloftheAmericanChemicalSociety,February1937.
bDensitiescalculatedfromvaluesgiveningLat0(cid:2)Cand760mmHintheInternationalCriticalTablesallowingfortheknown
deviationsfromthegaslaws.Wherethecoefficientofexpansionwasnotavailable,theassumedvaluewastakenas0.0037
per(cid:2)C.Comparethiswith0.003662,whichisthecoefficientforaperfectgas.Wherenodensitieswereavailable,the
volumeofthemolewastakenas22.4115L.
cConvertedtomeanBtuperlb(1=180oftheheatperlbofwaterfrom32to212(cid:2)F)fromdatabyFrederickD.Rossini,
NationalBureauofStandards,letterofApril10,1937,exceptasnoted.
Copyright © 2003 Marcel Dekker, Inc.

Cuftpercuftofcombustible Lbperlbofcombustible
Experimental
Requiredfor Requiredfor errorin
combustion Flueproducts combustion Flueproducts heatof
combustion
O2 N2 Air CO2 H2O N2 O2 N2 Air CO2 H2O N2 (
(cid:8)
%)
— — — — — — 2.664 8.863 11.527 3.664 — 8.863 0.012
0.5 1.882 2.382 — 1.0 1.882 7.937 26.407 34.344 — 8.937 26.407 0.015
— — — — — — — — — — — — —
— — — — — — — — — — — — —
0.5 1.882 2.382 1.0 — 1.882 0.571 1.900 2.471 1.571 — 1.900 0.045
— — — — — — — — — — — — —
2.0 7.528 9.528 1.0 2.0 7.528 3.990 13.275 17.265 2.744 2.246 13.275 0.033
3.5 13.175 16.675 2.0 3.0 13.175 3.725 12.394 16.119 2.927 1.798 12.394 0.030
5.0 18.821 23.821 3.0 4.0 18.821 3.629 12.074 15.703 2.994 1.634 12.074 0.023
6.5 24.467 30.967 4.0 5.0 24.467 3.579 11.908 15.487 3.029 1.550 11.908 0.022
6.5 24.467 30.967 4.0 5.0 24.467 3.579 11.908 15.487 3.029 1.550 11.908 0.019
8.0 30.114 38.114 5.0 6.0 30.114 3.548 11.805 15.353 3.050 1.498 11.805 0.025
8.0 30.114 38.114 5.0 6.0 30.114 3.548 11.805 15.353 3.050 1.498 11.805 0.071
8.0 30.114 38.114 5.0 6.0 30.114 3.548 11.805 15.353 3.050 1.498 11.805 0.11
9.5 35.760 45.260 6.0 7.0 35.760 3.528 11.738 15.266 3.064 1.464 11.738 0.05
3.0 11.293 14.293 2.0 2.0 11.293 3.422 11.385 14.807 3.138 1.285 11.385 0.021
4.5 16.939 21.439 3.0 3.0 16.939 3.422 11.385 14.807 3.138 1.285 11.385 0.031
6.0 22.585 28.585 4.0 4.0 22.585 3.422 11.385 14.807 3.138 1.285 11.385 0.031
6.0 22.585 28.585 4.0 4.0 22.585 3.422 11.385 14.807 3.138 1.285 11.385 0.031
7.5 28.232 35.732 5.0 5.0 28.232 3.422 11.385 14.807 3.138 1.285 11.385 0.037
7.5 28.232 35.732 6.0 3.0 28.232 3.073 10.224 13.297 3.381 0.692 10.224 0.12
9.0 33.878 32.g78 7.0 4.0 33.878 3.126 10.401 13.527 3.344 0.782 10.401 0.21
10.5 39.524 50.024 8.0 5.0 39.524 3.165 10.530 13.695 3.317 0.849 10.530 0.36
2.5 9.411 11.911 2.0 1.0 9.411 3.073 10.224 13.297 3.381 0.692 10.224 0.16
12.0 45.170 57.170 10.0 4.0 45.170 2.996 9.968 12.964 3.434 0.562 9.968 —
1.5 5.646 7.146 1.0 2.0 5.646 1.498 4.984 6.482 1.374 1.125 4.984 0.027
3.0 11.293 14.293 2.0 3.0 11.293 2.084 6.934 9.018 1.922 1.170 6.934 0.030
0.75 2.823 3.573 — 1.5 3.323 1.409 4.688 6.097 — 1.587 5.511 0.088
SO
2
— — — — — — 0.998 3.287 4.285 1.998 — 3.287 0.071
SO2 SO2
1.5 5.646 7.146 1.0 1.0 5.646 1.409 4.688 6.097 1.880 0.529 4.688 0.30
— — — — — — — — — — — — —
— — — — — — — — — — — — —
— — — — — — — — — — — — —
dDeductionfromgrosstonetheatingvaluedeterminedbydeducting18,919Btu=lbmolwaterintheproductsofcombustion.
Osborne,StimsonandGinnings,MechanicalEngineering,p.163,March1935,andOsborne,Stimson,andFlock,National
BureauofStandardsResearchPaper209.
eDenotesthateitherthedensityorthecoefficientofexpansionhasbeenassumed.Someofthematerialscannotexistas
gasesat60(cid:2)Fand30in.Hgpressure,inwhichcasethevaluesaretheoreticalonesgivenforeaseofcalculationofgas
problems.Undertheactualconcentrationsinwhichthesematerialsarepresenttheirpartialpressureislowenoughtokeep
themasgases.
fFromthirdeditionofCombustion.
AdaptedfromRef.8.
Copyright © 2003 Marcel Dekker, Inc.

6.09a
Q:
Natural gas having CH 83:4%;C H 15:8%, and N 0:8% by volume
4 ¼ 2 6 ¼ 2 ¼
isfiredinaboiler.Assuming15%excessair,70 Fambienttemperature,and80%
(cid:2)
relative humidity, perform detailed combustion calculations and determine flue
gas analysis.
A:
FromChapter5weknowthatairat70 Fand80%RHhasamoisturecontentof
(cid:2)
0.012lb=lb dry air. Table 6.3 can be used to figure air requirements of various
fuels.Forexample,weseethatCH requires9.53molofairpermoleofCH ,and
4 4
C H requires 16.68mol.
2 6
Let us base our calculations on 100mol of fuel. The theoretical dry air
required will be
83:4 9:53 16:68 15:8 1058:3mol
(cid:4) þ (cid:4) ¼
Considering 15% excess,
Actual dry air 1.15 1058.3 1217mol
¼ (cid:4) ¼
Excess air 0.15 1058.3 158.7mol
¼ (cid:4) ¼
Excess O 158.7 0.21 33.3mol
2¼ (cid:4) ¼
Excess N 1217 0.79 961mol
2¼ (cid:4) ¼
(Air contains 21% by volume O , and the rest is N .)
2 2
0:012
Moisture in air 1217 29 23:5mol
¼ (cid:4) (cid:4) 18 ¼
(We multiplied moles of air by 29 to get its weight, and then the water quantity
was divided by 18 to get moles of water.)
Table 6.3 can also be used to get the moles of CO ;H O, N and O [3].
2 2 2 2
CO 1 83:4 2 15:8 115mol
2 ¼ (cid:4) þ (cid:4) ¼
H O 2 83:4 3 15:8 23:5 237:7mol
2 ¼ (cid:4) þ (cid:4) þ ¼
O 33:3mol
2 ¼
N 961 0:8 961:8mol
2 ¼ þ ¼
The total moles of flue gas produced is 115 237.7 33.3 961.8 1347.8.
þ þ þ ¼
Hence
115
%CO 100 8:5
2 ¼1347:8(cid:4) ¼
Similarly,
%H O 17:7; %O 2:5; %N 71:3
2 ¼ 2 ¼ 2 ¼
Copyright © 2003 Marcel Dekker, Inc.

The analysis above is on a wet basis. On a dry flue gas basis,
100
%CO 8:5 10:3%
2 ¼ (cid:4)100 17:7¼
(cid:3)
Similarly,
%O 3:0%; %N 86:7%
2 ¼ 2 ¼
Toobtainw ,w ,w ,andw ,weneedthedensityofthefuelorthemolecular
da wa dg wg
weight, which is
1
83:4 16 15:8 30 0:8 28 18:30
100(cid:4)ð (cid:4) þ (cid:4) þ (cid:4) Þ¼
29
w 1217 19:29lb dry air=lb fuel
da ¼ (cid:4)100 18:3¼
(cid:4)
23:5 18
w 19:29 (cid:4) 19:52lb wet air=lb fuel
wa ¼ þ18:3 100¼
(cid:4)
115 44 33:3 32 961 28
w (cid:4) þ (cid:4) þ (cid:4)
dg ¼ 1830
18lb dry gas=lb fuel
¼
115 44 33:3 32 237:7 18 961:8 28
w (cid:4) þ (cid:4) þ (cid:4) þ (cid:4)
wg ¼ 1830
20:40lb wet gas=lb fuel
¼
This procedure can be used when the fuel analysis is given. More often, plant
engineers will be required to estimate the air needed for combustion without a
fuel analysis. In such situations, the MM Btu basis of combustion and calcula-
tions will come in handy. This is discussed in Q6.10a.
6.09b
Q:
ForthecasestatedinQ6.09a,estimatethepartialpressureofwatervapor,p ,and
w
of carbon dioxide, p , in the flue gas. Also estimate the density of flue gas at
c
300 F.
(cid:2)
A:
The partial pressures of water vapor and carbon dioxide are important in the
determination of nonluminous heat transfer coefficients.
volume of water vapor
p 0:177atm 2:6psia
w ¼ total flue gas volume ¼ ¼
volume of carbon dioxide
p 0:085atm 1:27psia
c ¼ total flue gas volume ¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

To estimate the gas density, its molecular weight must be obtained (see Q5.05).
MW MW y
¼ ð i(cid:4) iÞ
28 71:3 18 17:7 32 2:5 44 8:5
P(cid:4) þ (cid:4) þ (cid:4) þ (cid:4)
¼ 100
27:7
¼
Hence, from Eq. (6),
14:7
r 27:7 492 0:05lb=cuft
g ¼ (cid:4) (cid:4)359 760 14:7¼
(cid:4) (cid:4)
The gas pressure was assumed to be 14.7psia. In the absence of flue gas
analysis, we can obtain the density as discussed in Q5.03.
40
r 0:052lb=cuft
g ¼760¼
6.10a
Q:
Discuss the basis for the million Btu method of combustion calculations.
A:
Each fuel such as natural gas, coal, or oil requires a certain amount of
stoichiometric air per MM Btu fired (on HHV basis). This quantity does not
varymuchwiththefuelanalysisandhasthereforebecomeavaluablemethodof
evaluatingcombustionairandfluegasquantitiesproducedwhenfuelgasanalysis
is not available.
For solid fuels such as coal and oil, the dry stoichiometric air w in lb=lb
da
fuel can be obtained from
O
w 11:53 C 34:34 H 2 4:29 S
da ¼ (cid:4) þ (cid:4) 2(cid:3) 8 þ (cid:4)
(cid:1) (cid:2)
where C;H ;O , and S are carbon, hydrogen, oxygen, and sulfur in the fuel in
2 2
fraction by weight.
For gaseous fuels, w is given by
da
w 2:47 CO 34:34 H 17:27 CH
da ¼ (cid:4) þ (cid:4) 2þ (cid:4) 4
13:3 C H 14:81 C H
þ (cid:4) 2 2þ (cid:4) 2 4
16:12 C H 4:32 O
þ (cid:4) 2 6(cid:3) (cid:4) 2
Copyright © 2003 Marcel Dekker, Inc.

Example 1
Let us compute the amount of air required per MM Btu fired for fuel oil.
C 0.875, H 0.125, and API 28.
(cid:2)
¼ ¼ ¼
Solution. From (4a),
HHV 17,887 57:5 28 102:2 0
¼ þ (cid:4) (cid:3) (cid:4)
19,497Btu=lb
¼
The amount of air in lb=lb fuel from the above equation is
w 11:53 0:875 34:34 0:125
da ¼ (cid:4) þ (cid:4)
14:38lb=lbfuel
¼
1MMBtuoffuelfiredrequires(1 106)=19,497 51.28lboffuel.Hence,from
(cid:4) ¼
the above, 51.28lb of fuel requires
51:28 14:38 737lb of dry air
(cid:4) ¼
Table6.4showsarangeof735–750.Tothismustbeaddedexcessair;theeffect
of moisture in the air should also be considered.
Example 2
Letustakethecaseofnaturalgaswiththefollowinganalysis:methane 83.4%,
¼
ethane 15.8%, and nitrogen 0.8%.
¼ ¼
Solution. Converting this to percent weight basis, we have
Fuel % vol MW Col2 col 3 % wt
(cid:4)
CH 18.3 16 1334.4 72.89
4
C H 15.8 30 474 25.89
2 6
N 0.8 28 22.4 1.22
2
Let us compute the air required in lb=lb fuel.
From Table 6.3,
Air required 17:265 0:7289 16:119 0:2589
¼ (cid:4) þ (cid:4)
16:75lb=lbfuel
¼
HHV of fuel 0:7289 23,876 0:2589 22,320
¼ (cid:4) þ (cid:4)
23,181Btu=lb
¼
where 23,876 and 22,320 are HHV of methane and ethane from Table 6.3.
Copyright © 2003 Marcel Dekker, Inc.

TABLE6.4 Combustion ConstantA ForFuels
No. Fuel A
1 Blastfurnace gas 575
2 Bagasse 650
3 Carbonmonoxide gas 670
4 Refineryand oilgas 720
5 Natural gas 730
6 Furnace oiland lignite 745–750
7 Bituminous coals 760
8 Anthracite 780
9 Coke 800
The amount of fuel equivalent to 1MM Btu would be (1 106)=
(cid:4)
23,181 43.1lb, which requires 43.1 16.75 722lb of air, or 1MM Btu
¼ (cid:4) ¼
firedwouldneed722lbofdryair;thisisclosetothevalueindicatedinTable6.4.
Let us take the case of 100% methane and see how much air it needs for
combustion.FromTable6.3,air requiredperpoundofmethaneis17.265lb,and
its heating value is 23,879Btu=lb. In this case 1MM Btu is equivalent to
(1 106)=23,879 41.88lb of fuel, which requires 41.88 17.265 723lb of
(cid:4) ¼ (cid:4) ¼
dry air.
Taking the case of propane, 1lb requires 15.703lb of air.
1 106
1MM Btu (cid:4) 46:17lbfuel
¼ 21,661 ¼
This would require 46.17 15.703 725lb of air.
(cid:4) ¼
Thusforallfossilfuelswecancomeupwithagoodestimateoftheoretical
dry air per MM Btu fired on HHV basis, and gas analysis does not affect this
value significantly. The amount of air per MM Btu is termed A and is shown in
Table 6.4 for various fuels.
6.10b
Q:
A fired heater is firing natural gas at an input of 75MM Btu=h on HHV basis.
Determine the dry combustion air required at 10% excess air and the amount of
flue gas produced if the HHV of fuel is 20,000Btu=lb.
A:
From Table 6.4, A is 730lb=MM Btu. Hence the total air required is
W 75 1:1 730 60,200lb=h
a ¼ (cid:4) (cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

The flue gas produced is
106
W W W 60,200 60,250lb=h
g ¼ aþ f ¼ þ20,000¼
These values can be converted to volume rates at any temperature using the
procedure described in Chapter 5.
TheMMBtumethodisquiteaccurateforengineeringpurposessuchasfan
selection and sizing of ducts and air and gas systems. Its advantage is that fuel
analysis need not be known, which is generally the case in power and process
plants.TheefficiencyofheatersandboilerscanalsobeestimatedusingtheMM
Btu method of combustion calculations.
6.10c
Q:
A coal-fired boiler is firing coal of HHV 9500Btu=lb at 25% excess air. If
¼
ambient conditions are 80 F, relative humidity 80%, and flue gas temperature
(cid:2)
300 F,estimatethecombustionairinlb=lbfuel,thevolumeofcombustionairin
(cid:2)
cu ft=lb fuel, the flue gas produced in lb=lb fuel, and the flue gas volume in cu
ft=lb fuel.
A:
Because the fuel analysis is not known, let us use the MM Btu method. From
Table 6.4, A 760 for coal. 1MM Btu requires 760 1.25 950lb of dry air.
¼ (cid:4) ¼
At 80% humidity and 80 F, air contains 0.018lb of moisture per pound of air
(cid:2)
(Chap. 5). Hence thewet air required per MM Btu fired is 950 1.018lb. Also,
1MM Btu fired equals 106=9500 105lb of coal. Hence (cid:4)
¼
950
w dry air, lb=lb fuel 9:05
da ¼ ¼105¼
1:018
w wet air, lb=lb fuel 950 9:21
wa ¼ ¼ (cid:4) 105 ¼
492
r density of air at 80 F 29
a ¼ (cid:2) ¼ (cid:4)359 540
(cid:4)
0:0736lb=cuft seeChap:5;Q5:03 :
¼ ð Þ
Hence
9:21
Volume of air 125cu ft=lb fuel
¼0:0736¼
40
r density of flue gas 0:0526lb=cuft
g ¼ ¼760¼
950 105
w dry flue gas in lb=lb fuel þ 10:05
dg ¼ ¼ 105 ¼
10:05
Volume of flue gas, cu ft=lb fuel 191
¼0:0526¼
Copyright © 2003 Marcel Dekker, Inc.

6.11
Q:
Is there a way to figure the excess air from flue gas CO readings?
2
A:
Yes.AgoodestimateofexcessairEinpercentcanbeobtainedfromtheequation
K
E 100 1 1 10a
¼ (cid:4) %CO (cid:3) ð Þ
(cid:1) 2 (cid:2)
%CO is the percent of carbon dioxide in dry flue gas by volume, and K is a
2 1
constant depending on the type of fuel, as seen in Table 6.5. For example, if
%CO 15 in flue gas in a coal-fired boiler, then for bituminous coal
2¼
(K 18.6),
1¼
18:6
E 100 1 24%
¼ (cid:4) 15 (cid:3) ¼
(cid:1) (cid:2)
6.12
Q:
Discuss the significance of %CO and %O in flue gases.
2 2
A:
Excess air levels in fluegas can be estimated if the %CO and %O in dry flue
2 2
gas by volume are known. The higher the excess air, the greater the flue gas
quantity and the greater the losses. Plant engineers should control excess air
levelstohelpcontrolplantoperatingcosts.Thecostofoperationwithhighexcess
air is discussed in Q6.13.
A formula that is widely used to figure the excess air is [1]
O CO=2
E 100 2(cid:3) 10b
¼ (cid:4)0:264 N O CO=2 ð Þ
(cid:4) 2(cid:3)ð 2(cid:3) Þ
TABLE6.5 K Factors forFuels
1
Fueltype K
1
Bituminous coals 18.6
Coke 20.5
Oil 15.5
Refinerygasand gasoil 13.4
Natural gas 12.5
Blastfurnace gas 25.5
Source:Ref.1.
Copyright © 2003 Marcel Dekker, Inc.

whereO ;CO,andN aretheoxygen,carbonmonoxide,andnitrogenindryflue
2 2
gas, vol%, and E is the excess air, %.
Another formula that is quite accurate is [1]
O
E K 2 10c
¼ 2(cid:4)21 O ð Þ
(cid:3) 2
where K is a constant that depends on the type of fuel (see Table 6.6).
2
6.13
Q:
Inanaturalgasboilerofcapacity50MMBtu=h(HHVbasis),theoxygenlevelin
the flue gas is reduced from 3.0% to 2.0%. What is the annual savings in
operatingcostsiffuelcosts$4=MMBtu?TheHHVofthefuelis19,000Btu=lb.
The exit gas temperature is 500 F, and the ambient temperature is 80 F.
(cid:2) (cid:2)
A:
Theoriginalexcessairis90 3= 21 3 15%(seeQ6.12).Theexcessairis
(cid:4) ð (cid:3) Þ¼
now
2:0
E 90 9:47%
¼ (cid:4)21 2¼
(cid:3)
With 15% excess, the approximate air required (see Q6.10a) is 50 746
(cid:4) (cid:4)
1.15 42,895lb=h.
¼
106
Flue gas 42,895 50 45,256lb=h
¼ þ (cid:4)19,000¼
TABLE6.6 Constant k Used in
2
Eq. (10c)
Fuel K
2
Carbon 100
Hydrogen 80
Carbonmonoxide 121
Sulfur 100
Methane 90
Oil 94.5
Coal 97
Blastfurnace gas 223
Cokeoven gas 89.3
Source:Ref.1.
Copyright © 2003 Marcel Dekker, Inc.

With 9.47% excess air,
Air required 50 746 1:0947 40,832lb=h
¼ (cid:4) (cid:4) ¼
106
Flue gas produced 40,832 50
¼ þ (cid:4)19,000
43,463lb=h
¼
Reduction in heat loss 45,526 43,463 0:25 500 80
¼ð (cid:3) Þ(cid:4) (cid:4)ð (cid:3) Þ
0:22MMBtu=h
¼
This is equivalent to an annual savings of 0.22 4 300 24 $6336. (We
(cid:4) (cid:4) (cid:4) ¼
assumed 300 days of operation a year.) This could be a significant savings
considering the life of the plant. Hence plant engineers should operate the plant
realizing the implications of high excess air and high exit gas temperature.
Oxygen levels can be continuously monitored and recorded and hooked up to
combustion air systems in order to operate the plant more efficiently. (It may be
noted that exitgas temperaturewill also be reduced ifexcessair isreduced. The
calculation above indicates the minimum savings that can be realized.)
6.14
Q:
Fuels are often interchanged in boiler plants because of relative availability and
economics. It is desirable, then, to analyze the effect on the performance of the
system. Discuss the implications of burning coal of 9800Btu=lb in a boiler
originally intended for 11,400Btu=lb coal.
A:
Letusassumethatthedutydoesnotchangeandthattheefficiencyoftheunitis
not altered. However, the fuel quantity will change. Combustion air required,
beingafunctionofMMBtufired,willnotchange,butthefluegasproducedwill
increase. Let us prepare a table.
Coal1 Coal2
FuelHHV, Btu=lb 11,400 9800
FuelfiredperMMBtu (106=HHV) 87 102
Airrequired perMMBtu (25%excessair) 760 1.25 950 760 1.25 950
(cid:4) ¼ (cid:4) ¼
Fluegas,lb 1037 1052
Ratio offlue gas 1 1.015
Wecanusethesamefans,becausethevariationinfluegasproducedisnot
significantenoughtowarranthighergaspressuredrops.Wemustlookintoother
Copyright © 2003 Marcel Dekker, Inc.

aspects,suchasthenecessityofhighercombustionairtemperature(duetohigher
moisture in the fuel), ash concentration, and fouling characteristics of the new
fuel. If a different type of fuel is going to be used, say oil, this will be a major
change,andthefuel-handlingsystem’sburnersandfurnacedesignwillhavetobe
reviewed. Thegas temperature profileswill change owing to radiation character-
istics, and absorption of surfaces such as superheaters and economizers will be
affected. A discussion with the boiler design engineers will help.
6.15
Q:
What is meant by combustion temperature of fuels? How is it estimated?
A:
The adiabatic combustion temperature is the maximum temperature that can be
attained by the products of combustion of fuel and air. However, because of
dissociation and radiation losses, this maximum is never attained. Estimation of
temperatureafterdissociationrequiressolvingseveralequations.Forpurposesof
estimation, we may decrease the adiabatic combustion temperature by 3–5% to
obtain the actual combustion temperature.
From an energy balance it can be shown that
LHV Aa HHV C t 80 =106
t þ (cid:4) (cid:4) pa(cid:4)ða(cid:3) Þ 11
c ¼ 1 %ash=100 Aa HHV=106 C ð Þ
ð (cid:3) þ (cid:4) Þ(cid:4) pg
where
LHV;HHV lower and higher calorific value of fuel, Btu=lb
¼
A theoretical air required per million Btu fired, lb
¼
a excess air factor 1 E=100
¼ ¼ þ
t ;t temperature of air and combustion temperature, F
a c¼ (cid:2)
C ;C specific heats of air and products of combustion, Btu=lb F
pa pg¼ (cid:2)
For example, for fuel oil with combustion air at 300 F, LHV 17,000Btu=
(cid:2)
¼
lb, HHV 18,000Btu=lb, a 1.15, and A 745 (see Table 6.4). We have
¼ ¼ ¼
17,000 745 1:15 18,000 0:25 300 80 =106
t þ (cid:4) (cid:4) (cid:4) (cid:4)ð (cid:3) Þ
c ¼ 1 745 1:15 18,000=106 0:32
ð þ (cid:4) (cid:4) Þ(cid:4)
3400 F
(cid:2)
¼
C and C were taken as 0.25 and 0.32, respectively.
pa pg
Copyright © 2003 Marcel Dekker, Inc.

6.16a
Q:
How is the ash concentration in flue gases estimated?
A:
Particulate emissiondata are needed to size dust collectorsfor coal-firedboilers.
In coal-fired boilers, about 75% of the ash is carried away by the flue gases and
25% drops into the ash pit. The following expression may be derived using the
MM Btu method of combustion calculation [5]:
240,000 %ash=100
C (cid:4)ð Þ 12a
a ¼T 7:6 10 6 HHV 100 E 1 %ash=100 ð Þ
(cid:4)½ (cid:4) (cid:3) (cid:4) (cid:4)ð þ Þþ (cid:3)ð Þ(cid:5)
where
C ash concentration, grains=cu ft
a¼
E excess air, %
¼
T gas temperature, R
(cid:2)
¼
HHV higher heating value, Btu=lb
¼
Example
If coals of HHV 11,000Btu=lb having 11% ash are fired in a boiler with 25%
¼
excessairandthefluegastemperatureis850 R,determinetheashconcentration.
(cid:2)
Solution. Substituting into Eq. (12a), we have
240,000 0:11
C (cid:4)
a ¼850 7:6 10 6 11,000 125 1 0:11
(cid:4)ð (cid:4) (cid:3) (cid:4) (cid:4) þ (cid:3) Þ
2:75grains=cuft
¼
6.16b
Q:
Howdoyouconverttheashconcentrationinthefluegasinwt%tograins=acfor
grains=scf?
A:
Flue gases from incineration plants or solid fuel boilers contain dust or ash, and
oftenthesecomponentsareexpressedinmassunitssuchaslb=horwt%,whereas
engineers involved in selection of pollution control equipment prefer towork in
terms of grains=acf or grains=scf (actual and standard cubic feet). The relation-
ship is
C 0:01 A 7000 r 70A 12b
a ¼ (cid:4) (cid:4) (cid:4) ¼ ð Þ
Copyright © 2003 Marcel Dekker, Inc.

where
r gas density, lb=cu ft 39.5=(460 t)
¼ ¼ þ
t gas temperature, F
(cid:2)
¼
C ashcontent,grains=acforgrains=scfdependingonwhetherdensityis
a¼
computed at actual temperature or at 60 F
(cid:2)
A ash content, wt%
¼
Theexpressionfordensityisbasedonatmosphericfluegaseshavingamolecular
weight of 28.8 (see Q5.03).
Fluegasescontain1.5wt%ash.Theconcentrationingrains=acfat400 Fis
(cid:2)
39:5
C 70 1:5 4:8grains=acf
a ¼ (cid:4) (cid:4) 860 ¼
and at 60 F,
(cid:2)
39:5
C 70 1:5 7:98grains=scf
a ¼ (cid:4) (cid:4) 520 ¼
6.17
Q:
Discusstheimportanceofthemeltingpointofashincoal-firedboilers.Howisit
estimated?
A:
In the design of steam generators and ash removal systems, the ash fusion
temperatureisconsideredanimportantvariable.Lowashfusiontemperaturemay
cause slagging and result in deposition of molten ash on surfaces such as
superheaters and furnaces. The furnace will then absorb less energy, leading to
higher furnace exit gas temperatures and overheating of superheaters.
A quick estimate of ash melting temperature in C can be made using the
(cid:2)
expression [6]
t 19 Al O 15 SiO TiO
m ¼ (cid:4) 2 3þ (cid:4)ð 2þ 2Þ
10 CaO MgO
þ (cid:4)ð þ Þ
6 Fe O Na O K O
þ (cid:4)ð 2 3þ 2 þ 2 Þ
wheret isthefusiontemperaturein C,andtherestofthetermsarepercentash
m (cid:2)
content of oxides of aluminum, silicon, titanium, calcium, magnesium, iron,
sodium, and potassium.
Copyright © 2003 Marcel Dekker, Inc.

Example
Analysis of a given ash indicates the following composition:
Al O 20%; SiO TiO 30%
2 3 ¼ 2þ 2 ¼
Fe O Na O K O 20%; CaO MgO 15%
2 3þ 2 þ 2 ¼ þ ¼
Find the fusion temperature.
Solution. Substituting into Eq. (13), we find that t 1100 C.
m¼ (cid:2)
6.18a
Q:
WhatistheemissionofSO inlb=MMBtuifcoalsofHHV 11,000Btu=lband
2 ¼
having 1.5% sulfur are fired in a boiler?
A:
The following expression gives e, the emission of SO in lb=MM Btu:
2
S
e 2 104 14
¼ (cid:4) HHV ð Þ
where S is the percent sulfur in the fuel.
1:5
e 2 104 2:73lb=MMBtu
¼ (cid:4) (cid:4)11,000¼
If an SO scrubbing system of 75% efficiency is installed, the exiting SO
2 2
concentration will be 0.25 2.73 0.68lb=MM Btu.
(cid:4) ¼
6.18b
Q:
WhatistheSO levelinppm(partspermillion)byvolumeifthecoalsinQ6.18a
2
are fired with 25% excess air?
A:
We have to estimate the flue gas produced. Using the MM Btu method,
106
w 1:25 760 1041lb=MMBtu
g ¼11,000þ (cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

Let the molecular weight be 30, which is a good estimate in the absence of flue
gas analysis. Then,
1041
Moles of flue gas 34:7per MM Btu fired
¼ 30 ¼
2:73
Moles of SO
2 ¼ 64
0:042 (from Q6.18a and Table 5.1)
¼
(64 is the molecular weight of SO . Dividing weight by molecular weight gives
2
the moles.)
Hence ppm of SO in flue gas will be 0.042 106=34.7 1230ppm.
2 (cid:4) ¼
6.18c
Q:
If5%oftheSO getsconvertedtoSO ,estimatetheppmofSO inthefluegas.
2 3 3
A:
2:73
Moles of SO 0:05 0:0017perMMBtu
3 ¼ (cid:4) 80 ¼
Hence
0:0017
ppm by volume of SO 106 49ppm
3 ¼ 34:7 (cid:4) ¼
(80 is the molecular weight of SO .)
3
6.19a
Q:
How is the efficiency of a boiler or a fired heater determined?
A:
The estimation of the efficiency of a boiler or heater involves computation of
several losses such as those due to flue gases leaving the unit, unburned fuel,
radiationlosses,heatlossduetomoltenash,andsoon.Readersmayrefertothe
ASMEPowerTestCode[7]fordetails.Twomethodsarewidelyused,onebased
on the measurement of input and output and the other based on heat losses. The
latter is preferred, because it is easy to use.
Copyright © 2003 Marcel Dekker, Inc.

There are two ways of stating the efficiency, one based on HHV and the
other on LHV. As discussed in Q6.01,
Z HHV Z LHV
HHV(cid:4) ¼ LHV(cid:4)
The various losses are [1], on an HHV basis,
1. Dry gas loss, L :
1
t t
L 24w g(cid:3) a 15a
1 ¼ dg HHV ð Þ
2. Loss due to combustion of hydrogen and moisture in fuel, L :
2
L 9 H W 1080 0:46t t
2 ¼ð (cid:4) 2þ Þ(cid:4)ð þ g(cid:3) aÞ
100
(cid:4)HHV
3. Loss due to moisture in air, L :
3
t t
L 46Mw g(cid:3) a 15c
3 ¼ da HHV ð Þ
4. Radiation loss, L . The American Boiler Manufacturers Association
4
(ABMA) chart [7] may be referred to to obtain this value. A quick
estimate of L is
4
L 100:62 0:42logQ 15d
4 ¼ (cid:3) ð Þ
For Eqs. (15a)–(15d),
w dry flue gas produced, lb=lb fuel
dg¼
w dry air required, lb=lb fuel
da¼
H ;W hydrogen and moisture in fuel, fraction
2 ¼
M moisture in air, lb=lb dry air (see Q5.09b)
¼
t ;t temperatures of flue gas and air, F
g a¼ (cid:2)
Q duty in MM Btu=h
¼
5. To losses L –L must be added a margin or unaccounted loss, L .
1 4 5
Hence efficiency becomes
Z 100 L L L L L 15e
HHV ¼ (cid:3)ð 1þ 2þ 3þ 4þ 5Þ ð Þ
Note that combustion calculations are a prerequisite to efficiency determination.
If the fuel analysis is not available, plant engineers can use the MM Btu method
to estimate w rather easily and then estimate the efficiency (see Q6.20).
dg
The efficiency can also be estimated on LHV basis. The various losses
considered are the following.
Copyright © 2003 Marcel Dekker, Inc.

1. Wet flue gas loss:
t t
w C g(cid:3) a 15f
wg p HHV ð Þ
(C , gas specific heat, will be in the range of 0.26–0.27 for wet flue
p
gases.)
2. Radiation loss (see Q6.23)
3. Unaccounted loss, margin
Then
Z 100 sum of the above three losses
LHV ¼ (cid:3)ð Þ
One can also convert Z to Z using Eq. (3b) (see Q6.01).
HHV LHV
6.19b
Q:
Coals of HHV 13,500Btu=lb and LHV 12,600Btu=lb are fired in a boiler
¼ ¼
with25%excessair.Iftheexitgastemperatureis300 Fandambienttemperature
(cid:2)
is 80 F, determine the efficiency on HHV basis and on LHV basis.
(cid:2)
A:
FromtheMMBtumethodofcombustioncalculations,assumingthatmoisturein
air is 0.013lb=lb dry air,
1:013 760 1:25 106=13,500
w (cid:4) (cid:4) þ
wg ¼ 106=13,500
1036
14:0
¼ 74 ¼
(760 is the constant obtained from Table 6.4.) Hence
wet flue gas loss 100 14:0 0:26
¼ (cid:4) (cid:4)
300 80
(cid:3)
(cid:4) 12,600
6:35%
¼
Let radiation and unaccounted losses be 1.3%. Then
Z 100 6:35 1:3 92:34%
LHV ¼ (cid:3)ð þ Þ¼
12,600
Z 92:34 86:18%
HHV ¼ (cid:4)13,500¼
(Radiationlossesvaryfrom0.5%to1.0%inlargeboilersandmaygoupto2.0%
in smaller units. The major loss is the flue gas loss.)
Copyright © 2003 Marcel Dekker, Inc.

6.19c
Q:
DeterminetheefficiencyofaboilerfiringthefuelgiveninQ6.09aat15%excess
air. Assume radiation loss 1%, exit gas temperature 400 F, and ambient
(cid:2)
¼ ¼
temperature 70 F. Excess air and relative humidity are the same as in Q6.09a
(cid:2)
¼
(15% and 80%).
A:
Results of combustion calculations are already available.
Dry flue gas 18lb=lbfuel
¼
Moisture in air 19:52 19:29 0:23lb=lb fuel
¼ (cid:3) ¼
Water vapor formed due to combustion of fuel
¼
20:4 18 0:23 2:17lb=lbfuel
(cid:3) (cid:3) ¼
83:4 1013:2 15:8 1792
HHV (cid:4) þ (cid:4) 1128Btu=cuft
¼ 100 ¼
Fuel density at 60 F 18.3=379 0.483lb=cu ft, so
(cid:2)
¼ ¼
1128
HHV 23,364Btu=lb
¼0:0483¼
The losses are
1. Dry gas loss,
400 70
L 100 18 0:24 (cid:3) 6:1%
1 ¼ (cid:4) (cid:4) (cid:4) 23,364 ¼
2. Loss due to combustion of hydrogen and moisture in fuel,
1080 0:46 400 70
L 100 2:17 þ (cid:4) (cid:3)
2 ¼ (cid:4) (cid:4) 23,364
11:1%
¼
3. Loss due to moisture in air,
400 70
L 100 0:23 0:46 (cid:3) 0:15%
3 ¼ (cid:4) (cid:4) (cid:4) 23,364 ¼
4. Radiation loss 1.0%
¼
5. Unaccounted losses and margin 0%
¼
Total losses 6:1 11:1 0:15 1:0 18:35%
¼ þ þ þ ¼
Hence
Efficiency on HHV basis 100 18:35 81:65%
¼ (cid:3) ¼
One can convert this to LHV basis after computing the LHV.
Copyright © 2003 Marcel Dekker, Inc.

6.19d
Q:
How do excess air and boiler exit gas temperature affect the various losses and
boiler efficiency?
A:
Table 6.7 shows the results of combustion calculations for various fuels at
different excess air levels and boiler exit gas temperatures. It also shows the
amount of CO generated per MM Btu fired.
2
It can be seen that natural gas generates the lowest amount of CO .
2
106 9:06 44
CO =MMBtu, natural, gas 19:17 (cid:4) 116:5lb
2 ¼23,789(cid:4) (cid:4)27:57 100¼
(cid:4)
TABLE6.7 Combustion Calculations forVarious Fuels
Gas Oil Coal
T ; F 350 450 350 450 350 450 350 450 450 550
go (cid:2)
EA,% 5 5 15 15 5 5 15 15 25 25
CO 9.06 8.34 12.88 11.82 13.38
2
H O 19.11 17.70 12.37 11.47 7.10
2
N 70.93 71.48 73.83 74.19 75.43
2
O 0.90 2.48 0.92 2.53 3.94
2
SO 0.15
2
W =W 19.17 20.9 16.31 17.77 13.42
g f
L ,% 4.74 6.44 5.23 7.09 5.13 6.96 5.62 7.63 8.91 11.25
1
L ,% 0.09 0.12 0.10 0.13 0.09 0.12 0.10 0.14 0.15 0.19
2
L ,% 10.89 11.32 10.89 11.32 6.63 6.89 6.63 6.89 4.3 4.46
3
Gas Oil Coal
T , F 350 450 350 450 350 450 350 450 450 550
go (cid:2)
EA,% 5 5 15 15 5 5 15 15 25 25
L ,% 1.0
4
E ,% 83.2 81.1 82.9 80.5 87.1 85.0 86.7 84.3 85.6 83.0
h
E,% 92.3 89.9 91.7 89.2 92.8 90.0 92.3 89.9 89.0 86.4
l
MW 27.57 27.66 28.86 28.97 29.64
Coal (wt%): C 72.8, H 4.8, N 1.5, O 6.2, S 2.2, H O 3.5, ash 9.0;
¼ 2¼ 2¼ 2¼ ¼ 2 ¼ ¼
HHV 13139Btu=lb;LHV 12,634Btu=lb.
¼ ¼
Oil(wt%):C 87.5,H 12.5, API 32;HHV 19,727Btu=lb;LHV 18,512Btu=lb.
¼ 2¼ (cid:2) ¼ ¼ ¼
Gas(vol%):CH 97;C H 2,C H 1;HHV 23,789Btu=lb;LHV 21,462Btu=lb.
4¼ 2 6¼ 3 8¼ ¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

(The above is obtained by converting the volumetric analysis to weight basis
using the molecular weights of CO and the flue gas.) For oil, CO genera-
2 2
ted 162.4lb, and for coal, 202.9lb.
¼
6.20
Q:
A fired heater of duty 100MM Btu=h (HHV basis) firing No. 6 oil shows the
following dry flue gas analysis:
CO 13:5%; O 2:5%; N 84%
2 ¼ 2 ¼ 2 ¼
The exit gas temperature and ambient temperature are 300 F and 80 F, respec-
(cid:2) (cid:2)
tively. If moisture in air is 0.013lb=lb dry air, estimate the efficiency of the unit
on LHV and HHV basis. LHV 18,400Btu=lb and HHV 19,500Btu=lb.
¼ ¼
A:
Because the fuel analysis is not known, let us estimate the flue gas produced by
the MM Btu method. First, compute the excess air, which is
2:5
E 94:5 12:8%
¼ (cid:4)21 2:5¼
(cid:3)
The factor 94.5 is from Table 6.6 (see Q6.12). The wet flue gas produced is
745 1:128 1:013 106
(cid:4) (cid:4)
106 þ19,500
106=19,500
17:6lb=lbfuel
¼
Hence
300 80
Wet gas loss 100 17:6 0:26 (cid:3) 5:47%
¼ (cid:4) (cid:4) (cid:4) 18,400 ¼
The radiation loss on HHV basis can be approximated by Eq. (15d):
Radiation loss 100:62 0:42logQ 0:60%
(cid:3)
¼ ¼
Q 100MMBtu=h
¼
Let us use 1.0% on LHV basis, although this may be a bit high. Hence the
efficiency on LHV basis is 10076.47 93.53%. The efficiency on HHV basis
¼
would be [Eq. (3b)]
Z HHV Z LHV
HHV(cid:4) ¼ LHV(cid:4)
Copyright © 2003 Marcel Dekker, Inc.

or
18,400
Z 95:53 88:25
HHV ¼ (cid:4)19,500¼
Thus,evenintheabsenceoffuelultimateanalysis,theplantpersonnelcancheck
the efficiency of boilers and heaters based on operating data.
6.21
Q:
How is the loss due to incomplete combustion such as the formation of CO
determined?
A:
Effortsmust be made by theboilerand burnerdesigners to ensure that complete
combustion takes place inthefurnace.However, because of variousfactorssuch
as size offuel particles, turbulence, and availability ofair to fuel and themixing
process, some carbon monoxide will be formed, which means losses. If CO is
formed from carbon instead of CO , 10,600Btu=lb is lost. This is the difference
2
between the heat of reaction of the two processes
C O CO and C O CO
þ 2 ! 2 þ 2 !
The loss in Btu=lb is given by [1]
CO
L 10,160 C
¼CO CO (cid:4) (cid:4)
þ 2
whereCisthecarbon inthefuel,fractionbyweight,andCOandCO arevol%
2
of the gases.
Example
DeterminethelossesduetoformationofCO ifcoalwithHHVof12,000Btu=lb
isfiredinaboiler,giventhatCOandCO inthefluegasare1.5%and17%and
2
the fuel has a carbon content of 56%.
Solution. Substituting into the equation given above,
1:5 0:56
L 10,160 0:038
¼18:5(cid:4) (cid:4)12,000¼
or L 3.8% on HHV basis (dividing loss in Btu=lb by HHV).
¼
Copyright © 2003 Marcel Dekker, Inc.

6.22
Q:
Is there a simple formula to estimate the efficiency of boilers and heaters if the
excess air and exit gas temperature are known and the fuel analysis is not
available?
A:
Boilerefficiencydependsmainlyonexcessairandthedifferencebetweentheflue
gas exit temperature and the ambient temperature. The following expressions
have been derived from combustion calculations for typical natural gas and oil
fuels. These may be used for quick estimations.
For natural gas:
Z ,% 89:4 0:001123 0:0195 EA DT 16a
HHV ¼ (cid:3)ð þ (cid:4) Þ(cid:4) ð Þ
Z ,% 99:0 0:001244 0:0216 EA DT 16b
LHV ¼ (cid:3)ð þ (cid:4) Þ(cid:4) ð Þ
For fuel oils:
Z ,% 92:9 0:001298 0:01905 EA DT
HHV ¼ (cid:3)ð þ (cid:4) Þ(cid:4)
Z ,% 99:0 0:001383 0:0203 EA DT
LHV ¼ (cid:3)ð þ (cid:4) Þ(cid:4)
where
EA excess air factor (EA 1.15 means 15% excess air)
¼ ¼
DT difference between exit gas and ambient temperatures
¼
Example
Naturalgasat15%excessairisfiredinaboiler,withexitgastemperature280 F
(cid:2)
and ambient temperature 80 F. Determine the boiler efficiency. EA 1:15 and
(cid:2)
¼
DT 280 80 200 F.
(cid:2)
¼ (cid:3) ¼
Solution.
Z 89:4 0:001123 0:0195 1:15
HHV ¼ (cid:3)ð þ (cid:4) Þ
280 80 84:64%
(cid:4)ð (cid:3) Þ¼
Z 99:0 0:001244 0:0216 1:15
LHV ¼ (cid:3)ð þ (cid:4) Þ
280 80 93:78%
(cid:4)ð (cid:3) Þ¼
The above equations are based on 1% radiation plus unaccounted losses.
Copyright © 2003 Marcel Dekker, Inc.

6.23
Q:
Theaveragesurfacetemperatureofthealuminumcasingofagas-firedboilerwas
measured to be 180 F when the ambient temperature was 85 F and the wind
(cid:2) (cid:2)
velocity was 5mph. The boiler was firing 50,000scfh of natural gas with
LHV 1075Btu=scf. Determine the radiation loss on LHV basis if the total
surfac ¼ e area of the boiler was 2500ft2. Assume that the emissivity of the
casing 0.1.
¼
A:
Thisexampleshowshowradiationlosscanbeobtainedfromthemeasurementof
casing temperatures. Thewind velocity is 5mph 440fpm. From Q8.51 we see
that the heat loss q in Btu=ft2 h will be ¼
q 0:173 10 8 0:1 460 180 4 460 85 4
(cid:3)
¼ (cid:4) (cid:4) (cid:4)½ð þ Þ (cid:3)ð þ Þ (cid:5)
440 69
0:296 180 85 1:25 þ 17
þ (cid:4)ð (cid:3) Þ (cid:4) 69 ð Þ
rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
252Btu=ft2 h
¼
The total heat losswill be 2500 252 0.63 106Btu=h. The radiation loss on
LHV basis will be 0.63 106 (cid:4) 100=( ¼ 50,000 (cid:4) 1075) 1.17%. If the HHV of
(cid:4) (cid:4) (cid:4) ¼
the fuel were 1182Btu=scf, the radiation loss on HHV basis would be
0.63 1182=1075 1.06%.
(cid:4) ¼
6.24
Q:
How does the radiation loss vary with boiler duty or load? How does this affect
the boiler efficiency?
A:
Theheatlossesfromthesurfaceofaboilerwillbenearlythesameatallloadsif
theambienttemperatureandwindvelocityarethesame.Variationsinheatlosses
canoccurowingtodifferencesinthegastemperatureprofileintheboiler,which
varieswithload.However,forpracticalpurposesthisvariationcanbeconsidered
minor.Hencetheheatlossasapercentwillincreaseastheboilerdutydecreases.
The boiler exit gas temperature decreases with a decrease in load or duty
andcontributestosomeimprovementinefficiency,whichisoffsetbytheincrease
in radiation losses. Hence therewill be a slight increase in efficiency as the load
increases, and after a certain load, efficiency decreases.
Theabovediscussionpertainstofiredwatertubeorfiretubeboilersandnot
wasteheatboilers,whichhavetobeanalyzedforeachloadbecausethegasflow
Copyright © 2003 Marcel Dekker, Inc.

and inletgas temperature canvary significantly with load depending on the type
of process or application.
6.25a
Q:
Discuss the importance of dew point corrosion in boilers and heaters fired with
fuels containing sulfur.
A:
During the process of combustion, sulfur in fuels such as coal, oil, and gas is
converted to sulfur dioxide. Some portion of it (1–5%) is converted to sulfur
trioxide, which can combine with water vapor in the flue gas to form gaseous
sulfuric acid. If the surface in contact with the gas is cooler than the acid dew
point,sulfuricacidcancondenseonit,causingcorrosion.ADP(acid dewpoint)
isdependentonseveralfactors,suchasexcessair,percentsulfurinfuel,percent
conversion of SO to SO , and partial pressure of water vapor in the flue gas.
2 3
Manufacturers of economizers and air heaters suggest minimum cold-end
temperaturesthatarerequiredtoavoidcorrosion.Figures6.1and6.2aretypical.
Sometimes the minimum fluid temperature, which affects the tube metal
temperature, is suggested. The following equation gives a conservative estimate
of the acid dew point [8]:
T 1:7842 0:0269log p 0:129 logp
dp ¼ þ w(cid:3) SO 3 18a
0:329 logp logp ð Þ
þ w(cid:4) SO 3
where
T acid dew point, K
dp¼
p partial pressure of water vapor, atm
w¼
p partial pressure of sulfur trioxide, atm
SO 3¼
Table6.8givestypicalp valuesfor variousfuelsandexcessair.Q6.18c
SO
3
shows how ppmSO can be computed from which p is obtained.
3 SO
3
ApracticalwaytodetermineT istouseadewpointmeter.Anestimation
dp
of the cold-end metal temperature can give an indication of possible corrosion.
6.25b
Q:
How is the dew point of an acid gas computed?
A:
Table 6.9 shows the dew point correlations for various acid gases [9,11].
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 6.1 The relationship between SO and ADT. (Courtesy of Land
3
Combustion Inc.)
Fluegas from an incinerator has the following analysis (vol%): H O 12,
2 ¼
SO 0.02, HCl 0.0015 and the rest oxygen and nitrogen. Gas pressure
2¼ ¼
10in. wg. Compute the dew points of sulfuric and hydrochloric acids given
¼
that2%ofSO convertstoSO .Inordertousethecorrelations,thegaspressures
2 3
must be converted to mmHg. Atmospheric pressure 10in. wg 10=407
¼ ¼ ¼
0.02457atmg or 1.02457atm abs.
p 0:12 1:02457 760 93:44mmHg
H 2 O ¼ (cid:4) (cid:4) ¼
ln P 4:537
H 2 O ¼
P 0:0015 1:0245 760 0:1168mmHg
HCl ¼ (cid:4) (cid:4) ¼
ln p 2:1473
HCl ¼(cid:3)
Partial pressures of sulfuric acid and SO are equal. Hence
3
P 0:02 0:0002 760 1:0245 0:0031mmHg
SO 3 ¼ (cid:4) (cid:4) (cid:4) ¼
ln P 5:7716
SO 3 ¼(cid:3)
Substituting into the equations, we obtain the following.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 6.2 Limiting tube metal temperatures to avoid external corrosion in
economizersandairheaterswhenburningfuelscontainingsulfur.(FromRef.13,
with permission.)
For hydrochloric acid:
1000
3:7368 0:1591 4:537 0:0326 2:1473
T ¼ (cid:3) (cid:4) þ (cid:4)
dp
0:00269 4:537 2:1473 3:0588
(cid:3) (cid:4) (cid:4) ¼
or
T 327K 54 C 129 F
dp ¼ ¼ (cid:2) ¼ (cid:2)
TABLE6.8 SO inFlueGas (ppm)
3
Sulfur (%)
Fuel Excessair (%) 0.5 1.0 2.0 3.0 4.0 5.0
Oil 5 2 3 3 4 5 6
11 6 7 8 10 12 14
Coal 25 3–7 7–14 14–28 20–40 27–54 33–66
Copyright © 2003 Marcel Dekker, Inc.

TABLE6.9 DewPoints of AcidGasesa
Hydrobromicacid
1000=T 3.563970.1350ln P 70.0398 ln P
dp¼ H2O HBr
0.00235lnP lnP
þ H2O HBr
Hydrochloricacid
1000=T 3.736870.1591ln P 70.0326 ln P
dp¼ H2O HCl
0.00269lnP lnP
þ H2O HCl
Nitric acid
1000=T 3.661470.1446ln P 70.0827 ln P
dp¼ H2O HNO3
0.00756lnP lnP
þ H2O HNO3
Sulfurousacid
1000=T 3.952670.1863ln P 0.000867 lnP
dp¼ H3Oþ SO2
70.000913ln P ln P
H2O SO2
Sulfuric acid
1000=T 2.27670.0294 ln P 70.0858 lnP
dp¼ H2O H3SO4
0.0062ln P ln P
þ H2O H2SO4
aT is dewpoint temperature (K), and P is partial pressure(mmHg).
dp
Compared with published data, the predicted dew points are within
about6KofactualvaluesexceptforH SO ,whichiswithinabout9K.
2 4
Source: HCl, HBr, HNO and SO correlations were derived from
3 2
vapor–liquidequilibriumdata.TheH SO correlationisfromRef.5.
2 4
For sulfuric acid:
1000
2:276 0:0294 4:537 0:0858 5:7716
T ¼ (cid:3) (cid:4) þ (cid:4)
dp
0:0062 4:537 5:7716 2:4755
(cid:3) (cid:4) (cid:4) ¼
or
T 404K 131 C 268 F
dp ¼ ¼ (cid:2) ¼ (cid:2)
The dew points of other gases can be obtained in a similar manner.
6.25c
Q:
Doesthepotentialforaciddewpointcorrosiondecreaseifthegastemperatureat
the economizer is increased?
Copyright © 2003 Marcel Dekker, Inc.

A:
Acid dew pointswere computed in Q6.25a. If the tubewall temperatures can be
maintained above the dew point, then condensation of vapors is unlikely.
However, the tube wall temperature in a gas-to-liquid heat exchanger such as
theeconomizerisgovernedbythegasfilmheattransfercoefficientratherthanthe
tube-side water coefficient, which is very high.
Itcanbeshownbyusingtheelectricalanalogyandneglectingtheeffectsof
fouling that [9]
h
t t t t i
m ¼ o(cid:3)ðo(cid:3) iÞ h h
iþ o
where
t tube wall temperature
m¼
t gas- and tube-side fluid temperature
o¼
h tube-side heat transfer coefficient
i¼
h gas-side heat transfer coefficient
o¼
In an economizer, h is typically about 1000Btu=ft2 h F and h is about
i (cid:2) 0
15Btu=ft2 h F.
(cid:2)
Let us assume that water temperature t 250 F and compute the wall
i¼ (cid:2)
temperature t for two gas temperatures, 350 Fand 750 F.
m (cid:2) (cid:2)
1000
t 350 350 250 252 F
m1 ¼ (cid:3)ð (cid:3) Þ1015¼ (cid:2)
1000
t 750 750 250 258 F
m2 ¼ (cid:3)ð (cid:3) Þ1015¼ (cid:2)
Hence for a variation of 400 F in gas temperature, the tube wall temperature
(cid:2)
changes by only 6 F because the gas film heat transfer coefficient is so low
(cid:2)
compared to the water-side coefficient. Even with finned tubes the difference
would be marginal.
We seethatifwe specify a higher stack gastemperaturewhenselecting or
designing an economizer we cannot avoid corrosion concerns if the water
temperature is low or close to the acid dew point. A better way is to increase
the water temperature entering the economizer by raising the deaerator pressure
or by using a heat exchanger to preheat the water.
6.25d
Q:
Using the correlation given below, evaluate the sulfuric acid dew point.
T 203:25 27:6 log P 10:83 logP 1:06 logP 8 2:19
dp ¼ þ H 2 Oþ SO 3 þ ð SO 3 þ Þ
18b
ð Þ
Copyright © 2003 Marcel Dekker, Inc.

The partial pressures are in atmospheres and dew point is in degrees Celsius.
A:
Using the data from Q6.25b [14],
P 0:0031mmHg 4:1 10 6atm logP 5:3872
SO 3 ¼ ¼ (cid:4) (cid:3) SO 3 ¼(cid:3)
P 93:44mmHg 0:1229atm logP 0:9104
H 2 O ¼ ¼ H 2 O ¼(cid:3)
T 203:25 27:6 0:9104 10:83 5:3872 1:06 2:6128 2:19
dp ¼ (cid:3) (cid:4) (cid:3) (cid:4) þ (cid:4)ð Þ
128:4 C, or 263 F
(cid:2) (cid:2)
¼
which agrees with the other correlation. However, it should be mentioned that
these calculations have some uncertainty, and experience should be taken as the
guide.
6.26a
Q:
How do you convert pollutants such as NOx and CO from gas turbine exhaust
gases from mass units such as lb=h to ppm?
A:
With strict emission regulations, plant engineers and consultants often find it
necessarytorelatemassandvolumetricunitsofpollutantssuchasNOxandCO.
In gas turbine cogeneration and combined cycle plants, in addition to the
pollutants from the gas turbine itself, one has to consider the contributions
from duct burners or auxiliary burners that are added to increase the steam
generation from the HRSGs (heat recovery steam generators).
One can easily obtain the total lb=h of NOx or CO in the exhaust gas.
However, regulations refer to NOx and CO in ppmvd (parts per million volume
dry) referred to 15% oxygen in the gas. The conversion can be done as follows.
If w lb=h is the flow rate of NOx (usually reported as NO ) in a turbine
2
exhaustflowof W lb=h, the following expression givesNOx involumetric units
on dry basis [9].
w=46 = W=MW
V 100 ð Þ ð Þ 19
¼ (cid:4) 100 %H O ð Þ
(cid:3) 2
where
%H O volume of water vapor
2 ¼
MW molecular weight of the exhaust gases
¼
Copyright © 2003 Marcel Dekker, Inc.

ThevalueofV obtainedwithEq.(19)mustbeconvertedto15%oxygenondry
basis to give ppmvd of NOx:
V 21 15 106
V (cid:4)ð (cid:3) Þ(cid:4) V F 20
n ¼ 21 100 %O = 100 %H O ¼ (cid:4) ð Þ
(cid:3) (cid:4) 2 ð (cid:3) 2 Þ
where%O istheoxygenpresentinthewetexhaustgasesandfactorF converts
2
V to15%oxygenbasis,whichistheusualbasisofreportingemissions.Similarly,
CO emission in ppmvd can be obtained as
V 1:642 V (for the samewlb=hrate
c ¼ (cid:4) n Þ
because the ratio of the molecular weights of NO and CO is 1.642.
2
Example
Determine the NOx and CO concentrations in ppmvd, 15% oxygen dry basis if
25lb=hofNOxand15lb=hofCOarepresentin550,000lb=hofturbineexhaust
gas that has the following analysis by volumepercent (usually argonis added to
the nitrogen content):
CO 3:5; H O 10; N 75; O 11:5
2 ¼ 2 ¼ 2 ¼ 2 ¼
Solution. First,
MW 3:5 44 10 18 75 28 11:5 32 =100 28
¼ð (cid:4) þ (cid:4) þ (cid:4) þ (cid:4) Þ ¼
Let us compute NOx on dry basis in the exhaust.
100 25=46
V (cid:4)ð Þ 0:00003074
¼ 550,000=28 = 100 10 ¼
ð Þ ð (cid:3) Þ
106 21 15
F (cid:4)ð (cid:3) Þ 0:73 106
¼21 100= 100 10 11:5¼ (cid:4)
(cid:3)½ ð (cid:3) Þ(cid:5)(cid:4)
Hence
V 0:00003074 0:73 106 22:4ppmvd
n ¼ (cid:4) (cid:4) ¼
Similarly, V (15=25) 1.642 22.4 22.0ppmvd.
c¼ (cid:4) (cid:4) ¼
6.26b
Q:
How can the emissions due to NOx and CO in fired boilers be converted from
ppm to lb=MM Btu or vice versa [10]?
A:
Packagedsteam generators firing gas or oil must limit emissionsof pollutants in
order to meet state and federal regulations. Criteria on emissions of common
Copyright © 2003 Marcel Dekker, Inc.

pollutantssuchascarbonmonoxide(CO)andoxidesofnitrogen(NOx)areoften
specified in parts per million volume dry (ppmvd) at 3% oxygen. On the other
hand, burner and boiler suppliers often cite or guarantee values in pounds per
million Btu fired.
Table6.10demonstratesasimplemethodforcalculatingtheconversion.It
should be noted that excess air has little effect on the conversion factor.
Table6.10showstheresultsofcombustioncalculationsfornaturalgasand
No. 2 oil at various excess air levels. The table shows the flue gas analysis,
molecularweight,andamountoffluegasproducedpermillionBtufiredonhigher
heatingvalue(HHV)basis.Usingthese,wewillarriveattherelationshipbetween
ppmvd values of NOx orCO and thecorrespondingvalues inlb=MMBtu fired.
Calculations for Natural Gas
From simple mass-to-mole conversions we have
N MW 21 3
V 106 Y (cid:3) 21
n ¼ (cid:4) (cid:4)46(cid:4)W (cid:4)21 O Y ð Þ
gm (cid:3) 2(cid:4)
where
MW molecular weight of wet flue gases
¼
N pounds of NOx per million Btu fired
¼
O vol% oxygen in wet flue gases
2¼
V parts per million volume dry NOx
n¼
W flue gas produced per MM Btu fired, lb
gm ¼
Y 100=(1007%H O), where H O is the volume of water vapor in
¼ 2 2
wet flue gases
TABLE6.10 Resultsof Combustion Calculations (Analysis invol%)
Percentexcessair
0 10 20 30 0 10 20 30
Component Natural gasa No.2Oilb
CO 9.47 8.68 8.02 7.45 13.49 12.33 11.35 10.51
2
H O 19.91 18.38 17.08 15.96 12.88 11.90 11.07 10.36
2
N 70.62 71.22 71.73 72.16 73.63 74.02 74.34 74.62
2
O 0 1.72 3.18 4.43 0 1.76 3.24 4.50
2
MW 27.52 27.62 27.68 27.77 28.87 28.85 28.84 28.82
W 768 841 914 966 790 864 938 1011
gm
aNaturalgasanalysisassumed:C 97,C 2,C 1vol%.(HHVandLLV 23,759and
1¼ 2¼ 3¼ ¼
21,462Btu=lb,respectively.)
bNo.2oilanalysisassumed:C 87.5%,H 12.5%; API 32.(HHVandLLV 19,727and
¼ 2¼ (cid:2) ¼ ¼
18,512Btu=lb,respectively.)
Copyright © 2003 Marcel Dekker, Inc.

From Table 6.10; for zero excess air:
W 106=23,789 18:3 769
gm ¼ð Þ(cid:4) ¼
Y 100= 100 19:91 1:248
¼ ð (cid:3) Þ¼
MW 27:53; O 0
¼ 2 ¼
Substituting these into Eq. (21) we have
18
V 106 1:248 N 27:52 832N
n ¼ (cid:4) (cid:4) (cid:4) (cid:4)46 769 21¼
(cid:4) (cid:4)
Similarly,toobtainppmvdCO(partspermillionvolumedryCO),onewoulduse
28insteadof46inthedenominator.ThusthemolecularweightofNOxwouldbe
46 and the calculated molecular weight of CO would be 28.
V 1367CO
e ¼
whereCOisthepoundsofCOperMMBtufiredonhigherheatingvalue(HHV)
basis.
Now repeat the calculations for 30% excess air:
100
W 986:6; Y 1:189
gm ¼ ¼ 100 15:96¼
(cid:3)
MW 27:77; O 4:43
¼ 2 ¼
N 27:77
V 106 1:189
n ¼ (cid:4) (cid:4)46(cid:4)986:6
18
832N
(cid:4)21 4:43 1:189 ¼
(cid:3)ð (cid:4) Þ
Thus,independentofexcessair,weobtain832astheconversionfactorforNOx
and 1367 for CO.
Similarly, for No. 2 oil and using values from Table 6.10,
V 783N and V 1286CO
n ¼ c ¼
Example
If a natural gas burner generates 0.1lb of NOx per MM Btu fired, then the
equivalent would equal 832 0.1 83ppmvd.
(cid:4) ¼
6.26c
Q:
How can the emissions of unburned hydrocarbons (UHCs) be converted from
lb=MM Btu to ppmv basis?
Copyright © 2003 Marcel Dekker, Inc.

A:
Refer to Table 6.10, which shows the results of combustion calculations for oil
and gaseous fuels at various excess air levels. We can obtain UHC emissions on
ppmv basis if lb=MM Btu values are known.
Let us assume that U is the emission of UHC (treated as methane) in
lb=MM Btu in flue gases of natural gas at 20% excess air. Using Eq. (21) for
converting from mass tovolume units,
106 Y MW 21 3
V (cid:4) (cid:4) (cid:4)ð (cid:3) Þ
u ¼16 W 21 O Y
(cid:4) gm(cid:4)ð (cid:3) 2(cid:4) Þ
MW 16 for UHC and 27.68 for flue gases, water vapor in flue gases 17.08
¼ ¼
vol% at 20% excess air for natural gas, W 914lb=MM Btu, and % oxygen
gm¼
wet 3.18. Hence,
¼
100
V U 106
u ¼ (cid:4) (cid:4)82:92
27:68 18
(cid:4) 2394U ppmvd
(cid:4)16 914 21 3:18 100=82:92 ¼
(cid:4) (cid:4)ð (cid:3) (cid:4) Þ
Forexcessairat10%excessair,MW 27.62forfluegases,watervapor 18.38
¼ ¼
vol%, oxygen wet 1.72 vol% W 841.
¼ gm¼
100 27:62 18
V U 106 (cid:4)
u ¼ (cid:4) (cid:4)82:62(cid:4)16 841 21 1:72 100=82:62
(cid:4) (cid:4)ð (cid:3) (cid:4) Þ
2365U ppmvd
¼
Hence, if the UHC value is 0.1lb=MM Btu for natural gas, it is equivalent to
about 237ppmv.
For No. 2 oil at 20% excess air, W 938, oxygen 3.24, MW flue
gm¼ ¼
gases 28.84, water vapor 11.07 vol%.
¼ ¼
100 28:84 18
V U 106 (cid:4)
u ¼ (cid:4) (cid:4)88:93(cid:4)16 938 21 3:24 100=88:93
(cid:4) (cid:4)ð (cid:3) (cid:4) Þ
2240U ppmvd
¼
6.26d
Q:
Convert SOx values from lb=MM Btu to ppmvd.
Copyright © 2003 Marcel Dekker, Inc.

A:
Each pound of sulfur in fuel converts to 2lb of SO . Using natural gas at 20%
2
excess air, S lb=MM Btu of SO is equivalent to
2
100 27:68 18
V S 106 (cid:4)
s ¼ (cid:4) (cid:4)82:92(cid:4)64 914 21 3:18 100=82:92
(cid:4) (cid:4)ð (cid:3) (cid:4) Þ
598S ppmvd
¼
0.1lb=MM Btu of SOx is equivalent to 60ppmv. [We are simply using Eq. (21)
and substituting for MW and Y.]
Similarly, for No. 2 oil at 20% excess air;
100 28:84 18
V S 106 (cid:4) 534S ppmvd
s ¼ (cid:4) (cid:4)88:93(cid:4)64 21 3:24 100=82:92 ¼
(cid:4)ð (cid:3) (cid:4) Þ
6.26e
Q:
A gas turbine HRSG has the following data:
Exhaust gas flow 500,000lb=h at 900 F
(cid:2)
¼
Gas analysis vol%; CO 3;H O 7;N 75;O 15. The exhaust
2 ¼ 2 ¼ 2 ¼ 2 ¼
gas has 9lb=h of NOx and CO. The HRSG is fired to 1500 F using natural gas
(cid:2)
consisting of vol% methane 97, ethane 2, propane 1. Fuel input 90MM
¼ ¼ ¼ ¼
LHV. HHV of fuel 23,790Btu=lb, and LHV 21,439Btu=lb. The burner
¼ ¼
contributes 0.05lb=MM Btu of NOx and CO. Also see what happens when the
burner contributes 0.1lb=MM Btu of these pollutants. Flue gas analysis after
combustion vol% CO 4:42, H O 9:78, N 73:91, O 11:86, and flue
2 ¼ 2 ¼ 2 ¼ 2 ¼
gasflow 504,198lb=h.ComputetheNOxandCOlevelsinppmvdcorrectedto
¼
15% oxygen before and after the burner.
A:
WehavetoconvertthemassflowofNOxandCOtovolumetricunitsandcorrect
for 15% oxygen dry basis.
At the burner inlet, using Eqs. (19) and (20),
9 100 28:38 21 15
ppmvd NOx 106 (cid:3) 14:7
¼46(cid:4) 93 (cid:4)500,000(cid:4) (cid:4)21 15 100=93¼
(cid:3) (cid:4)
Inthisexample,themolecularweightsofNOx 46,fluegas 28.38.Themass
¼ ¼
of CO remains the same, so ppmvd CO (46=28) 14.7 24.2.
¼ (cid:4) ¼
At the burner exit; the mass of NOx in the exhaust gases after combus-
tion is
23,790
9 90 0:05 14lb=h
þ (cid:4)21,439(cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

BecausetheburnerheatinputisonLHVbasisandemissionsareonHHVbasis,
we correct the values using the above expression.
14 100 28:2
ppmvd NOx 106
¼46(cid:4)90:22(cid:4)504,198(cid:4)
21 15
(cid:3) 14:4
(cid:4)21 11:86 100=90:22¼
(cid:3) (cid:4)
ppmvd CO 46=28 14 23:7
¼ð Þ(cid:4) ¼
With 0.1lb=MM Btu emissions from the burner, NOx ppmvd 19.5 and CO
¼
ppmvd 32.1Thusboththeburnercontributionandtheinitialpollutantlevelsin
¼
theturbineexhaustgasesaffecttheppmvvaluesaftercombustion.ppmvdvalues
after the burner can be lower or higher than the inlet ppmvd values, though in
terms of mass flow they will always be higher.
6.26f
Q:
Steam generator emissions are usually referred to 3% oxygen dry basis, and gas
turbine or HRSG emissions are referred to 15% oxygen dry basis. However, in
operation,differentexcessairratesareusedthatgeneratefluegaseswithdifferent
oxygen levels. What is the procedure for converting from actual to 3% oxygen
basis?
A:
21 3
ppm (@ 3% dry) ppm (actual) (cid:3)
¼ (cid:4)21 O actual
(cid:3) 2 ð Þ
Ifdryoxygeninfluegasesis1.7%and12ppmofapollutantismeasured,thenat
3% oxygen,
21 3
Emission 12 (cid:3) 11:2ppm
¼ (cid:4)21 1:7¼
(cid:3)
6.27a
Q:
Ingasturbinecogenerationandcombinedcycleprojects,theheatrecoverysteam
generator may be fired with auxiliary fuel in order to generate additional steam.
Oneofthefrequentlyaskedquestionsconcernstheconsumptionofoxygeninthe
exhaust gas versus fuel quantity fired. Would there be sufficient oxygen in the
exhaust to raise the exhaust gas to the desired temperature?
Copyright © 2003 Marcel Dekker, Inc.

A:
Gasturbineexhaustgasestypicallycontain14–16%oxygenbyvolumecompared
to 21% in air. Hence generally there is no need for additional oxygen to fire
auxiliaryfuelsuchasgasoroilorevencoalwhileraisingitstemperature.(Ifthe
gas turbine is injected with large amounts of steam, the oxygen content will be
lower,andweshouldrefer theanalysistoaburnersupplier.)Also,iftheamount
of fuel fired is very large, then we can run out of oxygen in the gas stream.
Supplementary firing or auxiliary firing can double or even quadruple the steam
generationintheboilercomparedtoitsunfiredmodeofoperation[1].Theenergy
QinBtu=hrequiredtoraiseW lb=hofexhaustgasesfromatemperatureoft to
g 1
t is given by
2
Q W h h
¼ g(cid:4)ð 2(cid:3) 1Þ
where
h ;h enthalpy of the gas at t and t , respectively
1 2¼ 1 2
Thefuelquantityinlb=hisW inQ=LHV,whereLHVisthelowerheating
f
value of the fuel in Btu=lb.
If 0% volume of oxygen is available in the exhaust gases, the equivalent
amount of air W in the exhaust is [9]
a
100 W O 32
W (cid:4) g(cid:4) (cid:4)
a ¼ 23 100 29:5
(cid:4) (cid:4)
In this equation we are merely converting the moles of oxygen from volume to
weightbasis.Amolecularweightof29.5isusedfortheexhaustgases,and32for
oxygen. The factor 100=23 converts the oxygen to air.
W 0:0471 W O 22
a ¼ (cid:4) g(cid:4) ð Þ
Now let us relate the air required for combustion with fuel fired. From Q5.03–
Q.5.05weknowthateachMMBtuoffuelfiredonHHVbasisrequiresaconstant
amountAofair.Ais745foroiland730fornaturalgas;thus,106=HHVlboffuel
requires A lb of air. Hence Q=LHV lb of fuel requires
Q HHV
A lb air
LHV(cid:4) (cid:4) 106
and this equals W from (22).
a
Q HHV
A W 0:0471W O 23
LHV(cid:4) (cid:4) 106 ¼ a ¼ g(cid:4) ð Þ
or
LHV
Q 0:0471 W O 106 24
¼ (cid:4) g(cid:4) (cid:4) (cid:4)A HHV ð Þ
(cid:4)
Copyright © 2003 Marcel Dekker, Inc.

Now for natural gas and fuel oils, it can be shown that LHV= A HHV
ð (cid:4) Þ¼
0:00124. Substituting into Eq. (24), we get
Q 58:4 W O 25
¼ (cid:4) g(cid:4) ð Þ
This is avery important equation, because it relates the energy input by the fuel
(on LHV basis) with oxygen consumed.
Example
It is desired to raise the temperature of 150,000lb=h of turbine exhaust gases
from950 Fto1575 Finordertodoubletheoutputofthewasteheatboiler.Ifthe
(cid:2) (cid:2)
exhaust gases contain 15 vol% of oxygen, and the fuel input is 29MM Btu=h
(LHV basis), determine the oxygen consumed.
Solution. From Eq. (24),
29 106
O (cid:4) 3:32%
¼150,000 58:4¼
(cid:4)
Hence if the incoming gases had 15 vol% of oxygen, even after the firing of
29MM Btu=h wewould have1573.32 11.68% oxygenin the exhaustgases.
¼
A more accurate method would be to use a computer program [9], but the
above equation clearly tells us if there is likely to be a shortage of oxygen.
6.27b
Q:
150,000lb=h of turbine exhaust gases at 900 F having a gas analysis (vol%) of
(cid:2)
CO 3;H O 7;N 75 and O 15 enters a duct burner, and 35MM
2 ¼ 2 ¼ 2 ¼ 2 ¼
Btu=h(LHV)ofnaturalgasisfired.Determinetheexhaustgasanalysisafter the
burner. Use 100% methane as fuel gas analysis for illustrative purposes.
A:
From Table 6.3, the LHV 21,520Btu=lb. Hence fuel fired 35 106=
¼ ¼ (cid:4)
21,520 1626lb=h.
¼
From combustion basics,
CH 2O CO 2H O
4þ 2 ! 2þ 2
So16lbofmethanerequires64lbofoxygenandyields44lbofCO and36lbof
2
water vapor, using molecular weights of 16 for methane, 32 for oxygen, 44 for
carbon dioxide, and 18 for water vapor. Hence 1626lb=h of methane will
consume
1626 64=16 6504lb=h of oxygen
(cid:4)ð Þ¼
Copyright © 2003 Marcel Dekker, Inc.

Also, it will increase CO by
2
1626 44=16 4471lb=h
(cid:4)ð Þ¼
H O will increase by
2
1626 36=16 3659lb=h
(cid:4)ð Þ¼
Convert the volume percent in incoming exhaust gases to weight percent
basis as follows. The molecular weight of incoming gases is 0:03 44
(cid:4) þ
0:07 18 0:75 28 0:15 32 28:38
(cid:4) þ (cid:4) þ (cid:4) ¼
Fraction by weight of CO 0:03 44=28:38 0:0465
2 ¼ (cid:4) ¼
H O 0:07 18=28:38 0:0444
2 ¼ (cid:4) ¼
N 75 28=28:38 0:74
2 ¼ (cid:4) ¼
O 0:15 32=28:38 0:1691
2 ¼ (cid:4) ¼
The amounts of these gases in incoming exhaust gas in lb=h:
CO 150,000 0:0465 6975lb=h
2 ¼ (cid:4) ¼
H O 150,000 0:0444 6660lb=h
2 ¼ (cid:4) ¼
N 150,000 0:74 111,000lb=h
2 ¼ (cid:4) ¼
O 150,000 0:1691 25,365lb=h
2 ¼ (cid:4) ¼
The final products of combustion will have
CO 6975 4471 11,446lb=h
2 ¼ þ ¼
H O 6660 3659 10,319lb=h
2 ¼ þ ¼
N 111,000
2 ¼
O 25,365 6504 18,861lb=h
2 ¼ (cid:3) ¼
Total exhaust gas flow 11,446 10,319 111,000 18,861
¼ þ þ þ
151,626lb=h
¼
which matches the sum of exhaust gas flow and the fuel gas fired.
To convert the final exhaust gas to vol% analysis, we have to obtain the
number of moles of each constituent.
Moles of CO 11,446=44 260:1
2 ¼ ¼
H O 10,319=18 573:2
2 ¼ ¼
N 111,000=28 3964:3
2 ¼ ¼
O 18,861=32 589:4
2 ¼ ¼
Total moles 5387
¼
Copyright © 2003 Marcel Dekker, Inc.

Hence
CO 260:1=5387 0:0483,or4:83%by volume
2 ¼ ¼
Similarly,
H O 573:2=5387 0:1064,or10:64vol%
2 ¼ ¼
N 3964:2=5387 0:7359;or 73:59vol%
2 ¼ ¼
O 589:4=5387 0:1094,or10:94vol%
2 ¼ ¼
Using Eq. (25), we see that nearly 4% oxygen has been consumed
[(35 106)(58.4=150,000) 4%] or final oxygen 1574 11%, which
(cid:4) ¼ ¼ ¼
agrees with the detailed calculations.
When possible, detailed combustion calculations should be done because
theyalsorevealthevolumepercentofwatervapor,whichhasincreasedfrom7%
to10.64%.Thiswouldnaturallyincreasethegasspecificheatoritsenthalpyand
affect the heat transfer calculations.
Table 6.11 shows the exhaust gas analysis at various firing temperatures.
6.27c
Q:
Determine the final exhaust gas temperature after combustion in the example in
Q6.27b.
A:
To arrive at the final gas temperature, the enthalpy of the exhaust gases must be
obtained. A simplistic specific heat assumption can also give an idea of the
temperature but will not be accurate.
TABLE6.11 Effect of FiringTemperatureon ExhaustGas Analysis
Firing temperature, F
(cid:2)
1400 1800 2200 2600 3000
Burnerduty, MMBtu=h 22.5 41.83 62.98 86.54 111.1
Totalgas flow,lb=h 151,037 151,947 152,935 154,035 155,174
H O, vol% 9.33 11.29 13.39 15.67 18.00
2
CO ,vol% 4.19 5.18 6.26 7.42 8.6
2
O , vol% 12.38 10.18 7.83 5.27 2.67
2
150,000lb=h of exhaust gases at 900 F. Exhaust gas analysis (vol%): CO 3, H O 7,
(cid:2) 2¼ 2 ¼
N 75,O 15.Naturalgas:C 97vol%,C 3vol%.
2¼ 2¼ 1¼ 2¼
Copyright © 2003 Marcel Dekker, Inc.

Using, say, 0.3Btu=lb F for the averagegas specific heat for the tempera-
(cid:2)
ture range in consideration, the increase in gas temperature is
35 106= 150,000 0:3 777 F
(cid:2)
(cid:4) ð (cid:4) Þ¼
or
Final gas temperature 900 777 1677 F
(cid:2)
¼ þ ¼
However, let us use gas enthalpy calculations, which are more accurate. Figure
6.3showsthegasenthalpyfortheturbineexhaustgasatvarioustemperatures.(A
program was used to compute these values based on the enthalpy of individual
constituents.) Enthalpy of exhaust gas at 900 F 220Btu=lb.
(cid:2)
¼
From an energy balance across the burner;
150,000 220 35 106 151,626 h
(cid:4) þ (cid:4) ¼ (cid:4) g
whereh enthalpyoffinalproductsofcombustion.h 448.5Btu=lb.Fromthe
g¼ g¼
chart, the gas temperature 1660 F.
(cid:2)
¼
A computer program probably gives more accurate results, because it can
computethegastemperatureandenthalpyforanygasanalysisanditerateforthe
actual enthalpy, whereas a chart can be developed only for a given exhaust gas
analysis and a maximum firing temperature.
FIGURE 6.3 Enthalpyof turbineexhaust gasasafunction oftemperature.
Copyright © 2003 Marcel Dekker, Inc.

6.28
Q:
How can the fuel consumption for power plant equipment such as gas turbines
and diesel engines be determined if the heat rates are known?
A:
Theheatrate(HR)ofgasturbinesorenginesinBtu=kWhrefersindirectlytothe
efficiency.
3413
Efficiency
¼ HR
where 3413 is the conversion factor from Btu=h to kW. One has to be careful
about the basis for the heat rate, whether it is on HHV or LHV basis. The
efficiency will be on the same basis.
Example
If the heat rate for a gas turbine is 9000Btu=kWh on LHV basis and the higher
and lower heating values of the fuel are 20,000 and 22,000Btu=lb, respectively,
then
3413
Efficiency on LHV basis 0:379;or37:9%
¼9000¼
To convert this efficiency to HHV basis, simply multiply it by the ratio of the
heating values:
20,000
Efficiency on HHV basis 37:9 34:45%
¼ (cid:4)22,000¼
NOMENCLATURE
A Theoretical amount of air for combustion per MM Btu fired, lb
C;CO;CO Carbon, carbon monoxide, and carbon dioxide
2
C Ash concentration in flue gas, grains=cu ft
a
C Specific heat, Btu=lb F
p (cid:2)
e Emission rate of sulfur dioxide, lb=MM Btu
E Excess air, %
EA Excess air factor
HHV Higher heating value, Btu=lb or Btu=scf
HR Heat rate, Btu=kWh
h;h Inside and outside heat transfer coefficients, Btu=ft2 h F
i o (cid:2)
K Constant used in Eq. (7)
K ;K Constants used in Eq. (10a) and (10c)
1 2
Copyright © 2003 Marcel Dekker, Inc.

L –L Losses in steam generator, %
1 5
LHV Lower heating value, Btu=lb or Btu=scf
MW Molecular weight
P ;P ,P Partial pressures of carbon dioxide and water vapor, atm
c w HO
2
P Partial pressure of sulfur trioxide, atm
SO
3
P ;P Actual and standard pressures, psia
a s
DP Differential pressure, psi
q Heat loss, Btu=ft2 h
Q Energy, Btu=h or kW
s Specific gravity
S Sulfur in fuel
t ;t Temperatures of air and gas, F
a g (cid:2)
t Melting point of ash, C; tube wall temperature, C
m (cid:2) (cid:2)
T Acid dew point temperature, K
dp
T ;T Standard and actual temperatures, R
s a (cid:2)
V ;V Standard and actual volumes, cu ft
s a
V ;V CO and NOx ppmvd
c n
w Weight of air, lb=lb fuel; subscript da stands for dry air; wa, wet
air; wg, wet gas; dg, dry gas
W Moisture, lb=h
W ;W ;W Flow rates of air, gas, and fuel, lb=h
a g f
Z Efficiency; subscripts HHVand LHV denote the basis
r Density, lb=cu ft; subscript g stands for gas, f for fuel
REFERENCES
1. VGanapathy.AppliedHeatTransfer.Tulsa,OK:PennWellBooks,1982,pp14–24.
2. North American Combustion Handbook. 2nd ed. Cleveland, OH: North American
Mfg.Co.,1978,pp9–40.
3. Babcock and Wilcox. Steam: Its Generation and Use. 38th ed. New York, 1978,
p6–2.
4. VGanapathy,Usecharttoestimatefurnaceparameters.HydrocarbonProcessing,Feb
1982,p106.
5. VGanapathy. Figure particulate emission rate quickly. Chemical Engineering, July
26,1982,p82.
6. VGanapathy.Nomogramestimatesmeltingpointofash.PowerEngineering,March
1978,p61.
7. ASME.PowerTestCode.Performancetestcodeforsteamgeneratingunits,PTC4.1.
NewYork:ASME,1974.
8. VGanapathy.Estimatecombustiongasdewpoint.OilandGasJournal,April1978,
p105.
9. VGanapathy.WasteHeatBoilerDeskbook.Atlanta,GA:FairmontPress,1991.
Copyright © 2003 Marcel Dekker, Inc.

10. VGanapathy.Convertingppmtolb=MMBtu;aneasymethod.PowerEngineering,
April1992,p32.
11. KYHsiung.Predictingdewpointsofacidgases.ChemicalEngineering,Feb9,1981,
p127.
12. C Baukal Jr. The John Zink Combustion Handbook. Boca Raton, FL: CRC Press,
2001.
13. Babcock and Wilcox, Steam, its generation and use, 40th ed. The Babcock and
WilcoxCompany,Barberton,Ohio,1992.
14. AGOkkes.Getaciddewpointoffluegas.HydrocarbonProcessing,July1987.
Copyright © 2003 Marcel Dekker, Inc.

7
Fluid Flow, Valve Sizing,
and Pressure Drop Calculations
7.01 Sizing flow meters; discharge coefficients for orifices, venturis, and
nozzles; permanent pressure drop across flow meters; correcting steam
flow readings for different operating conditions
7.02 Sizing orifices for water flow measurement
7.03 Sizing orifices for steam flow measurement
7.04 Significanceofpermanentpressuredropinflowmeters;costofpermanent
pressure drop across flow meters
7.05 Converting pitot tube readings to air velocity, flow in ducts
7.06 Sizing safety valves for boilers; ASME Code procedure
7.07 Relieving capacities for steam service; orifice designations for safety
valves; relating set and accumulated inlet pressures
7.08 Selectingsafetyvalvesforboilersuperheater;actualandrequiredrelieving
capacities
7.09 Relieving capacities of a given safety valve on different gases
7.10 Relieving capacity of safety relief valve for liquid service
7.11 Determining relieving capacity of a given safety valve on air and steam
service
7.12 Sizing control valves; valve coefficient C
v
7.13 CalculatingC forsteamservice;saturatedandsuperheatedsteam;critical
v
and noncritical flow
7.14 Calculating C for liquid service
v
Copyright © 2003 Marcel Dekker, Inc.

7.15 On cavitation: recovery factors
7.16 Selecting valves for laminar flow
7.17 Calculating pressure loss in water line; determining friction factor for
turbulent flow; equivalent length of piping; viscosity of water
7.18 Pressure loss in boiler superheater; estimating friction factor in smooth
tubes; pressure drop in smooth tubing; Reynolds number for gases
7.19 Determiningpressuredropunderlaminarconditions;pressuredropinfuel
oil lines; effect of temperature on specific volume, viscosity of oils
7.20 Pressuredropforviscousliquids;frictionfactorunderturbulentconditions
7.21 Calculatingflowingpmandinlb=hforfueloils;expansionfactorsforfuel
oils at different temperatures
7.22 Pressure loss in natural gas lines using Spitzglass formula
7.23 Calculating pressure drop of flue gas and air in ducts; friction factors;
equivalent diameter for rectangular ducts; Reynolds number estimation
7.24 DeterminingReynoldsnumberforsuperheatedsteamintubes;viscosityof
steam; Reynolds number for air flowing over tube bundles.
7.25 Determining flow in parallel passes of a superheater
7.26 Equivalentlengthofpipingsystem;equivalentlengthofvalvesandfittings
7.27 Pressuredropofair andfluegases over plaintube bundles;frictionfactor
for in-line and staggered arrangements
7.28 Pressure drop of air and flue gases over finned tube bundles
7.29 Factors influencing boiler circulation
7.30 Purpose of determining circulation ratio
7.31 Determining circulation ratio in water tube boilers
7.32 Determining circulation ratio in fire tube boilers
7.33 Determining steam flow in blowoff lines
7.34 Sizing boiler blowdown lines
7.35 Stack height and friction losses
7.36 Flow instability in evaporators
7.01a
Q:
How are flow meters sized?
A:
The basic equation for pressure differential in head meters (venturis, nozzles,
orifices) is [1]
phr
W 359YC d2 1a
¼ d o 1 ffiffiffiffiffiffib4 ð Þ
(cid:3)
qffiffiffiffiffiffiffiffiffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

where
W flowof the fluid, lb=h
¼
Y expansionfactor,whichallowsforchangesindensityofcompressible
¼
fluids(forliquidsY 1,andformostgasesitvariesfrom0.92to1.0)
¼
C a coefficient of charge
d¼
d orifice diameter, in.
o¼
r density of fluid, lb=cu ft
¼
b ratio of orifice to pipe inner diameter d =d
¼ ¼ o i
h differential pressure, in. WC
¼
C maybetakenas0.61fororificesand0.95–0.98forventurisandnozzles.Itisa
d
complicated function of Reynolds number and orifice size. The permanent
pressure drop, Dp, across a flow meter is important, because it means loss in
power or additional consumption of energy. It is the highest for orifices [2]:
DP h 1 b2 1b
¼ ð (cid:3) Þ ð Þ
For nozzles,
1 b2
DP h (cid:3) 1c
¼ 1 b2 ð Þ
þ
and for venturis it depends on the angle of divergence but varies from 10% to
15% of h. Q7.04 discusses the significance of permanent pressure drop and the
cost associated with it.
7.01b
Q:
The differential pressure across an orifice of a steam flow meter shows 180 in.
WCwhentheupstream conditionsare1600psiaand900 F.Thesteam flowwas
(cid:2)
calibrated at 80,000lb=h under these conditions. Because of different plant load
requirements,thesteamparametersarenow900psiaand800 F.Ifthedifferential
(cid:2)
pressure is 200 in. WC, what is the steam flow?
A:
From Eq. (1a),
h
W rh
/ / v
rffiffiffi
where pffiffiffiffiffiffi
W steam flow, lb=h
¼
v specific volume, cu ft=lb
¼
h differential pressure, in. WC
¼
r density, lb=cu ft
¼
Copyright © 2003 Marcel Dekker, Inc.

From the steam tables (see the Appendix),
n 0:4553cuft=lbat1600psia;900 F
1 ¼ (cid:2)
n 0:7716cuft=lbat900psia;800 F
2 ¼ (cid:2)
h 180, h 200, and W 80,000. We need to find W .
1¼ 2¼ 1¼ 2
80;000 180 0:7716
(cid:4) 1:235
W ¼ 200 0:4553¼
2 rffiffiffiffiffiffiffiffiffi(cid:4)ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Hence W 64,770lb=h.
2¼
7.02
Q:
Determine the orifice size to limit the differential pressure to 100 in. WC when
700lb=sofwater at60 Fflows inapipe of inner diameter 18 in.The densityof
(cid:2)
water is 62.4lb=cu ft.
A:
Equation (1a) is not handy to use when it is required to solve for the orifice
diameter d . Hence, by substituting for b d =d and simplifying, we have
o ¼ o i
prhb2
W 359C Yd2 2
¼ d i p1 b4 ð Þ
ffiffiffiffiffiffi
(cid:3)
This equation is easy to use either when orifice size is needed or when flow
through a given orifice is required. The term b2=p1 b4 is a function of b and
(cid:3)
can be looked up from Table 7.1. Substituting for W 700 3600;
¼ (cid:4)
C 0:61;Y 1;r 62:4, and h 100, we have
d ¼ ¼ ¼ ¼
700 3600 359 0:61 1 182p62:4 100 F b
(cid:4) ¼ (cid:4) (cid:4) (cid:4) (cid:4) (cid:4) ð Þ
or ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
F b 0:45
ð Þ¼
FromTable7.1,byinterpolation,wenotethatb 0.64.Thustheorificediameter
¼
d 0.64 18 11.5in.
o¼ (cid:4) ¼
7.03
Q:
Whatsizeoforificeisneededtopassasaturatedsteamflowof26,480lb=hwhen
theupstreampressureis1000psiaandlinesizeis2.9in.andthedifferentialisnot
to exceed 300in. WC?
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.1 F b Values for Solving
ð Þ
Eq. (2)
b F b b2=p1 b4
ð Þ¼ (cid:3)
0.3 0.09
0.4 0.162
0.5 0.258
0.6 0.39
0.7 0.562
0.8 0.83
A:
Using Eq. (2) and substituting Y 0:95;r 1=v 1=0:4456 2:24lb/cu ft,
¼ ¼ ¼ ¼
and d 2.9, we have
i¼
W 26;480
¼
359 0:61 0:95 2:92 F b p2:24 300
¼ (cid:4) (cid:4) (cid:4) (cid:4) ð Þ(cid:4) (cid:4)
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Hence
F b 0:58
ð Þ¼
From Table 7.1, b 0.71. Hence
¼
d 0:71 2:9 2:03in:
o ¼ (cid:4) ¼
7.04
Q:
What is the significance of a permanent pressure drop across the flow measure-
ment device? 1.3 million scfh of natural gas with a specific gravity of 0.62 at
125psia is metered using an orifice platewith a differential head of 100in. WC.
The line size is 12in. What are the operating costs involved? Assume that
electricity costs 20mills=kWh.
A:
The first step is to size the orifice. Use a molecular weight of 0.62 29 18 to
(cid:4) ¼
compute the density. (The molecular weight of any gas specific gravity 29.)
¼ (cid:4)
From Q5.03
125
r 18 492 0:39lb=cuft
¼ (cid:4) (cid:4)359 520 15¼
(cid:4) (cid:4)
Copyright © 2003 Marcel Dekker, Inc.

(Atemperatureof60 Fwasassumed.)Thedensityatstandardconditionsof60 F,
(cid:2) (cid:2)
15psia, is
492
r 18 0:047lb=cuft
¼ (cid:4)359 520¼
(cid:4)
Hence mass flow is
W 1:3 106 0:047
¼ (cid:4) (cid:4)
359 0:61 122 p0:39 100 F b
¼ (cid:4) (cid:4) (cid:4) (cid:4) (cid:4) ð Þ
F b 0:31
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ð Þ¼
From Table 7.1, b 0:55, so b2 0:3. The permanent pressure drop, from
¼ ¼
Q7.01, is
DP 1 b2 h 1 0:3 100 70in. WC
¼ð (cid:3) Þ ¼ð (cid:3) Þ(cid:4) ¼
The horsepower consumed in developing this head is
DP
HP scfh 460 t 3
¼ (cid:4)ð þ Þ(cid:4)P 107 ð Þ
(cid:4)
It was assumed in the derivation of Eq. (3) that compressor efficiencywas 75%.
Substitution yields
70
HP 1:3 106 520 38
¼ (cid:4) (cid:4) (cid:4)107 125¼
(cid:4)
The annual cost of operation is
38 0:746 8000 0:02 $4535
(cid:4) (cid:4) (cid:4) ¼
(8000 hours of operation was assumed per year; 0.746 is the factor converting
horsepower to kilowatts.)
7.05
Q:
Often, pitottubesareusedtomeasureair velocitiesinducts inorder tocompute
the air flow. A pitot tube in a duct handling air at 200 F shows a differential of
(cid:2)
0.4in.WC.Iftheductcrosssectionis4ft2,estimatetheairvelocityandtheflow
rate.
A:
It can be shown [3] by substituting r 40= 460 t that for a pitot,
¼ ð þ Þ
V 2:85 h 460 t 4
¼ (cid:4) (cid:4)ð þ Þ ð Þ
pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

where
V velocity, fps
¼
h differential pressure, in. WC
¼
t air or flue gas temperature, F
(cid:2)
¼
V 2:85 p0:4 660 46fps
¼ (cid:4) (cid:4) ¼
The air flow rate inffiffiffiaffifficffiffifffiffimffiffiffiffiffiffiwffiffiffiiffiffill be 46 4 60 11,040acfm. The flow W in
(cid:4) (cid:4) ¼
lb=h 11,040 60 40=660 40,145lb=h. [W acfm 60 density, and
¼ (cid:4) (cid:4) ¼ ¼ (cid:4) (cid:4)
density 40= 460 t .]
¼ ð þ Þ
7.06
Q:
How are safety valves for boilers sized?
A:
The ASME Code for boilers and pressure vessels (Secs. 1 and 8) describes the
procedure for sizing safety or relief valves. For boilers with 500ft2 or more of
heating surface, two or more safety valves must be provided. Boilers with
superheaters must have at least one valve on the superheater. The valves on the
drum must relieve at least 75% of the total boiler capacity. Superheater valves
mustrelieveatleast20%.Boilersthathavereheatersmusthaveatleastonesafety
valve on the reheater outlet capable of handling a minimum of 15% of the flow.
The remainder of the flow must be handled by valves at the reheater inlet.
Ifthereareonlytwovalvesforaboiler,thecapacityofthesmalleronemust
be at least 50% of that of the larger one. The difference between drum pressure
and the lowest valve setting may be at least 5% above drum pressure but never
more than the design pressure and not less than 10psi. The range between the
lowestboilervalvesettingandthehighestsetvalueisnottobegreaterthan10%
ofthesetpressureofthehighestsetvalve.Afterblowing,eachvalveistocloseat
97%of itssetpressure.Thehighestsetboilervalvecannotbesethigherthan3%
over the design pressure.
Theguidelinesabovearesomeofthoseusedinselectingsafetyvalves.For
details the reader should refer to the ASME Code [4].
7.07
Q:
How are the capacities of safety valves for steam service determined?
Copyright © 2003 Marcel Dekker, Inc.

A:
The relieving capacities of safety valves are given by the following expressions.
ASME Code, Sec. 1 uses a 90% rating, whereas Sec. 8 uses a 100% rating [5].
W 45AP K 5a
¼ a sh ð Þ
W 50AP K 5b
¼ a sh ð Þ
where
W lb=h of steam relieved
A ¼ nozzle or throat area of valve, in.2
¼
P accumulated inlet pressure P 1 acc 15, psia (The factor
a¼ ¼ s(cid:4)ð þ Þþ
acc is the fraction of pressure accumulation.)
P set pressure, psig
s¼
K correction factor for superheat (see Fig. 7.1)
sh¼
ThenozzleareasofstandardorificesarespecifiedbylettersDtoTandare
given in Table 7.2. For saturated steam, the degree of superheat is zero, so
K 1. The boiler safety valves are sized for 3% accumulation.
sh ¼
7.08
Q:
Determine the sizes of valves to be used on a boiler that has a superheater. The
parameters are the following.
Total steam generation 650,000lb=h
¼
Design pressure 1500psig
¼
Drum operating pressure 1400psig
¼
Steam outlet temperature 950 F
(cid:2)
¼
Pressure accumulation 3%
¼
Superheater outlet operating pressure 1340psig
¼
A:
The set pressure must be such that the superheater valve opens before the drum
valves. Hence the set pressure can be 1500760740 1400psig (60 is the
¼
pressure drop and 40 is a margin). The inlet pressure P 1:03
a ¼ (cid:4)
1400 15 1457psia. From Fig. 7.1, K 0:79.
þ ¼ sh ¼
W 130;000
A 2:51in:2
¼45K P ¼45 0:79 1457¼
sh a (cid:4) (cid:4)
We used a value of 130,000lb=h, which is 20% of the total boiler capacity. A
K2 orifice is suitable. This relieves (2.545=2.51) 130,000 131,550lb=h.
(cid:4) ¼
The drum valves must relieve 650,0007131,550 518,450lb=h. About
¼
260,000lb=h may be handled by each drum valve if two are used. Let the first
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.1 Correction factorsforsuperheat.
valve be set at 1475psig, or
P 1:03 1475 15 1535psia
a ¼ (cid:4) þ ¼
and the next at P 1575psia.
a ¼
260;000
Area of first valve: A 3:76in:2
¼45 1535¼
(cid:4)
260;000
Area of second valve: A 3:67in:2
¼45 1575¼
(cid:4)
Use two M2 orifices, which each have an area of 3.976in.2 Relieving capacities
are
3:976 3:976
260;000 556;000lb=h
3:76 þ 3:67 (cid:4) ¼
(cid:1) (cid:2)
which exceeds our requirement of 520,000lb=h.
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.2 Orifice
Designation
Type Area (in.2)
D 0.110
E 0.196
F 0.307
G 0.503
H 0.785
J 1.287
K 1.838
K2 2.545
L 2.853
M 3.600
M2 3.976
N 4.340
P 6.380
Q 11.05
R 16.00
7.09a
Q:
How is the relieving capacity of safety valves for gaseous service found?
A:
Theexpressionusedforestimatingtherelievingcapacityforgasesandvapors[6]
is
MW
W CKAP 6
¼ a T ð Þ
rffiffiffiffiffiffiffiffiffi
where
C a function of the ratio k of specific heats of gases (Table 7.3)
¼
K valve discharge coefficient, varies from 0.96 to 0.98
¼
P accumulated inlet pressure P 1 acc 15;psia
a¼ ¼ sð þ Þþ
P set pressure, psig
s¼
MW molecular weight of gas
¼
T absolute temperature, R
(cid:2)
¼
7.09b
Q:
A safety valve is set for 100psig for air service at 100 F and uses a G orifice.
(cid:2)
What is the relieving capacity if it is used on ammonia service at 50 F, pressure
(cid:2)
being the same?
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.3 Constant C for Gas or Vapor Related to Ratio of Specific Heats
(k
¼
C
p
=Cv)
k ConstantC k ConstantC k Constant C
1.00 315 1.26 343 1.52 366
1.02 318 1.28 345 1.54 368
1.04 320 1.30 347 1.56 369
1.06 322 1.32 349 1.58 371
1.08 324 1.34 351 1.60 372
1.10 327 1.36 352 1.62 374
1.12 329 1.38 354 1.64 376
1.14 331 1.40 356 1.66 377
1.16 333 1.42 358 1.68 379
1.18 335 1.44 359 1.70 380
1.20 337 1.46 361 2.00 400
1.22 339 1.48 363 2.20 412
1.24 341 1.50 364
Source:Ref.5.
A:
Assumethatk isnearlythesameforbothairandammonia.Henceforthevalve,
CKAP is a constant. For air, use C 356, K 0.98, A 0.503, MW 29, and
a ¼ ¼ ¼ ¼
T 560.
¼
29
W 356 0:98 0:503 1:1 100 15
a ¼ (cid:4) (cid:4) (cid:4)ð (cid:4) þ Þ 560
rffiffiffiffiffiffiffiffi
4990lb=h
¼
(Anaccvalueof0.10wasusedabove.)FromEq.(6),substitutingMW 17and
¼
T 510 for ammonia, we have
¼
W 29 510
a (cid:4) 1:246
W ¼ 17 560¼
amm rffiffiffiffiffiffi(cid:4)ffiffiffiffiffiffiffiffiffiffiffiffi
Hence
4990
W 4006lb=h
amm ¼1:246¼
7.10a
Q:
How are the relieving capacities for liquids determined?
Copyright © 2003 Marcel Dekker, Inc.

A:
An expression for relieving capacity at 25% accumulation [5] is
q 27:2AK P P 7
¼ s 1(cid:3) b ð Þ
pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
where
P set pressure, psig
1¼
P backpressure, psig
b¼
K p1=s;s being the specific gravity
A s ¼ orifice area, in.2
¼ ffiffiffiffiffiffiffi
q capacity, gpm
¼
7.10b
Q:
Determine the relieving capacity of a relief valve on an economizer if the set
pressureis300psig,backpressureis15psig,ands 1.ThevalvehasaGorifice
(A 0.503in.2). ¼
¼
A:
Using Eq. (7), we have
q 27:2 0:503 1 p300 15
¼ (cid:4) (cid:4) (cid:4) (cid:3)
231gpm
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
¼
231 500 115;000lb=h
¼ (cid:4) ¼
At 10% accumulation, q would be 0.6 231 140gpm and the flow W
(cid:4) ¼ ¼
70,000lb=h (500 is the conversion factor from gpm to lb=h when s 1.)
¼
7.11
Q:
A safety valve bears a rating of 20,017lb=h at a set pressure of 450psig for
saturatedsteam.Ifthesamevalveistobeusedforairatthesamesetpressureand
at 100 F, what is its relieving capacity?
(cid:2)
A:
Foragivenvalve,CKAP isaconstantifthesetpressureisthesame.(SeeQ7.09a
a
for definition of these terms.)
For steam,
20;017 50 KAP
¼ (cid:4) a
Copyright © 2003 Marcel Dekker, Inc.

Hence
20;017
KAP 400:3
a ¼ 50 ¼
For air,
MW
W CKAP
¼ a T
rffiffiffiffiffiffiffiffiffi
C 356, MW 29, and T 560 R for the case of air. Hence,
(cid:2)
¼ ¼ ¼
29
W 356 400:3 32;430lb=h
a ¼ (cid:4) (cid:4) 560¼
rffiffiffiffiffiffiffiffi
Converting to acfm, we have
15
q 32;430 560
¼ (cid:4) (cid:4)0:081 492 465 60
(cid:4) (cid:4) (cid:4)
244acfm
¼
(The density of air was estimated at 465psia and 100 F.)
(cid:2)
7.12
Q:
How is the size of control valves for steam service determined?
A:
Control valves are specified by C or valve coefficients. The manufacturers of
v
controlvalvesprovidethesevalues(seeTable7.4).TheC providedmustexceed
v
theC required.Also,C atseveralpointsofpossibleoperationofthevalvemust
v v
befound,andthebestC characteristicsthatmeettheloadrequirementsmustbe
v
used, because controllability depends on this. For example. a quick-opening
characteristic(seeFig.7.2)isdesiredforon–offservice.Alinearcharacteristicis
desired for general flow control and liquid-level control systems, whereas equal
percentage trim is desired for pressure control or in systems where pressure
varies. The control valve supplier must be contacted for the selection and for
proper actuator sizing.
For the noncritical flow of steam (P <2P ) [7],
1 2
W 1 0:00065 t t
C v (cid:4)½ þ (cid:4)ð (cid:3) sÞ(cid:5) 8
¼ 2:11 DP P ð Þ
(cid:4) (cid:4) t
pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.4 FlowCoefficient C
v
Valve opening(%total travel)
Body Port Total
size (in.) diameter(in.) travel(in.) 10 20 30 40 50 60 70 80 90 100 K and C
m f
3=4 1=4 3=4 0.075 0.115 0.165 0.230 0.321 0.448 0.625 0.870 1.15 1.47 0.70
3=8 3=4 0.120 0.190 0.305 0.450 0.628 0.900 1.24 1.68 2.18 2.69 0.80
1=2 3=4 0.235 0.400 0.600 0.860 1.16 1.65 2.15 2.85 3.40 3.66 0.70
1 1=4 3=4 0.075 0.115 0.165 0.230 0.321 0.448 0.625 0.870 1.20 1.56 0.80
3=8 3=4 0.120 0.190 0.305 0.450 0.630 0.910 1.35 1.97 2.78 3.68 0.70
1=2 3=4 0.235 0.410 0.610 0.900 1.26 1.80 2.50 3.45 4.50 5.36 0.70
3=4 3=4 0.380 0.700 1.10 1.57 2.36 3.40 5.00 6.30 6.67 6.95 0.75
11=2 1=4 3=4 0.075 0.115 0.165 0.230 0.321 0.448 0.625 0.870 1.20 1.56 0.80
3=8 3=4 0.120 0.190 0.305 0.450 0.630 0.910 1.35 1.97 2.78 3.68 0.70
1=2 3=4 0.265 0.420 0.620 0.915 1.31 1.90 2.64 3.65 4.56 6.04 0.80
3=4 3=4 0.380 0.700 1.10 1.65 2.45 3.70 5.30 7.10 8.88 10.2 0.75
1 3=4 0.930 1.39 2.12 3.10 4.44 6.12 8.13 10.1 11.5 12.2 0.75
2 1=4 3=4 0.075 0.115 0.165 0.230 0.321 0.448 0.625 0.870 1.20 1.56 0.80
3=8 3=4 0.120 0.190 0.305 0.450 0.630 0.910 1.35 1.97 2.78 3.68 0.70
1=2 3=4 0.265 0.420 0.620 0.915 1.31 1.90 2.64 3.65 4.89 6.44 0.70
3=4 3=4 0.380 0.700 1.10 1.65 2.45 3.70 5.53 8.00 10.3 12.3 0.70
1 3=4 0.930 1.39 2.12 3.10 4.50 6.45 9.31 12.9 15.7 17.8 0.75
11=2 3=4 0.957 1.45 2.31 3.70 6.05 9.86 15.2 20.2 22.0 22.0 0.79
3 1=4 3=4 0.075 0.115 0.165 0.230 0.321 0.448 0.625 0.870 1.20 1.56 0.80
3=8 3=4 0.120 0.190 0.305 0.450 0.630 0.910 1.35 1.97 2.78 3.68 0.70
1=2 3=4 0.265 0.420 0.620 0.915 1.31 1.90 2.64 3.65 4.89 6.44 0.70
3=4 3=4 0.380 0.700 1.10 1.65 2.45 3.70 5.70 8.66 12.3 14.8 0.65
1 3=4 0.930 1.39 2.12 3.10 4.50 6.70 9.90 13.2 17.9 23.6 0.65
11=2 11=8 1.15 2.29 3.41 4.77 6.44 8.69 12.5 19.2 26.7 32.2 0.74
2 11=8 1.92 3.13 4.83 7.93 12.6 24.6 35.9 40.5 43.4 44.3 0.72
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.2 Typical controlvalvecharacteristics.
For critical flow (P 2P ),
l (cid:9) 2
W 1 0:00065 t t
C v (cid:4)½ þ (cid:4)ð (cid:3) sÞ(cid:5) 9
¼ 1:85 P ð Þ
(cid:4) 1
where
t;t steam temperature and saturation temperature (for saturated steam,
s¼
t t )
¼ s
W steam flow, lb=h
¼
P total pressure (P P ), psia
t¼ 1þ 2
Copyright © 2003 Marcel Dekker, Inc.

7.13a
Q:
Estimate the C required when 60,000lb=h of superheated steam at 900 F,
v (cid:2)
1500psia flows in a pipe. The allowable pressure drop is 30psi.
A:
Since this is a case of noncritical flow, from Eq. (8), substituting t 800 and
¼
t 596, we have
s ¼
60;000 1 0:00065 900 596
C v (cid:4)½ þ (cid:4)ð (cid:3) Þ(cid:5)
¼ 2:11 30 1500 1470
(cid:4) (cid:4)ð þ Þ
114
pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
¼
If the steam is saturated, t t and C 95. We have to choose from the valve
¼ s v ¼
supplier’scatalogavalvethatgivesthisC ormoreat90–95%oftheopeningof
v
thetrim.Thisensuresthatthevalveisoperatingatabout90%ofthetrimopening
and provides room for control.
7.13b
Q:
In a pressure-reducing station, 20,000lb=h of steam at 200psia, 500 F is to be
(cid:2)
reduced to 90psia. Determine C .
v
A:
Use Eq. (9) for critical flow conditions:
20;000 1 0:00065 500 382
C v (cid:4)½ þ (cid:4)ð (cid:3) Þ(cid:5) 58
¼ 1:85 200 ¼
(cid:4)
(382 is the saturation temperature at 200psia.)
7.14
Q:
Determinethevalvecoefficientforliquids.Aliquidwithdensity45lb=cuftflows
attherateof100,000lb=h.Iftheallowablepressuredropis50psi,determineC .
v
A:
The valve coefficient for liquid, C , is given by [8]
v
s
C q 10
v
¼ DP ð Þ
rffiffiffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

where
q flow, gpm
¼
DP pressure drop, psi
¼
s specific gravity
¼
From Q5.01,
W 8qr
¼
100;000
q 278gpm
¼ 8 45 ¼
(cid:4)
45
s 0:72
¼62:4¼
DP 50
¼
Hence
0:72
C 278 34
v
¼ (cid:4) 50 ¼
rffiffiffiffiffiffiffiffiffi
7.15
Q:
How is cavitation caused? How is thevalve sizing done to consider this aspect?
A:
Flashing and cavitation can limit the flow in a control valve for liquid. The
pressure distribution through a valve explains the phenomenon. The pressure at
thevenacontractaisthelowest,andasthefluidflowsitgainspressurebutnever
reachestheupstreampressure.Ifthepressureattheportorvenacontractashould
drop below the vapor pressure corresponding to upstream conditions, bubbles
will form. If the pressure at the exit remains below the vapor pressure, bubbles
remain in the stream and flashing occurs.
Avalve has a certain recovery factor associated with it. If the recovery of
pressure is high enough to raise the outlet pressure above the vapor pressure of
the liquid, the bubbles will collapse or implode, producing cavitation. High-
recovery valves tend to be more subject to cavitation [9]. The formation of
bubblestendstolimittheflowthroughthevalve.Hencethepressuredropusedin
sizing thevalve should allow for this reduced capacity. Allowable pressure drop
DP is used in sizing,
all
DP K P r P 11
all ¼ mð 1(cid:3) c vÞ ð Þ
where
K valve recovery coefficient (depends on valve make)
m¼
P upstream pressure, psia
1¼
r critical pressure ratio (see Fig. 7.3)
c¼
P vapor pressure at inlet liquid temperature, psia
v
¼
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.3 Criticalpressure ratiosforwater.
Full cavitation will occur if the actual DP is greater than DP and if the outlet
all
pressureishigherthanthefluidvaporpressure.IftheactualDPislessthanDP ,
all
theactual DP shouldbeusedfor valvesizing.Toavoidcavitation,selectavalve
with a low recovery factor (a high K factor).
m
7.16
Q:
How are valves selected for laminar flow and viscous liquids?
A:
Calculate the turbulent flow C from Eq. (10) and the laminar C from [10]
v v
mq 2=3
lamC 0:072 12
v
¼ (cid:4) DP ð Þ
(cid:1) (cid:2)
Use the larger C in the valve selection. (m is the liquid viscosity in centipoise.)
v
Copyright © 2003 Marcel Dekker, Inc.

7.17a
Q:
Determine the pressure loss in a 3in. schedule 80 line carrying water at 100 F
(cid:2)
and 2000psia if the total equivalent length is 1000ft. Flow is 38,000lb=h.
A:
The expression for turbulent flow pressure drop of fluids (Reynolds number
>2100) is [11]
v
DP 3:36 10 6 f W2L 13
¼ (cid:4) (cid:3) (cid:4) e d5 ð Þ
i
where
DP pressure loss, psi
¼
f Darcy friction factor
¼
W flow, lb=h
¼
L equivalent length, ft (Q7.26 shows how the equivalent length can be
e¼
computed)
v specific volume of fluid, cu ft=lb
¼
d tube inner diameter, in.
i¼
For water at 100 F and 2000psia, from Table A4 (Appendix 3), v 0.016. In
(cid:2)
¼
industrialheattransferequipmentsuchasboilers,superheaters,economizers,and
airheaters,thefluidflowisgenerallyturbulent,andhenceweneednotcheckfor
Reynoldsnumber.(Q7.24showshowRecanbefound.)However,letusquickly
check Re here:
W
Re 15:2 14
¼ dm ð Þ
i
Referring to Table 7.5, water viscosity, m, at 100 F is 1.645lb=ft h
(cid:2)
38,000
Re 15:2 121;070
¼ (cid:4)2:9 1:645¼
(cid:4)
Theinnerdiameterof2.9forthepipewasobtainedfromTable5.6.Forturbulent
flow and carbon or alloy steels of commercial grade, f may be obtained from
Table 7.6. Here f for a tube inner diameter of 2.9in. is 0.0175. Substituting into
Eq. (13) yields
0:016
DP 3:36 10 6 0:0175 38;000 2 100 6:6psi
¼ (cid:4) (cid:3) (cid:4) (cid:4)ð Þ (cid:4) (cid:4) 2:95 ¼
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.5 Viscosityof SteamandWater (lb =hft)
m
Pressure (psia)
Temp
( F) 1 2 5 10 20 50 100 200 500 1000 2000 5000
(cid:2)
1500 0.0996 0.0996 0.0996 0.0996 0.0996 0.0996 0.0996 0.0996 0.1008 0.1008 0.1019 0.1066
1400 0.0938 0.0938 0.0938 0.0938 0.0938 0.0938 0.0952 0.0952 0.0952 0.0961 0.0973 0.1019
1300 0.0892 0.0982 0.0892 0.0892 0.0892 0.0892 0.0892 0.0892 0.0892 0.0903 0.0915 0.0973
1200 0.0834 0.0834 0.0834 0.0834 0.0834 0.0834 0.0834 0.0834 0.0846 0.0846 0.0867 0.0926
1100 0.0776 0.0776 0.0776 0.0776 0.0776 0.0776 0.0776 0.0776 0.0788 0.0799 0.0811 0.0892
1000 0.0730 0.0730 0.0730 0.0730 0.0730 0.0730 0.0730 0.0730 0.0730 0.0741 0.0764 0.0857
900 0.0672 0.0672 0.0672 0.0672 0.0672 0.0672 0.0672 0.0672 0.0683 0.0683 0.0707 0.0846
800 0.0614 0.0614 0.0614 0.0614 0.0614 0.0614 0.0614 0.0614 0.0625 0.0637 0.0660 0.0973
700 0.0556 0.0556 0.0556 0.0556 0.0556 0.0556 0.0568 0.0568 0.0568 0.0579 0.0625 0.171
600 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.210 0.221
500 0.0452 0.0452 0.0452 0.0452 0.0452 0.0452 0.0452 0.0440 0.0440 0.250 0.255 0.268
400 0.0394 0.0394 0.0394 0.0394 0.0394 0.0394 0.0394 0.0382 0.317 0.320 0.323 0.335
300 0.0336 0.0336 0.0336 0.0336 0.0336 0.0336 0.441 0.442 0.444 0.445 0.448 0.460
250 0.0313 0.0313 0.0313 0.0313 0.0313 0.551 0.551 0.551 0.552 0.554 0.558 0.569
200 0.0290 0.0290 0.0290 0.0290 0.725 0.725 0.725 0.726 0.729 0.729 0.732 0.741
150 0.0255 0.0255 1.032 1.032 1.032 1.032 1.032 1.032 1.033 1.034 1.037 1.044
100 1.645 1.645 1.645 1.645 1.645 1.645 1.645 1.645 1.645 1.646 1.646 1.648
50 3.144 3.144 3.144 3.144 3.144 3.144 3.144 3.142 3.141 3.139 3.134 3.119
32 4.240 4.240 4.240 4.240 4.240 4.240 4.240 4.239 4.236 4.231 4.222 4.192
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.6 Tube Diameter
Versus Friction Factor
(Darcy) forTurbulentFlow
d (in.) f
i
0.5 0.028
0.75 0.0245
1.0 0.0230
1.5 0.0210
2.0 0.0195
2.5 0.0180
3.0 0.0175
4.0 0.0165
5.0 0.0160
8.0 0.0140
10.0 0.013
7.17b
Q:
Estimate the pressure drop in a superheater of a boiler that has an equivalent
lengthof200ft.Thetubeinnerdiameteris2.0in.,theflowperpassis8000lb=h,
the steam pressure is 800psia, and the temperature is 700 F.
(cid:2)
A:
Using Eq. (13) and substituting v 0.78cu ft=lb and f 0.0195 for turbulent
¼ ¼
flow from Table 7.6 (generally flow in superheaters, economizers, and piping
would be turbulent), we obtain
0:78
DP 3:36 10 6 0:0195 200 80002 21psi
¼ (cid:4) (cid:3) (cid:4) (cid:4) (cid:4) (cid:4) 25 ¼
7.18a
Q:
How does the friction factor depend on pipe roughness?
A:
For smooth tubes such as copper and other heat exchanger tubes, f is given by
[12]
f 0:133 Re 0:174 15
(cid:3)
¼ (cid:4) ð Þ
Copyright © 2003 Marcel Dekker, Inc.

Substituting this into Eq. (13) gives us
DP V1:826
0:0267r0:8267m0:174 16
L ¼ d1:174 ð Þ
e i
(m is the viscosity, lb=ft h; V is the velocity, fps.)
7.18b
Q:
Determine the pressure dropper 100ft ina drawncopper tube of inner diameter
1.0in.when250lb=hofairatapressureof30 psigandat100 Fflowsthroughit.
(cid:2)
A:
Calculate the density (see Chap. 5):
45
r 29 492 0:213lb=cuft
¼ (cid:4) (cid:4)359 560 15¼
(cid:4) (cid:4)
Theeffectofpressurecanbeneglectedintheestimationofviscosityofgasesup
to 40psig. For a detailed computation of viscosity as a function of pressure,
readers may refer to Ref. 11. From Table 7.7, m 0.047lb=ft h. The velocity is
¼
576
V 250 60fps
¼ (cid:4)3600 3:14 0:213¼
(cid:4) (cid:4)
DP 601:826
0:0267 0:2130:8267 0:0470:174 7:7psi
100¼ (cid:4) (cid:4) (cid:4) 1 ¼
TABLE7.7 Viscosityof Air
Temperature( F) Viscosity (lb=ft h)
(cid:2)
100 0.0459
200 0.0520
400 0.062
600 0.0772
800 0.0806
1000 0.0884
1200 0.0957
1400 0.1027
1600 0.1100
1800 0.1512
Copyright © 2003 Marcel Dekker, Inc.

7.19a
Q:
Derive the expression for DP for laminar flow of fluids.
A:
For laminar flow of fluids in pipes such as that occurring with oils, the friction
factor is
64
f 17a
¼Re ð Þ
Substituting into Eq. (13) and using Eq. (14) gives us
L v
DP
¼
3:36
(cid:4)
10
(cid:3)
6
(cid:4)
64
(cid:4)
d
i
mW2
15:2
e(cid:4)
Wd5
14:4 10 6 W L
vm (cid:4) i
ð
17b
Þ
¼ (cid:4) (cid:3) (cid:4) (cid:4) e(cid:4)d4
i
Converting lb=h to gph (gallons per hour), we can rewrite this as
gph
DP 4:5 10 6 L cS s 18
¼ (cid:4) (cid:3) (cid:4) e(cid:4) (cid:4) (cid:4) d4 ð Þ
i
where
cS viscosity, centistokes
¼
s specific gravity
¼
Equation (18) is convenient for calculations for oil flow situations.
7.19b
Q:
Estimate the pressure drop per 100ft in an oil line when the oil has a specific
gravity of 16 API and is at 180 F. The line size is 1.0in., and the flow is
(cid:2) (cid:2)
7000lb=h.
A:
We must estimate Re. To do this we need the viscosity [13] in centistokes:
195
cS 0:226SSU forSSU32 100 19
¼ (cid:3)SSU (cid:3) ð Þ
135
cS 0:220SSU forSSU>100 20
¼ (cid:3)SSU ð Þ
SSU represents the Saybolt seconds, a measure of viscosity. Also, cS s cP,
(cid:4) ¼
where cP is the viscosity in centipoise, and 0.413cP 1lb=ft h.
¼
Copyright © 2003 Marcel Dekker, Inc.

The specific gravity is to be found. At 180 F, from Eq. (23) (see Q7.21) it
(cid:2)
can be shown that the specific volume at 180 F is 0.0176cu ft=lb. Then
(cid:2)
1
s 0:91
¼0:0176 62:4¼
(cid:4)
Hence cP 0.91 24.83, where
¼ (cid:4)
135
cS 0:22 118 24:83
¼ (cid:4) (cid:3)118¼
and
m 2:42 0:91 24:83 54:6lb=fth
¼ (cid:4) (cid:4) ¼
7000
Re 15:2 1948
¼ (cid:4)0:91 24:83 2:42¼
(cid:4) (cid:4)
(2.42 was used to convert cP to lb=ft h.) From Eq. (17a),
64
f 0:0328
¼1948¼
Substituting into Eq. (17b) yields
1
DP 14 10 6 54:6 7000 100 9:42psi
(cid:3)
¼ (cid:4) (cid:4) (cid:4) (cid:4) (cid:4)0:91 62:4¼
(cid:4)
7.20a
Q:
For viscous fluids in turbulent flow, how is the pressure drop determined?
A:
For viscous fluids, the following expression can be used for the friction factor:
0:316
f 21
¼Re0:22 ð Þ
Substituting into Eq. (13) gives us
v
DP 3:36 10 6 0:361 dm 0:22L W2
¼ (cid:4) (cid:3) (cid:4) (cid:4)ð i Þ e (cid:4) 15:2W 0:22d5
v ð Þ i 22
0:58 10 6 m0:22W1:78L ð Þ
¼ (cid:4) (cid:3) (cid:4) e(cid:4)d4:78
i
Copyright © 2003 Marcel Dekker, Inc.

7.20b
Q:
Afueloilsystemdelivers4500lb=hoflightoilat70 Finapipe.Whatistheflow
(cid:2)
that can be delivered at 30 F, assuming that m =m 0:5;v =v 0:95, and
(cid:2) 70 30 ¼ 70 30 ¼
flow is turbulent?
A:
Using Eq. (22), we have
v W1:78m0:22 v W1:78m0:22
1 1 1 ¼ 2 2 2
45001:78 0:50:22 0:95 W1:78
(cid:4) (cid:4) ¼ 2
or
W 4013lb=h
2 ¼
7.21
Q:
What is the flow in gpm if 1000lb=h of an oil of specific gravity
(60=60 F) 0.91 flows in a pipe at 60 Fand at 168 F?
(cid:2) (cid:2) (cid:2)
¼
A:
We need to know the density at 60 Fand at 168 F.
(cid:2) (cid:2)
At 60 F:
(cid:2)
Density r 0:91 62:4 56:78lb=cuft
¼ ¼ (cid:4) ¼
1
v 0:0176cuft=lb
60 ¼56:78¼
Hence at 60 F,
(cid:2)
1000
q 0:293cuft=min cfm
¼60 56:78¼ ð Þ
(cid:4)
0:293 7:48 2:2gpm
¼ (cid:4) ¼
At 168 F, the specific volume of fuel oils increases with temperature:
(cid:2)
v v 1 E t 60 23
t ¼ 60½ þ ð (cid:3) Þ(cid:5) ð Þ
whereEisthecoefficientofexpansionasgiveninTable7.8[13].Forthisfueloil,
E 0.0004. Hence,
¼
v 0:0176 1 0:0004 108 0:01836cuft=lb
168 ¼ (cid:4)ð þ (cid:4) Þ¼
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.8 Expansion Factor
forFuelOils
API E
(cid:2)
14.9 0.00035
15–34.9 0.00040
35–50.9 0.00050
51–63.9 0.00060
64–78.9 0.00070
79–88.9 0.00080
89–93.9 0.00085
94–100 0.00090
Hence
0:01836
q 1000
168 ¼ (cid:4) 60
0:306cfm 0:306 7:48
¼ ¼ (cid:4)
2:29gpm
¼
7.22
Q:
Howisthepressurelossinnaturalgaslinesdetermined?Determinethelinesize
tolimitthegaspressuredropto20psiwhen20,000scfhofnaturalgasofspecific
gravity 0.7 flows with a source pressure of 80psig. The length of the pipeline is
150ft.
A:
The Spitzglass formula is widely used for compressible fluids [13]:
P2 P2
q 3410 F 1(cid:3) 2 24
¼ (cid:4) sL ð Þ
rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
where
q gas flow, scfh
¼
s gas specific gravity
¼
P ; P gas inlet and exit pressures, psia
1 2¼
F a function of pipe inner diameter (see Table 7.9)
¼
L length of pipeline, ft
¼
Substituting, we have
952 752
20;000 3410 F (cid:3)
¼ (cid:4) 0:7 150
rffiffiffiffiffiffiffiffi(cid:4)ffiffiffiffiffiffiffiffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

HenceF 1.03.FromTable7.9weseethatd shouldbe11in.Choosingthenext
¼ 4
higherstandardF ord limitsthepressuredroptodesiredvalues.Alternatively,if
q; d; L, and P are given, P can be found.
1 2
7.23
Q:
Determine the pressure loss in a rectangular duct 2ft 2.5ft in cross section if
(cid:4)
25,000lb=h of flue gases at 300 F flow through it. The equivalent length is
(cid:2)
1000ft.
TABLE7.9 Standard Steel Pipea Data(Black,Galvanized, Welded, and
Seamless)
Functions
Nominal Outside Inside Wall ofinside
pipesize diameter diameter thickness diameter,c
[in.(mm)] Scheduleb [in. (mm)] (in.) (in.) F(in.)
1=8(6) 40 0.405(10.2) 0.269 0.068 0.00989
1=4(8) 40 0.540(13.6) 0.364 0.088 0.0242
3=8(10) 40 0.675(17.1) 0.493 0.091 0.0592
1=2(15) 40 0.840(21.4) 0.622 0.109 0.117
3=4(20) 40 1.050(26.9) 0.824 0.113 0.265
1(25) 40 1.315(33.8) 1.049 0.113 0.533
11=4(32) 40 1.660(42.4) 1.380 0.140 1.17
11=2(40) 40 1.900(48.4) 1.610 0.145 1.82
2(50) 40 2.375(60.2) 2.067 0.154 3.67
21=2(65) 40 2.875(76.0) 2.469 0.203 6.02
3(80) 40 3.500(88.8) 3.068 0.216 11.0
4(100) 40 4.500(114.0) 4.026 0.237 22.9
5(125) 40 5.563(139.6) 5.047 0.258 41.9
6(150) 40 6.625(165.2) 6.065 0.280 68.0
8(200) 40 8.625(219.1) 7.981 0.322 138
8(200) 30 8.625 8.071 0.277 142
10(250) 40 10.75 (273.0) 10.020 0.365 247
10(250) 30 10.75 10.136 0.307 254
12(300) 40 12.75 (323.9) 11.938 0.406 382
12(300) 30 12.75 12.090 0.330 395
aASTMA53-68,standardpipe.
bSchedulenumbersareapprox.valuesof1000 maximuminternalservicepressure,psig
(cid:4) allowablestressinmaterial,psi
cF d 1 0:03d 3:6=d foruseinSpitzglassformula 5=23forgaslinepressureloss.
¼ ð þ þ Þ ¼
Source:AdaptedfromRef.13.
pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

A:
The equivalent diameter of a rectangular duct is given by
b 2:5
d 2 a 2 2
i ¼ (cid:4) (cid:4)a b¼ (cid:4) (cid:4)4:5
þ
2:22ft 26:64in:
¼ ¼
Thefrictionfactor f inturbulentflowregionfor flowinducts andpipesisgiven
by [11]
0:316
f 25
¼Re0:25 ð Þ
We make use of the equivalent diameter calculated earlier [Eq. (14)] while
computing Re:
W
Re 15:2
¼ dm
i
From Table 7.7 at 300 F, m 0.05lb=ft h.
(cid:2)
¼
25,000
Re 15:2 285;285
¼ (cid:4)26:64 0:05¼
(cid:4)
Hence
0:316
f 0:014
¼285;2850:25 ¼
For air or flue gases, pressure loss is generally expressed in inches of water
column and not in psi. The following equation gives DP [11]:
g
L
DP 93 10 6 fW2v e 26
g ¼ (cid:4) (cid:3) (cid:4) d5 ð Þ
where d is in inches and the specific volume is v 1=r.
i ¼
40
r 0:526lb=cuft
¼460 300¼
þ
Hence
1
v 19cuft=lb
¼0:0526¼
Substituting into Eq. (26), we have
1000
DP 93 10 6 0:014 25;0002 19 1:16in:WC
g ¼ (cid:4) (cid:3) (cid:4) (cid:4) (cid:4) (cid:4) 26:64 5 ¼
ð Þ
Copyright © 2003 Marcel Dekker, Inc.

7.24a
Q:
Determine the Reynolds number when 500,000lb=h of superheated steam at
1600psig and 750 F flows through a pipe of inner diameter 10in.
(cid:2)
A:
Theviscosityofsuperheatedsteamdoesnotvaryasmuchwithpressureasitdoes
with temperature (see Table 7.5).
m 0:062lb=fth
¼
Using Eq. (14), we have
W 500;000
Re 15:2 15:2
¼ (cid:4)dm¼ (cid:4)10 0:062
i (cid:4)
1:25 107
¼ (cid:4)
7.24b
Q:
Determine the Reynolds number when hot air flows over a tube bundle.
Air mass velocity 7000lb=ft2h
¼
Temperature of air film 800 F
(cid:2)
¼
Tube size 2in. OD
¼
Transverse pitch 4.0in.
¼
A:
The Reynolds number when gas or fluids flowover tube bundles is givenby the
expression
Gd
Re 27
¼12m ð Þ
where
G fluid mass velocity, lb=ft2 h
¼
d tube outer diameter, in.
¼
m gas viscosity, lb=ft h
¼
At 800 F, the air viscosity from Table 7.7 is 0.08lb=ft h; thus
(cid:2)
2
Re 7000 14;580
¼ (cid:4)12 0:08¼
(cid:4)
Copyright © 2003 Marcel Dekker, Inc.

7.25
Q:
There are three tubes connected between two headers of a super heater, and it is
requiredtodeterminetheflowineachparallelpass.Thetablegivesthedetailsof
each pass.
Tube no. (passno.) Inner diameter(in.) Equivalentlength(ft)
1 2.0 400
2 1.75 350
3 2.0 370
Total steam flow is 15,000lb=h, and average steam conditions are 800psia and
750 F.
(cid:2)
A:
Becausethepassesareconnectedbetweenthesameheaders,thepressuredropin
each will be the same. Also, the total steam flow will be equal to the sum of the
flow in each. That is,
DP DP DP
1 ¼ 2 ¼ 3
In other words, using the pressure drop correlation, we have
L L L
W2f e1 W2f e2 W2f e3
1 1d5 ¼ 2 2 d5 ¼ 3 3 d5
i1 i2 i3
and
W W W totalflow
1þ 2þ 3 ¼
Theeffectofvariationsinsteampropertiesinthevarioustubescanbeneglected,
because it will not be very significant.
Substituting the data and using f from Table 7.6, we obtain
W W W 15;000
1þ 2þ 3 ¼
400 350
W2 0:0195 W2 0:02
1 (cid:4) (cid:4) 25 ¼ 2 (cid:4) (cid:4) 1:75 5
ð Þ
370
W2 0:0195
¼ 3 (cid:4) (cid:4) 25
a constant
¼
Copyright © 2003 Marcel Dekker, Inc.

Simplifying and solving for flows, we have
W 5353lb=h; W 4054lb=h; W 5591lb=h
1 ¼ 2 ¼ 3 ¼
This type of calculation is done to check if each pass receives adequate steam
flowtocoolit.Notethatpass2hadtheleastflow,andametaltemperaturecheck
mustbeperformed.Ifthemetaltemperatureishigh,thetubelengthortubesizes
must be modified to ensure that the tubes are protected from overheating.
7.26
Q:
How is the equivalent length of a piping system determined? 100ft of a piping
systemhasthreeglobevalves,acheckvalve,andthree90 bends.Ifthelinesize
(cid:2)
is 2in., determine the total equivalent length.
A:
The total equivalent length isthesum ofthe developedlength ofthepipingplus
the equivalent lengths of valves, fittings, and bends. Table 7.10 gives the
equivalent length of valves and fittings. A globe valve has 58.6ft, a check
valvehas17.2ft, anda90 bendhas5.17ftofequivalentlength.The equivalent
(cid:2)
length of all valves and fittings is
3 58:6 17:2 3 5:17 208:5ft
(cid:4) (cid:4) þ (cid:4) ¼
Hence the total equivalent length is 100 208:5 308:5ft.
ð þ Þ¼
TABLE7.10 Equivalent LengthL forValvesand
e
Fittingsa
Pipesize (in.) 1b 2b 3b 4b
1 0.70 8.70 30.00 2.60
2 1.40 17.20 60.00 5.20
3 2.00 25.50 87.00 7.70
4 2.70 33.50 114.00 10.00
6 4.00 50.50 172.00 15.20
8 5.30 33.00 225.00 20.00
10 6.70 41.80 284.00 25.00
12 8.00 50.00 338.00 30.00
16 10.00 62.50 425.00 37.50
20 12.50 78.40 533.00 47.00
aL Kd=12f,whered isthepipeinnerdiameter(in.)andK is
e¼ i i
the number of velocity heads (adapted from Crane Technical
Paper410).f istheDarcyfrictionfactor.
b1, Gate valve, fully open; 2, swing check valve, fully open;
3,globevalve,fullyopen;4,90 elbow.
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

7.27
Q:
Determine the pressure drop of flue gases and air flowing over a tube bundle
under the following conditions:
Gas mass velocity 7000lb=ft2 h
¼
Tube size 2in. OD
¼
Transverse pitch 4.0in.
¼
Longitudinal pitch 3.6in.
¼
Arrangement: in-line
Average gas temperature 800 F
(cid:2)
¼
Number of rows deep 30
¼
A:
The following procedure may be used to determine gas pressure drop over tube
bundles in in-line and staggered arrangements [11].
N
DP 9:3 10 10 fG2 H 28
g ¼ (cid:4) (cid:3) (cid:4) (cid:4) r ð Þ
g
where
G gas mass velocity, lb=ft2 h
¼
DP gas pressure drop, in. WC
g¼
f friction factor
¼
r gas density, lb=cu ft
g¼
N number of rows deep
H¼
For an in-line arrangement for S =d 1.5–4.0 and for 2000<
T ¼
Re<40;000 [12],
0:08S =d
f Re 0:15 0:044 L 29
¼ (cid:3) þ ð S T =d (cid:3) 1 Þ 0:43 þ 1:13d=S L! ð Þ
where S is the transverse pitch and S is the longitudinal pitch, in.
T L
For a staggered arrangement for S =d 1.5–4.0,
T ¼
0:1175
f Re 0:16 0:25 30
¼ (cid:3) þ S =d 1 1:08 ð Þ
(cid:1) ð T (cid:3) Þ (cid:2)
Intheabsenceof informationongasproperties,useamolecular weightof
30 for flue gas. Then, from Chapter 5,
492
r 30 0:0326lb=cuft
g ¼ (cid:4)359 460 800 ¼
(cid:4)ð þ Þ
Copyright © 2003 Marcel Dekker, Inc.

The viscosity is to be estimated at the gas film temperature. However, it can be
computedattheaveragegastemperature,andthedifferenceisnotsignificantfor
Reynolds number computations.
From Table 7.7, m 0:08lb=ft h. From Eq. (27),
¼
Gd 7000 2
Re (cid:4) 14;580
¼12m¼12 0:08¼
(cid:4)
From Eq. (29),
0:08 2
f 14;580 (cid:3) 0:15 0:044 (cid:4) 0:0484
¼ð Þ þ 1 ¼
(cid:1) (cid:2)
30
DP 9:3 10 0 0:0484 70002
g ¼ (cid:4) (cid:3) (cid:4) (cid:4) (cid:4)0:0326
2:03in:WC
¼
Similarly, using Eq. (30) we can estimate DP for a staggered arrangement.
g
Note: The foregoing procedure may be used in the absence of field-tested
data or correlation.
7.28
Q:
Determine the gas pressure drop over a bundle of circumferentially finned tubes
in an economizer when
Gas mass velocity of flue gas 6000lb=ft2h
¼
(The method of computing G for plain and finned tubes is discussed in
Chapter 8.)
Average gas temperature 800 F
(cid:2)
¼
Tube size 2.0in.
¼
Transverse pitch S 4.0in.
T¼
Longitudinal pitch S 3.6in.
L¼
Number of rows deep N 10
H ¼
A:
The equation of Robinson and Briggs [11] may be used in the absence of
site-proven data or correlation provided by the manufacturer for staggered
arrangement:
1:58 10 8 G1:684d0:611m0:316 460 t N
DP (cid:4) (cid:3) (cid:4) ð þ Þ H 31
g ¼ S0:412S0:515 MW ð Þ
T L (cid:4)
Copyright © 2003 Marcel Dekker, Inc.

where
G gas mass velocity, lb=ft h
¼
MW gas molecular weight
¼
d tube outer diameter, in.
¼
F t m0:316 460 t
ðÞ¼ (cid:4)ð þ Þ
S ; S transverse and longitudinal pitch, in.
T L¼
F t isgivenasafunctionofgastemperatureinTable7.11.SubstitutingintoEq.
ð Þ
(31) gives us
DP 1:58 10 8 60001:684 20:611 556
g ¼ (cid:4) (cid:3) (cid:4) (cid:4) (cid:4)
10
(cid:4)40:412 3:60:515 30
(cid:4) (cid:4)
3:0in:WC
¼
7.29
Q:
What is boiler circulation, and how is it determined?
A:
The motive force driving the steam–water mixture through boiler tubes (water
tube boilers) or over tubes (in fire tube boilers) is often the difference in density
betweenthecoolerwaterinthedowncomercircuitsandthesteam–watermixture
in the riser tubes (Fig. 7.4). A thermal head is developed because of this
difference, which forces a certain amount of steam–water mixture through the
system. This head overcomes several losses in the system such as
Friction loss in the downcomers
Frictionlossandflowaccelerationlossintherisersandconnectingpipesto
the drum
TABLE7.11 F t
ð Þ
Versus t for Air or Flue
Gases
t F F t
(cid:2)
ð Þ ð Þ
200 251
400 348
600 450
800 556
1000 664
1200 776
1600 1003
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.4 Scheme of natural circulation boiler showing furnace, drum, riser,
and downcomercircuits.
Copyright © 2003 Marcel Dekker, Inc.

Gravity loss in the evaporator tubes and the riser system
Losses in the drum internals
Generally, the higher the drum operating pressure, the less the difference
betweenthedensitiesofwaterandthesteam–watermixture,andhencethelower
the circulation rate.
Circulation ratio (CR) is defined as the ratio between the mass of the
steam–water mixture flowing through the system and the mass of the steam
generated.IfCR 15,then aboilergenerating 10,000lb=hofsteam wouldhave
¼
150,000lb=h of steam–water mixture flowing through the downcomers, risers,
internals, etc. The quality of steam at the exit of the riser 1=CR, or 0.067 if
¼
CR 15. In other words, 6.7% would be the average wetness of steam in the
¼
mixture. Low pressure systems have an average CR ranging from 10 to 40. If
thereareseveralparallelcircuitsforthesteam–watermixture,eachwouldhavea
differentresistancetoflow,andhenceCRwouldvaryfrom circuittocircuit.For
natural circulation systems, CR is usually arrived at by trial and error or by
iterative calculation, which first assumes a CR and computes all the losses and
then balances the losses with the available thermal head. This computation is
iterated until the available head and the losses balance.
Sometimesthedifferenceindensitybetweenthewaterandthesteam–water
mixtureisinadequatetocirculatethemixturethroughthesystem.Insuchcases,a
circulationpump isinstalled atthebottomofthesteam drum,whichcirculatesa
desiredquantityofmixturethroughthesystem(Fig.7.5).Thissystemiscalleda
forcedcirculationsystem.Onehastoensurethatthereareanadequatenumberof
FIGURE 7.5 Scheme offorced circulation boiler.
Copyright © 2003 Marcel Dekker, Inc.

pumps to ensure circulation, because the failure of the pump would mean
starvation of flow in the evaporator tubes. Because we are forcing the mixture
through the tubes, the CR is preselected, and the circulating pump is chosen
accordingly. A CR of 3–10 is typical. This system is usually used when the
pressuredropthroughtheevaporatorislikelytobehighsuchaswhenhorizontal
tubes are used. When horizontal tubes are used, the critical heat flux to avoid
DNB (departure from nucleateboiling) conditions is lower, so forced circulation
helps to ensure adequate flow inside the tubes. Circulating pumps are also used
whentheboilerpressureishighowingtothelowerdifferenceindensitybetween
the water and the steam–water mixture.
7.30
Q:
What is the main purpose of determining CR?
A:
Determination of CR is not the end in itself. The CR value is used to determine
whether a given circuit in the boiler has all the conditions necessary to avoid
departure from nucleate boiling (DNB) problems. For each pressure and quality
(orCR)thereisaparticularheatfluxbeyondwhichthetypeofboilingmaychange
from nucleateboiling, whichispreferred,to film boiling, whichistobeavoided
because it can cause the tube wall temperatures to rise significantly, resulting in
tubefailure.DNBoccursatheatfluxesof100,000–400,000Btu=ft2hdepending
on size and orientation of tubes, pressure, mass velocity, quality, and tube
roughness. DNB occurs at a much lower heat flux in a horizontal tube than in
anequivalentverticaltubebecausethesteambubbleformationandreleaseoccurs
morefreelyandrapidlyinverticaltubesthaninhorizontaltubes,wherethereisa
possibility of bubbles adhering to the top of the tube and causing overheating.
More information on DNB and circulation can be found in references cited in
Refs. 11 and14.
Notethattheheatfluxinfinnedtubesismuchhigherthaninbaretubesowing
tothelargeratioofexternal tointernalsurfacearea;thisaspect isalsodiscussed
elsewhere.Henceonehastobecarefulindesigningboilerswithextendedsurfaces
to ensure that the heat flux in the finned tubes does not reach critical levels or
cause DNB. That is why boilers with very high gas inlet temperatures are
designedwithafewrowsofbaretubesfollowedbyafewrowsoflow-fin-density
tubes and then high-fin-density tubes. As the gas cools, the heat flux decreases.
7.31a
Q:
Describe the procedure for analyzing the circulation system for the water tube
boiler furnace shown in Fig. 7.4.
Copyright © 2003 Marcel Dekker, Inc.

A:
First, the thermal data such as energy absorbed, steam generated, pressure, and
geometry of downcomers, evaporator tubes, and risers should be known. These
are obtained from an analysis offurnace performance (see example in Chap. 8).
The circulation ratio (CR) is assumed; then the flow through the system is
computed, followed by estimation of various pressure losses. Thom’s method is
used for evaluating two-phase flow losses [15, 16].
Thelossescan beestimatedasfollows. DP , thefriction loss intwo-phase
f
flow (evaporators=risers), is given by
f L
DP 4 10 10 v G2r 32
f ¼ (cid:4) (cid:3) (cid:4) f d i 3 ð Þ
i
The factor r is shown in Fig. 7.6. G is the tube-side mass velocity in lb=ft2 h.
3 i
ThefrictionfactorusedisthatofFanning,whichis0.25timestheMoodyfriction
factor.
FIGURE 7.6 Thom’s two-phase multiplication factor for friction loss. (See Refs.
11, 15, and16.)
Copyright © 2003 Marcel Dekker, Inc.

DP , the gravity loss in the heated riser=evaporator, is given by
g
r
DP 6:95 10 3 L 4 33
g ¼ (cid:4) (cid:3) (cid:4) v ð Þ
f
where r is obtained from Fig. 7.7.
4
DP , the acceleration loss, which is significant at lower pressures and at
a
high mass velocities, is given by
DP 1:664 10 11 v G2 r 34
a ¼ (cid:4) (cid:3) (cid:4) f (cid:4) i (cid:4) 2 ð Þ
Figure 7.8 gives r .
2
Single-phase pressure losses such as losses in downcomers are obtained
from
V2
DP 12 f L r
¼ (cid:4) e 2g d
(cid:4) i
FIGURE 7.7 Thom’s two-phase multiplication factor for gravity loss. (See Refs.
11, 15, and16.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.8 Thom’s two-phase multiplication factor for acceleration loss. (See
Refs. 11,15, and 16.)
Copyright © 2003 Marcel Dekker, Inc.

or
W2
DP 3:36 10 6 f L v
¼ (cid:4) (cid:3) (cid:4) e d5
i
where
W flow per tube, lb=h
¼
V fluid velocity, fps
¼
f Moody’s friction factor
¼
L effective or equivalent length of piping, ft
v
e¼
specific volume of the fluid, cu ft=lb
¼
The unheated riser losses can be obtained from
12L v r
DP f e G2 f f 35
f ¼ (cid:4) d i 2g 144 ð Þ
i (cid:4)
r is given in Fig. 7.9.
f
The equivalent lengths have to be obtained after considering the bends,
elbows, etc., in the piping. See Tables 7.10 and 7.12.
FIGURE7.9 Two-phasefrictionfactorforunheatedtubes.(SeeRefs.11,15,and
16.)
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.12 L =d,RatiosforFittingTurbulent
e i
Flow
Fitting L =d
e i
45 elbow 15
(cid:2)
90 elbow, standardradius 32
(cid:2)
90 elbow, mediumradius 26
(cid:2)
90 elbow, longsweep 20
(cid:2)
180 close-returnbend 75
(cid:2)
180 medium-radiusreturn bend 50
(cid:2)
Tee(used aselbow,entering run) 60
Tee(used aselbow,entering branch) 90
Gatevalve, open 7
Gatevalve, one-quarterclosed 40
Gatevalve, half-closed 200
Gatevalve, three-quartersclosed 800
Gatevalve, open 300
Angle valve,open 170
Aheatbalanceisfirst donearound thesteam drumtoestimatetheamount
ofliquid heat tobeaddedtothesteam–water mixturebefore thestartofboiling.
The mixture is considered to be water until boiling starts.
Onceallofthelossesarecomputed,theavailableheadiscomparedwiththe
losses. If they match, the assumed circulation rate is correct; otherwise another
iteration is performed. As mentioned before, this method gives an average
circulation rate for a particular circuit. If there are several parallel circuits, then
the CR must be determined for each circuit. The circuit with the lowest CR and
highest heat fluxes should be evaluated for DNB.
InordertoanalyzeforDNB,onemaycomputetheallowablesteamquality
at a given location in the evaporator with the actual quality. The system is
considered safe if the allowable quality is higher than the actual quality. The
allowablequalityisbasedontheheatflux,pressure,massvelocity,androughness
and orientation of the tubes. Studies have been performed to arrive at these
values. Figure 7.10 shows a typical chart [14] that gives the allowable steam
qualityasafunctionofpressureandheatflux.Itcanbeseenthatasthepressure
or heat flux increases, the allowable quality decreases. Another criterion for
ensuringthatasystemissafeisthattheactualheatfluxonthesteamside(inside
tubes in water tube boilers and outside tubes in fire tube boilers) must be lower
than the critical heat flux (CHF) for the particular conditions of pressure, flow,
tube size, roughness, orientation, etc. CHF values are available in the literature;
boiler manufacturers have developed their own CHF correlations based on their
experience. See Chapter 8 for an example.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE7.10 Allowablequalityfornucleateboilingat2700psia,asafunctionof
massvelocityand heatfluxinside tubes.(From Ref.14.)
Copyright © 2003 Marcel Dekker, Inc.

7.31b
Q:
Compute the circulation ratio and check the system shown in Fig. 7.4 for DNB.
A:
Figure 7.4 shows a boiler schematic operating on natural circulation principles.
The basis for estimating the flow through water walls is briefly as follows.
1. Assumeacirculationratio(CR)basedonexperience.Forlowpressure
boilers (<1000psia), CR could be from 20 to 50. For high pressure
boilers (1000–2700psia), CR could range from 9 to 5. The following
expression relates circulation ratio and dryness fraction, x:
1
CR 36
¼ x ð Þ
Hence, flow through the evaporator CR the steam generated.
¼ (cid:4)
2. Furnace thermal performance data such as efficiency, furnace exit
temperature, and feedwater temperature entering the drum should be
knownbeforethestartofthisexercise,inadditiontodetailssuchasthe
location of the drum, bends, size, and length of various circuits.
3. Mixture enthalpy entering downcomers is calculated as follows
through an energy balance at the drum.
h CR h h CR h 37
fwþ (cid:4) e ¼ gþ (cid:4) m ð Þ
4. Astheflowentersthewaterwalls,itgetsheated,andboilingstartsafter
a particular distance from the bottom of the furnace. This distance is
calledboilingheight,anditincreasesasthesubcoolingincreases.Itis
calculated as follows.
h h
L L CR W f (cid:3) m
b ¼ (cid:4) (cid:4) s Q
Beyond the boiling height, the two-phase flow situation begins.
5. Friction loss in various circuits such as downcomers, connecting
headers, water wall tubes (single-phase, two-phase losses), riser
pipes, and drums are calculated. Gravity losses, DP , are estimated
g
along withtheaccelerationlosses,DP ,in aboiling regime.The head
a
availableinthedowncomeriscalculatedandequatedwiththelosses.If
they balance, the assumed CR is correct; otherwise, a revised trial is
made until they balance. Flow through the water wall tubes is thus
estimated.
6. Checks for DNB are made. Actual quality distribution along furnace
height is known. Based on the heat flux distribution (Fig. 7.11), the
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.11 Typical heatabsorptionrates alongfurnace height.
Copyright © 2003 Marcel Dekker, Inc.

allowable quality along the furnace height can be found. If the
allowable quality exceeds actual quality, the design is satisfactory;
otherwise, burnout possibilities exist, and efforts must be made to
improve the flow through water wall tubes.
Example
Acoal-firedboilerhasafurnaceconfigurationasshowninFig.7.4.Followingare
the parameters obtained after performing preliminary thermal design:
Steam generated 600,000 lb=h
Pressure at drum 2700 psia
Feedwater temperature entering drum
from economizer 570 F
(cid:2)
Furnace absorption 320 106Btu=h
(cid:4)
Number and size of downcomers 4, 12in. ID
Number and size of water wall tubes 416, 21in. OD 0.197in. thick
2 (cid:4)
Number and size of riser tubes 15, 6in. ID
Drum ID 54in.
Furnace projeced area 8400ft2
Because it is difficult to estimate flow through parallel paths, let us assume that
flow in each tube or circuit of downcomers, water walls, and risers may be near
the average flow values. However, computer programs may be developed that
take care of different circuits. The manual method gives a good idea of the
solution procedure (though approximate).
Method
Let circulation ratio CR 8. Then x 0.125. From the steam tables,
¼ ¼
t 680 F
sat¼ (cid:2)
h 1069.7Btu=lb
g¼
h 753.7Btu=lb
v f ¼ 0.0303cu ft=lb
v f ¼ 0.112cu ft=lb
g¼
h 568Btu=lb
fw¼
Enthalpy of steam leaving water walls is
h 0:125 1069:7 0:875 753:7 793:2Btu=lb
e ¼ (cid:4) þ (cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

Heat balance around the drum gives
Steam flow 600;000lb=h
¼
Water wall, downcomer flow 8 600;000
¼ (cid:4)
4;800;000lb=h
¼
600;000 568 8 600;000 793:2
(cid:4) þ (cid:4) (cid:4) ¼
600;000 1069:7 8 600;000h
(cid:4) þ (cid:4) m
Hence, h 731Btu=lb.
m¼
From the steam tables,
v 0:0286cuft=lb
m ¼
v 0:125 0:112 0:875 0:0303
e ¼ (cid:4) þ (cid:4)
0:0405cuft=lb
¼
a. DP headavailable 106= 0:0286 144 25:7psi.
g ¼ ¼ ð (cid:4) Þ¼
b. DP losses in downcomer circuit.
dc¼
The downcomer has one 90 bend and one entrance and exit loss.
(cid:2)
Using an approximate equivalent length of 7d,
i
L 104 16 7 12 204ft
e ¼ þ þð (cid:4) Þ¼
The value f from Table 7.6 is around 0.013.
i
8 600;000 0:0286 576
V (cid:4) (cid:4) (cid:4) 12:1fps
dc ¼ 3600 p 144 4 ¼
(cid:4) (cid:4) (cid:4)
0:013 204 12:1 2 12
DP (cid:4) (cid:4)ð Þ (cid:4)
dc ¼2 32 12 0:0286 144
(cid:4) (cid:4) (cid:4) (cid:4)
1:47psi
¼
c. Estimate boiling height:
753:7 731
L 100 8 600;000 (cid:3)
b ¼ (cid:4) (cid:4) (cid:4) 320 106
(cid:4)
31ft
¼
Hence, up to a height of 31ft, preheating of water occurs. Boiling
occurs over a length of only 100731 69ft.
¼
Copyright © 2003 Marcel Dekker, Inc.

d. Gravity loss in boiling height:
0:0286 0:0303
V ; mean specific volume þ
m ¼ 2
0:02945cuft=lb
¼
31
DP 7:3psi
g ¼0:02945 144¼
(cid:4)
e. Friction loss in boiling height. Compute velocity through water wall
tubes: d 2.1in.
i¼
8 600;000 576 0:02945
V (cid:4) (cid:4) (cid:4)
w ¼ 416 p 2:1 2 3600
(cid:4) (cid:4)ð Þ (cid:4)
3:93fps
¼
From Table 7.6, f 0.019.
i¼
One exit loss, one 135 bend, and one 45 bend can be con-
(cid:2) (cid:2)
sideredforcomputinganequivalentlength.L worksouttoabout45ft.
e
0:019 45 3:93 2 12
DP (cid:4) (cid:4)ð Þ (cid:4)
w ¼2 32 2:1 0:02945 144
(cid:4) (cid:4) (cid:4) (cid:4)
0:28psi
¼
f. Compute losses in two-phase flow, from Figs. 7.6–7.8, for x 12:5%
¼
and P 2700psi,
¼
r 0:22; r 1:15; r 0:85
2 ¼ 3 ¼ 4 ¼
For computing two-phase losses:
DP 1:664 10 11 v r G2
a ¼ (cid:4) (cid:3) (cid:4) f 2 i
8 600,000 576
G (cid:4) (cid:4) 480;000lb=ft2 h
i ¼ 416 p 2:1 2 ¼
(cid:4) (cid:4)ð Þ
DP 1:664 10 11 0:0303
a ¼ (cid:4) (cid:3) (cid:4)
4:8 105 2 0:22 0:026psi
(cid:4)ð (cid:4) Þ (cid:4) ¼
Friction loss,
0:0019
DP 4 10 10 0:0303
f ¼ (cid:4) (cid:3) (cid:4) (cid:4) 4
1:15
69 4:8 105 2
(cid:4) (cid:4)ð (cid:4) Þ (cid:4) 2:1
0:5psi
¼
Copyright © 2003 Marcel Dekker, Inc.

Gravity loss,
6:944 10 3 69 0:85
DP (cid:4) (cid:3) (cid:4) (cid:4) 13:4psi
g ¼ 0:0303 ¼
Total two-phase loss 0:026 0:5 13:4
¼ þ þ
13.926 psi, or 14.0 psi
¼
g. Risercircuitlosses.UseThom’smethodfortwo-phaseunheatedtubes.
Let the total equivalent length, considering bends and inlet and exit
losses, be 50ft.
r 1:4 Fig: 7:9 ; f 0:015from Table 7.6
f ¼ ð Þ i ¼
576 8 600,000
G (cid:4) (cid:4) 1:63 106 lb=ft2 h
i ¼ p 36 15 ¼ (cid:4)
(cid:4) (cid:4)
50 12 1:63 106 2
DP 0:015 (cid:4) ð (cid:4) Þ
f ¼ (cid:4) 6 (cid:4)2 32 36002
(cid:4) (cid:4)
1:4
0:0303 1:41psi
(cid:4)144(cid:4) ¼
Note that in estimating pressure drop by Thom’s method for heated
tubes,theDarcyfrictionfactorwasused.Forunheatedtubes,Moody’s
friction factor could be used. Void fraction a from Fig. 7.12 0.36.
0
¼
L
DP r 1 a1 r a 38
g ¼½ fð (cid:3) Þþ g 0 (cid:5)144 ð Þ
1 1
DP 0:64 0:36
g ¼ 0:0303(cid:4) þ 0:112(cid:4)
(cid:6)(cid:1) (cid:2) (cid:1) (cid:2)(cid:7)
5
0:85psi
(cid:4)144¼
Total losses in riser circuit 1.41 0.85 2.26psi.
¼ þ ¼
h. Losses in drum. This is a negligible value; use 0.2psi. (Generally the
supplier of the drums should furnish this figure.)
Total losses b d e f g h
¼ þ þ þ þ þ
1:47 7:3 0:28 14:0 2:26 0:2
¼ þ þ þ þ þ
25:51psi
¼
Available head a 25:7psi
¼ ¼
Hence, because these two match, an assumed circulation ratio of 8 is
reasonable.Thisisonlyanaveragevaluefortheentiresystem.Ifoneis
interested in a detailed analysis, the circuits should be separated
Copyright © 2003 Marcel Dekker, Inc.

FIGURE7.12 Voidfractionasafunctionofqualityandpressureforsteam[See
Refs. 11,16].
accordingtoheatloadings,andarigorouscomputeranalysisbalancing
flows and pressure drop in each circuit can be carried out.
Analysis for DNB
TypicalfurnaceabsorptionprofilesfortheactualfuelfiredaredesirableforDNB
analysis.Thesedataaregenerallybasedonfieldtests,butfortheproblemathand
let us use Fig. 7.11, which gives typical absorption profiles for a boiler.
furnace absorption 320 106
Average heat flux (cid:4)
¼furnace projected area¼ 8400
38,095 Btu/ft2 h
¼
There is a variation at any plan cross section of a boiler furnace between the
maximum heat flux and the average heat flux, based on the burner location,
burners in operation, excess air used, etc. This ratio between maximum and
average could be 20–30%. Let us use 25%.
Again, the absorption profile along furnace height shows a peak at some
distanceabovetheburnerwheremaximumheatreleasehasoccurred.Itdecreases
astheproductsofcombustionleavethefurnace.Theaveragefortheentireprofile
Copyright © 2003 Marcel Dekker, Inc.

may be found, and the ratio of actual to average heat flux should be computed.
Forthesakeof illustration,usethefollowingratiosofactualtoaverageheatflux
at the locations mentioned.
Distancefrom Ratio of actual to
bottom(ft) averageheatflux
40 1.4
56 1.6
70 1.0
80 0.9
100 0.4
We must determine the maximum inside heat flux at each of the locations
andcorrectitforfluxinsidethetubestocheckforDNB.Hence,consideringthe
tube OD=ID ratio of 1.19 and the 25% nonuniformity at each furnace elevation,
wehavethefollowinglocalmaximuminsideheatfluxatthelocationsmentioned
q is taken asq d=d :
ð i p(cid:4) iÞ
Location(ft) q (Btu=ft2h)
i
40 1.4 38,095 1.25 1.19 79,335
(cid:4) (cid:4) (cid:4) ¼
56 90,440
70 56,525
80 50,872
100 22,600
Itisdesirabletoobtainallowablequalityofsteamateachoftheselocations
and check to be sure actual quality does not exceed it.
DNBtestsbasedonparticulartubeprofiles,roughness,andwaterqualityas
used in the operation give the most realistic data for checking furnace tube
burnout. Correlations, though available in the literature, may give a completely
wrongpicturebecausetheyarebasedontubesize,heatingpattern,waterquality,
andtuberoughnessthatmaynottallywithactualoperatingconditions.However,
they give the trend, which could be useful. For the sake of illustrating our
example, let us use Fig. 7.10. This gives a good estimate only, because
Copyright © 2003 Marcel Dekker, Inc.

extrapolation must be carried out for the low heat flux in our case. We see the
following trend at G 480,000lb=ft2 h and 2700psia:
i¼
Location(ft) Allowable quality(%)
40 25
56 22
70 30
80 34
100 42
Figure7.13shows theactualquality (assuminglinear variation,perhaps in
reality quadratic) versus allowable quality. It shows that a large safety margin
exists; hence, the design is safe. This exercise should be carried out at all loads
(and for all circuits) before coming to a conclusion.
7.32a
Q:
How is the circulation system analyzed in fire tube boilers?
A:
The procedure is similar to that followed for water tube boilers in that the CR is
assumed and the various losses are computed. If the losses associated with the
assumed CR and the resulting mass flow are in balance with the available head,
thentheassumedCRiscorrect;otherwiseanotheriterationisdone.Becausefire
tubeboilersingeneralusehorizontaltubes,theallowableheatfluxtoavoidDNB
islowerthanwhenverticaltubesareused.Withgasstreamscontaininghydrogen
and steam as in hydrogen plant waste heat boilers, the tube-side and hence the
overallheattransfercoefficientandheatfluxwillberatherhighcomparedtoflue
gas stream from combustion of fossil fuels. Typical allowable heat fluxes for
horizontal tubes range from 100,000 to 150,000Btu=ft2h.
7.32b
Q:
Perform the circulation calculations for the system shown in Fig. 7.14 with the
following data:
Steam flow 20;000lb=h; steam pressure 400psig
¼ ¼
Assume that saturated water enters the drum.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.13 Actual qualityvs. allowablequality alongfurnaceheight.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.14 Circulation schemein fire tubeboiler.
A:
From steam tables, v 0.194 and v 1.12cu ft=lb. Assume there are two
f ¼ g¼
downcomers of size 4 in schedule 40 (d 4.026in.) and two risers of size 8 in
i¼
schedule 40 (d 7.981in.). The total developed length of each downcomer is
i¼
22.5ft,andeachhastwo90 bends;theriser pipeshaveatotaldevelopedlength
(cid:2)
of5ft.Exchangerdiameteris6ft,andthecenterdistancebetweentheexchanger
and the steam drum is 8ft.
1. Assume CR 15; then
¼
Mixture volume 0:067 1:12 0:933 0:0194
¼ (cid:4) þ (cid:4)
0:0931
¼
The head available due to the column of saturated water is
11=(0.0194 144) 3.94psi, where 11ft is the height of the water
(cid:4) ¼
column.
2. Losses in downcomers:
20,000
a. Water velocity 0:05 15
¼ (cid:4) (cid:4) 2
(cid:1) (cid:2)
0:0194
(cid:4) 4:026 2
ð Þ
9fps
¼
Inlet plus exit losses 1:5velocity head
¼
9
1:5 9
¼ (cid:4) (cid:4)2 32 144 0:0194
(cid:4) (cid:4) (cid:4)
0:68psi
¼
Copyright © 2003 Marcel Dekker, Inc.

b. Total developed length 22.5 2 10 42.5ft, where 10ft is
¼ þ (cid:4) ¼
the equivalent length of a 90 bend from Table 7.10.
(cid:2)
20 2
DP 3:36 0:0165 15
f ¼ (cid:4) (cid:4) (cid:4) 2
(cid:1) (cid:2)
0:0194
42:5
(cid:4) (cid:4) 4:026 5
ð Þ
0:98psi
¼
where0.0165isthefrictionfactor.Equation(13)wasusedforpressure
drop of single-phase flow.
Total downcomer losses 0:68 0:98
¼ þ
1:66psi
¼
3. Friction andaccelerationlossesintheexchangermaybeneglectedfor
thisfirsttrial,becauseinafiretubeboilertheywillbenegligibledueto
the low mass velocity.
4. Gravity losses in the exchanger: Using Fig. 7.7, r 0.57.
4¼
0:57
DP 0:00695 6 1:22psi
g ¼ (cid:4) (cid:4)0:0194¼
5. Gravity loss in riser pipe:
5
DP 0:37 psi
g ¼0:0931 144¼
(cid:4)
6. Friction loss in riser:
20;000 0:0931
Velocity 0:05 15 11fps
¼ (cid:4) (cid:4) 2 (cid:4) 7:981 2 ¼
(cid:1) (cid:2) ð Þ
Inlet plus exit losses 1:5 velocity head
¼ (cid:4)
1:5 11 11
(cid:4) (cid:4) 0:21psi
¼2 32 0:0931 144¼
(cid:4) (cid:4) (cid:4)
20 2
Friction loss 3:36 0:014 15
¼ (cid:4) (cid:4) (cid:4) 2
(cid:1) (cid:2)
0:0931
5 0:02psi
(cid:4) (cid:4) 7:981 5 ¼
ð Þ
where 5ft is the developed length of the riser.
Copyright © 2003 Marcel Dekker, Inc.

Let the losses in drum internals 0.5psi. This can vary depending on the
¼
type of internals used. Then
Total losses 1:66 1:22 0:37 0:21 0:02 0:50 3:98psi
¼ þ þ þ þ þ ¼
Thisisclosetotheavailablehead;henceCR 15isthecirculationratioforthis
¼
system.Thecalculationscanbefine-tunedwithactualdimensionsafterthelayout
is done. One can compute the heat flux and compare it with the allowable heat
flux to check if the circulation rate is adequate. Usually circulation is not a
problem in this type of boiler, because the heat flux is low, on the order of
20,000–30,000Btu=ft2h, whereas the allowable flux could be 100,000–
150,000Btu=ft2 h. See Chapter 8 for correlations for critical heat flux (CHF).
7.33
Q:
How is the flow in steam blowoff lines determined?
A:
Whenever steam flows to the atmosphere from a high pressure vessel, the flow
reachescriticalflowconditions,andbeyondacertainpressurefurtherloweringof
pressuredoesnotincreasethesteamdischarge.Theflowisgivenbytheequation
[17]
DP 0:5
W 1891 Y d2 39
¼ (cid:4) (cid:4) (cid:4) Kv ð Þ
(cid:1) (cid:2)
Thevalue of DP to be chosen depends on K, the system resistance, where
f L
K 12 e
¼ (cid:4) d
where
L totalequivalentlengthofalldownstreampipingincludingvalvesand
e¼
fittings, ft
f Darcy friction factor
¼
d pipe inner diameter, in.
¼
Y expansion factor (see Table 7.13)
v¼
specific volume of steam before expansion, cu ft=lb
¼
DP pressure drop, lower of actual upstream pressure minus downstream
¼
pressure or that obtained from Table 7.13
Copyright © 2003 Marcel Dekker, Inc.

TABLE7.13 Limiting Factors forSonic
Velocityk 1.3
¼
K DP=P 10 Y
1.2 0.525 0.612
1.5 0.550 0.631
2.0 0.593 0.635
3 0.642 0.658
4 0.678 0.670
6 0.722 0.685
8 0.750 0.698
10 0.773 0.705
15 0.807 0.718
20 0.831 0.718
40 0.877 0.718
100 0.920 0.718
Example
Determinetheflowofsaturatedsteamfromavesselat170psiatotheatmosphere
if the total equivalent system resistance K 10 and pipe inner diameter
¼ ¼
2.067in.
Solution. Specific volume of steam at 170psia 2.674ft3=lb. Actual
¼
DP 170714.7 155.3psia. From Table 7.13, for K 10, DP=P 0.773,
¼ ¼ ¼ 1¼
or DP 170 0.773 131.5psia. Hence, use DP 131.5psia. Also from Table
¼ (cid:4) ¼ ¼
7.13 for K 10, Y 0.705. Hence
¼ ¼
131:5 0:5
W 1891:0 0:705 2:067 2
¼ (cid:4) (cid:4)ð Þ (cid:4) 10 2:674
(cid:1) (cid:4) (cid:2)
12;630lb=h
¼
7.34
Q:
How is the flow through boiler blowdown lines determined?
A:
Sizing of blowdown or drain lines is very important in boiler or process plant
operations.
Theproblemofestimatingthedischargeratesfromaboilerdrumorvessel
to the atmosphere or to a vessel at low pressures involves two-phase flow
calculations and is a lengthy procedure [18].
Copyright © 2003 Marcel Dekker, Inc.

Presented below is a simplified approach to the problem that can save
considerable time for engineers who are involved in sizing or estimating
discharge rates from boiler drums, vessels, or similar applications involving
water.
Several advantages are claimed for these charts, including the following.
No reference to steam tables is required.
No trial-and-error procedure is involved.
Effect of friction can be easily studied.
Obtainingpipesizetodischargeadesiredrateoffluid,thereverseproblem,
is simple.
Theory
The basic Bernoulli’s equation can be written as follows for flow in a piping
system:
V2 v
104vdp dk dv dH 0 40
þ2g þg þ ¼ ð Þ
Substituting mass flow rate m V=v:
¼
m2 dv dP dH
dk 2 104 41
2g þ v ¼(cid:3) (cid:4) v (cid:3) v2 ð Þ
(cid:1) (cid:2)
Integrating between conditions 1 and 2:
m2 v 2dP 2dH
k 2ln 2 104 42a
2g þ v ¼(cid:3) v (cid:3) v2 ð Þ
(cid:1) 1(cid:2) ð1 ð1
2g 2 dP 2 dH 1=2
m 104 42b
¼ k 2ln v =v (cid:4) (cid:3) v (cid:3) v2 ð Þ
(cid:6) þ ð 2 1Þ (cid:1) ð1 ð1 (cid:2)(cid:7)
where K f l=d, the equivalent pipe resistance.
¼
Whenthepressureofthevesseltowhichtheblowdownpipeisconnectedis
decreased,theflowrateincreasesuntilcriticalpressureisreachedattheendofthe
pipe. Reducing the vessel pressure below critical pressure does not increase the
flow rate.
If the vessel pressure is less than the critical pressure, critical flow
conditions are reached and sonic flow results.
From thermodynamics, the sonic velocity can be shown to be
dP
V v2 g 104 43
c ¼sffi(cid:3)ffiffiffiffiffiffiffiffiffiffiffi
(cid:1)
ffiffiffiffidffiffiffi v ffiffiffi
(cid:2)
ffiffiffiffisffiffi(cid:4)ffiffiffiffiffiffiffiffiffiffiffiffi ð Þ
Copyright © 2003 Marcel Dekker, Inc.

and
dP
m 100 g 44
c ¼ sffi(cid:3)ffiffiffiffiffiffi
(cid:1)
ffiffiffiffidffiffiffi v ffiffiffi
(cid:2)
ffiffiffisffiffi ð Þ
The term dP=dv refers to the change in pressure-to-volume ratio at
ð Þs
critical flow conditions at constant entropy.
Hence,inordertoestimatem ,Eqs.(42)and(44)havetobesolved.Thisis
c
an iterative procedure. For the sake of simplicity, the term involving the height
differences will be neglected. For high pressure systems the error in neglecting
this term is marginal, on the order of 5%.
Theproblemis,then,givenK andP,toestimateP andm.Thisisatrial-
s c
and-error procedure, and the steps are outlined below, followed by an example.
Figs. 7.16 and 7.17 are two charts that can be used for quick sizing purposes.
1. Assume a value for P.
c
2. Calculate dP=dv at P for constant-entropy conditions. The volume
ð Þs c
change corresponding to 2–3% of P can be calculated, and then
c
dP=dv can be obtained.
ð Þs
3. Calculate m using Eq. (44).
c
4. Solve Eq. (42b) for m.
The term 10 4 2 dP=v is computed as follows using Simpson’s rule:
(cid:3) (cid:3) 1
2 dP Ð 2
104 104 rdP
(cid:3) v ¼(cid:3)
ð1 ð1
P P
s(cid:3) c r 4r r
¼ 6 (cid:4)ð sþ mþ cÞ
where r density at a mean pressure of P P =2.
m¼ ð sþ cÞ
The densities are computed as isenthalpic conditions. The term 2ln
v =v 2ln r =r is then found.
ð 2 1Þ¼ ð s cÞ
Thenmiscomputedusing Eq.(42b). Ifthe mvaluescomputedusingEqs.
(42b) and (44) tally, then the assumed P and the resultant m are correct.
c c
OtherwiseP hastobechanged,andallstepshavetoberepeateduntilmandm
c c
agree.
Example
Aboilerdrumblowdownlineisconnectedtoatanksetat8atm.Drumpressureis
100atm, and the resistance K of the blowdown line is 80. Estimate the critical
mass flow rate m and the critical pressure P .
c c
The procedure will be detailed for an assumed pressure P of 40atm.
c
For steam table P 100atm, s 0.7983kcal=kg C; h 334kcal=kg,
v 0.001445m3=kg, or r s¼ 692kg=m3. ¼ (cid:2) l¼
l¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

Let r 40atm; then h 258.2kcal=kg, h 669kcal=kg, S 0.6649,
S 1.4513, c¼v 0.001249, v l¼ 0.05078. v ¼ l¼
v ¼ l¼ v ¼
Hence:
S S 0:7983 0:6649
x (cid:3) l (cid:3)
¼S
v (cid:3)
S
l
¼1:4513
(cid:3)
0:6649
0:1696
¼
v v x v v
¼ lþ ð v (cid:3) lÞ
0:001249 0:1696 0:05078 0:001249
¼ þ (cid:4)ð (cid:3) Þ
0:009651m3=kg
¼
Again, compute v at 41atm (2.5% more than P ). Using steps similar to
c
those described above, v 0.0093m3=kg.
¼
Hence,
dP
m 100 g
c ¼ sffi(cid:3)ffiffiffiffiffiffi
(cid:1)
ffiffiffidffiffiffi v ffiffi
(cid:2)
ffiffiffiffisffi
9:8 1
100 (cid:4) 16;733kg=m2 s
¼ 0:00965 0:0093¼
rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi(cid:3)ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Compute the densities as
1
r 692kg=m3
s ¼0:001445¼
The dryness fraction at 40atm at isenthalphic condition is
334 258:2
x (cid:3) 0:1845
¼669 258:2¼
(cid:3)
v 0:001249 0:1845 0:05078 0:001249
c ¼ þ (cid:4)ð (cid:3) Þ
0:010387m3=kg
¼
r 96:3kg=m3
c ¼
Similarly, at P (100 40)=2 70atm,
m¼ þ ¼
v 0:03785m3=kg or r 264kg=m3
m ¼ m ¼
2dP 100 40
104 (cid:3) 692 4 264 96:3
(cid:3) v ¼ 6 (cid:4)ð þ (cid:4) þ Þ
ð1
v
184 106 2 ln 2
¼ (cid:4) (cid:4) (cid:4) v
1
r
2 ln s 4:6
¼ (cid:4) r ¼
c
Copyright © 2003 Marcel Dekker, Inc.

Substituting the various quantities into Eq. (42b),
2 9:8
m (cid:4) 184 106
¼ 80 4:6(cid:4) (cid:4)
rffiffiffiffiffiffiþffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
6530kg=m2 s
¼
Thetwovalues mandm donotagree.Hencewehavetorepeatthecalculations
c
for another P.
c
ThishasbeendoneforP 30and15,andtheresultsarepresentedinFig.
c¼
7.15. At about 19atm, the two curves intersect, and the mass flow rate is about
7000kg=m2 s. However, one may do the calculations at this pressure and check.
Use of Charts
As seen above, the procedure is lengthy and tedious, and trial and error is
involved. Also, reference to steam tables makes it cumbersome. Hence with
variousK valuesandinitialpressureP ,acalculatorwasusedtosolveforP and
s c
m, and the results are presented in Figs. 7.16 and 7.17.
FIGURE 7.15 Calculation results.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.16 Solvingfor m.
FIGURE 7.17 Solvingfor P.
Copyright © 2003 Marcel Dekker, Inc.

7.35
Q:
What is the effect of stack height on friction loss and draft?
A:
Wheneverhotfluegasesflowinaverticalstack,anaturaldraftiscreatedowingto
the difference in density between the low density flue gases and ambient air,
which has a higher density. However, due to the friction losses in the stack, this
available draft is reduced.
Example
If 100,000lb=h of flue gases at 400 F flow in a 48in. ID stack of 50ft height,
(cid:2)
determine the net stack effect. Ambient air temperature is 70 F.
(cid:2)
Solution. Density of flue gases (see Q5.02) at 400 F 39.5=860
(cid:2)
¼ ¼
0.0459lb=cu ft. Density of air at 70 F 40=530 0.0755lb=cu ft. Hence
(cid:2)
¼ ¼
Total draft available 0:0755 0:0459 50
¼ð (cid:3) Þ(cid:4)
1:48lb=ft2
¼
12
0:0755 0:0459 50
¼ð (cid:3) Þ(cid:4) (cid:4)62:4
0:285in: WC
¼
(The factor 62.4 is density of water, and 12 converts ft to in.)
Let us see how much the friction loss per unit length is. From Eq. (26),
v
DP 93 10 6 f W2
¼ (cid:4) (cid:3) (cid:4) (cid:4) (cid:4)d5
v 1=0.0459 21.79cu ft=lb. To estimate the friction factor f, we need the
¼ ¼
Reynolds number. From the Appendix, m 0.058lb=ft h. Hence
¼
100,000
Re 15:2 546,000
¼ (cid:4)48 0:058¼
(cid:4)
0:316
f 0:012
¼ 546;000 0:25 ¼
ð Þ
21:79
DP 93 10 6 0:012 100;000 2 50
¼ (cid:4) (cid:3) (cid:4) (cid:4)ð Þ (cid:4) (cid:4) 485
0:048in: WC
¼
Hence
Net draft available 0:285 0:048 0:237in: WC
¼ (cid:3) ¼
Copyright © 2003 Marcel Dekker, Inc.

7.36
Q:
Discuss the flow instability problem in boiler evaporators.
A:
In once-through boilers or evaporators generating steam at high quality, the
problemofflowinstabilityisoftenaconcern.Thisisduetothenatureofthetwo-
phasepressuredropcharacteristicsinsidetubes,whichcanhaveanegativeslope
with respect to flow under certain conditions. The problem is felt when multiple
streams are connected to common header systems as in once-through or forced
circulationsystems.Smallperturbationscancauselargechangesinflowthrough
afewtubes,resultinginpossibledryoutoroverheatingconditions.Vibrationcan
also occur. The problem has been observed in a few low pressure systems
generating steam at high quality.
To illustrate the problem, let us take up the example of steam generation
inside a tube. For the sake of analysis, a few assumptions will be made:
Heat flux is uniform along the length of the tube,
Steam at the exit of the tube has a quality x,
Some subcooling of feedwater is present. That is, the feedwater enters the
boiler at less than the saturation temperature.
Weareconsideringalongstraighttubewithoutbendstodescribethenature
of the problem.
Ifatubeissuppliedwithsubcooledwater,theboilingstartsaftertheenthalpy
of the water has risen to the saturated liquid level. Thus the length of the boiler
canbedividedintotwoportions,theeconomizerportionandtheevaporator,their
lengths being determined by the heat input to their respective sections.
LetW betheflowofwaterenteringinlb=h.LetQ totalheatinputtothe
¼
evaporatorandQ theheatinputperunitlength,Btu=fth.Thesteamqualityatthe
l
exit of the evaporator is x, fraction. Let the economizer length be L ft. The
1
pressure drop DP in the economizer section is
1
DP 3:36f L W2v =d5 45
1 ¼ 1 f i ð Þ
where
L WDh=Q 46
1 ¼ l ð Þ
Dh enthalpy absorbed by water in the economizer portion, Btu=lb
v ¼ average specific volume of water in the economizer, ft3=lb
f ¼
In Eq. (46) we are simply using the fact that heat addition is uniform along the
tube length.
d tube inner diameter, in.
i¼
Copyright © 2003 Marcel Dekker, Inc.

The pressure drop in the evaporator region of length L L is given by
(cid:3) 1
v x v v =2
DP 3:36f L L W2 f þ ð g(cid:3) fÞ 47
2 ¼ ð (cid:3) 1Þ d5 ð Þ
i
Now
xh L L
fg (cid:3) 1 48
Dh ¼ L ð Þ
1
because the heat applied is uniform along the evaporator length, and we are
simply taking the ratio of energy absorbed in the evaporator and economizer,
which is proportional to their lengths.
h latent heat of vaporization, Btu=lb
v fg ; ¼v specific volume of saturated liquid and vapor, ft3=lb
g f ¼
Now substituting for x from Eq. (48) in. to Eq. (47) and for L from Eq.
1
(46)andsimplifyingtheaboveequations,wecanobtainthetotalpressuredropas
follows.
DP DP DP
¼ 1þ 2
v v v v v v
kW3Dh2 g(cid:3) f kW2 Dh g(cid:3) f v kWL2Q g(cid:3) f
¼ 2Q
l
h
fg
(cid:3) h
fg
(cid:3) f !þ l 2h
fg
49
ð Þ
or
DP AW3 BW2 CW 50
¼ (cid:3) þ ð Þ
Though this is a simplistic analysis for two-phase flow pressure drop, it may be
used to show the effect of the variables on the process.
Equation (50) is shown in Fig. 7.18. It is seen that the curve of pressure
dropversusflowisnotmonotonicbuthasanegativeslope.Thisismoresoifthe
steam pressure is low. Hence it may lead to unstable conditions. For example, at
the pressure drop condition shown by the horizontal line, there could be three
possible operating points, which may cause oscillations and large variations in
flowthroughthecircuit.Thisislikelyifmultiple streamsareconnectedbetween
headers,whereafewtubescanreceiveverysmallflows,causingtubeoverheating
concerns and possible DNB conditions.
Toimprovethesituation,onemayaddarestrictionsuchasacontrolvalve
or orifice at the inlet to the economizer section. The orifice increases the
resistance in proportion to the square of the flow as shown by the term R in
Eq. (51). Figure 7.18a also shows the effect of the orifice, which makes the
pressure drop curve monotonic.
DP AW3 R B W2 CW 51
¼ þð (cid:3) Þ þ ð Þ
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 7.18 Effect of (a) orifice size, (b) pressure, and (c) inlet subcooling on
the stability oftwo-phaseboiling circuits.
Because theratio ofspecific volumes ofsteam andwater ismuch largerat
lowsteampressuresandthelatentheatisalsolarge,theproblemismorelikelyat
low pressures than at high pressures, as indicated in Fig 7.18b. Decreasing the
inlet subcooling by using a higher feedwater temperature also helps as shown in
Copyright © 2003 Marcel Dekker, Inc.

Fig. 7.18c. If inlet subcooling is eliminated, Dh 0 and then Eq. (50) becomes
¼
more stable as shown by the equation
DP BW2 CW 52
¼ þ ð Þ
NOMENCLATURE
A Area of orifice, in.2
C A constant depending on ratio of gas specific heats
CR Circulation ratio
C Discharge coefficient
d
C Control valve coefficient
v
d Tube or pipe outer diameter, in.
d ;d Orifice diameter and pipe or duct inner diameter, in.
o i
E Expansion factor for fuel oils
f Friction factor
G Gas mass velocity, lb=ft2 h
h Differential pressure across flow meter, in. WC
h Enthalpy of mixture at exit, Btu=lb
e
h ;h ;h ;h Enthalpy of saturated liquid, saturated steam, mixture, and
f g m fw
feedwater, Btu=lb
K System resistance
K Valve recovery coefficient
m
K Superheat correction factor
sh
L Length of pipe, ft
L Equivalent length, ft
e
M Constant used in Q7.25
m mass flow at critical condition, kg=m2 s
c
MW Molecular weight of gas or vapor
N Number of rows deep in a tube bundle
H
P Accumulated inlet pressure, psia
a
P Backpressure, psig
b
P Set pressure, psig
s
P Vapor pressure, psia
v
P ;P Inlet and exit pressures, psia
1 2
DP Pressure drop, psi
DP Gas pressure drop, in. WC
g
DP ;DP ;DP Acceleration loss, friction loss, and loss due to gravity, psi
a f g
q Fluid flow, gpm
Re Reynolds number
r ;r ;r ;r Factors used in two-phase pressure drop calculation
2 3 4 f
S Entropy
s Specific gravity of fluid
Copyright © 2003 Marcel Dekker, Inc.

S ;S Transverse and longitudinal pitch, in.
T L
t;T Fluid temperature, For R
(cid:2) (cid:2)
t Saturation temperature, F
s (cid:2)
v Specific volume of fluid, cu ft=lb
V Critical velocity, m=s
c
V Fluid velocity, ft=s
v ;v ;v Specificvolumeofsaturatedliquid,steam,andmixture,cuft=lb
f g m
W Flow, lb=h
x Steam quality, fraction
y Volume fraction of gas
Y Expansion factor
b d =d ratio
o i
m Fluid viscosity, lb=ft h
r Density of fluid, lb=cu ft; subscript g stands for gas
m Specific volume of fluid, m3=kg
REFERENCES
1. VGanapathy.Determiningflowmetersizes.PlantEngineering,Sept18,1980,p127.
2. ChemicalEngineers’Handbook.5thed.NewYork:McGraw-Hill,1974,pp5–7.
3. VGanapathy.Convertingpitottubereadings.PlantEngineering,June24,1982,p61.
4. ASME.BoilerandPressureVesselCode,Sec.1.NewYork:ASME,1980,pp59,67.
5. CrosbyValveCatalog402.Crosby,Wrentham,MA,1968,p27.
6. ASME.BoilerandPressureVesselCode,Sec.8.NewYork:ASME,1980,Appendix
11,p455.
7. VGanapathy.Controlvalvecoefficients.PlantEngineering,Aug20,1981,p80.
8. V Ganapathy. Nomogram estimates control valve coefficients. Power Engineering,
December1978,p60.
9. FD Jury. Fundamentals of Valve Sizing for Liquids. Fisher Tech Monograph 30.
Marshalltown,IA:FisherControlsCo.,1974,p2.
10. Masoneilan.HandbookforControlValveSizing.6thed.Norwood,MA:1977,p3.
11. VGanapathy.AppliedHeatTransfer.Tulsa,OK:PennWellBooks,1982,pp500–530.
12. VGanapathy.Chartspeedsestimatesofgaspressuredrop.OilandGasJournal,Feb4,
1980,p71.
13. North American Combustion Handbook. 2nd ed. Cleveland, OH: North American
Mfg.Co.,1978,pp20–25.
14. BabcockandWilcox.Stream:ItsGenerationandUse.38thed.
15. JRS Thom. Prediction of pressure drop during forced circulation boiling of water.
InternationalJournalofHeatTransfer7:1964.
16. W Roshenow, JP Hartnett. Handbook of Heat Transfer. New York: McGraw-Hill,
1972.
17. CraneCompanyTechnicalPaper410.
18. FJ Moody. Maximum two-phase vessel blowdown from pipes. Transactions of
ASME,JournalofHeatTransfer,August1966,p285.
Copyright © 2003 Marcel Dekker, Inc.

8
Heat Transfer Equipment Design and
Performance
8.01 Estimating surface area of heat transfer equipment; overall heat trans-
fer coefficient; approximating overall heat transfer coefficient in water
tube boilers, fire tube boilers, and air heaters; log-mean temperature
difference
8.02 Estimating tube-side heat transfer coefficient; simplified expression for
estimating tube-side coefficient
8.03 Estimating tube-side coefficient for air, flue gas, water, and steam
8.04 Estimating heat transfer coefficient outside tubes
8.05 Estimating convective heat transfer coefficient outside tubes using
Grimson’s correlations
8.06 Effect of in-line vs. staggered arrangement
8.07a Evaluating nonluminous radiation heat transfer using Hottel’s charts
8.07b Nonluminous radiation using equations
8.08a Predicting heat transfer in boiler furnaces
8.08b Design of radiant section for heat recovery application
8.09a Evaluating distribution of radiation to tube banks
8.09b Estimating the temperature of a lance inside boiler enclosure
8.10 Sizing fire tube boilers
8.11 Effect of gas velocity, tube size on fire tube boiler size
Copyright © 2003 Marcel Dekker, Inc.

8.12 Computing heat flux, tube wall temperatures
8.13 Effect of scale formation on tube wall temperature and boiler perfor-
mance
8.14 Design of water tube boilers
8.15a Predicting off-design performance
8.15b Logic for off-design performance evaluation for water tube boilers
8.16 Estimating metal temperature in a boiler superheater tube; thermal
resistances in heat transfer; calculating heat flux
8.17 Predicting performance of fire tube and water tube boilers
8.18 Why finned tubes are used and their design aspects
8.19a Heat transfer and pressure drop in finned tubes using ESCOA correla-
tions
8.19b Heat transfer in finned tubes using Briggs and Young correlation
8.19c Predicting the performance of a finned tube superheater
8.20 Sizing of finned tube evaporator
8.21 Comparison of bare tube and finned tube boilers
8.22 In-line versus staggered arrangement
8.23 Effect of tube-side heat transfer on fin configuration
8.24 Effect of tube-side fouling on bare and finned tube boilers
8.25 Estimating weight of finned tubes
8.26 Effect of fin thickness and conductivity on boiler performance and tube
and fin tip temperatures
8.27a Is surface area an important criterion for boiler selection?
8.27b Optimization of a finned evaporator surface
8.28 Design of tubular air heaters
8.29 Off-design performance of air heaters
8.30 Predicting performance of economizers using NTU method
8.31 Evaluating natural convection heat transfer coefficients in air
8.32 Natural convection heat transfer in liquids
8.33 Determining size of coil=tube bundle immersed in liquids
8.34 Evaluating gas=steam temperature profiles in HRSGs
8.35a Simulating off-design performance
8.35b A simplified approach to determining auxiliary fuel requirement in an
HRSG
8.36 Why gas exit temperature cannot be assumed in HRSGs
8.37 How to optimize temperature profiles in HRSGs
8.38 Efficiency of HRSGs according to ASME Power Test Code
8.39a Effect of fresh air fan size on HRSG performance
8.39b Performance of a multipressure HRSG in fresh air–fired mode
8.40 How to evaluate operating costs in HRSGs
8.41 Why economizer steaming occurs in gas turbine HRSGs
Copyright © 2003 Marcel Dekker, Inc.

8.42 Why water tube boilers are preferred to fire tube boilers for gas turbine
applications
8.43 Why 10% increase in surface area does not mean 10% more duty in
boilers or heat transfer equipment
8.44a Time required to heat up boilers
8.44b Transient heating of a superheater bundle
8.44c Transientresponseofawatertubeevaporatortocutoff inheatinputand
feedwater supply
8.44d Response of awater tube evaporator when steam demand increases and
feedwater supply is cut off
8.45a Parameters to be considered in testing performance of HRSGs
8.45b Evaluating HRSG performance from operating data
8.46 Estimatingboilingheattransfercoefficientandcriticalheatfluxinwater
tube boilers
8.47a Relating heat flux, steam pressure, quality, flow in water tube boilers
8.47b Estimating critical heat flux in fire tube boilers
8.47c Estimating critical heat flux in a fire tube boiler; correcting for bundle
geometry
8.48 Simplified approach to designing fire tube boilers
8.49 Simplified approach to designing water tube boilers
8.50 Estimating tube bundle size
8.51 Estimating thickness of insulation for flat and curvedsurfaces; effect of
wind velocity; estimating thickness to limit surface temperatures
8.52 Estimating surface temperature of given thickness of insulation; trial-
and-error procedure to determine casing temperature
8.53 Sizing insulation to prevent freezing; determining water dew point
8.54a Estimating heat loss from pipes for various insulation thicknesses
8.54b Estimating temperature drop of fluids in insulated piping
8.55 Optimumthicknessof insulation;life-cyclecosting;annualheatlossand
capitalized cost; annual heat loss if no insulation is used
8.56 Design of hot casing
8.57 Temperature of duct or stack wall with and without insulation
8.58 Effect of wind velocity, casing emissivity on heat loss
8.59a Checking for noise and vibration problems in heat transfer equipment
8.59b Determining natural frequency of vibration of a tube bundle
8.59c Computing acoustic frequency
8.59d Determining vortex shedding frequency
8.59e Checking for bundle vibrations
8.59f Checks for tube bundle vibration using damping and fluid elastic
instability criteria
8.60 Estimating specific heat, viscosity, and thermal conductivity for a gas
mixture
Copyright © 2003 Marcel Dekker, Inc.

8.61 Effect of gas analysis on heat transfer
8.62 Effect of gas pressure on heat transfer
8.63 Converting gas analysis from weight tovolume basis
8.64 Effect of gas pressure and analysis on design of fire tube boiler
8.01
Q:
How is the surface area of heat transfer equipment determined? What terms can
be neglected while evaluating the overall heat transfer coefficient in boilers,
economizers, and superheaters?
A:
The energy transferred in heat transfer equipment, Q, is given by the basic
equation
Q U A DT 1
¼ (cid:4) (cid:4) ð Þ
Also,
W Dh W Dh 2
h h ¼ c c ð Þ
where
A surface area, ft2
¼
W fluid flow, lb=h
¼
Dh change in enthalpy (subscripts h and c stand for hot and cold)
¼
DT corrected log-mean temperature difference, F
(cid:2)
U ¼ overall heat transfer coefficient, Btu=ft2h F
(cid:2)
¼
For extended surfaces, U can be obtained from [1]
1 A A
t ff t ff
U ¼hA þ i(cid:4)A þ oþ
i i i
A d d 1
t ln
A (cid:4)24K (cid:4) d þZh
w m i o
where
A surface area of finned tube, ft2=ft
A
t¼
tube inner surface area pd=12, ft2=ft
A i¼ average wall surface are ¼ a p i d d =24, ft2=ft
w¼ ¼ ð þ iÞ
K thermal conductivity of the tube wall, Btu=fth F
m¼ (cid:2)
d;d tube outer and inner diameter, in.
ff ;ff
i¼
fouling factors inside and outside the tubes, ft2h F=Btu
h
i
;h
o¼
tube-side and gas-side coefficients, Btu=ft2h F
(cid:2)
i o¼ (cid:2)
Z fin effectiveness
¼
If bare tubes are used instead of finned tubes, A pd=12.
t ¼
Copyright © 2003 Marcel Dekker, Inc.

Equation (3) can be simplified to
1 d 1 d d
ln
U ¼hd þh þ24K (cid:4) d
i i o m i
4
d ð Þ
ff ff
þ i(cid:4)d þ o
i
where h is the outside coefficient.
o
Now let us take the various cases.
Water Tube Boilers, Economizers, and Superheaters
The gas-side heat transfer coefficient h is significant; the other terms can be
o
neglected.Inatypicalbaretubeeconomizer,forexample,h 1500Btu=ft2h F,
ff andff 0:001ft2h F=Btu,andh 12Btu=ft2h F.d i ¼ 2.0in.,d 1.5i (cid:2) n.,
i o ¼ (cid:2) o ¼ (cid:2) ¼ i¼
and K 25Btu=fth F.
m¼ (cid:2)
Substituting into Eq. (4) yields
1 2:0 1 2:0 2
ln
U ¼1500 1:5þ12þ24 25(cid:4) 1:5
(cid:4) (cid:4)
2:0
0:001 0:001
þ (cid:4)1:5þ
0:0874
¼
Hence,
U 11:44Btu=ft2 h F
(cid:2)
¼
Thusweseethattheoverallcoefficientisclosetothegas-sidecoefficient,which
is the highest thermal resistance. The metal thermal resistance and the tube-side
resistance are not high enough to change the resistance distribution much.
However,inaliquid-to-liquidheat exchanger,all theresistanceswillbe of
the same order, and hence none of the resistances can be neglected.
Eveniffinnedtubeswereusedinthecaseabove,withA=A 9substituted
into Eq. (3), U 9.3Btu=ft2h F, which is close to h . Thu t s, i w ¼ hile trying to
¼ (cid:2) o
figureU foreconomizers,watertubeboilers,orgas-to-liquidheatexchangers,U
may be written as
U 0:8 to 0:9 h 5
¼ (cid:4) o ð Þ
Copyright © 2003 Marcel Dekker, Inc.

Fire Tube Boilers, Gas Coolers, and Heat Exchangers with Gas
Flow Inside Tubes with Liquid or Steam–Water Mixture on the
Outside
h islarge,on theorder of1000–1500Btu=ft2h F, whereash will beabout 10–
o (cid:2) i
12Btu=ft2h F. Again, using Eq. (4), it can be shown that
(cid:2)
d
U h i 6
(cid:10) i(cid:4) d ð Þ
Alltheotherthermalresistancescanbeseentobeverysmall,andU approaches
the tube-side coefficient h.
i
Gas-to-Gas Heat Exchangers (Example: Air Heater in Boiler
Plant)
In gas-to-gas heat transfer equipment, both h and h are small and comparable,
i o
while the other coefficients are high.
Assumingthath 10andh 15,andusingthetubeconfigurationabove,
o¼ i¼
1 2:0 1
0:001 9:6 10 4
(cid:3)
U ¼15 1:5þ10þ þ (cid:4)
(cid:4)
2
0:001 0:1922
þ (cid:4)1:5¼
or
U 5:2Btu=ft2 h F
(cid:2)
¼
Simplifying Eq. (4), neglecting the metal resistance term and fouling, we obtain
hd=d
U h i i 7
¼ o(cid:4)h hd=d ð Þ
oþ i i
Thus both h and h contribute to U.
o i
DT, the corrected log-mean temperature difference, can be estimated from
DT DT
DT F max(cid:3) min
¼ T (cid:4)ln DT =DT
ð max minÞ
where F is the correction factor for flow arrangement. For counterflow cases,
T
F 1.0. For other types of flow, textbooks may be referred to for F . It varies
T¼ T
from 0.6 to 0.95 [2]. DT and DT are the maximum and minimum terminal
max min
differences.
Copyright © 2003 Marcel Dekker, Inc.

In a heat exchanger the hotter fluid enters at 1000 Fand leaves at 400 F,
(cid:2) (cid:2)
whilethecolderfluidentersat250 Fandleavesat450 F.Assumingcounterflow,
(cid:2) (cid:2)
we have
DT 1000 450 550 F
max ¼ (cid:3) ¼ (cid:2)
DT 400 250 150 F
min ¼ (cid:3) ¼ (cid:2)
Then
550 150
DT (cid:3) 307 (cid:2) F
¼ln 550=150 ¼
ð Þ
In boiler economizers and superheaters, F could be taken as 1. In tubular air
T
heaters, F could vary from 0.8 to 0.9. If accurate values are needed, published
T
charts can be consulted [1,2].
8.02
Q:
How is the tube-side heat transfer coefficient h estimated?
i
A:
The widely used expression for h is [1]
i
Nu 0:023Re0:8 Pr0:4 8
¼ ð Þ
where the Nusselt number is
hd
Nu i i 9
¼12k ð Þ
the Reynolds number is
wd
Re 15:2 i 10
¼ m ð Þ
where w is the flow in the tube in lb=h, and the Prandtl number is
mC
Pr p 11
¼ k ð Þ
where
m viscosity, lb=fth
¼
C specific heat, Btu=lb F
p¼ (cid:2)
k thermal conductivity, Btu=fth F
(cid:2)
¼
all estimated at the fluid bulk temperature.
Copyright © 2003 Marcel Dekker, Inc.

Substituting Eqs. (9)–(11) into Eq. (8) and simplifying, we have
w0:8k0:6C0:4 w0:8C
h 2:44 p 2:44 12
i ¼ (cid:4) d1:8m0:4 ¼ (cid:4) d1:8 ð Þ
i i
where C is a factor given by
k0:6C0:4
C p
¼ m0:4
C is available in the form of charts for various fluids [1] as a function of
temperature. For air and flue gases, C may be taken from Table 8.1.
For hot water flowing inside tubes, Eq. (8) has been simplified and, for
t <300 F, can be written as [3]
(cid:2)
V0:8
h 150 1:55t 13
i ¼ð þ Þd0:2 ð Þ
i
where
V velocity, ft=s
¼
t water temperature, F
(cid:2)
¼
For very viscous fluids, Eq. (8) has to be corrected by the term involving
viscosities at tube wall temperature and at bulk temperature [1].
8.03a
Q:
Estimate h when 200lb=h of air at 800 F and atmospheric pressure flows in a
i (cid:2)
tube of inner diameter 1.75in.
TABLE8.1 Factor C for Air
and FlueGases
Temp( F) C
(cid:2)
200 0.162
400 0.172
600 0.180
800 0.187
1000 0.194
1200 0.205
Copyright © 2003 Marcel Dekker, Inc.

A:
Using Table 8.1 and Eq. (12), we have C 0.187.
¼
0:187
h 2:44 2000:8 11:55Btu=ft2 h F
i ¼ (cid:4) (cid:4)1:751:8 ¼ (cid:2)
where
w flow, lb=h
¼
d inner diameter, in.
i¼
For gases at high pressures, Ref. 1 gives the C values. (See also p. 531.)
8.03b
Q:
Inaneconomizer,50,000lb=hofwateratanaveragetemperatureof250 Fflows
(cid:2)
in a pipe of inner diameter 2.9in. Estimate h.
i
A:
Let us use Eq. (13). First the velocity has to be calculated. From Q5.07a,
V 0:05 wv=d2 :v, the specific volume of hot water at 250 F, is 0.017cuft=lb.
¼ ð iÞ (cid:2)
Then,
0:017
V 0:05 50;000 5:05ft=s
¼ (cid:4) (cid:4) 2:92 ¼
Hence, from Eq. (13),
5:050:8
h 150 1:55 250 1586Btu=ft2 h F
i ¼ð þ (cid:4) Þ(cid:4) 2:90:2 ¼ (cid:2)
8.03c
Q:
Estimate the heat transfer coefficient when 4000lb=h of superheated steam at
500psia and an average temperature of 750 F flows inside a tube of inner
(cid:2)
diameter 1.5in.
A:
Using Table 8.2, we see that C 0.318. From Eq (12)
¼
40000:8 0:318
h i ¼ 2:44 (cid:4) 1:5 (cid:4) 1:8 ¼ 285Btu=ft2 h (cid:2) F
If steam were saturated, C 0.383 and h 343Btu=ft2h F.
¼ i¼ (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.2 Factor C forSteam
Pressure(psia)
100 200 500 1000 2000
Saturation
Temperature( F) 0.282 0.310 0.383 0.498 0.8733
(cid:2)
400 0.2716 0.3059
500 0.2737 0.2909 0.3595
600 0.2813 0.2896 0.3228 0.413
700 0.2917 0.2965 0.3161 0.3586 0.5206
800 0.3050 0.3090 0.3206 0.3453 0.4214
900 0.3161 0.3197 0.3277 0.3477 0.3946
1000 0.3276 0.3302 0.3392 0.3531 0.386
8.04
Q:
How is the outside gas heat transfer coefficient h in boilers, air heaters,
o
economizers, and superheaters determined?
A:
The outside gas heat transfer coefficient h is the sum of the convective heat
o
transfer coefficient h and nonluminous heat transfer coefficient h .
c N
h h h 14
o ¼ cþ N ð Þ
Forfinnedtubes,h shouldbecorrectedforfineffectiveness.h isusuallysmall
o N
if the gas temperature is less than 800 Fand can be neglected.
(cid:2)
Estimating h for Bare Tubes
c
A conservative estimate of h for flow of fluids over bare tubes in in-line and
c
staggered arrangements is given by [1]
Nu 0:33Re0:6 Pr0:33 15
¼ ð Þ
Substituting, we have the Reynolds, Nusselt, and Prandtl numbers
Gd
Re 16
¼12m ð Þ
h d
Nu c 17
¼12k ð Þ
Copyright © 2003 Marcel Dekker, Inc.

and
mC
Pr p 18
¼ k ð Þ
where
G gas mass velocity, lb=ft2h
¼
d tube outer diameter, in.
¼
m gas viscosity, lb=fth
¼
k gas thermal conductivity, Btu=fth F
(cid:2)
¼
C gas specific heat, Btu=lb F
p¼ (cid:2)
All the gas properties above are to be evaluated at the gas film temperature.
Substituting Eqs. (16)–(18) into Eq. (15) and simplifying, we have
F
h 0:9G0:6 19
c ¼ d0:4 ð Þ
where
C0:33
F k0:67 p 20
¼ m0:27 ð Þ
FactorF hasbeencomputedforairandfluegases,andagoodestimateisgivenin
Table 8.3.
The gas mass velocity G is given by
W
G 12 g 21
¼ N L S d ð Þ
w ð T (cid:3) Þ
where
N number of tubes wide
w¼
S transverse pitch, in.
T¼
L tube length, ft
¼
W gas flow, lb=h
g¼
TABLE8.3 F Factor for Air
and FlueGases
Temp( F) F
(cid:2)
200 0.094
400 0.103
600 0.110
800 0.116
1000 0.123
1200 0.130
Copyright © 2003 Marcel Dekker, Inc.

Forquickestimates,gasfilmtemperaturet canbetakenastheaverageofgasand
f
fluid temperature inside the tubes.
Example
Determine the gas-side convective heat transfer coefficient for a bare tube
superheater tube of diameter 2.0in. with the following parameters:
Gas flow 150,000lb=h
¼
Gas temperature 900 F
(cid:2)
¼
Average steam temperature 500 F
(cid:2)
¼
Number of tubes wide 12
¼
Length of the tubes 10.5ft
¼
Transverse pitch 4.0in.
¼
Longitudinal pitch 3.5in. (staggered)
¼
Solution. Estimate G. From Eq. (21),
150;000
G 12 7142lb=ft2 h
¼ (cid:4)12 10:5 4 2 ¼
(cid:4) (cid:4)ð (cid:3) Þ
Using Table 8.3, at a film temperature of 700 F, F 0.113. Hence,
(cid:2)
¼
0:113
h 0:9 71420:6 15:8Btu=ft2 h F
c ¼ (cid:4) (cid:4) 20:4 ¼ (cid:2)
Because the gas temperature is not high, the h value will be low, so
N
U h h 15:8Btu=ft2 h F
(cid:10) o (cid:10) c ¼ (cid:2)
(Filmtemperaturemaybetakenastheaverageofgasandsteamtemperatures,for
preliminary estimates. If an accurate estimate is required, temperature drops
across the various thermal resistances as discussed in Q8.16a must be deter-
mined.)
The convective heat transfer coefficient obtained by the above method or
Grimson’smethodcanbemodifiedtoincludetheeffectofangleofattackaofthe
gas flowover the tubes. The correction factor F is 1 for perpendicular flowand
n
decreases as shown in Table 8.4 for other angles [1].
If, for example, h 15 and the angle of attack is 60 , then h
0:94 15 14:1Btu=ft2 c h ¼ F: (cid:2) c ¼
(cid:2)
(cid:4) ¼
TABLE8.4 Correction Factor forAngle ofAttack
a, deg 90 80 70 60 50 40 30 20 10
F 1.0 1.0 0.98 0.94 0.88 0.78 0.67 0.52 0.42
n
Copyright © 2003 Marcel Dekker, Inc.

8.05
Q:
How is the convective heat transfer coefficient for air and flue gases determined
using Grimson’s correlation?
A:
Grimson’s correlation, which is widely used for estimating h [1], is
c
Nu B ReN 22
¼ (cid:4) ð Þ
Coefficient B and power N are given in Table 8.5.
Example
150,000lb=h of flue gases having an analysis (vol%) of CO 12, H O 12,
2¼ 2 ¼
N 70, and O 6 flows over a tube bundle having 2in. OD tubes at 4in.
2¼ 2¼
square pitch. Tubes per row 18; length 10ft. Determine h if the fluid
¼ ¼ c
temperature is 353 F and average gas temperature is 700 F. The Appendix
(cid:2) (cid:2)
tables give the properties of gases.
At a film temperature of 0:5 353 700 526 F; C 0:2695;
(cid:4)ð þ Þ¼ (cid:2) p ¼
m 0:0642 and k 0.02344. Then mass velocity G is
¼ ¼
150;000
G 12 5000lb=ft2 h
¼ (cid:4)18 10 4 2 ¼
(cid:4) (cid:4)ð (cid:3) Þ
TABLE8.5 Grimson’s Valuesof B and N
S =d 1:25 S =d 1:5 S =d 2 S =d 3
T ¼ T ¼ T ¼ T ¼
S =d B N B N B N B N
L
Staggered
1.25 0.518 0.556 0.505 0.554 0.519 0.556 0.522 0.562
1.50 0.451 0.568 0.460 0.562 0.452 0.568 0.488 0.568
2.0 0.404 0.572 0.416 0.568 0.482 0.556 0.449 0.570
3.0 0.310 0.592 0.356 0.580 0.44 0.562 0.421 0.574
In-line
1.25 0.348 0.592 0.275 0.608 0.100 0.704 0.0633 0.752
1.50 0.367 0.586 0.250 0.620 0.101 0.702 0.0678 0.744
2.0 0.418 0.570 0.299 0.602 0.229 0.632 0.198 0.648
3.0 0.290 0.601 0.357 0.584 0.374 0.581 0.286 0.608
Copyright © 2003 Marcel Dekker, Inc.

From Table 8.5, for S =d S =d 2;B 0:229 and N 0:632, so
T ¼ L ¼ ¼ ¼
5000 2
Re (cid:4) 12;980
¼12 0:0642¼
(cid:4)
h 2
Nu 0:229 12;9800:632 91 c(cid:4)
¼ (cid:4) ¼ ¼12 0:02344
(cid:4)
or
h 12:8Btu=ft2 h F
c ¼ (cid:2)
8.06
Q:
Compare in-line versus staggered arrangements of plain tubes from the point of
view of heat transfer and pressure drop considerations. In a waste heat boiler
180,000lb=h of flue gases at 880 F are cooled to 450 F generating steam at
(cid:2) (cid:2)
150psig. The gas analysis is (vol%) CO 7, H O 12, N 75, and O 6.
2¼ 2 ¼ 2¼ 2¼
Tube OD 2in.; tubes=row 24; length 7.5ft. Compare the cases when tubes
¼ ¼ ¼
are arranged in in-line and staggered fashion with transverse pitch 4in. and
¼
longitudinal spacing varying from 1.5 to 3in.
A:
Using Grimson’s correlation, the convective heat transfer coefficient h was
c
computed for thevarious cases. The nonluminous coefficient was neglected due
to the low gas temperature. The surface area and the number of rows deep
requiredwerealsocomputedalongwithgaspressuredrop.Theresultsareshown
in Table 8.6.
180;000 12
Gas mass velocityG (cid:4) 6000lb=ft2 h
¼24 4 2 7:5¼
(cid:4)ð (cid:3) Þ(cid:4)
TABLE8.6 In-Line VersusStaggeredArrangement ofBare Tubes
S =d 1:5 S =d 2:0 S =d 3:0
L ¼ L ¼ L ¼
In-line Staggered In-line Staggered In-line Staggered
Heattransfercoeff. h 12.5 15.34 14.43 14.59 14.43 14.10
c
Friction factor f 0.0386 0.0785 0.0480 0.0785 0.0668 0.0785
No.of rowsdeep 79 65 69 68 69 70
Gas pressuredrop, 2.95 4.92 3.2 5.2 4.5 5.5
in.WC
Copyright © 2003 Marcel Dekker, Inc.

Average gas temperature 0.5 (880 450)=2 665 F, and film temp-
(cid:2)
¼ (cid:4) þ ¼
erature is about 525 F.
(cid:2)
C 0.2706, m 0.06479, k 0.02367 at gas film temperature and
p¼ ¼ ¼
C 0.2753 at the average gas temperature.
p¼
6000 2
Re (cid:4) 15;434
¼12 0:06479¼
(cid:4)
Duty Q 180,000 0.99 0.2753 (8807450) 21MMBtu=h
¼ (cid:4) (cid:4) (cid:4) ¼
Saturation temperature 366 F.
(cid:2)
¼
880 366 450 366
DT log-mean temperature difference ð (cid:3) Þ(cid:3)ð (cid:3) Þ
¼ ¼ln 880 366 = 450 366
½ð (cid:3) Þ ð (cid:3) Þ(cid:5)
237 F
(cid:2)
¼
With S =d 1.5 in-line, we have the values for B and N from Table 8.5:
L ¼
B 0:101 and N 0:702
¼ ¼
Hence
2
Nu 0:101 15;4340:702 88:0 h
¼ (cid:4) ¼ ¼ c(cid:4)12 0:02367
(cid:4)
or
h 12:5
c ¼
Because other resistances are small, U 0:95h 11:87Btu=ft2 h F.
¼ c ¼ (cid:2)
Hence
21 106
A (cid:4) 7465 3:14 2 24 7:5N =12
¼237 11:87¼ ¼ (cid:4) (cid:4) (cid:4) d
(cid:4)
or the number of rows deep N 79.
d¼
The friction factor f, using the method discussed in Q7.27, is
f 15;434 0:15 0:044 0:08 1:5 0:0386
(cid:3)
¼ ð þ (cid:4) Þ¼
Average gas density 0:0347lb=ft3
¼
0:0386
Gas pressure drop 9:3 10 10 60002 79 2:95in:WC
(cid:3)
¼ (cid:4) (cid:4) (cid:4) (cid:4)0:0347¼
The calculations for the other cases are summarized in Table 8.6.
1. The staggered arrangement of bare tubes does not have a significant
impact on the heat transfer coefficient when the longitudinal spacing
exceeds 2, which is typical in steam generators. Ratios lower than 1.5
are not used, owing to potential fouling concerns or low ligament
efficiency.
Copyright © 2003 Marcel Dekker, Inc.

2. The gas pressure drop is much higher for the staggered arrangement.
Hence, with bare tube boilers the in-line arrangement is preferred.
However, with finned tubes, the staggered arrangement is comparable
with the in-line and slightly better in a few cases. This is discussed
later.
8.07a
Q:
How is the nonluminous radiation heat transfer coefficient evaluated?
A:
Inengineeringheattransferequipmentsuchasboilers,firedheaters,andprocess
steam superheaters where gases at high temperatures transfer energy to fluid
inside tubes, nonluminous heat transfer plays a significant role. During combus-
tion offossil fuels such ascoaloil, orgas—triatomic gases—for example, water
vapor, carbon dioxide, and sulfur dioxide—are formed, which contribute to
radiation. The emissivity pattern of these gases has been studied by Hottel, and
chartsareavailabletopredictgasemissivityifgastemperature,partialpressureof
gases, and beam length are known.
Netinterchangeofradiationbetweengasesandsurroundings(e.g.,awallor
tube bundle or a cavity) can be written as
Q
s e T4 a T4 23
A ¼ ð g g (cid:3) g oÞ ð Þ
where
e emissivity of gases at T
g¼ g
a absorptivity at T
g¼ o
T absolute temperature of gas, R
g¼ (cid:2)
T absolute temperature of tube surface, R
o¼ (cid:2)
e is given by
g
e e Ze De 24
g ¼ cþ w(cid:3) ð Þ
a is calculated similarly at T . Z is the correction factor for thewater pressure,
g o
and De is the decrease in emissivity due to the presence of water vapor and
carbon dioxide.
Although it is desirable to calculate heat flux by (23), it is tedious to
estimatea attemperature T .Considering thefactthatT4 willbemuch smaller
g o o
Copyright © 2003 Marcel Dekker, Inc.

than T4, with a very small loss of accuracy we can use the following simplified
g
equation, which lends itself to further manipulations.
Q
se T4 T4 h T T 25
A ¼ gð g (cid:3) oÞ¼ Nð g(cid:3) oÞ ð Þ
The nonluminous heat transfer coefficient h can be written as
N
T4 T4
h se g (cid:3) o 26
N ¼ g T T ð Þ
g(cid:3) o
To estimate h , partial pressures of triatomic gases and beam length L are
N
required. L is a characteristic dimension that depends on the shape of the
enclosure. For a bundle of tubes interchanging radiation with gases, it can be
shown that
S S 0:785d2
L 1:08 T L(cid:3) 27a
¼ (cid:4) d ð Þ
Listakenapproximatelyas3.4–3.6timesthevolumeofthespacedividedbythe
surface area of the heat-receiving surface. For a cavity of dimensions a;b and c,
3:4 abc 1:7
L (cid:4) 27b
¼2 ab bc ca ¼1=a 1=b 1=c ð Þ
ð þ þ Þ þ þ
In the case of fire tube boilers, L d.
¼ i
e can be estimated using Figs. 8.1a–8.1d, which give e ;e ;Z, and De,
g c w
respectively. For purposes of engineering estimates, radiation effects of SO can
2
betakenassimilartothoseofCO .Hence,partialpressuresofCO andSO can
2 2 2
be added and Fig. 8.1 used to get e .
c
Example 1
Determine the beam length L if S 5in., S 3.5in., and d 2in.
T¼ L¼ ¼
Solution.
5 3:5 0:785 4
L 1:08 (cid:4) (cid:3) (cid:4) 7:8in:
¼ (cid:4) 2 ¼
Example 2
Inafiredheaterfiringawastegas,CO influegases 12%andH O 16%.The
2 ¼ 2 ¼
gasesflowoverabankoftubesintheconvectivesectionwheretubesarearranged
as in Example 1 (hence L 7.8). Determine h if t 1650 F and t 600 F.
¼ N g ¼ (cid:2) o ¼ (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.1a Emissivity ofcarbon dioxide.(From Ref1.)
Solution.
7:8
P L 0:12 0:078atmft
c ¼ (cid:4) 12 ¼
7:8
P L 0:16 0:104atmft
w ¼ (cid:4) 12 ¼
In Fig. 8.1a at T 1650 460 2110 R and P L 0:078;e 0:065. In
g ¼ð þ Þ¼ (cid:2) c ¼ c ¼
Fig.8.1b,atT 2110 RandP L 0:104;e 0:05.InFig.8.1c,correspond-
g ¼ (cid:2) w ¼ w ¼
ing to P P =2 1:16=2 0:58 and P L 0:104;Z 1:1. In Fig. 8.1d,
ð þ wÞ ¼ ¼ w ¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.1b Emissivityof watervapor. (FromRef1.)
corresponding to P = P P 0:16=0:28 and P P L 0:182; De
w ð cþ wÞ¼ ð cþ wÞ ¼ ¼
0:002. Hence,
e 0:065 1:1 0:05 0:002 0:118
g ¼ þð (cid:4) Þ(cid:3) ¼
Using Eq. (26) with the Boltzmann constant s 0:173 10 8,
(cid:3)
¼ (cid:4)
21104 10604
h N ¼ 0:173 (cid:4) 10 (cid:3) 8 (cid:4) 0:118 (cid:4) 2110 (cid:3) 1060
(cid:3)
3:6Btu=ft2 h F
(cid:2)
¼
Thus, h can be evaluated for gases.
N
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.1c,d (c) Correction factor for emissivity of water vapor. (d) Correction
termdue topresenceof watervaporand carbondioxide. (FromRef 1.)
Copyright © 2003 Marcel Dekker, Inc.

8.07b
Q:
Can gas emissivity be estimated using equations?
A:
Gas emissivity can be obtained as follows. h is given by Eq. (26),
N
T4 T4
h se g (cid:3) o
N ¼ g T T
g(cid:3) o
where
s Stefan–Boltzmann constant 0.173 10 8
(cid:3)
¼ ¼ (cid:4)
T and T gas and tube outer wall temperature, R
g o¼ (cid:2)
e , gas emissivity, is obtained from Hottel’s charts or from the expression
g
[1]
e 0:9 1 e KL 28a
g ¼ (cid:4)ð (cid:3) (cid:3) Þ ð Þ
0:8 1:6p 1 0:38T =1000
K ð þ wÞ(cid:4)ð (cid:3) g Þ p p 28b
¼ p p L (cid:4)ð cþ wÞ ð Þ
ð cþ wÞ
T isinK.Listhebeapmffiffilffiffieffiffinffiffigffiffitffiffihffiffiffiiffiffinffiffiffimffiffi eters,andp andp arethepartialpressures
g c w
of carbon dioxide and water vapor in atm. L, the beam length, can be estimated
for a tube bundle by Eq. (27a),
S S 0:785d2
L 1:08 T (cid:4) L(cid:3)
¼ (cid:4) d
S and S are the transverse pitch and longitudinal pitch. Methods of estimating
T L
p and p are given in Chapter 5.
c w
Example
Inaboilersuperheaterwithbaretubes,theaveragegastemperatureis1600 Fand
(cid:2)
the tube metal temperature is 700 F. Tube size is 2.0in., and transverse pitch
(cid:2)
S longitudinal pitch S 4.0in. Partial pressures of water vapor and carbon
T¼ L¼
dioxide are p 0.12, p 0.16. Determine the nonluminous heat transfer
w¼ c¼
coefficient.
From Eq. (27a), the beam length L is calculated.
4 4 0:785 2 2
L 1:08 (cid:4) (cid:3) (cid:4) (cid:4)
¼ (cid:4) 2
6:9in: 0:176m
¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

Using Eq. (28b) with T (1600732)=1.8 273 1114K, we obtain
g¼ þ ¼
0:8 1:6 0:12 1 0:38 1:114
K ð þ (cid:4) Þ(cid:4)ð (cid:3) (cid:4) Þ 0:28
¼ p0:28 0:176 (cid:4)
(cid:4)
0:721
¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
From Eq. (28a),
e 0:9 1 exp 0:721 0:176 0:107
g ¼ (cid:4)½ (cid:3) ð(cid:3) (cid:4) Þ(cid:5)¼
Then, from Eq. (26),
20604 11604
h N ¼ 0:173 (cid:4) 0:107 (cid:4) 10 (cid:3) 8 (cid:4) 1600 (cid:3) 700
(cid:3)
3:33Btu=ft2 h F
(cid:2)
¼
8.08a
Q:
How is heat transfer in a boiler furnace evaluated?
A:
Furnace heat transfer is a complex phenomenon, and a single formula or
correlation cannot be prescribed for sizing furnaces of all types. Basically, it is
an energy balance between two fluids—gas and a steam–water mixture. Heat
transferinaboilerfurnaceispredominantlyradiation,partlyduetotheluminous
part of the flame and partly due to nonluminous gases. A general approximate
expression can be written for furnace absorption using an energy approach:
Q A e e s T4 T4
F ¼ p w f ð g (cid:3) oÞ 29
W LHV W h ð Þ
¼ f (cid:3) g e
Gastemperature(T )isdefinedinmanyways;someauthorsdefineitasthe
g
exit gas temperature itself. Some put it as the mean of the theoretical flame
temperature and t . However, plant experience shows that better agreement
e
betweenmeasuredandcalculatedvaluesprevailswhent t 300to400 F[1].
g ¼ cþ (cid:2)
The emissivity of a gaseous flame is evaluated as follows [1]:
e b 1 e KPL 30
f ¼ ð (cid:3) (cid:3) Þ ð Þ
b characterizes flame-filling volumes.
b 1.0 for nonluminous flames
¼
0.75 for luminous sooty flames of liquid fuels
¼
0.65 for luminous and semiluminous flames of solid fuels
¼
L beam length, m
¼
Copyright © 2003 Marcel Dekker, Inc.

K attenuationfactor,whichdependsonfueltypeandpresenceofashand
¼
its concentration. For a nonluminous flame it is
0:8 1:6p
K þ w 1 0:38T =1000 p p 28b
¼ p p L ð (cid:3) e Þð cþ wÞ ð Þ
ð cþ wÞ
For a semilpumffiffiffiiffinffiffiffioffiffiuffiffiffisffiffiffiflffiffiffiaffiffimffiffi e, the ash particle size and concentration enter into the
calculation:
0:8 1:6p
K þ w 1 0:38T =1000 p p
¼ p p L ð (cid:3) e Þð cþ wÞ
ð cþ wÞ
pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi1ffiffiffiffiffi 1=3
7m 28c
þ d2 T2 ð Þ
(cid:1) m(cid:4) e(cid:2)
where
d the mean effective diameter of ash particles, in mm
m¼
d 13 for coals ground in ball mills
m¼
16 for coals ground in medium- and high-speed mills
¼
20 for combustion of coals milled in hammer mills
m ¼ ash concentration in g=N m3
¼
T furnace exit temperature, K
e¼
For a luminous oil or gas flame,
1:6T
K e 0:5 28d
¼ 1000 (cid:3) ð Þ
p andp arepartialpressuresofwater vaporandcarbondioxideinthefluegas.
w c
Theaboveequations giveonlyatrend.Awidevariation could existdueto
the basic combustion phenomenon itself. Again, the flame does not fill the
furnacefully.Unfilledportionsaresubjectedtogasradiationonly,theemissivity
of which (0.15–0.30) is far below that of the flame. Hence, e decreases.
f
Godridge reports that in a pulverized coal-fired boiler, emissivity varied as
follows with respect to location [3]:
Excess air 15% 25%
Furnace exit 0.6 0.5
Middle 0.7 0.6
Also,furnacetubescoatedwithferricoxidehaveemissivities,e ,oftheorderof
w
0.8, depending on whether a slag layer covers them. Soot blowing changes e
w
considerably. Thus, only an estimate of e and e can be obtained, which varies
f w
with type of unit, fuel, and operation regimes.
Copyright © 2003 Marcel Dekker, Inc.

Toillustratetheseconcepts,afewexamplesareworkedout.Thepurposeis
only to show the effect of variables like excess air and heat release rates on
furnace absorption and furnace exit gas temperature.
Example 1
Determinetheapproximatefurnaceexitgastemperatureofaboilerwhennetheat
input is about 2000 106Btu=h, of which 1750 106Btu=h is due to fuel and
(cid:4) (cid:4)
the rest is due to air. HHVand LHVof coals fired are 10,000 and 9000Btu=lb,
respectively, and a furnace heat release rate of 80,000Btu=ft2h (projected area
basis) has been used. The values e and e may be taken as 0.6 and 0.5,
w f
respectively; 25% is the excess air used. Water-wall outer temperature is 600 F.
(cid:2)
Ash content in coal is 10%.
Solution.
Q LHV
80;000 W
A ¼ ¼ f A
p p
From combustion calculation methods discussed in Chapter 5, using 1MMBtu
fired basis, we have the following ratio of flue gas to fuel:
W 760 1:24 104 10
g (cid:4) (cid:4) 1
W ¼ 106 þ (cid:3)100
f
10:4lb=lb
¼
Q A e e s T4 T4 W LHV W h
¼ P w f ð g (cid:3) oÞ¼ f (cid:3) g e
Dividing throughout by W gives
f
A W
p e e s T4 T4 LHV g h
W w f ð g (cid:3) oÞ¼ (cid:3)W e
f f
A =W LHV=80;000 0:1125
p f ¼ ¼
Assume t 1900 F. Then
e¼ (cid:2)
C 0:3Btu=lb F
pm ¼ (cid:2)
t 1900 300 2200 F 2660 R
g ¼ þ ¼ (cid:2) ¼ (cid:2)
Letusseeiftheassumedt iscorrect.SubstitutingforA =W ;e ;e ;s;T ;T in
e p f w f g e
the above equation, we have (LHS left-hand side; RHS right-hand side)
¼ ¼
LHS 0:1125 0:6 0:5 0:173
¼ (cid:4) (cid:4) (cid:4)
26:64 10:64 2850
(cid:4)ð (cid:3) Þ¼
RHS 9000 10:4 1900 0:3 3072
¼ð (cid:3) (cid:4) (cid:4) Þ¼
Copyright © 2003 Marcel Dekker, Inc.

These do not tally, sowe try t 1920 F. Neglect the effect of variation in C :
e¼ (cid:2) pm
LHS 0:1125 0:6 0:5 26:84 10:64
¼ (cid:4) (cid:4) (cid:4)ð (cid:3) Þ
0:173 2938
(cid:4) ¼
RHS 9000 1920 0:3 10:4 3009
¼ (cid:3) (cid:4) (cid:4) ¼
These agree closely, so furnace exitgas temperature is around 1920 F. Note that
(cid:2)
the effect of external radiation to superheaters has been neglected in the energy
balance.Thismaygiverisetoanerrorof1.5–2.5%int ,butitsomissiongreatly
e
simplifies the calculation procedure. Also, losses occurring in the furnace were
omitted to simplify the procedure. The error introduced is quite low.
Example 2
Itisdesiredtouseaheatloadingof100,000Btu=ft2hinthefurnaceinExample
1.Otherfactorssuchasexcessairandemissivitiesremainunaltered.Estimatethe
furnace exit gas temperature.
Solution.
Q LHV
100;000 W
A ¼ ¼ f A
p p
A LHV
p 0:09
W ¼100;000¼
f
w
g 10:4; t 2000 F; t 2300 F
w ¼ e ¼ (cid:2) g ¼ (cid:2)
f
C 0:3Btu=lb F; T 2300 460 2760 R
pm ¼ (cid:2) g ¼ þ ¼ (cid:2)
LHS 0:09 0:6 0:5 0:173
¼ (cid:4) (cid:4) (cid:4)
27:64 10:64 2664
(cid:4)ð (cid:3) Þ¼
RHS 9000 10:4 2000 0:3 2760
¼ð (cid:3) (cid:4) (cid:4) Þ¼
From this it is seen that t will be higher than assumed. Let
e
t 2030 F; T 2790 R
e ¼ (cid:2) g ¼ (cid:2)
Then
LHS 0:09 0:6 0:5 0:173
¼ (cid:4) (cid:4) (cid:4)
27:9 4 10:6 4 2771
(cid:4)½ð Þ (cid:3)ð Þ (cid:5)¼
RHS 9000 10:4 2030 0:3 2667
¼ (cid:3) (cid:4) (cid:4) ¼
Hence, t will lie between 2000 and 2030 F, perhaps 2015 F.
e (cid:2) (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

Theexerciseshowsthattheexitgastemperatureinanysteamgeneratorwill
increaseasmoreheatinputisgiventoit;thatis,thehighertheloadoftheboiler,
the higher the exit gas temperature. Example 3 shows the effect of excess air on
t .
e
Example 3
What will be the furnace exit gas temperature when 40% excess air is used
insteadof25%,heatloading remainingatabout100,000Btu=ft2hinthefurnace
mentioned in earlier examples?
Solution.
Q LHV A
100;000 W ; p 0:09
A ¼ ¼ f A W ¼
p p f
W 760 1:4 104
g (cid:4) (cid:4) 0:9 11:54lb=lb
W ¼ 106 þ ¼
f
t 1950 F; C 0:3Btu=lb F
e ¼ (cid:2) pm ¼ (cid:2)
T 1950 300 460 2710 R
g ¼ þ þ ¼ (cid:2)
LHS 0:09 0:6 0:5 0:173
¼ (cid:4) (cid:4) (cid:4)
27:1 4 10:6 4 2460
(cid:4)½ð Þ (cid:3)ð Þ (cid:5)¼
RHS 9000 11:54 1950 0:3 2249
¼ (cid:3)ð (cid:4) (cid:4) Þ¼
These nearly tally; hence, t is about 1950 F, compared to about 2030 F in
e (cid:2) (cid:2)
Example 2. The effect of the higher excess air has been to lower t .
e
Example 4
Ife e 0:5 insteadof0.3,whatwillbetheeffectont whenheatloadingis
100 w ,0 (cid:4) 00B f t ¼ u=ft2h and excess air is 40%? e
Solution. Let
t 1800 F; T 1800 300 460 2560 R
e ¼ (cid:2) g ¼ þ þ ¼ (cid:2)
LHS 0:09 0:5 0:173 25:6 4 10:6 4
¼ (cid:4) (cid:4) (cid:4)½ð Þ (cid:3)ð Þ (cid:5)
3245
¼
RHS 9000 11:54 1800 0:3 2768
¼ (cid:3)ð (cid:4) (cid:4) Þ¼
Try
t 1700 F; T 2460 R
e ¼ (cid:2) g ¼ (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

Then
LHS 0:09 0:5 0:173 24:6 4 10:6 4
¼ (cid:4) (cid:4) (cid:4)½ð Þ (cid:3)ð Þ (cid:5)
2752
¼
RHS 9000 11:54 1700 0:3 3115
¼ (cid:3)ð (cid:4) (cid:4) Þ¼
Try
t 1770 F; T 2530 R
e ¼ (cid:2) g ¼ (cid:2)
Then
LHS 3091; RHS 2872
¼ ¼
Hence, t will be around 1760 F. This example shows that when surfaces are
e (cid:2)
cleaner and capable of absorbing more radiation, t decreases.
e
Inpractice,furnaceheattransferisnotevaluatedassimplyasshownabove
because of the inadequacy of accurate data on soot emissivity, particle size,
distribution, flame size, excess air, presence and effect of ash particles, etc.
Hence, designers develop data based on field tests. Estimating t is the starting
e
point for the design of superheaters, reheaters, and economizers.
Some boiler furnaces are equipped with tilting tangential burners, whereas
somefurnaceshaveonlyfrontorrearnontiltablewallburners.Thelocationofthe
burners affects t significantly. Hence, in these situations, correlations with
e
practical site datawouldhelp inestablishing furnace absorption and temperature
profiles. (See also p. 112, Chapter 3.)
A promising technique for predicting furnace heat transfer performance is
thezonemethodofanalysis.Itisassumedthatthepatternoffluidflow,chemical
heatrelease,andradiatinggasconcentrationareknown,andequationsdescribing
conservation of energy within the furnace are developed. The furnace is divided
into many zones, and radiation exchange calculations are carried out.
8.08b
Q:
How is heat transfer evaluated in unfired furnaces?
A:
Radiantsectionsusingpartiallyorfullywater-cooledmembranewalldesignsare
used to cool gas streams at high gas temperatures (Fig. 8.2). They generate
saturated steam and may operate in parallel with convective evaporators if any.
The design procedure is simple and may involve an iteration or two. The higher
the partial pressures of triatomic gases, the higher will be the nonluminous
radiation and hence the duty.
Copyright © 2003 Marcel Dekker, Inc.

Figure 8.2 Radiant furnaceina watertubeboiler.
If a burner is used as in the radiant section of a furnace-fired HRSG, the
emissivity of the flame must also be considered. As explained elsewhere [8],
radiant sections are necessary to cool the gases to below the softening points of
anyeutecticspresentsoastoavoidbridgingorslaggingattheconvectionsection.
They are also required to cool gases to a reasonable temperature at the super-
heater if it is used.
Example
200,000lb=h of flue gases at 1800 F has to be cooled to 1600 F in a radiant
(cid:2) (cid:2)
section of a waste heat boiler of cross section 9ft 11ft. Saturated steam at
(cid:4)
200psigisgenerated.Determinethefurnacelengthrequired.Fluegasanalysisis
(vol%) CO 8, H O 18, N 72, O 2. Assume a length of 25ft and that
2¼ 2 ¼ 2¼ 2¼
the furnace is completely water-cooled.
Surface area for cooling 11 9 2 25 1000ft2
¼ð þ Þ(cid:4) (cid:4) ¼
volume
Beam length 3:4
¼ (cid:4)surface area
9 11 25
3:4 (cid:4) (cid:4) 7:1ft 2:15m
¼ (cid:4)2 11 9 9 25 11 25 ¼ ¼
(cid:4)ð (cid:4) þ (cid:4) þ (cid:4) Þ
Copyright © 2003 Marcel Dekker, Inc.

Average gas temperature 1700 F 1200K. Partial pressure of
(cid:2)
¼ ¼
CO 0.08, and that of H O 0.18. Using Eq. (28b),
2¼ 2 ¼
0:26
K 0:8 1:6 0:18 1 0:38 1:2 0:2053
¼ð þ (cid:4) Þð (cid:3) (cid:4) Þ(cid:4) 0:26 2:15 0:5 ¼
ð (cid:4) Þ
Gas emissivitye 0:9 1 e 0:2053 2:16 0:3223
g ¼ (cid:4)ð (cid:3) (cid:3) (cid:4) Þ¼
Let the average surface temperature of the furnace be 420 F (saturation
(cid:2)
temperature plus a margin). Then the energy transferred is
Q 0:173 0:9 0:3223 21:64 8:84 1000 10:63MMBtu=h
r ¼ (cid:4) (cid:4) (cid:4)ð (cid:3) Þ(cid:4) ¼
Required duty 200;000 0:99 0:32 200 12:67MMbtu=h
¼ (cid:4) (cid:4) (cid:4) ¼
where0.32isthegasspecificheat.Hencethefurnaceshouldbelonger.Thebeam
lengthandhencethegasemissivitywillnotchangemuchwithchangeinfurnace
length; therefore one may assume that the furnace length required
¼
(12.67=10.63) 25 29.8 or 30ft.
(cid:4) ¼
If the performances at other gas conditions are required, a trial-and-error
procedureiswarranted.Firsttheexitgastemperatureisassumed;thentheenergy
transferred is computed as shown above and compared with the assumed duty.
8.09a
Q:
How is the distribution of external radiation to tube bundles evaluated? Discuss
the effect of tube spacing.
A:
Tubebanksareexposedtodirectorexternalradiationfromflames,cavities,etc.,
inboilers.Dependingonthetubepitch,theenergyabsorbedbyeachrowoftubes
varies,withthefirstrowfacingtheradiationzonereceivingthemaximumenergy.
It is necessary to compute the energy absorbed by each row, particularly in
superheaters,becausethecontributionoftheradiationcanresultinhightubewall
temperatures.
The following formula predicts the radiation to the tubes [8].
d d d S 2 S
a 3:14 sin 1 1 31
(cid:3)
¼ 2S(cid:3)S 2 S þsffiffiffiffidffiffiffiffiffiffiffi(cid:3)ffiffiffiffiffiffiffi(cid:3)d3 ð Þ
(cid:1) (cid:2) (cid:1) (cid:2)
4 5
whereaisthefractionofenergyabsorbedbythefirstrow.Thesecondrowwould
then absorb 1 a a; the third row, 1 a 1 a a a; and so on.
ð (cid:3) Þ f (cid:3)½ þð (cid:3) Þ (cid:5)g
Copyright © 2003 Marcel Dekker, Inc.

Example
1MMBtu=h of energy from a cavity is radiated to a superheater tube bank that
has2in.ODtubesatapitchof8in.Iftherearesixrows,estimatethedistribution
of energy to each row.
Solution. Substituting d 2, S 8 into Eq. (31), we have
¼ ¼
2=8 2 2 8
a 3:14 sin 1 p4 4 1
(cid:3)
¼ 2 (cid:3)8 8 þ (cid:4) (cid:3) (cid:3)2
(cid:1) (cid:2) (cid:6) (cid:1) (cid:2) (cid:7)
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
0:3925 0:25 0:2526 p15 4 0:361
¼ (cid:3) ð þ (cid:3) Þ¼
ffiffiffiffiffi
Hence the first row absorbs 0.361MMBtu=h.
The second row would receive (170.361) 0.361 0.231 or 0.231
(cid:4) ¼
MMBtu=h.
The third row receives [17(0.361 0.231)] 0.361 0.147MMBtu=h.
þ (cid:4) ¼
The fourth row, [17(0.361 0.231 0.147)] 0.361 0.094MM
þ þ (cid:4) ¼
Btu=h, and so on.
It can be seen that the first row receives the maximum energy and the
amount lessens as the number of rows increases. For a tube pitch S of 4in.,
a 0.6575.Thefirstrowreceives0.6575MMBtu=h;thesecond,0.225MBtu=h;
¼
andthethird,0.077MMBtu=h.Henceifthetubepitchissmall,alargeamountof
energyisabsorbedwithinthefirsttwotothreerows,resultinginhighheatfluxin
those tubes and consequently high tube wall temperatures. Hence it is better to
useawidepitchwhentheexternalradiationislargesothattheradiationisspread
over more tubes and the intensity is not concentrated within two or three tubes.
Screen tubes in boilers and fired heaters perform this function.
8.09b
Q:
Asootblowerlanceisinsertedinaboilerconvectionsectionwherehotfluegases
at 2000 Fare flowing around the tubes. If the water wall enclosure is at 400 F,
(cid:2) (cid:2)
what will be the lance temperature? Assume that the heat transfer coefficient
between the flue gas and the lance is 15Btu=ft2h F and the emissivity of the
(cid:2)
lance and the water wall tubes is 0.9.
Copyright © 2003 Marcel Dekker, Inc.

A:
Theenergytransferredbetweenthefluegasesandlanceandfromthelancetothe
water wall enclosure in Btu=ft2h is given by
Q h 2000 T
¼ cð (cid:3) Þ
0:173 0:9 0:9 T 460 4 400 460 4 10 8
(cid:3)
¼ (cid:4) (cid:4) (cid:4)½ð þ Þ (cid:3)ð þ Þ (cid:5)(cid:4)
where
T lance temperature, F
(cid:2)
0.1 ¼ 73 10 8 is the radiation constant
(cid:3)
(cid:4)
Emissivity of lance and enclosure 0.9
¼
Actually,atrial-and-errorprocedureisrequiredtosolvetheaboveequation.
However, it may be shown that at T 1250 F, both sides balance and
(cid:2)
Q 11,250Btu=ft2h. At low loads, when ¼ h 5 and with other parameters
¼ c¼
remaining the same, what will be the lance temperature? It can be shown to be
about 970 Fand Q 5150btu=ft2h.
(cid:2)
¼
Hencejustasathermocouplereadsalowertemperatureduetotheradiation
totheenclosure,thelancealsowillnotreachthegastemperature.Itstemperature
will be lower than that of the gas.
8.10
Q:
Determine the size of a fire tubewaste heat boiler required to cool 100,000lb=h
offluegasesfrom1500 Fto500 F.Gasanalysisis(vol%)CO 12,H O 12,
(cid:2) (cid:2) 2¼ 2 ¼
N 70, and O 6; gas pressure is 5in.WC. Steam pressure is 150psig, and
2¼ 2¼
feedwater enters at 220 F. Tubes used are in 2in. OD 1.77in. ID; fouling
(cid:2)
factors are gas-side fouling factor (ft); 0.002ft2h F (cid:4) =Btu and steam-side
(cid:2)
ff 0.001ft2h F=Btu. Tube metal thermal conductivity 25Btu=fth F. Steam-
(cid:2) (cid:2)
sid ¼ e boiling heat transfer coefficient 2000Btu=ft2 F. A ¼ ssume that heat losses
(cid:2)
¼
and margin 2% and blowdown 5%.
¼ ¼
A:
UseEq.(4)tocomputetheoverallheattransfercoefficient,andthenarriveatthe
size from Eq. (1).
1 d d ln d =d 1
o ff ff o d ð o iÞ
U ¼dh þ oþ i d þ o 24K þh
i i i m o
Copyright © 2003 Marcel Dekker, Inc.

h, thetube-side coefficient, isactuallythe sum ofa convectiveportion h plus a
i c
nonluminous coefficient h : h is obtained from Q8.04:
n c
C
h 2:44 w0:8
c ¼ (cid:4) (cid:4)d1:8
i
Attheaveragegastemperatureof1000 F,thegaspropertiescanbeshowntobe
(cid:2)
C 0.287Btu=lb F, m 0.084lb=fth, and k 0.0322Btu=fth F. Hence,
p¼ (cid:2) ¼ ¼ (cid:2)
0:287 0:4
C 0:0322 0:6 0:208
¼ 0:084 (cid:4)ð Þ ¼
(cid:1) (cid:2)
Boiler dutyQ 100;000 0:98 0:287 1500 500
¼ (cid:4) (cid:4) (cid:4)ð (cid:3) Þ
28:13 106 Btu=h
¼ (cid:4)
Enthalpies of saturated steam, saturated water, and feedwater from steam tables
are1195.5,338,and188Btu=lb,respectively.Theenthalpyabsorbedbysteamis
then (1195.57188) 0.05 (3387188) 1015Btu=lb, where 0.05 is the
þ (cid:4) ¼
blowdown factor corresponding to 5% blowdown.
Hence,
28:13 106
Steam generation (cid:4) 27;710lb=h
¼ 1015 ¼
In order to compute h, the flow per tube w is required. Typically w ranges from
i
100 to 200lb=h for a 2in. tube. Let us start with 600 tubes; hence w
¼
100,000=600 167lb=h.
¼
1670:8
h 2:44 0:208 10:9Btu=ft2 h F
c ¼ (cid:4) (cid:4) 1:77 1:8 ¼ (cid:2)
ð Þ
Thenonluminouscoefficientisusuallysmallinfiretubeboilersbecausethebeam
length corresponds to the tube inner diameter. However, the procedure used in
Q8.07 can also be used here. Let us assume that it is 0.45Btu=ft2h F. Then
(cid:2)
h 10:90 0:45 11:35Btu=ft2 h F
i ¼ þ ¼ (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

Let us compute U. Because it is based on tube outside surface, let us call it U .
o
1 2=1:77 2
0:001 0:002
U ¼ 11:35 þ þ (cid:4)1:77
o
2 2
ln 0:0005
þ 1:77 (cid:4)24 25þ
(cid:1) (cid:2) (cid:4)
0:10 0:001 0:00226 0:00041 0:0005
¼ þ þ þ þ
0:10417
¼
Hence, U 9.6Btu=ft2h F.
The o v ¼ arious resistan (cid:2) ces in ft2h F=Btu are
(cid:2)
Gas-side heattransfer 0.10
Gas-side fouling 0.00226
Metalresistance 0.00041
Steam-side fouling 0.001
Steam-side heattransfer 0.0005
IfU iscomputedon thebasis of tube inner surfacearea,then U isgivenby the
i
expression
A U A U
i(cid:4) i ¼ o(cid:4) o
Hence,
2
U 9:6 10:85Btu=ft2 h F
i ¼ (cid:4)1:77¼ (cid:2)
Log-mean temperature difference is
1500 366 500 366
DT ð (cid:3) Þ(cid:3)ð (cid:3) Þ 468 (cid:2) F
¼ln 1500 366 = 500 366 ¼
½ð (cid:3) Þ ð (cid:3) Þ(cid:5)
Hence
28:13 106
A (cid:4) 6261ft2
o ¼ 468 9:6 ¼
(cid:4)
L
3:14 2 600
¼ (cid:4) (cid:4) (cid:4)12
so required length L of the tubes 19.93ft. Use 20ft. Then
¼
20
A 3:14 2 600 6280ft2
o ¼ (cid:4) (cid:4) (cid:4)12¼
A 5558ft2
i ¼
Copyright © 2003 Marcel Dekker, Inc.

Let us compute the gas pressure drop using Eq. (12) of Chapter 7.
v
DP 93 10 6 w2f L
g ¼ (cid:4) (cid:3) (cid:4) ed5
i
Friction factor f depends on tube inner diameter and can be taken as 0.02. The
equivalentlengthL canbeapproximatedbyL 5d toincludethetubeinletand
e þ i
exit losses.
Specific volume v obtained as 1=density, or v 1=r. Gas density at the
¼
averagegastemperatureof1000 Fisr 39=1460 0.0267lb=cuft.Therefore,
(cid:2) g¼ ¼
DP 93 10 6 1672 0:02
g ¼ (cid:4) (cid:3) (cid:4) (cid:4)
20 5 1:77
þ (cid:4) 3:23in:WC
(cid:4)0:0267 1:77 5 ¼
(cid:4)ð Þ
This isonlyone design. Severalvariablessuchas tube size and mass flowcould
be changed to arrive at several options that could be reviewed for optimum
operating and installed costs.
8.11
Q:
Whatistheeffectoftubesizeandgasvelocityonboilersize?Issurfaceareathe
sole criterion for boiler selection?
A:
Surface area should not be used as the sole criterion for selecting or purchasing
boilers, because tube size and gas velocity affect this variable.
Shown in Table 8.7 are the design options for the same boiler duty using
differentgasvelocitiesandtubesizes;theproceduredescribedinQ8.10wasused
toarriveattheseoptions.Thepurposebehindthisexampleistobringoutthefact
that surface area can vary by as much as 50% for the same duty.
1. As the gas velocity increases, the surface area required decreases,
which is obvious.
2. The smaller the tubes, the higher the heat transfer coefficient for the
same gas velocity, which also decreases the surface area.
3. For the same gas pressure drop, the tube length is smaller if the tube
size is smaller. This fact helps when we try to fit a boiler into a small
space.
4. For the same tube size, increasing the gas velocity results in a longer
boiler, a greater gas pressure drop, but smaller surface area.
In the case of water tube boilers, more variables such as tube spacing and
in-line or staggered arrangement in addition to gas velocity and tube size can
affect surface area. This is discussed elsewhere.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.7 Effect ofTube Sizeand GasVelocity onFire TubeBoiler Design
Tubesize 1.75 1.521 2 1.773 2.5 2.238
(cid:4) (cid:4) (cid:4)
Velocity, ft=s 109 141 166 110 140 165 109 140 166
Tubes 1100 850 725 800 630 535 510 395 335
Length,ft 19 20 21 22.5 24 25 29.5 31.5 33
Surfacearea, ft2 8318 6766 6059 8351 7015 6205 8811 7286 6474
U, Btu=ft2h F 9.74 11.78 13.25 9.6 11.43 12.89 9.15 11.02 12.43
(cid:2)
Pressuredrop in.WC 2.5 4.4 6.3 2.6 4.4 6.2 2.5 4.3 6.2
Gas flow 110,000lb=h; inlet temperature 1450 F; exit temperature 500 F; steam pressure 300psig; feedwater in 230 F;
¼ ¼ (cid:2) ¼ (cid:2) ¼ ¼ (cid:2)
blowdown 5%;steam 28,950lb=h;gasanalysis(vol%):CO 7;H O 12;N 75;O 6;boilerduty 29.4MMBtu=h.
¼ ¼ 2¼ 2 ¼ 2¼ 2¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

8.12
Q:
How is the tube wall temperature in fire tube boilers evaluated? Discuss the
importance of heat flux.
A:
To compute the tube wall temperatures, heat flux must be known.
q heat flux outside tubes U t t Btu=ft2 h
o ¼ ¼ o(cid:4)ðg(cid:3) iÞ
Similarly, q (heat flux inside the tube) would be U t t . However, heat
i i(cid:4)ðg(cid:3) iÞ
flux outside the tubes is relevant in fire tube boilers because boiling occurs
outside the tubes, whereas in water tube boilers the heat flux inside the tubes
wouldberelevant.Ahighheatfluxcanresultinaconditioncalleddeparturefrom
nucleate boiling (DNB), which will result in overheating of the tubes. It is
preferable to keep the actual maximum heat flux below the critical heat flux,
which varies from 150,000 to 250,000Btu=ft2h depending on steam quality,
pressure, and tube condition [1].
An electrical analogy can be used in determining the tube wall tempera-
tures.Heatfluxisanalogoustocurrent,electricalresistancetothermalresistance,
and voltage drop to temperature drop. Using the example worked in Q8.10, we
have that at average gas conditions the product of current (heat flux) and
resistance (thermal resistance) gives the voltage drop (temperature drop):
q heat flux 9:6 1000 366 6086Btu=ft2 h
o ¼ ¼ (cid:4)ð (cid:3) Þ¼
Temperature drop across gas film 6086 0:1 609 F
(cid:2)
¼ (cid:4) ¼
Temperature drop across gas-side fouling 6086 0:00226 14 F
(cid:2)
¼ (cid:4) ¼
Temperature drop across tube wall 6086 0:00041 3 F
(cid:2)
¼ (cid:4) ¼
Temperature drop across steam-side fouling 6086 0:001 6 F
(cid:2)
¼ (cid:4) ¼
Temperature drop across steam film 6085 0:0005 3 F
(cid:2)
¼ (cid:4) ¼
Hence,
Average inside tube wall temperature 1000 609 14 377 F
(cid:2)
¼ (cid:3) (cid:3) ¼
Outside tube wall temperature 377 3 347 F:
(cid:2)
¼ (cid:3) ¼
The same results are obtained working from the steam side.
Outside tube wall temperature 366 6 3 375 F
(cid:2)
¼ þ þ ¼
Copyright © 2003 Marcel Dekker, Inc.

Onecanalsocomputethemaximumtubewalltemperaturebyobtainingtheheat
flux at the hot gas inlet end.
8.13
Q:
What is the effect of scale formation on tube wall temperatures?
A:
Ifnonsolublesaltssuchascalciumormagnesiumsaltsorsilicaarepresentinthe
feedwater, they can deposit in a thin layer on tube surfaces during evaporation,
thereby resulting in higher tube wall temperatures.
Table 8.8 lists the thermal conductivity k of a few scales. Outside fouling
factor ff can be obtained if the scale information is available.
o
thickness of scale
ff
o ¼ conductivity
Let us use the same example as in Q8.10 and check the effect of ff on boiler
o
duty and tube wall temperatures. Let a silicate scale of thickness 0.03in. be
formed. Then,
0:03
ff 0:05ft2 h F=Btu
o ¼ 0:6 ¼ (cid:2)
TABLE8.8 Thermal Conductivities ofScale
Materials
Material Thermal conductivity
[(Btu=ft2h F)=in.]
(cid:2)
Analcite 8.8
Calcium phosphate 25
Calcium sulfate 16
Magnesiumphosphate 15
Magnetic ironoxide 20
Silicate scale(porous) 0.6
Boiler steel 310
Firebrick 7
Insulatingbrick 0.7
Copyright © 2003 Marcel Dekker, Inc.

Assume that other resistances have not changed. (Because of different duty and
gas temperature profile, the gas-side heat transfer coefficient will be slightly
different. However, for the sake of illustration, we neglect this.) We have
1
0:10 0:00226 0:00041 0:05 0:0005
U ¼ þ þ þ þ
o
0:15317
¼
Hence, U 6.52Btu=ft2h F
o¼ (cid:2)
Heat fluxq 6:52 1000 366 4133Btu=ft2 h
o ¼ (cid:4)ð (cid:3) Þ¼
Temperature drop across outside steam film 0:0005 4133
¼ (cid:4)
2 F
(cid:2)
¼
Temperature drop across steam-side fouling layer or scale 4133 0:05
¼ (cid:4)
207 F
(cid:2)
¼
Temperature drop across tube wall 4133 0:00041
¼ (cid:4)
2 F
(cid:2)
¼
We see that average tube wall temperature has risen to 366 2 207
þ þ þ
2 577 F from an earlier value of about 375 F. Scale formation is a serious
(cid:2) (cid:2)
¼
problem.Notethattheheatfluxisnowlower,butthatdoesnothelp.Atthefront
end, where the heat flux is higher, the tubes would be much hotter.
Now let us check the effect on boiler duty. It can be shown [1,8] that
t t UA
ln g1(cid:3) sat 32
t t ¼W C h ð Þ
g2(cid:3) sat g(cid:4) p(cid:4) lf
where h is the heat loss factor. If 2% losses are assumed, then h 0.98.
lf lf¼
We know that U 6.52, A 6280, t 1500, t 366. Hence,
o¼ o¼ g1¼ sat¼
1500 366 6:52 6280
ln (cid:3) (cid:4)
t 366 ¼100;000 0:98 0:287
g2(cid:3) (cid:4) (cid:4)
1:456
¼
or
1500 366
(cid:3) 4:29
t 366 ¼
g2(cid:3)
Hence t 630 F compared to 500 Fearlier. The reason for t going up is the
g2¼ (cid:2) (cid:2) g2
lower U caused by scale formation.
o
Hence new duty 100,000 0.98 0.287 (15007630) 24.47 106
¼ (cid:4) (cid:4) (cid:4) ¼ (cid:4)
Btu=h.Thedecreaseindutyis28.13724.47 3.66MMBtu=h.Evenassuming
¼
Copyright © 2003 Marcel Dekker, Inc.

a modest energy cost of $3=MMBtu, the annual loss due to increased fouling is
3.66 3 8000 $87,800. The steam production in turn gets reduced.
(cid:4) (cid:4) ¼
Plant engineers should check the performance of their heat transfer
equipment periodically to see if the exit gas temperature rises for the same
inletgasflowandtemperature.If itdoes,thenitislikelyduetofoulingoneither
thegasorsteamside,whichcanbechecked.Foulingonthegassideaffectsonly
the duty and steam production, but fouling on the steam side increases the tube
wall temperature in addition to reducing the duty and steam production.
To ensure that variations inexitgas temperature arenot dueto fouling but
are due to changes in gas flowor temperature, one can use simulation methods.
Forexample,if,forthesamegasflow,theinletgastemperatureis1800 F,wecan
(cid:2)
expect the exit gas temperature to rise. Under clean conditions, this can be
estimated using the equation (32)
1500 366 1800 366
500 (cid:3) 366 ¼ t (cid:3) 366 ; or t g2 ¼ 535 (cid:2) F
(cid:3) g2(cid:3)
Nowif,inoperation,theexitgastemperaturewere570–600 F,thenfoulingcould
(cid:2)
be suspected; but if the gas temperature were only about 535 F, this would only
(cid:2)
be due to the increased gas inlet temperature. Similarly, one can consider the
effect of gas flow and saturation temperature.
8.14
Q:
How is the size of a water tube boiler determined?
A:
Thestartingpointinthedesignofanevaporator(Fig.8.3)istheestimationofthe
overallheattransfercoefficientU.Thecross-sectionaldatasuchasthenumberof
tubes wide, spacing, and length of tubes are assumed. From the duty and log-
mean temperature difference, the surface area is obtained. Then the number of
rowsdeepisestimated.Tubewalltemperaturecalculationsandgaspressuredrop
evaluation then follow. A computer program is recommended to perform these
tedious calculations, particularly if several alternatives have to be evaluated.
Example
200,000lb=hofcleanfluegasfromanincineratormustbecooledfrom1100 Fto
(cid:2)
600 F in a bare tube evaporator. Steam pressure 250psig saturated. Feedwater
(cid:2)
¼
temperature 230 F. Blowdown 5%. Fouling factors on steam- and gas-side
(cid:2)
0.001ft2h ¼ F=Btu. Gas analy ¼ sis (vol%): CO 7; H O 12; N 75;
¼ (cid:2) 2 ¼ 2 ¼ 2 ¼
O 6. Let heat loss from casing 1%.
2 ¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.3 Boiler evaporatorbundle.
Solution: Use 2 1.773 in carbon steel tubes; number wide 24;
(cid:4) ¼
length 10ft; tube spacing 4in. square.
¼ ¼
Average gas temperature 0:5 1100 600 850 F
(cid:2)
¼ (cid:4)ð þ Þ¼
Steam temperature inside tubes 406 F. Assume tubewall temperature 410 F
(cid:2) (cid:2)
¼ ¼
(this should be checked again later).
Film temperature 0:5 850 410 630 F
(cid:2)
¼ (cid:4)ð þ Þ¼
Gas properties at film temperature are (from Appendix) C 0.2741,
p¼
m 0.0693, k 0.0255
¼ ¼
C at average gas temperature 0.282
p ¼
Duty Q 200,000 0.99 0.282 (11007600) 27.92MMBtu=h
¼ (cid:4) (cid:4) (cid:4) ¼
Steam enthalpy change (1201.77199) 0.05 (381.47199)
¼ þ (cid:4) ¼
1011.82 Btu=lb
Copyright © 2003 Marcel Dekker, Inc.

Hence
106
Steam generation 27:92 27;600lb=h
¼ (cid:4)1011:82¼
200;000 12
Gas mass velocityG (cid:4) 4167lb=ft2 h
¼24 12 4 2 ¼
(cid:4) (cid:4)ð (cid:3) Þ
4167 2
Reynolds number Re Gd=12m (cid:4) 10;021
¼ ¼12 0:0693¼
(cid:4)
Using Grimson’s correlation,
Nu 0:229 10;021 0:632 77:3
¼ (cid:4)ð Þ ¼
The convective heat transfer coefficient
k 0:0255
h Nu 12 77:3 12 11:83Btu=ft2 h F
c ¼ (cid:4) d ¼ (cid:4) (cid:4) 2 ¼ (cid:2)
Let us compute the nonluminous heat transfer coefficient h . Partial
N
pressures of CO and H O are 0.06 and 0.12, respectively; beam length
2 2
L 1.08 (4 470.785 4)=2 6.95in. 0.176m.
¼ (cid:4) (cid:4) (cid:4) ¼ ¼
Average gas temperature 850 F 727K
(cid:2)
¼ ¼
Using Eq. (28b),
0:8 1:6 0:12 1 0:38 0:727 0:19
K ð þ (cid:4) Þ(cid:4)ð (cid:3) (cid:4) Þ(cid:4) 0:746
¼ 0:19 0:176 0:5 ¼
ð (cid:4) Þ
Gas emissivitye 0:9 1 e 0:746 0:176 0:1107
g ¼ (cid:4)ð (cid:3) (cid:3) (cid:4) Þ¼
Assuming that the tube wall is at 420 F (to be checked later)
(cid:2)
13:14 8:84
h N ¼ 0:173 (cid:4) 0:9 (cid:4) 0:1107 (cid:4) 1310 (cid:3) 880 ¼ 0:94Btu=ft2 h (cid:2) F
(cid:3)
Usingaconservativeboilingheattransfercoefficientof2000Btu=ft2handatube
thermal conductivity of 25Btu=fth F; we have
(cid:2)
1 1
0:001 0:001
U ¼0:94 11:83þ þ
þ
2 2 ln 2=1:773
2 ð Þ
(cid:4)1:773þ1:773 2000þ 24 25
(cid:4) (cid:4)
0:0782 0:001 0:0011 0:000565 0:0004 0:0813
¼ þ þ þ þ ¼
Copyright © 2003 Marcel Dekker, Inc.

or
U 12:3Btu=ft2 h F
(cid:2)
¼
1100 406 600 406
Log-mean temperature difference ð (cid:3) Þ(cid:3)ð (cid:3) Þ
¼ln 1100 406 = 600 406
½ð (cid:3) Þ ð (cid:3) Þ(cid:5)
393 F
(cid:2)
¼
27:92 106
Surface area requiredA (cid:4) 5776ft2
¼ 12:3 393 ¼
(cid:4)
A 3:14 2 N 24 12=12 5776; orN 38:4
¼ (cid:4) (cid:4) d (cid:4) (cid:4) ¼ d ¼
Use 40 rows deep. Surface provided 6016ft2. Let us estimate the gas pressure
¼
drop.
28:2 492
Gas densityr (cid:4) 0:0295lb=ft3
¼359 460 850 ¼
(cid:4)ð þ Þ
Friction factorf 10;020 0:15 0:044 0:08 2 0:0512
(cid:3)
¼ (cid:4)ð þ (cid:4) Þ¼
0:0512
DP 9:3 10 10 41672 40 1:12in:WC
g ¼ (cid:4) (cid:3) (cid:4) (cid:4) (cid:4)0:0295¼
The average heat flux on tube ID basis is
q 12:3 850 406 2=1:773 6160Btu=ft2 h
¼ (cid:4)ð (cid:3) Þ(cid:4) ¼
Temperature drop across inside fouling layer 6160 0.001 62 F
(cid:2)
¼ (cid:4) ¼
Temperature drop across inside film coefficient 6160=2000 3.1 F
(cid:2)
¼ ¼
Drop across tube wall 0.0004 1.773 6160=2 2.2 F
(cid:2)
¼ (cid:4) (cid:4) ¼
Hence tube outer wall temperature 406 6.2 3.1 2.2 418 F. Since this
(cid:2)
¼ þ þ þ ¼
is close to the assumed value another iteration is not necessary.
Notethatthisisonlytheaveragetubewalltemperature.Themaximumheat
flux is at the gas inlet, and one has to redo these calculations to obtain the
maximumtubewalltemperature.Acomputerprogramwouldhelpspeedupthese
calculations.
8.15a
Q:
Howistheoff-designperformanceofaboilerevaluated?Predicttheperformance
of the boiler designed earlier under the following conditions: Gas flow
¼
230,000lb=h; gas inlet temperature 1050 F; steam pressure 200psig. Gas
(cid:2)
¼ ¼
analysis remains the same.
Copyright © 2003 Marcel Dekker, Inc.

A:
Performancecalculationsaremoreinvolvedthandesigncalculations,becausewe
do not know the gas exit temperature. The NTU method discussed in Q8.30
minimizes the number of iterations. However, for an evaporator, a simple
procedure exists for predicting the performance.
The boiler duty Q is given by the expression
UA t t
Q W C t t ð1(cid:3) 2Þ 33
¼ g pð1(cid:3) 2Þ¼ln t t = t t ð Þ
½ð1(cid:3) sÞ ð2(cid:3) sÞ(cid:5)
where
t ;t gas inlet and exit temperatures, F
1 2¼ (cid:2)
t saturation temperature, F
s¼ (cid:2)
W gas flow, lb=h (correcting for heat loss factor)
g¼
C gas specific heat at average gas temperature, Btu=lb F
U
p¼
overall heat transfer coefficient, Btu=ft2h F
(cid:2)
(cid:2)
A ¼ surface area, ft2
¼
Simplifying, we have
t t UA
ln 1(cid:3) s 34
t t ¼W C ð Þ
2(cid:3) s g p
First we have to estimate U. Assuming 580 Fas the gas exit temperature,
(cid:2)
average gas temperature 815 Fand average film temperature 613 F.
(cid:2) (cid:2)
¼ ¼
m 0:06875; k 0:0252; C 0:2735
¼ ¼ p ¼
C at average gas temperature 0.28Btu=lb F
p ¼ (cid:2)
12
G 230;000 4791lb=ft2 h
¼ (cid:4)24 12 2¼
(cid:4) (cid:4)
4791 2
Re (cid:4) 11;615
¼12 0:06875¼
(cid:4)
Nu 0:229 11;6150:632 84:9
¼ (cid:4) ¼
or
h 84:8 12 0:0252=2 12:9Btu=ft2 h F
c ¼ (cid:4) (cid:4) ¼ (cid:2)
Thenonluminousheattransfercoefficientmaybecomputedasbeforeandshown
to be 0.895Btu=ft2h F.
(cid:2)
1
1= 0:895 12:9 0:001 0:0011 0:000565 0:0004 0:0756
U ¼ ð þ Þþ þ þ þ ¼
U 13:2Btu=ft2 h F
(cid:2)
¼
Copyright © 2003 Marcel Dekker, Inc.

Using Eq. (34) with saturation temperature of 388 F, we have
(cid:2)
1050 388 13:2 6016
ln (cid:3) (cid:4) 1:2455
t 388 ¼230;000 0:99 0:28¼
2(cid:3) (cid:4) (cid:4)
or
t 578 F
2 ¼ (cid:2)
From eq. (32)
Q 230;000 0:99 0:28 1050 578 30:0MMBtu=h
¼ (cid:4) (cid:4) (cid:4)ð (cid:3) Þ¼
Steam generation 29;770lb=h
¼
The tube wall temperature and gas pressure drop may be computed as
before.Itmaybeshownthatthegaspressuredropis1.5in.WCandthetubewall
temperature is 408 F. Thus off-design performance is predicted for the evapora-
(cid:2)
tor. With an economizer or superheater, more calculations are involved as the
water or steam temperature changes. Also, the duty is affected by the configura-
tionoftheexchanger,whethercounterflow,parallelflow,orcrossflow.TheNTU
method discussed in Q8.29 and Q8.30 may be used to predict the off-design
performance of such an exchanger.
8.15b
Q:
Discuss the logic for determining the off-design performance of a water tube
waste heat boiler with the configuration shown in Fig. 8.4.
A:
In the design procedure one calculates the size of the various heating surfaces
such as superheaters, evaporators, and economizers by the methods discussed
earlierbasedontheequationA Q= U DT .Inthissituation,thedutyQ,log-
¼ ð (cid:4) Þ
mean temperature difference DT, and overall heat transfer coefficient U are
known or can be obtained easily for a given configuration.
In the off-design procedure, which is more involved, the purpose is to
predict the performance of a given boiler under different conditions of gas flow,
inlet gas temperature, and steam parameters. In these calculations several trial-
and-error steps are required before arriving at the final heat balance and duty,
because the surface area is now known. The procedure is discussed for a simple
case, configuration 1ofFig.8.4,whichconsists ofascreen section, superheater,
evaporator, and economizer.
1. Assume a steam flow W based on gas conditions.
s
2. Solve for the screen section, which is actually an evaporator, by using
the methods discussed in Q8.15a.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.4 Configurationsforwater tubeboiler.
3. Solve for the superheater section, either using the NTU method or by
trial and error. Assume a value for the duty and compute the exit
gas=steam temperatures and then DT.
Assumed dutyQ W C T T h
a ¼ g pð gi(cid:3) goÞ lf
W h h
¼ sð so(cid:3) siÞ
where
h ;h enthalpies of steam at exit and inlet
so si¼
T ;T gas inlet and exit temperatures.
gi go¼
ComputeU.ThentransferreddutyisQ U A DT.IfQ andQ areclose,
t ¼ (cid:4) (cid:4) a t
then the assumed duty and gas=steam temperatures are correct; proceed to the
next step. Otherwise assume another duty and repeat step 3.
Copyright © 2003 Marcel Dekker, Inc.

4. Solve for the evaporator section as in step 1. No trial and error is
required, because the steam temperature is constant.
5. Solvefortheeconomizerasinstep3.Assumeavalueforthedutyand
then compute exit gas=water temperatures, DT, and Q. Iteration
t
proceeds until Q and Q match. The NTU method can also be used
a t
to avoid several iterations.
6. The entireHRSGduty isnowobtained by adding the transferred duty
of the four sections. The steam flow is corrected based on the actual
total duty and enthalpy rise.
7. Iftheactualsteamflowfromstep6equalsthatassumedinstep1,then
the iterations are complete and the solution is over; if not, go back to
step 1 with the revised steam flow.
Thecalculationsbecomemorecomplexifsupplementaryfiringisaddedto
generate a desired quantity of steam; the gas flow and analysis change as the
firing temperature changes, and the calculations for U and the gas=steam
temperature profile must take this into consideration. Again, if multipressure
HRSGsareinvolved,thecalculationsareevenmorecomplexandcannotbedone
without a computer.
8.16a
Q:
Determine the tube metal temperature for the case of a superheater under the
following conditions:
Average gas temperature 1200 F
(cid:2)
¼
Average steam temperature 620 F
(cid:2)
Outside gas heat transfer co ¼ efficient 15Btu=ft2h F
(cid:2)
Steam-side coefficient 900Btu=ft2h ¼ F
(cid:2)
¼
(Estimationofsteam andgasheattransfer coefficientsisdiscussedinQ8.03and
Q8.04.)
Tube size 2 0.142in. (2in. OD and 0.142in. thick)
¼ (cid:4)
Tube thermal conductivity 21Btu=fth F (carbon steel)
(cid:2)
¼
(Thermal conductivity of metals can be looked up in Table 8.9.)
A:
Becausetheaverageconditionsaregivenandtheaveragetubemetaltemperature
is desired, we must have the parameters noted above under the most severe
conditions of operation—the highest gas temperature, steam temperature, heat
flux, and so on.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.9 Thermal Conductivity ofMetals, Btu=ft h
(cid:2)
F
Temperature( F)
(cid:2)
Material 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500
Aluminum(annealed)
Type1100-0 126 124 123 122 121 120 118
Type3003-0 111 111 111 111 111 111 111
Type3004-0 97 98 99 100 102 103 104
Type6061-0 102 103 104 105 106 106 106
Aluminum(tempered)
Type1100(all tempers) 123 122 121 120 118 118 118
Type3003(all tempers) 96 97 98 99 100 102 104
Type3004(all tempers) 97 98 99 100 102 103 104
Type6061-T4and T6 95 96 97 98 99 100 102
Type6063-T5and T6 116 116 116 116 116 115 114
Type6063-T42 111 111 111 111 111 111 111
Castiron 31 31 30 29 28 27 26 25
Carbonsteel 30 29 28 27 26 25 24 23
Carbonmoly(1%) steel 29 28 27 26 25 25 24 23
2
Chromemoly steels
1%Cr,1% Mo 27 27 26 25 24 24 23 21 21
2
21% Cr,1%Mo 25 24 23 23 22 22 21 21 20 20
4
5%Cr,1% Mo 21 21 21 20 20 20 20 19 19 19
2
12%Cr 14 15 15 15 16 16 16 16 17 17 17 18
Austeniticstainlesssteels
18%Cr, 8%Ni 9.3 9.8 10 11 11 12 12 13 13 14 14 14 15 15
25%Cr, 20%Ni 7.8 8.4 8.9 9.5 10 11 11 12 12 13 14 14 15 15
(continued)
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.9 Continued
Temperature( F)
(cid:2)
Material 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500
Admiralty metal 70 75 79 84 89
Naval brass 71 74 77 80 83
Copper(electrolytic) 225 225 224 224 223
Copperand nickel alloys
90% Cu,10%Ni 30 31 34 37 42 47 49 51 53
80% Cu,20%Ni 22 23 25 27 29 31 34 37 40
70% Cu,30%Ni 18 19 21 23 25 27 30 33 37
30% Cu,70%Ni (Monel) 15 16 16 16 17 18 18 19 20 20
Nickel 38 36 33 31 29 28 28 29 31 33
Nickel-chrome-iron 9.4 9.7 9.9 10 10 11 11 11 12 12 12 13 13 13
Titanium(gr B) 10.9 10.4 10.5
Copyright © 2003 Marcel Dekker, Inc.

Let us use the concept of electrical analogy, in which the thermal and
electrical resistances, heat flux and current, and temperature difference and
voltage are analogous. For the thermal resistance of the tube metal,
d d 2 2
R ln ln
m ¼24K d ¼24 21(cid:4) 1:72
m i (cid:4)
0:0006ft2 h F=Btu
(cid:2)
¼
Outside gas film resistance
1
R 0:067ft2 h F=Btu
o ¼15¼ (cid:2)
1
Inside film resistanceR 0:0011ft2 hr F=Btu
i ¼900¼ (cid:2)
Total resistanceR 0:067 0:0006 0:0011
t ¼ þ þ
0:0687ft2 h F=Btu
(cid:2)
¼
Hence
1200 620
Heat fluxQ (cid:3) 8443Btu=ft2 h
¼ 0:0687 ¼
Temperature drop across the gas film 8443 0:067 565 F
(cid:2)
¼ (cid:4) ¼
Temperature drop across the tube metal 8443 0:0006 5 F
(cid:2)
¼ (cid:4) ¼
Temperature drop across steam film 8443 0:0011 9:3 F
(cid:2)
¼ (cid:4) ¼
(Here we have applied the electrical analogy, where voltage drop is equal to the
product of current and resistance.) Hence,
1200 565 620 9:3
Average tube metal temperature ð (cid:3) Þþð þ Þ 632 (cid:2) F
¼ 2 ¼
We note that the tube metal temperature is close to the tube-side fluid tempera-
ture. This is because the tube-side coefficient is high compared to the gas heat
transfer coefficient. This trend would prevail in equipment such as water tube
boilers, superheaters, economizers, or any gas–liquid heat transfer equipment.
An approximation of the tube metal temperature for bare tubes in a gas–
liquid or gas–gas heat transfer device is
h
t t i t t 35
m ¼ o(cid:3)h h ðo(cid:3) iÞ ð Þ
iþ o
Copyright © 2003 Marcel Dekker, Inc.

where
h; h heattransfercoefficients insideandoutside thetubes,Btu=ft2h F
i o¼ (cid:2)
t; t fluid temperatures inside and outside, F
i o¼ (cid:2)
8.16b
Q:
In a boiler air heater, h 9, h 12, t 200 F, and t 800 F. Estimate the
o¼ i¼ i¼ (cid:2) o¼ (cid:2)
average tube wall temperature t .
m
A:
Using Eq. (35), we have
12
t 800 800 200 457 F
m ¼ (cid:3)12 9(cid:4)ð (cid:3) Þ¼ (cid:2)
þ
8.17
Q:
How is the performance of fire tube and water tube boilers evaluated? Can we
infer the extent offouling from operational data? Awater tubewaste heat boiler
as shown in Fig. 8.5 generates 10,000lb=h of saturated steam at 300psia when
thegasflowis75,000lb=handgastemperaturesinandoutare1000 Fand500 F.
(cid:2) (cid:2)
Whatshouldthesteam generationandexitgastemperaturebewhen50,000lb=h
of gas at 950 Fenters the boiler?
(cid:2)
A:
It can be shown as discussed in Q8.15a that in equipment with a phase change
[1,8],
t t UA
ln 1(cid:3) sat
t t ¼W C
2(cid:3) sat g p
which was given there as Eq. (34).
Forfiretubeboilers,theoverallheattransfercoefficientisdependentonthe
gascoefficientinsidethetubes;thatis,U isproportionaltoW0:8.Inawatertube
g
boiler, U is proportional to W0:6. Substituting these into Eq. (34) gives us the
g
following.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.5 Sketchof (a)fire tubeand (b)watertubeboilers.
For fire tube boilers:
t t K
ln 1(cid:3) sat 1 36
t t ¼W0:2 ð Þ
2(cid:3) sat g
For water tube boilers:
t t K
ln 1(cid:3) sat 2 37
t t ¼W0:4 ð Þ
2(cid:3) sat g
As long as the fouling is not severe, Eqs. (36) and (37) predict the exit gas
temperaturescorrectly.Ift isgreaterthanpredicted,wecaninferthatfoulinghas
2
occurred. Also, if the gas pressure drop across the boiler is more than the
calculated value (see Chap. 7 for pressure drop calculations), we can infer that
fouling has taken place.
Copyright © 2003 Marcel Dekker, Inc.

Calculate K from Eq. (37). t 417 from the steam tables (see the
2 sat¼
Appendix).
1000 417
K ln (cid:3) 75;000 0:4 173
2 ¼ 500 417 (cid:4)ð Þ ¼
(cid:1) (cid:3) (cid:2)
Let us predict the exit gas temperature when W 50,000.
g¼
950 417 50;000 0:4
ln (cid:3) ð Þ 2:29
t 417 ¼ 173 ¼
(cid:1) 2(cid:3) (cid:2)
950 417
t 2 ¼ 417 þ exp (cid:3) 2:29 ¼ 471 (cid:2) F
ð Þ
Now the actual exit gas temperature is 520 F, which means that the fouling is
(cid:2)
severe.
The energy loss due to fouling is
Q 50;000 0:26 520 471
¼ (cid:4) (cid:4)ð (cid:3) Þ
0:63 106 Btu=h
¼ (cid:4)
If energy costs $3=MMBtu, the annual loss of energy due to fouling will be
3 0.63 8000 $15,120 (assuming 8000 hours of operation a year).
(cid:4) (cid:4) ¼
8.18
Q:
When and where are finned tubes used? What are their advantages over bare
tubes?
A:
Finned tubes are used extensively in boilers, superheaters, economizers, and
heatersfor recoveringenergyfromcleangasstreamssuchasgasturbineexhaust
orfluegasfromcombustionofpremiumfossilfuels.Iftheparticulateconcentra-
tioninthegasstreamisverylow,finnedtubeswithalowfindensitymaybeused.
However,thechoiceoffinconfiguration,particularlyincleangasapplications,is
determined by several factors such as tube-side heat transfer coefficient, overall
size, cost, and gas pressure drop, which affects the operating cost.
Solid and serrated fins (Fig. 8.6) are used in boilers and heaters. Finned
surfacesareattractivewhentheratiobetweentheheattransfercoefficientsonthe
outside of the tubes to that inside is very small. In boiler evaporators or
economizers, the tube-side coefficient could be in the range of 1500–
3000Btu=ft2h F, and the gas-side coefficient could be in the range of 10–
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

Figure 8.6 Solid and serratedfins.
20Btu=ft2h F. A large fin density or a large ratio of external to internal surface
(cid:2)
area is justified in this case. As the ratio between the outside and inside
coefficients decreases, the effectiveness of using a large ratio of external to
internalsurfaceareasdecreases.Forexample,insuperheatersorhighpressureair
heaters, where the tube-side coefficient could be in the range of 30–
300Btu=ft2h F, it does not pay to use a large fin surface; in fact, it is counter-
(cid:2)
productive, as will be shown later. A moderate fin density such as two or three
finsperinchwouldbeadequate,whereasforeconomizersorevaporators,fiveor
even six fins per inch may be justified if cleanliness permits.
The other important fact to be kept in mind is that more surface area does
notnecessarilymean more energytransfer. Itispossible,through poorchoiceof
finconfiguration,tohavemoresurfaceareaandyettransferlessenergy.Onehas
tolookattheproductofsurfaceareaandoverallheattransfercoefficientandnot
atsurfaceareaalone.Theoverallheattransfercoefficientissignificantlyreduced
as we increase the fin surface or use more fins per inch.
Finned tubes offer several advantages over bare tubes such as a compact
designthatoccupieslessspace,lowergaspressuredrop,lowertube-sidepressure
drop due to the fewer rows of tubes, and smaller overall weight and cost.
Solid fins offer slightly lower gas pressure drop than serrated fins, which
haveahigherheattransfercoefficientforthesamefindensityandconfiguration.
Particulates, if present, are likely to accumulate on serrated finned tubes, which
may be difficult to clean.
Copyright © 2003 Marcel Dekker, Inc.

8.19a
Q:
How are the heat transfer and pressure drop over finned tubes and tube and fin
wall temperatures evaluated?
A:
ThewidelyusedESCOAcorrelationsdevelopedbyESCOACorporation[9]will
be used to evaluate the heat transfer and pressure drop over solid and serrated
finned tubes in in-line and staggered arrangements. The basic equation for heat
transfer coefficient with finned tubes is given by Eq. (3).
The calculation for tube-side coefficient h was discussed earlier. h
i o
consists of two parts, a nonluminous coefficient h ; which is computed as
N
discussedinQ8.07,andh ,theconvectiveheattransfercoefficient.Computation
c
of h involves an elaborate procedure and the solving of several equations, as
c
detailed below.
Determination of h [9]
c
d 2h 0:5 t 460 0:25
h C C C þ gþ
c ¼ 3 1 5 d (cid:4) t 460
(cid:1) (cid:2) (cid:1)aþ (cid:2)
0:67
k
GC 38
(cid:4) p(cid:4) mC p! ð Þ
W
g
G 39
¼ S =12 A N L ð Þ
½ð T Þ(cid:3) o(cid:5) w
d nbh
A 40
o ¼12þ 6 ð Þ
C ;C ; and C are obtained from Table 8.10.
1 2 3
Gd
Re 41
¼12m ð Þ
1
s b 42
¼n(cid:3) ð Þ
Fin Efficiency and Effectiveness
For both solid and serrated fins, effectiveness Z is
A
Z 1 1 E f 43
¼ (cid:3)ð (cid:3) Þ A ð Þ
t
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.10a FactorsC –C forSolidandSerratedFinsinIn-Lineand
1 6
StaggeredArrangements—old ESCOA Correlations.
Solidfins
C
1¼
0:25Re(cid:3) 0:35 C
2¼
0:07
þ
8Re(cid:3) 0:45
In-line
C 3¼ 0:2 þ 0:65e (cid:3) 0:25h=s C 4¼ 0:08 ð 0:15S T =d Þ (cid:3) 1:1 ð h=s Þ 0:15
C 5 C ¼
6¼
1:1 1: (cid:3) 6 ð
(cid:3)
0:
ð
7 0 5 :7 (cid:3) 5 1
(cid:3)
:5 1 e :5 (cid:3) e 0:
(cid:3)
7N 0: d 7N Þ e d (cid:3)
Þ
e 2:
(cid:3)
0S 0: L 2 =
ð
S S T L=STÞ 2
Staggered
C C C 6 5 3 ¼ ¼ ¼ 1 0 0 : : : 1 7 35 þ þ þ ð ð 1 0 0 : : : 8 7 65 (cid:3) (cid:3) e 2 0 (cid:3) : : 0 1 8 :2 e e 5 (cid:3) (cid:3) h= 0 0 s : : 1 1 5 5 N N d d 2 2 C Þ Þ e e 4 (cid:3) (cid:3) ¼ 2 1 : : 0 0 ð S 0 S L : L = 1 = S S 1 T T ð Þ 0 (cid:3) :15 ð 0 S :7 T = (cid:3) d Þ 0 (cid:3) : 0 8 : e 7 ð (cid:3) h= 0 s :1 Þ 0 5 :2 N 0 d2 Þ e (cid:3) 0:6 ð SL=STÞ
Serrated fins
C
1¼
0:25Re(cid:3) 0:35 C
2¼
0:07
þ
8:0Re(cid:3) 0:45
In-line
C 3¼ 0:35 þ 0:5e (cid:3) 0:35h=s C 4¼ 0:08 ð 0:15S T =d Þ (cid:3) 1:1 ð h=s Þ 0:2
C 5 C ¼
6¼
1:1 1: (cid:3) 6 ð
(cid:3)
0:
ð
7 0 5 :7 (cid:3) 5 1
(cid:3)
:5 1 e :5 (cid:3) e 0:
(cid:3)
7N 0: d 7N Þ e d (cid:3)
Þ
e 2:
(cid:3)
0S 0: L 2 =
ð
S S T L=STÞ 2
Staggered
C C C 6 5 3 ¼ ¼ ¼ 1 0 0 : : : 1 7 55 þ þ þ ð ð 1 0 0 : : : 8 7 45 (cid:3) (cid:3) e 2 0 (cid:3) : : 0 1 8 :3 e e 5 (cid:3) (cid:3) h= 0 0 s : : 1 1 5 5 N N d d 2 2 C Þ Þ e e 4 (cid:3) (cid:3) ¼ 2 1 : : 0 0 ð S 0 S L : L = 1 = S S 1 T T ð Þ 0 (cid:3) :05 ð 0 S :7 T = (cid:3) d Þ 0 (cid:3) : 0 8 : e 7 ð (cid:3) h= 0 s :1 Þ 0 5 :2 N 3 d2 Þ e (cid:3) 0:6 ð SL=STÞ
Source:FintubeTechnologies,Tulsa,OK.
For solid fins,
4dh 4h2 2bd 4bh
A pn þ þ þ 44
f ¼ (cid:4) 24 ð Þ
d 1 nb
A A p ð (cid:3) Þ 45
t ¼ f þ 12 ð Þ
E 1= 1 0:002292m2h2 d 2h =d 0:5 46
¼ f þ ½ð þ Þ (cid:5) g ð Þ
where
m 24h =Kb 0:5 47
¼ð o Þ ð Þ
For serrated fins,
2h ws b bws
A pdn ð þ Þþ 48
f ¼ 12ws ð Þ
1 nb
A A pd ð (cid:3) Þ 49
t ¼ f þ 12 ð Þ
tanh mh
E ð Þ 50
¼ mh ð Þ
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.10b Factors C C forSolid andSerratedFins in In-line and StaggeredArrangements—Revised
1(cid:3) 6
Correlations
Solid fins
In-line
J C C C 3 5 1 ¼ ¼ ¼ C 0 1 0 : : : C 2 1 0 0 5 (cid:3) C 3 þ ð ð 1 0 0 : : d 4 : 7 6 5 5 5 (cid:3) e (cid:3) 2 (cid:3) h 2 1 0 : : : 2 9 = 5 5 d S e h= L (cid:3) 0 s = 0 :5 d :7N Þ t (cid:3) d 2 Þ C : e 3 4 (cid:3) R 4 2 ¼ : 6 e 0 0 S (cid:3) 0 L 0 : = = : 0 S 21 T 8 t ð 0:1 4 5 C C 6 S 2 0 6 T ¼ ¼ = 0 d :5 0 1 Þ : : (cid:3) 1 6 1 1 : (cid:3) 1þ ð h ð = 0 s 1 Þ : : 0 7 4 :1 5 5 R (cid:3) e(cid:3) 1 0 :5 :4 e (cid:3) 0:7Nd Þ e (cid:3) 0:2 ð SL=STÞ 2
f
¼
C
1
C
3
C
5½ð
d
þ
2h
Þ
=d
(cid:5)
t
½ðg
4
þ
60 = t
Þ ða
4
þ
60
0:2Þ(cid:5)5
¼ 2 4 6½ð þ Þ (cid:5)½ðgþ Þ ðaþ Þ(cid:5)
Staggered
J C C C 3 5 1 ¼ ¼ ¼ C 0 0 0 : : : C 3 7 0 5 9 þ C 1 þ ð R 0 0 : e d : 7 6 (cid:3) (cid:3) 5 0: e 2 2 0 5 (cid:3) h : 0 8 = :2 e d 5 (cid:3) h 0 = C 0 s : : 5 1 2 5N ¼ t d2 0 C Þ : ½ 0 e 4 4 7 (cid:3) 6 ¼ 5 1 0 :0 þ 0 S = : L 1 1 = t S 1 :8 T ð 0 (cid:5) 5 : 4 0 R 6 5 e 0 S (cid:3) C T 0 6 0 : = 3 :5 d ¼ Þ (cid:3) 1 0 : : 1 7 ð h þ =s ð Þ 0 1 :2 : 0 8 (cid:3) 2:1e (cid:3) 0:15Nd2 Þ e (cid:3) 2:0 ð SL=STÞ (cid:3)½ 0:7 (cid:3) 0:8e (cid:3) 0:15N d 2 (cid:5) e (cid:3) 0:6 ð SL=STÞ
f ¼ ¼ C 2 1 C 4 3 C 6 5 ½ ½ ð ð d þ þ 2h Þ =d (cid:5) (cid:5) 0:5½ ½ ð ð t g g þ þ 460 Þ Þ = ð ð t a a þ þ 460 Þ Þ (cid:5) (cid:5) (cid:3) 0:25
Serrated fins
In-line
J C C C 5 3 1 ¼ ¼ ¼ C 1 0 0 : : : C 1 2 0 5 5 (cid:3) C 3 þ ð ð 1 0 0 : : d 4 : 7 6 5 5 e (cid:3) (cid:3) (cid:3) 2 0 h 2 : 1 2 : 6 : 9 = 5 h d S = e s L (cid:3) 0 = 0 :5 d :7N Þ t (cid:3) d C 2 Þ : 4 e 3 (cid:3) ¼ R 4 2: 6 e 0 0 0 S (cid:3) : L 0 0 = = : 8 S 21 T ð t 0:15 4 S C C 6 T 2 0 6 = ¼ ¼ d 0 Þ :5 0 1 (cid:3) : 1 : 1 6 :1 1 ð (cid:3) hþ=s ð Þ 0 1 0: : 1 : 7 5 4 5 R (cid:3) e(cid:3) 1 0 :5 :4 e (cid:3) 0:7Nd Þ e (cid:3) 0:2 ð SL=STÞ 2
f
¼
C
1
C
3
C
5½ð
d
þ
2h
Þ
=d
(cid:5)
t
½ðg
4
þ
60 = t
Þ ða
4
þ
60
0:2Þ(cid:5)5
¼ 2 4 6½ð þ Þ (cid:5)½ðgþ Þ ðaþ Þ(cid:5)
Staggered
C J C C 3 5 1 ¼ ¼ ¼ C 0 0 0 : : : C 3 7 0 5 9 þ C 1 þ ð R 0 0 : e d : 7 6 (cid:3) (cid:3) 5 0: e 2 2 0 5 (cid:3) h : 0 8 :1 = e 7 d (cid:3) h= C 0 0 s :1 : 2 5 5N ¼ t d2 0 C Þ : e 0 4 (cid:3) 7 4 ¼ 1 5 6 :0 0 S þ 0 L : = = 1 1 S 1 t : T 8 ð 0 5 :0 R 4 5 e 6 C S (cid:3) 0 6 T 0: = ¼ 3 0 d :2 1 Þ 5 (cid:3) :1 0:7 þ ð h= ð s 1 Þ 0 : : 8 2 (cid:3) 2:1e (cid:3) 0:15Nd2 Þ e (cid:3) 2:0 ð SL=STÞ (cid:3)ð 0:7 (cid:3) 0:8e (cid:3) 0:15Nd2 Þ e (cid:3) 0:6 ð SL=STÞ
f ¼ ¼ C 2 1 C 4 3 C 6 5 ½ ½ ð ð d þ þ 2h Þ Þ =d (cid:5) (cid:5)0:5 ½ ½ ð ð t g g þ þ 460 Þ Þ = ð ð t a a þ þ 460 Þ Þ (cid:5) (cid:5) (cid:3) 0:25
Source:FintubeTechnologies,Tulsa,OK.
Copyright © 2003 Marcel Dekker, Inc.

where
24 h b ws 0:5
m (cid:4) oð þ Þ 51
¼ Kbws ð Þ
(cid:6) (cid:7)
Gas pressure drop DP is
g
G2N
DP f a d 52
g ¼ð þ Þ r 1:083 109 ð Þ
g(cid:4) (cid:4)
where
d 2h 0:5
f C C C þ for staggered arrangement 53
¼ 2 4 6(cid:4) d ð Þ
(cid:1) (cid:2)
d 2h
C C C þ for in-line arrangement 54
¼ 2 4 6(cid:4) d ð Þ
1 B2 t tg
a þ g2(cid:3) 1 55
¼ 4N (cid:4)460 t ð Þ
d þ g
free gas area 2
B 56
¼ total area ð Þ
(cid:1) (cid:2)
C ;C ;C are given in Table 8.10 for solid and serrated fins.
2 4 6
Tube Wall and Fin Tip Temperatures
Forsolidfinstherelationshipbetweentubewallandfintiptemperaturesisgiven
by
t t K mr I mr I mr K mr
g(cid:3) f 1ð eÞ(cid:4) 0ð eÞþ 1ð eÞ(cid:4) 0ð eÞ 57
t t ¼K mr I mr K mr I mr ð Þ
g(cid:3) b 1ð eÞ(cid:4) 0ð 0Þþ 0ð 0Þ(cid:4) 1ð eÞ
ThevariousBesselfunctionaldataareshowninTable8.11forserratedfins,
treated as longitudinal fins:
t t 1
g(cid:3) f 58
t t ¼cosh mb ð Þ
g(cid:3) b ð Þ
A good estimate of t can also be obtained for either type of fin as follows:
f
t t t t 1:42 1:4E 59
f ¼ bþðg(cid:3) bÞ(cid:4)ð (cid:3) Þ ð Þ
t , the fin base temperature, is estimated as follows:
b
t t q R R R 60
b ¼ iþ ð 3þ 4þ 5Þ ð Þ
where R ;R ; and R are resistances to heat transfer of the inside film, fouling
3 4 5
layer, and tube wall, respectively, and heat flux q is given by
o
q U t t 61
o ¼ oðg(cid:3) iÞ ð Þ
The following example illustrates the use of the equations.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.11 I ;I ;K ; and K ValuesforVarious Arguments
0 1 0 1
x I x I x K x K x
0ð Þ 1ð Þ 0ð Þ 1ð Þ
0 1.0 0 8 8
0.1 1.002 0.05 2.427 9.854
0.2 1.010 0.10 1.753 4.776
0.3 1.023 0.152 1.372 3.056
0.4 1.040 0.204 1.114 2.184
0.5 1.063 0.258 0.924 1.656
0.6 1.092 0.314 0.778 1.303
0.7 1.126 0.372 0.66 1.05
0.8 1.166 0.433 0.565 0.862
0.9 1.213 0.497 0.487 0.716
1.0 1.266 0.565 0.421 0.602
1.2 1.394 0.715 0.318 0.434
1.4 1.553 0.886 0.244 0.321
1.6 1.75 1.085 0.188 0.241
1.8 1.99 1.317 0.146 0.183
2.0 2.28 1.591 0.114 0.140
2.2 2.629 1.914 0.0893 0.108
2.4 3.049 2.298 0.0702 0.0837
2.6 3.553 2.755 0.554 0.0653
2.8 4.157 3.301 0.0438 0.0511
3.0 4.881 3.953 0.0347 0.0402
3.2 5.747 4.734 0.0276 0.0316
3.4 6.785 5.670 0.0220 0.0250
3.6 8.028 6.793 0.0175 0.0198
3.8 9.517 8.140 0.0140 0.0157
4.0 11.30 9.759 0.0112 0.0125
4.2 13.44 11.70 0.0089 0.0099
4.4 16.01 14.04 0.0071 0.0079
4.6 19.09 16.86 0.0057 0.0063
4.8 22.79 20.25 0.0046 0.0050
5.0 27.24 24.34 0.0037 0.0040
Example
A steam superheater is designed for the following conditions.
Gas flow 225,000pph
¼
Gas inlet temperature 1050 F
(cid:2)
¼
Gas exit temperature 904 F
(cid:2)
¼
Gas analysis (vol%): CO 3, H O 7, N 75, O 15
2¼ 2 ¼ 2¼ 2¼
Copyright © 2003 Marcel Dekker, Inc.

Steam flow 50,000pph
¼
Steam temperature in 501 F (sat)
(cid:2)
¼
Steam exit temperature 758 F
(cid:2)
¼
Steam pressure (exit) 650psig
¼
Tubes used: 2 0.120 low alloy steel tubes; 18 tubes=row, 6 deep, 10ft long,
(cid:4)
in-line arrangement with 4in. square pitch and nine streams. Tube inner dia-
meter 1.738in.; outer diameter 2 in.
¼ ¼
Fins used: solid stainless steel, 2fins=in., 0.5in. high and 0.075in. thick.
Fin thermal conductivity K 15Btu=fth F.
(cid:2)
¼
Determine the heat transfer coefficient and pressure drop.
Solution.
2 2 0:5 0:075
A (cid:4) (cid:4) 0:17917ft2=ft
o ¼12þ 6 ¼
225;000
G 8127lb=ft2 h
¼18 10 4=12 0:17917 ¼
(cid:4) (cid:4)½ð Þ(cid:3) Þ(cid:5)
The gas properties at the average gas temperature (from the Appendix) are
C 0:276; m 0:086; k 0:03172
p ¼ ¼ ¼
8127 2
Re (cid:4) 15;750
¼12 0:086¼
(cid:4)
C 1 ¼ 0:25 (cid:4)ð 15;750 Þ (cid:3) 0:35 ¼ 0:0085
s 1=2 0:075 0:425
¼ (cid:3) ¼
C 0:2 0:65e 0:25 0:5=0:425 0:6843
3 ¼ þ (cid:3) (cid:4) ¼
C 1:1 0:75 1:5e 0:7 6 e 2 4=4 1:0015
5 ¼ (cid:3)ð (cid:3) (cid:3) (cid:4) Þð (cid:3) (cid:4) Þ¼
Assume that the average fin temperature is 750 F. The average gas
(cid:2)
temperature 977 F, and steam temperature 630 F. The fin thermal conduc-
(cid:2) (cid:2)
¼ ¼
tivity K is assumed to be 15Btu=fth F. Then,
(cid:2)
3 0:5
h 0:0085 0:6843 1:0015
c ¼ (cid:4) (cid:4) (cid:4) 2
(cid:1) (cid:2)
977 460 0:25
þ 8127 0:276
(cid:4) 750 460 (cid:4) (cid:4)
(cid:1) þ (cid:2)
0:03172 0:67
20:29
(cid:4) 0:276 0:086 ¼
(cid:1) (cid:4) (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

UsingmethodsdiscussedinQ8.07,wefindh 1.0.Thebeamlengthforfinned
N¼
tubes is computed as 3.4 volume=surface area. Hence
(cid:4)
h 20:29 1:0 21:29
o ¼ þ ¼
24 21:29 0:5
m (cid:4) 21:31
¼ 15 0:075 ¼
(cid:1) (cid:4) (cid:2)
E 1= 1 0:002292 21:31 21:31 0:5 0:5 p1:5
¼ ð þ (cid:4) (cid:4) (cid:4) (cid:4) (cid:4) Þ
0:758
ffiffiffiffiffiffiffi
¼
A 3:14 2
f ¼ (cid:4)
4 2 0:5 4 0:5 0:5 2 0:075 2 4 0:075 5
(cid:4) (cid:4) þ (cid:4) (cid:4) þ (cid:4) (cid:4) þ (cid:4) (cid:4)
(cid:4) 24
1:426
¼
1 2 0:075
A 1:426 3:14 2 (cid:3) (cid:4) 1:871
t ¼ þ (cid:4) (cid:4) 12 ¼
Hence
1:426
Z 1 1 0:758 0:8156
¼ (cid:3)ð (cid:3) Þ 1:871¼
Let us compute h for steam. w 50,000=9 5555 lb=h per tube. From
i ¼ ¼
Table 8.2, factor C 0.34.
¼
5555 0:8
h i ¼ 2:44 (cid:4) 0:34 (cid:4) ð 1:738 Þ 1:8 ¼ 303Btu=ft2h (cid:2) F
ð Þ
1 1 1:871
12
U ¼21:29 0:816þ (cid:4)303 3:14 1:738
(cid:4) (cid:4) (cid:4)
1:871 12 2
0:001 0:001 (cid:4) 24 ln
þ þ (cid:4)3:14 1:738þ 1:738
(cid:4) (cid:1) (cid:2)
1:871
(cid:4)24 20 3:14 1:738
(cid:4) (cid:4) (cid:4)
0:0576 0:01358 0:001 0:0041 0:0032
¼ þ þ þ þ
0:0795 or U 12:58Btu=ft2hF
¼ ¼
Calculation of Tube Wall and Fin Tip Temperature
Heat fluxq 12:58 977 630 4365Btu=ft2 h
¼ (cid:4)ð (cid:3) Þ¼
t 630 4365 0:0032 0:0041 0:01358
b ¼ þ (cid:4)ð þ þ Þ
722 F
(cid:2)
¼
Copyright © 2003 Marcel Dekker, Inc.

Using the elaborate Bessel functions, from Table 8.11,
1:5
mr 21:29 2:661ft; mr 1:7742ft
e ¼ (cid:4) 12 ¼ o ¼
K 2:661 0:0517 K 2:661 0:061
0 ð Þ¼ 1 ð Þ¼
I 2:661 3:737; I 2:661 2:921
0ð Þ¼ 1ð Þ¼
K 1:7742 0:1515; I 1:7742 1:959
0ð Þ¼ 0ð Þ¼
Hence,
977 t 0:061 3:737 2:921 0:0517
(cid:3) f (cid:4) þ (cid:4) 0:6743
977 722¼0:061 1:959 0:1515 2:921¼
(cid:3) (cid:4) þ (cid:4)
t 805 F
f ¼ (cid:2)
Using the approximation
t t 1:42 1:4 0:758 977 722 813 F
f ¼ bþð (cid:3) (cid:4) Þ(cid:4)ð (cid:3) Þ¼ (cid:2)
Note that this is only an average base and fin tip temperature. For material
selection purposes one should look at the maximum heat flux, whichoccurs, for
instance, at the gas inlet in a counterflow arrangement, and also consider the
nonuniformityormaldistributioningasandsteamflow.Acomputerprogramcan
be developedto compute the tubewall and fin tip temperatures at various points
along the tube length and the results used to select appropriate materials.
Itcanbenotedfromtheabovethatthereareafewwaystoreducethefintip
temperature:
1. Increase fin thickness. This reduces the factor m and hence t .
f
2. Increase the thermal conductivity of the fin material. This may be
difficult, because the thermal conductivity of carbon steels is higher
than that of alloy steels, and carbon steels can withstand temperatures
only up to 850 F, whereas alloy steels can withstand up to 1300 F
(cid:2) (cid:2)
depending on the alloy composition.
3. Reduce h or the gas-side coefficient by using a lower gas mass
o
velocity.
4. Reduce fin height or density.
5. In designs where the gas inlet temperature is very high, use a
combination of bare and finned rows. The first few rows could be
bare, followed by tubes with a low fin density or height or increased
thickness and then followed by tubes with higher fin density or height
or smaller thickness to obtain the desired boiler performance. A row-
by-row analysis of the finned bundle is necessary, which requires the
use of a computer program.
Copyright © 2003 Marcel Dekker, Inc.

Computation of Gas Pressure Drop
C 2 ¼ 0:07 þ 8 (cid:4)ð 15;750 Þ (cid:3) 0:45 ¼ 0:1734
C 4 ¼ 0:08 (cid:4)ð 0:15 (cid:4) 2 Þ (cid:3) 1:11 (cid:4)ð 0:5=0:425 Þ 0:15 ¼ 0:3107
C 1
6 ¼
3
f 0:1734 0:3107 1 0:0808
¼ (cid:4) (cid:4) (cid:4)2¼
0:333 0:17917 2
B2 (cid:3) 0:2134
¼ 0:333 ¼
(cid:1) (cid:2)
904 1050 1 0:2134
a (cid:3) þ 0:005
¼ 460 977 (cid:4) 24 ¼(cid:3)
þ
6
DP 0:0808 0:0051 8120 8120
g ¼ð (cid:3) Þ(cid:4) (cid:4) (cid:4)0:0271 1:083 109
(cid:4) (cid:4)
1:02in:WC
¼
Gas density 0:0271:
ð ¼ Þ
Computer solution of the above system of equations saves a lot of time.
However,Ihavedevelopedachart(Fig.8.7)thatcanbeusedtoobtainh (orh )
c g
and Z values for serrated fins and an in-line arrangement for various fin
configurationsandgasmassvelocitiesforgasturbineexhaustgasesatanaverage
gastemperatureof700 F.Althoughacomputerprogramisthebesttool,thechart
(cid:2)
canbeusedtoshowtrendsandtheeffectoffinconfigurationontheperformance
of finned surfaces. The use of the chart is explained later with an example. The
following points should be noted.
1. FromFig.8.7,itcanbeseenthatforagivenmassvelocity,thehigher
the fin density or height, the lower the gas-side coefficient or effec-
tiveness, which results in lower U . The amount of energy transferred
o
in heat transfer equipment depends on the product of the overall heat
transfer coefficient and surface area and not on the surface area alone.
We will see later that one can have more surface area and yet transfer
less duty due to poor choice of fin configuration.
2. HigherfindensityorheightresultsinhigherDP .Evenafteradjusting
g
for the increased surface area per row, it can be shown that the higher
the fin density or the greater the height, the higher the gas pressure
drop will be for a given mass velocity.
Copyright © 2003 Marcel Dekker, Inc.

Figure 8.7 Chart of convective heat transfer coefficient and pressure drop
versusfingeometry. (DatafromRef.10)
8.19b
Q:
Describe Briggs and Young’s correlation.
A:
Chartsandequationsprovidedbythemanufactureroffinnedtubescanbeusedto
obtain h . In the absence of such data, the following equation of Briggs and
c
Young for circular or helical finned tubes in staggered arrangement [4] can be
used.
h d Gd 0:681 mC 0:33 S 0:2 S 0:113
c 0:134 p 62
12k ¼ 12m k h b ð Þ
(cid:1) (cid:2) (cid:1) (cid:2) (cid:1) (cid:2) (cid:1) (cid:2)
Simplifying, we have
G0:681 k0:67C0:33 S0:313
h 0:295 p 63
c ¼ d0:319 m0:351 h0:2b0:113 ð Þ
(cid:1) (cid:2)(cid:1) (cid:2)(cid:1) (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

where
G gas mass velocity
¼
W
g Eq: 39
¼ N L S =12 A ½ ð Þ(cid:5)
w ð T (cid:3) oÞ
S fin clearance 1=n b;in [Eq. (42)]
¼ ¼ (cid:3)
d; h; b tube outer diameter, height, and thickness, in.
¼
d nbd
A fin obstruction area ;ft2=ft Eq: 40
o¼ ¼12þ 6 ½ ð Þ(cid:5)
The gas properties C ;m, and k are evaluated at the average gas temperature.
p
Thegas heat transfer coefficient h has to be corrected for the temperature
c
distribution along the fin height by the fin efficiency
1
E 64
¼ 1 mh 2 d 2h ð Þ
1 þ
þ3 12 d
(cid:1) (cid:2) rffiffiffiffiffiffiffiffiffiffiffiffiffiffi
where
24h
m c Eq: 47
¼sffiKffiffiffimffiffiffibffiffi ½ ð Þ(cid:5)
K is the fin metal thermal conductivity, in Btu=fth F.
m (cid:2)
In order to correct for the effect of finned area, a term called fin
effectiveness is used. This term, Z, is given by
A
Z 1 1 E f Eq:43
¼ (cid:3)ð (cid:3) Þ(cid:4)A ½ (cid:5)
t
where the finned area A and total area A are given by
f t
pn
A 4dh 4h2 2bd 4bh Eq: 44
f ¼ 24 ð þ þ þ Þ ½ ð Þ(cid:5)
pd
A A 1 nb Eq: 45
t ¼ f þ12 ð (cid:3) Þ ½ ð Þ(cid:5)
n is the fin density in fins=in. The factor
k0:67C0:33
F p 65
¼ m0:35 ð Þ
is given in Table 8.12.
Theoverallheattransfercoefficientwithfinnedtubes,U,canbeestimated
as U 0:85Zh , neglecting the effect of the non-luminous heat transfer coeffi-
¼ c
cient.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.12 Factor F for
Finned Tubes
Temp( F) F
(cid:2)
200 0.0978
400 0.1250
600 0.1340
800 0.1439
1000 0.1473
1200 0.1540
1600 0.1650
Example
Determine the gas-side heat transfer coefficient when 150,000lb=h of flue gases
at an average temperature of 900 F flow over helically finned economizer tubes
(cid:2)
with the following parameters:
d tube outer diameter 2.0in.
¼ ¼
n fins=in. 3
¼ ¼
h fin height 1in.
¼ ¼
b fin thickness 0.06in.
¼ ¼
L effective length of tubes 10.5ft
¼ ¼
N number of tubes wide 12
w¼ ¼
S transverse pitch 4.5in. (staggered)
T¼ ¼
Calculate A ;A , and A. From Eq. (40),
o f t
2 1
A 3 0:06 0:2ft2=ft
o ¼12þ (cid:4) (cid:4)6¼
From Eq. (44),
3
A p 4 2 1 4 1 1
f ¼ (cid:4)24 (cid:4)ð (cid:4) (cid:4) þ (cid:4) (cid:4)
(cid:1) (cid:2)
2 0:06 2 4 0:06 4:9ft2=ft
þ (cid:4) (cid:4) þ (cid:4) Þ¼
From Eq. (45),
2 1 3 0:06
A 4:9 p (cid:4)ð (cid:3) (cid:4) Þ 5:33ft2=ft
t ¼ þ 12 ¼
Copyright © 2003 Marcel Dekker, Inc.

From Eq. (39),
150;000
G 6800lb=ft2 h
¼12 10:5 4:5=12 0:2 ¼
(cid:4) (cid:4)ð (cid:3) Þ
1
Fin pitchS 0:06 0:27
¼3(cid:3) ¼
Using Eq. (65) with F 0.145 from Table 8.12 gives us
¼
h 0:295 68800:681 0:145
c ¼ (cid:4) (cid:4)
0:270:313
12:74Btu=ft2h F
(cid:4)20:319 10:2 0:060:113 ¼ (cid:2)
(cid:4) (cid:4)
Calculate fin efficiency from Eq. (64). Let metal thermal conductivity of
fins (carbon steel) 24Btu=fth F.
(cid:2)
¼
24 12:74
m (cid:4) 14:57
¼ 24 0:06 ¼
rffiffiffiffiffiffiffiffi(cid:4)ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1
E 0:6
¼1 0:33 14:57 1=12 2 2 2 =2¼
þ (cid:4)ð (cid:4) Þ (cid:4) ð þ Þ
4:9
pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Fin effectivenessZ 1 1 0:6 0:63
¼ (cid:3)ð (cid:3) Þ 5:33¼
Hence,
Zh 0:63 12:74 8Btu=ft2 h F
c ¼ (cid:4) ¼ (cid:2)
K ranges from 23to27Btu=fth F forcarbon steels, dependingon temperature
m (cid:2)
[1]. For alloy steels it is lower.
8.19c
Q:
Thisexampleshowshowonecanpredicttheperformanceofagivenheattransfer
surface. A superheater is designed for the following conditions: 18 tubes=row, 6
rowsdeep,10ftlongwith2fins=in.,0.5in.highand0.075in.thicksolid fins.It
has 18 streams. Surface area 2022ft2. Tube spacing 4in. square.
¼ ¼
Predicttheperformanceofthesuperheater under thefollowingconditions:
Gas flow 150,000lb=h at 1030 F
(cid:2)
¼
Steam flow 35,000lb=h at 615psig sat
¼
Flue gas analysis (vol%): CO 7, H O 12, N 75, O 6
2¼ 2 ¼ 2¼ 2¼
Heat loss 2%
Surface ar ¼ ea A 2022ft2
¼
Copyright © 2003 Marcel Dekker, Inc.

LetussaythatU hasbeenestimatedas10.6Btu=ft2h Fusingmethodsdiscussed
(cid:2)
earlier.
A:
LetususetheNTUmethodtopredicttheperformanceofthesuperheater.Thisis
discussed in Q8.30. The superheater is in counterflow arrangement.
Energy transferred Q eC t t
¼ minðg 1 (cid:3) S 1Þ
where
1 exp NTU 1 C
e (cid:3) ½(cid:3) ð (cid:3) Þ(cid:5)
¼1 C exp NTU 1 C
(cid:3) ½(cid:3) ð (cid:3) Þ(cid:5)
C C =C
¼ min max
C is the lower of (mass specific heat of the fluid) on gas and steam
min (cid:4)
sides.
T ;t gas and steam temperature at inlet to superheater, F
g 1 s 1¼ (cid:2)
Use 491 F for steam saturation temperature.
(cid:2)
Though NTU methods generally require no iterations, a few rounds are
necessary in this case to evaluate the specific heat for steam and gas, which are
functions of temperature. However, let us assume that the steam-side specific
heat 0.6679 and that of gas 0.286Btu=lb F.
(cid:2)
¼ ¼
C 150;000 0:98 0:286 42;042
gas ¼ (cid:4) (cid:4) ¼
C 35;000 0:6679 23;376
steam ¼ (cid:4) ¼
Hence, C 23,376.
min¼
23;376
C 0:556
¼42;042¼
10:62 2022
NTU UA=C (cid:4) 0:9186
¼ min ¼ 23;376 ¼
Hence
1 exp 0:9186 1 0:556
e (cid:3) ½(cid:3) (cid:4)ð (cid:3) Þ(cid:5) 0:5873
¼1 0:556 exp 0:9186 1 0:556 ¼
(cid:3) ½(cid:3) (cid:4)ð (cid:3) Þ(cid:5)
Copyright © 2003 Marcel Dekker, Inc.

Hence
Energy transferedQ 0:5873 23;376 1030 491 6:7MMBtu=h
¼ (cid:4) (cid:4)ð (cid:3) Þ¼
6;700;000
Exit steam temperature 491 287 491 778 F
(cid:2)
¼35;000 0:06679þ ¼ þ ¼
(cid:4)
6;700;000
Exit gas temperature 1030 871 F
(cid:2)
¼ (cid:3)150;000 0:286 0:98¼
(cid:4) (cid:4)
Steam-side pressure drop is obtained as follows:
Equivalent length of tube 18=9 6 10 18=9 6 2:5 2
¼ð Þ(cid:4) (cid:4) þð Þ(cid:4) (cid:4) (cid:4)
180ft
¼
Use 185ft for estimation. Specific volume of steam at the average steam
conditions of 620psia and 635 F is 0.956ft3=lb.
(cid:2)
35 2 185
Pressure drop 3:36 0:02 0:956 11:4psi
¼ (cid:4) (cid:4) (cid:4) 9 (cid:4)1:7385 ¼
(cid:1) (cid:2)
Gas-sidepressuredropmaybeestimatedusing thechartinFig.8.7andisabout
0.6in.WC.
8.20
Q:
A gas turbine HRSG evaporator operates under the following conditions:
Gas flow 230,000lbh (vol % CO 3, H O 7, N 75, O 15)
¼ 2¼ 2 ¼ 2¼ 2¼
Gas inlet temperature 1050 F
(cid:2)
¼
Exit gas temperature 406 F
(cid:2)
¼
Duty 230,000 0.99 0.27 (10507406) 39.6MMBtu=h
¼ (cid:4) (cid:4) (cid:4) ¼
Steam pressure 200psig
¼
Feedwater temperature 230 F
(cid:2)
¼
Blowdown 5%
Fouling fac ¼ tors 0.001ft2h F=Btu on both gas and steam sides
(cid:2)
¼
Arrangement: 4in.square pitch
Tubes used: 2 1.773in., 24 tubes=row, 11ft long
(cid:4)
Fins: 5 fins=in., 0.75in. high, 0.05in. thick, serrated
Determine the overallheat transfer coefficientand pressure drop using the chart.
A:
The chart shown in Fig. 8.7 has been developed for serrated fins in in-line
arrangement for the above gas analysis. Users may develop their charts for
Copyright © 2003 Marcel Dekker, Inc.

various configurations or use a computer program. The chart is based on an
averagegastemperatureof700 Fandagasanalysis(vol%)ofCO 3,H O 7,
(cid:2) 2¼ 2 ¼
N 75, O 15.
2¼ 2¼
2 0:05
A 5 0:75 0:1979ft2=ft
o ¼12þ (cid:4) (cid:4) 6 ¼
(cid:1) (cid:2)
230;000
G 6434lb=ft2 h
¼24 11 0:3333 0:1979 ¼
(cid:4) (cid:4)ð (cid:3) Þ
Average gas temperature 728 F. From Table 8.12, the correction factor is
(cid:2)
¼
0.1402=0.139 1.008.
ForG ¼ 6434,h fromthechart 11.6Btu=ft2h F,Gaspressuredropover
¼ c ¼ (cid:2)
10 rows 1.7in.WC.
¼
Fin effectiveness 0.75
h is small, abou ¼ t 0.4Btu=ft2h F
N (cid:2)
h 0.75 (0.4 1.008 11.6) 9.07Btu=ft2h F
o¼ (cid:4) þ (cid:4) ¼ (cid:2)
The fin total surface area can be shown to be 5.7ft2=ft.
Hence
A 5:7 12
t (cid:4) 12:29
A ¼3:14 1:773¼
i (cid:4)
Let tube-side boiling coefficient 2000Btu=ft2h F and fin thermal con-
(cid:2)
¼
ductivity 25Btu=fth F
(cid:2)
¼
1 1 12:29 ln 2=1:773
0:001 12:29 0:001 12:29 2 ð Þ
U ¼9:07þ (cid:4) þ þ 2000 þ (cid:4) (cid:4) 24=25
0:110 0:01229 0:001 0:006145 0:004935 0:1344
¼ þ þ þ þ ¼
U 7:4Btu=ft2 h F
(cid:2)
¼
1050 388 406 388
Log-mean temperature difference ð (cid:3) Þ(cid:3)ð (cid:3) Þ
¼ln 1050 388 = 406 388
½ð (cid:3) Þ ð (cid:3) Þ(cid:5)
178 F
(cid:2)
¼
39:6 106
Surface area required (cid:4) 30;063ft2
¼ 178 7:4 ¼
(cid:4)
30;063
Number of rows deep required 20
¼24 11 5:7¼
(cid:4) (cid:4)
Gas pressure drop 1:7 2 3:4in. Wc
¼ (cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

8.21
Q:
How does a finned surface compare with a bare tube bundle for the same duty?
A:
Let us try to design a bare tube boiler for the same duty as above.Use the same
tube size and spacing, tubes per row, and length. Use 2 1.773in. bare tubes.
(cid:4)
Using the procedure described in Q8.14, we can show that U 13.05
Btu=ft2h F and that 124 rows are required for the same duty. The res ¼ ults are
(cid:2)
shown in Table 8.13.
It may be seen that the finned tube bundle is much more compact and has
fewerrowsandalsoalowergaspressuredrop.Italsoweighslessandshouldcost
less. Therefore, in clean gas applications such as gas turbine exhaust or fume
incineration plants, extended surfaces may be used for evaporators. In dirty gas
applications such as municipal waste incineration or with flue gases containing
ashorsolidparticles, baretubes are preferred.Finnedtubes mayalso be usedin
packaged boiler evaporators.
However, the heat flux inside the finned tubes is much larger, which is a
concern in high gas temperature situations. The tube wall temperature is also
higher.Hencewhenthegastemperatureishigh, say1400–1700 F,weuseafew
(cid:2)
TABLE8.13 Comparison of BareTube and FinnedTube Boilers
Bare tube Finnedtube
Gas flow,lb=h 230,000
Inlet gastemperature, F 1050
(cid:2)
Exitgas temperature, F 407
(cid:2)
Duty, MMBtu=h 39.5
Steampressure,psig 200
Feedwatertemperature, F 230
(cid:2)
Steamflow,lb=h 39,200
Surfacearea, ft2 17,141 30,102
Overall heattransfercoeff, Btu=ft2h F 13.0 7.39
(cid:2)
Gas pressuredrop, in.WC 5.0 3.5
Number ofrows deep 124 20
Heatflux, Btu=ft2h 9707 60,120
Tube wall temperature, F 409 516
(cid:2)
Weight oftubes, lb 81,100 38,800
Tubes=row 24;effectivelength 11ft;4in.squarespacing.Gasanalysis(vol%)CO 3
¼ ¼ 2¼
H 7,N 75,O 15.Blowdown 5%.
2¼ 2¼ 2¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

baretubesfollowedbytubeswith, say,2fins=in.findensityandthen gobackto
four or more fins per inch. This ensures that the gas stream is cooled before
entering tube bundles with a high fin density and that the tubes are operating at
reasonable temperatures, which should also lower the fin tip temperatures.
Whenthetube-sidefoulingislarge,ithasthesameeffectasalowtube-side
heattransfercoefficient,resultinginpoorperformancewhenahighfindensityis
used.SeeQ8.24.Onemayalsonotethesignificantdifferenceinsurfaceareasand
not be misled by this value.
8.22
Q:
Which is the preferred arrangement for finned tubes, in-line or staggered?
A:
Bothin-lineandstaggeredarrangementshavebeenusedwithextendedsurfaces.
The advantages of the staggered arrangement are higher overall heat transfer
coefficients and smaller surface area. Cost could be marginally lower depending
on the configuration. Gas pressure drop could be higher or lower depending on
thegasmassvelocityused.Ifcleaninglanesarerequiredforsootblowing,anin-
line arrangement is preferred.
Bothsolidandserratedfinsareusedintheindustry.Generally,solidfinsare
used in applications where the deposition of solids is likely.
The following example illustrates the effect of arrangement on boiler
performance.
Example
150,000lb=h of turbine exhaust gases at 1000 F enter an evaporator of a waste
(cid:2)
heat boiler generating steam at 235psig. Determine the performance using solid
and serrated fins and in-line versus staggered arrangements. Tube size is
2 1.77in.
(cid:4)
Solution. Using the ESCOA correlations and the methodology discussed
above for evaporator performance, the results shown in Table 8.14 were arrived
at.
8.23
Q:
How does the tube-side heat transfer coefficient or fouling factor affect the
selection of fin configuration such as fin density, height, and thickness?
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.14 Comparison Between Staggered and In-Line Designs for Nearly
SameDuty andPressure Dropa
Serratedfins Solid fins
In-line Staggered In-line Staggered
Fin config. 5 0.75 0.05 0.157 2 0.75 0.05 0
(cid:4) (cid:4) (cid:4) (cid:4) (cid:4) (cid:4)
Tubes=row 18 20 18 20
No.of finsdeep 20 16 20 16
Length 10 10 10 11
U 7.18 8.36 9.75 10.02
o
DP 3.19 3.62 1.72 1.42
g
Q 23.24 23.31 21.68 21.71
Surface 20,524 18,244 9802 9584
aDuty,MMBtu=h;DP ,in.WC;surface,ft2;temperature, F;U ,Btu=ft2h F.
g (cid:2) o (cid:2)
A:
Findensity,height,andthicknessaffecttheoverallheattransfercoefficientascan
be seen in Fig. 8.7. However, the tube-side coefficient also has an important
bearing on the selection of fin configuration.
A simple calculation can be done to show the effect of the tube-side
coefficient on U . It was mentioned earlier that the higher the tube-side
o
coefficient, the higher the ratio of external to internal surface area can be. In
otherwords,itmakesnosensetousethesamefinconfiguration,say5fins=in.fin
density, for a superheater as for an evaporator.
RewritingEq.(3)basedontube-sideareaandneglectingother resistances,
1 1 A=A
i t 66
U ¼h þ h Z ð Þ
i i o
Using the data from Fig. 8.7, U values have been computed for different fin
i
densitiesandfordifferenth valuesfor theconfigurationindicatedinTable8.15.
i
The results are shown in Table 8.15. Also shown are the ratio of U values
i
between the 5 and 2 fins=in. designs as well as their surface area.
The following conclusions can be drawn [10].
1. Asthetube-sidecoefficientdecreases,theratioofU values(between5
i
and2fins=in.)decreases.Withh 20,theU ratioisonly1.11.With
i ¼ i
an h of 2000, the U ratio is 1.74. What this means is that as h
i i i
decreases, the benefit of increasing the external surface becomes less
attractive. With 2.325 times the surface area we have only 1.11-fold
improvement in U. With a higher h of 2000, the increase is better,
i i
1.74.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.15 Effect of h onU
i i
h 20 100 1000
i
n,fins=in. 2 5 2 5 2 5
G,lb=ft2h 5591 6366 5591 6366 5591 6366
A=AZh a 0.01546 0.00867 0.01546 0.00867 0.01546 0.00867
t i o
U 2.73 1.31 7.03 4.12 11.21 8.38
o
U 15.28 17.00 39.28 53.55 62.66 109
i
Ratio U 1.11 1.363 1.74
i
RatioDP 1.6 1.3 1.02
g
Calculationsbasedon2.0 0.105tubes,29tubes=row,6ftlong,0.05in.thickserratedfins;
(cid:4)
tubes on 4.0in. square pitch; fin height 0.75in.; gas flow 150,000pph; gas inlet
¼ ¼
temp 1000 F.
aSurf ¼ aceare (cid:2) aA of2fins=in.tube 2.59ft2=ft,andfor5fins=in.,A 6.02ft2=ft.
t ¼ t¼
2. Asimpleestimationoftubewalltemperaturecantellusthatthehigher
the fin density, the higher the tube wall temperature will be. For the
caseofh 100,withn 2,U 39.28,gastemperature 900 F,and
i¼ ¼ i¼ ¼ (cid:2)
fluid temperature of 600 F,
(cid:2)
Heat fluxq 900 600 39:28
i ¼ð (cid:3) Þ(cid:4)
11;784Btu=ft2 h
¼
The temperature drop across the tube-side film (h 100)
i¼ ¼
11,784=100 118 F. The wall temperature 600 118 718 F.
(cid:2) (cid:2)
With ¼ n 5, U 53.55, q 53.55 ¼ 300 þ 16,0 ¼ 65Btu=ft2h.
¼ i¼ i¼ (cid:4) ¼
Tube wall temperature 600 16,065=100 761 F. Note that we
(cid:2)
¼ þ ¼
are comparing for the same height. The increase in wall temperature
is 43 F.
(cid:2)
3. Theratioofthegaspressuredropbetweenthe5and2fins=in.designs
(after adjusting for the effect of U values and differences in surface
i
areaforthesameenergytransfer)increasesasthetube-sidecoefficient
reduces.Itis1.6forh 20and1.02forh 2000.Thatis,whenh is
i¼ i¼ i
smaller, it is prudent to use a smaller fin surface.
Effect of Fouling Factors
The effects of inside and outside fouling factors ff and ff are shown in Tables
i o
8.16 and 8.17. The following observations can be made.
1. With a smaller fin density, the effect of ff is less. With 0.01 fouling
i
and2fins=in.,U 6.89comparedwith10.54with0.001fouling.The
o¼
ratio is 0.65. With 5 fins=in., the corresponding values are 4.01 and
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.16 Effect of ff,Tube-Side FoulingFactora
i
Fins=in., n 2 2 5 5
U ,clean 11.21 11.21 8.38 8.38
o
ff 0.001 0.01 0.001 0.01
i
U ,dirty 10.54 6.89 7.56 4.01
o
U as% 100 65 100 53
o
aTube-sidecoefficient 2000.
¼
7.46, the ratio being 0.53. That means that with increased tube-side
fouling it makes sense to use a lower fin density or smaller ratio of
external to internal surface area. The same conclusion was reached
with a smaller tube-side coefficient.
2. The effect of ff is less significant, because it is not enhanced by the
o
ratio of external to internal surface area. A review of Eq. (1) tells us
thatthetube-sideheattransfercoefficientorfoulingfactorisincreased
bytheratiooftheexternaltointernalsurfacearea,andhenceitseffect
is easily magnified.
8.24
Q:
Compare the effect of tube-side fouling on bare, low, and high finned tubes.
A:
Threeboilerevaporatorsweredesignedusingbaretubes,2fins=in.and5fins=in.,
to cool 150,000lb=h of clean flue gases from 1000 F to 520 F. The effect of
(cid:2) (cid:2)
fouling factors of 0.001 and 0.01 on duty, tube wall temperatures, and steam
productionareshowninTable8.18.Thefollowingpointsmaybeobserved[11].
1. With bare tubes, the higher tube-side fouling results in the lowest
reduction in duty, from 19.65 to 18.65MMBtu=h, with the exit gas
TABLE8.17 Effect of ff ,OutsideFouling Factora
o
Fins=in., m 2 2 5 5
U ,clean 11.21 11.21 8.38 8.38
o
ff 0.001 0.01 0.001 0.01
o
U ,dirty 11.08 10.08 8.31 7.73
o
U as% 100 91 100 93
o
aTube-sidecoefficient 2000.
¼
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.18 Effect of FoulingFactors
Case 1 2 3 4 5 6
1.Gas tempin, F 1000 1000 1000 1000 1000 1000
(cid:2)
2.Exit temp, F 520 545 520 604 520 646
(cid:2)
3.Duty, MMBtu=h 19.65 18.65 19.65 16.30 19.65 14.60
4.Steamflow,lb=h 19,390 18,400 19,390 16,110 19,390 14,400
5.ff,ft2h F=Btu 0.001 0.01 0.001 0.01 0.001 0.01
i (cid:2)
6.Heat flux,Btu=ft2h 9314 8162 35,360 23,080 55,790 30,260
7.Wall temp, F 437 516 490 680 530 760
(cid:2)
8.Fin temp, F — — 730 840 725 861
(cid:2)
9.A=A 1.13 1.13 5.6 5.6 12.3 12.3
t i
10. Fins bare bare (2 0.75 (5 0.75
(cid:4) (cid:4)
0.05 0.157) 0.05 0.157)
(cid:4) (cid:4) (cid:4) (cid:4)
11. Tubes perrow 20 20 20 20 20 20
12. No.deep 60 60 16 16 10 10
13. Length,ft 8 8 8 8 8 8
14. Surfacearea, ft2 5024 5024 6642 6642 9122 9122
15. GasDp,in.WC 3.0 3.1 1.80 1.90 2.0 2.1
temperature going up to 545 F from 520 F—see columns 1 and 2.
(cid:2) (cid:2)
With 2 fins=in., the exit gas temperature increases from 520 F to
(cid:2)
604 F, with the duty reducing to 16.3 from 19.65MMBtu=h. The
(cid:2)
steam generation is about 3200lb=h lower. With 5fins=in., the reduc-
tion in duty and steam generation are the greatest.
2. Theheatfluxincreaseswithfindensity.Therefore,withhightempera-
tureunitsonehastobeconcernedwithDNBconditions;however,heat
flux decreases because of fouling.
3. The tubewall temperature increases significantly with fin density. The
samefoulingfactor resultsinamuch higher tubewalltemperature for
finned tubes than for bare tubes. The tube wall temperature increases
from530 Fto760 Fwith5fins=in.,andfrom437 Fto516 Fforbare
(cid:2) (cid:2) (cid:2) (cid:2)
tubes. The effect of fouling is more pronounced in tubes of high fin
density,whichmeansthathighfindensitytubeshavetobekeptcleaner
than bare tubes. Demineralized water and good water treatment are
recommended in such situations.
8.25
Q:
How is the weight of solid and serrated fins determined?
Copyright © 2003 Marcel Dekker, Inc.

A: The weight of fins is given by the formulas
W 10:68 Fbn d h h 0:03 for solid fins
f ¼ (cid:4) (cid:4)ð oþ Þ(cid:4)ð þ Þ
W 10:68 Fbnd h 0:12 for serrated fins
f ¼ (cid:4) o(cid:4)ð þ Þ
where
W the fin weight, lb=ft (The segment width does not affect theweight.)
f ¼
b fin thickness, in.
¼
n fin density, fins=in.
¼
h fin height, in.
¼
d tube outer diameter, in.
o¼
Factor F corrects for material of fins and is given in Table 8.19 [9].
The weight of the tubes has to be added to the fin weight togive the total
weight of the finned tube. Tube weight per unit length is given by
W 10:68 F d t 68
t ¼ (cid:4) (cid:4) m(cid:4) m ð Þ
where
d mean diameter of tube, in.
m¼
t average wall thickness, in.
m¼
Example
Determine the weight of solid carbon steel fins on a 2in. OD tube if the fin
density is 5fins=in., height 0.75in., and thickness 0.05in. Average tubewall
¼ ¼
thickness is 0.120in.
TABLE8.19 Table ofF Factors
Material F
Carbonsteel 1
Type304, 316,321alloys 1.024
Type409, 410,430 0.978
Nickel 200 1.133
Inconel600,625 1.073
Incoloy 800 1.013
Incoloy 825 1.038
Hastelloy B 1.179
Copyright © 2003 Marcel Dekker, Inc.

Solution. F from Table 8.19 1. Using Eq. (67a), we have
¼
W 10:68 1 0:05 5 2 0:75
f ¼ (cid:4) (cid:4) (cid:4) (cid:4)ð þ Þ
0:75 0:03 5:725lb=ft
(cid:4)ð þ Þ¼
The tube weight has to be added to this. The tube weight is given by
W 10:68 1:94 0:12 2:49lb=ft
t ¼ (cid:4) (cid:4) ¼
Hence the total weight of the finned tube 2.49 5.725 8.215lb=ft.
¼ þ ¼
8.26
Q:
What is the effect of fin thickness and conductivity on boiler performance and
tube and fin tip temperatures?
A:
Table 8.20 gives the performance of a boiler evaporator using different fins.
2 0.120 carbon steel tubes; 26 tubes=row, 14 deep, 20ft long
4 (cid:4) 0.75 0.05 thick solid fins; surface area 35,831ft2
4 (cid:4) 0.75 (cid:4) 0.102 thick solid fins; surface area ¼ 36,426ft2
(cid:4) (cid:4) ¼
In-line arrangement, 4in. square pitch.
Gas flow 430,000lb=h at 1400 F in; vol%, CO 8.2, H O 20.9,
¼ (cid:2) 2¼ 2 ¼
N 67.51, O 3.1
2¼ 2¼
Steam pressure 635psig
Fouling factors ¼ 0.001ft2h F=Btu on both gas and steam.
(cid:2)
¼
It can be seen that
1. Due to the slightly larger surface area and higher heat transfer
coefficient, more duty is transferred with higher fin thickness.
TABLE8.20 Fin Configurationand Performance
Tube Fin
Fin cond. Fin thickness Duty temp. temp. U
(Btu=ft h F) (in.) (MMBtu=h) ( F) ( F) (Btu=ft2h F)
(cid:2) (cid:2) (cid:2) (cid:2)
25 0.05 104 673 996 8.27
25 0.102 106.35 692 874 9.00
15 0.05 98.35 642 1164 6.78
15 0.102 103.48 670 990 7.98
Copyright © 2003 Marcel Dekker, Inc.

2. The overall heat transfer coefficient is increased owing to higher fin
effectiveness for the same fin conductivity and greater fin thickness.
3. Lower fin conductivity reduces the fin effectiveness and the overall
heat transfer coefficient U, and hence less duty is transferred.
4. Thoughfintiptemperatureisreducedwithgreaterfinthickness,owing
to improved effectiveness the tube wall temperature increases. This is
due to the additional resistance imposed by the larger surface area.
8.27a
Q:
Is surface area an important criterion for evaluating different boiler designs?
A:
The answer is yes if the person evaluating the designs is knowledgeable in heat
transfer–related aspects and no if the person simply compares different designs
looking only for surface area information. We have seen this in the case of fire
tube boilers (Q8.11), where, due to variations in tube size and gas velocity,
differentdesignswithover40–50%differenceinsurfaceareaswereobtainedfor
thesameduty.Inthecaseofwatertubeboilersalso,duetovariationsintubesize,
pitch, and gas velocity, one can have different surface areas for the same duty;
hence one has to be careful in evaluating boilers based only on surface areas.
In the case of finned tube boilers, in addition to tube size, pitch, and
arrangement (staggered or in-line), one has to review the fin configuration—the
height,thickness,andfindensity.Thehigherthefindensityorratioofexternalto
internal surface area, the lower the overall heat transfer coefficient will be even
though the surface area can be 100–200% greater. It is also possible to transfer
more duty with less surface area by proper selection of fin geometry.
Example
AsuperheateristobedesignedfortheconditionsshowninTable8.21.Studythe
different designs possible with varying fin configurations.
Solution. Using the methods discussed above, various designs were
arrived at, with the results shown in Table 8.22 [10]. Several interesting
observations can be made. In cases 1 and 2, the same energyof 19.8MMBtu=h
is transferred; however, the surface area of case 2 is much higher because of the
highfindensity,whichdecreasesU,theoverallheattransfercoefficient.Also,the
tubewallandfintiptemperaturesarehigherbecauseofthelargeratioofexternal
to internal surface area.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.21 Data forHRSG Superheater
Gas flow 240,000lb=h
¼
Gas inlet temperature 1300 F
(cid:2)
¼
Gas analysis (vol%)
CO 7
2¼
H O 12
2 ¼
N 75
2¼
O 6
2¼
Comparingcases3and4,weseethatcase3transfersmoreenergywithless
surfaceareabecauseofbetterfinselection.Thusitisnotagoodideatoselector
evaluate designs based on surface area alone, because this can be misleading. In
addition, excessive fin surface can lead to higher tube wall and fin tip tempera-
tures, forcing one to use better materials and increasing the cost. Some purchas-
ing managers believe incorrectly that if they can get more surface area for the
sameprice,theyaregettingagooddeal.Nothingcouldbefurtherfromthetruth.
8.27b
Q:
Whenextendedsurfacesareused,thechoiceoffindensityisgenerallyarrivedat
basedonoptimizationstudiesasillustratedbelow.Varyingthefindensityaffects
TABLE8.22 Effect of FinGeometry onSuperheaterPerformance
Case1 Case2 Case3 Case4
Duty, MMBtu=h 19.8 19.87 22.62 22.44
Exitsteam temperature, F 729 730 770 768
(cid:2)
Gas pressuredrop, in.WC 0.8 1.3 1.2 1.5
Exitgas temp, F 1017 1016 976 979
(cid:2)
Fins=in. 2 4.5 2.5 5.5
Fin height,in. 0.5 0.75 0.75 0.625
Fin thickness,in. 0.075 0.075 0.075 0.075
Surfacearea, ft2 2965 5825 5223 7106
Maxtubewall temp, F 890 968 956 988
(cid:2)
Fin tiptemperature, F 996 1095 1115 1069
(cid:2)
Overall heattransfercoeff, 12.1 6.19 8.49 6.16
F
(cid:2)
Tube-side pressuredrop, psi 12 8 12.3 10
Number ofrows deep 6 4 6 5
Copyright © 2003 Marcel Dekker, Inc.

the gas pressure drop, surface area, and weight of the boiler, not to mention the
tube wall and fin tip temperatures. An incineration plant evaporator is to be
designed to cool 550,000lb=h of clean flues gases from 1000 F to about 460 F.
(cid:2) (cid:2)
Steampressureis250psigsat.Feedwaterenterstheevaporatorat230 F.Fluegas
(cid:2)
analysis (vol%) is CO 7, H O 12, N 75 O 6. Fouling factors are
0.001ft2h F=Btu on b 2 o ¼ th the 2 gas ¼ and ste 2 a ¼ m sides 2 . ¼ Study the effect of fin
(cid:2)
configuration on the design.
A:
The calculation procedure for finned tubes is detailed in Q8.19a–Q8.19c. Only
theresultsfromusingacomputerprogramwillbediscussedhere.Usingserrated
finsofdensity2,4,and6fins=in.,0.75in.high,0.05in.thickwith30tubes=row,
4in. square pitch configuration, the lengths were varied to obtain different gas
mass velocities. The number of rows deep was adjusted to obtain an exit gas
temperature of about 460 F or a duty of about 82MMBtu=h. Figure 8.8 shows
(cid:2)
the results from the study.
As the gas mass velocity increases we see that the gas pressure drop
increases, whereas the surface area decreases for both 2 and 6 fins=in.
designs, which should be obvious. The surface area required for the 6
fins=in. design is much larger than with 2 fins=in. As discussed in
Q8.27a, the heat transfer coefficient with higher fin density or large
external fin surface area is lower. The weight of the tube bundle is also
higher with higher fin density.
FIGURE8.8 EffectoffingeometryonHRSGsurfaceareaandgaspressuredrop.
Copyright © 2003 Marcel Dekker, Inc.

Table 8.23 summarizes the designs for the 2 and 6 fins=in. cases for the
same duty and gas pressure drop of 4in.WC. It is seen that the surface
areaismuchlargerwiththe6fins=in.design.Thetubewalltemperature
isalsohigherduetothehigherheatflux,andtheweightisslightlymore.
However, the fabrication cost may be less due to the smaller number of
rows deep. Depending on the design, the drum length could also be
smaller due to this. One may evaluate these factors and select the
optimum design.
Note on Surface Areas
As discussed earlier, surface areas from different designs should be interpreted
carefully. One should not select a design based on surface area considerations.
Withhigherfindensity,theheattransfercoefficientwillbelowerandviceversa.
Simply looking at a spreadsheet that shows surface areas of tubes of different
suppliers and deciding that the design with more surface area is better is
technically incorrect. As can be seen below, the higher surface area option has
higher tube wall temperature and heat flux inside the tubes. If one wants to
compare alternative designs, one should look at UA, the product of overall heat
transfer coefficient U and surface area A and not the surface area alone. The
equationforenergytransferisQ UADT:QandDT beingthesame,UAshould
¼
be constant for thevarious options. Unless one knows how to calculate the heat
transfer coefficients, comparison of surface areas alone should not be attempted,
becauseitcanbemisleading.Factorssuchastubesize,spacing,geometry,andfin
configurationaffectU.Thediscussionalsoappliestofiretubeboilers,wheretube
sizes and gas velocities can impact surface areas.
TABLE8.23 DesignofaBoilerwith2and6Fins=in.
Fins=in. 2 6
Gas massvelocity, lb=ft2h 7500 8000
Surfacearea, ft2 32,500 50,020
Tube wall temp, F 488 542
(cid:2)
Fin tiptemp, F 745 724
(cid:2)
Tubes wide 30 30
Tube length,ft 16 17.6
No.of rowsdeep 26 14
Weight, lb 59,650 64,290
Copyright © 2003 Marcel Dekker, Inc.

8.28
Q:
How are tubular air heaters designed?
A:
LetW ,andW bethegasandairquantities.Normally,fluegasflowsinsidethe
g a
tubeswhile air flows across thetubes incrossflowfashion,as shownin Fig. 8.9.
Carbon steel tubes of 11–3.0in. OD are generally used. Thickness ranges from
2
0.06to0.09in.becausehighpressuresarenotinvolved.Thetubesarearrangedin
in-line fashion and are connected to the tube sheets at the ends. More than one
blockmaybeusedinseries;inthiscase,airflowsacrossthetubebundleswitha
few turns. Hence, while calculating log-mean temperature difference, we must
consider correction factors F .
T
Flue gas velocity is in the range of 40–70fps, and air-side mass velocities
range from 4000 to 8000lb=ft2h. N and N , the numbers of tubes wide and
w d
deep,canbedecidedonthebasisofductdimensionsleadingtotheairheater.In
the case of a separate heater, we have the choice of N or N . In a boiler, for
w d
example, duct dimensions at the economizer section fix dimensions of the air
heater also, because the air heater is located below the economizer.
To size the air heater, first determine the total number of tubes N [1]:
t
0:05W
N g 69
t ¼ d2r V ð Þ
i g g
S =d and S =d range from 1.25 to 2.0. For the gas-side heat transfer coefficient
T L
h, Eq. (12) is used:
i
C
h 2:44 w0:8
i ¼ (cid:4) d1:8
i
Values of C are evaluated at average flue gas temperature.
Theair-sideheattransfercoefficienth isgivenbyEq.(19)(variationinh
o o
between staggered and in-line arrangements is small in the range of Reynolds
number and pitches one comes across),
F
h 0:9 G0:6
o ¼ (cid:4) d0:4
The value h is calculated at air film temperature.
o
Because the temperature drops across the gas and air films are nearly the
same,unlikeinanevaporatororsuperheater,filmtemperatureisapproximatedas
t 3t t =4 70
f ¼ð gþ aÞ ð Þ
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.9 Tubularair heater.
Copyright © 2003 Marcel Dekker, Inc.

wheret andt refertotheaverageofgasandairtemperatures.CalculateU using
g a
1 1 d 1
(cid:4) 71
U ¼ hd þh ð Þ
i i o
Metal resistance is neglected. Air-and gas-side pressure drops can be computed
by Eqs. (26) and (28) of Chapter 7, after surfacing is done:
L 5d
DP g ¼ 93 (cid:4) 10 (cid:3) 6 (cid:4) fw2 r þ d5 i
g i
N
DP 9:3 10 10 fG2 d
air ¼ (cid:4) (cid:3) (cid:4) r
air
It is also good to check for partial load performance to see if dew point
corrosion problemsare likely. Methodslike air bypass or steam-air heating must
be considered. Vibration of tube bundles must also be checked.
C and F are given in Table 8.24 for easy reference.
Example
A quantity of 500,000lb=h of flue gas from a boiler is cooled from 700 F;
(cid:2)
400,000lb=hofairat80 Fisheatedto400 F.Designasuitabletubularairheater.
(cid:2) (cid:2)
Carbon steel tubes of 2in. OD and 0.087in. thickness are available.
Solution. Assume that duct dimensions are not a limitation. Hence, the
bundle arrangement is quite flexible. Choose S =d 1.5 and S =d 1.25in. in-
T ¼ L ¼
line; use a maximum flue gas velocity of 50ft=s.
Fromanenergybalance,assumingnegligiblelossesandforaspecificheat
of 0.25 for gas and 0.24 for the air side,
Q 500;000 0:25 700 t
¼ (cid:4) (cid:4)ð (cid:3) Þ
400;000 0:24 400 80
¼ (cid:4) (cid:4)ð (cid:3) Þ
30:7 106 Btu=h
¼ (cid:4)
TABLE8.24 C and F Factors for Calculating h
i
and h ofTubular Air
o
Temp( F) C F
(cid:2)
200 0.162 0.094
400 0.172 0.103
600 0.18 0.110
800 0.187 0.116
Copyright © 2003 Marcel Dekker, Inc.

Hence, the gas temperature leaving the air heater is 454 F. The average flue gas
(cid:2)
temperature is (700 454)=2 577 F. Let the molecular weight of the flue gas
(cid:2)
þ ¼
be 30. Then
30 492
r 0:0396lb=cuft
g ¼359(cid:4)460 577¼
þ
From Eq. (69),
0:05 500;000
N (cid:4) 3800
t ¼1:8262 0:0396 50¼
(cid:4) (cid:4)
S 3:0in:; S 2:5in:
T ¼ L ¼
Let N 60. Hence, the width of the air heater is
w¼
3:0
60 15ft
(cid:4) 12 ¼
N 63becauseN N N ;so
d ¼ t ¼ w(cid:4) d
Depth 63 2:5=12 13:2ft
¼ (cid:4) ¼
At 577 F, from Table 8.24 we have C 0.178:
(cid:2)
¼
500;000 0:8 0:178
h 2:44
i ¼ (cid:4) 3780 (cid:4) 1:826 1:8
(cid:1) (cid:2) ð Þ
7:2Btu=ft2 h F
(cid:2)
¼
Toestimateh ; Gisrequired.ThisrequiresanideaofL.Wemustassumea
o
valueforthelengthandchecklatertoseeifitissufficient.Hence,itisatrial-and-
error approach. Try L 15ft:
¼
S d 1
FGA T (cid:3) N L 60 15 75ft2
¼ 12 (cid:4) w ¼12(cid:4) (cid:4) ¼
G 400;000=75 5333lb=ft2 h
¼ ¼
Average gas and air temperatures are
t 577 F; t 240 F
g ¼ (cid:2) a ¼ (cid:2)
3 577 240
t f ¼ (cid:4) 4 þ ¼ 492 (cid:2) F
Copyright © 2003 Marcel Dekker, Inc.

From Table 8.24, F is 0.105. Then
h 0:9 53330:6 0:105=20:4 12:3Btu=ft2h F
o ¼ (cid:4) (cid:4) ¼ (cid:2)
1 1 2:0 1
U ¼7:2(cid:4)1:826þ12:3
0:152 0:081 0:233
¼ þ ¼
U 4:3Btu=ft2 h F
(cid:2)
¼
We must calculate F , the correction factor for DT, for the case of one fluid
T
mixed and the other unmixed. From Fig. 8.10 (single-pass crossflow),
700 454
R (cid:3) 0:77
¼ 400 80 ¼
(cid:3)
400 80
P (cid:3) 0:516
¼700 80¼
(cid:3)
F 0:9
T ¼
Therefore,
454 80 700 400
DT 0:9 ð (cid:3) Þ(cid:3)ð (cid:3) Þ 302 (cid:2) F
¼ (cid:4) ln 374=300 ¼
ð Þ
Q 30:7 106
A (cid:4) 23;641ft2
¼U DT ¼ 4:3 302 ¼
(cid:4) (cid:4)
p 2
(cid:4) 3780L
¼ 12 (cid:4)
L 11:95ft
¼
Hence, the assumed L is not correct. Try L 11.0ft.
¼
11
FGA 75 55ft2
¼15(cid:4) ¼
G 7272lb=ft2 h
¼
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.10 Crossflow correctionfactors(From Refs.1and 2).
Copyright © 2003 Marcel Dekker, Inc.

Taking ratios,
7272 0:6
h 12:3 14:8Btu=ft2 h F
o ¼ 5333 (cid:4) ¼ (cid:2)
(cid:1) (cid:2)
1 1 2:0 1
(cid:4) 0:152 0:067
U ¼7:2 1:826þ14:8¼ þ
(cid:4)
0:219
¼
U 4:56Btu=ft2 h F
(cid:2)
¼
30:7 106
A (cid:4) 22;293ft2; L 11:25ft
¼4:56 302¼ ¼
(cid:4)
Thecalculatedandassumedlengthsareclosetoeachother,andthedesign
maybefrozen.Checkthemetaltemperatureattheexitportion.Becausethegas-
sideresistanceandairfilmresistancesare0.152and0.067,themetaltemperature
at theexitofthe air heater can be calculated as follows. The dropacross thegas
film will be
0:152 454 80
ð (cid:3) Þ 260 (cid:2) F
0:152 0:067 ¼
þ
Metal temperature will be 4547260 194 F.
(cid:2)
¼
If the flue gas contains sulfur, dew point corrosion may occur at the exit.
The air-side heat transfer coefficient is high, so the drop across its film is low
compared to the gas-side film drop. If we increase the flue gas heat transfer
coefficient,thedropacrossitsfilmwillbelowandthemetaltemperaturewillbe
higher.
8.29
Q:
How is the off-design performance evaluated?
The air heater described in Q8.28 works at partial loads. W
g¼
300,000lb=h, and flue gas enters the air heater at 620 F. W 250,000lb=h,
(cid:2) a¼
and the air temperature is 80 F. Check the exit gas temperatures of gas and air.
(cid:2)
A:
Assume the gas leaves the air heater at 400 F. Then
(cid:2)
Q 300;000 0:25 620 400
¼ (cid:4) (cid:4)ð (cid:3) Þ
250;000 0:24 t 80 16:5 106
¼ (cid:4) ð (cid:3) Þ¼ (cid:4)
Air temperature leaving 355 F
(cid:2)
¼
Copyright © 2003 Marcel Dekker, Inc.

To calculate h and h , see Table 8.24. At an average flue gas temperature
i o
of 620 400 =2 510 F; C 0:175: And at a film temperature of
(cid:2)
ð þ Þ ¼ ¼
3 510 355 80 =2=4 437 F;F 0:104.
(cid:2)
½ (cid:4) þð þ Þ (cid:5) ¼ ¼
300;000 0:8 0:175
h 2:44
i ¼ (cid:4) 3825 (cid:4) 1:826 1:8
(cid:1) (cid:2) ð Þ
4:75Btu=ft2 h F
(cid:2)
¼
250;000
G 3333lb=ft2 h
¼ 75 ¼
3333 0:6
h o ¼ 0:9 (cid:4) ð 20:4 Þ (cid:4) 0:104 ¼ 9:22Btu=ft2 h (cid:2) F
1 2 1
0:238
U ¼1:826 4:73þ9:22¼
(cid:4)
U 4:22Btu=ft2 h F
(cid:2)
¼
From Fig. 8.10,
355 80
P (cid:3) 0:51
¼620 80¼
(cid:3)
620 400
R (cid:3) 0:8
¼ 355 80 ¼
(cid:3)
F 0:9
T ¼
400 80 620 355
DT 0:9 ð (cid:3) Þ(cid:3)ð (cid:3) Þ 262 (cid:2) F
¼ (cid:4) ln 320=265 ¼
ð Þ
Transferred Q 4.2 262 23,640 26 106Btu=h, and assumed
Q 16.5 106Btu=h. ¼ They (cid:4) don’t (cid:4) tally. ¼ (cid:4)
¼ (cid:4)
Since the air heater can transfer more energy, assume a higher air
temperature, 390 F, at the exit:
(cid:2)
Q 250;000 0:24 390 80 18:6 106
¼ (cid:4) ð (cid:3) Þ¼ (cid:4)
300;000 0:25 620 t
¼ (cid:4) (cid:4)ð (cid:3) Þ
Then gas temperature leaving 372 F.
(cid:2)
Assume U remains the s ¼ ame at 4.2Btu=ft2h F. Then
(cid:2)
R 0:8; P 0:574; F 0:82
¼ ¼ T ¼
DT 213 F
(cid:2)
¼
TransferredQ 4:2 23;640 213
¼ (cid:4) (cid:4)
21:1 106 Btu=h
¼ (cid:4)
Copyright © 2003 Marcel Dekker, Inc.

Again, they don’t tally. Next, try Q 20 106Btu=h.
¼ (cid:4)
Air temperature leaving 410 F
(cid:2)
¼
Gas temperature leaving 353 F
(cid:2)
¼
F 0.75, DT 0.75 242 182 F
T¼ ¼ (cid:4) ¼ (cid:2)
TransferredQ 4:2 23;640 182 18 106Btu=h
¼ (cid:4) (cid:4) ¼ (cid:4)
Again, try an exit air temperature at 400 F. Then
(cid:2)
Q 250;000 0:24 400 80
¼ (cid:4) (cid:4)ð (cid:3) Þ
19:2 106Btu=h
¼ (cid:4)
19:2 106
Exit gas temperature 620 (cid:4)
¼ (cid:3)300;000 0:25
(cid:4)
364 F
(cid:2)
¼
320
R 0:8; P 0:593; F 0:77
¼ ¼540¼ T ¼
284 220
DT 0:77 (cid:3) 193 (cid:2) F
¼ (cid:4)ln 284=220 ¼
ð Þ
TransferredQ 4:2 193 23;640 19:16 106 Btu=h
¼ (cid:4) (cid:4) ¼ (cid:4)
Q 19:2 106 Btu=h
¼ (cid:4)
The gas leaves at 364 Fagainst 454 Fat full load.
(cid:2) (cid:2)
Metal temperature can be computed as before. At lower loads, metal
temperature is lower, and the air heater should be given some protection. This
protectionmaytaketwoforms:Bypasspartoftheairorusesteamtoheattheair
entering the heater to 100–120 F. Either of thesewill increase the average metal
(cid:2)
temperatureoftheairheater.Inthefirstcase,theair-sideheattransfercoefficient
will fall. Because U decreases, the gas temperature leaving the air heater will
increaseandlessQwillbetransferred.Hence,metaltemperaturewillincrease.In
the second case, air temperature entering increases, so protection of the metal is
ensured.Again,thegastemperaturedifferentialattheexitwillbehigher,causing
a higher exit gas temperature.
Example
Solve the problem using the NTU method.
Copyright © 2003 Marcel Dekker, Inc.

Solution. Often the NTU method is convenient when trial-and-error
calculations of the type shown above are involved.
UA 4:2 23;640
NTU (cid:4) 1:65
¼C ¼250;000 0:24¼
min (cid:4)
C 250;000 0:24
mixed (cid:4) 0:80
C ¼300;000 0:25¼
unmixed (cid:4)
e effectiveness
¼
C
1 exp max 1 exp NTU C
¼ (cid:3) f(cid:3)C ½ (cid:3) ð(cid:3) (cid:4) Þ(cid:5)g 72
min
ð Þ
1 exp 1:251 exp 1:65 0:8
¼ (cid:3) f(cid:3) ½ (cid:3) ð(cid:3) (cid:4) Þ(cid:5)g
0:59
¼
air temperature rise
Effectiveness 0:59
¼ ¼ 620 80
(cid:3)
Air temperature rise 319 F
(cid:2)
¼
Air temperature leaving 319 80 399 F
(cid:2)
¼ þ ¼
This compares well with the answer of 400 F. When U does not change
(cid:2)
much, this method is very handy.
8.30
Q:
Predict the exit gas and water temperatures and the energy transferred in an
economizer under the following conditions:
t gas temperature in 1000 F
g1¼ ¼ (cid:2)
t water temperature in 250 F
w
A
1¼
surface area 6000ft
¼2 (cid:2)
¼ ¼
W gas flow 75,000lb=h
g¼ ¼
W water flow 67,000lb=h
U w¼ overall hea ¼ t transfer coefficient 8Btu=ft2h F
(cid:2)
¼ ¼
C gas specific heat 0.265Btu=lb F
pg¼ ¼ (cid:2)
C water specific heat 1Btu=lb F
pw¼ ¼ (cid:2)
A:
Figure8.11showsthearrangementofaneconomizer.Atrial-and-errormethodis
usuallyadoptedtosolveforthedutyofanyheattransferequipmentifthesurface
area is known. This procedure is detailed in Q8.29. Alternatively, the numberof
transferunits(NTU)methodpredictstheexittemperaturesandduty.Formoreon
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.11 Economizer.
this theory, the reader is referred to any textbook on heat transfer [2]. Basically,
the duty Q is given by
Q eC t t 73
¼ minðg1(cid:3) w1Þ ð Þ
where e depends on the type of flow, whether counterflow, parallel flow, or
crossflow. In economizers, usually a counterflow arrangement is adopted. e for
this is given by
1 exp NTU 1 C
e (cid:3) ½(cid:3) (cid:4)ð (cid:3) Þ(cid:5) 74
¼1 C exp NTU 1 C ð Þ
(cid:3) ½(cid:3) (cid:4)ð (cid:3) Þ(cid:5)
where
UA WC
NTU and C ð pÞmin
¼C ¼ WC
min ð pÞmax
WC 75;000 0:265 19;875
ð pÞmin ¼ (cid:4) ¼
WC 67;000 1 67;000
ð pÞmax ¼ (cid:4) ¼
19;875
C 0:3
¼67;000¼
6000
NTU 8 2:42
¼ (cid:4)19;875¼
Substituting into Eq. (74) yields
1 exp 2:42 0:7
e (cid:3) ð(cid:3) (cid:4) Þ 0:86
¼1 0:3 exp 2:42 0:7 ¼
(cid:3) (cid:4) ð(cid:3) (cid:4) Þ
Copyright © 2003 Marcel Dekker, Inc.

From Eq. (73),
Q 0:86 19;875 1000 250
¼ (cid:4) (cid:4)ð (cid:3) Þ
12:8 106 Btu=h
¼ (cid:4)
Let us calculate the exit water and gas temperatures.
Q W C t t W C t t
¼ w pwðw2(cid:3) w1Þ¼ g pgðg1(cid:3) g2Þ
Hence,
106
t 250 12:8 441 F
w2 ¼ þ (cid:4)67;000 1¼ (cid:2)
(cid:4)
106
t 1000 12:8 355 F
g2 ¼ (cid:3) (cid:4)75;000 0:265¼ (cid:2)
(cid:4)
TheNTUmethodcanbeusedtoevaluatetheperformanceofothertypesof
heat transfer equipment, Table 8.25 gives the effectiveness factor e.
TABLE8.25 Effectiveness Factors
Exchangertype Effectiveness
1 exp NTU 1 C
Parallelflow, single-pass e (cid:3) ½(cid:3) (cid:4)ð þ Þ(cid:5)
¼ 1 C
þ
1 exp NTU 1 C
Counterflow,single-pass e (cid:3) ½(cid:3) (cid:4)ð (cid:3) Þ(cid:5)
¼1 C exp NTU 1 C
(cid:3) ½(cid:3) (cid:4)ð (cid:3) Þ(cid:5)
1 exp NTU 1 C2 1=2
e 2 1 C þ ½(cid:3) (cid:4)ð þ Þ (cid:5)
Shell-and-tube (oneshellpass; 1¼ " þ þ1 exp NTU 1 C2 1=2
2, 4,6, etc.,tubepasses) (cid:3) ½(cid:3) (cid:4)ð þ Þ (cid:5)
1
(cid:3)
1 C2 1=2
(cid:4)ð þ Þ #
Shell-and-tube (n shell passes; 1 e C n 1 e C n (cid:3) 1
e (cid:3) 1 1 (cid:3) 1 C
2n, 4n, 6n,etc., tubepasses) n ¼ 1 e (cid:3) 1 e (cid:3)
(cid:6)(cid:1) (cid:3) 1 (cid:2) (cid:7)(cid:6)(cid:1) (cid:3) 1 (cid:2) (cid:7)
Crossflow, bothstreams e 1 exp C NTU0:22exp C
unmixed (cid:10) (cid:3) NTU0 f :78 (cid:4) 1 ½ ð(cid:3)
(cid:4) Þ(cid:3) (cid:5)g
NTU
Crossflow, bothstreamsmixed e NTU
¼ 1 exp NTU
(cid:6) (cid:3) ð(cid:3) Þ
NTU C (cid:3) 1
(cid:4) 1
þ 1 exp NTU C (cid:3)
(cid:3) ð(cid:3) (cid:4) Þ (cid:7)
Crossflow, streamC unmixed e C 1 exp C 1 exp NTU
min ¼ f (cid:3) ½(cid:3) ½ (cid:3) ð(cid:3) Þ(cid:5)(cid:5)g
Crossflow, streamC unmixed e 1 exp C1 exp NTU C
max ¼ (cid:3) f(cid:3) ½ (cid:3) ð(cid:3) (cid:4) Þ(cid:5)g
Copyright © 2003 Marcel Dekker, Inc.

8.31
Q:
How is the natural or free convectionheat transfer coefficient in air determined?
A:
Thesituations of interesttosteam plantengineerswouldbethoseinvolvingheat
transfer between pipes or tubes and air as when an insulated pipe runs across a
room or outside it and heat transfer can take place with the atmosphere.
Simplified forms of these equations are the following [12].
1. Horizontal pipes in air:
DT 0:25
h 0:5 75a
c ¼ (cid:4) d ð Þ
(cid:1) o(cid:2)
where
DT temperature difference between the hot surface and cold
¼
fluid, F
(cid:2)
d tube outside diameter, in.
o¼
2. Long vertical pipes:
DT 0:25
h 0:4 75b
c ¼ (cid:4) d ð Þ
(cid:1) o(cid:2)
3. Vertical plates less than 2ft high:
DT 0:25
h 0:28 75c
c ¼ z ð Þ
(cid:1) (cid:2)
where z height, ft.
¼
4. Vertical plates more than 2ft high:
h 0:3 DT 0:25 75d
c ¼ (cid:4)ð Þ ð Þ
5. Horizontal plates facing upward:
h 0:38 DT 0:25 75e
c ¼ (cid:4)ð Þ ð Þ
6. Horizontal plates facing downward:
h 0:2 DT 0:25 75f
c ¼ (cid:4)ð Þ ð Þ
Example
Determinetheheattransfercoefficientbetweenahorizontalbarepipeofdiameter
4.5in. at 500 Fand atmospheric air at 80 F.
(cid:2) (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

Solution.
500 80 0:25
h c ¼ 0:5 (cid:4) 4 (cid:3) :5 ¼ 1:55Btu=ft2 h (cid:2) F
(cid:1) (cid:2)
Note that the above equations have been modified to include the effect of wind
velocity in the insulation calculations; see Q8.51.
8.32
Q:
How is the natural or free convection heat transfer coefficient between tube
bundles and liquids determined?
A:
One has to determine the free convection heat transfer coefficient when tube
bundlessuchasdesuperheatercoilsordrumpreheatcoilsareimmersedinboiler
waterinordertoarriveattheoverallheattransfercoefficientandthenthesurface
area. Drum coil desuperheaters are used instead of spray desuperheaters when
solids are not permitted to be injected into steam. The heat exchanger is used to
coolsuperheatedsteam(Fig.8.12),whichflowsinsidethetubeswhilethecooler
waterisoutsidethetubesinthedrum.Drumheatingcoilsareusedtokeepboiler
water hot for quick restart or to prevent freezing.
Inthisheatexchanger,steamcondensesinsidetubeswhilethecoolerwater
isoutsidethetubes.Thenaturalconvectioncoefficientbetweenthecoilanddrum
water has to be determined to arrive at the overall heat transfer coefficient and
then the size or surface area.
The equation that relates h with other parameters is [2]
c
d3r2gbDT mC 0:25
Nu 0:54 p 76
¼ m2 (cid:4) k ð Þ
(cid:1) (cid:2)
FIGURE 8.12 Exchanger inside boilerdrum.
Copyright © 2003 Marcel Dekker, Inc.

Simplifying the above we have
r2bDTC 0:25
h 144 k3 p 77
c ¼ (cid:4) (cid:4) md ð Þ
(cid:1) o (cid:2)
where
d tube outer diameter, in.
o¼
k fluid thermal conductivity, Btu=fth F
(cid:2)
¼
C fluid specific heat, Btu=lb F
b
p¼
volumetric expansion coef
(cid:2)
ficient, R 1
(cid:2) (cid:3)
¼
DT temperature difference between tubes and liquid, F
(cid:2)
¼
m viscosity of fluid, lb=fth
r ¼ fluid density, lb=ft3
¼
InEq.(77)allthefluidpropertiesareevaluatedatthemeantemperaturebetween
fluidandtubesexceptfortheexpansioncoefficient,whichisevaluatedatthefluid
temperature.
Fluid properties at saturation conditions are given in Table 8.26.
Example
1in. pipes are used to maintain boiler water at 100 F in a tank using steam at
(cid:2)
212 F, which is condensed inside the tubes. Assume that the pipes are at 200 F,
(cid:2) (cid:2)
andestimatethefreeconvectionheattransfercoefficientbetweenpipesandwater.
Solution. From Table 8.26, at a mean temperature of 150 F,
(cid:2)
k 0:381; m 1:04; b 0:0002; r 61:2
¼ ¼ ¼ f ¼
C 1:0; DT 100; d 1:32
p ¼ ¼ o ¼
61:22 1:0 0:0002 100 0:25
h 144 0:3813 (cid:4) (cid:4) (cid:4)
c ¼ (cid:4) (cid:4) 1:04 1:32
(cid:1) (cid:4) (cid:2)
188Btu=ft2 h F
(cid:2)
¼
8.33
Q:
Estimate the surface area of the heat exchanger required to maintain water in a
boilerat100 Fusingsteamat212 FasintheexampleofQ8.32.Assumethatthe
(cid:2) (cid:2)
heat loss to the cold ambient from the boiler is 0.5MMBtu=h. Steam is
condensed inside the tubes. 1in. schedule 40 pipes are used.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.26 Properties of SaturatedWater
t C r m v k a b
p
(cid:2)F (Btu=lb
(cid:2)
F) (lb=ft3) (lb=ft h) (ft2=h) (Btu=hft
(cid:2)
F) (ft2=h) (cid:2)R(cid:3) 1 N
ð Þ ð Þ
32 1.009 62.42 4.33 0.0694 0.327 0.0052 0.03 10(cid:3) 3 13.37
(cid:4)
40 1.005 62.42 3.75 0.0601 0.332 0.0053 0.045 11.36
50 1.002 62.38 3.17 0.0508 0.338 0.0054 0.070 9.41
60 1.000 62.34 2.71 0.0435 0.344 0.0055 0.10 7.88
70 0.998 62.27 2.37 0.0381 0.349 0.0056 0.13 6.78
80 0.998 62.17 2.08 0.0334 0.355 0.0057 0.15 5.85
90 0.997 62.11 1.85 0.0298 0.360 0.0058 0.18 5.13
100 0.997 61.99 1.65 0.0266 0.364 0.0059 0.20 4.52
110 0.997 61.84 1.49 0.0241 0.368 0.0060 0.22 4.04
120 0.997 61.73 1.36 0.0220 0.372 0.0060 0.24 3.65
130 0.998 61.54 1.24 0.0202 0.375 0.0061 0.27 3.30
140 0.998 61.39 1.14 0.0186 0.378 0.0062 0.29 3.01
150 0.999 61.20 1.04 0.0170 0.381 0.0063 0.31 2.72
160 1.000 61.01 0.97 0.0159 0.384 0.0063 0.33 2.53
170 1.001 60.79 0.90 0.0148 0.386 0.0064 0.35 2.33
180 1.002 60.57 0.84 0.0139 0.389 0.0064 0.37 2.16
190 1.003 60.35 0.79 0.0131 0.390 0.0065 0.39 2.03
200 1.004 60.13 0.74 0.0123 0.392 0.0065 0.41 1.90
210 1.005 59.88 0.69 0.0115 0.393 0.0065 0.43 1.76
220 1.007 59.63 0.65 0.0109 0.395 0.0066 0.45 1.66
230 1.009 59.38 0.62 0.0104 0.395 0.0066 0.47 1.58
240 1.011 59.10 0.59 0.0100 0.396 0.0066 0.48 1.51
250 1.013 58.82 0.56 0.0095 0.396 0.0066 0.50 1.43
260 1.015 58.51 0.53 0.0091 0.396 0.0067 0.51 1.36
270 1.017 58.24 0.50 0.0086 0.396 0.0067 0.53 1.28
280 1.020 57.94 0.48 0.0083 0.396 0.0067 0.55 1.24
290 1.023 57.64 0.46 0.0080 0.396 0.0067 0.56 1.19
300 1.026 57.31 0.45 0.0079 0.395 0.0067 0.58 1.17
350 1.044 55.59 0.38 0.0068 0.391 0.0067 0.62 1.01
400 1.067 53.65 0.33 0.0062 0.384 0.0068 0.72 0.91
450 1.095 51.55 0.29 0.0056 0.373 0.0066 0.93 0.85
500 1.130 49.02 0.26 0.0053 0.356 0.0064 1.18 0.83
550 1.200 45.92 0.23 0.0050 0.330 0.0060 1.63 0.84
600 1.362 42.37 0.21 0.0050 0.298 0.0052 — 0.96
A:
The overall heat transfer coefficient can be estimated from
1 1 1
R ff ff
U ¼h þh þ mþ iþ o
o o i
Copyright © 2003 Marcel Dekker, Inc.

where R metal resistance, and ff and ff are inside and outside fouling
m¼ i o
factors; see Eq. (3).
h ,thefreeconvectionheattransfercoefficientbetweenthetubesandboiler
o
water, obtained from Q8.32, 188Btu=ft2h F. Assume h 1500, ff ff
¼ (cid:2) i¼ i ¼ o¼
0.001, and
d d
Metal resistanceR o ln o 0:0005
m ¼24K d ¼
i
Then
1 1 1
0:0025 0:00849
U ¼188þ1500þ ¼
o
or
U 177Btu=ft2 h F
o ¼ (cid:2)
DT log-mean temperature difference 212 100 112 F
(cid:2)
¼ ¼ (cid:3) ¼
Then,
Q 500;000
Surface areaA 38ft2
¼U DT ¼117 112¼
o (cid:4)
8.34
Q:
Can we determine gas or steam temperature profiles in a heat recovery steam
generator (HRSG) without actually designing it?
A:
Yes. One can simulate the design as well as the off-design performance of an
HRSG without designing it in terms of tube size, surface area, etc. The
methodology has several applications. Consultants and plant engineers can
determine for a given set of gas inlet conditions for an HRSG how much
steamcanbegeneratedandwhatthegas=steamtemperatureprofilewilllooklike,
andhencewritebetterspecifications for theHRSGorselectauxiliariesbased on
this simulation without going to a boiler firm for this information. Thus several
options can be ruled out or ruled in depending on the HRSG performance. The
methodology has applications in complex, multipressure cogeneration or
combined cycle plant evaluation with gas turbines. More information on
HRSG simulation can be found in Chapters 1 and 3 and Refs. 11, 12.
Copyright © 2003 Marcel Dekker, Inc.

Example
140,000lb=h of turbine exhaust gases at 980 F enter an HRSG generating
(cid:2)
saturated steam at 200psig. Determine the steam generation and temperature
profiles if feedwater temperature is 230 F and blowdown 5%. Assume that
(cid:2)
¼
average gas specific heat is 0.27 at the evaporator and 0.253 at the economizer.
Twoimportanttermsthatdeterminethedesignshouldbedefinedhere(see
Fig. 8.13). Pinchpoint is the difference between thegas temperature leaving the
evaporator and saturation temperature. Approach point is the difference between
the saturation temperature and the water temperature entering the evaporator.
More information on how to select these important values and how they are
influenced by gas inlet conditions is discussed in examples below.
For unfiredgasturbineHRSGs,pinch andapproachpointslieintherange
of 15–30 F. The higher thesevalues, thesmaller will be theboiler size and cost,
(cid:2)
and vice versa.
Let us choose a pinch point of 20 F and an approach point of 15 F.
(cid:2) (cid:2)
Saturation temperature 388 F. Figure 8.14 shows the temperature profile. The
(cid:2)
¼
gas temperature leaving the evaporator 388 20 408 F, and water tempera-
(cid:2)
¼ þ ¼
ture entering it 388715 373 F.
(cid:2)
¼ ¼
Evaporator duty 140;000 0:99 0:27 980 408
¼ (cid:4) (cid:4) (cid:4)ð (cid:3) Þ
21:4MMBtu=h
¼
(0.99 is the heat loss factor with a 1% loss.)
Enthalpy absorbed by steam in evaporator
1199:3 345 0:05 362:2 345
¼ð (cid:3) Þþ (cid:4)ð (cid:3) Þ
855:2Btu=lb
¼
(1199.3, 345, and 362.2 are the enthalpies of saturated steam, water entering the
evaporator,andsaturatedwater,respectively.0.05istheblowdownfactorfor5%
blowdown.)
FIGURE 8.13 Pinch andapproachpoints.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.14 Temperature profileinanHRSG.
Hence
21:4 106
Steam generated (cid:4) 25;000lb=h
¼ 855:2 ¼
Economizer duty 25;000 1:05 345 198:5
¼ (cid:4) (cid:4)ð (cid:3) Þ
3:84MMBtu=h
¼
3;840;000
Gas temperature drop
¼140;000 0:253 0:99
(cid:4) (cid:4)
109 F
(cid:2)
¼
Hence gas temperature leaving economizer 4087109 299 F. Thus the
(cid:2)
¼ ¼
thermal design of the HRSG is simulated.
8.35a
Q:
Simulate the performance of the HRSG designed in Q8.34 when a gas flow of
165,000lb=h enters the HRSG at 880 F. The HRSG will operate at 150psig.
(cid:2)
Feedwater temperature remains at 230 F.
(cid:2)
A:
Gas turbine exhaust flow and temperature change with ambient conditions and
load.AsaresulttheHRSGhastooperateatdifferentgasparameters,andhence
simulationisnecessarytodeterminehowtheHRSG behavesunder different gas
and steam parameters.
Copyright © 2003 Marcel Dekker, Inc.

TheevaporatorperformancecanbedeterminedbyusingEq.(37).Basedon
design conditions, compute K.
980 388
ln (cid:3) K 140;000 (cid:3) 0:4 3:388
408 388 ¼ (cid:4)ð Þ ¼
(cid:6) (cid:3) (cid:7)
K 387:6
¼
Under the new conditions,
880 366
ln (cid:3) 387:6 165;000 (cid:3) 0:4 3:1724
" t g2(cid:3) 366 #¼ (cid:4)ð Þ ¼
Hence t 388 F.
g2¼ (cid:2)
Evaporator duty 165;000 0:99 0:27 880 388
¼ (cid:4) (cid:4) (cid:4)ð (cid:3) Þ
21:70MMBtu=h
¼
In order to estimate the steam flow, the feedwater temperature leaving the
economizer must be known. This is arrived at through a series of iterations.
Try t 360 F. Then
w2¼ (cid:2)
21:70 106
Steam flow (cid:4)
¼ 1195:7 332 0:05 338:5 332
ð (cid:3) Þþ (cid:4)ð (cid:3) Þ
25;110lb=h
¼
Economizer assumed dutyQ 25;110 1:05
a ¼ (cid:4)
332 198:5
(cid:4)ð (cid:3) Þ
3:52MMBtu=h
¼
Compute the term US Q=DT for the economizer based on design
ð Þdesign ¼
conditions.
Q 3:84 106
¼ (cid:4)
299 230 408 373
DT ð (cid:3) Þ(cid:3)ð (cid:3) Þ 50 (cid:2) F
¼ ln 69=35 ¼
ð Þ
Hence US 3;840;000=50 76;800. Correct this for off-design condi-
ð Þdesign ¼ ¼
tions.
gas flow, perf 0:65
US US
ð Þperf ¼ð Þdesign(cid:4) gas flow, design
(cid:1) (cid:2)
165;000
76;800 85;200
¼ (cid:4) 140;000 ¼
(cid:1) (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

The economizer transferred duty is then US DT. Based on 360 F water
ð Þperf (cid:4) (cid:2)
leaving the economizer, Q 3.52MBtu=h and the exit gas temperature is
a¼
3;520;000
t 85 F
g2 ¼165;000 0:99 0:253¼ (cid:2)
(cid:4) (cid:4)
Hence t 388785 303 F, and
g2¼ ¼ (cid:2)
303 230 388 360
DT ð (cid:3) Þ(cid:3)ð (cid:3) Þ 47 (cid:2) F
¼ ln 73=28 ¼
ð Þ
Transferred dutyQ 85;200 47 4:00MMBtu=h
t ¼ (cid:4) ¼
Becausetheassumedandtransferreddutydonotmatch,anotheriterationis
required. We can show that at duty of 3.55MMBtu=h the, assumed and
transferred duty match. Water temperature leaving the economizer 366 F
(cid:2)
¼
(saturation); exit gas temperature 301 F. Steam generation 25,310lb=h.
(cid:2)
¼ ¼
Because the calculations are quite involved, I have developed a software
program calledHRSGSthatcansimulatethedesignandoff-designperformance
of complex, multipressure fired and unfired HRSGs. More information can be
had by writing to V. Ganapathy, P.O. Box 673, Abilene, TX 79604.
8.35b
Q:
In the above case, how much fuel is required and at what firing temperature if
35,000lb=h steam at 200psig is to be generated? Gas flow is 140,000lb=h at
980 Fas in Q8.35a.
(cid:2)
A:
A simple solution is given here, though the HRSG simulation would provide
more accurate evaluation and temperature profiles. We make use of the concept
that the fuel efficiency is 100% and all of that goes to generating the additional
steam as discussed earlier.
Energy absorbed by steam 35;000 1199:3 198:5
¼ (cid:4)ð (cid:3) Þ
35:1MMBtu=h
¼
Additional energy to be provided by the burner 35.1725.24 9.86MM
¼ ¼
Btu=h (the HRSG absorbs 25.24 as shown in Q8.34).
The oxygen consumed in the process of combustion (see Q6.27) is
9:86 106= 140;000 58:4 1:2%
(cid:4) ð (cid:4) Þ¼
Copyright © 2003 Marcel Dekker, Inc.

The firing temperature T is obtained as follows:
9:86 106 140;000 0:3 T 980
(cid:4) ¼ (cid:4) (cid:4)ð (cid:3) Þ
or
T 1215 F
(cid:2)
¼
Thus, by using a few simple concepts, preliminary information about the HRSG
may be obtained. However, a complete temperature profile analysis requires a
computer program such as the HRSG simulation software.
8.36
Q:
Can we assume that a particular exit gas temperature can be obtained in gas
turbine HRSGs without doing a temperature profile analysis?
A:
No.ItisnotgoodpracticetoassumetheHRSGexitgastemperatureandcompute
thedutyorsteamgenerationassomeconsultantsandengineersdo.Theproblem
isthat,dependingonthesteampressureandtemperature,theexitgastemperature
will vary significantly. Often, consultants and plant engineers assume that any
stack gas temperature can be achieved. For example, I have seen catalogs
published by reputable gas turbine firms suggesting that 300 F stack gas
(cid:2)
temperature can be obtained irrespective of the steam pressure or parameters.
Now this may be possible at low pressures but not at all steam conditions. In
ordertoarriveatthecorrecttemperatureprofile,severalheatbalancecalculations
have to be performed, as explained below.
Itwillbeshownthatonecannotarbitrarilyfixthestackgastemperatureor
the pinch point.
Looking at the superheater and evaporator of Fig. 8.13,
W C T T W h h 78
g(cid:4) pg(cid:4)ð g1(cid:3) g3Þ¼ s(cid:4)ð so(cid:3) w2Þ ð Þ
Looking at the entire HRSG,
W C T T W h h 79
g(cid:4) pg(cid:4)ð g1(cid:3) g4Þ¼ s(cid:4)ð s0(cid:3) w1Þ ð Þ
Blowdownwasneglectedintheaboveequationsforsimplicity.DividingEq.(78)
by Eq. (79) and neglecting variations in C , we have
pg
T T h h
g1(cid:3) g3 s0(cid:3) w2 X 80
T T ¼h h ¼ ð Þ
g1(cid:3) g4 s0(cid:3) w1
Copyright © 2003 Marcel Dekker, Inc.

FactorX dependsonlyonsteam parametersandontheapproachpointused. T
g3
depends on the pinch point selected. Hence if T is known, T can be
g1 g4
calculated.
It can be concluded from the above analysis that one cannot assume that
any HRSG exit gas temperature can be obtained. To illustrate, Table 8.27 shows
severaloperatingsteamconditionsandX valuesandexitgastemperatures.Asthe
steam pressure or steam temperature increases, so does the exit gas temperature,
with the result that less energy is transferred to steam. This also tells uswhy we
needtogoinformultiple-pressure-levelHRSGswhenthemainsteampressureis
high. Note that even with infinite surface areas we cannot achieve low tempera-
tures, because this is a thermodynamic limitation.
Example 1
Determine the HRSG exit gas temperature when the gas inlet temperature is
900 Fand the steam pressure is 100psig sat.
(cid:2)
Solution. X 0.904. Saturation temperature 338 F. Hence with a 20 F
(cid:2) (cid:2)
¼ ¼
pinch point, T 358 F, and t 323 F with a 15 Fapproach point,
g3 ¼ (cid:2) w2 ¼ (cid:2) (cid:2)
900 T
(cid:3) g4 0:904; or T 300 F
900 358¼ g4 ¼ (cid:2)
(cid:3)
Example 2
What is T when steam pressure is 600psig and temperature is 750 F?
g4 (cid:2)
TABLE8.27 HRSG ExitGas Temperaturesa
Pressure Steamtemp Sat. temp Exitgas temp
(psig) ( F) ( F) X ( F)
(cid:2) (cid:2) (cid:2)
100 sat 338 0.904 300
150 sat 366 0.8754 313
250 sat 406 0.8337 332
400 sat 448 0.7895 353
400 600 450 0.8063 367
600 sat 490 0.740 373
600 750 492 0.7728 398
aBased on 15 F approach point, 20 F pinch point, 900 F gas inlet temperature, and no
(cid:2) (cid:2) (cid:2)
blowdown. Feedwater temperature is 230 F. Similar data can be generated for other
(cid:2)
conditions.
Copyright © 2003 Marcel Dekker, Inc.

Solution. X 0.7728. Saturation temperature 492 F; t 477 F;
¼ ¼ (cid:2) w2 ¼ (cid:2)
T 512 F.
g3 ¼ (cid:2)
900 512
900 (cid:3) T ¼ 0:7728; orT g4 ¼ 398 (cid:2) F
(cid:3) g4
Soa300 Fstacktemperatureisnotthermodynamicallyfeasible.Letusseewhat
(cid:2)
happens if we try to achieve that.
Example 3
Can you obtain a 300 F stack gas temperature with 900 F inlet gas temperature
(cid:2) (cid:2)
and at 600psig, 750 F, and 15 Fapproach temperature?
(cid:2) (cid:2)
Solution. X 0.7728.Letussee,usingEq.(80),whatT resultsinaT
¼ g3 g4
of 300 F, because that is the only unknown.
(cid:2)
900 T = 900 300 0:7728; orT 436 F
ð (cid:3) g3Þ ð (cid:3) Þ¼ g3 ¼ (cid:2)
which is not thermodynamically feasible because the saturation temperature at
615psig is 492 F! This is the reason one has to be careful in specifying HRSG
(cid:2)
exit gas temperatures or computing steam generation based on a particular exit
gas temperature.
Example 4
What should be done to obtain a stack gas temperature of 300 Fin the situation
(cid:2)
described in Example 3?
Solution. Oneoftheoptionsistoincreasethegasinlettemperaturetothe
HRSG by supplementary firing. If T is increased, then it is possible to get a
g1
lower T . Say T 1600 F. Then
g4 g1 ¼ (cid:2)
1600 T
(cid:3) g3 0:7728; orT 595 F
1600 300¼ g3 ¼ (cid:2)
(cid:3)
This is a feasible temperature because the pinch point is now (5957492)
¼
103 F. This brings us to another important rule: Pinch point and exit gas
(cid:2)
temperature cannot be arbitrarily selected in the fired mode. It is preferable to
analyze the temperature profiles in the unfired mode and evaluate the off-design
performance using available simulation methods discussed earlier.
Example 5
IfgasinlettemperatureinExample1is800 Finsteadof900 F,whathappensto
(cid:2) (cid:2)
the exit gas temperature at 100psig sat?
Copyright © 2003 Marcel Dekker, Inc.

Solution.
800 358
(cid:3) 0:904
800 T ¼
(cid:3) g4
or T 312 F versus the 300 F when the inlet gas temperaturewas 900 F. We
g4 ¼ (cid:2) (cid:2) (cid:2)
note that the exit gas temperature increases when the gas inlet temperature
decreases, and vice versa. This is another important basic fact.
Once the exit gas temperature is arrived at, one can use Eq. (79) to
determine how much steam can be generated.
8.37
Q:
How can HRSG simulation be used to optimize gas and steam temperature
profiles?
A:
HRSGsimulationisamethodofarrivingatthedesignoroff-designperformance
of HRSGs without physically designing them as shown in Q8.34. By using
different pinch and approach points and different configurations, particularly in
multipressure HRSGs, one can maximize heat recovery. We will illustrate this
with an example [12].
Example
A gas turbine exhausts 300,000lb=h of gas at 900 F. It is desired to generate
(cid:2)
about 20,500lb=h of superheated steam at 600psig and 650 F and as much as
(cid:2)
200psigsaturatedsteamusingfeedwaterat230 F.Usingthemethoddiscussedin
(cid:2)
Q8.34, we can arrive at the gas=steam temperature profiles and steam flows.
Figure 8.15 shows results obtained with HRSGS software. In option 1, we have
the high pressure (HP) section consisting of the superheater, evaporator, and
economizer followed by the low pressure (LP) section consisting of the LP
evaporator and economizer.By usinga pinchpointof190 Fandapproachpoint
(cid:2)
of 15 F, wegenerate 20,438lb=h of high pressure steam at 650 F. Then, using a
(cid:2) (cid:2)
pinch point of 20 F and approach point of 12 F, we make 18,670lb=h low
(cid:2) (cid:2)
pressuresteam. Thestackgastemperatureis370 F.Inoption2,wehavetheHP
(cid:2)
sectionconsistingofthesuperheaterandevaporatorandtheLPsectionconsisting
ofonlytheevaporator.AcommoneconomizerfeedsboththeHPandLPsections
withfeedwaterat375 F.BecauseofthelargerheatsinkavailablebeyondtheLP
(cid:2)
evaporator, the stack gas temperature decreases to 321 F. The HP steam
(cid:2)
generation is adjusted using the pinch point to make 20,488lb=h while the LP
steam is allowed to float. With a pinch point of 20 F, we see that we can make
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

Figure 8.15 Optimizing temperatureprofiles.
22,400lb=h in comparison with the 18,673lb=h earlier. The ASME system
efficiency is much higher now. Thus by manipulating the HRSG configuration,
one can maximize the heat recovery.
8.38
Q:
How is the HRSG efficiency determined according to ASME Power Test Code
4.4?
A:
The efficiency E is given by
energy given to steam=water=fluids
E
¼gasflow inlet enthalpy fuel input on LHV basis
(cid:4) þ
Copyright © 2003 Marcel Dekker, Inc.

To evaluate the efficiency, the enthalpy of the turbine exhaust gas should be
known.TheAppendixgivestheenthalpybasedonaparticulargasanalysis.Fuel
input on LHV basis should also be known if auxiliary firing is used.
In Q8.37 the efficiency in the design case is
21:4 3:84 106
E ð þ Þ(cid:4) 0:715; or71:5%
¼ 140;000 242 ¼
(cid:4)
If steam or water injection is resorted to, then the gas analysis will change, and
the enthalpy has to be computed based on the actual analysis.
The HRSG system efficiency in gas turbine plants will improve with the
addition of auxiliary fuel, which increases thegas temperature to the HRSG and
hence increases its steam generation. There are two reasons for this.
1. Additionofauxiliaryfuelreducestheeffectiveexcessairintheexhaust
gases,becausenoairisadded,onlyfuel.Hencetheexhaustgaslossin
relation to steam production is reduced.
2. With increased steam generation, usually the HRSG exhaust gas
temperature decreases. This is due to the increased flow of water in
the economizer, which offers a larger heat sink, which in turn pulls
down the gas temperature further. In gas turbine units, the gas flow
does not vary much with steam output as in conventional steam
generators, which accounts for the larger temperature drop.
MoreinformationonHRSGtemperatureprofilescanbefoundinChapters
1 and 2.
Table 8.28 shows the performance of an HRSG under various operating
conditions. Case 1 is the unfired case; cases 2 and 3 have different firing
conditions. It can be seen that the system efficiency is higher when more fuel
is fired, for reasons explained above.
TABLE8.28 Data forSupplementary-Fired HRSG
Case1 Case2 Case3
Gas flow,lb=h 250,000 250,000 250,000
Inlet gastemperature, F 1000 1000 1000
(cid:2)
Firingtemperature, F 1000 1257 1642
(cid:2)
Burnerduty, MMBtu=h 0 19.3 49.8
Steamflow,lb=h 45,700 65,000 95,000
Steampressure,psig 300 300 300
Feedwatertemperature, F 230 230 230
(cid:2)
Exitgas temperature, F 298 278 265
(cid:2)
Boiler duty,MMBtu=h 46.3 66.1 96.7
ASME efficiency,% 74.91 80.95 85.65
Copyright © 2003 Marcel Dekker, Inc.

8.39a
Q:
In some cogeneration plantswith gas turbines, a forced draft fan is used to send
atmosphericair totheHRSGintowhich fuel is firedtogeneratesteam whenthe
gas turbine is not in operation. What should the criteria be for the fan size?
A:
TheairflowshouldbelargeenoughtohaveturbulentflowregimesintheHRSG
andatthesametimebesmallenoughtominimizethelossduetoexitinggases.If
the air flow is high, the firing temperaturewill be low, but the system efficiency
willbelowerandthefuelinputwillbehigher.Thisisillustratedforasimplecase
of two fans generating 250,000 and 210,000lb=h of air flow in the HRSG. The
HRSGS program was used in the simulation. See Table 8.29.
Itcan be seen that though the firing temperature ishigher with the smaller
fan,theefficiencyishigherduetothelowerexitgaslossesconsideringthelower
mass flow and exit gas temperature. It should be noted that as the firing
temperatureincreases,theexitgastemperaturewilldecreasewhenaneconomizer
is used. Also, with the smaller fan the initial and operating costs are lower. One
should ensure that the firing temperature does not increase to the point of
changing the basic design concept of the HRSG. For example, an insulated
casing design is used up to 1700 F firing temperature, beyond which a water-
(cid:2)
cooled membrane wall design is required. See Chapter 1.
8.39b
Q:
How is the performance of an HRSG determined in fresh air fired mode?
A:
In this example, a multiple pressure HRSG with a common economizer is
simulated in the design unfired mode and we are predicting its performance in
the fired mode with fresh air firing using the HRSGS program.
TABLE8.29 Fresh AirFiringPerformance
Airflow, lb=h 250,000 210,000
Inlet temperature, F 80 80
(cid:2)
Firingtemperature, F 1258 1417
(cid:2)
Exitgas temp, F 278 267
(cid:2)
Steamflow,lb=h 65,000 65,000
Burnerduty, MMBtu=h 79.7 76.88
ASME efficiency,% 81.66 84.82
Copyright © 2003 Marcel Dekker, Inc.

ThisisathreepressurelevelHRSGwithHPsteamat600psig,IPsteamat
200psig, and LP steam at 10psig. (HP high pressure, IP intermediate
¼ ¼
pressure, LP low pressure.) A common economizer feeds the HP and IP
¼
steam. Once the pinch points for the HP, IP, and LP evaporators are suggested,
theprogramarrivesatthesteamflowsandtemperatureprofilesasshowninFigs.
8.16a and 8.16b. The flow through the common economizer is arrived at after a
FIGURE 8.16a UnfiredmultipressureHRSG temperatureprofile.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.16b Fresh airfiredtemperature profile.
Copyright © 2003 Marcel Dekker, Inc.

few complex iterations. Figure 8.16a shows the design mode results from the
HRSGS program.
Intheoff-designorfiredmode,freshairisusedinsteadofturbineexhaust.
Theairflowusedisclosetothedesignexhaustgasflow.Weinputtheambientair
flow and the desired HP steam flow, and the program asks for fuel analysis and
automatically arrives at the firing temperature. The off-design performance is
shown in Fig. 8.16b.
TheefficiencyaccordingtoASMEPowerTestCode4.4,USvaluesofeach
surfaceinboththedesignandoff-designmodesmayalsobeseen,aswellasthe
exhaust gas analysis after combustion.
This is yet another example of how simulation may be used to perform
variousstudieswithoutaphysicaldesignofanHRSG.Consultantsandplanners
of cogeneration or combined cycle projects should find this a valuable tool.
8.40
Q:
HowdoweevaluatealternativeHRSGdesignsiftheoperatingcostsaredifferent?
A:
Let us consider the design of two HRSGs, one with low pinch and approach
points(andhencemoresurfaceareaandgaspressuredrop),calleddesignA,and
anotherwithhigherpinchandapproachpoints,calleddesignB,whichcostsless.
TheseHRSGsoperateinbothunfiredandfiredmodesfor50%ofthetime.Inthe
fired mode, both HRSGs generate 70,000lb=h of steam; in the unfired mode,
design A naturally generates more steam. Table 8.30 shows the performance of
the HRSGs in unfired and fired modes.
Let fuel cost $3=MMBtu (LHV). Cost of steam $3.5=1000lb and
¼
electricity 6 cents=kWh. Assume that an additional 4in.WC of gas pressure
¼
drop is equivalent to a 1% decrease in gas turbine power output, which is a
nominal 8000kW. The HRSG operates in unfired and fired modes for 4000h=y
each.
Design A has the following edge over design B in operating costs.
Due to higher steam generation in unfired mode:
4000
50;000 47;230 3 $33;240
ð (cid:3) Þ(cid:4) (cid:4)1000¼
Due to lower fuel consumption:
22:55 19:23 3:5 4000 $46;480
ð (cid:3) Þ(cid:4) (cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.30 Performance ofAlternativeHRSG Designs
Design A Design B
Unfired Fired Unfired Fired
Gas tempto HRSG 980 1208 980 1248
Gas tempto economizer, F 437 441 466 483
(cid:2)
Exitgas temperature, F 314 298 353 343
(cid:2)
Gas pressuredrop, in.WC 4.0 4.3 2.75 3.0
Steamflow,lb=h 50,000 70,000 47,230 70,000
Watertemp toeconomizer, F 398 373 396 370
(cid:2)
Burnerduty, MmBtu=h 0 19.23 0 22.55
Evaporator surfacearea ft2 39,809 27,866
Economizersurfacearea, ft2 24,383 13,933
Pinchpoint, F 16 20 45 62
(cid:2)
Approachpoint, F 23 48 25 51
(cid:2)
Gas flow 287,000lb=h; Gas analysis (vol%) CO 3, H O 7, N 75, O 15. Steam
¼ 2¼ 2 ¼ 2¼ 2¼
pressure 300psigsat;gasturbinepower 8000kW.
¼ ¼
Due to higher gas pressure drop of 1.3in.WC:
8000
1:3 8000 0:07 $14;560
(cid:4) (cid:4) (cid:4)100 4¼
(cid:4)
Thus the net benefit of using design A over B is $(33,240 46,4807
þ
14,560) $65,160 per year.
¼
IftheadditionalcostofdesignAoverBduetoitssizeis,say,$50,000,the
paybackofusingdesignAislessthan1year.However,iftheHRSGoperatesfor
less than, say, 3000h=year, the payback will be longer and has to be reviewed.
8.41
Q:
What is steaming, and why is it likely in gas turbine HRSGs and not in
conventional fossil fuel fired boilers?
A:
When the economizer in a boiler or HRSG starts generating steam, particularly
with downward flowof water, problems can arise in the form of water hammer,
vibration, etc. With upward water flow design, a certain amount of steaming, 3–
5%, can be tolerated because the bubbles have a natural tendency to go upward
along with the water. However, steaming should generally be avoided.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.31 Typical Exhaust Gas Flow, Temperature Characteristics of a Gas
Turbine
Ambient temp, F 20.0 40.0 59.0 80.0 100.0 120.0
(cid:2)
Poweroutput,kW 38,150 38,600 35,020 30,820 27,360 24,040
Heatrate,Btu=kWh 9384 9442 9649 9960 10,257 10,598
Waterflow rate lb=h 16,520 17,230 15,590 13,240 10,540 6990
Turbineinlet temp, F 1304 1363 1363 1363 1363 1363
(cid:2)
Exhaust temp, F 734 780 797 820 843 870
(cid:2)
Exhaust flow,lb=s 312 304 286 264 244 225
Fuel:naturalgas;elevation:sealevel;relativehumidity60%;inletloss4in.H O;exhaustloss
2
15in.H O;speed:3600rpm;outputterminal:generator.
2
Tounderstandwhytheeconomizerislikelytosteam,weshouldfirstlookat
thecharacteristicsofagasturbineasafunctionofambienttemperatureandload
(see Tables 8.31 and 1.4).
In single-shaft machines, which are widely used, as the ambient tempera-
ture or load decreases, the exhaust gas temperature decreases. The variation in
mass flow is marginal compared to fossil fuel fired boilers, while the steam or
waterflowdropsoffsignificantly.(Theeffectofmassflowincreaseinmostcases
does not offset the effect of lower exhaust gas temperature.) The energy-
transferring ability of the economizer, which is governed by the gas-side heat
transfer coefficient, does not change much with gas turbine load or ambient
temperature; hence nearly the same duty is transferred with a smaller water flow
through the economizer, which results in a water exit temperature approaching
saturationtemperatureasseeninQ8.35.Henceweshoulddesigntheeconomizer
suchthatitdoesnotsteam inthelowestunfiredambientcase, whichwillensure
thatsteamingdoesnotoccur atotherambientconditions.Afewother stepsmay
also be taken, such as designing the economizer [8] with a horizontal gas flow
with horizontal tubes (Fig. 8.17). This ensures that the last few rows of the
economizer, which are likely to steam, have a vertical flow of steam–water
mixture.
Inconventionalfossilfuelfiredboilersthegasflowdecreasesinproportion
to the water flow, and the energy-transferring ability of the economizer is also
loweratlowerloads.Thereforesteamingisnotaconcernintheseboilers;usually
theapproachpointincreasesatlowerloadsinfiredboilers,whereasitisaconcern
in HRSGs.
The other measures that may be considered to minimize steaming in an
economizer are
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.17 Horizontal gas floweconomizer.
Increase thewaterflowthroughtheeconomizerduringtheseconditionsby
increasingtheblowdownflow.Thissolutionworksonlyifsmallamounts
of steam are formed and the period of operation in this mode is small.
Blowdown results in a waste of energy.
Increasing the inlet gas temperature either by supplementary firing or by
increasing the turbine load helps togenerate more steam and thus more
water flowthroughtheeconomizer, which willpreventsteaming. Aswe
saw in Chapter 1, the economizer steams at low loads of the turbine.
Exhaust gases can be bypassed around the HRSG during such steaming
conditions. This minimizes the amount of energy transferred at the
economizer as well as the evaporator. Gas can also be bypassed around
the economizer, mitigating the steaming concerns.
Water can also be bypassed around the economizer during steaming conditions,
but this is not a good solution. When the gas turbine load picks up, it will be
difficult to put the water back into the economizer while the tubes are hot. The
coldwaterinsidehottubescanflashandcausevibrationandthermalstressesand
can even damage the economizer tub.
Copyright © 2003 Marcel Dekker, Inc.

8.42
Q:
Whyarewatertubeboilersgenerallypreferredtofiretubeboilersforgasturbine
exhaust applications?
A:
Fire tube boilers require a lot of surface area to reduce the temperature of gas
leavingtheevaporatortowithin15–25 Fofsaturationtemperature(pinchpoint).
(cid:2)
They have lower heat transfer coefficients than those of bare tube water tube
boilers (see Q8.10), which do not compare well with finned tube boilers. Water
tubeboilerscanuseextendedsurfacestoreducethepinchpointto15–25 Finthe
(cid:2)
unfired mode and hence be compact. The tubes will be very long if fire tube
boilers are used; hence the gas pressure drop will be higher. (A fire tube boiler
can be made into a two-pass boiler to reduce the length; however, this will
increasetheshelldiameterandthelaborcost,becausetwicethenumberoftubes
willhavetobeweldedtothetubesheets.)Thefiretubeboilerwillhavetobeeven
largerifthesamegaspressuredropistobemaintained.Table8.32comparesthe
performance of water tube and fire tube boilers for the same duty and pressure
drop.
It can be seen from the table footnotes that the water tube boiler is very
compact.Ifthegasflowisverysmall,say less than 50,000lb=h,then afire tube
boiler may be considered.
TABLE8.32 WaterTubevs.FireTubeBoilerforGasTurbine
Exhaust
Water tubea Fire tubeb
Gas flow,lb=h 100,000 100,000
Inlet temp, F 900 900
(cid:2)
Exittemp, F 373 373
(cid:2)
Duty, MMBtu=h 13.72 13.72
Gas pressuredrop, in.WC 2.75 2.75
Feedwatertemp, F 220 220
(cid:2)
Steampressure,psig 125 125
Steamflow,lb=h 13,500 13,500
Surfacearea, ft2 12,315 9798
aWatertubeboiler:2 0.105in.tubes,20wide,18deep,6ftlong,with
(cid:4)
5serratedfins=in.,0.75in.high,0.05in.thick.
bFiretubeboiler:14001.5 0.105in.tubes,21ftlong.
(cid:4)
Copyright © 2003 Marcel Dekker, Inc.

8.43
Q:
Does the addition of 10% surface area to a boiler increase its duty by 10%?
A:
No. The additional surface area increases the duty only slightly. The increased
temperature drop across the boiler and the temperature rise of water or steam (if
single-phase) due to the higher duty results in a lower log-mean temperature
difference. This results in lower transferred duty, even assuming that the overall
heattransfercoefficientU remainsunchanged.Ifthelargersurfacearearesultsin
lowergasvelocities,theincreaseindutywillbemarginalasU isfurtherreduced.
Asanexample,considertheperformanceofafiretubeboilerwith10%and
20% increase in surface area as shown in Table 8.33. As can be seen, a 10%
increase in surface area increases the duty by only 3%, and a 20% increase in
surface area increases the duty by only 6%. Similar trends may be shown for
water tube boilers, superheaters, economizers, etc.
8.44a
Q:
How do we estimate the time required to heat a boiler?
A:
Aboilercan take along time toheat up, dependingon the initial temperature of
the system, mass of steel, and amount of water stored. The following procedure
givesaquickestimateofthetimerequiredtowarmupaboiler.Themethodology
is applicable to either fire tube or water tube boilers.
TABLE8.33 Boiler Performancewith IncreasedSurface Areaa
No.of Length Surface Duty Exit gas
Case tubes (ft) (ft2) (MMBtu=h) temp ( F)
(cid:2)
1 390 16 2839 20.53 567
2 390 17.6 3123 21.16 533
3 390 19.2 3407 21.68 505
aGas flow 70,000lb=h; inlet gas temperature 1600 F. Gas analysis (vol%): CO 7,
¼ ¼ (cid:2) 2¼
H O 12, N 75, O 6; steam pressure 125psig saturated. Tubes: 2 0.120 carbon
2 ¼ 2¼ 2¼ ¼ (cid:4)
steel.
Copyright © 2003 Marcel Dekker, Inc.

Gas at a temperature of T enters the unit, which is initially at a
g1
temperature of t (both the water and the boiler tubes). The following energy
1
balance equation can then be written neglecting heat losses:
dt
M W C T T UADT 81
cdz¼ g pg(cid:4)ð g1(cid:3) g2Þ¼ ð Þ
where
M water equivalent of the boiler
c¼
mass of steel specific heat of steel mass of water specific
¼ (cid:4) þ (cid:4)
heat of water (Weight of the boiler tubes, drum, casing, etc., is
included in the steel weight.)
dt=dz rate of change of temperature, F=h
(cid:2)
¼
W gas flow, lb=h
g¼
C gas specific heat, Btu=lb F
pg¼ (cid:2)
T ;T entering and exit boiler gas temperature, F
g1
U
g2¼
overall heat transfer coefficient, Btu=ft2h
(cid:2)
F
(cid:2)
A ¼ surface area, ft2
¼
DT log-mean temperature difference, F
(cid:2)
¼
T t T t
ð g1(cid:3) Þ(cid:3)ð g2(cid:3) Þ
¼ln T t = T t
½ð g1(cid:3) Þ ð g2(cid:3) Þ(cid:5)
t temperature of the water=steam in boiler, F
(cid:2)
¼
From Eq. (81) we have
T t UA
ln
g1(cid:3)
82
" T g2(cid:3) t #¼W g C pg ð Þ
or
T t T t
T t g1(cid:3) t g1(cid:3) 83
g2 ¼ þeUA=W g C pg ¼ þ K ð Þ
Substituting Eq. (83) into Eq. (81), we get
dt K 1
M W C T t (cid:3)
cdz¼ g pgð g1(cid:3) Þ K
or
dt W C K 1
g pg (cid:3) dz 84
T t ¼ M (cid:4) K ð Þ
g1(cid:3) c
Copyright © 2003 Marcel Dekker, Inc.

To estimate thetime to heat up the boiler from an initial temperature t to t , we
1 2
have to integrate dt between the limits t and t .
1 2
T t W C K 1 z
ln g1(cid:3) 1 g pg ð (cid:3) Þ 85
T t ¼ M (cid:4) K ð Þ
g1(cid:3) 2 c
The above equation can be used to estimate the time required to heat the boiler
fromatemperatureoft tot ,usingfluegasesenteringatT .However,inorder
1 2 g1
to generate steam, we must first bring the boiler to the boiling point at
atmospheric pressure and slowly raise the steam pressure through manipulation
of vent valves, drains, etc; the first term of Eq. (81) would involve the term for
steam generation and flow in addition to metal heating.
Example
Awater tube waste heat boiler of weight 50,000lb and containing 30,000lb of
water is initially at a temperature of 100 F. 130,000lb of flue gases at 1400 F
(cid:2) (cid:2)
enter the unit. Assume the following:
Gas specific heat 0.3Btu=lb F
(cid:2)
¼
Steel specific heat 0.12Btu=lb F
(cid:2)
Surface area of boi ¼ ler 21,000ft2
Overall heat transfer c ¼ oefficient 8Btu=ft2h F
(cid:2)
¼
Estimate the time required to bring the boiler to 212 F.
(cid:2)
Solution.
U 8 21;000
(cid:4) 4:3
W C ¼130;000 0:3¼
g pg (cid:4)
K e4:3 74
¼ ¼
M 50;000 0:12 30;000 1 36;000
c ¼ (cid:4) þ (cid:4) ¼
1400 100 130;000 0:3 73
ln (cid:3) 0:09 (cid:4) z
1400 212¼ ¼ 36;000 (cid:4)74
(cid:3)
or z 0.084h 5.1min.
¼ ¼
One could develop a computer program to solve Eq. (81) toincludesteam
generationandpressure-raisingterms.Inreal-lifeboileroperation,theprocedure
is corrected by factors based on operating data of similar units.
Itcanalsobenotedthat,ingeneral,firetubeboilerswiththesamecapacity
aswater tubeboilerswouldhavealargerwaterequivalentandhencethestart-up
time for fire tube boilers would be longer.
Copyright © 2003 Marcel Dekker, Inc.

8.44b
Q:
AssumingthatthesuperheaterinQ8.19cisdry,howlongdoesittaketoheatthe
metal from 80 F to 900 F? Assume that the gas-side heat transfer coefficient is
(cid:2) (cid:2)
12Btu=ft2h F. Gas flow and temperature are the same as before. The weight of
(cid:2)
thesuperheateris5700lb.150,000lb=hofexhaustgasesenter thesuperheaterat
1030 F.
(cid:2)
A:
Let us use Eq. (85),
t t W C K 1 z
ln g1(cid:3) 1 g p gð (cid:3) Þ
t t ¼ M K
g1(cid:3) 2 c(cid:4)
UA 12 2022
K exp exp (cid:4) 1:76
¼ " W g C p g #¼ (cid:6) 150;000 (cid:4) 0:286 (cid:7) ¼
M 5700 0:12 684
c ¼ (cid:4) ¼
1030 80 150;000 0:286 0:76z
ln (cid:3) (cid:4) (cid:4) 27z 1:99
1030 900¼ 1:76 684 ¼ ¼
or (cid:3) (cid:4)
z 0:0737h 4:5 min
¼ ¼
This is an estimate only but gives an idea of how fast the metal gets heated up.
This is important in gas turbine plants without a gas bypass system. A large
quantity of exhaust gases can increase the metal temperatures quickly. Hence if
frequent start-ups and shutdowns are planned, a stress analysis is required to
ensure that critical components are not subjected to undue stresses due to quick
changes in tube wall or header temperatures.
Bythesametoken,thesuperheater tubescoolfastwhentheexhaustgasis
shut off compared to, say, evaporator tubes, which are still hot due to the
inventoryofhotsaturatedliquid.Thiscanleadtocondensationofsteamwhenthe
HRSGisrestarted,leadingtoblockageofflowinsidethesuperheatertubesunless
adequate drains are provided.
8.44c
Q:
Alargemass ofmetal andwaterinventoryinaboiler resultsinalonger start-up
period,buttheresidualenergyinthemetalalsohelpstorespondtoloadchanges
fasterwhentheheatinputtotheboilerisshutoff.Drumlevelfluctuationsalsoare
Copyright © 2003 Marcel Dekker, Inc.

smoothedoutbyalargewaterinventory.Inordertounderstandthedynamics,let
us look at an evaporator in a waste heat boiler with the following data:
Gas flow 350,000lb=h
¼
Gas inlet temp 1000 F
(cid:2)
¼
Gas exit temp 510 F
(cid:2)
¼
Steam pressure 600psig sat
¼
Feedwater temp 222 F
(cid:2)
¼
Tubes: 2 0.105, 30 tubes=row, 20 deep, 12ft long with 4.5 0.75
(cid:4) (cid:4) (cid:4)
0.05in. serrated fins
Steam drum 54in., mud drum 36in; both are 13ft long. Boiler gener-
¼ ¼
ates 45,000lb=h of steam.
Weight of steel including drums 75,000lb
¼
Weight of water in evaporator 18,000lb
Volume of steam space 115f ¼ t3
¼
Feedwater temperature 220 F
(cid:2)
¼
Energy transferred by gas to evaporator 45.9MMBtu=h
¼
What happens to the steam pressure and steam generation when the heat input
and the feedwater supply are turned off?
A:
The basic equation for energy transfer to an evaporator is
dT dh dp
Q W h h h W W C W 86a
¼ s fgþð l(cid:3) fÞ f þ m pdpþ wdp dz ð Þ
(cid:1) (cid:2)
where
W mass of metal, lb
m¼
W steam generated, lb=h
s¼
W feedwater flow, lb=h
f ¼
W amount of water inventory in boiler system including drums,
w¼
tubes, pipes, lb
dh=dp change of enthalpy to change in pressure, Btu=lb psi
¼
dT=dp change of saturation temperature to change in pressure, F=psi
(cid:2)
¼
Q energy transferred to evaporator, Btu=h
¼
dp=dz rate of pressure change, psi=h
¼
Now assuming that the volume of space between the drum level and the
valve Vft3, we can write the following expression for change in pressure
¼
using the perfect gas law:
pV C pV=m
¼ ¼
Copyright © 2003 Marcel Dekker, Inc.

where
C a constant
¼
m mass of steam, lb, in volume V
¼
or
pV Cm
C or p
m ¼ ¼ V
dp pV
W W 86b
dz ¼ V ð s(cid:3) lÞ ð Þ
where
p pressure, psia
¼
W ;W steam generated and steam withdrawn, lb=h
s l¼
Forsteamat600–630psia,wehavefromthesteamtablesthatthesaturation
temperature 486 Fand 492 F, respectively.
(cid:2) (cid:2)
¼
Enthalpy of water 471.6 and 477.9Btu=lb
¼
Average latent heat h 730Btu=lb
Specific volume 0.7 fg 5 ¼ ft3=lb
¼
Hence
dh 477:9 471:6
(cid:3) 0:21Btu=lbpsi
dp¼ 30 ¼
dT 492 486
(cid:3) 0:2 (cid:2) F=psi
dp ¼ 30 ¼
When Q 0 and W 0, we have from Eq. (86) that
¼ f ¼
dp
W 730 75;000 0:12 0:2 18;000 0:21 0
s(cid:4) þð (cid:4) (cid:4) þ (cid:4) Þdz ¼
dp 615 0:75
(cid:4) W W 4 W W
dz ¼ 115 ð s(cid:3) lÞ¼ (cid:4)ð s(cid:3) lÞ
or, combining this with the previous equation,
W 730 5580 4 W W 0 or W 43;570lb=h
s(cid:4) þð Þ(cid:4) (cid:4) s(cid:3) l ¼ s ¼
Using Eq. (87), (cid:8) (cid:9)
dp
4 43;570 45;000 5720psi=hor 1:59psi=s
dz ¼ (cid:4)ð (cid:3) Þ¼(cid:3) (cid:3)
The pressure decay will be about 1.59psi=s if this situation continues without
correcting feedback such as matching heat input and feedwater flow.
These calculations, though simplistic, give an idea of what happens when,
for example, the turbine exhaust gas is switched off. In fresh air fired HRSGs,
there is a small time delay, on the order of a minute, before the fresh air fired
Copyright © 2003 Marcel Dekker, Inc.

burnercancomeonandfiretofullcapacity.Thesteampressuredecayduringthis
period can be evaluated by this procedure.
8.44d
Q:
Letusassumethattheboilerisoperatingat45,000lb=handsuddenlythedemand
goes to 50,000lb=h.
Case1: Whathappenstothesteampressureifwemaintainthesameheat
input to the evaporator and the feedwater supply?
Case 2: What happens if the feedwater is cut off but heat input remains
the same?
A:
Case 1: Q 45:0 106 Btu=h; W 45;000lb=h;W 50;000lb=h: First
¼ (cid:4) f ¼ l ¼
let us com-pute the steam generation. Using Eq. (86a),
h 471:6Btu=lb and h 189:5Btu=lb
1 ¼ f ¼
From Eq. (86a),
dp
45;000 471:6 189:6 W 730 5580 Q
(cid:4)ð (cid:3) Þþ s(cid:4) þ dz ¼
also, dp=dz 4 W 50;000 ,
¼ ð s(cid:3) Þ
Simplifying,
12:69 106 W 730 5580 4 W 50;000 45:9 106
(cid:4) þ s(cid:4) þ (cid:4) ð s(cid:3) Þ¼ (cid:4)
W 49;857lb=h
s ¼
Thus,
dp
4 49;857 50;000 572psi=h 0:159psi=s
dz ¼ (cid:4)ð (cid:3) Þ¼(cid:3) ¼(cid:3)
Case 2: W 0 and Q 45:9MMBtu=h: Using the above equations,
f ¼ ¼
W 730 5580 4 W 50;000 45:9 106; orW 50;405lb=h
s(cid:4) þ (cid:4) ð s(cid:3) Þ¼ (cid:4) s ¼
dp
1620psi=h 0:45psi=s
dz ¼ ¼
Thepressureactuallyincreases,becausethecoolingeffectofthefeedwaterisnot
sensed.
Inpractice,controlsrespondfastandrestorethebalanceamongheatinput,
feedwater flow, and steam generation to match the demand. If we cannot adjust
theheatinput,asinunfiredwasteheatboilers,thepressurewillslideasshownif
we withdraw more steam than can be supplied by the boiler.
Copyright © 2003 Marcel Dekker, Inc.

8.45a
Q:
Discuss the parameters influencing the test results of an HRSG during perfor-
mance testing.
A:
Themainvariablesaffectingtheperformance ofanHRSGarethegas flow,inlet
gastemperature,gasanalysis,andsteamparameters.AssumingthatanHRSGhas
been designed for a given set of gas conditions, in reality several of the
parameters could be different at the time of testing. In the case of a gas turbine
HRSG in particular, ambient temperature also influences the exhaust gas condi-
tions.TheHRSGcould,asaresult,bereceivingadifferentgasflowatadifferent
temperature, in which case the steam production would be different from that
predicted.
Eveniftheambienttemperatureandthegasturbineloadweretoremainthe
same,itisdifficulttoensurethattheHRSGwouldreceivethedesigngasflowat
thedesigntemperature.Thisisduetoinstrumenterrors.Typically,inlargeducts,
thegasmeasurementcouldbeoffby3–5%andthegastemperaturescoulddiffer
by 10–20 Faccording to ASME Power Test Code 4.4. As a result it is possible
(cid:2)
that the HRSG would receive 5% less flow at 10 F lower gas temperature than
(cid:2)
designconditions,eventhough theinstrumentsrecordeddesignconditions.Asa
result, the HRSG steam generation and steam temperature would be less than
predicted through no fault of the HRSG design. Figure 8.18 shows the per-
formance of an HRSG designed for 500,000lb=h gas flow at 900 F; steam
(cid:2)
generationis 57,000lb=h at 650psig and 750 F. Thegraph shows howthe same
(cid:2)
HRSGbehaveswhenthemassflowchangesfrom485,000to515,000lb=hwhile
theexhausttemperaturevariesfrom880 Fto902 F.Thesteamtemperaturefalls
(cid:2) (cid:2)
to 741 F with 880 F gas temperature, whereas it is 758 F at 920 F. The steam
(cid:2) (cid:2) (cid:2) (cid:2)
flow increases from 52,900 to 60,900lb=h as the gas mass flow increases. Thus
thefigure shows themap ofperformance ofthe HRSG for possibleinstrumental
error variations only. Hence HRSG designers and plant users should mutually
agree upon possible variations in gas parameters and their influence on HRSG
performance before conducting such tests.
8.45b
Q:
Based on operating data, can we determine whether an HRSG is operating
well?
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.18 HRSG performanceasafunction ofgas flow andtemperature.
A:
Itispossibletoevaluatetheoperatingdataforpossibledeviationsfrompredicted
or guaranteed data as shown below. An HRSG supplier has guaranteed certain
dataforhisHRSGinhisproposal,whichareshownalongsidethemeasureddata
in Table 8.34. How are these data to be reconciled?
Note that the actual gas flow is difficult to measure and is not shown.
However, using an energy balance, one can obtain thegas flow based on energy
TABLE8.34 Proposed andActual HRSG Performance
Data Proposal guarantee Actual data
Gas flow,lb=h 550,000 ?
Exhaust gastemp, F 1000 970
(cid:2)
Exitgas temp, F 372 380
(cid:2)
Steampressure,psig 600 500
Steamtemp, F 700 690
(cid:2)
Feedwatertemp, F 230 230
(cid:2)
Blowdown, % 2 0
Steamflow,lb=h 79,400 68,700
Copyright © 2003 Marcel Dekker, Inc.

absorbed by steam and the difference between gas temperatures at the inlet and
exit. Note that the operating steam pressure is lower than that called for in the
design.
From the energy balance, we have
W h h 0:99 W Dh
g(cid:4)ð i(cid:3) oÞ(cid:4) ¼ s
where h;h refer to the enthalpy of gas at the inlet and exit of the HRSG
i o
corresponding to the gas temperatures measured. The steam flow, W , and the
s
enthalpyabsorbedbysteam,Dh,areknownfromsteamtables.HenceW ,thegas
g
flow, can be calculated. It can be shown to be 501,300lb=h.
Now using the HRSGS program, one can simulate the design mode using
theproposaldataasshowninFig.8.19a.Then,usingthecalculatedgasflowand
the inlet temperature, run the HRSGS program in the off-design mode at the
lower steam pressure. The results are shown in Fig. 8.19b. It may be seen that
69,520lb=h of steam should have been generated at 690 F and the exit gas
(cid:2)
temperatureshouldbe364 F,whereaswemeasuredonly68,700lb=handexitgas
(cid:2)
at380 F.Hencemoreanalysisisrequired,butthereisaprimafacieconcernwith
(cid:2)
the HRSG performance.
8.46
Q:
Estimate the boiling heat transfer coefficient inside tubes for water and the tube
wall temperature rise for a given heat flux and steam pressure.
A:
Subcooledboilingheattransfercoefficientinsidetubesforwatercanbeestimated
by the following equations.
According to Collier [13],
DT 0:072e P=1260 q0:5 87a
(cid:3)
¼ ð Þ
According to Jens and Lottes [13],
DT 1:9e P=900 q0:25 87b
(cid:3)
¼ ð Þ
where
DT differencebetweensaturationtemperatureandtubewalltemperature,
¼
F
(cid:2)
P steam pressure, psia
q ¼ heat flux inside tubes, Btu=ft2h
¼
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.19a SimulationofHRSG design data.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.19b Simulation ofHRSG operatingdata.
Copyright © 2003 Marcel Dekker, Inc.

The heat transfer coefficient is then given by
h q=DT
i ¼
Example
Whatistheboilingheattransfercoefficientinsidethetubes,andwhatisthetube
walltemperatureiftheheatfluxinsideboilertubesis60,000Btu=ft2handsteam
pressure 1200psia?
¼
Solution. Using Collier’s equation,
DT 0:072 e 1200=1260 60;0000:5 6:8 F
(cid:3) (cid:2)
¼ (cid:4) (cid:4) ¼
h 60;000=6:8 8817Btu=ft2 h F
i ¼ ¼ (cid:2)
Using Jens and Lottes’s equation,
DT 1:9 e 1200=900 60;0000:25 7:8 F
(cid:3) (cid:2)
¼ (cid:4) (cid:4) ¼
h 60;000=7:8 7650Btu=ft2 h F
i ¼ ¼ (cid:2)
The above expressions assume that the tube surface where boiling occurs is
smooth and clean.
8.47a
Q:
Whatistherelationshipamongcriticalheatflux,steampressure,quality,andflow
in water tube boilers?
A:
Several variables influence the critical heat flux or the departure from nucleate
boiling (DNB) condition. These are
Steam pressure
Mass velocity of mixing inside the tubes
Steam quality
Tube roughness and cleanliness
Tube size and orientation
Correlations such as the Macbeth correlation are available in the literature
[13].
The Macbeth correlation is
q 0:00633 106 h d 0:1 G=106 0:51 1 x 88a
c ¼ (cid:4) (cid:4) fg i(cid:3) ð i Þ (cid:4)ð (cid:3) Þ ð Þ
Copyright © 2003 Marcel Dekker, Inc.

where
q critical heat flux, Btu=ft2h
c¼
h latent heat of steam, Btu=lb
G
fg¼
mass velocity inside tubes, lb=ft2 h
i¼
x steam quality, expressed as a fraction
¼
d tube inner diameter, in.
i¼
Example
Estimate the critical heat flux under the following conditions:
Steam pressure 1000psia
¼
Tube inner diameter 1.5in.
Mass velocity 600, ¼ 000lb=ft2 h
¼
Steam quality 0.20
¼
q 0:00633 106 650 1:50 0:1 0:60:51
c ¼ (cid:4) (cid:4) (cid:4) (cid:3) (cid:4)
1 0:2 2:43 106Btu=ft2 h
(cid:4)ð (cid:3) Þ¼ (cid:4)
In real-life boilers, theallowableheat fluxto avoidDNB ismuch lower,say 20–
30% lower, than the values obtained by laboratory tests under controlled
conditions due to factors such as roughness of tubes, water quality, and safety
considerations. Boiler suppliers have their own data and design boilers accord-
ingly.
8.47b
Q:
Howisthecriticalheatfluxq determinedinpoolboilingsituationsasinfiretube
c
boilers?
A:
Several correlations are available in the literature, but only two will be cited.
Motsinki suggests the simple equation [13]
P 0:35 1 P 0:9
q 803P s (cid:3) s 88b
c ¼ c P P ð Þ
(cid:1) c(cid:2) (cid:1) c (cid:2)
where P ;P are the steam pressure and critical pressure, both in psia.
s c
Copyright © 2003 Marcel Dekker, Inc.

Zuber’s correlation takes the form [13]
0:25
q s r r gg
c 0:13 ð f (cid:3) gÞ 0
r g h fg ¼ (cid:4) r2 g !
0:5
r
f
(cid:4) r gþ r f!
where
s surface tension
¼
r density
¼
h latent heat
fg¼
g;g acceleration due to gravity and conversion factor g in force units
0¼
all in metric units.
Example
Determine the critical heat flux for steam at 400psia under pool boiling
conditions.
Solution. The following data can be obtained from steam tables:
Saturation temperature at 400psia 445 F
(cid:2)
Density of liquid 51lb=cu ft (827 ¼ kg=m3)
Density of vapor ¼ 0.86lb=cu ft (13.8kg=m3)
¼
Latent heat of vaporization 780Btu=lb (433kcal=kg)
¼
From Table 8.26 at a saturation temperature of 445 F, surface tension is
(cid:2)
0.0021lb=ft (0.31kg=m).
f f
g 9:8 36002 m=h2
¼ (cid:4)
g 9:8 36002 kg =Kg h2
0 ¼ (cid:4) m f
Substituting into (88b):
400 0:35 400 0:9
q 803 3208 1
c ¼ (cid:4) (cid:4) 3208 (cid:4) (cid:3)3208
(cid:1) (cid:2) (cid:1) (cid:2)
1:102MMBtu=ft2 h
¼
Copyright © 2003 Marcel Dekker, Inc.

Using Eq. (88c),
q 13:8 433 0:13 0:0031 813 9:82
c ¼ (cid:4) (cid:4) (cid:4) (cid:4) (cid:4)
36004 0:25 8(cid:8)27 0:5
(cid:4) 13:8 2 (cid:4) 827 13:8
ð Þ (cid:2) (cid:1) þ (cid:2)
2:95 106kcal=m2 1:083MMBtu=ft2 h
¼ (cid:4) ¼
Again, as before, factors such as surface roughness, water quality, scale forma-
tion, and bundle configuration play a role, and for conservative estimates, boiler
designers use a value that is 20–30% of these values.
8.47c
Q:
Estimate the critical heat flux for a tube bundle of a fire tube boiler with the
following data:
Tube OD 2in.
¼
Number of tubes 590
¼
Length 29.5ft
¼
Tube spacing 2.75in., triangular
Surface area ¼ 9113ft2
¼
Tube bundle diameter 78in.
¼
A:
The heat flux for a tube bundle is obtained by correcting the heat flux for pool
boiling obtained from Q8.47b.
First compute a factor C D L=A
¼ b
where
D bundle diameter, ft
b¼
L length of tubes, ft
A ¼ surface area of bundle, ft2
¼
78 29:5
C (cid:4) 0:021
¼12 9113¼
(cid:4)
The correction factor F is obtained from the correlation
logF 0:8452 0:994logC
¼ þ
For C 0:021;logF 0:8224; or F 0:15:
¼ ¼(cid:3) ¼
Hence,
Corrected heat flux 1:083 106 0:15 162;500Btu=ft2 h
¼ (cid:4) (cid:4) ¼
Typically a value such as 70–80% of this is used for tube bundles.
Copyright © 2003 Marcel Dekker, Inc.

8.48
Q:
Discuss the simplified approach to designing fire tube boilers.
A:
Engineers often must estimate the size of heat transfer equipment such as heat
exchangers, gascoolers,boilers, and economizersfor preliminarycostingand to
check space requirements. With the approach presented here, one can quickly
determine one or more configurations to accomplish a certain amount of heat
transfer. One can also size equipment so as to limit the pressure drop without
performing lengthy calculations. Life-cycle costing can then be applied to select
the optimum design.
Two situations will be discussed [8].
1. Thetube-sideheattransfercoefficientgovernstheoverallheattransfer.
Examples: Fire tube boilers; gas coolers; heat exchangers in which a
mediumsuchasairorfluegasflowsonthetubesideandafluidwitha
high heat transfer coefficient flows on the outside. Phase changes can
also occur on the outside of the tubes.
2. The shell side governs. Examples: Water tube boilers, steam–air
exchangers, and gas–liquid heat transfer equipment. See Q8.49.
Tube-Side Transfer Governs
In a fire tube boiler, gas flows inside the tubes and a steam–water mixture flows
ontheoutside.Thegasheattransfercoefficientissmall,about10–20Btu=ft2h F,
(cid:2)
compared to the outside coefficient of 2000–3000Btu=ft2h F. The metal resis-
(cid:2)
tance is also small; hence the gas-side coefficient governs the overall coefficient
and the size of the equipment.
The energy transferred is given by
Q UADT WC T T 89
¼ ¼ i p(cid:4)ð 1(cid:3) 2Þ ð Þ
The overall heat transfer coefficient is obtained from Eq. (4),
1 d 1 d d d
o ln o ff o ff
U ¼hd þh þ24K d þ i d þ o
i i o m i i
BecausetheinsidecoefficientgovernsU,wecanrewriteEq.(4)asfollows
(neglecting lower order resistances, such as h , metal resistance, and fouling
o
factors, which contribute to about 5% of U):
d
U 0:95h i 90
¼ id ð Þ
o
Copyright © 2003 Marcel Dekker, Inc.

Thevalue ofthetube-side coefficientisobtainedfrom thefamiliarDittus–
Boelter equation, Eq. (8),
Nu 0:023Re0:8 Pr0:4
¼
where
hd w
Nu i i; Re 15:2
¼12k ¼ dm
i
The fluid transport properties are evaluated at the bulk temperature.
Substituting Eqs. (8)–(11) into Eq. (90) and simplifying, we have the
following expression [Eq. (12)]:
h 2:44w0:8F =d1:8
i ¼ 1 i
where
F C =m 0:4k0:6 91
1 ¼ð p Þ ð Þ
Combining Eqs. (89)–(91) we have, after substituting A 3:14dLN=12
¼ i
and for flow per tube w W=N,
¼ i
Q LN0:2
0:606 92
DT F W0:8 ¼ (cid:4) d0:8 ð Þ
1 i i
This simple equation relates several important variables. Given Q;DT;W, and
i
F ,onecantrycombinationsofL;d,andN toarriveatasuitableconfiguration.
1 i
Also, for given thermal data, LN0:2=d0:8 is constant in Eq. (92).
i
F is shown in Table 8.35 for flue gas and air. For other gases, F can be
1 1
computed from Eq. (91).
When a phase change occurs, as in a boiler, DT is written as
T t T t
DT ð 1(cid:3) sÞ(cid:3)ð 2(cid:3) sÞ 93
¼ln T t T t ð Þ
½ð 1(cid:3) sÞ(cid:3)ð 2(cid:3) sÞ(cid:5)
CombiningEqs.(92)and(93)andsimplifying,wearriveattheexpression
T t F L
ln 1(cid:3) s 0:606 1 N0:2 94
T t ¼ (cid:4)C (cid:4) (cid:4)W0:2d0:8 ð Þ
2(cid:3) s p i i
Factor F =C is also given in Table 8.35.
1 p
Equation (94) relates the major geometric parameters to thermal perfor-
mance. Using this method, one need not evaluate heat transfer coefficients.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.35 Factors F =C ;F =C ;F , and F for Air and
1 p 2 p 2 3
FlueGasa
Temp( F) F =C F F =C F
(cid:2) 1 p 2 2 p 3
Air
100 0.6660 0.0897 0.3730 0.5920
200 0.6870 0.0952 0.3945 0.6146
300 0.7068 0.1006 0.4140 0.6350
400 0.7225 0.1056 0.4308 0.6528
600 0.7446 0.1150 0.4591 0.6810
1000 0.7680 0.1220 0.4890 0.6930
1200 0.7760 0.1318 0.5030 0.7030
0.1353 0.7150
Flue gasa
200 0.6590 0.0954 0.3698 0.5851
300 0.6780 0.1015 0.3890 0.6059
400 0.6920 0.1071 0.4041 0.6208
600 0.7140 0.1170 0.4300 0.6457
800 0.7300 0.1264 0.4498 0.6632
1000 0.7390 0.1340 0.4636 0.6735
1200 0.7480 0.1413 0.4773 0.6849
aFluegasisassumedtohave12%watervaporbyvolume.
Gas Pressure Drop
Now considergas pressure drop. The equation that relates thegeometry to tube-
side pressure drop in in.H O is
2
W 2 n
DP 9:3 10 5 f i L 5d
i ¼ (cid:4) (cid:3) (cid:4) N ð þ iÞ(cid:4)d5
(cid:1) (cid:2) i 95
W 2 ð Þ
9:3 10 5 i K n
¼ (cid:4) (cid:3) (cid:4) N 2
(cid:1) (cid:2)
where
K f L 5d =d5 96
2 ¼ ð þ iÞ i ð Þ
Combining Eqs. (94)–(96) and eliminating N,
T t F n0:1
ln 1(cid:3) s 0:24 1 K 97
T t ¼ (cid:4)C (cid:4) 1 DP0:1 ð Þ
2(cid:3) s p i
where
K L 5d 0:1Lf0:1=d1:3 98
1 ¼ð þ iÞ i ð Þ
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.36 Values ofK as aFunctionofTube Diameter andLength
1
d (in.)
i
L(ft) 1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75 3.00
8 7.09 5.33 4.22 3.46 2.92 2.52 2.20 1.95 1.75
10 8.99 6.75 5.34 4.38 3.70 3.17 2.78 2.46 2.21
12 10.92 8.20 6.48 5.31 4.48 3.85 3.36 2.98 2.67
14 12.89 9.66 7.63 6.25 5.27 4.53 3.95 3.50 3.14
16 14.88 11.14 8.80 7.21 6.07 5.21 4.55 4.02 3.61
18 16.89 12.65 9.98 8.17 6.88 5.91 5.15 4.56 4.10
20 18.92 14.16 11.17 9.14 7.70 6.60 5.76 5.10 4.56
22 20.98 15.70 12.38 10.12 8.52 7.31 6.37 5.64 5.05
24 23.05 17.24 13.59 11.11 9.35 8.02 6.99 6.19 5.54
26 25.13 18.80 14.81 12.11 10.19 8.74 7.61 6.74 6.03
28 27.24 20.37 16.05 13.11 11.00 9.46 8.74 7.30 6.52
TABLE8.37 Values ofK as aFunctionofTube Diameter andLength
2
d (in.)
i
L(ft) 1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75 3.00
8 0.2990 0.1027 0.0428 0.0424 0.0109 0.0062 0.0037 0.0024 0.0016
10 0.3450 0.1171 0.0484 0.0229 0.0121 0.0069 0.0041 0.0027 0.0018
12 0.3910 0.1315 0.0539 0.0252 0.0134 0.0075 0.0045 0.0029 0.0019
14 0.4370 0.1460 0.0595 0.0277 0.0146 0.0082 0.0049 0.0031 0.0021
16 0.4830 0.1603 0.0650 0.0302 0.0158 0.0088 0.0053 0.0033 0.0022
20 0.5750 0.1892 0.0760 0.0350 0.0183 0.0101 0.0060 0.0038 0.0025
22 0.6210 0.2036 0.0816 0.0375 0.0195 0.0108 0.0064 0.0040 0.0027
24 0.6670 0.2180 0.0870 0.0400 0.0207 0.0114 0.0067 0.0042 0.0028
26 0.7130 0.2320 0.0926 0.0423 0.0219 0.0121 0.0071 0.0045 0.0030
28 0.7590 0.2469 0.0982 0.0447 0.0231 0.0217 0.0075 0.0047 0.0031
K andK appearinTables8.36and8.37respectively,asafunctionoftube
1 2
IDandlength.Intheturbulentrange,thefrictionfactorforcold-drawntubesisa
function of inner diameter.
Using Eq. (97), one can quickly figure the tube diameter and length that
limit tube pressure drop to a desired value. Any two of the three variables N;L,
andd determinethermalperformanceaswellasgaspressuredrop.Letusdiscuss
i
the conventional design procedure:
Copyright © 2003 Marcel Dekker, Inc.

1. Assume w, calculate N.
2. Calculate U, using Eqs. (4) and (90).
3. Calculate L after obtaining A from Eq. (89).
4. Calculate DP from Eq. (95).
i
If the geometry or pressure drop obtained is unsuitable, repeat steps 1–4. This
procedure is lengthy.
Some examples will illustrate the simplified approach. The preceding
equations are valid for single-pass design. However, with minor changes one
can derive the relationships for multipass units (e.g., use length L=2 for two-
¼
pass units).
Example 1
A fire tube waste heat boiler will cool 66,000lb=h of flue gas from 1160 F to
(cid:2)
440 F. Saturation temperature is 350 F. Molecular weight is 28.5, and gas
(cid:2) (cid:2)
pressure is atmospheric. If L is to be limited to 20ft due to layout, determine
N and DP for two tube sizes: (1) 2 1.77in. (2in. OD, 1.77in. ID) and (2)
i (cid:4)
1.75 1.521in.
(cid:4)
Solution. Use Eq.(92) tofindN.Use2in.tubes.F =C from Table8.35
1 p
is0.73forfluegasattheaveragegastemperatureof0.5 (1160 440) 800 F.
(cid:2)
(cid:4) þ ¼
1160 350
ln (cid:3) 2:197
440 350 ¼
(cid:6) (cid:3) (cid:7)
20
2:197 0:606 0:73 N0:2
¼ (cid:4) (cid:4) (cid:4) 66;000 0:2 1:77 0:8
ð Þ (cid:4)ð Þ
0:6089N0:2; N 611
¼ ¼
Compute DP using Eq. (95). From Table 8.37, K is 0.035. Compute the gas
i 2
specific volume.
492
Density r 28:5 0:031lb=ft3
ð Þ¼ (cid:4)359 460 800 ¼
(cid:4)ð þ Þ
n 32:25ft3=lb
¼
Substituting into Eq. (95), we have
66;000 2
DP 9:3 10 5 0:035 32:25
i ¼ (cid:4) (cid:3) (cid:4) 611 (cid:4) (cid:4)
(cid:1) (cid:2)
1:23in:H O
¼ 2
Repeat the exercise with 1.75in. tubes; length remains at 20ft. From Eq.
(92) we note that for the same thermal performance and gas flow, N0:2L=d0:8
i ¼
Copyright © 2003 Marcel Dekker, Inc.

aconstant.Theaboveconceptcomesinhandywhenonewantstoquicklyfigure
the effect of geometry on performance. Hence,
20 20
6110:2 N0:2
(cid:4) 1:77 0:8 ¼ (cid:4) 1:521 0:8
ð Þ ð Þ
N 333
¼
Withsmallertubes,oneneedsfewertubesforthesameduty.Thisisdueto
ahigherheattransfercoefficient;however,thegaspressuredropwouldbehigher.
From Table 8.37, K 0.076 for 1.521in. tubes. From Eq. (95),
2¼
66;000 2
DP 9:3 10 5 0:076 32:25
i ¼ (cid:4) (cid:3) (cid:4) 333 (cid:4) (cid:4)
(cid:1) (cid:2)
8:95in:H O
¼ 2
Example 2
Size the heat exchanger for 2.0in. tubes with a pressure drop of 3.0in.H O. For
2
the same thermal performance, determine the geometry.
Solution. Theconventionalapproachwouldtakeseveraltrialstoarriveat
the right combination. However, with Eq. (97), one can determine the geometry
rather easily:
1160 350 F K n0:1
ln (cid:3) 2:197 0:24 1 1
440 350 ¼ ¼ (cid:4)C (cid:4) DP0:1
(cid:3) p i
From Table 8.35, F =C 0.73; DP 3, n 32.25. Then
1 p¼ i¼ ¼
1160 350
ln (cid:3) 2:197 0:24K 32:25 0:1
440 350 ¼ ¼ 1(cid:4)ð Þ
(cid:3)
0:73
0:222K
(cid:4) 30:1 ¼ 1
K 9:89
1 ¼
FromTable8.36,wecanobtainseveralcombinationsoftubediameterand
length that have the same K value and would yield the same thermal perfor-
1
mance and pressure drop. For the 1.77in. ID tube, L is 21.75ft. Use Eq. (92) to
calculate the number of tubes.
N0:2
2:197 0:606 0:73 21:75
¼ (cid:4) (cid:4) (cid:4) 66;000 0:2 1:77 0:8
ð Þ (cid:4)ð Þ
N 402
¼
Thus, several alternative tube geometries can be arrived at for the same
performance, using the preceding approach. One saves a lot of time by not
calculating heat transfer coefficients and gas properties.
Copyright © 2003 Marcel Dekker, Inc.

Life-Cycle Costing
Suchtechniques determinetheoptimum design,givenseveralalternatives.Here,
the major operating cost is from moving the gas through the system, and the
installed cost is that of the equipment and auxiliaries such as the fan. The life-
cycle cost is the sum of the capitalized cost of operation and the installed cost:
LCC C I
¼ coþ c
The capitalized cost of operation is
1 YT
C C Y (cid:3)
co ¼ a 1 Y
(cid:3)
where Y 1 e = 1 i .
¼ð þ Þ ð þ Þ
The annual cost of operating the fan is estimated as
C 0:001 PHC
a ¼ (cid:4) e
where the fan power consumption in kW is
DP
P 1:9 10 6 W i
¼ (cid:4) (cid:3) (cid:4) i(cid:4) rZ
The above procedure is used to evaluate LCC. The alternative with the lowest
LCCisusuallychosenifthegeometryisacceptable.(C iscostofelectricity.)and
e
H is the number of hours of operation per year.
8.49
Q:
Discuss the simplified approach to designing water tube boilers.
A:
Whenever gas flows outside a tube bundle—as in water tube boilers, economi-
zers, and heat exchangers with high heat transfer coefficients on the tube side—
the overall coefficient is governed by the gas-side resistance. Assuming that the
other resistances contribute about 5% to the total, and neglecting the effect of
nonluminous transfer coefficients, one may write the expression for U as
U 0:95h 99a
¼ o ð Þ
where the outside coefficient, h , is obtained from
o
Nu 0:35Re0:6 Pr0:3 99b
¼ ð Þ
Copyright © 2003 Marcel Dekker, Inc.

where, using Eqs. (16)–(18) and (21),
h d Gd mC
Nu o o; Re ; Pr p
¼ 12k ¼12m ¼ k
W
G 12 o
¼ N L S d
w ð T (cid:3) oÞ
Equation(99)isvalidforbothin-line(squareorrectangularpitch)andstaggered
(triangular pitch) arrangements. For bare tubes, the difference in h between in-
o
line and staggered arrangements at Reynolds numbers and pitches found in
practice is 3–5%. For finned tubes, the variation is significant.
Substituting Eqs. (17)–(21) into Eq. (99a) and (99b) and simplifying,
h 0:945G0:6F =d0:4 100
o ¼ 2 o ð Þ
U 0:9G0:6F =d0:4 101
¼ 2 o ð Þ
where
F k0:7 C =m 0:3 102
2 ¼ ð p Þ ð Þ
F is given in Table 8.35. Gas transport properties are computed at the film
2
temperature.
A pd N N L=12
¼ o w d
Combining the above with Eq. (89) and simplifying gives
Q=DT UA p0:9G0:6F d N N L=12d0:4
¼ ¼ 2 o w d o
0:235F G0:6N N Ld0:6
¼ 2 w d o
Substituting for G from Eq. (21),
Q N0:4L0:4N
1:036F W0:6 w d 103
DT ¼ 2 o S =d 1 0:6 ð Þ
ð T o(cid:3) Þ
The above equation relates thermal performance to geometry. When there is a
phase change, as in a boiler, further simplification leads to
T t F N
ln 1(cid:3) s 2:82 2 d 104
T t ¼ C (cid:4)G0:4 S =d 1 d0:4 ð Þ
2(cid:3) s p ð T o(cid:3) Þ o
Ifthetubediameterandpitchareknown,onecanestimateN orG foradesired
d
thermal performance.
Letusnowaccountforgaspressuredrop.Theequationthatrelatesthegas
pressure drop to G is Eq. (28) of Chapter 7:
N
DP 9:3 10 10 G2f d
o ¼ (cid:4) (cid:3) (cid:4) r
Copyright © 2003 Marcel Dekker, Inc.

Forin-linearrangements,thefrictionfactorisobtainedfromEq.(29)ofChapter
7:
f Re 0:15 X
(cid:3)
¼
where
0:08S =d
X 0:044 L o
¼ þ ð S T =d o(cid:3) 1 Þ 0:43 þ 1:13d o =S L
Another form of Eq. (28) of Chapter 7 is
W1:85nN2:85m0:15X
DP 1:34 10 7 o d 105
o ¼ (cid:4) (cid:3) (cid:4)N1:85L1:85d0:15 S d 1:85 ð Þ
w o ð T (cid:3) oÞ
Substitutingforf inEq.(28)ofChapter7andcombiningwithEq.(104)wecan
relate DP to performance in a single equation:
o
DP 4:78 10 10 G2:25 S d
o ¼ (cid:4) (cid:3) (cid:4) ð T (cid:3) oÞ
T t X
ln 1(cid:3) s 106
(cid:4) T t (cid:4)d0:75 F r ð Þ
(cid:6) 2(cid:3) s(cid:7) o 3
where
F F =C m 0:15 107
3 ¼ð 2 pÞ (cid:3) ð Þ
F is given in Table 8.35. With Eq. (107), one can easily calculate thegeometry
3
for a given tube bank so as to limit the pressure drop to a desired value. An
example will illustrate the versatility of the technique.
Example
In a water tube boiler, 66,000lb=h of flue gas is cooled from 1160 F to 440 F.
(cid:2) (cid:2)
Saturation temperature is 350 F. Tube outside diameter is 2in., and an in-line
(cid:2)
arrangement is used with S S 4in. Determine a suitable configuration to
T ¼ L¼
limit the gas pressure to 3in.H O.
2
Let us use Eq. (106). Film temperature is 0.5 (800 350) 575 F.
(cid:2)
(cid:4) þ ¼
Interpolating from Table 8.35 at 475 F, F 0:643. Gas density at 800 F is
0.031lb=ft3 from Example 1. (cid:2) 3 ¼ (cid:2)
DP 4:78 10 10 G2:25 4 2
o ¼ (cid:4) (cid:3) (cid:4) ð (cid:3) Þ
1160 350
ln (cid:3)
(cid:4) 440 350
(cid:6) (cid:3) (cid:7)
0:044 0:08 2
ð þ (cid:4) Þ
(cid:4)20:75 0:643 0:031
(cid:4) (cid:4)
128 10 10 G2:25 3
(cid:3)
¼ (cid:4) (cid:4) ¼
Copyright © 2003 Marcel Dekker, Inc.

Hence, G 5200lb=ft2 h. From Eq. (21) one can choose different combinations
¼
of N and L:
w
N L 66;000 12= 2 5200 76
w ¼ (cid:4) ð (cid:4) Þ¼
If N 8, then L 9.5ft.
w ¼ ¼
Calculate N from Eq. (104):
d
1160 350
ln (cid:3) 2:197
440 350 ¼
(cid:6) (cid:3) (cid:7)
F N
2:82 2 d
¼ C (cid:4)G0:4 S d 1 d0:4
p ð T o(cid:3) Þ o
2:197 2:82 0:426N = 52000:4 1 20:4 orN 74
¼ (cid:4) d ð (cid:4) (cid:4) Þ d ¼
Thus, the entire geometry has been arrived at.
8.50
Q:
How is the bundle diameter of heat exchangers or fire tube boilers determined?
A:
Tubesofheatexchangersandfiretubeboilersaretypicallyarrangedinsquareor
triangular pitch (Fig.8.20).The ratio oftube pitch to diameter could range from
1.25 to 2 depending on the tube size and the manufacturer’s past practice.
Lookingatthetriangularpitcharrangement,weseethathalfofatubearea
is located within the triangle, whose area is given by
Area of triangle 0:5 0:866p2 0:433p2
¼ (cid:4) ¼
If there are N tubes in the bundle, then
Total area occupied 0:866Np2
¼
If the bundle diameter is D, then 3:14 D2=4 area of bundle 0.866Np2, or
(cid:4) ¼ ¼
D 1:05pN0:5 108
¼ ð Þ
Similarly,forthesquarepitch,theareaoccupiedbyonetube p2.Hencebundle
¼
area 3:14 D2=4 Np2, or
¼ (cid:4) ¼
D 1:128pN0:5 109
¼ ð Þ
In practice, a small clearance is added to the above number for manufacturing
purposes.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.20 Square (top) and triangular (bottom) pitch for boiler=exchanger
tubes.
Copyright © 2003 Marcel Dekker, Inc.

Example
If500tubes of2in.diameter arelocatedinafiretube boiler shellatatriangular
pitch of 3in., the bundle diameter would be
D 1:05 3 5000:5 70:5in:
¼ (cid:4) (cid:4) ¼
If the pitch were square, the bundle diameter would be
D 1:128 3 5000:5 75:7in:
¼ (cid:4) (cid:4) ¼
Sometimes tubes have to be located within a given sector of a circle. In such
cases, it is helpful to know the area of a sector of a circle given its height and
diameter. Table 8.38 gives the factor C, which when multiplied by D2 gives the
sector area.
Example
Find the area of a sector of height 10in. and diameter 24in.
Solution. Forh=D 10=24 0:4167;CfromTable8.38 0.309.Hence,
¼ ¼ ¼
Area C D2 0:309 24 24 178in:2
¼ (cid:4) ¼ (cid:4) (cid:4) ¼
8.51
Q:
How is the thickness of insulation for a flat or curved surface determined?
Determinethethicknessof insulationtolimitthecasingsurfacetemperatureofa
pipe operating from 800 F to 200 F, when
(cid:2) (cid:2)
Ambient temperature t 80 F
a¼ (cid:2)
Thermal conductivity of insulation K at average temperature of 500 F
0.35Btuin.=ft2h F m (cid:2) ¼
(cid:2)
Pipe outer diameter d 12in.
¼
Wind velocity V 264ft=min (3mph)
¼
Emissivity of casing 0.15 (oxidized)
¼
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.38 C Factorsfor FindingAreaof SectorofaCircle (Area CD2)
¼
h=D C h=D C h=D C h=D C h=D C
0.050 0.01468 0.100 0.04087 0.150 0.07387 0.200 0.11182
0.001 0.00004 0.051 0.01512 0.101 0.04148 0.151 0.07459 0.201 0.11262
0.002 0.00012 0.052 0.01556 0.102 0.04208 0.152 0.07531 0.202 0.11343
0.003 0.00022 0.053 0.01601 0.103 0.04269 0.153 0.07603 0.203 0.11423
0.004 0.00034 0.054 0.01646 0.104 0.04330 0.154 0.07675 0.204 0.11504
0.005 0.00047 0.055 0.01691 0.105 0.04391 0.155 0.07747 0.205 0.11584
0.006 0.00062 0.056 0.01737 0.106 0.04452 0.156 0.07819 0.206 0.11665
0.007 0.00078 0.057 0.01783 0.107 0.04514 0.157 0.07892 0.207 0.11746
0.008 0.00095 0.058 0.01830 0.108 0.04578 0.158 0.07965 0.208 0.11827
0.009 0.00113 0.059 0.01877 0.109 0.04638 0.159 0.08038 0.209 0.11908
0.010 0.00133 0.060 0.01924 0.110 0.04701 0.160 0.08111 0.210 0.11990
0.011 0.00153 0.061 0.01972 0.111 0.04763 0.161 0.08185 0.211 0.12071
0.012 0.00175 0.062 0.02020 0.112 0.04826 0.162 0.08258 0.212 0.12153
0.013 0.00197 0.063 0.02068 0.113 0.04889 0.163 0.08332 0.213 0.12235
0.014 0.00220 0.064 0.02117 0.114 0.04953 0.164 0.08406 0.214 0.12317
0.015 0.00244 0.065 0.02166 0.115 0.05016 0.165 0.08480 0.215 0.02399
0.016 0.00268 0.066 0.02215 0.116 0.05080 0.166 0.08554 0.216 0.12481
0.017 0.00294 0.067 0.02265 0.117 0.05145 0.167 0.08629 0.217 0.12563
0.018 0.00320 0.068 0.02315 0.118 0.05209 0.168 0.08704 0.218 0.12646
0.019 0.00347 0.069 0.02366 0.119 0.05274 0.169 0.08779 0.219 0.12729
0.020 0.00375 0.070 0.02417 0.120 0.05338 0.170 0.08854 0.220 0.12811
0.021 0.00403 0.071 0.02468 0.121 0.05404 0.171 0.08929 0.221 0.12894
0.022 0.00432 0.072 0.02520 0.122 0.05469 0.172 0.09004 0.222 0.12977
0.023 0.00462 0.073 0.02571 0.123 0.05535 0.173 0.09080 0.223 0.13060
0.024 0.00492 0.074 0.02624 0.124 0.05600 0.174 0.09155 0.224 0.13144
(continued)
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.38 (continued)
h=D C h=D C h=D C h=D C h=D C
0.025 0.00523 0.075 0.02676 0.125 0.05666 0.175 0.09231 0.225 0.13277
0.026 0.00555 0.076 0.02729 0.126 0.05733 0.176 0.09307 0.226 0.13311
0.027 0.00587 0.077 0.02782 0.127 0.05799 0.177 0.09384 0.227 0.13395
0.028 0.00619 0.078 0.02836 0.128 0.05866 0.178 0.09460 0.228 0.13478
0.029 0.00653 0.079 0.02889 0.129 0.05933 0.179 0.09537 0.229 0.13562
0.030 0.00687 0.080 0.02943 0.130 0.06000 0.180 0.09613 0.230 0.13646
0.031 0.00721 0.081 0.02998 0.131 0.06067 0.181 0.09690 0.231 0.13731
0.032 0.00756 0.082 0.03053 0.132 0.06135 0.182 0.09767 0.232 0.13815
0.033 0.00791 0.083 0.03108 0.133 0.06203 0.183 0.09845 0.233 0.13900
0.034 0.00827 0.084 0.03163 0.134 0.06271 0.184 0.09922 0.234 0.13984
0.035 0.00864 0.085 0.03219 0.135 0.06339 0.185 0.10000 0.235 0.14069
0.036 0.00901 0.086 0.03275 0.136 0.06407 0.186 0.10077 0.236 0.14154
0.037 0.00938 0.087 0.03331 0.137 0.06476 0.187 0.10155 0.237 0.14239
0.038 0.00976 0.088 0.03387 0.138 0.06545 0.188 0.10233 0.238 0.14324
0.039 0.01015 0.089 0.03444 0.139 0.06614 0.189 0.10312 0.239 0.14409
0.040 0.01054 0.090 0.03501 0.140 0.06683 0.190 0.10390 0.240 0.14494
0.041 0.01093 0.091 0.03559 0.141 0.06753 0.191 0.10469 0.241 0.14580
0.042 0.01133 0.092 0.03616 0.142 0.06822 0.192 0.10547 0.292 0.14666
0.043 0.01173 0.093 0.03674 0.143 0.06892 0.193 0.10626 0.243 0.14751
0.044 0.01214 0.094 0.03732 0.144 0.06963 0.194 0.10705 0.244 0.14837
0.045 0.01255 0.095 0.03791 0.145 0.07033 0.195 0.10784 0.245 0.14923
0.046 0.01297 0.096 0.03850 0.146 0.07103 0.196 0.10864 0.246 0.15009
0.047 0.01339 0.097 0.03909 0.147 0.07174 0.197 0.10943 0.247 0.15095
0.048 0.01382 0.098 0.03968 0.148 0.07245 0.198 0.11023 0.248 0.15182
0.049 0.01425 0.099 0.04028 0.149 0.07316 0.199 0.11102 0.249 0.15268
0.250 0.15355 0.300 0.19817 0.350 0.24498 0.400 0.29337 0.450 0.34278
Copyright © 2003 Marcel Dekker, Inc.

0.251 0.15441 0.301 0.19908 0.351 0.24593 0.401 0.29435 0.451 0.34378
0.252 0.15528 0.302 0.20000 0.352 0.24689 0.402 0.29533 0.452 0.34477
0.253 0.15615 0.303 0.20092 0.353 0.24784 0.403 0.29631 0.453 0.34577
0.254 0.15702 0.304 0.20184 0.354 0.24880 0.404 0.29729 0.454 0.34676
0.255 0.15789 0.305 0.20276 0.355 0.24976 0.405 0.29827 0.455 0.34776
0.256 0.15876 0.306 0.20368 0.356 0.25071 0.406 0.29926 0.456 0.34876
0.257 0.15964 0.307 0.20460 0.357 0.25167 0.407 0.30024 0.457 0.34975
0.258 0.16501 0.308 0.20553 0.358 0.25263 0.408 0.30122 0.458 0.35075
0.259 0.16139 0.309 0.20645 0.359 0.25359 0.409 0.30220 0.459 0.35175
0.260 0.16226 0.310 0.20738 0.360 0.25455 0.410 0.30319 0.460 0.35274
0.261 0.16314 0.311 0.20830 0.361 0.25551 0.411 0.30417 0.461 0.35374
0.262 0.16402 0.312 0.20923 0.362 0.25647 0.412 0.30516 0.462 0.35474
0.263 0.16490 0.313 0.21015 0.363 0.25743 0.413 0.30614 0.463 0.35573
0.264 0.16578 0.314 0.21108 0.364 0.25839 0.414 0.30712 0.464 0.35673
0.265 0.16666 0.315 0.21201 0.365 0.25936 0.415 0.30811 0.465 0.35773
0.266 0.16755 0.316 0.21294 0.366 0.26032 0.416 0.30910 0.466 0.35873
0.267 0.16843 0.317 0.21387 0.367 0.26128 0.417 0.31008 0.467 0.35972
0.268 0.16932 0.318 0.21480 0.368 0.26225 0.418 0.31107 0.468 0.36072
0.269 0.17020 0.319 0.21573 0.369 0.26321 0.419 0.31205 0.469 0.36172
0.270 0.17109 0.320 0.21667 0.370 0.26418 0.420 0.31304 0.470 0.36272
0.271 0.17198 0.321 0.21760 0.371 0.26514 0.421 0.31403 0.471 0.36372
0.272 0.17287 0.322 0.21853 0.372 0.26611 0.422 0.31502 0.472 0.36471
0.273 0.17376 0.323 0.21947 0.373 0.26708 0.423 0.31600 0.473 0.36571
0.274 0.17465 0.324 0.22040 0.374 0.26805 0.424 0.31699 0.474 0.36671
0.275 0.17554 0.325 0.22134 0.375 0.26901 0.425 0.31798 0.475 0.36771
0.276 0.17644 0.326 0.22228 0.376 0.26998 0.426 0.31897 0.476 0.36871
0.277 0.17733 0.327 0.22322 0.377 0.27095 0.427 0.31996 0.477 0.36971
0.278 0.17823 0.328 0.22415 0.378 0.27192 0.428 0.32095 0.478 0.37071
(continued)
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.38 (continued)
h=D C h=D C h=D C h=D C h=D C
0.279 0.17912 0.329 0.22509 0.379 0.27289 0.429 0.32194 0.479 0.37171
0.280 0.18002 0.330 0.22603 0.380 0.27386 0.430 0.32293 0.480 0.37270
0.281 0.18092 0.331 0.22697 0.381 0.27483 0.431 0.32392 0.481 0.37370
0.282 0.18182 0.332 0.22792 0.382 0.27580 0.432 0.32491 0.482 0.37470
0.283 0.18272 0.333 0.22886 0.383 0.27678 0.433 0.32590 0.483 0.37570
0.284 0.18362 0.334 0.22980 0.384 0.27775 0.434 0.32689 0.484 0.37670
0.285 0.18452 0.335 0.23074 0.385 0.27872 0.435 0.32788 0.485 0.37770
0.286 0.18542 0.336 0.23169 0.386 0.27969 0.436 0.32887 0.486 0.37870
0.287 0.18633 0.337 0.23263 0.387 0.28067 0.437 0.32987 0.487 0.37970
0.288 0.18723 0.338 0.23358 0.388 0.28164 0.438 0.33086 0.488 0.38070
0.289 0.18814 0.339 0.23453 0.389 0.28262 0.439 0.33185 0.489 0.38170
0.290 0.18905 0.340 0.23547 0.390 0.28359 0.440 0.33284 0.490 0.38270
0.291 0.18996 0.341 0.23642 0.391 0.28457 0.441 0.33384 0.491 0.38370
0.292 0.19086 0.342 0.23737 0.392 0.28554 0.442 0.33483 0.492 0.38470
0.293 0.19177 0.343 0.23832 0.393 0.28652 0.443 0.33582 0.493 0.38570
0.294 0.19268 0.344 0.23927 0.394 0.28750 0.444 0.33682 0.494 0.38670
0.295 0.19360 0.345 0.24022 0.395 0.28848 0.445 0.33781 0.495 0.38770
0.296 0.19451 0.346 0.24117 0.396 0.28945 0.446 0.33880 0.496 0.38870
0.297 0.19542 0.347 0.24212 0.397 0.29043 0.447 0.33980 0.497 0.38970
0.298 0.19634 0.348 0.24307 0.398 0.29141 0.448 0.34079 0.498 0.39070
0.299 0.19725 0.349 0.24403 0.399 0.29239 0.449 0.34179 0.499 0.38170
0.500 0.39270
Copyright © 2003 Marcel Dekker, Inc.

A:
The heat loss q from the surface is given by [7]
t 459:6 4 t 459:6 4
q 0:174e sþ aþ
¼ " 100 (cid:3) 100 #
(cid:1) (cid:2) (cid:1) (cid:2)
V 68:9 1=2
0:296 t t 1:25 þ 110
þ ðs(cid:3) aÞ (cid:4) 68:9 ð Þ
(cid:1) (cid:2)
emaybetakenas0.9foroxidizedsteel,0.05forpolishedaluminum,and0.15for
oxidized aluminum. Also,
K t t K t t
q mð (cid:3) sÞ mð (cid:3) sÞ 111
¼ d 2L =2 ln d 2L =d ¼ L ð Þ
½ð þ Þ (cid:5)(cid:4) ½ð þ Þ (cid:5) e
where t is the hot face temperature, F, and L is the equivalent thickness of
(cid:2) e
insulation for a curved surface such as a pipe or tube.
d 2L d 2L
L þ ln þ 112
e ¼ 2 d ð Þ
Substituting t 200, t 80, V 264, and e 0.15 into Eq. (110), we have
s¼ a¼ ¼ ¼
q 0:173 0:15 6:64 5:44 0:296
¼ (cid:4) (cid:4)ð (cid:3) Þþ
264 69 0:5
660 540 1:25 þ
(cid:4)ð (cid:3) Þ (cid:4) 69
(cid:1) (cid:2)
285Btu=ft2 h
¼
From Eq. (111),
800 200
L 0:35 (cid:3) 0:74in:
e ¼ (cid:4) 285 ¼
We can solve for L given L and d by using Eq. (112) and trial and error, or we
e
canuseTable8.39.ItcanbeshownthatL 0.75in.Thenextstandardthickness
¼
available will be chosen. A trial-and-error method as discussed next will be
neededtosolveforthesurfacetemperaturet .(NotethatListheactualthickness
s
of insulation.)
8.52
Q:
Determine the surface temperature of insulation in Q8.51 when 1.0in. thick
insulation is used on the pipe. Other data are as given earlier.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.39 Equivalent Thicknessof Insulation,aL
e
Thickness ofinsulation L(in.)
Tube diam.d (in.) 0.5 1 1.5 2.0 3.0 4.0 5.0 6.0
1 0.69 1.65 2.77 4.0 6.80 9.90 13.2 16.7
2 0.61 1.39 2.29 3.30 5.50 8.05 10.75 13.62
3 0.57 1.28 2.08 2.97 4.94 7.15 9.53 12.07
4 0.56 1.22 1.96 2.77 4.55 6.60 8.76 11.10
5 0.55 1.18 1.88 2.65 4.34 6.21 8.24 10.40
6 0.54 1.15 1.82 2.55 4.16 5.93 7.85 9.80
8 0.53 1.12 1.75 2.43 3.92 5.55 7.50 9.15
10 0.52 1.09 1.70 2.35 3.76 5.29 6.93 8.57
12 0.52 1.08 1.67 2.30 3.65 5.11 6.65 8.31
16 0.52 1.06 1.63 2.23 3.50 4.86 6.31 7.83
20 0.51 1.05 1.61 2.19 3.41 4.70 6.10 7.52
d 2L d 2L
aL þ ln þ .Forexample,ford 3andL 1.5,L 2.08.
e¼ 2 d ¼ ¼ e¼
A:
Calculate the equivalent thickness L . From Eq. (112),
e
12 2 14
L þ ln 1:08in:
e ¼ 2 12¼
Assume that for the first trial t 150 F. Let K at a mean temperature of
(800 150)=2 475 F be 0.34B s t ¼ uin.=f (cid:2) t2h F. Fro m m Eq. (110),
(cid:2) (cid:2)
þ ¼
q 0:173 0:15 6:14 5:44 0:296
¼ (cid:4) (cid:4)ð (cid:3) Þþ
264 69 0:5
610 540 1:25 þ
(cid:4)ð (cid:3) Þ (cid:4) 69
(cid:1) (cid:2)
145Btu=ft2 h
¼
From Eq. (111),
800 150
q 0:34 (cid:3) 205Btu=ft2 h
¼ (cid:4) 1:08 ¼
Because these twovalues of q do not agree, we must go for another trial.
Try t 170 F. Then, from Eq. (110),
s¼ (cid:2)
q 200Btu=ft2h
¼
Copyright © 2003 Marcel Dekker, Inc.

and from Eq. (111),
q 198Btu=ft2h
¼
These two are quite close. Hence the final surface temperature is 170 F, and the
(cid:2)
heat loss is about 200Btu=ft2h.
8.53
Q:
A horizontal flat surface is at 10 F. The ambient dry bulb temperature is 80 F,
(cid:2) (cid:2)
and the relative humidity is 80%. Determine the thickness of fibrous insulation
that will prevent condensation of water vapor on the surface. Use K
m¼
0.28Btu=fth F. The wind velocity is zero. Use a surface emissivity of 0.9 for
(cid:2)
the casing.
A:
The surface temperature must be above the dew point of water to prevent
condensation of water vapor. Q5.10shows howthe dewpoint canbecalculated.
The saturated vapor pressure at 80 F, from the steam tables in the Appendix, is
(cid:2)
0.51psia. At 80% relative humidity, the vapor pressure will be 0.8 0.51
(cid:4) ¼
0.408psia.Fromthesteamtables,thiscorrespondstoasaturationtemperatureof
73 F, which is also the dew point. Hence we must design the insulation so the
(cid:2)
casing temperature is above 73 F.
(cid:2)
From Eq. (110),
q 0:173 0:9 5:44 5:334
¼ (cid:4) (cid:4)ð (cid:3) Þ
0:296 80 73 1:25 10:1Btu=ft2 h
þ (cid:4)ð (cid:3) Þ ¼
Also, from Eq. (111),
K 0:28
q t t m 73 10
¼ðd (cid:3) sÞ(cid:4) L ¼ð (cid:3) Þ(cid:4) L
(In this case of a flat surface, L L.)
e ¼
Note that the heat flow is from the atmosphere to the surface. t and t are
d s
the dew point and surface temperature, F. Solving for L, we get L 1.75in.
(cid:2)
¼
Hence, by using the next standard insulation thickness available, we can
ensure that the casing is above the dew point. To obtain the exact casing
temperaturewiththestandardthicknessof insulation,atrial-and-error procedure
as discussed in Q8.52 may be used. But this is not really necessary, because we
have provided a safe design thickness.
Copyright © 2003 Marcel Dekker, Inc.

8.54a
Q:
A11in.schedule40pipe1000ftlongcarrieshotwaterat300 F.Whatistheheat
2 (cid:2)
lossfromitssurfaceif itisnotinsulated(case1)orif ithas1in.,2in.,and3in.
thick insulation (case 2)?
The thermal conductivity of insulation may be assumed to be
0.25Btuin.=ft2h F. The ambient temperature is 80 F, and the wind velocity is
(cid:2) (cid:2)
zero.
A:
Case1. Equation(110)canbeusedtodeterminetheheatloss.Forthebarepipe
surface, assume that e is 0.90. Then
q 0:173 0:9 7:64 5:44
¼ (cid:4) (cid:4)ð (cid:3) Þ
0:296 300 80 1:25 638Btu=ft2 h
þ (cid:4)ð (cid:3) Þ ¼
Case2. Determinationofthesurfacetemperaturegiventheinsulationthickness
involves a trial-and-error procedure as discussed in Q8.52 and will be done in
detail for the 1in. case.
Various surface temperatures are assumed, and q is computed from Eqs.
(110)and(111).Letususeaevalueof0.15.Thefollowingtablegivestheresults
of the calculations.
t q fromEq. (110) q fromEq. (111)
s
110 26 34
120 37 32
140 61 28
We can draw a graph of t versus q with these values and obtain the correct t .
s s
However,weseefromthetable,byinterpolation,thatatt 115 F,q,fromboth
equations, is about 33Btu=ft2 h.
s¼ (cid:2)
3:9
Total heat loss 3:14 1000 33
¼ (cid:4) 12 (cid:4) (cid:4)
33;675Btu=h
¼
Similarly,wemaysolveforqwhenthethicknessesare2and3in.Itcanbeshown
that at L 2in., q 15Btu=ft2 h, and at L 3in., q 9Btu=ft2 h. Also, when
¼ ¼ ¼ ¼
L 2in., t 98 Fand total heat loss 23,157Btu=h. When L 3in., t 92 F
¼ s¼ (cid:2) ¼ ¼ s¼ (cid:2)
and total loss 18,604Btu=h.
¼
Copyright © 2003 Marcel Dekker, Inc.

8.54b
Q:
Estimate the drop in water temperature of 1in. thick insulation used in Q8.54a.
The water flow is 7500lb=h.
A:
The total heat loss has been shown to be 33,675Btu=h. This is lost by thewater
and can be written as 7500 DT, where DT is the drop in temperature, assuming
that the specific heat is 1. Hence
33;675
DT 4:5 F
(cid:2)
¼ 7500 ¼
Byequatingtheheatloss frominsulationtotheheatlostbythe fluid,beit
air, oil, steam, or water, one can compute the drop in temperature in the pipe or
duct. This calculation is particularly important when oil lines are involved,
because viscosity is affected, leading to pumping and atomization problems.
8.55
Q:
InQ8.54determinetheoptimumthicknessof insulationwiththefollowingdata.
Cost of energy $3=MMBtu
¼
Cost of operation $8000=year
¼
Interest and escalation rates 12% and 7%
¼
Life of the plant 15 years
¼
Total cost of 1in. thick insulation, including labor and material, $5200;
¼
for 2in. insulation, $7100; and for 3in. insulation, $10,500
A:
Let us calculate the capitalization factor F from Q5.22.
1:07 1 1:07=1:12 15
F (cid:3)ð Þ 10:5
¼1:12(cid:4) 1 1:07=1:12 ¼
(cid:3)
Let us calculate the annual heat loss.
For L 1in.,
¼
8000
C 33;675 3 $808
a ¼ (cid:4) (cid:4) 106 ¼
Copyright © 2003 Marcel Dekker, Inc.

For L 2in.,
¼
8000
C 23;157 3 $555
a ¼ (cid:4) (cid:4) 106 ¼
For L 3in.,
¼
8000
C 18;604 3 $446
a ¼ (cid:4) (cid:4) 106 ¼
Calculate capitalized cost C F.
a
For L 1in.,
¼
C F 808 10:5 $8484
a ¼ (cid:4) ¼
For L 2in.,
¼
C F 555 10:5 $5827
a ¼ (cid:4) ¼
For L 3in.,
¼
C F 446 10:5 $4683
a ¼ (cid:4) ¼
Calculate total capitalized cost or life-cycle cost (LCC):
For L 1in.,
¼
LCC 8484 5200 $13;684
¼ þ ¼
For L 2in., LCC $12,927; and for L 3in., LCC $15,183.
¼ ¼ ¼ ¼
Hence we see that the optimum thickness is about 2in. With higher
thicknesses, the capital cost becomes more than the benefits from savings in
heat loss. A trade-off would be to go for 2in. thick insulation.
Severalfactorsenterintocalculationsofthistype.Iftheperiodofoperation
were less, probably a lesser thickness would be adequate. If the cost of energy
were more, we might havetogo fora greater thickness. Thus each case must be
evaluatedbeforewedecideontheoptimumthickness.Thisexamplegivesonlya
methodology, and the evaluation can be as detailed as desired by the plant
engineering personnel.
If there were no insulation, the annual heat loss would be
1:9 8000
3:14 1000 638 3 $7600
(cid:4) 12 (cid:4) (cid:4) (cid:4) (cid:4) 106 ¼
Hence simple payback with even 1in. thick insulation is 5200=
(76007808) 0.76 year, or 9 months.
¼
8.56
Q:
What is a hot casing? What are its uses?
Copyright © 2003 Marcel Dekker, Inc.

A:
Whenever hot gases are contained in an internally refractory-lined (or insulated)
duct,thecasingtemperaturecanfallbelowthedewpointofacidgases,whichcan
seep through the refractory cracks and cause acid condensation, which is a
potential problem. To avoid this, some engineers prefer a ‘‘hot casing’’design,
which ensures that the casing or the vessel or duct containing the gases is
maintained at a high enough temperature to minimize or prevent acid condensa-
tion.Atthesametime,thecasingisalsoexternallyinsulatedtominimizetheheat
lossestotheambient(seeFig.8.21).A‘‘hotcasing’’isacombinationof internal
plusexternalinsulationusedtomaintainthecasingatahighenoughtemperature
to avoidacid condensation while ensuring that the heat losses to the atmosphere
are low.
Consider the use of a combination of two refractories inside the boiler
casing: 4in. of KS4 and 2in. of CBM. The hot gases are at 1000 F. Ambient
(cid:2)
temperature 60 F, and wind velocity is 100ft=min. Casing emissivity is 0.9.
(cid:2)
¼
To keep the boiler casing hot, an external 0.5in. of mineral fiber is added.
Determine the boiler casing temperature, the outer casing temperature, and the
heat loss.
One can perform the calculations discussed earlier to arrive at the
temperatures and heat loss. For the sake of illustrating the point, a computer
printoutoftheresultisshowninFig.8.22.Itcanbeseenthattheboilercasingis
at392 F,andtheoutermostcasingisat142 F.Theheatlossis180Btu=ft2h.The
(cid:2) (cid:2)
boiler casing is hot enough to avoidacid condensation, while the heat losses are
kept low.
FIGURE 8.21 Arrangement ofhot casing.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.22 Printouton casingtemperatures.
8.57
Q:
What happens if ducts or stacks handling flue gases are not insulated? What
would the gas or stack wall temperature be?
A:
This question faces engineers involved in engineering of boiler plants. If ducts
andstacksarenotinsulated,theheatlossfromthecasingcanbesubstantial.Also,
the stack wall temperature can drop low enough to cause acid dew point
corrosion.
Let the flue gas flow be W lb=h at a temperature of t at the inlet to the
g1
ductorstack(Fig.8.23).TheheatlossfromthecasingwallisgivenbyEq.(110),
t 460 4 t 460 4
q 0:174e cþ aþ
¼ (cid:4)" 100 (cid:3) 100 #
(cid:1) (cid:2) (cid:1) (cid:2)
V 69 0:5
0:296 t t 1:25 þ
þ ðc(cid:3) aÞ (cid:4) 69
(cid:6) (cid:7)
The temperature drop across the gas film is given by
d =d
t t q o i
g(cid:3) w1 ¼ h
c
Copyright © 2003 Marcel Dekker, Inc.

where
h convective heat transfer coefficient Btu=ft2h F
c¼ (cid:2)
d ;d outer and inner diameter of the stack, in.
o i¼
W0:8C
h 2:44
c ¼ (cid:4) d1:8
i
where, from Eq. (12),
C 0:4
C p k0:6
¼ m
(cid:1) (cid:2)
TheductwalltemperaturedropisgivenbyEq.(111),whichcanberearrangedto
give
ln d =d
t t qd ð o iÞ
w1(cid:3) wo ¼ o 24K
m
where t ;t are the inner and outer wall temperatures, F.
w1 wo (cid:2)
ThetotalheatlossfromtheductorstackisQ 3:14d H=12whereH is
¼ o(cid:4)
the height, ft. The exit gas temperature is then
Q
t t 113
g2 ¼ g1(cid:3)W C ð Þ
g(cid:4) p
FIGURE 8.23 Stackwall temperature.
Copyright © 2003 Marcel Dekker, Inc.

Theaboveequationshavetobesolvediteratively.Atrialvaluefort isassumed,
g2
and the gas properties are computed at the average gas temperature. The casing
temperature is also obtained through an iterative process. The total heat loss is
computed and t is again evaluated. If the assumed and calculated t values
g2 g2
agree, then iteration stops. A computer program can be developed to obtain
accurateresults,particularlyifthestackistallandcalculationsarebetterdonein
several segments.
Example
110,000lb=h of flue gases at 410 Fenter a 48in. ID stack that is 50ft long and
(cid:2)
1in. thick. If the ambient temperature is 70 F and wind velocity is 125ft=min,
(cid:2)
determine the casing temperature, total heat loss, and exit gas temperature.
Flue gas properties can be assumed to be as follows at 400 F (or com-
(cid:2)
puted from methods discussed in Q8.12 if analysis is known): C 0.265,
p¼
m 0.058lb=fth, k 0.0211Btu=fth F. Let the gas temperature drop in the
(cid:2)
¼ ¼
stack 20 F; hence the exit gas temperature 390 F.
(cid:2) (cid:2)
¼ ¼
The gas-side heat transfer coefficient is
0:265 0:4
2:44 110;000 0:8 0:0211 0:6 4:5Btu=ft2 h F
(cid:2)
(cid:4)ð Þ (cid:4) 0:058 (cid:4)ð Þ ¼
(cid:1) (cid:2)
Let the casing temperature t ( t without insulation) be 250 F.
c ¼ wo (cid:2)
q 0:174 0:9 7:1 4 5:3 4
¼ (cid:4) (cid:4)½ð Þ (cid:3)ð Þ (cid:5)
125 69 0:5
0:296 710 530 1:25 þ
þ (cid:4)ð (cid:3) Þ (cid:4) 69
(cid:1) (cid:2)
601Btu=ft2 h
¼
Gas temperature drop across gas film 601=4.5 134 F.
(cid:2)
¼ ¼
Temperature drop across the stack wall
¼
ln 50=48
601 50 ð Þ 2 (cid:2) F
(cid:4) (cid:4) 24 25 ¼
(cid:4)
Hence stack wall outer temperature 400713472 264 F.
(cid:2)
¼ ¼
It can be shown that at a casing or wall temperature of 256 F, the heat
(cid:2)
loss through gas film matches the loss through the stack wall. The heat
loss 629Btu=ft2h, and total heat loss 411,400Btu=h.
¼ ¼
411;400
Gas temperature drop 14 F
(cid:2)
¼110;000 0:265¼
(cid:4)
The average gas temperature 410714 396 F, which is close to the 400 F
(cid:2) (cid:2)
¼ ¼
assumed.Withacomputerprogram,onecanfine-tunethecalculationstoinclude
fouling factors.
Copyright © 2003 Marcel Dekker, Inc.

8.58
Q:
What are the effects of wind velocity and casing emissivity on heat loss and
casing temperature?
A:
Using the method described earlier, the casing temperature and heat loss were
determined for the case of an insulated surface at 600 F using 3in. of mineral
(cid:2)
fiberinsulation.(Aluminumcasinghasanemissivityofabout0.15,andoxidized
steel, 0.9.) The results are shown in Table 8.40.
It can be seen that the wind velocity does not result in reduction of heat
losses though the casing temperature is significantly reduced. Also, the use of
lower emissivity casing does not affect the heat loss, though the casing
temperature is increased, particularly at low wind velocity.
8.59a
Q:
How does one check heat transfer equipment for possible noise and vibration
problems?
A:
A detailed procedure is outlined in Refs. 1 and 8. Here only a brief reference to
the methodology will be made.
Whenever a fluid flows across a tube bundle such as boiler tubes in an
economizer, air heater, or superheater (see Fig. 8.24), vortices are formed and
shedinthewakebeyond thetubes.Thissheddingon alternate sides ofthetubes
causesaharmonicallyvaryingforceonthetubeperpendiculartothenormalflow
of the fluid. It is a self-excited vibration. If the frequency of the von Karman
vortices, as they are called, coincides with the natural frequency of vibration of
thetubes,resonanceoccursandthetubesvibrate,leadingtoleakageanddamage
TABLE8.40 Resultsof InsulationPerformance
Casing Emissivity Wind vel.(fpm) Heat loss Casing temp ( F)
(cid:2)
Aluminum 0.15 0 67 135
Aluminum 0.15 1760 71 91
Steel 0.90 0 70 109
Steel 0.90 1760 70 88
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.24 Crossflow of gas over tube bundles. (a) Water tube boiler design;
(b)air heater;(c)superheater.
Copyright © 2003 Marcel Dekker, Inc.

atsupports.VortexsheddingismoreprevalentintherangeofReynoldsnumbers
from 300 to 2 105. This is the range in which many boilers, economizers, and
(cid:4)
superheaters operate. Another mechanism associated with vortex shedding is
acoustic oscillation, which is normal to both fluid flow and tube length. This is
observed only with gases and vapors. These oscillations coupled with vortex
shedding lead to resonance and excessive noise. Standing waves are formed
inside the duct.
Hence in order to analyze tube bundle vibration and noise, three frequen-
cies must be computed: natural frequencyof vibration of tubes, vortex shedding
frequency, and acoustic frequency. When these are apart by at least 20%,
vibration and noise may be absent. Q8.59b–Q8.59e show how these values are
computed and evaluated.
8.59b
Q:
How is the natural frequency of vibration of a tube bundle determined?
A:
The natural frequency of transverse vibrations of a uniform beam supported at
each end is given by
C Elg 0:5
f o 114a
n ¼2p M L4 ð Þ
(cid:1) e (cid:2)
where
C a factor determined by end conditions
¼
E Young’s modulus of elasticity
¼
I moment of inertia p d4 d4 =64
¼ ¼ ð o (cid:3) iÞ
M mass per unit length of tube, lb=ft (including ash deposits, if any, on
e¼
the tube)
L tube length, ft
¼
Simplifying (114a), we have for steel tubes
90C d4 d4 0:5
f o (cid:3) i 114b
n ¼ L2 M ð Þ
(cid:1) e (cid:2)
where d and d are in inches.
o i
Table 8.41 gives C for various end conditions.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.41 Values ofC forEq. (114b)
Modeofvibration
End supportconditions 1 2 3
Bothends clamped 22.37 61.67 120.9
Oneclamped, onehinged 15.42 49.97 104.2
Bothhinged 9.87 39.48 88.8
8.59c
Q:
How is the acoustic frequency computed?
A:
f is given by V =l, where V velocity of sound at the gas temperature in the
d a uct or shell, ft= s s. It is given s b ¼ y the expression V g nRT 0:5. For flue gases
s ¼ð 0 Þ
and air, sonic velocity is obtained by substituting 32 for g , 1.4 for n, and
0
1546=MW for R, wherethe molecular weight for fluegases is nearly 29. Hence,
V 49 T0:5 115
s ¼ (cid:4) ð Þ
Wavelength l 2W=n, where W is the duct width, ft, and n is the mode of
¼
vibration.
8.59d
Q:
How is the vortex shedding frequency f determined?
e
A:
f is obtained from the Strouhal number S:
e
S f d =12V 116
¼ e o ð Þ
where
d tube outer diameter, in.
o¼
V gas velocity, ft=s
¼
S is available in the form of charts for various tube pitches; it typically ranges
from 0.2 to 0.3 (see Fig. 8.25) [1].
Q8.59e shows how a tube bundle is analyzed for noise and vibration.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.25a Strouhalnumberforin-line bank oftubes.
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.25b Strouhalnumber forstaggered bank oftubes.
8.59e
Q:
Atubularairheater11.7ftwide,12.5ftdeep,and13.5fthighisusedinaboiler.
Carbon steel tubes of 2in. OD and 0.08in. thickness are used in in-line fashion
withatransversepitchof3.5in.andlongitudinalpitchof3.0in.Theheateris40
tubes wide (3.5in. pitch) and 60 tubes deep (2.5in. pitch). Air flow across the
Copyright © 2003 Marcel Dekker, Inc.

FIGURE8.25c,d Strouhalnumber(c)forstaggeredbankoftubes(top),(d)forin-
linebank of tubes(bottom).
Copyright © 2003 Marcel Dekker, Inc.

tubes is 300,000lb=h at an average temperature of 219 F. The tubes are fixed at
(cid:2)
both ends in tube sheets. Check whether bundlevibrations are likely. Tube mass
per unit length 1.67lb=ft.
¼
A:
First compute f ;f , and f . L 13.5ft, d 2in., d 1.84in., M 1.67lb=ft,
a e n ¼ o¼ i¼ e¼
and, from Table 8.41, C 22.37.
¼
Using Eq. (114b), we have
90 22:37 24 1:844 0:5
f (cid:4) ð (cid:3) Þ 18:2Hz
n ¼ 13:5 2 (cid:4) 1:67 0:5 ¼
ð Þ ð Þ
This is in mode 1. In mode 2, C 61.67; hence f is 50.2Hz. (The first two
¼ n2
modes are important.)
Let us compute f . S from Fig. 8.25 for S =d 3.5=2 1.75 and a
e T o¼ ¼
longitudinal pitch of 3.0=2 1.5 is 0.33.
¼
From Eq. (1) of Chapter 5, r 40=(219 460) 0.059lb=cuft.
¼ þ ¼
Free gas area 40 3:5 2 13:5=12 67:5lb=ft2 h
¼ (cid:4)ð (cid:3) Þ(cid:4) ¼
(13.5isthetube length, and40tubeswide isused with apitch of3.5in.) Hence
air velocity across tubes is
300;000
V 21ft=s
¼67:5 3600 0:059¼
(cid:4) (cid:4)
Hence
12SV 0:33 21
f 12 (cid:4) 41:6Hz
e ¼ d ¼ (cid:4) 2 ¼
o
Let us compute f . T (219 460) 679 R. Hence V 49 6790:5
a ¼ þ ¼ (cid:2) s ¼ (cid:4) ¼
1277ft=s. Width W 11.7ft, and l 2 11.7 23.4ft. For mode 1 or n 1,
¼ ¼ (cid:4) ¼ ¼
f 1277=23:4 54:5Hz
a1 ¼ ¼
For n 2,
¼
f 54:5 2 109Hz
a2 ¼ (cid:4) ¼
Theresultsformodes1and2aresummarizedinTable8.42.Itcanbeseen
thatwithoutbafflesthefrequenciesf andf arewithin20%ofeachother.Hence
a e
noise problems are likely to arise. If a baffle or plate is used to divide the duct
width into two regions, the acoustic frequency is doubled as the wavelength or
width is halved. This is a practical solution to acoustic vibration problems.
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.42 SummaryofFrequenciesforModes1and2
Modeof vibrationn 1 2
f (cpsor Hz) 18.2 50.2
n
f (cpsor Hz) 41.6 41.6
e
f (without baffles) 54.5 109
a
f (with onebaffle) 109 218
a
8.59f
Q:
Whataretheotherchecksforensuringthattubebundlevibrationsareminimized?
The vortex shedding frequencies often coincide with acoustic frequency, and
oftennostandingwavesdevelopandthetransversegascolumndoesnotvibrate.
Resonance is more the exception than the rule. Chen proposed a damping
criterion C based on tube geometry as follows [1]:
Re S=d 1 2 d
C l (cid:3) 117
¼ S S=d S ð Þ
(cid:1) l (cid:2) t
where S and S are the transverse and longitudinal spacing and d is the tube
t l
diameter. The method of calculating the Strouhal number S is given in Q8.59d.
For an in-line bank of tubes without fins, Chen stated that C must exceed 600
before a standing wave develops. A large variation in C exists in practice.
According toonestudy,inspiral finned economizersC reached 15,000before a
sonic vibration developed. If C is less than 2000, then vibrations due to vortex
sheddingmaynotoccur.Vibrationanalysisisnotanexactscience,andalotof it
is based on experience operating units of similar design. In some cases the
calculations showed that the vortex shedding and acoustic frequencies were
matching but no damaging vibrations occurred.
ASME Sec.3 Appendix N1330,1995 onflow-inducedvibrationsuggests
that if the reduced damping factor C exceeds 64 where
C 4pmx=rd2 118
¼ ð Þ
thenvortexsheddingisunlikelytocausedamage.Thisisduetothelargemassof
the system compared to the low energy in the gas stream. In Eq. (118),
m mass per unit length of tube, lb=ft
¼
x damping factor (typically 0.001 for systems with no intermediate
¼
support and 0.01 for systems with intermediate supports)
r gas density, lb=ft3
¼
d tube OD, in.
¼
Copyright © 2003 Marcel Dekker, Inc.

Table8.43showstheresultsofcalculationsforawasteheatboiler thathas
both bare and finned tubes. The high gas temperature region at the entrance
section has bare tubes, and the cooler section has finned tubes.
Coincidenceofvortexsheddingfrequencywiththenaturalfrequencyinthe
fourth mode is not a concern. Due to the low amplitudes at lower modes, tube
damageisunlikely.Also,owingtothehighvalueofC,whichexceeds64,vortex
shedding is unlikely to cause tube damage.
Fluid Elastic Instability
The need for intermediate tube supports is governed by fluid elastic instability
considerations.ASMESec.3givesanideaofthestabilityoftubebundles.Ifthe
nondimensional flow velocity as a function of mass damping factor is above the
curve shown in Fig. 8.26, then intermediate supports are required; without them
frettingandwearoftubesduetovibrationispossible.Basicallythiscriteriontells
usthatifwehaveatalltubebundlewithoutintermediatesupports,itcanoscillate
due to thegas flow; intermediate supports help to increase the natural frequency
ofthetubesandthusreducethenondimensionalflowvelocity,makingthebundle
design more stable. Using the criterion showed that intermediate supports are
required even for short boilers (under 12ft high). However, based on my
experience designing several hundred water tube waste heat boilers that are
now in operation, the boilers operated well without intermediate supports,
indicating once again the generality of these types of analysis. One has to
consider operational experience of a similar unit along with these calculation
procedures before modifying any boiler design.
TABLE8.43 Damping Factors forEvaporator Tubes
Item Bare tubesection Finned section
Gas temperature, F 1600 510
(cid:2)
Gas density,lb=ft3 0.0188 0.0394
Gas velocity,ft=s 53.9 25.8
Fins No 2 0.75 0.075in.
(cid:4) (cid:4)
Tube mass,lb=ft 3.132 7.33
Tube span,ft 17.33 17.33
StrouhalnumberS 0.25 0.25
Vortexsheddingfrequency,Hz 80.85 38.66
Damping factor 0.01 0.01
Factor C 753 845
Tube naturalfreq,Hz 8.8,24, 48, 79 5.7,16, 31, 51.6
Amplitude,in. 0.0018 0.00167
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.26 Damping factorversusnondimensional flow velocity.
Example
In a boiler with mass per unit length m 3.132lb=ft, damping factor x 0.001,
gas velocity 87ft=s, and gas density r ¼ 0.0188lb=ft3, d 2in. ¼
¼ ¼ ¼
2pmx
Mass damping factor 2p 3:132 0:001 144= 0:0188 22
¼ d2r ¼ (cid:4) (cid:4) (cid:4) ð (cid:4) Þ
37:7
¼
Nondimensional velocity 12U=fd, where f natural frequency of vibration,
¼ ¼
Hz; U gas velocity, ft=s; and d tube outer diameter, in.
¼ ¼
Based on previous calculations, f 20.6Hz. Hence
¼
Flow velocity 87 12= 20:6 2 25:5
¼ (cid:4) ð (cid:4) Þ¼
ItcanbeseenfromFig.8.26thatthisisaborderlinecaseandthatanintermediate
support would have further increased the natural frequency and made the flow
velocity fall within the stable region. In practice, for tall tube bundles, inter-
mediate supports at 11–15ft intervals are used.
8.60
Q:
How are the gas properties C ;m, and k estimated for a gaseous mixture?
p
Determine C ;m, and k for a gas mixture having the following analysis at
p
1650 Fand 14.7psia.
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

Gas Vol% C m k MW
p
N 80 0.286 0.108 0.030 28
2
O 12 0.270 0.125 0.043 32
2
SO 8 0.210 0.105 0.040 64
2
Mixture properties are needed to evaluate heat transfer coefficients. For flue gas
obtained from thecombustion offossilfuels, in theabsence of fluegas analysis,
one can use the data on air.
A:
Foragaseousmixtureatatmosphericpressure,thefollowingrelationsapply.For
high gas pressures, readers are referred to Ref. 1.
ym MW
m i i i 119a
m ¼
P
y
i
pMffiffiffiWffiffiffiffiiffiffiffi ð Þ
P ppffi3ffiffiMffiffiffiffiffiWffiffi
k yk i 119b
m ¼ P i i y i 3 ffiffiMffiffiffiffiWffiffiffi i ð Þ
qffiffiffiffiffiffiffiffiffiffi
C MW y
C pi (cid:4) i 119c
pm ¼ MW y ð Þ
P (cid:4) i
where P
MW molecular weight
¼
y volume fraction of any constituent
¼
Subscript m stands for mixture.
Substituting into Eqs. (119), we have
0:286 0:8 28 0:27 0:12 32 0:21 0:08 64
C (cid:4) (cid:4) þ (cid:4) (cid:4) þ (cid:4) (cid:4)
pm ¼ 0:8 28 0:12 32 0:08 64
(cid:4) þ (cid:4) þ (cid:4)
0:272Btu=lb F
(cid:2)
¼
0:03 281=3 0:80 0:043 321=3 0:12 0:04 641=3 0:08
k (cid:4) (cid:4) þ (cid:4) (cid:4) þ (cid:4) (cid:4)
m ¼ 281=3 0:80 321=3 0:12 641=3 0:08
(cid:4) þ (cid:4) þ (cid:4)
0:032Btu=ft F
(cid:2)
¼
0:108 p28 0:8 0:125 p32 0:12 0:105 p64 0:08
m (cid:4) (cid:4) þ (cid:4) (cid:4) þ (cid:4) (cid:4)
m ¼ p28 0:8 p32 0:12 p64 0:105
ffiffiffiffiffi ffiffiffiffiffi ffiffiffiffiffi
(cid:4) þ (cid:4) þ (cid:4)
0:109lb=fth
¼ ffiffiffiffiffi ffiffiffiffiffi ffiffiffiffiffi
Copyright © 2003 Marcel Dekker, Inc.

8.61
Q:
How do gas analysis and pressure affect heat transfer performance?
A:
The presence of gases such as hydrogen and water vapor increases the heat
transfercoefficientsignificantly,whichcanaffecttheheatfluxandtheboilersize.
Also,ifthegasisathighpressure,say100psi or more, themass velocityinside
thetubes(firetubeboilers)oroutsidetheboilertubes(watertubeboilers)canbe
much higher because of the higher density, which also contributes to the higher
heat transfer coefficients. Table 8.44 compares two gas streams, reformed gases
from a hydrogen plant and flue gases from combustion of natural gas.
Factors C and F used in the estimation of heat transfer coefficients inside
andoutsidethetubesarealsogiveninTable8.44.Itcanbeseenthattheeffectof
gasanalysisisverysignificant.Evenatlowgaspressuresofreformedgases(50–
100psig),thefactorsCandF wouldbeveryclosetothevaluesshown,within2–
5%.
8.62
Q:
How does gas pressure affect the heat transfer coefficient?
TABLE8.44 Effect of GasAnalysison HeatTransfer
Reformedgas Fluegas
CO ,vol% 5.0 17.45
2
H O, vol% 38.0 18.76
2
N , vol% — 62.27
2
O , vol% — 1.52
2
CO,vol% 9.0 —
H , vol% 45.0 —
2
CH ,vol% 3.0 —
4
Gas pressure,psia 400 15
Temp, F 1550 675 1540 700
(cid:2)
C ,Btu=lb F 0.686 0.615 0.320 0.286
p (cid:2)
m,lb=ft h 0.087 0.056 0.109 0.070
k,Btu=ft h F 0.109 0.069 0.046 0.028
(cid:2)
Factor Ca 0.571 0.225
Factor Fa 0.352 0.142
aC C =m0:4k0:6; F C0:33k0:67=m0:27.
¼ð p Þ ¼ p
Copyright © 2003 Marcel Dekker, Inc.

A:
TheeffectofgaspressureonfactorsCandF forsomecommongasesisshownin
Figs.8.27and8.28.Itcanbeseenthatthepressureeffectbecomessmallerathigh
gastemperatures,whileatlowtemperaturesthereisasignificantdifference.Also,
the pressure effect is small and can be ignored up to a gas pressure of 200psia.
8.63
Q:
How do we convert gas analysis in percent by weight to percent by volume?
A:
One of the frequent calculations performed by heat transfer engineers is the
conversion from weight tovolume basis and vice versa. The following example
shows how this is done.
Example
A gas contains 3% CO , 6% H O, 74% N , and 17% O by weight. Determine
2 2 2 2
the gas analysis in volume percent.
Solution. Moles of a gas are obtained by dividing the weight by the
molecular weight; moles of CO 3=44 0.06818.
2¼ ¼
Thevolumeofeachgas,then,isthemolefraction 100.Percentvolumeof
(cid:4)
O (0.5312=3.57563) 100 14.86, and so on. One can work in reverse and
2¼ (cid:4) ¼
convert from volume (or mole) basis to weight basis.
Gas W% MW Moles Vol%
CO 3 44 0.06818 1.91
2
H O 6 18 0.3333 9.32
2
N 74 28 2.6429 73.91
2
O 17 32 0.5312 14.86
2
Total 3.57563 100
8.64
Q:
Whatistheeffectofgaspressureandgasanalysisondesignofafiretubewaste
heat boiler? Compare the following two cases. In case 1, reformed gas in a
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 8.27 Effect of gas pressure on heat transfer—flow inside tubes. (From
Ref. 1.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE8.28 Effectofgaspressureonheattransfer—flowoutsidetubes.(From
Ref. 1.)
Copyright © 2003 Marcel Dekker, Inc.

hydrogen plant iscooled in awaste heat boiler, whereasin case 2, fluegas in an
incineration plant is cooled. Maximum allowable heat flux is 100,000Btu=ft2h.
Case1. Reformedgas.Flow 100,000lb=h;gaspressure 300psig;gas
¼ ¼
analysis (vol%):
CO 5;H O 30;N 0:1;H 52;CH 2:9;CO 10.
2 ¼ 2 ¼ 2 ¼ 2 ¼ 4 ¼ ¼
Case 2. Flue gas. Flow 100,000lb=h; gas pressure atmospheric; gas
¼ ¼
analysis (vol%):
CO 7;H O 12;N 75;O 6.
2 ¼ 2 ¼ 2 ¼ 2 ¼
Steam is generated at 500psig using 230 F feedwater. Blowdown 2%. Use
(cid:2)
¼
fouling factors of 0.001 on both gas and steam sides. Tubes are 1.5in. OD and
1.14in. ID. Material is T11 for reformed gas boiler and carbon steel for fluegas
boiler. Saturation temperature is 470 F.
(cid:2)
A:
Calculations were done using the procedure discussed in Q8.10. The results are
presented in Table 8.45. The following points may be noted:
The boiler is much smaller when thegas pressure is higher because of the
high gas density.
The heat transfer coefficient is much higher for the reformed gas owing to
thepresenceofhydrogenandwatervapor.Theheatfluxisalsoveryhigh
compared to that in the flue gas boiler.
TABLE8.45 EffectofGasAnalysisandPressureonDesignof
FireTube Boiler
Item Reformed gas Fluegas
Gas flow,lb=h 100,000 100,000
Gas inlet temp, F 1650 1650
(cid:2)
Gas exittemp, F 650 650
(cid:2)
Gas pressure,psia 315 15
Duty, MMBtu=h 70.00 28.85
Steamgeneration,lb=h 69,310 28,570
Gas pressuredrop, in.WC 9 5
Heatflux, Btu=ft2h 92,200 12,300
Surfacearea, ft2 1566 4266
No.of tubes 350 1300
Length,ft 15 11
Heattransfercoeff, U 87 13.4
Maxgasvelocity, ft=s 68 165
Tube wall temp, F 653 498
(cid:2)
Copyright © 2003 Marcel Dekker, Inc.

TABLE8.46 Composition ofTypical Waste Gases
vol%component
Waste gasa Temp( C) Pressure (psig) N NO H O O SO SO CO CO CH H S H NH HCL
(cid:2) 2 2 2 2 3 2 4 2 2 3
1 300–1000 1 80 10 10
2 250–500 1 81 11 1 7
3 250–850 3–10 66 9 19 6
4 200–1100 1 70 18 3 9
5 300–1100 30–50 0.5 37 6 8 5.5 43
6 200–500 200–450 20 60 20
7 100–600 1 75 7 15 3
8 175–1000 1 72 10 6 12 trace
9 250–1350 1 76 8 4 7 5
10 150–1000 1 73 20 2 5
11 300–1450 1.5 55 23 6 6 3 3 4
a1,Rawsulfurgases;2,SO gasesafterconverter;3,nitrousgases;4,reformerfluegases;5,reformedgas;6,synthesisgas;7,gasturbine
3
exhaust;8,MSWincineratorexhaust;9,chlorinatedplasticsincineration;10,fumeorVOCincineratorexhaust;11,sulfurcondensereffluent.
Copyright © 2003 Marcel Dekker, Inc.

The tubewall temperature is also higher with reformed gas. Hence steam-
side fouling should be low in these boilers.
Itisobviousthatgasanalysisandpressureplayasignificantroleinthedesignof
boilers. Table 8.46 gives the analysis and gas pressure for typical waste gas
streams.
NOMENCLATURE
A Surface area, ft2
A ;A;A;A Fin, total, inside, and obstruction surface areas, ft2=ft
f t i o
A Area of tube wall, ft2=ft
w
B Factor used in Grimson’s correlation
b Fin thickness, in.
C Factor used to estimate heat transfer coefficient
C Specific heat, Btu=lb F; subscripts g;w;m stand for gas, water,
p (cid:2)
and mixture
C –C Factors used in heat transfer and pressure drop calculations for
1 6
finned tubes
D Exchanger diameter, in.
d;d Tube outer and inner diameter, in.
i
e Escalation factor used in life-cycle costing calculations; base of
natural logarithm
E Efficiency of HRSG or fins
f Frequency,Hzorcps;subscriptsa;e;nstandforacoustic,vortex
shedding, and natural
ff Fouling factor, ft2h F=Btu; subscripts i and o stand for inside
(cid:2)
and outside
F Factor used in the estimation of outside heat transfer coefficient
and in the estimation of capitalized costs
G Gas mass velocity, lb=ft2h
h Fin height, in.
h Convective heat transfer coefficient, Btu=ft2h F
c (cid:2)
h;h Heat transfer coefficients inside and outside tubes, Btu=ft2h F
i o (cid:2)
h Heat loss factor, fraction
lf
h Nonluminous heat transfer coefficient, Btu=ft2h F
N (cid:2)
Dh Change in enthalpy, Btu=lb
i Interest rate
k Thermalconductivity,Btu=fth ForBtuin.=ft2h F;subscriptm
(cid:2) (cid:2)
stands for mixture
K Metal thermal conductivity, Btu=fth F
m (cid:2)
K ;K Constants
1 2
Copyright © 2003 Marcel Dekker, Inc.

L Length, ft; thickness of insulation, in.; or beam length
L Equivalent thickness of insulation, in.
e
m Factor used in Eq. (47, 51)
M Water equivalent, Btu= F
c (cid:2)
M Weight of tube, lb=ft
e
MW Molecular weight
n Number of fins per inch
N Constant used in Grimson’s correlation; also number of tubes
Nu Nusselt number
NTU Number of transfer units
P Term used in temperature cross-correction
P ;P Partial pressure of water vapor and carbon dioxide
w c
Pr Prandtl number
Q Energy transferred, Btu=h; heat flux, Btu=ft2h
q Heat flux, heat loss, Btu=ft2h
q Critical heat flux, Btu=ft2h
c
R Thermal resistance, ft2h F=Btu; subscripts i;o, and t stand for
(cid:2)
inside, outside, and total
Re Reynolds number
R Metal thermal resistance, ft2h F=Btu
m (cid:2)
S Fin clearance, in.; Strouhal number; surface area, ft2
S ;S Transverse and longitudinal pitch, in.
T L
t Fluid temperature, F; subscripts a;s;b stand for ambient,
(cid:2)
surface, fin base
t Fin tip temperature, F
f (cid:2)
t Metal temperature, F
m (cid:2)
t Saturation temperature, F
sat (cid:2)
T Absolutetemperature, Kor R;subscriptsg andwstandforgas
(cid:2)
and wall
DT Log-mean temperature difference, F
(cid:2)
U Overall heat transfer coefficient, Btu=ft2h F
(cid:2)
V Fluid velocity, ft=s or ft=min
V Sonic velocity, ft=s
s
W Fluid flow, lb=h; subscripts g;s;w stand for gas, steam, and
water
w Flow per tube, lb=h
x Steam quality, fraction
y Volume fraction of gas
e Effectiveness factor
e ;e ;e Emissivity of CO , water, gas emissivity
c w g 2
De Emissivity correction term
Copyright © 2003 Marcel Dekker, Inc.

Z Fin effectiveness
m Viscosity, lb=fth; subscript m stands for mixture
r gas density, lb=cu ft
l wavelength, ft
n ratio of specific heats
REFERENCES
1. VGanapathy.AppliedHeatTransfer.Tulsa,OK:PennWellBooks,1982.
2. DQKern.ProcessHeatTransfer.NewYork:McGraw-Hill,1950.
3. V Ganapathy. Nomogram determines heat transfer coefficient for water flowing in
pipesortubes.PowerEngineering,July1977,p69.
4. VGanapathy.Chartssimplifyspiralfinnedtubecalculations.ChemicalEngineering.
Apr25,1977,p117.
5. VGanapathy.Estimatenonluminousradiationheattransfercoefficients.Hydrocarbon
Processing,April1981,p235.
6. VGanapathy.Evaluatetheperformanceofwasteheatboilers.ChemicalEngineering,
Nov16,1981,p291.
7. WC Turner, JF Malloy. Thermal Insulation Handbook. New York: McGraw-Hill,
1981,pp40–45.
8. VGanapathy.WasteHeatBoilerDeskbook.Atlanta,GA:FairmontPress,1991.
9. ESCOACorp.ESCOAFintubeManual.Tulsa,OK:ESCOA,1979.
10. VGanapathy.Evaluateextendedsurfacescarefully.HydrocarbonProcessing,October
1990,p65.
11. V Ganapathy. Fouling—the silent heat transfer thief. Hydrocarbon Processing,
October1992,p49.
12. VGanapathy.HRSGtemperatureprofilesguideenergyrecovery.Power,September
1988.
13. W Roshenow, JP Hartnett. Handbook of Heat Transfer. New York: McGraw-Hill,
1972,pp13–56.
Copyright © 2003 Marcel Dekker, Inc.

9
Fans, Pumps, and Steam Turbines
9.01 Determining steam rates in steam turbines; actual and theoretical steam
rates;determiningsteamquantityrequiredtogenerateelectricity;calculat-
ing enthalpy of steam after isentropic and actual expansion
9.02a Cogeneration and its advantages
9.02b Comparison of energy utilization between a cogeneration plant and a
power plant
9.03 Which is the better location for tapping deaeration steam, boiler or
turbine?
9.04 Determining fan power requirements and cost of operation; calculating
BHP (brake horsepower) of fans; actual horsepower consumed if motor
efficiency is known; annual cost of operation of fan
9.05 Effect of elevation and air density on fan performance
9.06a Density of air and selection of fan capacity
9.06b How fan horsepower varies with density for forced draft fans
9.07 Determining power requirements of pumps
9.08 Electric and steam turbine drives for pumps; annual cost of operation
using steam turbine drive; annual cost of operation with motor
9.09a Howspecificgravityofliquidaffectspumpperformance;BHPrequiredat
different temperatures
9.09b How water temperature affects boiler feed pump power requirements
9.10 Effect of speed on pump performance; effect of change in supply
frequency
Copyright © 2003 Marcel Dekker, Inc.

9.11 Effect of viscosity on pump flow, head, and efficiency
9.12 Determining temperature rise of liquids through pumps
9.13 Estimating minimum recirculation flow through pumps
9.14 Net positive suction head (NPSH) and its determination
9.15 Effect of pump suction conditions on NPSH (available NPSH)
a
9.16 Estimating NPSH (required NPSH) for centrifugal pumps
r
9.17 Determining NPSH for reciprocating pumps
a
9.18 Checking performance of pumps from motor readings; relating motor
currentconsumptiontopumpflowandhead;analyzingforpumpproblems
9.19 Checking performance of fan from motor data; relating motor current
consumption to fan flow and head
9.20 Evaluating performance of pumps in series and in parallel
9.21 Parameters affecting Brayton cycle efficiency
9.22 How to improve the efficiency of the Brayton cycle
9.01
Q:
How is the steam rate for steam turbines determined?
A:
The actual steam rate (ASR) for a turbine is given by the equation
3413
ASR 1
¼Z h h ð Þ
t(cid:4)ð 1(cid:3) 2sÞ
where ASR is the actual steam rate in lb=kWh. This is the steam flow in lb=h
requiredtogenerate1kWofelectricity.h isthesteamenthalpyattheinlettothe
1
turbine, Btu=lb, and h is the steam enthalpy at turbine exhaust pressure if the
2s
expansionisassumedtobeisentropic,Btu=lb.Thatis,theentropyisthesameat
inlet condition and at exit.Givenh , h can be obtained either from the Mollier
1 2s
chart or by calculation using steam table data (see the Appendix). Z is the
t
efficiencyoftheturbine,expressedasafraction.Typically,Z rangesfrom0.65to
t
0.80.
AnotherwaytoestimateASRistousepublisheddataonturbinetheoretical
steam rates (TSRs) (see Table 9.1).
3413
TSR 2
¼h h ð Þ
1(cid:3) 2s
TSRdividedbyZ givesASR.Thefollowingexampleshowshowthesteamrate
t
can be used to find required steam flow.
Copyright © 2003 Marcel Dekker, Inc.

TABLE9.1 Theoretical SteamRatesforSteamTurbines atSome CommonConditions (lb=kWh)
Inlet
200psig 400psig 600psig 600psig 850psig,
150psig 200psig 500 F 750 F 750 F 825 F 825 F,
(cid:2) (cid:2) (cid:2) (cid:2) (cid:2)
Exhaust 366 F 388 F 94 F 302 F 261 F 336 F 298 F,
(cid:2) (cid:2) (cid:2) (cid:2) (cid:2) (cid:2) (cid:2)
pressure saturated saturated superheat superheat superheat superheat superheat
2in.Hg 10.52 10.01 9.07 7.37 7.09 6.77 6.58
4in.Hg 11.76 11.12 10.00 7.99 7.65 7.28 7.06
0psig 19.37 17.51 15.16 11.20 10.40 9.82 9.31
10psig 23.96 21.09 17.90 12.72 11.64 10.96 10.29
30psig 33.6 28.05 22.94 15.23 13.62 12.75 11.80
50psig 46.0 36.0 28.20 17.57 15.36 14.31 13.07
60psig 53.9 40.4 31.10 18.75 16.19 15.05 13.66
70psig 63.5 45.6 34.1 19.96 17.00 15.79 14.22
75psig 69.3 48.5 35.8 20.59 17.40 16.17 14.50
Source:Ref.4.
Copyright © 2003 Marcel Dekker, Inc.

Example
Howmanylb=hofsuperheatedsteamat1000psia,900 F,isrequiredtogenerate
(cid:2)
7500kW in a steam turbine if the backpressure is 200psia and the overall
efficiency of the turbine generator system is 70%?
Solution. From the steam tables, at 1000psia, 900 F, h 1448.2Btu=lb
(cid:2) 1¼
and entropy s 1.6121Btu=lb F. At 200psia, corresponding to the same
1¼ (cid:2)
entropy, we must calculate h by interpolation. We can note that steam is in
2s
superheated condition. h 1257.7Btu=lb. Then
2s¼
3413
ASR 25:6lb=kWh
¼0:70 1448 1257:7 ¼
(cid:4)ð (cid:3) Þ
Hence, to generate 7500kW, the steam flow required is
W 25:6 7500 192;000lb=h
s ¼ (cid:4) ¼
9.02a
Q:
What is cogeneration? How does it improve the efficiency of the plant?
A:
Cogeneration is the term used for simultaneous generation of power and process
steam from a single full source, as in a system of gas turbine and process waste
heat boiler, wherein thegas turbine generates electricity and the boiler generates
steam for process (see Fig. 9.1).
In a typical power plant that operates at 35–43% overall efficiency, the
steam pressure inthe condenser isabout 2–4in.Hg. A lot of energyiswasted in
the cooling water, which condenses the steam in the condenser.
If, instead, the steam is generated at a high pressure and expanded in a
steamturbinetotheprocesssteampressure,wecanusethesteamforprocess,and
electricityisalsogenerated.Afullcreditfortheprocesssteamcanbegivenifthe
steam is used—hence the improvement in overall energy utilization. Q9.02b
explains this in detail.
9.02b
Q:
50,000lb=hofsuperheatedsteamat1000psiaand900 Fisavailableinaprocess
(cid:2)
plant.Onealternativeistoexpandthisisasteam turbineto200psia andusethe
200psia steam for process (cogeneration). Another alternative is to expand the
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 9.1 Cogeneration produces power and steam from the same fuel
source by converting the turbine exhaust heat in a boiler, which produces steam
forprocess.
superheated steam in a steam turbine to 1psia, generating electricity alone in a
power plant. Evaluate each scheme.
A:
Scheme 1. The steam conditions are as in Q9.01, so let us use the data on
enthalpy.Assumethattheturbineefficiencyis70%.Theelectricityproducedcan
be written as follows using Eq. (1):
h h
P W Z 1(cid:3) 2s 3
¼ s t(cid:4) 3413 ð Þ
P is in kilowatts. h 1448Btu=lb and h 1257.7Btu=lb, from Q 9.01.
1¼ 2s¼
Substituting into Eq. (3), we have
0:70
P 50;000 1448 1257:7 1954kW
¼ (cid:4)ð (cid:3) Þ(cid:4)3413¼
Now let us calculate the final enthalpy at condition 2, h . Using the equation
2
Z h h h h 4
tð 1(cid:3) 2sÞ¼ 1(cid:3) 2 ð Þ
we obtain
0:70 1448 1257:7 1448 h
(cid:4)ð (cid:3) Þ¼ (cid:3) 2
Copyright © 2003 Marcel Dekker, Inc.

or
h 1315Btu=lb
2 ¼
This enthalpy is available for process in the cogeneration mode. The energy Q
availableinthecogenerationmodeisthesumoftheelectricity producedandthe
energy to process, all in Btu=h. Hence the total energy is
Q 1954 3413 50;000 1315 72:4 106 Btu=h
¼ (cid:4) þ (cid:4) ¼ (cid:4)
Scheme 2. Let us take the case when electricity alone is generated. Let us
calculate the final steam conditions at a pressure of 1psia. s 1.6121 s . At
1¼ ¼ 2s
1psia, from the steam tables, at saturated conditions, s 0.1326 and
f ¼
s 1.9782. s and s are entropies of saturated liquid and vapor. Since the
g¼ f g
entropy s isin between s and s , thesteam atisentropic conditions iswet. Let
2s f g
us estimate the quality x. From basics,
0:1326 1 x 1:9782x 1:6121
ð (cid:3) Þþ ¼
Hence
x 0:80
¼
The enthalpy corresponding to this condition is
h 1 x h xh
¼ð (cid:3) Þ f þ g
or
h 0:80 1106 0:2 70 900Btu=lb
2s ¼ (cid:4) þ (cid:4) ¼
(h and h are 70 and 1106 at 1psia.) Using a turbine efficiency of 75%, from
f g
Eq. (3) we have
0:75
P 50;000 1448 900 6023kW
¼ (cid:4)ð (cid:3) Þ(cid:4)3413¼
20:55 106 Btu=h
¼ (cid:4)
Hencewenotethatthereisalotofdifferencebetweentheenergypatternsofthe
twocases,withthecogenerationschemeusingmuchmoreenergythanthatused
in Scheme 2.
Even ifthesteam inScheme1were usedfor oilheating, thelatent heatof
834Btu=lb at 200psia could be used.
Total output 1954 3413 50;000 834
¼ (cid:4) þ (cid:4)
48:3 106 Btu=h
¼ (cid:4)
This is still more than the output in the case of power generation alone.
Note, however, that if the plant electricity requirement were more than
2000kW,Scheme1shouldhavemoresteamavailable,whichmeansthatabigger
boiler shouldbeavailable.Evaluationofcapitalinvestmentisnecessarybeforea
Copyright © 2003 Marcel Dekker, Inc.

particular scheme is chosen. However, it is clear that in cogeneration the
utilization of energy is better.
9.03
Q:
Whichisabetterlocationfortappingsteamfordeaerationinacogenerationplant
with an extraction turbine, the HRSG or the steam turbine?
A:
When steam is taken for deaeration from the HRSG and not from an extraction
pointinasteamturbine,thereisanetlosstothesystempoweroutputbecausethe
steamisthrottledandnotexpandedtothelowerdeaerator pressure.Throttlingis
a mere waste of energy, whereas steam generates power while it expands to a
lower pressure. To illustrate, consider the following example.
Example
An HRSG generates 80,000lb=h of steam at 620psig and 650 F from
(cid:2)
550,000lb=h of turbine exhaust gases at 975 F. The steam is expanded in an
(cid:2)
extraction-condensing steam turbine. Figure 9.2 shows the two schemes. The
FIGURE 9.2 Optionsfortaking steam fordeaeration.
Copyright © 2003 Marcel Dekker, Inc.

condenser operates at 2.5in.Hg abs. The deaerator is at 10psig. Blowdown
losses 2%.Neglectingflashsteamandventflow,wecanshowthatwhensteam
¼
is taken for deaeration from the HRSG,
81;700 208 1700 28 80;000 X 76 1319X
(cid:4) ¼ (cid:4) þð (cid:3) Þ(cid:4) þ
where208,28,76,and1319areenthalpies offeedwaterat240 F,makeupwater
(cid:2)
at 60 F, condensate at 108 F, and steam at 620psig, 650 F.
(cid:2) (cid:2) (cid:2)
The deaeration steam X 8741lb=h; use 8785 to account for losses. Now
¼
compute the actual steam rate (ASR) in the steam turbine (see Q9.01). It can be
shown that ASR 11.14lb=kWh at 70% expansion efficiency; hence power
¼
output of the turbine generator 0.96 (80,00078785)=11.14 6137kW,
¼ (cid:4) ¼
assuming 4% loss in the generator.
Similarly, when steam is taken at 30psia from the extraction point in the
steam turbine, the enthalpy of steam for deaeration is 1140.6Btu=lb. An energy
balance around the deaerator shows
81;700 208 1140:6X 80;000 X 76 1700 28
(cid:4) ¼ þð (cid:3) Þ(cid:4) þ (cid:4)
Hence X 10,250lb=h. Then ASR for expansion from 620psig to
¼
30psia 19lb=kWh and 11.14 for the remaining flow. The power output is
¼
10;250 80;000 10;250
P 0:96 (cid:3) 6528kW
¼ (cid:4) 19 þ 11:14 ¼
(cid:1) (cid:2)
Thus a significant difference in power output can be seen. However, one has to
review the cost of extraction machine versus the straight condensing type and
associated piping, valves, etc.
9.04
Q:
Afandevelopsan18in.WCstaticheadwhentheflowis18,000acfmandstatic
efficiency of the fan is 75%. Determine the brake horsepower required, the
horsepower consumed when the motor has an efficiencyof 90%, and the annual
cost of operation if electricity costs 5cents=kWh and the annual period of
operation is 7500h.
A:
The power required when the flow is q acfm and the head is H in. WC is
w
H
BHP q w 5
¼ 6356Z ð Þ
f
where Z is the efficiency of the fan, fraction; in this case, Z 0.75.
f f ¼
Copyright © 2003 Marcel Dekker, Inc.

The horsepower consumed is
BHP
HP 6
¼ Z ð Þ
m
where Z is the motor efficiency, fraction. Substituting the data, we have
m
18
BHP 18;000 68hp
¼ (cid:4)0:75 6356¼
(cid:4)
and
68
HP 76hp
¼0:9¼
The annual cost of operation will be
76 0:74 0:05 7500 $21;261
(cid:4) (cid:4) (cid:4) ¼
(0.74 is the conversion factor from hp to kW.)
9.05
Q:
A fan develops18,000acfm at 18in. WC when the ambient conditions are 80 F
(cid:2)
andtheelevationis1000ft(case1).Whataretheflowandtheheaddevelopedby
the fan when the temperature is 60 Fand the elevation is 5000ft (case 2)?
(cid:2)
A:
The head developed by a fan would vary with density as follows:
H H
w1 w2 7
r ¼ r ð Þ
1 2
where r is the density, lb=cu ft, and the subscripts 1 and 2 refer to any two
ambient conditions.
Theflowqinacfmdevelopedbyafanwouldremainthesamefordifferent
ambientconditions;however,theflowinlb=hwouldvaryasthedensitychanges.
Let us use Table 9.2 for quick estimation of density as a function of
elevation and temperature. r 0.075=factor from Table9.2. At 80 Fand 1000ft
(cid:2)
¼
elevation,
0:075
r 0:0707lb=cuft
1 ¼ 1:06 ¼
At 60 Fand 5000ft,
(cid:2)
0:075
r 0:0636lb=cuft
2 ¼ 1:18 ¼
Copyright © 2003 Marcel Dekker, Inc.

TABLE9.2 Temperatureand Elevation Factors
Altitude (ft)andbarometric pressure(in.Hg)
0 500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000
Temp.( F) (29.92) (29.38) (28.86) (28.33) (27.82) (27.31) (26.82) (26.32) (25.84) (25.36) (24.90) (24.43) (23.96)
(cid:2)
40 .79 .81 .82 .84 .85 .87 .88 .90 .92 .93 .95 .97 .99
(cid:3)
0 .87 .88 .90 .92 .93 .95 .97 .99 1.00 1.02 1.04 1.06 1.08
40 .94 .96 .98 1.00 1.01 1.03 1.05 1.07 1.09 1.11 1.13 1.16 1.18
70 1.00 1.02 1.04 1.06 1.08 1.10 1.12 1.14 1.16 1.18 1.20 1.22 1.25
80 1.02 1.04 1.06 1.08 1.10 1.12 1.14 1.16 1.18 1.20 1.22 1.25 1.27
100 1.06 1.08 1.10 1.12 1.14 1.16 1.18 1.20 1.22 1.25 1.27 1.29 1.32
120 1.09 1.11 1.13 1.16 1.18 1.20 1.22 1.24 1.27 1.29 1.31 1.34 1.37
140 1.13 1.15 1.17 1.20 1.22 1.24 1.26 1.29 1.31 1.34 1.36 1.39 1.41
160 1.17 1.19 1.21 1.24 1.26 1.28 1.31 1.33 1.35 1.38 1.41 1.43 1.46
180 1.21 1.23 1.25 1.28 1.30 1.32 1.35 1.37 1.40 1.42 1.45 1.48 1.51
200 1.25 1.27 1.29 1.32 1.34 1.36 1.39 1.42 1.44 1.47 1.50 1.53 1.55
250 1.34 1.36 1.39 1.41 1.44 1.47 1.49 1.52 1.55 1.58 1.61 1.64 1.67
300 1.43 1.46 1.49 1.51 1.54 1.57 1.60 1.63 1.66 1.69 1.72 1.76 1.79
350 1.53 1.56 1.58 1.61 1.64 1.67 1.70 1.74 1.77 1.80 1.84 1.87 1.91
400 1.62 1.65 1.68 1.71 1.75 1.78 1.81 1.84 1.88 1.91 1.95 1.99 2.02
450 1.72 1.75 1.78 1.81 1.85 1.88 1.92 1.95 1.99 2.03 2.06 2.10 2.14
500 1.81 1.84 1.88 1.91 1.95 1.98 2.02 2.06 2.10 2.14 2.18 2.22 2.26
550 1.91 1.94 1.98 2.01 2.05 2.09 2.13 2.17 2.21 2.25 2.29 2.33 2.38
600 2.00 2.04 2.07 2.11 2.15 2.19 2.23 2.27 2.32 2.36 2.40 2.45 2.50
650 2.09 2.13 2.17 2.21 2.25 2.29 2.34 2.38 2.43 2.47 2.52 2.56 2.61
700 2.19 2.23 2.27 2.31 2.35 2.40 2.44 2.49 2.53 2.58 2.63 2.68 2.73
750 2.28 2.32 2.37 2.41 2.46 2.50 2.55 2.60 2.64 2.69 2.74 2.80 2.85
800 2.38 2.42 2.46 2.51 2.56 2.60 2.65 2.70 2.75 2.80 2.86 2.91 2.97
850 2.47 2.52 2.56 2.61 2.66 2.71 2.76 2.81 2.86 2.92 2.97 3.03 3.08
900 2.57 2.61 2.66 2.71 2.76 2.81 2.86 2.92 2.97 3.03 3.08 3.14 3.20
950 2.66 2.71 2.76 2.81 2.86 2.91 2.97 3.02 3.08 3.14 3.20 3.26 3.32
1000 2.76 2.81 2.86 2.91 2.96 3.02 3.07 3.13 3.19 3.25 3.31 3.37 3.44
Copyright © 2003 Marcel Dekker, Inc.

Substitution into Eq. (7) yields
18 H
w2
0:0707¼0:0636
H 16:1in. WC
w2 ¼
In case 1 flow will be
18;000 0:0707 60 76;356lb=h
(cid:4) (cid:4) ¼
and in case 2 the flow will be
18;000 0:0636 60 68;638lb=h
(cid:4) (cid:4) ¼
Theexactoperatingpointofthefancanbeobtainedafter plottingthenew
H versus q characteristic and noting the point of intersection of the new curve
w
with the system resistance curve.
9.06a
Q:
Whyshouldthecapacityofforceddraftfansforboilersbereviewedatthelowest
density condition?
A:
For the same heat input to boilers, the air quantity required in mass flow units
(lb=h) remains the same irrespective of the ambient conditions.
W 60rq
¼
where
W massflow; lb=h
¼
r density; lb=cuft
¼
q volumetricflow; acfm
¼
Fans dischargeconstant volumetric flowat any density. Hence if the fan is sized
to give a particular volumetric flow at the high density condition, the mass flow
would decrease when density decreases as can be seen in the equation above.
Hence the fan must be sized to deliver thevolumetric flowat the lowest density
condition, in which case the output in lb=h will be higher at the higher density
condition, which can be then controlled.
Also, the gas pressure drop DP in in. WC across the wind-box is
proportional to W2=r. If the air density decreases as at high temperature
conditions, the pressure drop increases, because W remains unchanged for a
given heat input. Considering the fact that H=r is a constant for a given fan,
Copyright © 2003 Marcel Dekker, Inc.

where H is the static head in in. WC, using the lowest r ensures that the head
available at higher density will be larger.
9.06b
Q:
Howdoesthehorsepowerofaforceddraftfanforboilersorheaterschangewith
density?
A:
Equation (5) gives the fan horsepower:
qH
BHP w
¼6356Z
f
Using the relation W 60qr, we can rewrite the above as
¼
WH
BHP w
¼381;360rZ
f
For a boiler at a given duty, the air flow in lb=h and the head in in. WC, H ,
w
remainunchanged;henceasthedensitydecreases,thehorsepowerincreases.This
is yet another reason to check the fan power at the lowest density condition.
However, if the application involves an uncontrolled fan that delivers a given
volume of air at all densities, then the horsepower should be evaluated at the
highest density case because the mass flow would be higher as well as the gas
pressure drop.
9.07
Q:
Atriplexreciprocatingpumpisusedforpumping40gpm(gallonsperminute)of
water at 100 F. The suction pressure is 4psig and the discharge pressure is
(cid:2)
1000psig. Determine the BHP required.
A:
Use the expression
DP
BHP q 8
¼ (cid:4)1715Z ð Þ
p
Copyright © 2003 Marcel Dekker, Inc.

where
q flow; gpm
¼
DP differentialpressure; psi
¼
Z pumpefficiency; fraction
p ¼
In the absence of data on pumps, use 0.9 for triplex and 0.92 for quintuplex
pumps.
1000 4
BHP 40 (cid:3) 25:8hp
¼ (cid:4)1715 0:90¼
(cid:4)
A 30hp motor can be used.
Thesameexpressioncanbeusedforcentrifugalpumps.Theefficiencycan
be obtained from the pump characteristic curve at the desired operating point.
9.08
Q:
A pump is required to develop 230gpm of water at 60 Fat a head of 970ft. Its
(cid:2)
efficiencyis 70%. There are two options for the drive:an electric motor with an
efficiencyof 90% or a steam turbine drivewith a mechanical efficiencyof 95%.
Assume that the exhaust is used for process and not wasted.
If electricity costs 50mills=kWh, steam for the turbine is generated in a
boilerwithanefficiencyof85%(HHVbasis),andfuelcosts$3=MMBtu(HHV
basis), determine the annual cost of operation of each drive if the plant operates
for 6000h=year.
A:
Another form of Eq. (8) is
H
BHP W 9
¼ (cid:4)1;980;000Z ð Þ
p
where
W flow; lb=h
¼
H headdevelopedbythepump; ftof liquid
¼
For relating head in ft with differential pressure in psi or flow in lb=h with gpm,
refer to Q5.01. Substituting into Eq. (9) and assuming that s 1, W 230
¼ ¼
500lb=h,
(cid:4)
970
BHP 230 500 81hp
¼ (cid:4) (cid:4)0:70 1;980;000¼
(cid:4)
Copyright © 2003 Marcel Dekker, Inc.

The annual cost of operation with an electric motor drive will be
6000
81 0:746 0:05 $20;142
(cid:4) (cid:4) (cid:4) 0:90 ¼
(0.746 is the conversion factor from hp to kW.)
If steam is used, the annual cost of operation will be
3
81 2545 6000 $4595
(cid:4) (cid:4) (cid:4)0:85 0:90 106 ¼
(cid:4) (cid:4)
(2545Btu=h 1hp; 0.85 is the boiler efficiency; 0.95 is the mechanical effi-
¼
ciency.) Hence the savings in cost of operation is 20,14274545
¼
$15,547=year.
Dependingonthedifferenceininvestmentbetweenthetwodrives,payback
canbeworkedout.Inthecalculationaboveitwasassumedthatthebackpressure
steamwasusedforprocess.If itwaswasted,theeconomicsmaynotworkoutthe
same way.
9.09a
Q:
How does the specific gravity or density of liquid pumped affect the BHP, flow,
and head developed?
A:
Apumpalwaysdeliversthesameflowingpm(assumingthatviscosityeffectscan
be neglected) and head in feet of liquid at any temperature. However, due to
changes in density, the flow in lb=h, pressure in psi, and BHP would change. A
variation of Eq. (9) is
qDP W DP
BHP 10
¼1715Z ¼857;000Z s ð Þ
p p
where
q liquidflow; gpm
¼
W liquidflow; lb=h
¼
s specificgravity
¼
DP pressuredeveloped; psi
¼
H headdeveloped; ftof liquid
¼
Also,
DP
H 2:31 11
¼ s ð Þ
Copyright © 2003 Marcel Dekker, Inc.

Example
Ifapumpcandevelop1000gpmofwaterat40 Fthrough1000ft,whatflowand
(cid:2)
head can it developwhen thewater isat 120 F? Assume that pump efficiencyis
(cid:2)
75% in both cases.
Solution. s at 40 F is 1 (from the steam tables; see the Appendix). s at
1 (cid:2) 2
120 F is 0.988.
(cid:2)
1
DP 1000 433psi
1 ¼ (cid:4)2:31¼
From Eq. (11),
433
BHP 1000 337hp
1 ¼ (cid:4)0:75 1715¼
(cid:4)
W 500q s 500 1000 1 500;000lb=h
1 ¼ 1 1 ¼ (cid:4) (cid:4) ¼
At 120 F,
(cid:2)
0:988
DP 1000 427psi
2 ¼ (cid:4) 2:31 ¼
427
BHP 1000 332hp
2 ¼ (cid:4)0:75 1715¼
(cid:4)
W 500 0:988 1000 494;000lb=h
2 ¼ (cid:4) (cid:4) ¼
If the same W is to be maintained, BHP must increase.
9.09b
Q:
How does the temperature of water affect pump power consumption?
A:
Theanswercanbeobtainedbyanalyzingthefollowingequationsforpumppower
consumption. One is based on flow in gpm and the other in lb=h.
QHs
BHP 12
¼3960Z ð Þ
p
where
Q flow; gpm
¼
H head; ftof water
¼
s specificgravity
¼
Z efficiency
p ¼
Copyright © 2003 Marcel Dekker, Inc.

Inboilers,onewouldliketomaintainaconstantflowinlb=h,notingpm,andata
particular pressure in psi. The relationships are
W DP
Q and H 2:31
¼500s ¼ (cid:4) s
where
W flow; lb=h
¼
DP pumpdifferential; psi
¼
Substituting these terms into (1), we have
DP
BHP W 13
¼ 857;000Z s ð Þ
p
As s decreases with temperature, BHP will increase if we want to maintain the
flowinlb=handheadorpressureinpsi.However,iftheflowingpmandheadin
ftshouldbemaintained,thentheBHPwilldecreasewithadecreaseins,whichin
turn is lower at lower temperatures.
Asimilaranalogycan bedrawnwith fans inboiler plants, whichrequirea
certain amount of air in lb=h for combustion and a particular head in in. WC.
9.10
Q:
Acentrifugalpumpdelivers100gpmat155ftofwaterwitha60Hzsupply.Ifthe
electric supply is changed to 50Hz, how will the pump perform?
A:
For variations in speed or impeller size, the following equation applies:
q N pH
1 1 1 14
q ¼N ¼pH ð Þ
2 2 ffiffiffiffi2ffiffi
where ffiffiffiffiffiffi
q pumpflow; gpm
¼
H headdeveloped; ft
¼
N speed; rpm
¼
Use of Eq. (14) gives us the head and the flow characteristics of a pump at
different speeds. However, to get the actual operating point, one must plot the
Copyright © 2003 Marcel Dekker, Inc.

newhead versus flow curve and note the point of intersection of this curvewith
the system resistance curve. In the case above,
50
q 100 83gpm
2 ¼ (cid:4)60¼
50 2
H 155 107ft
2 ¼ (cid:4) 60 ¼
(cid:1) (cid:2)
In this fashion, the new H versus q curve can be obtained. The new operating
point can then be found.
9.11
Q:
How does the performance of a pump change with the viscosity of the fluids
pumped?
A:
TheHydraulicInstitutehaspublishedchartsthatgivecorrectionfactorsforhead,
flow,andefficiencyforviscousfluidswhentheperformancewithwaterisknown
(see Figs. 9.3a and 9.3b).
Example
A pump delivers 750gpm at 100ft head when water is pumped. What is the
performancewhenitpumpsoilwithviscosity1000SSU?Assumethatefficiency
with water is 82%.
Solution. InFig.9.3b,goupfromcapacity750gpmtocuttheheadlineat
100ft and move horizontally to cut viscosity at 1000SSU; move up to cut the
various correction factors.
C 0:94; C 0:92; C 0:64
Q ¼ H ¼ E ¼
Hence the new data are
q 0:94 750 705gpm
¼ (cid:4) ¼
H 0:92 100 92ft
¼ (cid:4) ¼
Z 0:64 92 52%
p ¼ (cid:4) ¼
The new H versus q data can be plotted for various flows to obtain the
characteristic curve. The operating point can be obtained by noting the point of
intersection of the system resistance curve with the H versus q curve. C , C ,
Q H
and C are correction factors for flow, head, and efficiency.
E
Copyright © 2003 Marcel Dekker, Inc.

FIGURE9.3a Viscositycorrections.(CourtesyofHydraulicInstitute=GouldPump
Manual.)
Copyright © 2003 Marcel Dekker, Inc.

FIGURE 9.3b Determination of pump performance when handling viscous
liquids. (Courtesyof HydraulicInstitute=Gould Pump Manual.)
Copyright © 2003 Marcel Dekker, Inc.

9.12
Q:
Whatisthetemperatureriseofwaterwhenapumpdelivers100gpmat1000ftat
an efficiency of 60%?
A:
The temperature rise of fluids through the pump is an important factor in pump
maintenanceandperformanceconsiderationsandmustbelimited.Therecircula-
tion valve is used to ensure that the desired flow goes through the pump at low
load conditions of the plant, thus cooling it.
Fromenergybalance,thefrictionlossesareequatedtotheenergyabsorbed
by the fluid.
2545
DT BHP theoretical power 15a
¼ð (cid:3) Þ(cid:4)WC ð Þ
p
where
DT temperatureriseof thefluid; F
(cid:2)
¼
BHP brakehorsepower
¼
W flowof thefluid; lb=h
¼
C specificheatof thefluid; Btu=lb F
p ¼ (cid:2)
For water, C 1.
p¼
From Eq. (9),
H
BHP W
¼ (cid:4)Z 3600 550
p(cid:4) (cid:4)
whereZ isthepumpefficiency,fraction.SubstitutingintoEqs.(15a)and(9)and
r
simplifying, we have
1=Z 1
DT H p(cid:3) 15b
¼ (cid:4) 778 ð Þ
If H 100ft of water and Z 0.6, then
¼ r¼
1:66 1
DT 1000 (cid:3) 1 (cid:2) F
¼ (cid:4) 778 (cid:10)
9.13
Q:
How is the minimum recirculation flow through a centrifugal pump determined?
Copyright © 2003 Marcel Dekker, Inc.

A:
Letusillustratethiswiththecaseofapumpwhosecharacteristicsareasshownin
Fig. 9.4. We need to plot the DT versus Q characteristics first. Note that at low
flows when the efficiency is low, we can expect a large temperature rise. At
100gpm, for example,
Z 0:23 and H 2150ft
p ¼ ¼
Then
1=0:23 1
DT 2150 (cid:3) 9 (cid:2) F
¼ (cid:4) 778 ¼
In a similar fashion, DT is estimated at various flows. Note that DT is higher at
low flows owing to the low efficiency and also because of the lesser cooling
capacity.
Themaximumtemperatureriseisgenerallylimitedtoabout20 F,depend-
(cid:2)
ing on the recommendations of the pump manufacturer. This means that at least
40gpm must be circulated through the pump in this case. If the load is only
30gpm, then depending on the recirculation control logic, 10–70gpm could be
recirculated through the pump.
FIGURE 9.4 Typical characteristic curve of a multistage pump also showing
temperature riseversuscapacity.
Copyright © 2003 Marcel Dekker, Inc.

9.14
Q:
What is net positive suction head (NPSH), and how is it calculated?
A:
The NPSH is the net positive suction head in feet absolute determined at the
pump suction after accounting for suction piping losses (friction) and vapor
pressure.NPSH helps one to check ifthere isa possibilityof cavitation at pump
suction. This is likely when the liquid vaporizes or flashes due to low local
pressure and collapses at the pump as soon as the pressure increases. NPSH
determined from pump layout in this manner is NPSH (NPSH available). This
a
will vary depending on pump location as shown in Fig. 9.5.
FIGURE9.5 CalculationofsystemNPSHavailablefortypicalsuctionconditions.
Copyright © 2003 Marcel Dekker, Inc.

NPSH (NPSH required) is the positive head in feet absolute required to
r
overcomethepressuredropduetofluidflowfromthepumpsuctiontotheeyeof
theimpellerandmaintaintheliquidaboveitsvapor pressure.NPSH varieswith
r
pump speed and capacity. Pump suppliers generally provide this information.
NPSH can be determined by a gauge reading at pump suction:
a
NPSH P VP PG VH 16
a ¼ B(cid:3) (cid:8) þ ð Þ
where
VH velocityheadatthegaugeconnection; ft
¼
PG pressuregaugereading; convertedtoft
¼
VP vapor pressure; ftabsolute
¼
P barometricpressure; ft if suctionisatmospheric
B ¼ ð Þ
To avoid cavitation, NPSH must be greater than NPSH .
a r
9.15
Q:
Does the pump suction pressure change NPSH ?
a
A:
NPSH is given by
a
NPSH P H VP H 17
a ¼ sþ (cid:3) (cid:3) f ð Þ
where
P suctionpressure; ftof liquid
s ¼
H headof liquid; ft
¼
VP vapor pressureof theliquidatoperatingtemperature; ft
¼
H frictionlossinthesuctionline; ft
f ¼
For saturated liquids, VP P , so changes in suction pressure do not
(cid:10) s
significantly change NPSH .
a
Example
Determine the NPSH for the system shown in Fig. 9.5b when H 10ft,
a ¼
H 3ft, and VP 0.4psia (from the steam tables). Assume that the water has
f ¼ ¼
a density of 62lb=cu ft.
Copyright © 2003 Marcel Dekker, Inc.

Solution.
144
VP 0:4 0:93ft
¼ (cid:4) 62 ¼
166
Suction presssure 14:6psia 14:6 33:9ft
¼ ¼ (cid:4) 62 ¼
NPSH 33:9 3 0:93 10 40ft
a ¼ (cid:3) (cid:3) þ ¼
9.16
Q:
In the absence of information from the pump supplier, can we estimate NPSH ?
r
A:
AgoodestimateofNPSH canbemadefromtheexpressionforspecificspeedS.
r
pq
S N 18
¼ (cid:4)NPSH0:75 ð Þ
ffiffiffir
S ranges from 7000 to 12,000 for water.
Forexample,whenq 100gpm, N 1770, andassumingthat S 10,000
¼ ¼ ¼
for water,
1:33
p100
NPSH 1770 2:2ft
r ¼ (cid:4) 10;000 ¼
(cid:1) ffiffiffiffiffiffiffiffi(cid:2)
Even if we took a conservative value of 7000 for S, we would get
NPSH 3:43ft
r ¼
This information can be used in making preliminary layouts for systems
involving pumps.
9.17
Q:
How is NPSH for a reciprocating pump arrived at?
a
A:
NPSH forareciprocatingpumpiscalculatedinthesamewayasforacentrifugal
a
pump except that the acceleration head H is included with the friction losses.
a
Thisistheheadrequiredtoacceleratetheliquidcolumnoneachsuctionstrokeso
Copyright © 2003 Marcel Dekker, Inc.

that therewill beno separationofthis columninthepump suctionline orinthe
pump [1]:
LNVC
H 19
a ¼ K ð Þ
g
where
L lengthof thesuctionline; ft actuallength; notdeveloped
¼ ð Þ
V velocityinthesuctionline; ft=s
¼
N pumpspeed; rpm
¼
C is a constant: 0.066 for triplex pump, 0.04 for quintuplex, and 0.2 for duplex
pumps.K isafactor:2.5forhotoil,2.0formosthydrocarbons,1.5forwater,and
1.4 for deaerated water. g 32ft=s2. Pulsation dampeners are used to reduce L
¼
significantly. By proper selection, L can be reduced to nearly zero.
Example
Atriplexpumprunningat360rpmanddisplacing36gpmhasa3in.suctionline
8ft long and a 2in. line 18ft long. Estimate the acceleration head required.
Solution. First obtainthevelocityofwater ineachpartoftheline.Inthe
3in. line, which has an inner diameter of 3.068in.,
q 36
V 0:41 0:41 1:57ft=s
¼ d2 ¼ (cid:4) 3:068 2 ¼
i
ð Þ
In the 2in. line, which has an inner diameter of 2.067in.,
36
V 0:41 3:45ft=s
¼ (cid:4) 2:067 2 ¼
ð Þ
The acceleration head in the 3in. line is
0:066
H 8 360 1:57 6:7ft
a ¼ (cid:4) (cid:4) (cid:4)1:4 32¼
(cid:4)
In the 2in. line,
0:066
H 18 3:45 360 32:9ft
a ¼ (cid:4) (cid:4) (cid:4)1:4 32¼
(cid:4)
The total acceleration head is 32.9 6.7 39.6ft.
þ ¼
9.18
Q:
How can we check the performance of a pump from the motor data?
Copyright © 2003 Marcel Dekker, Inc.

A:
A good estimate of the efficiency of a pump or a fan can be obtained from the
current reading if we make a few reasonable assumptions. The efficiency of a
motor is more predictable than that of a pump owing to its small variations with
duty. The pump differential pressure and flow can be obtained rather easily and
accurately. By relating the power consumed by the pump with that delivered by
themotor,thefollowingcanbederived.Thepumppowerconsumption,P,inkW
from Eq. (8) is
DP
P 0:00043q 20
¼ (cid:4) Z ð Þ
p
Motor power output 0:001732EI cosfZ 21
¼ m ð Þ
Equating Eqs. (20) and (21) and simplifying, we have
qDP 4EI cosfZ Z 22
¼ p m ð Þ
where
q flow; gpm
¼
DP differentialpressure; psi
¼
E voltage; V
¼
I current; A
¼
Z ; Z efficiencyof pumpandmotor; fraction
p m ¼
cosf powerfactor
¼
From Eq. (22) we can solve for pump efficiency given the other variables.
Alternatively, we can solve for the flow by making a reasonable estimate of Z
p
and check whether the flow reading is good. The power factor cosf typically
varies between 0.8 and 0.9, and the motor efficiency between 0.90 and 0.95.
Example
Aplantengineerobservesthatata90gpmflowofwaterand1000psidifferential,
themotorcurrentis100A.Assumingthatthevoltageis460V,thepowerfactoris
0.85, and the motor efficiency is 0.90, estimate the pump efficiency.
Solution. Substituting the data into Eq. (22), we obtain
90 1000 4 460 100 0:85 0:90 Z
(cid:4) ¼ (cid:4) (cid:4) (cid:4) (cid:4) (cid:4) p
Solving for Z , we have Z 0.65.
p p¼
We can use this figure to check whether something is wrong with the
system. For instance, if the pump has been operating at this flow for some time
butthecurrentdrawnismore,onecaninferthatthemachineneedsattention.One
Copyright © 2003 Marcel Dekker, Inc.

canalsocheckthepumpefficiencyfromitscharacteristiccurveandcomparethe
calculated and predicted efficiencies.
9.19
Q:
Derive an expression similar to (22) relating fan and motor.
A:
Equating the power consumption of a fan with that delivered by its motor,
P 1:17 10 4 qH 0:001732EI cosfZ 23
¼ (cid:4) (cid:3) (cid:4) w ¼ m ð Þ
where
q flow; acfm
¼
H staticheadof fan; in:WC
w ¼
Other terms are as in Q9.18.
Iftheefficiencyofafanisassumedtobe65%whenitsdifferentialheadis
4in.WC,themotorvoltageis460,andthecurrentis7A,thenthepowerfactoris
0.8 and the motor efficiency is 85%. Solving for q, we have
1:17 10 4 q 4 0:001732 460 7 0:80 0:85 0:65
(cid:3)
(cid:4) (cid:4) (cid:4) ¼ (cid:4) (cid:4) (cid:4) (cid:4) (cid:4)
or
q 5267acfm
¼
Onecancheckfromthefancurvewhethertheflowisreasonable.Alternatively,if
theflowisknown,onecanchecktheheadfromEq.(23)andcompareitwiththe
measured value. If the measured head is lower, for example, we can infer that
something is wrong with the fan or its drive or that the flow measured is not
correct.
9.20
Q:
How is the performance of pumps in series and in parallel evaluated?
A:
For parallel operation of two or more pumps, the combined performance curve
(H versusq)isobtainedbyaddinghorizontallythecapacitiesofthesameheads.
For series operation, the combined performance curve is obtained by adding
vertically the heads at the same capacities.
Copyright © 2003 Marcel Dekker, Inc.

The operatingpoint isthe intersectionof the combined performance curve
with the system resistance curve. Figure 9.6 explains this. Head and flow are
shownaspercentages[2].ABCistheH versusqcurveforasinglepump,DEF is
the H versus q curve for two such pumps in series, and AGH is the H versus q
curvefortwosuchpumpsinparallel.ToobtainthecurveDEF,weaddtheheads
at a given flow. For example, at q 100%, H with one pump is 100%, and with
¼
two pumps H will be 200%. Similarly, AGH is obtained by adding flows at a
given head. At H 100, q for two pumps will be 200%.
¼
LetthesystemresistancecurvebeKBGE.Whenonepumpaloneoperates,
theoperatingpointisB.Withtwopumpsinseries,Eistheoperatingpoint.With
two pumps in parallel, G is the operating point.
BHP curves also have been plotted and reveal that with series operation
BHP 250%andwithpumpsinparallelBHP 164%,indicatingthatBHP=qis
¼ ¼
larger in series operation than in parallel. This varies with pump and system
resistance characteristics. NPSH also increases with pump capacity.
r
Note that if the full capacity of the plant were handled by two pumps in
parallel and one tripped, the operating BHP would not be 50% of that with two
pumps,butmore,dependingonthenatureoftheH versusqcurveandthesystem
resistancecurve.Inthecaseabove,withKBGE asthesystemresistance,Gisthe
operatingpointwithtwopumps,andifonetripsBwouldbetheoperatingpoint.
FIGURE 9.6 Series and parallel operations of pumps with flat head capacity
curves. (FromRef. 2.)
Copyright © 2003 Marcel Dekker, Inc.

BHP at G is 142%, whereas at B it is 100% (see the inset of Fig. 9.6). Hence in
sizing drives for pumps in parallel, this fact must be taken into account. It is a
good idea to check on whether the pump has an adequately sized drive.
A similar procedure can be adopted for determining the performance of
fans in series and in parallel and for sizing drives.
9.21
Q:
Determine the parameters affecting the efficiency of the Brayton cycle [3].
A:
Figure 9.7a shows a simple reversible Brayton cycle used in gas turbine plants.
Air is taken at a temperature T absolute and compressed, and the temperature
1
after compression is T . Heat is added in the combustor, raising the gas
2
temperature to T ; the hot gases expand to T in the turbine, performing work.
3 4
Following are some of the terms used to describe the performance.
Q Q
Thermal efficiency TE a(cid:3) r 24
¼ Q ð Þ
a
FIGURE 9.7 (a)Simple and(b) regenerativeBrayton cycle.
Copyright © 2003 Marcel Dekker, Inc.

where
Q heataddedtocycle; Btu=lb
a ¼
Q heatrejected; Btu=lb
r ¼
Q C T T 25
a ¼ pð 3(cid:3) 2Þ ð Þ
Q C T T 26
r ¼ pð 4(cid:3) 1Þ ð Þ
P P and P P 27
2 ¼ 3 1 ¼ 4 ð Þ
Also,
T T
2 3 rk 1=k 28
ð (cid:3) Þ
T ¼T ¼ ð Þ
1 4
where
P P
r pressure ratio 2 3 29
¼ ¼P ¼P ð Þ
1 4
k ratioof gasspecificheats
¼
C gasspecificheat; Btu=lb
p ¼
T T temperatures; R
1(cid:3) 4 ¼ (cid:2)
P P pressure; psia
1(cid:3) 4 ¼
Using the above, we can write
Q T T
TE 1 r 1 4(cid:3) 1
¼ (cid:3)Q ¼ (cid:3)T T
a 3(cid:3) 2
T T =T 1
1 1 4 1(cid:3) 30a
¼ (cid:3)T (cid:4)T =T 1 ð Þ
2 3 2(cid:3)
Since, from Eq. (28), T =T T =T , we have
4 1 ¼ 3 2
T
TE 1 1 1 1=rk 1=k 30b
ð (cid:3) Þ
¼ (cid:3)T ¼ (cid:3) ð Þ
2
Example
A simple cycle takes in air at 80 F and 14.7psia and compresses it at constant
(cid:2)
entropythroughapressureratioof4.Thecombustorraisesthegastemperatureto
1500 F. The heated air expands to 14.7psia at constant entropy in the turbine.
(cid:2)
Assumek 1.3andC 0.28.Find(1)compressionwork,W ;(2)heatinputto
¼ p¼ c
cycle, Q ; (3) expansion work, Q ; (4) thermal efficiency, TE.
a e
Copyright © 2003 Marcel Dekker, Inc.

Solution. From Eq. (28),
T 80 460 41:3 1=1:3 742 R
2 ¼ð þ Þ(cid:4) ð (cid:3) Þ ¼ (cid:2)
Note that 41:3 1=1:3 1.375. Hence
ð (cid:3) Þ
¼
W C T T 0:28 742 540
c ¼ p(cid:4)ð 2(cid:3) 1Þ¼ (cid:4)ð (cid:3) Þ
56:6Btu=lb
¼
Heat input to cycle Q
¼ a
C T T
¼ p(cid:4)ð 3(cid:3) 2Þ
0:28 1500 460 742
¼ (cid:4)ð þ (cid:3) Þ
341Btu=lb
¼
T 1960
T 3 1425 R
4 ¼1:375¼1:375¼ (cid:2)
Expansion work Q 0:28 1960 1425 150Btu=lb
e ¼ (cid:4)ð (cid:3) Þ¼
150 56:6
TE (cid:3) 0:273; or 27:3%
¼ 341 ¼
Using Eq. (30b), TE 1 71=1.375 0.273.
¼ ¼
It can be seen that as the pressure ratio increases, TE increases. Also, as
inlet air temperature decreases, the efficiency increases. That is why some gas
turbine suppliers install chillers or air coolers at the compressor inlet so that
duringsummermonthstheturbineoutputdoesnotfalloffcomparedtothewinter
months.
9.22
Q:
How can the efficiency of a simple Brayton cycle be improved?
A:
One of the ways of improving the cycle efficiency is to use the energy in the
exhaustgases(Fig.9.7b)topreheattheairenteringthecombustor.Thisiscalled
regeneration.
Assuming 100% regeneration, the exhaust gas at temperature T preheats
4
airfromT toT whilecoolingittoT .Theactualheatrejectedcorrespondstoa
2 5 6
temperature drop of T T , while the heat added corresponds to T T , and
6(cid:3) 1 3(cid:3) 5
hence the cycle is more efficient. Assuming constant C ,
p
Q T T
TE 1 r 1 6(cid:3) 1
¼ (cid:3)Q ¼ (cid:3)T T
a 3(cid:3) 5
Copyright © 2003 Marcel Dekker, Inc.

Now P P P and P P P . Also,
2 ¼ 5 ¼ 3 4 ¼ 6 ¼ 1
T T T T
2 6 rk 1=k 3 3
ð (cid:3) Þ
T ¼T ¼ ¼T ¼T
1 1 4 5
T =T 1
TE 1 T 6 1(cid:3)
¼ (cid:3) 1 T T =T 1
5ð 3 5(cid:3) Þ
T
1 1 T =T T =T ;from above
¼ (cid:3)T ð 6 1 ¼ 3 5 Þ
5
T T T T
1 1 3 1 rk 1=k
ð (cid:3) Þ
T ¼T (cid:4)T ¼T (cid:4)
5 3 5 3
Hence
T
TE 1 1 rk 1=k 31
ð (cid:3) Þ
¼ (cid:3)T (cid:4) ð Þ
3
Example
Using the same data as above, compute the following for the ideal regenerative
cycle: (1) Work of compression, W ; (2) heat added to cycle; (3) heat added to
c
regenerator; (4) expansion work in turbine; (5) cycle efficiency.
Solution. For the same inlet temperature and pressure ratio, W 56.6
c¼
and T 742 R. Exhaust temperature from above 1425 R T .
2¼ (cid:2) ¼ (cid:2) ¼ 5
Heat added in regenerator C T T
¼ p(cid:4)ð 5(cid:3) 2Þ
0:28
¼
1425 742 191:3Btu=lb
(cid:4)ð (cid:3) Þ¼
Heat added in combustor Q C T T
¼ a ¼ p(cid:4)ð 3(cid:3) 5Þ
0:28 1960 1425
¼ (cid:4)ð (cid:3) Þ
150Btu=lb
¼
Heat rejected Q C T T
¼ r ¼ p(cid:4)ð 6(cid:3) 1Þ
0:28 742 540 56:6Btu=lb
¼ (cid:4)ð (cid:3) Þ¼
Q 56:6
TE 1 r 1 0:622;or62:2%
¼ (cid:3)Q ¼ (cid:3) 150 ¼
a
Using (31)
540
TE 1 41:3 1=1:3 0:621;or 62:1%
ð (cid:3) Þ
¼ (cid:3)1960(cid:4) ¼
It is interesting to note that as the pressure ratio increases, the efficiency
decreases. As the combustor temperature increases, the efficiency increases.
However, it can be shown that the power output increases with increases in the
Copyright © 2003 Marcel Dekker, Inc.

pressureratio.Henceindustrialgasturbinesoperateatapressureratiobetween9
and 18 and an inlet gas temperature of 1800–2200 F.
(cid:2)
NOMENCLATURE
ASR Actual steam rate, lb=kWh
BHP Brake horsepower, hp
C ;C ;C Factors correcting viscosity effects for flow, head, and efficiency
Q H E
C Specific heat, Btu=lb F
p (cid:2)
d Tube or pipe diameter, in.; subscript i stands for inner diameter
E Voltage
h Enthalpy, Btu=lb; subscripts f and g stand for saturated liquid and
vapor
H Head developed by pump, ft; subscript a stands for acceleration
HP Horsepower
H Head developed by fan, in. WC
w
I Current, A
k Ratio of gas specific heats, C =C
p v
L Length, ft
N Speed of pump or fan, rpm
NPSH Net positive suction head, ft; subscripts a and r stand for available
and required
P Power, kW
DP Differential pressure, psi
q Flow, gpm or acfm
Q ;Q Heat added, rejected, Btu=lb
a r
r Pressure ratio
s Specific gravity
s ;s Entropy of saturated liquid and vapor, Btu=lb R
f g (cid:2)
S Specific speed
DT Temperature rise, F
(cid:2)
TE Thermal efficiency
T Temperature, R
(cid:2)
TSR Theoretical steam rate, lb=kWh
V Velocity, ft=s
W Flow, lb=h
W Work of compression, Btu=lb
c
Z Efficiency, fraction; subscripts f;m;p, and t stand for fan, motor,
pump, and turbine
r Density, lb=cu ft
Copyright © 2003 Marcel Dekker, Inc.

REFERENCES
1. CameronHydraulicData.16thed.WoodcliffLake,NJ:IngersollRand,1981,p5.1.
2. IKarassik.CentrifugalPumpClinic.NewYork:MarcelDekker,1981,p102.
3. PowerMagazine,PowerHandbook.NewYork:McGraw-Hill,1983.
4. RHPerry,CHChilton.ChemicalEngineersHandbook.5thed.NewYork:McGraw-
Hill,1974.
Copyright © 2003 Marcel Dekker, Inc.

Appendix 1
A Quiz on Boilers and HRSGs
[The answers to all of these questions can be found in the book. However,
email me for the list of answers or clarifications if required. My email is:
v_ganapathy@yahoo.com.]
1. If boiler efficiency for a typical natural gas fired boiler is 83% on higher
heating value basis, what is it approximatelyon lower heating value basis?
a. 73% b. 83% c. 92%
2. IfNOxinanatural gasfiredboileris50ppmv(3% oxygendry),whatisit
in lb=MM Btu (HHV) basis?
a. 0.06 b. 0.10 c. 0.20
3. 1in.WCofadditionalgaspressuredropina100,000lb=hpackagedboiler
is worth about how many kWof fan power consumption?
a. 5 b. 20 c. 50
4. Ifboilerwaterconcentrationinaboilerdrumis1000ppmandsteampurity
is 1ppm, what is the percent steam quality?
a. 99.9 b. 99 c. 99.99
5. Boilers of the same capacity are located at different sites, whose ambient
conditions and elevation are as follows. Which case requires the biggest
fan?
a. 80 Fand sea level b. 100 Fand 3000ft c. 10 Fand 7000ft
(cid:2) (cid:2) (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

6. In a boiler plant if the conductivity of the condensate, makeup, and
feedwater are 800, 40, and 150mmho=cm, respectively, what is the percent
condensate returns in the feedwater?
a. 5 b. 50 c. 15
7. A20 F change inexitgastemperature of anoil-firedboiler changes boiler
(cid:2)
efficiency by approximately what percent?
a. 1 b. 0.5 c. 2.0
8. Approximate air flow (acfm) required in a packaged boiler firing 100MM
Btu=h (HHV) of natural gas is:
a. 19,000 b. 30,000 c.12,000
9. The steam pressure drop in a boiler superheater is 50psi when generating
600psig, 650 F steam. What is it likely to be at 400psig, 600 F with the
(cid:2) (cid:2)
same flow?
a. 70 b. 30 c. 50
10. Which is the worst case scenario for an economizer from the viewpoint of
sulfuric acid condensation? Assume that the oil-fired boiler flue gas
contains 12% water vapor and 0.03% SO .
2
a. Flue gas at 680 F and feedwater at 200 F b. Flue gas at 320 F and
(cid:2) (cid:2) (cid:2)
feedwater at 275 F.
(cid:2)
11. If vol% of oxygen (dry) in a natural gas fired boiler is 2.0%, what is the
excess air used?
a. 15 b. 5 c. 10
12. If boiler casing heat loss is 0.2% at 100% load, what is it at 25% load,
assuming that wind velocity and ambient temperature are unchanged?
a. 1.0 b. 2.0 c. 0.8
13. Plantmanagementdecidestochangethetubeinnerdiameterofanexisting
superheaterfrom1.7in.to1.5in.Thesteam-sidepressuredropforthesame
steam conditions will go up by what percent?
a. 87 b. 65 c. 29
14. Theheattransfercoefficientinafinnedtubebundleishigherthaninabare
tube exchanger for the same gas velocity, temperature, tube size, and
geometry.
a. True b. False
15. Inafiretubewasteheatboiler,asmalldiametertubehasahighertubeside
heattransfercoefficientandhigherheatfluxthanalargertubeforthesame
gas velocity.
a. True b. False
16. Superheated steam temperature from a boiler firing oil will be higher than
when firing natural gas at the same steam generation rate (assuming steam
temperature is uncontrolled).
a. True b. False
17. More flue gas is generated in a boiler while firing oil than while firing
Copyright © 2003 Marcel Dekker, Inc.

natural gas at the same excess air and steam generation.
a. True b. False
18. Themaximumpossiblefuel(naturalgas=distillateoil)thatcanbefiredinan
HRSG with exhaust gas flow 200,000lb=h and 14% oxygen wet in MM
¼
Btu=h (LHV) is:
a. 100 b. 150 c. 50
19. SurfaceareagivesagoodindicationofwhetheraboilerorHRSGdesignis
adequate or not.
a. True b. False
20. An uncooled soot blower lance is located in a boiler convection bank at
1700 F gas temperature. Its temperature will be:
(cid:2)
a. >1700 F b. 1700 F c. <1700 F
(cid:2) (cid:2) (cid:2)
21. (a) A fire tubewaste heat boiler using small diameter tubes will be longer
than the design using larger diameter tubes for the same duty and gas
pressure drop.
a. True b. False
(b) A fire tube waste heat boiler using small diameter tubes requires less
surface area than the design using larger diameter tubes for the same
duty and gas pressure drop.
a. True b. False
22. For the same mass flow and gas temperature drop, a flue gas containing
16% water vapor will transfer more energy than a gas stream having 5%
water vapor.
a. True b. False
23. Designoftubularairheatersinsteam generatorscanbeimprovediffinned
tubes are used instead of plain tubes.
a. True b. False c. Depends on fuel used
24. In a crossflowheat transfer situation, an in-line arrangement of plain tubes
is better than a staggered one.
a. True b. False
25. For the same casing insulation thickness and ambient conditions, alumi-
nium casing will run hotter than carbon steel.
a. True b. False
26. Ifadditionalsteamisrequiredinacogenerationplant,supplementaryfiring
the HRSG rather than using a packaged boiler will be more prudent.
a. True b. False
27. Required thickness of a boiler tube subjected to external pressure will be
less than when the same tube is subjected to the same internal pressure at
the same temperature.
a. True b. False
28. Which is a better choice for fin density for a superheater in a HRSG?
a. 5 fins=in. b. 2 fins=in.
Copyright © 2003 Marcel Dekker, Inc.

29. The exit gas temperature in a single-pressure unfired HRSG generating
steam at 600psig, 700 F can be less than 300 F. (Assume exhaust gas at
(cid:2) (cid:2)
950 Fand feedwater at 230 F.)
(cid:2) (cid:2)
a. True b. False
30. A boiler designed for 1000psig, 800 F steam can be operated at the same
(cid:2)
steam flow at 300psig without modifications.
a. True b. False
31. A gas turbine HRSG economizer is likely to steam at which ambient
temperature in unfired mode?
a. 40 F b. 90 F
(cid:2) (cid:2)
32. Moreenergycanbetransferredtoaboilerevaporatorifthecirculationratio
is higher.
a. True b. False
33. Heat flux will be higher in a packaged boiler furnace for which fuel?
Assume same steam generation.
a. Fuel oil b. Natural gas
34. For the same excess air and exit gas temperature, an oil-fired boiler will
have a higher efficiency on HHV basis than a gas-fired boiler.
a. True b. False
35. For the same mass flow per tube and length of tube, superheated steam at
600psig, 800 F will have a higher pressure drop than 150psig saturated
(cid:2)
steam.
a. True b. False
36. Gas-side fouling increases the tubewall temperature inawaste heat boiler.
a.True b.False c.Dependsonwhetheritisafiretubeorwatertubeboiler
37. Thefeedpumprequiresmorepowertogenerateagivenamountofsteamat
agivenpressureandtemperatureinaonce-throughHRSGthaninanatural
circulation HRSG.
a. True b. False
38. The volumetric heat release rate is more important in a gas-fired packaged
boiler than the area heat release rate.
a. True b. False
39. Large margins on flow and head should not generally be used while
selecting the fan for a packaged boiler.
a. True b. False
40. If an economizer with counterflow arrangement is experiencing low
temperature corrosion problems, then re-piping it with a parallel flow
arrangement can fix the problem.
a. True b. False
41. Exit gas temperature from a single-pressure HRSG having a superheater,
evaporator, and economizer increases as steam generation increases.
a. True b. False
Copyright © 2003 Marcel Dekker, Inc.

42. It is better to preheat condensate or feedwater using extraction steam from
the steam turbine rather than use the energy in the HRSG exhaust gases.
a. True b. False
43. Steamfordeaerationshouldpreferablybetakenfromtheboileroutletrather
than from an extraction point in the steam turbine.
a. True b. False
44. The maldistribution of steam flow through superheater tubes will be the
worst at a boiler load of:
a. 20% b. 50% c. 100%
45. WhichfuelgeneratesthemaximumamountofcarbondioxideperMMBtu
fired?
a. Oil b. Natural gas c. Coal
46. Is it possible to predict the off-design performance of an HRSG without
knowing its mechanical constructional features?
a. Yes b. No
47. Can we have more surface area in an HRSG and yet transfer less duty?
a. Yes b. No
48. Can we use finned tubes for the evaporator or superheater of a gas-fired
packaged boiler?
a. Yes b. No
49. What happens to the pinch and approach points of the evaporator in an
HRSG as we increase the supplementary firing rate?
a. Both increase b. Both decrease c. Pinch point increases while
approach point decreases d. They are unchanged
50. In a packaged boiler, the furnace performance and circulation are more
critical in oil firing than in gas firing.
a. True b. False
51. Can a superheater be located between the evaporator and economizer in a
packaged boiler?
a. Yes b. No
52. Good steam-separating devices cannot prevent carryover of silica from
boiler water into steam at high pressures.
a. True b. False
53. Superheated steam for use in turbines should havebetter steam purity than
saturated steam.
a. True b. False
54. Feedwater used for attemperation in a desuperheater for steam temperature
control should preferably have low to zero solids.
a. True b. False
55. Tube-sideheatfluxwillbehigherinaplaintubeevaporatorthaninafinned
tube evaporator for the same gas- and steam-side conditions.
a. True b. False
Copyright © 2003 Marcel Dekker, Inc.

56. In a waste heat boiler containing hydrogen chloride gas, a low steam
temperature (say 700 F vs 850 F) is preferred.
(cid:2) (cid:2)
a. True b. False
57. A higher steam pressure requires a higher steam temperature to minimize
wetness in steam after expansion in a steam turbine.
a. True b. False
58. An ammonia–water mixture has a varying boiling point and hence is a
better fluid for energy recovery from waste flue gases than steam.
a. True b. False
59. The cross section of a 100,000lb=h packaged boiler will be much smaller
than that of an unfired gas turbine HRSG generating the same amount of
steam.
a. True b. False
60. Gas conditions being the same, as steam pressure increases, the steam
generation in an unfired HRSG:
a. increases b. decreases c. is unchanged
61. ThecrosssectionofaforcedcirculationHRSGanditssurfaceareawillbe
much different from a natural circulation HRSG for the same duty and
pressure drop.
a. True b. False c. Can’t say
62. Afiretubewasteheatboilergenerallyrespondsfastertoloadchangesthan
an equivalent water tube design.
a. True b. False
63. The amount of deaeration steam is impacted by the conductivity of boiler
feedwater.
a. True b. False
64. InaboilerorHRSG evaporator,theallowable steam qualitytoavoidDNB
conditions decreases as the heat flux increases.
a. True b. False
65. A natural circulation HRSG using vertical evaporator tubes can handle
higher heat flux than a forced circulation or once-through unit using
horizontal tubes.
a. True b. False
66. A gas turbine plant has two options: a supplementary-fired HRSG and an
unfired HRSG. The cross section of the supplementary-fired HRSG
generating twice the amount of steam as the unfired HRSG should be
much larger.
a. True b. False
Think About It!
1. WhyismultiplepressuresteamgenerationoftenrequiredinHRSGsbutnot
in a packaged boiler?
Copyright © 2003 Marcel Dekker, Inc.

2. Explainhowsurfaceareascanbedifferentinsteamgenerators(orHRSGs)
and yet the duty transferred is the same.
3. Why is supplementary firing very efficient in HRSGs?
4. Why is an economizer preferred to an air heater in oil- and gas-fired
packaged boilers? Give at least two reasons.
5. Why is steaming in the economizer often a concern in HRSGs and not in
packaged boilers?
6. Whycanweachievealowexitgastemperatureinapackagedboileratany
steam pressure, whereas it is difficult in a single-pressure unfired HRSG?
7. Why is the superheated steam temperature generally lower with oil firing
than with gas firing in a packaged boiler?
8. Why is a low fin density, say 2fins=in., preferred in a HRSG superheater
over, say, 5fins=in.?
9. Why does raising the gas temperature at the economizer alone not help
minimize low temperature corrosion problems?
10. Compute typical operating costs of fuel and electricity for various boilers
and HRSGs in your plant and suggest how to lower these costs.
11. Is a supplementary-fired HRSG a better choice than an unfired HRSG in a
combined cycle plant?
12. Whydowenotworryaboutpinchandapproachpointsinapackagedboiler,
whereas they are very important in an HRSG?
13. What are the advantages of a convective superheater in a packaged boiler
over a radiant design?
14. What are the various factors to be considered while modifying an existing
packaged boiler to meet lower emissions of NOx and CO?
15. Inapackagedboiler,whyisinterstageattemperationforsteamtemperature
control generally preferred to attemperation at the superheater exit?
16. A single-pressure unfired HRSG generates 600psig steam at 750 F using
(cid:2)
230 F feedwater with an exit gas temperature of 380 F. To lower the exit
(cid:2) (cid:2)
gas temperature, is it more prudent to add a condensate heater rather than
increase the surface area of the evaporator significantly?
17. Explain why rules of thumb relating surface areas with steam generation
can be misleading.
18. Aneconomizerhasbeenremovedfromapackagedboilerformaintenance.
Can the plant generate the same amount of steam as before? What are the
concerns?
Copyright © 2003 Marcel Dekker, Inc.

Appendix 2
Conversion Factors
Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

Appendix 3
Tables
TABLEA1 ThermodynamicPropertiesofDrySaturatedSteam—PressureTable
TABLEA2 Thermodynaic Properties of Dry Saturated Steam—Temperature
Table
TABLEA3 Thermodynamic Propertiesof Superheated Steam
TABLEA4 Enthalpyof CompressedWater
TABLEA5 SpecificHeat,Viscosity,andThermalConductivityofSomeCommon
GasesatAtmospheric Pressurea
TABLEA6a Specific Heat, Viscosity, and Thermal Conductivity of Products of
Combustion ofNatural Gas,Fuel Oil,and Ambient Air
TABLEA6b Gas TurbineExhaust Gases
TABLEA7a Enthalpy ofGasesa
TABLEA7b Enthalpy of Products of Combustion of Natural Gas and Fuel Oila
(Btu=lb)
TABLEA8 Correlation forSuperheated SteamProperties
TABLEA9 Coefficients to Estimate Properties of Dry, Saturated Steam with
Equationa
TABLEA10 Saturation Line; SpecificHeat Capacityand TransportProperties
TABLEA11 SurfaceTension of Water
TABLEA12a Specific Heat at Constant Pressure of Steam and Water
Btu=lbm F
(cid:2)
TABLEA12b ð Viscosity of Þ Steamand Water lbm=hft
TABLEA12c Thermal Conductivity of Steam ð and Wa Þ ter Btu=hft
(cid:2)
F 103
½ð Þ(cid:4) (cid:5)
Copyright © 2003 Marcel Dekker, Inc.

TABLEA1 Thermodynamic Properties ofDry SaturatedSteam—Pressure Table
Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

TABLEA2 Thermodynaic Properties of DrySaturatedSteam—Temperature Table
Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

TABLEA3 Thermodynamic Properties ofSuperheated Steam
Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

TABLEA3 Continued
Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

TABLEA4 Enthalpyof CompressedWater
Copyright © 2003 Marcel Dekker, Inc.

Copyright © 2003 Marcel Dekker, Inc.

TABLEA5 SpecificHeat, Viscosity, and ThermalConductivity of SomeCommon Gasesat Atmospheric Pressurea
Copyright © 2003 Marcel Dekker, Inc.

TABLEA6a Specific Heat, Viscosity, and Thermal Conductivity of Products of
Combustion ofNatural Gas,FuelOil, and Ambient Air
Natural gas Fueloil Air
Temp,
F C m k C m k C m k
(cid:2) p p p
2000 0.3326 0.1174 0.0511 0.3206 0.1178 0.0497 0.2906 0.1232 0.0475
1600 0.3203 0.1050 0.0437 0.3094 0.1055 0.0427 0.2817 0.1108 0.0414
1200 0.3059 0.0908 0.0362 0.2959 0.0915 0.0356 0.2712 0.0967 0.0351
800 0.2907 0.0750 0.0287 0.2812 0.0757 0.0284 0.2602 0.0807 0.0287
400 0.2757 0.0575 0.0211 0.2660 0.0583 0.0211 0.2498 0.0631 0.0221
Analysis of natural gas–15% excess air vol%: CO 8.29, H O 18.17, N 71.08,
2¼ 2 ¼ 2¼
O 2.46.
2¼
Fueloil–15%excessairvol%:CO 11.57,H O 12.29,N 73.63,O 2.51.
2¼ 2 ¼ 2¼ 2¼
Air vol%: H O 1, N 78, O 21, C specific heat, Btu=lb F. m viscosity, lb=ft h;
2 ¼ 2¼ 2¼ p¼ (cid:2) ¼
k thermalconductivity,Btu=fth F.
¼ (cid:2)
TABLEA6b Gas TurbineExhaust Gases
Temp, F C m k
(cid:2) p
1000 0.2768 0.087 0.0321
800 0.2704 0.0789 0.0287
600 0.2643 0.0702 0.0252
400 0.2584 0.0612 0.0217
200 0.2529 0.0517 0.0182
Gas analysis vol%: CO 3, H O 7, N 75,
2¼ 2 ¼ 2¼
O 15.
2¼
Copyright © 2003 Marcel Dekker, Inc.

TABLEA7a Enthalpy ofGasesa
Temp, ( F) A B C D
(cid:2)
200 34.98 31.85 35.52 33.74
400 86.19 78.57 87.83 83.00
600 138.70 126.57 141.79 133.42
800 192.49 175.77 197.35 184.91
1000 247.56 226.2 254.47 237.52
1400 330.15 372.93 345.77
1800 437.86 496.42 457.82
a Content(vol%)
CO H O N O SO
2 2 2 2 2
A Gasturbineexhaust 3 7 75 15 —
B Sulfurcombustion — — 81 10 9
C Fluegas 12 12 70 6 —
D Dryair 79 21 —
TABLEA7b Enthalpy of Products of
Combustion of Natural Gas and Fuel
Oila(Btu=lb)
Temp( F) Natural gas Fueloil
(cid:2)
3000 928.6 894.9
2600 787.1 759.5
2200 649.5 627.3
1800 516.3 498.8
1400 387.9 374.8
1000 264.9 255.8
600 147.9 142.6
200 37.1 35.7
aSamefuelanalysisasinTableA6a.
Copyright © 2003 Marcel Dekker, Inc.

TABLEA8 Correlation forSuperheated SteamProperties
Copyright © 2003 Marcel Dekker, Inc.

TABLEA9 CoefficientstoEstimatePropertiesofDry,SaturatedSteamwithEquationa
Copyright © 2003 Marcel Dekker, Inc.

TABLEA9
Copyright © 2003 Marcel Dekker, Inc.

TABLEA10 Saturation Line; SpecificHeat Capacityand TransportProperties
t t p C m 106 n 106 l 103 C m 106 n 106 l 103
c pf f (cid:4) f (cid:4) f (cid:4) pg g(cid:4) g(cid:4) g(cid:4)
ð
(cid:2)F
Þ ð
(cid:2)C
Þ ð
lbft=in:2
Þ ð
Btu=lb
(cid:2)
F
Þ ð
lb=fts
Þ ð
ft2=s
Þ ð
Btu=fth
(cid:2)
F
Þ ð
Pr
Þf ð
Btu=lb
(cid:2)
F
Þ ð
lb=fts
Þ ð
ft2=s
Þ ð
Btu=fth
(cid:2)
F
Þ ð
Pr
Þg
32 0.0 0.0886 1.006 1180.0 18.9 329 12.9 0.442 5.91 19500 10.0 0.94
40 4.4 0.1217 1.004 1027.0 16.5 333 11.1 0.443 6.02 14700 10.5 0.91
60 15.6 0.2562 1.000 753.0 12.1 345 7.86 0.447 6.24 7530 10.9 0.92
80 26.7 0.5069 0.998 576.0 9.26 354 5.85 0.447 6.47 4100 11.3 0.92
100 37.8 0.949 0.998 457.0 7.37 363 4.52 0.449 6.71 2350 11.7 0.93
120 49.9 1.693 0.999 372.0 6.03 371 3.61 0.452 6.95 1410 12.1 0.94
140 60.0 2.889 1.000 311.0 5.07 378 2.96 0.458 7.20 886 12.4 0.96
160 71.1 4.741 1.001 264.0 4.33 383 2.48 0.465 7.45 576 13.0 0.96
180 82.2 7.511 1.003 229.0 3.78 388 2.13 0.474 7.70 387 13.5 0.97
200 93.3 11.53 1.006 201.0 3.34 392 1.86 0.484 7.96 268 14.0 0.99
220 104.4 17.19 1.009 179.0 3.00 394 1.65 0.495 8.22 190 14.6 1.00
240 115.6 24.97 1.013 160.0 2.71 396 1.47 0.508 8.50 139 15.2 1.02
260 126.7 35.42 1.018 145.0 2.48 397 1.34 0.522 8.77 103 15.8 1.04
280 137.8 49.20 1.024 133.0 2.29 397 1.23 0.538 9.05 78.2 16.5 1.06
300 148.9 67.00 1.030 122.0 2.13 397 1.14 0.556 9.32 60.3 17.3 1.08
320 160.0 89.64 1.038 113.0 2.00 395 1.07 0.577 9.58 47.1 18.1 1.10
340 171.1 118.00 1.047 105.0 1.88 393 1.01 0.600 9.85 37.3 18.9 1.13
360 182.2 153.00 1.057 98.6 1.79 390 0.96 0.627 10.1 29.9 19.9 1.15
380 193.3 195.7 1.069 92.7 1.70 387 0.92 0.658 10.4 24.2 21.0 1.17
400 204.4 247.3 1.082 87.5 1.63 382 0.89 0.692 10.6 19.8 22.1 1.19
Copyright © 2003 Marcel Dekker, Inc.

420 215.6 308.8 1.097 82.9 1.57 377 0.87 0.731 10.9 16.3 23.4 1.23
440 226.7 381.6 1.115 78.8 1.52 371 0.85 0.774 11.2 13.6 24.9 1.25
460 237.8 466.9 1.135 75.2 1.47 364 0.84 0.823 11.5 11.4 26.5 1.29
480 248.9 566.1 1.158 71.9 1.44 357 0.84 0.885 11.7 9.60 28.4 1.31
500 260.0 680.8 1.186 68.9 1.41 349 0.84 0.951 12.1 8.14 30.5 1.36
520 271.1 812.4 1.229 66.2 1.38 340 0.86 1.038 12.4 6.94 32.9 1.41
540 282.2 962.6 1.275 63.7 1.37 330 0.88 1.147 12.8 5.95 35.8 1.48
560 293.3 1133.2 1.338 61.5 1.36 319 0.92 1.286 13.2 5.11 39.2 1.56
580 304.4 1326.1 1.420 59.8 1.36 308 0.99 1.472 13.6 4.38 43.3 1.66
600 315.6 1543.3 1.520 58.0 1.37 296 1.07 1.735 14.4 3.85 48.4 1.86
620 326.7 1787.1 1.659 55.7 1.37 283 1.17 2.153 15.3 3.37 54.9 2.16
640 337.8 2060.3 1.880 52.9 1.37 269 1.33 2.832 16.4 2.95 63.6 2.63
660 348.9 2366.0 2.310 49.5 1.37 254 1.62 3.943 17.9 2.58 76.1 3.34
680 360.0 2708.3 3.466 45.2 1.37 231 2.44 5.676 20.2 2.25 97.0 4.26
Copyright © 2003 Marcel Dekker, Inc.

TABLEA11 SurfaceTension of Water
Temp( F) lbft=ft 103 Temp( F) lbft=ft 103
(cid:2) (cid:2)
(cid:4) (cid:4)
32 5.184 350 2.942
40 5.141 400 2.512
60 5.003 450 2.071
80 4.914 500 1.624
100 4.794 550 1.178
150 4.473 600 0.744
200 4.124 650 0.340
250 3.752 700 0.018
300 3.357
Copyright © 2003 Marcel Dekker, Inc.

TABLEA12a SpecificHeat atConstant Pressureof SteamandWater Btu=lbm
(cid:2)
F
ð Þ
Pressure (psia)
Temp
(cid:2)F 1 2 5 10 20 50 100 200 500 1000 2000 5000
ð Þ
1500 0.559 0.559 0.559 0.559 0.559 0.560 0.561 0.563 0.569 0.580 0.601 0.668
1400 0.551 0.551 0.551 0.551 0.551 0.552 0.553 0.555 0.563 0.575 0.600 0.681
1300 0.543 0.543 0.543 0.543 0.543 0.544 0.545 0.548 0.556 0.570 0.600 0.702
1200 0.533 0.533 0.533 0.533 0.534 0.535 0.536 0.540 0.550 0.567 0.603 0.740
1100 0.524 0.542 0.524 0.524 0.525 0.526 0.528 0.532 0.544 0.564 0.612 0.814
1000 0.515 0.515 0.515 0.515 0.516 0.518 0.519 0.524 0.539 0.566 0.633 0.970
900 0.506 0.506 0.506 0.506 0.507 0.509 0.512 0.518 0.537 0.576 0.683 1.382
800 0.497 0.497 0.497 0.497 0.498 0.501 0.505 0.513 0.544 0.605 0.800 2.420
700 0.488 0.488 0.488 0.489 0.490 0.494 0.500 0.513 0.563 0.681 1.181 1.897b
600 0.479 0.480 0.480 0.481 0.483 0.489 0.499 0.522 0.621 0.888 1.453 1.253
500 0.472 0.472 0.473 0.475 0.478 0.489 0.508 0.554 0.773 1.181 1.157 1.106
400 0.464 0.465 0.467 0.470 0.476 0.497 0.536 0.636 1.077 1.072 1.063 1.041
300 0.458 0.459 0.463 0.469 0.482 0.524 1.029 1.028 1.027 1.024 1.019 1.006
250 0.456 0.458 0.463 0.471 0.489 1.015 1.014 1.014 1.013 1.011 1.007 0.996
200 0.453 0.455 0.463 0.475 1.005 1.005 1.005 1.004 1.003 1.002 0.998 0.989
150 0.451 0.455 0.866 1.001 1.000 1.000 1.000 1.000 0.998 0.997 0.993 0.984
100 0.998 0.998 0.998 0.998 0.998 0.998 0.998 0.997 0.996 0.994 0.990 0.980
50 1.002 1.002 1.002 1.002 1.002 1.002 1.001 1.001 0.999 0.996 0.989 0.972
32 1.007 1.007 1.007 1.007 1.007 1.007 1.006 1.006 1.003 0.999 0.990 0.969
aHorizontalbarsindicatephasechange
bCriticalpoint(P 3,206.2psia;T 705.4 F).
¼ ¼ (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

TABLEA12b Viscosity ofSteamand Water lbm=hft
ð Þ
Pressure(psia)
Temp
( F) 1 2 5 10 20 50 100 200 500 1000 2000 5000
(cid:2)
1500 0.0996 0.0996 0.0996 0.0996 0.0996 0.0996 0.0996 0.0996 0.1008 0.1008 0.1019 0.1066
1400 0.0938 0.0938 0.0938 0.0938 0.0938 0.0938 0.0952 0.0952 0.0952 0.0961 0.0973 0.1019
1300 0.0892 0.0982 0.0892 0.0892 0.0892 0.0892 0.0892 0.0892 0.0892 0.0903 0.0915 0.0973
1200 0.0834 0.0834 0.0834 0.0834 0.0834 0.0834 0.0834 0.0834 0.0846 0.0846 0.0867 0.0926
1100 0.0776 0.0776 0.0776 0.0776 0.0776 0.0776 0.0776 0.0776 0.0788 0.0799 0.0811 0.0892
1000 0.0730 0.0730 0.0730 0.0730 0.0730 0.0730 0.0730 0.0730 0.0730 0.0741 0.0764 0.0857
900 0.0672 0.0672 0.0672 0.0672 0.0672 0.0672 0.0672 0.0672 0.0683 0.0683 0.0707 0.0846
800 0.0614 0.0614 0.0614 0.0614 0.0614 0.0614 0.0614 0.0614 0.0625 0.0637 0.0660 0.0973
700 0.0556 0.0556 0.0556 0.0556 0.0556 0.0556 0.0568 0.0568 0.0568 0.0579 0.0625 0.171b
600 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.0510 0.210 0.221
500 0.0452 0.0452 0.0452 0.0452 0.0452 0.0452 0.0452 0.0440 0.0440 0.250 0.255 0.268
400 0.0394 0.0394 0.0394 0.0394 0.0394 0.0394 0.0394 0.0382 0.317 0.320 0.323 0.335
300 0.0336 0.0336 0.0336 0.0336 0.0336 0.0336 0.441 0.442 0.444 0.445 0.448 0.460
250 0.0313 0.0313 0.0313 0.0313 0.0313 0.551 0.551 0.551 0.552 0.554 0.558 0.569
200 0.0290 0.0290 0.0290 0.0290 0.725 0.725 0.725 0.726 0.729 0.729 0.732 0.741
150 0.0255 0.0255 1.032 1.032 1.032 1.032 1.032 1.032 1.033 1.034 1.037 1.044
100 1.645 1.645 1.645 1.645 1.645 1.645 1.645 1.645 1.645 1.646 1.646 1.648
50 3.144 3.144 3.144 3.144 3.144 3.144 3.144 3.142 3.141 3.139 3.134 3.119
32 4.240 4.240 4.240 4.240 4.240 4.240 4.240 4.239 4.236 4.231 4.222 4.192
aHorizontalbarsindicatephasechange.
bCriticalpoint(P 3,206.2psia;T 705.4 F).
¼ ¼ (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

TABLEA12c Thermal Conductivity ofSteamand Water Btu=hft
(cid:2)
F 103
½ð Þ(cid:4) (cid:5)
Pressure (psia)
Temp
( F) 1 2 5 10 20 50 100 200 500 1000 2000 5000
(cid:2)
1500 63.7 63.7 63.7 63.7 63.7 63.8 64.0 64.3 65.4 67.1 70.7 82.0
1400 59.2 59.2 59.2 59.2 59.3 59.4 59.6 59.9 60.9 62.7 66.3 78.2
1300 54.8 54.8 54.8 54.8 54.8 54.9 55.1 55.5 56.5 58.3 62.0 74.6
1200 50.4 50.4 50.4 50.4 50.4 50.5 50.7 51.0 52.1 53.9 57.8 71.6
1100 46.0 46.0 46.0 46.0 46.1 46.2 46.3 46.7 47.8 49.6 53.7 69.8
1000 41.7 41.7 41.8 41.8 41.8 41.9 42.1 42.4 43.5 45.5 50.0 70.7
900 37.6 37.6 37.6 37.6 37.6 37.7 37.9 38.3 39.4 41.5 46.8 80.2
800 33.6 33.6 33.6 33.6 33.6 33.7 33.9 34.3 35.5 37.9 44.9 129.6
700 29.7 29.7 29.7 29.7 29.8 29.9 30.1 30.4 31.8 35.0 47.5 262.8b
600 26.0 26.0 26.1 26.1 26.1 26.2 26.4 26.9 28.7 34.1 301.9 333.7
500 22.6 22.6 22.6 22.6 22.7 22.8 23.0 23.6 26.9 350.8 357.4 373.8
400 19.4 19.4 19.4 19.4 19.5 19.6 20.0 21.3 383.0 384.9 388.5 398.6
300 16.5 16.5 16.5 16.5 16.6 16.9 396.9 397.2 398.0 399.2 402.0 409.9
250 15.1 15.1 15.1 15.2 15.3 396.9 397.0 397.3 398.1 399.4 402.1 409.7
200 13.8 13.8 13.9 14.0 391.6 391.6 391.8 392.1 393.0 394.4 397.2 404.9
150 12.7 12.7 380.5 380.5 380.6 380.7 380.8 381.1 382.1 383.7 386.7 394.7
100 363.3 363.3 363.3 363.3 363.3 363.4 363.6 363.9 365.0 366.6 369.8 378.3
50 339.1 339.1 339.1 339.1 339.2 339.3 339.4 339.8 340.8 342.5 345.7 354.6
32 328.6 328.6 328.6 328.6 328.6 328.7 328.9 329.2 330.3 331.9 335.1 344.1
aHorizontalbarsindicatephasechange.
bCriticalpoint(P 3,206.2psia;T 705.4 F).
¼ ¼ (cid:2)
Copyright © 2003 Marcel Dekker, Inc.

Bibliography
BOOKS
ASME.2001ASMEBoilerandPressureVesselCode,Sec.1and8,July2001.
ASME.ASMEPowerTestCodePTC4.4-1981,GasTurbineHRSGs.NewYork,1981.
ASME.ASMEPowerTestCodePTC4-1998.FiredSteamGenerators.NewYork,1998.
Babcock&Wilcox.Steam,ItsGenerationandUse,40thed.NewYork,1992.
Betz Laboratories. Betz Handbook of Industrial Water Conditioning. Trevose, Pennsyl-
vania,1976.
CombustionEngineering,Combustion-FossilPowerSystems,3rded.Windsor,1981.
CraneCo.FlowofFluids,TechnicalPaper410.NewYork,1981.
ElliottCT.StandardHandbookofPowerPlantEngineering.McGraw-Hill,NewYork,1989.
HicksTG.HandbookofMechanicalEngineeringCalculations.McGraw-Hill,NewYork,
1998.
JohnZinkCo.,CombustionHandbook.Tulsa,Oklahoma,2001.
KakacS.Boilers,EvaporatorsandCondensers.JohnWiley,NewYork,1991.
KarassikIJ.CentrifugalPumpClinic.MarcelDekker,NewYork,1981.
KernDQ.ProcessHeatTransfer.McGraw-Hill,NewYork,1950.
NalcoChemicalCo.TheNalcoGuidetoBoilerFailureAnalysis.McGraw-Hill,NewYork,
1991.
RoshenowWM,HartnettJP.HandbookofHeatTransfer.McGraw-Hill,NewYork,1972.
Copyright © 2003 Marcel Dekker, Inc.

JOURNALS
ChemicalEngineering.ChemicalWeekPublishing,NewYork.
ChemicalEngineeringProgress.AlChe,NewYork.
CogenerationandOnsitePowerGeneration.SciencePublishers,London,UK.
HeatTransferEngineering.Taylor&Francis,London,UK.
HydrocarbonProcessing.GulfPublishing,Houston,Texas.
ModernPowerSystems.WilmingtonPublishing,Kent,UK.
OilandGasJournal,PennWell.Tulsa,Oklahoma.
PetroleumTechnologyQuarterly.CrambethAllenPublishing,London,UK.
PlantEngineering.Cahners,OakBrook,Illinois.
PollutionEngineering.BusinessNewsPublishing,Troy,MI.
Power.McGraw-Hill,NewYork.
PowerEngineering.PennWell,Tulsa,Oklahoma.
Seealsohttp://vganapathy.tripod.com/boilers.htmlformorearticles.
Copyright © 2003 Marcel Dekker, Inc.

Glossary
acfh Actual cubic feet per hour.
acfm Actualcubicfeetperminute,atermusedtoindicatetheflowrate
of gases, at any condition of temperature and pressure.
API Ascale adoptedby AmericanPetroleum Institute toindicate the
(cid:2)
specific gravityofa liquid. Water has an API gravityof 10 API
(cid:2)
and No. 2 fuel oil, about 35 API.
(cid:2)
ABMA American Boiler Manufacturers Association.
ASME American Society of Mechanical Engineers.
ASR Actual steam rate, a term used to indicate the actual steam
consumption of steam turbines in lb=kWh.
BHP Brakehorsepower,atermusedfor powerconsumption or rating
of turbomachinery. This does not include the efficiency of the
drive.
Btu British thermal unit, a term for measuring heat.
CFD Computational fluid dynamics
CO Carbon monoxide
CO Carbon dioxide
2
cP Centipoise, a unit for measurement of absolute viscosity.
CR Circulationratio,atermusedtoindicatetheratiobyweightofa
mixtureofsteamandwatertothatofsteaminthemixture.ACR
Copyright © 2003 Marcel Dekker, Inc.

of4meansthat1lbofsteam–watermixturehas1lbofsteamand
4
the remainder water.
dB Decibel, a unit for measuring noise or sound pressure levels.
dBA Decibel, scale A; a unit for measuring sound pressure levels
corrected for frequency characteristics of the human ear.
DNB Departure from nucleate boiling.
FGR Flue gas recirculation.
fps, fpm, fph Feet per second, minute, and hour; units for measuring the
velocity of fluids.
HAT Humid air turbine.
gpm, gph Volumetric flow rate in gallons per minute or hour.
HHV Higher heating value or gross heating value of fuels.
HRSG Heat recovery steam generator.
ICAD Intercooled aeroderivative.
ID Inner diameter of tube or pipe.
IGCC Integrated gasification and combined cycle.
in. WC A unit to measure pressure of gas streams; inches of water
column.
kW Kilowatt, a unit of measurement of power.
LHV Lower heating value or net heating value of a fuel.
LMP Larson–Miller parameter.
LMTD Log-mean temperature difference.
ln Logarithm to base e; natural logarithm.
log Logarithm to base 10.
M lb=h Thousands of pounds per hour
MM Btu Millions of British thermal units.
MW Molecular weight.
NOx Oxides of nitrogen.
NPSH Net positive suction head, a term used to indicate the effective
head in feet of liquid column to avoid cavitation. Subscripts r
and a stand for required and available.
NTU Number of transfer units; a term used in heat exchanger design.
OD Outer diameter of tube or pipe.
oz Ounce.
ozi Ounces per square inch, a term for measuring fluid pressure.
ppm Parts per million by weight or volume.
psia Pounds per square inch absolute, a term for indicating pressure.
psig Pounds per square inch gauge, a term for measuring pressure.
PWL Soundpowerlevel,atermforindicatingthenoisegeneratedbya
source such as a fan or turbine.
RH Relative humidity.
SBV, SBW Steambyvolumeandbyweightinasteam–watermixture,terms
Copyright © 2003 Marcel Dekker, Inc.

used by boiler designers.
scfm, scfh Standard cubic feet per minute or hour, units for flow of gases
at standard conditions of temperature and pressure, namely at
70 F and 29.92in.Hg, or 14.696psia. Sometimes 60 F and
(cid:2) (cid:2)
14.696psia is also used. The ratio of scfm at 70 F to scfm at
(cid:2)
60 F is 1.019.
(cid:2)
SCR Selective catalytic reduction.
SNCR Selective noncatalytic reduction.
SPL Soundpressurelevel,aunitofmeasurementofnoiseindecibels.
SSU Seconds, Saybolt Universal; a unit of kinematic viscosity of
fluids.
SVP Saturatedvaporpressure,pressureofwatervaporinamixtureof
gases.
TSR Theoretical steam rate, a term indicating the theoretical
consumption of steam to generate a kilowatt of electricity in a
turbine in lb=h.
UHC Unburned hydrocarbon.
VOC Volatile organic compound.
Copyright © 2003 Marcel Dekker, Inc.
