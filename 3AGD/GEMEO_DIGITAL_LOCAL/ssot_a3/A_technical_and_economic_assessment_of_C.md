# A_technical_and_economic_assessment_of_C

**Fonte**: A_technical_and_economic_assessment_of_C.pdf  
**Data de conversão**: 2025-07-30 15:14:28  
**Origem**: base_relevantes

---

Carnegie Mellon University
A Technical and Economic Assessment of
CO Capture Technology for
2
IGCC Power Plants
A Dissertation
Submitted in Partial Fulfillment of the Requirements
for the Degree of
Doctor of Philosophy
in
Engineering and Public Policy
by
Chao Chen
Pittsburgh, Pennsylvania
December 2005

ABSTRACT
As an emerging technology for electric power generation, Integrated Gasification
Combined Cycle (IGCC) power plants are of increasing interest because of their potential
advantage for CO capture in addition to conventional pollution control. To further
2
explore this technology, this thesis develops a general modeling framework to provide
tools for assessing gasification-based energy conversion systems with various CO
2
capture options on a systematic and consistent basis.
Many factors influence the performance and cost of an IGCC power plant.
Simulation studies of an oxygen-blown Texaco quench gasifier system with a water gas
shift (WGS) reactor and Selexol CO capture unit indicated that the CO avoidance cost
2 2
is lowest when the CO removal efficiency is in the range of 85%-90%. The overall cost
2
of IGCC systems with and without CO and storage varied significantly with coal quality
2
and plant size (among other factors). For low rank coals (sub-bituminous and lignite)
costs increased significantly relative to the nominal case with bituminous coal. It was also
found that larger IGCC plants have slightly higher thermal efficiency and lower capital
cost. Without incentive financing, however, an IGCC power plant without CO capture
2
was found to be less competitive (more costly) than PC and NGCC power plants in terms
of both the total capital requirement and cost of electricity production. However, IGCC
plants with CO capture were competitive with PC and NGCC capture plants without
2
incentive financing.
This thesis also provides an overview of available options and decisions factors for
using IGCC technology to repower aging PC power plants. Studies in this thesis show
- i -

that IGCC repowering is less capital intensive than greenfield plants, but the feasibility of
repowering is very site-specific. Under suitable conditions, IGCC repowering may be an
economically attractive option for existing PC plants.
This thesis also attempts to characterize key uncertainties affecting the performance
and cost of IGCC systems with CO capture through data mining and Monte Carlo
2
simulation. Most of the capital cost uncertainty in an IGCC capture plant comes from the
IGCC process, rather than the CO capture process. Considering the historical variability
2
of capacity factor and coal price for large U.S. coal plants, the COE of an IGCC capture
plant may be higher than the expected value based on typical deterministic assumptions.
This thesis also presents preliminary evaluations of IGCC systems using two
advanced technologies, the Ion Transport Membrane (ITM) system for oxygen
production and the GE H-class gas turbine system for power generation. Study results
show that these two technologies can significantly improve the competitiveness of IGCC
systems and will influence the application of IGCC technologies in the near future.
- ii -

ACKNOWLEDGEMENTS
This thesis was written with the generous contributions of time, advice, patient
guidance and support of many people.
First, I would like to express my gratitude to my thesis advisor, Prof. Edward S.
Rubin, for his unwavering support. He met with me for countless hours to lead me
carefully towards the creation of a final piece of work. His expertise, vast knowledge,
understanding, patience and kindness added considerably to my graduate experience, and
truly made a difference in my life. I doubt that I would ever be able to convey my
appreciation fully, but I owe him my eternal gratitude.
I would like to thank the members of my committee, Professors Jay Apt, Howard J.
Herzog, and Allen L. Robinson, for their constant encouragement and feedback at all
levels of this research project. Their inputs were very helpful in fulfilling the objectives
of this research.
I also want to acknowledge the extensive contributions of the entire IECM team.
My special thanks go to Mike Berkenpas for his never-ending assistance in computer
modeling, and technical writing, and to Connie Zaremsky for her tremendous input and
help in the manuscript editing during the stressful writing-up period. I would also like to
thank Anand Rao and Sean McCoy, two PhD students in our team, for our exchanges of
knowledge, skills, and venting of frustration during my graduate program, which
enriched my experience. I would like to thank the entire Department of Engineering and
Public Policy which provided a friendly and warm environment. I am especially thankful
- iii -

to Gloria Blake, Elizabeth Ganley and Victoria Finney for their help. Thank you all,
without you all, life would have been very difficult.
I would also like to thank my whole family for the support they provided me
through my entire life and in particular, I must acknowledge my wife, Li Li, without
whose love, encouragement and support, I would not have finished this thesis.
This research was supported by the Carnegie Mellon Electricity Industry Center
(CEIC) and the U.S. Department of Energy National Energy Technology Laboratory
(DOE/NETL).
- iv -

TABLE OF CONTENTS
ABSTRACT ............................................................................................................................................I
ACKNOWLEDGEMENTS.......................................................................................................................III
TABLE OF CONTENTS.............................................................................................................................V
LIST OF FIGURES.................................................................................................................................VIII
LIST OF TABLES......................................................................................................................................XI
NOMENCLATURE................................................................................................................................XIV
CHAPTER 1. INTRODUCTION.........................................................................................................22
1.1. CLIMATE CHANGE AND CO 2 EMISSIONS............................................................................22
1.2. IGCC—A PROMISING TECHNOLOGY FOR CO 2 EMISSION CONTROL...................................24
1.3. RESEARCH MOTIVATION AND OBJECTIVES........................................................................25
REFERENCES (CHAPTER 1).................................................................................................................27
CHAPTER 2. THE ROLE OF IGCC POWER PLANTS FOR ABATING CO EMISSIONS......28
2
2.1. OVERVIEW OF IGCC SYSTEM...........................................................................................28
2.2. MAJOR COMPONENTS OF AN IGCC SYSTEM......................................................................30
2.2.1. Coal handling equipment.................................................................................................31
2.2.2. Gasification technology and gasifier...............................................................................31
2.2.3. Air Separation Unit (ASU)...............................................................................................44
2.2.4. Syngas cooling.................................................................................................................46
2.2.5. Syngas clean-up...............................................................................................................47
2.2.6. Combined cycle power unit..............................................................................................49
2.3. LITERATURE REVIEW OF CO 2 CAPTURE FROM IGCC SYSTEMS.........................................51
REFERENCES (CHAPTER 2).................................................................................................................56
CHAPTER 3. PERFORMANCE AND ECONOMIC SIMULATION MODEL OF IGCC
SYSTEMS.......................................................................................................................59
3.1. MODEL DESIGN BASIS.......................................................................................................59
3.1.1. Gasification technology selection....................................................................................61
3.1.2. Air separation unit...........................................................................................................61
3.1.3. Syngas clean up system....................................................................................................62
3.1.4. Gas turbine selection and steam cycle design..................................................................63
3.2. MAJOR PROCESS SECTIONS OF THE IGCC MODEL.............................................................64
3.2.1. Coal slurry preparation and gasification flowsheet........................................................65
3.2.2. Low temperature gas cooling and clean up.....................................................................70
3.2.3. H S capture and sulfur recovery section..........................................................................76
2
3.2.4. Clean syngas saturation, expend, and reheat section......................................................81
3.2.5. Gas turbine section..........................................................................................................83
3.2.6. Steam cycle section..........................................................................................................88
3.2.7. Convergence sequence of the IGCC model......................................................................95
3.3. IGCC COST MODEL..........................................................................................................96
3.3.1. Oxidant Feed Section.......................................................................................................97
3.3.2. Coal Handling Section and Slurry Preparation...............................................................99
3.3.3. Gasification Section.......................................................................................................100
3.3.4. Low temperature gas cooling.........................................................................................101
3.3.5. Selexol Section...............................................................................................................102
3.3.6. Claus sulfur recovery Section........................................................................................103
3.3.7. Beavon-Stretford Tail Gas Removal Section..................................................................103
3.3.8. Boiler Feedwater System...............................................................................................104
- v -

3.3.9. Process Condensate Treatment......................................................................................105
3.3.10. Gas Turbine Section.......................................................................................................105
3.3.11. Heat Recovery Steam Generator....................................................................................106
3.3.12. Steam Turbine................................................................................................................107
3.3.13. General Facilities..........................................................................................................108
3.3.14. Total Capital Requirement of IGCC systems.................................................................108
REFERENCES (CHAPTER 3)...............................................................................................................113
CHAPTER 4. PERFORMANCE AND COST MODEL OF WATER GAS SHIFT REACTION
SYSTEM.......................................................................................................................115
4.1. INTRODUCTION...............................................................................................................115
4.2. EFFECTS OF OPERATION TEMPERATURE AND TWO-STAGE SHIFT REACTION SYSTEM.......116
4.3. CLEAN SHIFT CATALYSTS...............................................................................................117
4.4. SULFUR TOLERANCE SHIFT CATALYSTS..........................................................................119
4.5. PERFORMANCE MODEL OF THE WATER-GAS SHIFT REACTION PROCESS...........................120
4.5.1. Input and output parameters of the WGS performance model.......................................123
4.5.2. Performance model output.............................................................................................123
4.6. COST MODEL OF WGS REACTION PROCESS.....................................................................129
4.6.1. Process facility cost.......................................................................................................129
4.6.2. Total capital requirement of WGS reaction system.......................................................133
REFERENCES (CHAPTER 4)...............................................................................................................134
CHAPTER 5. PERFORMANCE AND COST MODEL OF SELEXOL PROCESS FOR CO
2
CAPTURE....................................................................................................................135
5.1. INTRODUCTION TO THE SELEXOL ABSORPTION PROCESS................................................135
5.2. SELEXOL SOLVENT PROPERTY........................................................................................137
5.3. TECHNICAL OVERVIEW SELEXOL PROCESS FOR ACID GAS REMOVAL.............................140
5.3.1. Selexol process for selective H S removal.....................................................................141
2
5.3.2. Selexol process for H S and CO removal.....................................................................142
2 2
5.3.3. An optimal design for Selexol process for sulfur and CO capture from IGCC systems143
2
5.4. PERFORMANCE MODEL OF SELEXOL PROCESS................................................................147
5.4.1. Performance model of Selexol process for CO capture................................................148
2
5.4.2. Power consumption model of Selexol process...............................................................157
5.5. COST MODEL OF THE SELEXOL PROCESS.........................................................................162
5.5.1. Process facility costs of the Selexol system for CO capture.........................................162
2
5.5.2. Total Capital Requirement of the Selexol process.........................................................169
REFERENCES (CHAPTER 5)...............................................................................................................171
CHAPTER 6. GREENFIELD IGCC POWER PLANT WITH AND WITHOUT CO CAPUTRE
2
.......................................................................................................................................172
6.1. THE EFFECTS OF COAL TYPES ON IGCC PERFORMANCE..................................................173
6.2. EFFECTS OF CO 2 CAPTURE EFFICIENCY...........................................................................181
6.3. EFFECTS OF PLANT SIZE..................................................................................................188
6.4. FINANCE ANALYSIS OF IGCC SYSTEMS..........................................................................190
REFERENCES (CHAPTER 6)...............................................................................................................199
CHAPTER 7. IGCC REPOWERING WITH CO CAPTURE.......................................................200
2
7.1. IGCC REPOWERING OPTIONS..........................................................................................201
7.1.1. Site Repowering.............................................................................................................201
7.1.2. Feedwater heating repowering......................................................................................202
7.1.3. Boiler windbox repowering............................................................................................202
7.1.4. Heat recovery repowering.............................................................................................203
7.1.5. Evaluation of repowering options..................................................................................203
7.2. DECISION FACTORS FOR IGCC REPOWERING..................................................................204
- vi -

7.3. HEAT RECOVERY REPOWERING DESIGN..........................................................................206
7.4. IGCC REPOWERING ECONOMIC AND PERFORMANCE ANALYSIS......................................211
REFERENCES (CHAPTER 7)...............................................................................................................216
CHAPTER 8. PERFORMANCE AND COST UNCERTAINTY ANALYSIS OF IGCC SYSTEMS
.......................................................................................................................................217
8.1. METHODOLOGY FOR UNCERTAINTY ANALYSIS...............................................................218
8.2. PROBABILITY DISTRIBUTION ESTIMATION OF UNCERTAINTY PARAMETERS.....................219
8.2.1. Data visualization..........................................................................................................220
8.2.2. Probability distribution selection...................................................................................220
8.2.3. Distribution functions of uncertain parameters.............................................................222
8.3. UNCERTAINTY ANALYSIS RESULTS.................................................................................226
REFERENCES (CHAPTER 8)...............................................................................................................231
CHAPTER 9. IGCC SYSTEMS WITH ADVANCED TECHNOLOGIES....................................233
9.1. ION TRANSPORTATION MEMBRANE (ITM)-BASED AIR SEPARATION UNIT....................234
9.2. GE H-CLASS TURBINES...................................................................................................237
9.3. IGCC SYSTEMS WITH ITM OXYGEN PRODUCTION..........................................................239
9.3.1. ITM performance model................................................................................................239
9.3.2. IGCC designs with ITM air separation..........................................................................243
9.4. IGCC SYSTEMS USING GE H TURBINE............................................................................248
9.5. IGCC SYSTEM WITH ITM AND H TURBINE.....................................................................250
REFERENCES (CHAPTER 9)...............................................................................................................253
CHAPTER 10. CONCLUSION............................................................................................................254
10.1. MODEL DEVELOPMENT...................................................................................................254
10.2. MODEL APPLICATIONS....................................................................................................255
10.2.1. Greenfield IGCC plants.................................................................................................255
10.2.2. IGCC Repowering..........................................................................................................257
10.2.3. Uncertainty analysis of IGCC systems...........................................................................258
10.2.4. IGCC with advanced technologies.................................................................................258
10.3. SOME CONSIDERATIONS ABOUT FUTURE WORK..............................................................259
APPENDIX A. CO CONVERSION EFFICIENCY OF THE WGS REACTION...........................261
APPENDIX B. METHODOLOGY FOR CALCULATING THE CATALYST VOLUME OF THE
WGS REACTION........................................................................................................264
REFERENCES (APPENDIX B).............................................................................................................269
APPENDIX C. CALCULATION PROCESS OF THE WGS REACTION SYSTEM....................270
APPENDIX D. CALCULATION PROCESS OF THE SELEXOL SYSTEM FOR CO CAPTURE
2
.......................................................................................................................................276
APPENDIX E. PRELIMINARY DISTRIBUTIONS OF UNCERTAIN PARAMETERS..............284
REFERENCES (APPENDIX E).............................................................................................................290
- vii -

LIST OF FIGURES
FIGURE 2 - 1 SIMPLIFIED PROCESS OF AN IGCC POWER PLANT [BROWN, 2003]....................................30
FIGURE 2 - 2 SIMPLIFIED PROCESS OF THE LURGI DRY-ASH GASIFIER [BROWN, 2003]..........................34
FIGURE 2 - 3 SIMPLIFIED PROCESS OF THE KRW GASIFIER [BROWN, 2003]..........................................38
FIGURE 2 - 4 TEXACO GASIFIER WITH RADIANT SYNGAS COOLERS [BROWN, 2003]..............................41
FIGURE 3 - 1 AN IGCC SYSTEM WITHOUT CO 2 CAPTURE......................................................................60
FIGURE 3 - 2 AN IGCC SYSTEM WITH CO 2 CAPTURE.............................................................................60
FIGURE 3 - 3 SLURRY PREPARATION AND GASIFICATION FLOWSHEET...................................................66
FIGURE 3 - 4 SYNGAS COOLING SECTION FLOWSHEET OF THE REFERENCE PLANT.................................72
FIGURE 3 - 5 SYNGAS COOLING SECTION FLOWSHEET OF THE CAPTURE PLANT.....................................75
FIGURE 3 - 6 SULFUR REMOVAL AND RECOVERY SECTION FLOWSHEET.................................................80
FIGURE 3 - 7 FUEL SATURATION AND REHEAT SECTION FLOWSHEET OF THE REFERENCE PLANT...........82
FIGURE 3 - 8 CO 2 CAPTURE, FUEL SATURATION, AND REHEAT SECTION FLOWSHEET OF THE CAPTURE
IGCC POWER PLANT.........................................................................................................83
FIGURE 3 - 9 GAS TURBINE SECTION FLOWSHEET..................................................................................86
FIGURE 3 - 10 GE 7FA GAS TURBINE AND STEAM CYCLE SECTION FLOWSHEET......................................90
FIGURE 3 - 11 TYPICAL EXHAUST GAS TEMPERATURE PROFILE OF ONE PRESSURE SYSTEM.....................94
FIGURE 3 - 12 TYPICAL EXHAUST GAS/STEAM CYCLE TEMPERATURE PROFILE FOR THREE-PRESSURE
REHEAT HRSG SYSTEM....................................................................................................95
FIGURE 3 - 13 OXYGEN FLOW RATE VS. OXIDANT FEED SECTION COST...................................................98
FIGURE 3 - 14 COAL HANDLING SECTION COST VS. COAL FEED FLOW RATE...........................................100
FIGURE 3 - 15 COAL FLOW RATE VS. GASIFIER COST.............................................................................101
FIGURE 3 - 16 LOW TEMPERATURE GAS COOLING SYSTEM COST VS. THE SYNGAS FLOW RATE..............102
FIGURE 3 - 17 GAS TURBINE COST VS. GAS TURBINE NET OUTPUT.........................................................106
FIGURE 3 - 18 STEAM TURBINE COST VS. STEAM TURBINE NET POWER OUTPUT....................................107
FIGURE 4 - 1 EFFECTS OF TEMPERATURE AND CO/STEAM ON THE CO CONVERSION OF THE WGS
REACTION (THIS FIGURE IS DERIVED BASED ON THAT THE ORIGINAL MOLAR
CONCENTRATION RATIOS OF CO TO H 2 O ARE 1.5, 2, 2.5, AND 3, AND THE ORIGINAL
CONCENTRATIONS OF CO 2 AND H 2 EQUAL ZERO)...........................................................115
FIGURE 4 - 2 TYPICAL CO VARIATION IN HIGH TEMPERATURE SHIFT AND LOW TEMPERATURE SHIFT
CATALYST BEDS [FRANK, 2003A]...................................................................................117
FIGURE 4 - 3 COAL GASIFICATION SYSTEM WITH A CLEAN WATER GAS SHIFT REACTION.....................118
FIGURE 4 - 4 SCHEMATIC PROCESS OF A GASIFIER SYSTEM WITH A SOUR SHIFT...................................120
FIGURE 4 - 5 MASS AND ENERGY FLOW OF THE WATER GAS SHIFT REACTION SYSTEM........................122
FIGURE 5 - 1 CHARACTERISTICS FOR CHEMICAL AND PHYSICAL SOLVENTS [SCIAMANNA, 1988]......138
FIGURE 5 - 2 SELEXOL FLOW DIAGRAM FOR SELECTIVE H 2 S REMOVAL [KUBEK, 2000]....................141
FIGURE 5 - 3 SELEXOL PROCESS FOR SULFUR AND CO 2 REMOVAL [KOHL, 1985]..............................142
FIGURE 5 - 4 OPTIMIZED SELEXOL ABSORPTION PROCESS FOR H 2 S REMOVAL....................................144
FIGURE 5 - 5 OPTIMIZED H
2
S SOLVENT REGENERATION.....................................................................145
FIGURE 5 - 6 OPTIMIZED SELEXOL PROCESS FOR CO 2 ABSORPTION....................................................146
FIGURE 5 - 7 OPTIMIZED SELEXOL REGENERATION THROUGH CO 2 FLASH..........................................147
FIGURE 5 - 8 SIMPLIFIED SELEXOL PROCESS.......................................................................................150
FIGURE 5 - 9 CALCULATION PROCESS FOR THE FLOW RATE OF SELEXOL.............................................155
FIGURE 5 - 10 CALCULATION PROCESS FOR THE OPERATING PRESSURE OF THE SUMP TANK.................157
FIGURE 6 - 1 EFFECT OF WATER PERCENTAGE IN SLURRY ON IGCC PERFORMANCE............................175
FIGURE 6 - 2 EFFECT OF WATER PERCENTAGE IN SLURRY ON TCR AND COE.....................................176
FIGURE 6 - 3 EFFECT OF COAL RANK ON THE EFFICIENCY AND HEAT RATE OF IGCC PLANTS..............178
FIGURE 6 - 4 THE EFFECT OF COAL RANK ON THE TCR AND COE OF IGCC PLANTS (FOR THE COE
CALCULATION, THE COAL PRICE RATIOS BASED ON THE ACTUAL MINE MONTH COAL PRICE
ARE: PITTSBURGH #8: ILLINOIS #6: PRB: ND LIGNITE=1:0.667:0.2:0.265)...................179
FIGURE 6 - 5 RELATIVE OXYGEN AND COAL MASS FLOW RATE PER MWH POWER GENERATION.........180
FIGURE 6 - 6 RELATIVE CO 2 EMISSION FOR PER MWH POWER GENERATION.......................................180
FIGURE 6 - 7 POWER REQUIREMENT AND CAPITAL COST OF SELEXOL PROCESS FOR CO 2 CAPTURE.....182
FIGURE 6 - 8 THERMAL EFFICIENCY OF IGCC POWER PLANTS WITH CO 2 CAPTURE.............................183
- viii -

FIGURE 6 - 9 ENERGY PENALTY FOR CO 2 REMOVAL (THE THERMAL EFFICIENCY OF THE IGCC
REFERENCE PLANT WITHOUT IN THIS CASE IS 0.371).......................................................184
FIGURE 6 - 10 TOTAL CAPITAL COST OF AN IGCC POWER PLANT WITH CO 2 CAPTURE..........................185
FIGURE 6 - 11TOTAL CAPITAL COST INCREASE PERCENTAGE OF IGCC POWER PLANTS WITH CO 2 CAPTURE
(THE TOTAL CAPITAL REQUIREMENT OF THE REFERENCE PLANT IS 1547 $/KW IN THIS
STUDY)...........................................................................................................................185
FIGURE 6 - 12 COE INCREASE PERCENTAGE OF IGCC PLANTS WITH CO 2 CAPTURE (IN THIS CASE, THE
COE OF THE REFERENCE PLANT IS 56 $/MWH)..............................................................186
FIGURE 6 - 13 CO 2 AVOIDANCE COST OF IGCC PLANTS........................................................................187
FIGURE 6 - 14 CO 2 EMISSION RATE OF THE CAPTURE IGCC PLANT.......................................................188
FIGURE 6 - 15 COST OF ELECTRICITY, THERMAL EFFICIENCY AND TOTAL CAPITAL REQUIREMENT OF
DIFFERENT SIZE IGCC PLANTS WITHOUT CO 2 CAPTURE.................................................189
FIGURE 6 - 16 COST OF ELECTRICITY, THERMAL EFFICIENCY, AND TOTAL CAPITAL REQUIREMENT OF
DIFFERENT SIZE IGCC PLANTS WITH CO 2 CAPTURE (THE COE OF THE CAPTURE PLANT
INCLUDES THE CO 2 TRANSPORTATION AND STORAGE COST AT A VALUE OF 10 $/TONNE-
CO )...............................................................................................................................190
2
FIGURE 6 - 17 EFFECT OF PLANT SIZE ON THE CO 2 AVOIDANCE COST...................................................190
FIGURE 6 - 18 TOTAL CAPITAL REQUIREMENT OF THE IGCC AND PC PLANT BASED ON DIFFERENT
CAPITAL STRUCTURES.....................................................................................................195
FIGURE 6 - 19 COST OF ELECTRICITY OF IGCC PLANT WITH DIFFERENT CAPITAL STRUCTURES............196
FIGURE 6 - 20 TOTAL CAPITAL REQUIREMENT OF IGCC AND PC CAPTURE PLANTS UNDER DIFFERENT
CAPITAL STRUCTURES.....................................................................................................196
FIGURE 6 - 21 COE OF IGCC, PC AND NGCC CAPTURE PLANTS WITH DIFFERENT CAPITAL STRUCTURES
.......................................................................................................................................197
FIGURE 7 - 1 ONE-PRESSURE, NON-REHEAT STEAM CYCLE WITH STEAM EXTRACTION FOR FEEDWATER
HEATING.........................................................................................................................207
FIGURE 7 - 2 TWO-PRESSURE, NON-REHEAT STEAM CYCLE WITH STEAM EXTRACTION FOR FEEDWATER
HEATING.........................................................................................................................208
FIGURE 7 - 3 THREE-PRESSURE, REHEAT STEAM CYCLE WITH STEAM EXTRACTION FOR FEEDWATER
HEATING.........................................................................................................................208
FIGURE 7 - 4 IGCC REPOWERING WITH ALL FEEDWATER HEATERS (MINIMUM REPOWERING )............210
FIGURE 7 - 5 IGCC REPOWERING WITH REMOVING SOME FEEDWATER HEATERS (MEDIUM REPOWERING)
.......................................................................................................................................211
FIGURE 7 - 6 IGCC REPOWERING WITHOUT FEEDWATER HEATERS (MAXIMUM REPOWERING CASE)...211
FIGURE 7 - 7 CO 2 AVOIDANCE COST OF IGCC REPOWERING PLANTS (THE GREENFIELD IGCC PLANT
WITHOUT CO 2 CAPTURE IS USED AS THE REFERENCE PLANT TO CALCULATE THE CO 2
AVOIDANCE COST. FULL CAPTURE REFERS TO CO 2 CAPTURE, COMPRESSION, TRANSPORT
AND STORAGE; W/O T&S REFERS TO CO 2 CAPTURE AND COMPRESSION WITHOUT
TRANSPORT AND STORAGE; W/O COMP. REFERS TO CO 2 CAPTURE WITHOUT TRANSPORT,
COMPRESSION AND STORAGE).........................................................................................214
FIGURE 8 - 1 EMPIRICAL CUMULATIVE DISTRIBUTION FUNCTIONS OF THE CAPACITY FACTOR DATA AND
THE DISTRIBUTION OF THE WEIBULL(8.5, 0.81) WITH TRUNC(0, 1).................................224
FIGURE 8 - 2 CENTRAL APPALACHIAN COAL PRICE IN THE NEW YORK MERCANTILE EXCHANGE (THE
ORIGINAL COAL PRICES WERE GIVEN FOR JULY OF EACH YEAR; THE PRICES SHOWN HERE
WERE INFLATION ADJUSTED TO THE DOLLAR VALUE IN 2000)........................................225
FIGURE 8 - 3 COMPARISON OF EMPIRICAL CUMULATIVE DISTRIBUTION FUNCTION OF CENTRAL
APPALACHIAN COAL PRICE DATA WITH THE DISTRIBUTION OF LOGNORMAL(1.169, 0.273)
.......................................................................................................................................226
FIGURE 8 - 4 CUMULATIVE DISTRIBUTIONS OF THE TOTAL CAPITAL REQUIREMENT OF THE IGCC PLANT
(UNC. OF CAP. PROCESS IS GIVEN BY TABLE E-2; UNC. OF IGCC IS GIVEN BY TABLE E-1 IN
APPENDIX E; ALL FACTORS TAKE INTO ACCOUNT THE UNCERTAINTIES FROM TABLE E-1
AND E-2).........................................................................................................................227
FIGURE 8 - 5 CUMULATIVE DISTRIBUTION OF THE COST OF ELECTRICITY OF THE IGCC PLANT...........228
FIGURE 8 - 6 CUMULATIVE DISTRIBUTION OF THE CO 2 AVOIDANCE COST...........................................230
FIGURE 9 - 1 SEPARATION MECHANISM OF MEMBRANE-BASED OXYGEN PRODUCTION [MATHIEU, 2002]
.......................................................................................................................................235
- ix -

FIGURE 9 - 2 PROCESS TEMPERATURE AND OXYGEN PURITY OF DIFFERENT AIR SEPARATION
TECHNOLOGIES [PRASAS, 2002].....................................................................................236
FIGURE 9 - 3 SIMPLIFIED SCHEMATIC PROCESS OF AN ITM UNIT.........................................................240
FIGURE 9 - 4 OVERVIEW OF AN IGCC SYSTEM FULLY INTEGRATING WITH THE ITM OXYGEN
PRODUCTION...................................................................................................................245
FIGURE 9 - 5 OVERVIEW OF AN IGCC SYSTEM WITH STANDALONE ITM OXYGEN PRODUCTION.........246
FIGURE 9 - 6 COMBINED POWER BLOCK CYCLE WITH GE H TURBINE [MATTA, 2000].........................249
- x -

LIST OF TABLES
TABLE 2 - 1 MAJOR MILESTONES OF THE HISTORY OF IGCC DEVELOPMENT (SOURCE: GE WEBPAGE) 29
TABLE 2 - 2 IMPORTANT CHARACTERISTICS OF THREE TYPES OF GASIFIERS [BROWN, 2003]...............42
TABLE 2 - 3 COMPARISON OF PARAMETERS OF GASIFICATION TECHNOLOGIES [U.K. DEPARTMENT OF
TRADE AND INDUSTRY, 1998]..........................................................................................43
TABLE 2 - 4 CLASSIFICATION OF FUEL GASES [FOSTER, 2003].............................................................50
TABLE 3 - 1 STEAM AND GAS PRODUCT LINE STEAM TURBINE THROTTLE AND ADMISSION STEAM
CONDITIONS......................................................................................................................64
TABLE 3 - 2 COAL COMPOSITION AND ITS CORRESPONDING INPUT IN ASPEN PLUS..............................66
TABLE 3 - 3 COAL SLURRY PREPARATION AND GASIFICATION PROCESS UNIT DESCRIPTION.................69
TABLE 3 - 4 SYNGAS COOLING PROCESS UNIT DESCRIPTION OF THE REFERENCE PLANT.......................71
TABLE 3 - 5 SYNGAS COOLING PROCESS UNIT DESCRIPTION OF THE CAPTURE PLANT...........................74
TABLE 3 - 6 SULFUR REMOVAL AND RECOVERY UNIT DESCRIPTION.....................................................79
TABLE 3 - 7 SULFUR REMOVAL AND RECOVERY UNIT DESCRIPTION.....................................................82
TABLE 3 - 8 GAS TURBINE UNIT DESCRIPTION......................................................................................87
TABLE 3 - 9 STAG PRODUCT LINE STEAM TURBINE THROTTLE AND ADMISSION STEAM CONDITIONS..88
TABLE 3 - 10 STEAM CYCLE SECTION UNIT DESCRIPTION.......................................................................91
TABLE 3 - 11 REFERENCES USED FOR UPDATING THE IGCC COST MODEL.............................................96
TABLE 3 - 12 IGCC SYSTEM PROCESS AREAS.........................................................................................97
TABLE 3 - 13 PROCESS CONTINGENCY OF COST SECTIONS....................................................................110
TABLE 3 - 14 CAPITAL COST ELEMENTS OF AN IGCC POWER PLANT....................................................111
TABLE 3 - 15 UNIT COSTS OF CONSUMABLES (SOURCE: IECM MANUAL)............................................112
TABLE 4 - 1 RANGE OF MODEL PARAMETER VALUES FOR THE WGS REACTION SYSTEM....................123
TABLE 4 - 2 INPUT AND OUTPUT PARAMETERS OF THE WGS REACTION SYSTEM...............................123
TABLE 4 - 3 WATER GAS SHIFT REACTOR COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000
[DOCTOR, 1996].............................................................................................................130
TABLE 4 - 4 GAS-LIQUID HEAT EXCHANGER COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000
[DOCTOR, 1996].............................................................................................................131
TABLE 4 - 5 GAS-GAS HEAT EXCHANGER COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000
[DOCTOR, 1996].............................................................................................................132
TABLE 4 - 6 COST PARAMETERS OF WATER GAS SHIFT PROCESS.........................................................133
TABLE 5 - 1 PROPERTY OF GLYCOL SOLVENT.....................................................................................137
TABLE 5 - 2 RELATIVE SOLUBILITY OF GASES IN SELEXOL SOLVENT [DOCTOR, 1994]......................139
TABLE 5 - 3 SOLUBILITY OF GASES IN THE SELEXOL SOLVENT [KORENS, 2002]...............................139
TABLE 5 - 4 INPUT AND OUTPUT PARAMETERS OF SELEXOL MODEL...................................................149
TABLE 5 - 5 SPECIFIC HEAT OF GASES IN THE SYNGAS........................................................................151
TABLE 5 - 6 SOLUTION HEAT (BTU/LB-SOLUTE) OF GASES IN THE SELEXOL.......................................152
TABLE 5 - 7 ABSORBER COST DATA ADJUSTED TO THE DOLLAR VALUES IN 2000 [DOCTOR, 1996]....163
TABLE 5 - 8 POWER RECOVERY TURBINE COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000
[DOCTOR, 1996].............................................................................................................164
TABLE 5 - 9 SUMP TANK COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000 [DOCTOR, 1996]....165
TABLE 5 - 10 RECYCLE COMPRESSOR COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000 [DOCTOR,
1996]..............................................................................................................................165
TABLE 5 - 11 SELEXOL PUMP COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000 [DOCTOR, 1996]166
TABLE 5 - 12 CO 2 COMPRESSOR COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000 [DOCTOR, 1996]
.......................................................................................................................................166
TABLE 5 - 13 CO 2 FINAL COMPRESSOR COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000 [DOCTOR,
1996]..............................................................................................................................167
TABLE 5 - 14 REFRIGERATION UNIT COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000 [DOCTOR,
1996]..............................................................................................................................168
TABLE 5 - 15 FLASH TANK COST DATA ADJUSTED TO THE DOLLAR VALUE IN 2000 [DOCTOR, 1996]...169
TABLE 5 - 16 PARAMETERS FOR TCR OF SELEXOL PROCESS................................................................170
TABLE 6 - 1 TECHNICAL DESIGN ASSUMPTION OF THE IGCC POWER PLANT......................................172
TABLE 6 - 2 ECONOMIC AND FINANCIAL ASSUMPTION OF THE IGCC POWER PLANT..........................172
- xi -

TABLE 6 - 3 COMPOSITIONS OF THE FOUR COALS AND THEIR WATER PERCENTAGE IN SLURRY..........177
TABLE 6 - 4 CAPITAL STRUCTURE OF A TYPICAL POWER PLANT PROJECT (SOURCE: IECM MANUAL) 191
TABLE 6 - 5 CAPITAL STRUCTURES AND COST OF CAPITAL FOR IGCC FINANCING.............................193
TABLE 7 - 1 ECONOMIC AND FINANCIAL ASSUMPTION FOR REPOWERING STUDIES.............................212
TABLE 7 - 2 STUDY RESULTS OF IGCC REPOWERING WITH AND WITHOUT CO 2 CAPTURE..................213
TABLE 8 - 1 STATISTICAL DESCRIPTION OF POWER PLANT CAPACITY FACTOR DATA AND THE FITTED
WEIBULL DISTRIBUTION.................................................................................................223
TABLE 8 - 2 STATISTIC DESCRIPTION OF COAL PRICE DATA AND THE FITTED LOGNORMAL DISTRIBUTION
.......................................................................................................................................225
TABLE 9 - 1 PERFORMANCE CHARACTERISTICS OF H-CLASS AND F-CLASS TURBINES [MATTA, 2000]239
TABLE 9 - 2 RECOMMENDED OPERATING PARAMETERS FOR ITM OXYGEN PROCESS DESIGN [AIR
PRODUCT, 2002].............................................................................................................242
TABLE 9 - 3 DESIGN PARAMETERS OF ITM UNITS IN THE ASPEN SIMULATION MODELS.....................244
TABLE 9 - 4 PERFORMANCE AND COST COMPARISON OF IGCC REFERENCE PLANTS WITH ITM.........247
TABLE 9 - 5 PERFORMANCE AND COST COMPARISON OF IGCC CAPTURE PLANT WITH ITM...............248
TABLE 9 - 6 STEAM CYCLE PARAMETERS OF THE IGCC USING GE H TURBINE..................................249
TABLE 9 - 7 PERFORMANCE AND COST COMPARISON OF IGCC REFERENCE PLANTS USING DIFFERENT
GAS TURBINES.................................................................................................................250
TABLE 9 - 8 PERFORMANCE AND COST COMPARISON OF IGCC CAPTURE PLANTS USING DIFFERENT GAS
TURBINES........................................................................................................................250
TABLE 9 - 9 PERFORMANCE AND COST IMPROVEMENT OF THE IGCC REFERENCE PLANT USING ITM
AND GE 7H TURBINE......................................................................................................251
TABLE 9 - 10 PERFORMANCE AND COST IMPROVEMENT OF THE IGCC CAPTURE PLANT USING ITM AND
GE 7H TURBINE..............................................................................................................252
TABLE C - 1 INPUT PARAMETERS OF THE WGS MODEL......................................................................270
TABLE C - 2 CALCULATION OF THE CO CONVERSION EFFICIENCY IN THE HIGH TEMPERATURE REACTOR
.......................................................................................................................................271
TABLE C - 3 CALCULATION OF THE CO CONVERSION EFFICIENCY IN THE LOW TEMPERATURE REACTOR
.......................................................................................................................................271
TABLE C - 4 SYNGAS COMPOSITIONS FROM THE HIGH TEMPERATURE REACTOR.................................272
TABLE C - 5 SYNGAS COMPOSITIONS FROM THE LOW TEMPERATURE REACTOR..................................273
TABLE C - 6 CALCULATION OF CATALYST VOLUME AND PFC OF THE HIGH TEMPERATURE REACTOR 274
TABLE C - 7 CALCULATION OF CATALYST VOLUME AND PFC OF THE LOW TEMPERATURE REACTOR.274
TABLE C - 8 PROCESS FACILITY COSTS OF THE HEAT EXCHANGERS....................................................275
TABLE D - 1 SELEXOL PROPERTIES FOR CALCULATION.......................................................................276
TABLE D - 2 PROPERTIES OF GASES IN SYNGAS...................................................................................276
TABLE D - 3 COMPOSITION OF SYNGAS BEFORE CO 2 CAPTURE...........................................................277
TABLE D - 4 ASSUMPTION FOR POWER CONSUMPTION CALCULATION................................................277
TABLE D - 5 CO 2 CAPTURE EFFICIENCY AND FLASHING TANK PRESSURES..........................................277
TABLE D - 6 CO 2 CAPTURE AMOUNT REQUIRED BY CAPTURE EFFICIENCY..........................................278
TABLE D - 7 CALCULATING THE FLOW RATE OF SELEXOL SOLVENT...................................................278
TABLE D - 8 CALCULATION OF THE OPERATING PRESSURE OF SUMP TANK.........................................279
TABLE D - 9 CALCULATION THE TEMPERATURE CHANGE OF SELEXOL DUE TO CO 2 RELEASE FROM
FLASH TANK....................................................................................................................279
TABLE D - 10 GASES RETAINED IN THE SOLVENT AT THE FLASH TANK 1..............................................280
TABLE D - 11 GASES RELEASED FROM THE SOLVENT AT THE FLASH TANK 1........................................280
TABLE D - 12 GASES RETAINED IN THE SOLVENT AT THE FLASH TANK 2..............................................280
TABLE D - 13 GASES RELEASED IN THE SOLVENT AT THE FLASH TANK 2..............................................281
TABLE D - 14 GASES RETAINED IN THE SOLVENT AT THE FLASH TANK 3..............................................281
TABLE D - 15 GASES RELEASED IN THE SOLVENT AT THE FLASH TANK 3..............................................281
TABLE D - 16 FINAL PRODUCT OF CO 2 FROM SELEXOL........................................................................281
TABLE D - 17 POWER CONSUMPTION CALCULATION.............................................................................282
TABLE D - 18 PROCESS FACILITY COST OF SELEXOL PROCESS..............................................................283
TABLE E - 1 DISTRIBUTION FUNCTIONS ASSIGNED TO THE PARAMETERS OF THE IGCC PROCESS (THE
DISTRIBUTION FUNCTIONS IN THIS TABLE, EXCEPT THE DISTRIBUTION OF THE FIXED
- xii -

CHARGE FACTOR, MAINLY COME FROM REFERENCE [1] AND WERE UPDATED WITH DATA
FROM REFERENCE [2] AND [3]).......................................................................................284
TABLE E - 2 DISTRIBUTION FUNCTIONS ASSIGNED TO SELEXOL-BASED CO 2 CAPTURE PROCESS........286
TABLE E - 3 DISTRIBUTION FUNCTIONS ASSIGNED TO THE FUEL COST AND CAPACITY.......................286
- xiii -

NOMENCLATURE
α CO 2 removed from the syngas (percent)
ω Selexol flow rate (lb-mole/hr)
ψ CO Solution heat of CO 2 in selexol (Btu/lb solute)
2
η Percentage of the theoretical recovery
η HS H 2 S removal efficiency (%)
η Power recovery turbine efficiency (%)
tur
η Compressor efficiency (%)
comp
η Pump efficiency (%)
pump
γ Ratio of actual to required flow rate of selexol (fraction)
χ Solubility of gas component i in selexol (SCF/gallon-psia)
i
∆T Temperature increase of solvent in the absorber (F)
∆T Selexol temperature change due to heat transfer from syngas (F)
1
∆T Selexol temperature change due to solution heat (F)
2
∆T Selexol temperature difference between the inlet and outlet of the refrigeration
Sel
unit (C )
ξ CO conversion
ξ CO conversion in the high temperature shift reactor
h
ξ CO conversion in the low temperature shift reactor
l
ξ Total CO conversion in the shift reactors
tot
B The amount of debt
C
cat. Capital cost of catalysts (k$ in 2000)
C Specific heat (constant pressure) of selexol (Btu/lb-F)
p,S
- xiv -

C Specific heat (constant pressure) of gas component i (Btu/lb-F)
p,i
C Specific heat (constant volume) of gas component i (Btu/lb-F)
v,i
dP Pressure increase in the pump (psia)
pump
dP Decreased pressure of Selexol in the power recovery turbine (F)
tur
dT Log mean temperature difference in the heat exchanger (C)
HE
dT Decreased temperature of Selexol in the power recovery turbine (F)
tur
dT Increased temperature of CO lean Selexol due to pumping (F)
pump 2
dT Approach temperature in the high temperature reactor (F)
h
dT Approach temperature in the low temperature reactor (F)
l
(dT)
HE1 Log temperature difference in heat exchanger 1 (F)
(dT) Log temperature difference in heat exchanger 2 (F)
HE2
(dT) Log temperature difference in heat exchanger 3 (F)
HE3
F Molar flow rate of air fed into the ITM unit (mole/hr)
F Molar flow rate of permeated oxygen (mole/hr)
perm
f Total molar flow rate of syngas at the inlet of high temperature reactor (lb-
0
mole/hr)
f Total molar flow rate of syngas (fuel) from Selexol process (lb-mole/hr)
fuel
f Flow rate of gas captured in Selexol (lb-mole/hr)
gas
f Flow rate of Selexol (gal/min or lb-mole/hr)
Sel
f Total flow rate of syngas entering the absorber (lb-mole/hr)
SG,i
f Total molar flow rate of syngas from the exit of heat exchanger 2 (lb-mole/hr)
SG,HE2,o
f Water molar flow rate entering heat exchanger 1 (lb-mole/hr)
water
- xv -

H Total dynamic pressure head of a turbine or pump (psia)
s
hp Power consumption of compressor (hp)
comp
hp Power consumption of pump (hp)
pump
hp Power recovered through the power turbine (hp)
tur
hp Power consumption of the recycle compressor (hp)
RC
hp Power consumption of the Selexol pump (hp)
SP
h
T Enthalpy of water at the saturation temperature (Btu/lb-mole)
satt.
h Enthalpy of water at the inlet of heat exchanger 1 (Btu/lb-mole)
T
0
K Reaction equilibrium constant
k Specific heat capacity ratio of gas (C /C )
gas p v
K Shift reaction equilibrium constant in the high temperature reactor with taking
h
accounting of the approach temperature
K Shift reaction equilibrium constant in the high temperature reactor without
k,real
taking accounting of the approach temperature
K Shift reaction equilibrium constant in the low temperature reactor with taking
l
accounting of the approach temperature
K Shift reaction equilibrium constant in the low temperature reactor without
l,real
taking of the approach temperature
k Reaction rate constant
M Total molar flow rate of syngas through the sulfur removal system (lb-
syn,S,i
moles/hr)
MW Selexol molecular weight (lb/lb-mole)
S
N Operating train number of the sump tanks
O,slump
N Operating train number of the refrigeration unit
O,reft
- xvi -

N Operating train number of flash tank
O,tank
N Operating train number of the heat exchanger
O,HE
N Number of operating sulfur removal absorber vessels
O,S
N Operating train number of reactor
O,R
N Operating train number of heat exchanger 1
O,HE1
N Operating train number of heat exchanger 2
O,HE2
N Operating train number of heat exchanger 3
O,HE3
N Total train number of the refrigeration unit
T,reft
N Total train number of flash tank
T,tank
N Total train number of sump tanks
T,sump
N Total train number of the heat exchanger
T,HE
N Total number of sulfur removal absorber vessels (operating plus spares)
T,S
N Train number of absorbers
T,abso
N Total train number of reactor
T,R
N Total train number of heat exchanger 1
T,HE1
N Total train number of heat exchanger 2
T,HE2
N Total train number of heat exchanger 3
T,HE3
P Syngas pressure at the inlet of high temperature reactor (psia)
0
P Inlet pressure of absorber (atm)
abso.,i
P Pressure of permeated oxygen (psia)
perm
P Total pressure at the outlet of recovery turbine #1 (psia)
o,1
- xvii -

P Total pressure at the outlet of recovery turbine #2 (psia)
o,2
P Inlet pressure of compressor (psia)
comp,i
P Outlet pressure of compressor (psia)
comp,o
P Partial pressure of gas component i (psia)
i
P Outlet pressure of the turbines (atm)
tur,o
P Pressure of syngas entering the heat exchanger (atm)
HE
P
HE2 Pressure at heat exchanger 2 (atm)
P
R Pressure in the shift reactor (atm)
P
sc Steam cycle pressure (psia)
PFC Process facility cost of the absorber (US k$ in 2000)
avso
PFC Process facility cost of power recovery turbine (US k$ in 2000)
tur
PFC Process facility cost of sump tank (US k$ in 2000)
sump
PFC Process facility cost of the recycle compressor (US k$ in 2000)
RC
PFC Process facility cost of the Selexol pump (US k$ in 2000)
SP
PFC Process facility cost of the CO compressor (US k$ in 2000)
comp1 2
PFC Process facility cost of the compressor (US k$ in 2000)
comp2
PFC Process facility cost of the refrigeration unit (US k$ in 2000)
refr
PFC Process facility cost of flash tanks (US k$ in 2000)
tank
PFC Process facility cost of the heat exchanger (US k$ in 2000)
HE
PFC
R Process facility cost of shift reactor (k$ in 2000)
PFC
HE1 Process facility cost of heat exchanger 1
- xviii -

PFC
HE2 Process facility cost of heat exchanger 2
PFC
HE3 Process facility cost of heat exchanger 3
Q Heat released from the syngas to the solvent (Btu/hr)
1
Q Heat load of the exchangers (kW), 1200~96000 /train
HE
Q Heat exchanged in heat exchanger 1 (Btu/hr or kW)
HE1
Q Heat exchanged in heat exchanger 2 (Btu/hr or kW)
HE2
Q Heat exchanged in heat exchanger 3 (Btu/hr or kW)
HE3
q Heat released in heat exchanger 1 by per lb-mole syngas (Btu/lb-mole)
HE1
q Heat released in heat exchanger 2 by per lb-mole syngas (Btu/lb-mole)
HE2
q Heat absorbed in heat exchanger 3 by per lb-mole feed water (Btu/lb-mole)
HE3
R Overall recovery of the ITM unit
R Theoretical overall recovery of the ITM unit
T
r Cost of debt (borrowing rate)
B
r Cost of equity
S
r Average cost of capital after tax for the project
WACC
S Amount of equity
SV Space velocity in a reactor (1/hr)
T
0 Temperature of syngas at the inlet of high temperature reactor (F)
T Tax rate
C
T Evaporation temperature of refrigerant (F)
evap
T Syngas temperature at the inlet of the absorber (F)
SG,i
T Syngas temperature at the outlet of the absorber (F)
SG,o
- xix -

T Temperature of syngas exiting the heat exchanger 2 (F)
HE2,o
T Equilibrium temperature in the high temperature reactor (F)
h
T
l Equilibrium temperature in the low temperature reactor (F)
T Temperature of saturation water (F)
sat.
T Temperature of syngas at the inlet of heat exchanger 3 (F)
SG,HE3,i
T Temperature of water at the exit of heat exchanger 3 (F)
wat.,HE3,o
V Catalyst volume (ft3)
cat.
V High temperature catalyst volume (ft3)
cat.,h
V Low temperature catalyst volume (ft3)
cat.,l
V Volume flow rate of residual CO in the lean solvent (lb-mole/hr)
CO ,res 2
2
V Volume flow rate of CO captured in the absorber (lb-mole/hr)
CO ,abs 2
2
V Volume flow rate of gas component i captured by Selexol (SCF/hr)
i
v Specific volume of CO (SCF/lb-mole)
i 2
VF Volumetric flow rate of syngas (ft3/hr)
VF Volume flow rate of gas (ft3/min)
gas
W Sulfur removal equipment power consumption (kW)
e,S
W Power consumption of solvent refrigeration process (kW)
ref.
x Molar concentration of oxygen in the air
feed
y
[y] Molar concentration of species in syngas
y
[y] Molar concentration of species in syngas entering the high temperature
0
reactor
- xx -

y
[y] Molar concentration of species in syngas exiting the high temperature
h,o
reactor
y
[y] Molar concentration of species in syngas exiting the low temperature
l,o
reactor
- xxi -

Chapter 1. INTRODUCTION
1.1. Climate change and CO emissions
2
Global climate change, a widely discussed topic in environmental studies,
represents a potentially serious threat to natural ecosystems, and to the quality of human
life on earth. Studies predict that the adverse consequences of climate change induced by
human activities will include some of the following in the future [World Energy
Assessment, 1999]:
• The average temperature of the global surface air will increase by 1.0~3.5°C
during this century.
• The global mean sea level is likely to rise by about 6cm per decade during this
century, mainly due to the thermal expansion of the ocean and the melting of
some land ice.
• Even though food production may increase in some areas, the high likelihood of
its decrease in other areas, especially in the tropics and subtropics, will bring
hardship to large segments of population.
• Fast climatic changes may result in the instability of ecosystems, causing natural
disasters such as floods and droughts.
• Some diseases currently contained within certain areas may spread further to
threaten new populations.
To minimize the impacts of climate change, it is important to pinpoint and eliminate
factors responsible for this phenomenon. It is well-known that a number of gases, such as
22

carbon dioxide, ozone, methane, nitrous oxide and CFCs in the atmosphere, induce the
greenhouse effect that drives global climate change. The contribution of carbon dioxide
is, however, dominant because of two reasons. First, the concentration of this gas is
already higher than other greenhouse gases in the atmosphere, and, second, human
activity on earth today is adding carbon dioxide to the atmosphere at historically
unprecedented rates.
The recent increase in the atmospheric concentration of carbon dioxide has resulted
from the large scale utilization of fossil fuels in modern times. Since the onset of the
industrial revolution, for instance, 296 gigatonnes of carbon from fossil fuels have been
released to the atmosphere, raising carbon dioxide concentration from 280ppm to
360ppm [World Energy Assessment, 1999].
At present, fossil fuels fulfill about 84.8% of the world’s primary energy
consumption needs [International Energy Annual 1999], and in the foreseeable future,
fossil fuels will still be the major energy source. Estimates indicate that the world’s fossil
fuel reserves contain approximately 6600 gigatonnes of carbon, with 5200 gigatonnes of
carbon in coal alone. In the absence of adequate measures to control the emissions of
carbon dioxide from these sources, the atmospheric concentration of carbon dioxide
could more than double by the end of this century [World Energy Assessment, 1999].
Concerns about the greenhouse effect call for new strategies regarding the use of coal to
reduce the emission of carbon dioxide into the atmosphere. The task of reducing carbon
dioxide emissions without abruptly cutting off the utilization of fossil fuels, however,
presents a serious challenge. The following section discusses some methods for facing
this challenge.
23

1.2. IGCC—a promising technology for CO emission control
2
As the most carbon-intensive and most abundant fossil fuel, coal is traditionally
utilized through combustion. Coal combustion plants produce flue gas streams consisting
mostly of nitrogen (from combustion air), with diluted concentrations of CO .
2
Technologies have been developed to capture CO with low partial pressure from flue gas
2
stream, but the energy and economic performance of coal combustion power plants
would be degraded substantially. Post-combustion CO capture from coal combustion
2
plants would nearly double the cost of electricity (COE), and reduce their net output by
about 25-30% [Parson, 1998; Doctor, 1994; McCarthy, 1985]. Although oxyfuel can
make CO capture from coal combustion power plant much cheaper, the expensive
2
oxygen production required adds significantly to the overall plant cost. For these reasons,
there is growing interest in Integrated Gasification Combustion Cycle (IGCC) systems as
an alternative.
Gasification offers a way of converting coal to a gaseous state where it can be
cleaned and burnt in a gas turbine. CO emissions can be prevented in a gasification
2
power plant by transferring almost all carbon compounds to CO through the water gas
2
shift reaction, and then removing the CO before it is diluted in the combustion stage.
2
Hence, CO removal from IGCC requires considerably smaller and simpler process
2
equipment than the post-combustion CO removal [Herzog, 1999; Herzog, 1997].
2
Therefore, compared to coal combustion plants, IGCC power plants provide an option for
CO capture with relatively low cost and small energy losses.
2
In addition, IGCC systems are of interests to governments and utility companies in
many countries for other reasons. For example, the United Stated government may be
24

interested in developing reliable and cost effective IGCC systems for generating power
using its abundant coal reserves in order to reduce US dependence on foreign energy
sources.
1.3. Research motivation and objectives
As a new emerging coal-based technology, IGCC systems are becoming an
increasingly attractive option to limit CO emissions and other pollutants relative to
2
conventional coal power plants.
A number of previous studies have reported cost and performance results for IGCC
systems with CO capture [Michael, 1997; OLeefe, 2000; Doctor, 1997]. However, there
2
are no generally available process models that can be used or modified for studying
options of CO removal from IGCC systems in detail. Currently reported cost data also
2
are relatively limited and often incomplete, and uncertainties are seldom considered.
This research, therefore, is motivated by a desire to have a better understanding of
the technological options for CO capture from IGCC systems and their effects on the
2
performance and cost of IGCC systems. Some key research questions which need to be
addressed include: What kind of technologies may be used for CO capture? What are the
2
key parameters that affect the performance and the cost of IGCC systems with and
without CO capture? What are the uncertainties associated with IGCC system? How will
2
CO capture influence the future development and application of IGCC systems? How
2
will IGCC systems and CO capture benefit from developing technologies?
2
With these objectives in mind, this thesis develops a general framework to assess
the range of options for CO capture from IGCC power systems. In this general
2
25

framework, energy and economic models are developed to simulate the performance and
costs of IGCC systems with and without CO capture under different scenarios. Both new
2
and retrofit (repowering) applications of IGCC systems with and without CO capture are
2
studied. The thesis also characterizes key uncertainties affecting performance and costs.
It also assesses process design improvements and technology development trends that
offer the potential to reduce the cost of IGCC power generation with CO capture.
2
Through evaluating and comparing various IGCC power plant configurations in terms of
the cost, performance, and uncertainty, this thesis provides a method for systemic
comparison of IGCC options with and without CO capture.
2
26

REFERENCES (CHAPTER 1)
1. Doctor R.D., Molburg J.C., Thimmapuram P.R., 1997: Oxygen-Blown Gasification
Combined Cycle: Carbon Dioxide Recovery, Transport, and Disposal. Energy
Convers. Mgmt. Vol. 38, Suppl.
2. Doctor R.D., etc., 1994: Gasification combined cycle: carbon dioxide recovery,
transport, and disposal, ANL/ESD-24
3. Herzog H, 1999: An Introduction to CO Separation and Capture Technologies.
2
Cambridge, U.S.A: MIT Energy Laboratory Working Paper; 1999
4. Herzog H and Drake E., 1997: CO capture, reuse, and storage technology for
2
mitigating global climate change: A White Paper. DOE order #DE-AF22-96PC01257,
1997
5. International Energy Annual 1999, Energy information Administration, U.S.
6. Keith DW and Morgan MG, 2000: Industrial carbon management: a review of the
technology and its implications for climate policy, Elements of Change 2000, Aspen
Global Change Institute
7. McCarthy, C.B., and Clark W.N., 1985: Integrated gasification/combined cycle
(IGCC) electric power production-A rapidly emerging energy alternative. Presented at
symposium on coal gasification and synthetic fuels for power generation, San
Francisco, CA
8. OLeefe. L.F., Griffiths J., 2000: A single IGCC design for variable CO capture, 2000
2
Gasification technologies conference, San Francisco, California, Oct. 2000
9. Parson EA, Keith DW, 1998: Climate change - Fossil fuels without CO emissions,
2
SCIENCE, 282 (5391) NOV 6, 1998
10. World Energy Assessment, 1999: Energy and the challenge of sustainability,
http://www.undp.org/seed/eap/activities/wea/drafts-header.html
27

Chapter 2. THE ROLE OF IGCC POWER PLANTS FOR ABATING CO
2
EMISSIONS
This section discusses the potential role of IGCC power plants for abating CO
2
emissions. As the first step, it presents a brief introduction to gasification and IGCC
technology, starting with a generalized overview of IGCC systems. This is followed with
detailed descriptions of major IGCC components, including the air separation unit, coal
preparation facility, gasifier, syngas cooling unit, basic syngas cleanup options, and
combined cycle power block. Then the expected advantages of IGCC for abating CO
2
emissions are discussed, along with technologies that can be incorporated into IGCC
systems for CO capture, and the process designs for IGCC systems with CO capture.
2 2
2.1. Overview of IGCC system
IGCC is an innovative electric power generation system that combines modern coal
gasification technologies with both gas turbine (Brayton cycle) and steam turbine
(Rankine cycle) technologies, and offers an exceptionally clean, flexible and cost-
efficient way to generate electricity. The gasification system converts coal or other solid
or liquid feed stocks such as petroleum coke or heavy oils into a gaseous syngas, which is
mainly composed of hydrogen (H ) and carbon monoxide (CO). The combustible syngas
2
is used to fuel a combined cycle generation power block to produce electricity.
The first commercial IGCC plants were put into service in 1980 in the U.S. through
DOE’s cooperative Clean Coal Technology (CCT) program. Through the rapid
development in recent 20 years, IGCC is now considered as a mature technology and a
viable coal power plant option. So far, four IGCC power plants have been commercially
running, and other IGCC projects are being planned. All these IGCC projects have
28

achieved, or are expected to achieve the lowest levels of criteria pollutant air emissions
(NOx, SOx, CO, PM10) among any coal-fueled power plants in the world [Brown, 2003].
Table 2-1 represents the major milestones during the course of IGCC development
history.
Table 2 - 1 Major milestones of the history of IGCC development (source: GE
webpage)
Time Events
1887 The first patent for a gasifier was granted to Lurgi GmbH in Germany.
1940 Commercial coal gasification to provide cities with gas for streetlights and domestic
consumption became common in Europe and the United States.
1950 The chemical industry began using gasification to make chemicals such as ammonia
and fertilizers. However, the feedstock was mostly crude oils rather than coal.
1970 The U.S. Department of Energy funded various studies to evaluate the feasibility of
gasifying coal and using syngas as a gas turbine fuel. These studies showed good
economics.
1980 Coolwater was commissioned in 1984, which demonstrated the feasibility of IGCC.
1996 Polk Tampa Electric plant was built, which successfully used nitrogen injection for
NOx control and demonstrated the commercial feasibility of IGCC technology,
Wabash River IGCC repowering plant began operation.
2000 Exxon Singapore plant was built, which employs the widest variety of gas turbine
fuels and operability range.
Present IGCC is now considered a mature technology and a viable coal power plant option.
A general figure of the major processes of an IGCC power plant is given by Figure
2-1. The first part of the IGCC process involves the chemical conversion of coal into
syngas, a mixture of mostly hydrogen and carbon monoxide. This conversion is carried
out in a gasifier, using very high temperature and only a limited amount of oxygen. When
the syngas leaves the gasifier, it must be cleaned of any particulates and other
contaminants such as sulfur, so that it can be used as a fuel for gas turbines for power
generation. After the syngas is cleaned, it is fed into a gas turbine, which turns an electric
generator to produce electric power. In addition, the hot exhaust gas from the gas turbine
29

flows into a heat recovery steam generator (HRSG) for steam production, which turns a
steam turbine that drives another electric generator to generate power.
Figure 2 - 1 Simplified process of an IGCC power plant [Brown, 2003]
2.2. Major components of an IGCC system
The major components of IGCC power plants, as shown in Figure 2-1, include the
coal handling facility, gasifier, air separation unit, syngas cooling process, syngas clean-
up processes, and combined cycle power block. Most of the components of IGCC power
plants are associated with processes that have been already widely used in the power,
petroleum refining, and chemicals industries. The following sections describe each of
these components.
30

2.2.1. Coal handling equipment
The coal handling facility is employed to unload, convey, prepare, store and feed
coal delivered to an IGCC power plant. Generally, the coal handling facility used for an
IGCC plant can be divided into five sections: unloading unit, feeding unit, crushing and
screening unit, stacking and reclaiming unit, and bunker [Joshi, 2000], which is largely
the same as that used at PC power plants.
2.2.2. Gasification technology and gasifier
The gasification process is the heart of an IGCC plant. The process is a partial
oxidation process which converts many carbon-based fuels, including most grades of
coal, into a synthesis gas (syngas). The fuel is fed into a pressurized vessel, which
contains controlled and limited amounts of oxygen or air and steam or water. The
chemistry of coal gasification reactions is quite complex. The basic conversion
procedures are as in the following. Rising temperature in the gasifier initiates
devolatilization and breaking of weaker chemical bonds to yield tars, oils, phenols and
hydrocarbon gases. The fixed carbon that remains after devolatilization is gasified
through reactions with O , steam, CO , and H The heat produced by the partial
2 2 2.
oxidation provides most of the energy required to break chemical bonds in the feedstock,
and increases the products to the reaction temperature, and drives endothermic
gasification reactions [Rubin, 1989]. These reactions further produce the final syngas.
Syngas is a mixture of mainly hydrogen and carbon monoxide, with a small fraction of
CO . A small amount of methane may also be present. Methane formation is a highly
2
exothermic reaction and does not consume oxygen and, therefore methane amount is
relatively higher in lower-temperature systems, and methane formation increases the
31

efficiency of gasification and the final heating value of the syngas [O’Brien, 2004].
Overall, about 70% of the feed fuel’s heating value is associated with the CO and H
2
components of the gas [O’Brien, 2004], but this value can be higher or lower depending
upon the gasifier type and feed stock quality. Most gasification processes being
demonstrated use oxygen, instead of air, as the oxidant.
Coal gasification technology has been developed for over one hundred years and by
now more than one hundred processes of gasification have been developed [O’Brien,
2004]. According to the coal movement and coal/gas contact pattern in the gasifier,
gasification technologies can be classified into three types as the moving bed, fluidized
bed and entrained flow bed. Different types of gasifiers have advantages and
disadvantages of their own, and IGCC systems can incorporate any one of a number of
gasifier designs, but all are based on one of these three types [O’Brien, 2004, Rubin,
1989, Brown, 2003, Cargill, 2001]. The next section will briefly discuss these three types
of gasifiers.
Moving-bed gasifier
In moving-bed gasifiers, gas and solid contact in the pattern of counter flow, where
large particles of coal move slowly down through the gasifier and react with gases
moving up through it. Several different reaction zones are formulated that implement the
gasification process. In the drying zone at the top of the gasifier, the entering coal is
heated and dried, and the product gas is cooled before it leaves the reactor. The coal is
further heated and devolatized by higher temperature gas as it descends through the
carbonization zone. In the next zone, the gasification zone, the devolatized coal gasifies
by reaction with steam and carbon dioxide. Near the bottom of the gasifier is the
32

combustion zone, which operates at the highest temperature, where oxygen reacts with
the remaining char. For the moving bed gasifiers, the discharge gas temperature is
principally controlled by the feed coal moisture content. High-moisture lignite coal
produces a raw gas temperature of about 600 °F, and low-moisture bituminous coal
produces a raw gas temperature of over 1000 °F [Brown, 2003].
The cold gas efficiency (chemical energy in cold gas/chemical energy in fuel) of
moving bed gasifiers is higher than that of fluidized bed and entrained flow gasifiers, and
the oxidant requirement for moving bed gasifiers is also relatively lower. Because the
moving-bed gasifier has higher cold gas efficiency, a larger portion of the original
heating value of the coal turns into the chemical energy in the gas, instead of the thermal
energy in the gas. Hence, the moving bed gasifier typically does not require the high
temperature heat exchangers that are required by entrained-flow and fluidized-bed
systems. Thus, more of the total output is generated by the gas turbine and less by the
steam turbine in an IGCC system using a moving-bed gasifier. Because of lower gas
temperature, the volatile material in coal is difficult to decompose, and there is greater
concentration of methane and tar in gas.
The Lurgi dry-ash gasifier, shown in Figure 2-2, is a pressurized, dry ash, moving-
bed gasifier. It uses steam and O as the oxidants. It uses lump coal rather than pulverized
2
coal and, it produces tars. For the Lurgi gasifier, lump coal enters the top of the gasifier
through a lock hopper and moves down through the bed. A rotating coal distributor
ensures even distribution of coal around the reactor. Steam and oxygen enter at the
bottom and react with the coal as the gases move up the bed. Ash is removed at the
bottom of the gasifier by a rotating grate and lock hopper. The coal moves slowly down
33

the gasifier, and it is warmed by the syngas flowing upwards through the bed; thus the
coal is sequentially dried and devolatilized, then gasified. The countercurrent operation
results in a temperature drop in the reactor. Gas temperatures in the drying and
devolatization zone near the top are approximately 260 to 538 °C. The very bottom of the
bed is the hottest part of the gasifier (~1000 °C), where almost any remaining coal is
oxidized. The CO produced at the bottom reacts with carbon higher in the bed to form
2
CO [DOT, 1998].
Figure 2 - 2 Simplified process of the Lurgi dry-ash gasifier [Brown, 2003]
The Lurgi dry-ash gasifier uses about a 4-5:1 ratio of steam to O as oxidant. The
2
result of this is that the temperature in the dry-ash system is kept sufficiently low at all
34

points. Thus, the ash does not melt, and can be removed as a dry ash. The low
temperature of the dry-ash system means that it is suited more to reactive coals, such as
lignite, than to bituminous coals [DOT, 1998].
Fluidized-Bed gasifier
For a fluidized-bed gasifier, coal is typically supplied through one side of the
reactor, and oxidant and steam are supplied near the bottom. Fluidized-bed reactors can
efficiently mix coal particles in the reactor vessel. Thus, a constant temperature is
sustained that is below the ash fusion temperature, which avoids clinker formation and
possible de-fluidization of the bed. This means that fluidized bed gasifiers are best suited
to relatively reactive fuels, such as biomass. Some char particles are entrained in the raw
gas as it leaves the top of the gasifier, but are recovered and recycled back to the reactor
via a cyclone. Ash particles which are removed below the bed give up heat to the
incoming steam and recycle gas. Fluidized bed gasifiers may differ in ash conditions and
in design configurations for improving char use [Worldbank, 2000].
The fluidized bed gasifier has the advantages of simpler reactor structure, uniform
and moderate operating temperature, easy operating, accepting a wide range of solid
feedstock, free of tar and phenol, and moderate oxygen and steam requirements. In
conventional fluidized bed coal gasifiers, like the Winkler gasifier, absence of selected
ash discharge design results in low temperature operation and higher carbon content in
bottom ash, which causes low carbon conversion, limited coal feedstock resources and
relatively small gasification capacity [Worldbank, 2000].
35

There are relatively few large fluidized bed gasifiers in operation. Commercial
versions of this type of gasifier include the high temperature Winkler (HTW) and KRW
designs. The latter gasifier was incorporated into the Piñon Pine Coal Gasification Plant
[Cargill, 2001].
The KRW gasification process, originally developed by M.W. Kellogg Company, is
a pressurized, dry feed, fluidized bed slagging process. The gasifier design is shown in
Figure 2-3. The KRW technology is capable of gasifying all types of coals, including
high sulfur, high-ash, low rank, and high-swelling coals, and it is also capable of
gasifying bio-derived and refuse-derived waste. The only solid waste from the plant is a
mixture of ash and calcium sulfate, which is identified as a non-hazardous waste [NETL,
2000]. Coal and limestone, crushed to below 1/4", are transferred from feed storage to the
KRW fluidized-bed gasifier via a lock hopper system. Gasification takes place by mixing
steam and air (or oxygen) with the coal at a high temperature. The fuel and oxidant enter
the bottom of the gasifier through concentric high velocity jets, which assure complete
mixing of the fuel with oxidant and char and limestone that collects in the gasifier. Upon
entering the gasifier, the coal immediately releases its volatile matters, which are
oxidized rapidly to supply the endothermic heat of reaction for gasification. The oxidized
volatiles form a series of large bubbles that rise up in the center of the gasifier, which
cause the char and sorbent in the bed to move down the sides of the reactor and back into
the central jet. The recycling of solids cools the jet and efficiently transfers heat to the
bed material. Steam, which enters with the oxidant and through a multiplicity of jets in
the conical section of the reactor, reacts with the char in the bed, converting it to syngas.
36

At the same time, the limestone sorbent, which has been calcined to CaO, reacts with H S
2
released from the coal during gasification to from CaS [NETL, 2000].
As the char reacts, the particles become enriched in ash. Repeated recycling of the
ash-rich particles through the hot gas of the jet melts the low-melting components of the
ash, which causes the ash particles to stick together. These particles are cool when they
return to the bed, and this agglomeration permits the efficient conversion of even small
particles of coal in the feed. The velocity of gases in the reactor is selected to maintain
most of the particles within the bed. The smaller particles that are carried out of the
gasifier are recaptured in a high efficiency cyclone and returned to the conical section of
the gasifier. Eventually, most of the smaller particles agglomerate when they become
richer in ash and gravitate to the bottom of the gasifier. Since the ash and spent sorbent
particles are substantially denser than the coal feed, they settle to the bottom of the
gasifier, where they are cooled by a counter-current stream of recycled gas [Cargill,
2001].
The char, ash, and spent sorbent from the bottom of the gasifier flow to the fluid-
bed sulfator, where both char and calcium sulfide are oxidized. The CaS forms CaSO ,
4
which is chemically inert and can be disposed of in a landfill. Sulfur released from
burning residual char in the sulfator is also converted to CaSO [Cargill, 2001].
4
37

Figure 2 - 3 Simplified process of the KRW gasifier [Brown, 2003]
Entrained-flow gasifier
In an entrained-flow gasifier, fine coal particles react with steam and oxygen at high
temperatures. Entrained-flow gasifiers have the ability to gasify all coals regardless of
rank. Depending on designs, entrained-flow systems may use different coal feed systems
(dry or water slurry) and heat recovery systems.
In an entrained flow bed, the contact time of gas and solid is very short, which is
only about several seconds, but the reaction rate and gasification capacity is greater
because of higher gasification temperature (1200-1500 °C) and smaller diameter of
38

pulverized coal (<100um). On the other hand, because of higher operating temperature,
part of the coal energy is converted to heat and its cold gasification efficiency is lower.
High gas temperature also makes gas cleaning and waste heat recovery system more
expensive [Worldbank, 2000]. Entrained-flow gasifiers have the following
characteristics:
• Ability to gasify all coals regardless of coal rank, caking characteristics, or
amount of coal fines (although feed stocks with lower ash content are favored)
• Uniform temperatures
• Very short fuel residence time in gasifier
• Solid fuel must be very finely divided and homogeneous
• Relatively large oxidant requirements
• Large amount of sensible heat in the raw gas
• High-temperature slagging operation
• Entrainment of some molten slag in the raw gas.
Nearly all commercial IGCC systems in operation or under construction are based
on entrained-flow gasifiers. Commercial entrained-flow gasifier systems are available
from GE Energy Gasification Technology (formerly ChevronTexaco), ConocoPhillips,
Shell, Prenflo, and Noell [Rosenberg, 2004]. The commercial gasification processes
believed most suited for near-term IGCC applications using coal or petroleum coke feed
39

stocks are the GE Energy, ConocoPhillips, and Shell entrained-flow gasifiers [SFA
Pacific, 2003].
ChevronTexaco gasification technology uses a single-stage, downward-feed,
entrained-flow gasifier, shown as Figure 2-4. Fuel/water slurry (e.g., 60-70% coal) and
95% pure oxygen (from an air separation unit) are fed to at the top of a hot, pressurized
gasifier. The fuel and oxygen react exothermally to produce raw fuel gas and molten ash
at a temperature ranging from 2200 to 2700 °F, and a pressure greater than 20
atmospheres. Operation at the elevated temperatures eliminates the production of
hydrocarbon gases and liquids in the syngas. In the syngas cooler design-type, the hot gas
flows downward into a radiant syngas cooler where high-pressure steam is produced. The
syngas cooler is specifically designed to meet the conditions of high thermal gradients
and the ability to handle soot. The syngas passes over the surface of a pool of water at the
bottom of the radiant syngas cooler and exits the vessel. The slag drops into the water
pool and is fed from the radiant syngas cooler sump to a lock hopper. The black water
flowing out with the slag is separated and recycled after processing in a dewatering
system. The slag is eventually removed through a lock hopper. This design configuration
maximizes heat recovery for steam production, as well as CO production, which is
appropriate for an IGCC application. After exiting the gasifier, the syngas is further
cooled and cleaned by a water scrubber, and the fine particulate matter and char may be
recycled to the gasifier. The cooled, water-scrubbed syngas consists mainly of hydrogen
and carbon monoxide, and contains no hydrocarbons heavier than methane. Metals and
other ash constituents become part of the glassy slag [Cargill, 2001].
40

Figure 2 - 4 Texaco gasifier with radiant syngas coolers [Brown, 2003]
An alternate design to the use of a radiant syngas cooler is the use of an exit gas
quench. In this design mode, hot gas exiting the reaction chamber is cooled by direct
contact with water, and then enters a scrubber for particulate and soot removal. This
design provides an effective mechanism to add water to the syngas to promote the water-
gas shift reaction and maximize hydrogen production. The quench design mode is often
used to accommodate heavy hydrocarbon feedstock [Brown, 2003].
41

Table 2 - 2 Important characteristics of three types of gasifiers [Brown, 2003]
Gasifier type Moving bed Fluidized bed Entrained
flow
Commercial Lurgi KRW Texaco,
Manufacturer Shell
Ash conditions Dry ash slagging Dry ash Agglomerating Slagging
Fuel size limits 6-50 mm 6-50 mm <6 mm < 6 mm <0.1 mm
Acceptability Yes Yes Possibly No, non-caking Yes
of caking coal
Preferred Lignite, Bituminous, Lignite, Lignite, Lignite,
feedstock reactive anthracite, reactive bituminous, reactive
bituminous, pet coke, bituminous, anthracite, bituminous,
anthracite waste anthracite, cokes, anthracite,
wastes waste biomass, pet cokes
wastes
Ash content No < 25% No No limitations <25%
limits limitation preferred limitation preferred
Preferred ash >2200 <2370 >2000 >2000 <2372
melting
temperature, F
Exit gas Low (800- Low (800- Moderate Moderate High
temperature, °F 1200) 1200) (1700- (1700-1900) (>2300)
1900)
Gasification 435+ 435+ 15 15-435 <725
pressure, psia
Oxidant Low Low Moderate Moderate High
requirement
Steam High Low Moderate Moderate Low
requirement
Unit capacity, 10-350 10-350 100-700 20-150 Up to 700
MWh
Key Hydrocarbon liquids in raw Large char recycle Large
distinguishing gas amount of
characteristics sensible of
heat energy
in the hot
raw gas
Key technical Utilization of fines & Carbon conversion Raw gas
issue hydrocarbon liquids cooling
42

Table 2 - 3 Comparison of parameters of gasification technologies [U.K.
Department of Trade and Industry, 1998]
Type of Ash Fixed bed Fluidized Entrained flow bed
gasifier agglomerating bed
fluidized bed
Gasification Oxygen blow Lurgi HTW K-T Texaco
technology (atmosphere) pressurized
Coal feeder Dry, crushed Lump Lump Dry, Pulverized Slurry
tyep crushed coal
Gasification ~1080 C 800~1000 C 800~1000 800~1000 ~1800 C ~1400 C
temperature C C
Gasification ~30 kPa ~20 kPa 2.24 MPa 1.0~2.5 34~48 kPa 3.4 MPa
pressure MPa
Ash agglomerating solid solid solid slag slag
removed
Gasification 92% 95.2% O2+steam O2+steam O2+steam O2+steam
medium O2+steam O2+steam
Oxygen/coal 0.454 0.64 0.41 0.37 0.7 1.17
Nm3/kg
Steam/coal 0.94 1.37 1.65 0.37 0.27 0.92
kg/kg
Carbon ~90 >95 >95 ~95 99 >95
conversion
%
Cold gas ~73 ~85 ~85 76 76 ~76
efficiency %
Carbon 7.7 11 9
content in
ash %
A general comparison of these three types of gasifiers, and a specific comparison of
some commercial gasifiers are given in Table 2-2 and Table 2-3, respectively.
43

2.2.3. Air Separation Unit (ASU)
This section discusses the function of the air separation units (ASU) in IGCC power
plants, followed by descriptions of current commercial technology and developing
technology for oxygen production.
Is ASU necessary for IGCC systems?
All coal gasification processes require an oxidant for the gasification reactions. Air,
oxygen, or oxygen-enriched air can be used as oxidant for gasification processes. The
choice of oxidant affects the amount of nitrogen the gasification system has to handle,
and depends on the application, types of gasifiers, and the degree of the system
integration. Air-blown gasification eliminates the need for the ASU. Oxygen-blown
IGCC systems, however, have several advantages over air-blown IGCC systems.
Syngas from an oxygen-blown gasifier has a heating value ranging from 250 to 400
Btu/scf, compared to an air-blown gasifier with 90 to 170 Btu/scf fuel gas and high
nitrogen content [Rubin, 1989]. Syngas with a medium heating value can potentially be
used as a replacement for natural gas as gas turbine fuel. In addition, the moderate
heating value of the gas helps minimize the size of the gasifier and auxiliary systems. The
cold-gas efficiency is 7-10 percentage points higher for oxygen-blown gasification than
air-blown gasification due to the avoidance of nitrogen dilution. Gasifier operability and
carbon conversion also improves with the use of oxygen [Rubin, 1989]. Comparing to
oxygen-blown gasification, air-blown gasification creates additional technical challenges
for the gas clean up and combustion turbine operation. Air-blown gasification also is less
suited for cost effective separation and capture of CO due to the diluted CO by nitrogen.
2 2
For these reasons, the next generation of IGCC facilities are expected to be based on
44

entrained-flow, oxygen-blown gasification technologies [Rosenberg, 2004]. To date, all
of the gasification processes demonstrated for commercial IGCC plants is oxygen-blown
systems.
Cryogenic oxygen production and novel air separation methods
Currently, air separation in large scale is achieved by using a cryogenic process in
which air is cooled to a liquid state and then subjected to distillation. The basic elements
of an air separation are [Air Products, 2004].
• Filtering and compressing air
• Removing contaminants, including water vapor and carbon dioxide (which would
freeze in the process)
• Cooling the air to very low temperature through heat exchange and refrigeration
processes
• Distilling the partially-condensed air (at about -300˚F / -185˚C) to produce
oxygen.
• Warming oxygen and waste streams by heat exchange with incoming air
Cryogenic oxygen production, commercialized early in the 20th century, is an
established process that is used extensively worldwide. Currently cryogenic processes
remain the most economically efficient separation method of making high purity oxygen
for high production rate plants. However, an ASU based on the cryogenic process
requires a large amount of power and accounts for the largest parasitic load on an
45

oxygen-blown IGCC plants. In addition, cryogenic processes in general have large capital
cost, due mostly to the cost of compressors, turbines, and numerous heat exchangers for
high pressure requirements and the recovery of refrigeration energy [Holt, 2001].
For these reasons, lowering the cost of air separation will significantly improve the
economics and efficiency of IGCC power plants and lower their capital costs. The
Department of Energy is sponsoring a research project to develop a novel air separation
technology--the Ion Transport Membrane Oxygen (ITM). ITM is based on ceramic
membranes that selectively transport oxygen ions when operated at high temperature. A
commercial-scale ITM oxygen module with a capacity of producing 0.5 ton/day oxygen
has been run by Air Products. It is predicted that ITM oxygen module capable of
producing 1000 ton/day oxygen will be available in 2010. According to Air Products, this
technology has the potential to lower the cost of producing oxygen by more than 30%
[Air Products, 2004]. Hence, it is expected that the upgrade in air separation technology
will significantly improve the economics of IGCC systems [O’Brien, 2004].
2.2.4. Syngas cooling
Coal gasification systems operate at high temperatures and produce raw, hot syngas
at temperatures from 800 to 1800 °C. The syngas from the gasifier has to be cooled
down for cleanup. Heat recovery is typically utilized to cool down the syngas and
increase overall system efficiency. Heat recovered can represent about 15% of the energy
in the feed fuel, but this varies with the gasification technology employed (5% for
moving bed to 25% for entrained flow processes) [Bruijn, 2003]. Depending on the
design of a gasifier, the raw syngas leaving the gasification reactor can be cooled by
radiant and/or convective heat exchange and/or by a direct quench system, which injects
46

either water or cool recycle gas into the hot raw syngas. In most IGCC plant design
configurations, saturated steam raised from cooling the raw gasifier syngas is sent to the
heat recovery steam generator (HRSG) for superheat and reheat. The steam and water
systems are integrated between the gasification island and the power conversion block,
but the superheated steam is generally better generated in the HRSG than in the raw
syngas coolers [Bruijn, 2003].
2.2.5. Syngas clean-up
The raw syngas produced by the gasification contains various impurities. However,
the concentrations of these various components depend on the feedstock composition and
the specific gasification process employed. The primary feedstock impurities of concern
are the sulfur and ash constituents. In gasification, the sulfur is converted mainly to H S
2
and COS, a portion of the ash and unburned carbon is entrained as particulates. Small
amounts of HCN and NH , and traces of metal carbonyl compounds, are also produced
3
[McCarthy, 1985].
Particulate materials have to be removed from raw syngas before it can be used as a
fuel of gas turbine to avoid damaging the turbine. This is generally accomplished by
cooling the syngas to much lower temperatures, and then using conventional cleaning
methods including cyclones or water scrubbers. The particulate material, including char
and fly ash, is then typically recycled back to the gasifier [Bruijn, 2003]. Another option
to water scrubbing for particulate removal is the use of ceramic candle filters or sintered
metal filters [Korens, 2002].
47

Next the syngas is treated in “cold-gas” clean up processes, also known as the Acid
Gas Recovery (AGR) process, to remove most of the H S, carbonyl sulfide (COS) and
2
nitrogen compounds. The primary processes are chemical solvent-based processes or
physical solvent-based processes. Sulfur recovery processes recover sulfur either as
sulfuric acid or as elemental sulfur. The most common removal system for sulfur
recovery is the Claus process, which produces elemental sulfur from the H S in the
2
syngas [O’Brien, 2004].
Carbonyl sulfide (COS), which is usually present at a several hundred ppmv level in
syngas from coal and petroleum residues, is difficult to remove in AGR units. Therefore,
further sulfur removal may be accomplished by the addition of a COS hydrolysis unit
(before the AGR), which catalytically converts COS to H S. For high sulfur coal, IGCC
2
plants that use COS hydrolysis, together with conventional AGR and sulfur recovery
units, have been able to achieve nearly 99% sulfur recovery [Wabash Energy Ltd, 2000].
DOE is currently working on new syngas cleanup systems in which the syngas will
need to be cooled only moderately [Simbeck, 2002]. Such a system would have higher
process efficiency achievable without syngas cooling and removal of water from the
syngas. Potential capital and operating cost savings of these new processes are related to
their reduced complexity compared to current cold gas cleanup processes. Hence, once
these technologies are commercialized, the economics and environmental friendliness of
IGCC power plants is expected to improve.
The focus of most new syngas cleanup programs is the removal of the sulfur,
chloride, alkali, and particulates from syngas at temperatures close to the highest inlet
48

temperature at which gas turbine fuel control and delivery systems could be designed.
This level was set at about 1,000 ºF by the requirement for very low alkali (potassium and
sodium) content of the fuel gas to prevent alkali corrosion of hot gas turbine components
and the desire to avoid expensive materials and unreliable refractory-lined piping [Todd,
1994; Holt, 2001]. However, both industry interest and government interest in such
processes have declined for several reasons [Stiegel, 2001], including the technical
challenge of the process and equipment development, the trend toward more stringent air
emissions and the success of the demonstration and commercial O -blown gasification
2
projects.
2.2.6. Combined cycle power unit
The clean syngas is sent to the combined cycle power unit. In a combined cycle
system, the first generation cycle involves the combustion of syngas in a combustion
turbine. The gas turbine powers an electric generator, and the hot exhaust gases from the
gas turbine is directed to a heat recovery steam generator to produce steam for a steam
turbine to complete the combined power cycle.
For any gas turbine manufacturer, the fuels that will be used will have a profound
effect upon both the machine design and the materials of construction. It is most
meaningful from the standpoint of turbine application to classify gaseous fuels by their
calorific values, which cover a very wide range: from a low of about 100 Btu/ft3 to a high
of 5,000 Btu/ft3. Table 2-4 shows such a classification of gaseous fuels.
49

Table 2 - 4 Classification of fuel gases [Foster, 2003]
Classification by Calorific value Primary gas
Typical specific fuels
calorific value kcal/nm3 (Btu/scf) components
10700-44500 Liquefied Petroleum Propane
Very high
(1200-5000) Natural gas liquids Butane
Natural gas
7100-10700
High Synthetic natural gas Methane
(800-1200)
Sour gas
Coal gas
Hydrogen
2700-7100 (O blown syngas)
Medium 2 Carbon monoxide
(300-800) Coke oven gas
Methane
Refinery gas
Carbon Monoxide
900-2700 Coal gas (air blown
Low Hydrogen
(100-300) syngas)
Nitrogen
Under 900 Carbon Monoxide
Very low Blast furnace gas
(under 100) Nitrogen
Historically, natural gas has been the primary fuel for gas turbines. According to
Table 2-4, comparing to natural gas, the volumetric heating value of cleaned syngas is
about 40-50 percent that of natural gas, so a much larger volume of fuel is required with
syngas firing to provide the necessary energy input to the gas turbine. Hence, when
syngas is used as fuel for modern combustion turbines, there are some process
differences. Recently GE initiated a program of extensive analysis to investigate the
combustion characteristics of a number of lower-heating-value fuels. Based upon the
results of this study, full scale single-burner and sector tests were conducted to confirm
expected performance of their MS5000 and LM2500 engine. In general, the only change
required to the standard combustion system is modification of the gas fuel nozzle to
handle the increased volume of fuel. A variation in heating value of more than 20 percent
could be tolerated while still maintaining adequate combustor performance. Many
improvements that have maintained flexibility for lower grade fuels have been made in
50

the modern, higher temperature machines such as the MS6001, MS7001, and MS9001
units [Foster, 2003].
The exhaust temperature from the combustion turbine is generally about 1100°F,
which can make additional power through a steam cycle. A HRSG can produce steam by
cooling the combustion turbine flue gas. This steam is supplied to a steam turbine to
generate additional electric power. In addition, the HRSG is always used to superheat the
high-pressure steam generated in the syngas cooler since satisfactory superheater
materials have not been demonstrated in the reducing atmosphere of a syngas cooler
[Rubin, 1989].
2.3. Literature Review of CO capture from IGCC systems
2
As one of the most promising technologies for CO capture from coal-fueled power
2
plants, IGCC power plants with CO capture have been studied in some previous studies
2
over the past 15 years [Holt 2003]. These studies covered conceptual technology
descriptions, flowsheet modeling and simulation. This section provides a review of the
literatures associated with CO capture from IGCC power plants.
2
Doctor et al. [Doctor 1994, 1996] developed engineering evaluations of CO
2
capture technologies combined with IGCC power plants. The base case for this study was
a 458 MW IGCC system that used an air-blown KRW agglomerating fluidized-bed
gasifier, Illinois No.6 bituminous coal feed, and in-bed sulfur removal. This study
investigated several commercial available chemical and physical solvents for CO capture
2
from IGCC plants, which included amine, glycol , chilled methanol and hot potassium
carbonate, and two emerging technologies for CO capture were also considered, which
2
51

were high-temperature CO separation with calcium-based sorbents and ambient
2
temperature facilitated transport polymer membranes for acid gas removal. The CO
2
capture efficiency was set to be 90%. From the IGCC plant, a 500-km pipeline took the
CO to geologic sequestering. This group also did case studies of Shell gasifier-based
2
multi-product system with CO capture. Life Cycle Analysis (LCA) was adopted in their
2
studies. For these cases, the net electric power production was reduced by 73.6~185.1
MW, with a CO release rate of 0.29~0.53 kg/kWh. The life cycle CO sequestering costs
2 2
ranged from $113 to $201/ton of CO .
2
Chiesa et al. [Chiesa, 1999] evaluated the energy balances, performance and cost of
electricity for two IGCC plants based on oxygen-blown, Texaco gasifiers and large,
heavy-duty gas turbines. In one plant, the raw syngas exiting the gasifier was cooled in a
high-temperature, radiation cooler; in the other it is quenched by the injection of liquid
water. Selexol systems were employed to recovery 90% CO in the syngas after shift
2
reaction. Comparing to the reference plants, the thermal efficiencies of the capture plants
were reduced by 5 to 7 percentage points and the cost of electricity were increased by
about 40 percent.
Haslbeck et al. [Haslbeck, 2002] investigated CO capture from oxygen-blown,
2
Destec- and Shell-based IGCC power plants. The reference plants fed with Illinois #6
coal, using W501G gas turbine and, three pressure level sub-critical reheat steam cycle,
had a net output of 400 MW. Selexol process was used for CO capture with an overall
2
capture efficiency of 87%, and the CO final product was compressed to 2100 psia. For
2
the Destec case with CO capture, the net output was reduced by 42 MW, and the thermal
2
efficiency was decreased by 6.6 percentage points. The COE also showed a
52

corresponding increase to 54.5 from 40.9 $/MWh. For the Shell case with CO capture,
2
the net output was reduced by 61 MW, and the thermal efficiency was decreased by 7.3
percentage points. The COE showed a corresponding increase to 62.9 from 40.6 $/MWh.
The study from the report of Parsons [Parsons, 2002] investigated oxygen-blown E-
gas and GE 7H turbine based IGCC power plants with and without CO capture. For the
2
reference plant, particulate was removed by the hot side filter, MDEA for sulfur removal
were employed. For the capture plant, two-stage Selexol are used for H S and then CO
2 2
removal at capture efficiency of 90%, and then CO is compressed to 2200 psig. The net
2
output of the reference plant was 424.5 MW, and the net output of capture plant was
reduced by 21 MW. Comparing with the capture plant, the thermal efficiency was
decreased by 6.1 percentage points. The COE also showed a corresponding increase to
65.7 from 52.4 $/MWh at a capacity factor of 65%.
O’Keefe et al. [O’Keefe, 2002] studied a 900 MW IGCC power plant configured to
remove 75% of the feed carbon as CO . The authors’ aim was to present a concept using
2
currently available commercial technology to provide an IGCC plant with the option to
capture CO . The plant used Texaco Quench gasifiers followed by a sour shift system, a
2
physical absorption acid gas removal, a sulfur recovery system, and a combined cycle
unit consisting of two GE 9FA gas turbines and a single steam turbine. The coal
feedstock was Pittsburgh 8. Selexol was used for acid gas removal. 75% of the carbon in
the coal was removed, but this could be higher. The capture of 75% of the carbon in the
coal results in a loss of efficiency of only two percentage points and a decrease in net
output of 3%, or 26MW.
53

A research group of the Foster Wheeler [Foster Wheeler, 2003] assessed the current
state of the art of coal-based 750 MWe nominal IGCC, with and without CO capture,
2
and the potential for improvements, between now and 2020. Two types of gasifier were
selected, one was the slurry feed gasifier, with product gas cooling by Water Quench
(Texaco quench gasifier); the other one was dry feed gasifier, with product gas cooling in
a waste heat recovery boiler (Shell gasifier). Several chemical solvents and physical
solvents for H S removal and CO capture are investigated. An open-cut coal from
2 2
eastern Australia was used for these plants. All the IGCC plant configurations were based
on two 9FA frame gas turbines. The ASU based on the cryogenic process was integrated
with gas turbines. Nitrogen produced by the ASU and exceeding the process consumption
was injected into the gas turbine for NO reduction and power augmentation.
X
Sensitivities to a variety of potentially significant parameters, such as gasification
pressure, separate removal of CO and H S vs. production of a combined CO /H S
2 2 2 2
stream, are assessed to help to determine the way forward for IGCC with CO capture.
2
For each alternative plant configuration, overall performances and investment cost were
estimated and used to evaluate the electric power production cost. For some alternatives
specific optimization studies had been made in order to select the most convenient acid
gas removal process and the best arrangement of the shift reactors. This study showed
that dry feed gasifier-based IGCC displayed a higher thermal efficiency, however slurry
feed gasifier-based IGCC required a lower investment, and in term of cost of electricity
and cost of CO recovery, slurry feed gasifier based IGCC was marginally better than the
2
dry feed gasifier based IGCC. The authors also pointed out that the pressure at which
gasification was operated was an important design parameter for IGCC optimization.
54

Increasing the gasifier operating pressure, the heat recovery on the syngas stream was
enhanced, the driving force for physical solvent scrubbing of CO was increased and the
2
equipment size was reduced.
According to the above review, the costs of CO capture and sequestration from
2
new IGCC plants added 25-50% to the COE and reduced the thermal efficiency by 10-
20% percent. Most studies concluded that the costs of pre-combustion CO capture from
2
syngas in an IGCC plant was much lower than the post combustion removal from
Pulverized Coal (PC) or Natural Gas Combined Cycle (NGCC) plants. Most studies
focused on the use of bituminous coals. In addition, for bituminous coals the costs of CO
2
removal vary significantly between the various coal gasification technologies and, the
advantage in capture costs over PC plants heavily depends on the gasification technology
selected.
The IGCC studies surveyed in this section covered the main gasification
technologies offered by ChevronTexaco, Shell and ConocoPhillips (E Gas). Among these
studies, Texaco quench gasifier was likely to provide the lowest cost option, and the
Selexol process was usually used for CO capture from IGCC systems.
2
55

REFERENCES (CHAPTER 2)
1. Air products, 2004: ITM Oxygen for Gasification, presented at Gasification
Technologies Conference, Washington, D.C.
2. Brown J.R., Manfredo L., Hoffmann J., and Ramezan M., 2002: Major
Environmental Aspects of Gasification-based Power Generation Technologies,
Final Report, Project Prepared for and Supported by: Gasification Technologies
Program, National Energy Technology Laboratory, DOE
3. Bruijn et al, 2003: Treating Options for Syngas, presented at the Gasification
Technologies Conference, San Francisco
4. Buchanan T.,DeLallo M., Schoff R., and White J., 2002, Evaluation of Innovative
Fossil Fuel Power Plants with CO Removal, Technical report prepared for EPRI,
2
Palo Alto, CA
5. Cargill P., 2001: Pinon Pine IGCC Project - Final Technical Report to the
Department of Energy, Sierra Pacific Resources, Reporting Period August 1, 1992
to January 1, 2001
6. Chiesa P. and Consonni S., 1999: Shift Reactors and Physical Absorption for
Low-CO Emission IGCCs, Journal of Engineering for Gas Turbines and Power,
2
Vol. 121
7. Clayton S.J., Stiegal G.J., Wiemer J.G., 2002: Gasification Markets and
Technologies – Present and Future: An Industry Perspective, National Energy
Technology Laboratory (NETL) U.S. Department of Energy (Report No.
DOE/FE-0447)
8. Doctor R.D., etc., 1994: Gasification combined cycle: carbon dioxide recovery,
transport, and disposal, Report prepared by ANL/ESD
9. Doctor R.D., etc., 1996: KRW oxygen-blown gasification combined cycle carbon
dioxide recovery, transport, and disposal, Report prepared by ANL/ESD
10. Edward L. P., Shelton W.W., and Lyons J.L., 2002: Advanced Fossil Power
Systems Comparison Study, Final report prepared for National Energy
Technology Laboratory
11. Foster, A.D., Doering H.E., and Hilt M.B., 2003, Fuels Flexibility in Heavy Duty
Gas Turbines, GE Company Schenectady, New York
12. Foster Wheel, 2003: Potential for improvement in gasification combined cycle
power generation with CO capture. Report # PH4/19, May 2003
2
56

13. O’Keefe L.F., Griffiths J., Weissman R.C., De Puy R.A., and Wainwright J.M.,
2002: A Single IGCC Design for Variable CO Capture, Fifth European
2
Gasification Conference
14. Haslbeck J.L., 2002, Evaluation of Fossil Power Plants with CO Recovery,
2
Parsons Infrastructure & Technology Group Inc., February 2002
15. Holt N., Booras G., and Todd D., 2003: A Summary of Recent IGCC Studies of
CO Capture for Sequestration By Presented at The Gasification Technologies
2
Conference San Francisco, CA
16. Holt N., 2001: Coal Gasification Research, Development and Demonstration –
Needs and Opportunities, 2001 Gasification Technologies Conference, sponsored
by the gasification Technologies Council and EPRI, San Francisco, CA
17. Korens N., Simbeck D.R., Wilhelm D.J., 2002: Process Screening Analysis of
Alternative Gas Treating and Sulfur Removal for Gasification, Revised Final
Report prepared for National Energy Technology Laboratory, U.S. Department of
Energy
18. Joshi M.M., 2000, Quality Assured maintenance Management For Coal Handling
Plant. http://www.plant-
maintenance.com/articles/Maintenance_Management_QA.pdf
19. McCarthy, C.B., and Clark W.N., 1985: Integrated gasification/combined cycle
(IGCC) electric power production- A rapidly emerging energy alternative.
Presented at symposium on coal gasification and synthetic fuels for power
generation, EPRI, Palo alto, CA
20. O’Brien J.N., Blau J., Rose M., 2004: An Analysis of the Institutional Challenges
to Commercialization and Deployment and Deployment of IGCC Technology in
the U.S. Electricity Industry: Recommended Policy, Regulatory, Executive and
Legislative Initiatives, Final Report, Project Prepared for and Supported by: DOE,
NETL, Gasification Technologies Program and National Association of
Regulatory Utility Commissioners
21. Parsons E., NETL, “Advanced fossil power systems comparisons study”, NETL
report, 2002
22. Rosenberg W.G., Alpern D.C., Walker M.R., 2004: Deploying IGCC in This
Decade With 3 Party Covenant Financing, Volume I
23. Rubin, E., 1989: Implications of Future Environmental Regulation of Coal-Based
Electric Power, Annual Rev. Energy, 14:19-45
24. SFA Pacific, Inc., 2003: Evaluation of IGCC to Supplement BACT Analysis of
Planned Prairie State Generating Station
57

25. Simbeck D.R., 2002: Industrial Perspective on Hot Gas Cleanup, Presentation at
the 5th International Symposium on Gas Cleaning at High Temperatures, U. S.
DOE National Energy Technology Laboratory
26. Stiegel G.J., Clayton S.J., and Wimer J.G., 2001: DOE’s Gasification Industry
Interviews: Survey of Market Trends, Issues and R&D Needs, 2001 Gasification
Technologies Conference, sponsored by the Gasification Technologies Council
and EPRI, San Francisco, CA
27. Todd D.M., 1994: Clean Coal and Heavy Oil Technologies for Gas Turbines,
Paper No. GER-3650D, 38th GE Turbine State-of-the-Art Technology Seminar,
GEZ-7970, General Electric Company, Schenectady, NY
28. U.K. Department of Trade and Industry, 1998: Gasification of Solid And Liquid
Fuels For Power Generation - Status Report,
http://www.dti.gov.uk/cct/pub/tsr008.pdf
29. Wabash Energy Ltd, 2000: The Wabash River Coal Gasification Repowering
Project, U.S. Department of Energy Topical Report Number 20, prepared for
National Energy Technology Laboratory, U.S. Department of Energy
30. World Bank, 2000:
http://www.worldbank.org/html/fpd/em/power/EA/mitigatn/igccsubs.stm#igcctec
h
31. NETL, 2000:
http://www.netl.doe.gov/coalpower/gasification/description/gasifiers.html#Lurgi
58

Chapter 3. PERFORMANCE AND ECONOMIC SIMULATION MODEL OF
IGCC SYSTEMS
The purpose of this chapter is to summarize the information of IGCC modeling
process. Plants with and without CO capture are modeled with Aspen Plus. The details
2
include the design basis, the mass and energy balances of major units of the IGCC
systems, design specifics which is required by commercial available technologies, and
the convergence sequence, which specifics the calculation sequence of the simulation
model.
3.1. Model design basis
Figure 3-1 provides a simplified overview of the reference plant configuration,
which does not incorporate CO recovery. This layout is a typical oxygen-blown IGCC
2
with cold-gas cleanup in which H S is captured by an acid gas removal system. The
2
cleaned gas is then saturated and reheated before it is fed into gas turbine combustion
chamber. The hot exhaust from gas turbine is used to generate steam for a steam cycle
through the HRSG. Oxygen is supplied by an air separation unit.
Figure 3-2 is an overview of the capture plant configuration. Comparing to the
reference plant, a water gas shift reactor is added to increase CO partial pressure through
2
converting CO into CO . CO is captured in a Selexol process, a commercial glycol-
2 2
based process for acid gas removal.
59

Figure 3 - 1 An IGCC system without CO capture
2
Figure 3 - 2 An IGCC system with CO capture
2
The objective of this modeling study is to assess coal-based IGCC plants with and
without CO capture based on current commercial available technology, hence equipment
2
60

selection and system design of this IGCC system focuses on mature technologies and
methodologies
3.1.1. Gasification technology selection
Currently, many different types of gasifier are commercially available, such as
Texaco, Shell, E-gas. This study is based on the oxygen-blown, slurry feed Texaco
quench gasifier with product gas cooling by water quench, which is the most widely used
gasifier type in IGCC plants. In addition, the Texaco quench gasifier is known for its
low-capital cost requirement.
Currently available Texaco gasifiers can be operated in a wide pressure range, from
15 bar to 70 bar. For a given capacity an increase of the gasification pressure will reduce
the size of the equipment but increase the operating costs. In this study, a medium
pressure (42 bar) gasifier is adopted. Considering that the final destination of the syngas
in an IGCC is the combustion chamber of the gas turbine, which available today with a
rang of 20~30 bar, a gas expander is installed between the gasification and the gas
turbine, which can offset the extra operation cost due to the high gasification pressure.
3.1.2. Air separation unit
The state-of-the-art air separation plants are based on cryogenic mechanism.
Various ASU configurations can be used in IGCC systems, ranging from complete
integration, in which all of the air for the ASU is provided by the gas turbine compressor,
to zero integration in which the ASU is a completely stand-alone unit providing only
oxygen to gasifiers. Considering operation stability and flexibility, the “stand alone”
option is employed.
61

For the “stand alone” option, low pressure air separation plant is chosen, with its
own air compressors delivering air to the cryogenic process at the minimum pressure
requirement to meet the energy demand of the process. In this case, syngas
humidification is generally preferred to nitrogen addition for NO control to avoid the
x
large nitrogen compression energy consumption.
3.1.3. Syngas clean up system
Raw syngas from gasification unit is hot, humid and contaminated with H S, and
2
COS. Before used as gas turbine fuel, this raw syngas has to be cleaned by removing all
the contaminants and prepared at the proper conditions of temperature, pressure and
water content to meet the requirement of the gas turbine combustion under conditions of
desired environmental performance and operation stability.
The key factor in achieving the environmental performance of IGCC systems is
sulfur removal from the syngas. Sulfur is contained in two types of acid gases, H S and
2
COS. The first step in the sour gases removal process is to remove the carbonyl sulfide
(COS) from the gas stream. For an IGCC system without CO capture, the conventional
2
method is to pass the syngas through a fixed bed, catalytic hydrolysis reactor, which will
hydrolyze the COS to CO , H S and CO. Hence for the plant without CO capture, a
2 2 2
particle scrubber is employed to remove solids entrained in the syngas, then COS
hydrolysis reactors are used to converted COS into H S. The Selexol/Claus/SCOT
2
process is used for sulfur removal and recovery.
For the capture plant, after particle removal, the water gas shift reactor is used to
convert CO into CO . The CO shift catalyst also hydrolyses COS to H S. Hence there is
2 2
62

no need of a separate COS hydrolysis system. Two types of catalyst are usually used for
the water gas shift reaction [IEA, 2003]:
• Sour shift catalysts based on Co-Mo, which operate at medium/high temperature
and requiring a steam/dry gas volume ratio in the range of 1.1-1.6. This type of
catalysts can withstand high concentration of sulfur in syngas.
• Clean shift catalysts based on Fe-Cr or Cu, which operate at high temperature or
low temperature and require a steam/dry gas volume ratio equal to 1. For this type
of catalyst, the total sulfur content of syngas should be less than 10 ppm.
For IGCC systems with Texaco quench design, preliminary thermodynamic
analysis shows that sour shift dominates the clean shift option because syngas at particle
scrubber outlet has all the characteristics required by the sour shift reaction (temperature
and steam to carbon ratio). In the capture plant, the acid gases, H S and CO , are
2 2
removed through two Selexol processes, separately.
3.1.4. Gas turbine selection and steam cycle design
Syngas produced by gasification process is a type of Low Calorific Value (LCV)
fuel. GE gas turbines applied to LCV applications have accumulated rich experience and
hold a leading position in this field. In this study, GE 7FA is selected, which has been
designed to operate at base load conditions on syngas at Tampa Electric [Brdar, 2003].
Selection of a single- or multiple-pressure steam cycle for a specific application is
determined by economic evaluation, which considers the plant-installed cost, fuel cost
and quality, plant-duty cycle, and operating and maintenance cost. According to the
63

recommendation of GE, single- and multiple-pressure non-reheat steam cycles are
applied to systems equipped with GE gas turbines that have rating point exhaust gas
temperatures of approximately 1000°F / 538°C or less. Multiple-pressure reheat steam
cycles are applied to systems with GE gas turbines that have rating point exhaust gas
temperatures of approximately 1100°F / 593°C or greater [Chase, 2003]. Table 3-1 gives
such recommendations in detail. Since the exhaust gas temperature of GE 7FA is
approximately 1104 °F/596 °C, a three-pressure reheat steam cycle is employed in this
study.
Table 3 - 1 Steam and gas product line steam turbine throttle and admission steam
conditions
Heat Recovery Steam Cycle Non-Reheat Three-Pressure Reheat Three-Pressure
Steam Turbine Size (MW) ≤ 40 > 40 <60 ≥ 60 > 60
Throttle Pressure (psig) 820 960 1200 1400-1800
Throttle Temperature (°F) 40 approach to Gas Turbine 1000-1050
Exhaust Gas Temperature
Reheat Pressure (psig) 300-400
Reheat Temperature (°F) 1000-1050
IP Admission Pressure (psig) 100 120 155 300-400
IP Admission Temperature (°F) 20 Approach to Exhaust Gas Temperature upstream of
Superheater
LP Admission Pressure (psig) 25 25 25 40
LP Admission Temperature (°F) 20 Approach to Exhaust Gas Temperature upstream of
superheater
3.2. Major process sections of the IGCC model
The present model consists of slurry preparation units, gasification units with
quench, particle removal, low temperature gas cooling and clean up units, fuel expender,
fuel gas saturator and reheater, by product sulfur production, gas turbine system, steam
64

cycle system, and heat integration among different units. In addition to these units and
heat integration, the model also incorporates auxiliary power consumption for ASU and
summary files of the whole IGCC system.
Each major process section mentioned above is referred to as a flowsheet section in
Aspen models. Within each flowsheet, unit operation models represent specific
components of that process. There are user-specified inputs regarding key design
assumptions for each unit model. The numerical values of these design assumptions are
shown in this report. However, users can change these values to simulate their specific
design alternatives. The major flowsheet sections in the IGCC system are presented as in
the following.
3.2.1. Coal slurry preparation and gasification flowsheet
Coal from the coal grinding system is continuously fed to the grinding mill. Grey
water from waste water treatment facility is used for slurrying the coal feed. The coal
slurry with a desired slurry concentration is pumped into the gasifier. In this section, the
methodology used to model coal preparation is presented.
Coal is a type of non-conventional solid, and its composition has to be input by the
user in forms which Aspen accepts. In Aspen, the component attributes of coal are
specified in three forms: PROXANAL for proximate analysis, ULTANAL for ultimate
analysis, and SULFANAL for sulfur analysis. Table 3-2, as an example, gives the typical
compositions of Pittsburgh #8 coal and its input values for Aspen model. Aspen Plus
estimates the heat of coal combustion based on its PROXANAL, ULTANAL, and
SULFANAL. Users can also enter the heat of combustion directly.
65

Table 3 - 2 Coal composition and its corresponding input in Aspen Plus
Coal composition
(wet basis) PROXANAL ULTANAL SULFANAL
Element Value Element Value Element Value Element Value
ASH 7.24 MOISTURE 5.05 ASH 7.63 PYRITIC 1.23
CARBON 73.81 FC 49.855 CARBON 77.74 SULFATE 0
HYDROGEN 4.88 VM 42.515 HYDROGEN 5.14 ORGANIC 1
NITROGEN 1.42 ASH 7.63 NITROGEN 1.5
CHLORINE 0.06 CHLORINE 0.06
SULFUR 2.13 SULFUR 2.23
OXYGEN 5.41 OXYGEN 5.7
Figure 3 - 3 Slurry preparation and gasification flowsheet
Figure 3-3 illustrates the mass and heat flows in the coal slurry preparation process
and gasification units, and Table 3-3 shows the corresponding unit operations that are
simulated in Aspen Plus. The coal slurry is compressed up to 710 psia through a slurry
pump, which is simulated by a unit named as “SlurryPump”. Gasification simulation
calculates the Gibbs free energy of the coal. However, the Gibbs free energy of coal
cannot be calculated because it is a non-conventional component. Hence, a RYield unit,
which simulate a reactor with a known yield, and does not require reaction stoichiometry
66

and kinetics, named as “DeCoal” is used to decompose the coal into its constituent
elements based on the ultimate composition analysis of coal.
The gasification unit converts coal slurry into syngas. The coal slurry and oxygen
from the air separation unit react in the gasifier at high temperature (approximately 2450
°F), high pressure (approximately 620 psia in this study) and under the condition of
insufficient oxygen to produce syngas. Syngas consists primarily of hydrogen and carbon
monoxide with lesser amounts of water vapor, carbon dioxide, hydrogen sulfide,
methane, and nitrogen. Traces of carbonyl sulfide and ammonia are also formed. Ash
presenting in the coal melts into slag. Hot syngas and molten slag from the gasifier flow
downward into a quench chamber, which is filled with water, and is cooled into medium
temperature (approximately 450 °F). The slag solidifies and flows to the bottom of the
quench chamber.
In addition to CO, H and CO , small amounts of CH , HCl, COS and NH are also
2 2 4 3
formed. Various amounts of H S depending on the sulfur content of the feed coal.
2
The Texaco process uses an entrained flow gasifier. Slagging is an important
problem with this type of gasifier. The slagging formation is modeled as follows.
In this study the gasification process is modeled on the fixed carbon conversion
model [Altafini, 2003; Zaimal, 2002], and simulated in three steps. At first, slag
formation is simulated in the Slag block based on the following stoichiometric reaction.
The stoichiometric coefficients of carbon and ash are determined by the ash percentage in
the coal and carbon loss in the gasification process.
67

mC+nAshåSlag
Second, coal slurry from the Slag block mixed with oxygen from the ASU unit
enter the gasifier reactor, reactions occur in the reactor is simulated in GasifRx unit,
which is based on RGibbs model. RGibbs models chemical equilibrium by minimizing
Gibbs free energy. Chemical reactions and their approach temperatures1 modeled in this
equilibrium gasifier reactor are as follows [Altafini, 2003; Zaimal, 2002, Zhu, 2003]:
C+2H 2åCH
4
(approach temperature: -300°F)
C+H
2
OåCO+H
2
C+O 2åCO
2CO+O 2å2CO
2
(approach temperature: -550°F)
CH
4
+2O 2åCO
2
+2H
2
O (approach temperature: -500°F)
S+H 2åH
2
S (approach temperature: -500°F)
N
2
+3H 2å2NH
3
(approach temperature: -500°F)
CO+H
2
SåCOS+H
2
(approach temperature: -500°F)
1 The approach temperature is a pseudo-temperature used in Aspen to adjust
calculated equilibrium concentrations to actual (observed) values under non-equilibrium
conditions.
68

Cl
2
+H 2å2HCl (approach temperature: -300°F)
The reaction temperature and heat loss, which is assumed to be 1% of the total low
heating value of the inlet coal flow, in the gasification reactor is maintained by adjusting
the inlet flow rate of oxygen.
Third, raw syngas and molten slag discharge from the reactor into the quench
chamber, which is simulated by the Quench unit. The Quench unit performs rigorous
vapor-liquid equilibrium calculations to determine the thermal and phase conditions of
syngas saturation process. In this quench unit, molten slag is cooled down and separated
from the syngas.
Table 3 - 3 Coal slurry preparation and gasification process unit description.
No Aspen unit ID Unit parameters Unit function
1 CoalMult (Mult) Multiplication factor: Manipulate slurry flow rates through
0.5~5 Design Spefic
2 SlurryPMP Discharge P=710 psi This unit simulate coal slurry pump
(Pump)
Efficiency=Default
3 DeCoal(RStoic) Pressure=620 psi This block decomposes coal into its
elements using the Calcularor
Temperature=59 F
4 MkSlag (RStoic) Pressure=620 psi Simulate the stoichiometric reaction
which produces slag based on the
Temperature=59 F
coal’s ultimate analysis and carbon
loss percentage in gasification
process
5 GasifRX (RGibbs) Pressure=620 psi Simulate the stoichiometric reactions
occurring in the gasifier. Heating loss
Temperature=2450 F
in the gasifier is maintained as 1% of
Products: O2, N2, H2, CO, the total LHV of coal through Design
CO , H O, CH , H S, NH , Specific
2 2 4 2 3
COS, HCL
6 Quench (Flash 2) Pressure drop=15 psi Simulate the quench process of
syngas, slag cooling and separation
Heat duty=0 But/hr
69

3.2.2. Low temperature gas cooling and clean up
Raw syngas from the quench chamber enters the scrubber to remove solid particles.
Figure 3-4 illustrates the mass flows in the syngas cooling process, and Table 3-4 shows
the corresponding unit operations that are simulated in Aspen Plus. The scrubber is
simulated by the block PartRemv, which separates solids from the syngas. As the first
step of sour gases removal, the syngas passes through a fixed bed, catalytic hydrolysis
reactor, which hydrolyzes the COS to CO and H S, and the HCN to NH and CO.
2 2 3
Activated alumina type catalysts are generally employed for this application, and COS
concentrations approaching equilibrium levels can be achieved. This reactor is modeled
by a block named COSHydro, which is a rigorous equilibrium reactor based on
stoichiometric approach for the following hydrolysis reaction:
COS+H
2
OåH
2
S+CO
2
Syngas after COS hydrolysis is at a temperature of approximately 460 °F, which
has to be cooled down to approximately 100 °F for H S removal. Blocks named as
2
SgasCol1~5 simulate this cooling process. Condensate water from this cooling process is
collected for the syngas quench and scrubber processes. Heat released from syngas
cooling is recovered to produce low pressure steam (390°F/48 psia) for steam cycle, and
intermediate pressure hot water (408°F/325 psia) for syngas saturation and reheating. The
flow rate of feed water for the low pressure steam and intermediate pressure hot water is
manipulated by the Design Specification SGTEMP, which adjusts the feed water flow
rate to satisfy the syngas temperature at the exit of the last syngas cooler is 100°F. The
flow rate ratio of the low pressure steam to the intermediate pressure hot water is
70

controlled by another Design Specification SGIPFLOW, which adjusts the flow rate of
the intermediate pressure hot water to meet the need of syngas saturating and reheating.
Table 3 - 4 Syngas cooling process unit description of the reference plant
No Aspen unit ID Unit parameters Unit function
1 Scrubber Pressure drop=10 psia Simulate the scrubber process of
(Flash 2) Heat duty=0 But/hr particle removal from raw syngas
2 COSHydro Pressure drop=5 psia Simulate the COS hydrolysis process
(REquil) Heat duty=0 But/hr converting COS into H S
2
3 SgasCol1 Pressure drop=3 psia Simulate syngas cooler
(Heater)
4 SgasCol2 Pressure drop=3 psia Simulate syngas cooler
(Heater)
5 SgasCol3 Pressure drop=5 psia Simulate syngas cooler
(Heater)
6 SgasCol4 Pressure drop=3 psia Simulate syngas cooler
(Heater)
7 SgasCol5 Pressure drop=5 psia Simulate syngas cooler
(Heater)
8 FWPMP2 Discharge pressure=18 psia Simulate feed water pump
(Pump) Efficiency=default value
9 FWPMP3 Discharge pressure=18 psia Simulate feed water pump
(Pump) Efficiency=default value
10 FWSPLIT Indicate that feed water is divided into
(SPLIT) two streams, the flow rate to the LP
steam evaporator is manipulated by the
Design Specification SGIPFLOW
71

Figure 3 - 4 Syngas cooling section flowsheet of the reference plant
Figure 3-5 illustrates the mass flows in the syngas cooling process of the capture
plant, and Table 3-5 shows the corresponding unit operations that are simulated in Aspen
Plus. For the capture plant, syngas from the scrubber is at a temperature of approximately
420 °F. The water gas shift reaction occurs at two rectors, the high temperature reactor
and the low temperature reactor, which are simulated by block HTShift and LTShift. In
the shift reactors, the following reactions occur in the presence of catalysts:
72

CO+H
2
OåCO
2
+H
2
COS+H
2
OåH
2
S+CO
2
Because the shift reaction is exothermic, there is high quality energy available for
generating high pressure and intermediate pressure steam during the syngas cooling
process. Blocks named as HTCol1~4 and LTCOl1~5 simulate this cooling process. The
condensate water from this cooling process is collected for syngas quench and scrubber
processes. The high pressure steam is sent to the high pressure steam turbine. Part of the
intermediate pressure is used for syngas reheating, and the rest is sent to the steam cycle.
The flow rate of the feed water for the high pressure steam and the intermediate pressure
steam is manipulated by the Design Specification SGTEMP, which adjusts the feed water
flow rate to maintain the design syngas temperature at the exit of last syngas cooler. The
flow rate ratio of intermediate pressure steam to the high pressure steam is controlled by
another Design Specification SGSHIFT, which adjusts the flow rate of the high pressure
feed water to meet the temperature requirement for the low temperature shift reaction.
73

Table 3 - 5 Syngas cooling process unit description of the capture plant
No Aspen unit ID Unit parameters Unit function
1 Scrubber Pressure drop=10 psia Simulate the scrubber process of
(Flash 2) Heat duty=0 But/hr particle removal from raw syngas
2 SgasHet (Heater) Pressure drop=4 psia Simulate the syngas heater
Temperature=469.4 F
3 HTShift (Requil) Pressure drop=4 psia Simulate the high temperature shift
Heat duty=0 Btu/hr reactor
4 HTCol1 (Heater) Pressure drop=4 psia Simulate syngas cooler
5 HTCol2 (Heater) Pressure drop=3 psia Simulate syngas cooler
6 HTCol3 (Heater) Pressure drop=4 psia Simulate syngas cooler
7 HTCol4 (Heater) Pressure drop=5 psia Simulate syngas cooler
8 LTShift (Requil) Pressure drop=5 psia Simulate the low temperature shift
Heat duty=0 Btu/hr reactor
9 LTCol1 (Heater) Pressure drop=4 psia Simulate syngas cooler
10 LTCol2 (Heater) Pressure drop=4 psia Simulate syngas cooler
11 LTCol3 (Heater) Pressure drop=4 psia Simulate syngas cooler
12 LTCol4 (Heater) Pressure drop=4 psia Simulate syngas cooler
13 LTCol5 (Heater) Pressure drop=5 psia Simulate syngas cooler
14 FWPMP1 (Pump) Discharge pressure=365 Simulate feed water pump
psia
Efficiency=default value
15 FWPMP3 (Pump) Discharge Simulate feed water pump
pressure=1734 psia
Efficiency=default value
16 FWSPLIT (SPLIT) This unit is used to indicate that feed
water is divided into two streams, the
flow rate to the intermediate pressure
steam evaporator is manipulated by
the Design Specification SGSHIFT
74

Figure 3 - 5 Syngas cooling section flowsheet of the capture plant
75

3.2.3. HS capture and sulfur recovery section
2
After COS hydrolysis, almost all of the sulfur in the gasifier feedstock is converted
into H S. Figure 3-6 illustrates the mass and energy flows in the sulfur removal and
2
recovery section, and Table 3-6 shows the corresponding unit operations that are
simulated in Aspen Plus. In this modeling study, Selexol process, a physical solvent
system, is employed to capture H S. A block, named as SulfSep, is used to simulate this
2
Selexol process. In this block, approximately 99% of H S is removed from the syngas.
2
The H S rich gas and the flash gas from the Selexol process are sent to the Claus/Scot
2
unit for sulfur recovery.
The Claus process has been the sulfur recovery workhorse for applications with
large amounts of sulfur. The Clause process is carried out in two stages. In the first stage,
about one third of the gases from the Selexol unit, which exits at about 120 °F, are burned
in the first furnace. This first furnace is simulated by the block named Furnace. In this
block, the following reaction is modeled based on stoichiometric mechanism which is
close to the real situation in the reactor. Low pressure air from an air compressor is used
as the oxidant of Claus reaction.
H
2
S+O 2åSO
2
+H
2
O with 33% of H
2
S converted
The remaining acid gases enter the second stage furnace, where the H S and SO
2 2
react in the presence of a catalyst to form elemental sulfur:
2H
2
S+SO 2å3S+2H
2
O
76

The gas is cooled in a waste heat boiler and then sent through a series of reactors
where more sulfur is formed. The sulfur is condensed and removed between each reactor.
An Aspen block, ClausRxr, is used to simulate the reactors, where 98% of H S is
2
recovered because the Claus process is limited by chemical equilibrium to removal
efficiencies of approximately 98% if three catalytic reactor stages are employed. To
achieve higher removal efficiencies, a tail gas treating unit is required.
SCOT process is a conventional tail gas treating process. In the process, the tail gas
from the Claus unit and the flash gas from the Selexol unit are heated to approximately
570 °F in an in-line burner, which serves the dual purpose of heating the gas stream and
producing a reducing gas, which is needed in the downstream reactor. The effluent from
the burner is then passed over a cobalt-molybdenum catalyst. In the reactor, all of the SO
2
and CS are converted to H S by a combination of hydrogenation and hydrolysis
2 2
reactions. This process is modeled by the block named BsComb. In this block, the
following combustion and hydrogenation reactions occur:
CO+0.5åCO
2
CH
4
+2O 2åCO
2
+2H
2
O
SO
2
+3H 2åH
2
S+2H
2
O
COS+H
2
OåH
2
S+CO
2
The reactor effluent gas is then cooled and processed through a Stretford unit,
where H S is converted to elemental sulfur, and remaining gases exhaust to the
2
77

atmosphere. The block named StretFrd is used to model this process, where the following
reactions occur:
2H
2
S+O 2å2S+2H
2
O
2H
2
+O 2å2H
2
O
The block QMix, which simulates the heat recovery process of the waste heat
boiler, collects heat from the above reactors to preheat the feed water from the steam
cycle.
78

Table 3 - 6 Sulfur removal and recovery unit description
No Aspen unit ID Unit parameters Unit function
1 SulfSep (Sep) Flue gas: T=85 F, P=32 atm This unit simulates the Selexol
Acid gas: T=120 F, P=22 psia process for H S removal.
2
Flash gas: T=58 F, P=115 psia
2 CAirComp Type: Isentropic Model the air compressor for
(Compr) Discharge pressure=23 psia Claus process
Isentropic efficiency=0.9
3 CAirMix1 Simulate the mixer of air and acid
(Mixer) gas from Selexol unit
4 Furnace (RStoic) Pressure drop=0 psia Simulate the first stage of Clause
Temperature=589 F process, where about one third of
acid gas from Selexol process is
burned.
5 ClausRxR Pressure drop=0 psia Simulate the second stage of
(RStoic) Temperature=589 F Clause process, where the H S
2
and SO react in the presence of a
2
catalyst to form elemental sulfur.
6 ClausSep (Sep) Simulate the sulfur removal
process between each reactor,
water condensate, and tail gas
separation.
7 BsComp1 Type: Isentropic Model the air compressor for Scot
(Compr) Discharge pressure=30 psia process
Isentropic efficiency=0.9
8 BsComp2 Type: Isentropic Model the tail gas compressor for
(Compr) Discharge pressure=30 psia Scot process
Isentropic efficiency=0.9
9 BsMix (Mixer) Simulate the mixer of tail gas and
air
10 BsComb (RStoic) Pressure drop=0 psia Simulate the tail gas treatment
Temperature=400 F process, which converts SO into
2
H S with the aid of a cobalt-
2
molybdate catalyst
11 Stretfrd (RStoic) Pressure drop=0 psia Simulate sulfur recovery process,
Temperature=100 F where H S reacts with O to
2 2
generate Sulfur
12 QMix (Mixer) Simulate the waste heat boilers
which recover heat generated in
sulfur recovery process for feed
water heating in steam cycle
79

Figure 3 - 6 Sulfur removal and recovery section flowsheet
80

3.2.4. Clean syngas saturation, expend, and reheat section
Clean syngas from the Selexol unit for sulfur removal could be used as the fuel of
the gas turbine. In order to meet the emission and pressure requirements of the gas
turbine combustion, the fuel is saturated, expended, and preheated before entering the
combustion chamber. For the reference plant, fuel from the Selexol unit at a temperature
is heated up by the condensate water from the syngas cooling process in the heat, which
is simulated by the block FuelHet1. The heated fuel is expended in a turbine expender to
generate electricity, and its pressure is reduced to match the pressure at the gas turbine
combustor. Fuel from the expender enters the saturator to mix with the intermediate
pressure hot water produced in the syngas cooling process. Before entering the gas
turbine combustion chamber, the saturated fuel is preheated up to about 400 °F by the
intermediate pressure hot water from syngas cooling unit. Figure 3-7 illustrates the mass
and energy flows in the sulfur removal and recovery section, and Table 3-7 shows the
corresponding unit operations that are simulated in Aspen Plus.
81

Table 3 - 7 Sulfur removal and recovery unit description
No Aspen unit ID Unit parameters Unit function
0 CO Sep (Sep) Simulate the CO capture process in a
2 2
Selexol unit for the capture plant
1 FuelHet1 Pressure drop=5 psia Simulate the fuel heater
(Heater) Temperature=290 F
2 FuelExpd Type: Isentropic Simulate the fuel expender which
(Compr) Discharge pressure=280 psia reduce the pressure of fuel to match
Isentropic efficiency=0.9 the requirement of gas turbine
combustor requirement
3 Satur Pressure drop=15 psi Simulate the fuel saturator, where
(Flash 2) Heat duty=0 But/hr water steam volume percentage in the
fuel is increased up to 16%
4 FuelHet2 Pressure drop=5 psia Simulate the fuel heater which heat
(Heater) Temperature=401 F the fuel to a temperature of 401 F
Figure 3 - 7 Fuel saturation and reheat section flowsheet of the reference plant
For the capture plant, fuel from the Selexol unit is sent to another Selexol unit for
CO capture, which is simulated by the block CO Sep. The CO capture efficiency and
2 2 2
power consumption is calculated based CO capture model, which will be discussed later.
2
Fuel after CO capture is heated up by the hot water from syngas saturator. The fuel
2
heater is simulated by the block FuelHet1. The heated fuel is expended in a turbine
82

expender to generate electricity, and its pressure is reduced to match the pressure at the
gas turbine combustor. Fuel from the expender enters the saturator to mix the
intermediate pressure saturation water to added warm steam in the syngas. Before
entering the gas turbine combustion chamber, the saturated fuel is preheated by the
intermediate pressure steam from syngas cooling unit. Figure 3-8 illustrates the mass and
energy flows in the sulfur removal and recovery section, and Table 3-7 shows the
corresponding unit operations that are simulated in Aspen Plus.
Figure 3 - 8 CO capture, fuel saturation, and reheat section flowsheet of the
2
capture IGCC power plant
3.2.5. Gas turbine section
The gas turbine section design bases on the GE 7FA gas turbine system. Although
the original turbine design specifications are based on a natural gas rather than a coal
derived syngas, GE heavy-duty gas turbines have operated successfully burning alternate
gaseous fuels with heating values ranging from 11.2 to 116 MJ/m3 (300 to 3100 Btu/ft3
lower heating value) [Foster, 2003]. Figure 3-9 illustrates the mass and energy flows in
83

gas turbine section, and Table 3-8 shows the corresponding unit operations that are
simulated in Aspen Plus.
The pressure ratio of GE 7FA is 15.5, hence the air at the ambient conditions (59 F,
14.7 psia, and 60 percent relative humidity) is compressed up to 230 psia at a three-stage
compressor. The pressure ratio of each compression stage is one third of the total
pressure ratio. The compressor has several extraction points, from which some amount of
compressed air is removed and injected into the blades and vanes of the hottest turbine
stages for cooling. For GE 7FA gas turbine, approximately 11% of the total air flow rate
is used for gas turbine cooling.
The three-stage compressor is simulated by three units, GTComp1, GTComp2, and
GTComp3. The outlet pressures for these three stages are 37.82, 93.3 and 230 psia,
respectively. Three cooling air streams are moved at the outlet of each stage for turbine
cooling.
The saturated and reheated fuel and the air from the last stage of the compressor
enter the gas turbine combustion chamber, which is simulated by the block GTBurn. The
following chemical reactions are employed to simulate the combustion process:
2CO+O 2å2CO
2
2H
2
+O 2å2H
2
O
CH
4
+1.5O 2åCO+2H
2
O
2H
2
S+3O 2å2H
2
O+2SO
2
84

COS+1.5O 2åCO
2
+SO
2
2NH
3
+2.445O 2å0.1N
2
+1.71NO+0.09NO
2
+3H
2
O
N
2
+1.05O 2å1.9NO+0.1NO
2
An amount of intermediate pressure steam from the steam cycle is used for the
combustion chamber cooling. The cooling process is simulated by the block GT_Qloss.
The heated steam comes back to the steam cycle. The firing temperature of GE 7FA gas
turbine is approximately 2350 °F, this temperature is maintained by a Design
Specification TIT, which manipulates the inlet temperature of the first stage gas turbine
by adjusting the flow rate of the coal slurry.
Hot combustion product gases enter the three-stage turbines at pressures of 228,
92.45, 37.29 psia, respectively. The outlet pressure of the last stage turbine is 15.2 psia.
The three turbines are modeled by three blocks, GTTurb1, GTTurb2, and GTTurb3. The
exhaust temperature of GE 7FA is 1106 °F, which is maintained through a Design
Specific TEXHAUST. The hot exhaust gases enter the HRSG to produce steam for the
steam cycle.
The overall mass flow rate in a gas turbine is typically limited by the turbine nozzle.
When the March number at the turbine nozzle is unity, the flow at the inlet of gas turbine
expender is choked. The choke flow rate calculation used in this model based on the
model developed by Frey [Frey, 2001]. The design specification TCHOKE sets the flow
rate of air at the compressor inlet to meet the choked flow condition.
85

Figure 3 - 9 Gas turbine section flowsheet
86

Table 3 - 8 Gas turbine unit description
No Aspen unit ID Unit parameters Unit function
1 GTMix1 Simulate the mixing of fuel and the
(mixer) compressed air for gas turbine
combustion
2 GTMix2 Simulate the mixing of cooling air
(mixer) and the combustion products
3 GTMix3 Simulate the mixing of cooling air
(mixer) and the combustion products
4 GTMix4 Simulate the mixing of cooling air
(mixer) and the combustion products
5 GTComp1 Discharge pressure=37.82 psia Simulate the fist stage of gas turbine
(Compr) Isentropic=0.918 compressor
6 GTComp2 Discharge pressure=93.3 psia Simulate the fist stage of gas turbine
(Compr) Isentropic=0.918 compressor
7 GTComp3 Discharge pressure=230 psia Simulate the fist stage of gas turbine
(Compr) Isentropic efficiency=0.918 compressor
8 GTBurn Pressure=228 psia Simulate the gas turbine combustor
(RStoic) Heat duty=0 Btu/hr
9 GT_Qloss Pressure drop=0 psia Simulate the heat loss in the
(Heater) Temperature change=16 F combustor during to cooling process
10 GTTurb1 Discharge pressure=92.45 psia Simulate the first stage of the gas
(Compr) Isentropic=0.919 turbine
11 GTTurb2 Discharge pressure=37.49 psia Simulate the second stage of the gas
(Compr) Isentropic=0.919 turbine
12 GTTurb1 Discharge pressure=15.2 psia Simulate the third stage of the gas
(Compr) Isentropic=0.919 turbine
13 GTSplit1 This block splits the compressed air
(Split) from the first stage of the gas turbine
compressor for gas turbine first stage
rotor cooling
14 GTSplit2 This block splits the compressed air
(Split) from the first stage of the gas turbine
compressor for gas turbine second
stage vane cooling
15 GTSplit1 This block splits the compressed air
(Split) from the first stage of the gas turbine
compressor for gas turbine first stage
vane cooling
87

3.2.6. Steam cycle section
The major components of the steam cycle section include the heat recovery steam
generator, the steam turbines (high, intermediate, and low pressure), condenser, the steam
bleed for gas turbine cooling, the recycle water pump and heater, and the deaerator. As
discussed above, a three-pressure reheat HRSG is adopted for this IGCC system. The
major parameters of this HRSG are given in Table 3-9.
Table 3 - 9 STAG product line steam turbine throttle and admission steam
conditions
Heat Recovery Steam Cycle Reheat Three-Pressure
Throttle Pressure (psig) 1400
Throttle Temperature (°F) 1000
Reheat Pressure (psig) 300
Reheat Temperature (°F) 1000
IP Admission Pressure (psig) 300
IP Admission Temperature (°F) 20 Approach to Exhaust Gas Temperature
upstream of Superheater
LP Admission Pressure (psig) 40
LP Admission Temperature (°F) 20 Approach to Exhaust Gas Temperature
upstream of superheater
Steam cycle process
The three-pressure reheat steam cycle is shown schematically in Figure 3-10, and
Table 3-10 gives the corresponding operation units in the Aspen Plus model. The
feedwater coming from the steam turbine condenser is preheated up to 221.9 °F in the
feed water preheater, which is simulated by the block FWHeat. The heat recovered from
the sulfur recovery process/and steam removed from the low pressure turbine is used to
preheat the feed water. The preheated feedwater enters the deaerator, which is simulated
88

by the block Dearer. After deaeration, the feed water is compressed up to 52 psia, and
enters the low pressure economizer, which is simulated by the block LPEc. In the low
pressure economizer, the feedwater is heated up to 253° F. Part of the low pressure feed
water is used to generate the superheated low pressure steam at 42 psia/500 °F through
the low pressure evaporator, which is modeled by the block LPEvap, and the low
pressure superheater, which is modeled by the block LPSupH. Another amount of the
feedwater is compressed up to 360.2 psig, and heated up to 408 °F in the intermediate
pressure economizer, which is simulated by the block IPEc2. Part of the intermediate
pressure feed water is used to generate the superheated intermediate pressure steam at
303 psia/581 °F through the intermediate pressure evaporator, which is modeled by the
block IPEvap, and the intermediate pressure superheater, which is modeled by the block
IPSupH. Another part of the intermediate feedwater is compressed to 1824.4 psia, and
heated up to 585 °F in the high pressure economizer, which is molded by the block
HPEc3. The high pressure hot water enters the high pressure evaporator, which is
modeled by the block HPEvap, to generate the high pressure saturation steam.
Before entering the high pressure turbine, the high pressure saturation steam is
heated up to 1000 °F in the high pressure superheater, which is simulated by the block
HPSupH. Steam from the high pressure turbine at 336 psia/606 °F mixes with the
intermediate pressure superheated steam, then is heated up to 1000 °F after flowing
through the reheater, which is modeled by the block ReHeat. The reheated steam flows
through the intermediate turbine, which is simulated by block IPTur1 and IPTur2. The
steam from the intermediate turbine at 40 psia/501.9 °F mixes with the steam from the
low pressure superheater, and then passes through the low pressure turbine, which is
89

simulated by block LPTur1, and LPTur2. The steam from the low pressure turbine at 0.67
psia/93.5 °F is condensed at the condenser, which is modeled by the block Cond.
Figure 3 - 10 GE 7FA gas turbine and steam cycle section flowsheet
90

Table 3 - 10 Steam cycle section unit description
No Aspen unit ID Unit parameters Unit function
Discharge pressure=20 psia
1 PmpMK (PUMP) Simulate the make up feed water pump
Efficiency=default value
Discharge pressure=17 psia
2 CndPmp1 (Pump) Simulate the condensate water pump
Efficiency=default value
Indicate the mixing of make up feed
3 FWMix (Mixer)
water and the condensate water
Pressure=17 psia Simulate the pre-heater of the feed
4 FWHeat (Heater)
Vapor fraction=0 water
Indicate the mixing of feed water and
5 DearMix (Mixer)
the low pressure hot water
Pressure=16.3 psia
6 Deaer (Flash 2) Simulate the deaerator
Vapor fraction=0.005
Indicate a amount of feed water is split
7 LPLoop (Fsplit)
to the low pressure economizer
Discharge pressure=52 psia Simulate the low pressure feed water
8 LPPump (Pump)
Efficiency=default value pump
Pressure drop=4 psia Simulate the low pressure economizer
9 LPEc (Heater)
Temperature=253 F for low pressure steam generation
Indicate a amount of low pressure feed
10 SP_LPEc (Fsplit)
water is split to the deaerator
Simulate the low pressure evaporator,
Pressure drop=4 psia
11 LPEvap (Flash 2) where the blow down is 1% of the inlet
Vapor fraction=0.99
water
Pressure drop=-2 psia Simulate the low pressure steam
12 LPSupH (Heater)
Temperature=500 F superheater
Indicate a amount of feed water is split
13 SP_Pmps (Fsplit)
to the intermediate pressure economizer
Discharge pressure=360.2 psia Simulate the intermediate pressure
14 IPPmp (Pump)
Efficiency= default value pump
Pressure=342.1 psia Simulate the first intermediate pressure
15 IPEc1 (Heater)
Temperature=253 F economizer
Pressure=325 psia Simulate the second intermediate
16 IPEc2 (Heater)
Temperature=408 F pressure economizer
Simulate the intermediate pressure
Pressure=308.8psia
17 IPEvap (Flash 2) evaporator, where the blow down is 1%
Vapor fraction=0.99
of the inlet water
Pressure=303psia Simulate the high pressure steam
18 IPSupH (Heater)
Temperature=581 F superheater
91

Table 3 – 10 continued
No Aspen unit ID Unit parameters Unit function
Discharge pressure=1824.4 psia
19 HPPmp (Pump) Simulate the high pressure pump
Efficiency= default value
Pressure=1733.2 psia Simulate the first high pressure
20 HPEc1 (Heater)
Temperature=253°F economizer
Pressure=1646.5 psia Simulate the second high pressure
21 HPEc2 (Heater)
Temperature=408°F economizer
Pressure=1564.2 psia Simulate the third high pressure
22 HPEc2 (Heater)
Temperature=585°F economizer
Simulate the high pressure evaporator,
Pressure=1486psia
23 HPEvap (Flash 2) where the blow down is 1% of the inlet
Vapor fraction=0.99
water
Pressure=1400 psia Simulate the high pressure steam
24 IPSupH (Heater)
Temperature=1000°F superheater
Discharge pressure=336 psia
25 HPTur (Compr) Simulate the high pressure turbine
Isentropic efficiency=0.92
Indicate the mixing of superheat
26 Re_Mix (Mixer) intermediate pressure steam and the
steam from high pressure turbine
Pressure=300 psia
27 ReHeat (heater) Simulate the steam reheater
Temperature=1000°F
Discharge pressure=60 psia Simulate the first stage of the
28 IPTur1 (Compr)
Isentropic efficiency=0.92 intermediate pressure turbine
Discharge pressure=40 psia Simulate the second stage of the
29 IPTur2 (Compr)
Isentropic efficiency=0.92 intermediate pressure turbine
Indicate the mixing of low pressure
30 LPMix (Mixer) superheat steam and the steam from the
intermediate turbine
Discharge pressure=24 psia Simulate the first stage of the low
31 LPTur1 (Compr)
Isentropic efficiency=0.89 pressure turbine
Indicate a amount of low pressure
32 BleedLP (Fsplit) steam is removed to the feed water pre-
heater
Discharge pressure=0.67 psia Simulate the second stage of the low
33 LPTur2 (Compr)
Isentropic efficiency=0.89 pressure turbine
Simulate the condenser, where the
Pressure=0.6252
34 Cond (Heater) steam from the last stage of the low
Vapor fraction=0
pressure turbine is condensed
92

Design specifications of the steam cycle
• Gas turbine exhaust stack temperature
In general, the HRSG stack temperature should be kept as low as possible to extract
as much gas turbine exhaust energy as possible to maximize cycle efficiency.
Occasionally, a concern with high sulfur gas turbine fuels is acid condensation on low
temperature heat transfer surfaces. In these cases, a low pressure turbine extraction may
be used to heat feedwater above the acid dew point prior to feedwater supply to the
HRSG economizer. In this study, the stack temperature of the gas turbine exhaust gases is
set to be 230 °F. This temperature is maintained by the design specification TSTACK,
which can adjust the feed water flow rate of the HRSG to meet the requirement of the
stack temperature.
• Pinch, sub-cool, and approach temperature
As shown in Figure 3-11, the pinch temperature is the temperature difference
between the gas turbine exhaust temperature and the temperature of saturation water at
the inlet of evaporator. The approach temperature is the temperature difference between
the main steam temperature and the GT exhaust temperature. The sub-cool temperature is
the temperature difference between the water temperature at the outlet of the economizer
and the temperature of the saturation water.
93

Figure 3 - 11 Typical exhaust gas temperature profile of one pressure system
If the pinch temperature and the approach temperature are too big, the gas turbine
exhaust energy will not be utilized efficiently. On the other hand, if they are too small,
heat transfer area will be very large, which will raise the capital cost. Generally, the pinch
temperature rage is from 8 to 20 °C, and the approach temperature range from 5 to 20 °C.
In order to avoid some of hot water in economizers evaporating, typically the sub-cool
temperature range is from 5 to 20 °C. The temperature profile of this three-pressure
reheat HRSG is shown by Figure 3-12.
The approach temperature and the sub-cool temperature can be satisfied by setting
the main steam temperature and the outlet temperature at the outlet of an economizer.
The pinch temperature is satisfied through a design specification TPINCH, which adjusts
the feedwater flow rates entering the high, intermediate, and low pressure economizers.
94

Figure 3 - 12 Typical exhaust gas/steam cycle temperature profile for three-
pressure reheat HRSG system
3.2.7. Convergence sequence of the IGCC model
Using the sequential-modular (SM) strategy, Aspen Plus performs flowsheet
calculations by executing each unit operation block in sequence, and using the calculated
output streams of each block as feed to the next block. When flowsheets with recycle
loops, design specifications, or optimization problems, it must be solved iteratively. In
this study, the convergence sequence is based on eleven design specifications and seven
calculators with FORTRAN blocks. Some of them are mentioned in earlier sections of
this report and the rest are elaborated upon in this section.
The water to coal ratio is varied by the FORTRAN block H2OCOAL in order to
meet the specified coal slurry composition. The elemental composition of coal
decomposition is calculated by the FORTRAN block DECOM based on the ultimate
composition analysis of the coal.
95

The FORTRAN block BSAIR maintains the air flow rate entering the combustion
reactor of the SCOT process based on the stoichiometric calculation. The FORTRAN
block CLAIR maintains the air flow rate entering the first reactor of the Claus process
based on the stoichiometric calculation. The flow rate of the make up feedwater for the
steam cycle is determined by the FORTRAN block STMAKUP, which takes into account
the blowdown in the IGCC system.
3.3. IGCC Cost Model
The cost models for oxygen-blown Texaco quench IGCC systems are developed
through updating a previous IGCC cost model developed by Frey [Frey, 1993]. The
references used for updating the cost model are given by the following table.
Table 3 - 11 References used for updating the IGCC cost model
Report No. Company Authors Year Sponsor Gasifier
1. Evaluation of Innovative Parsons W. Owens, 2000 DOE/EPRI E-gas
Fossil Fuel Power Plants
with CO Removal
2
2. Texaco Gasifier IGCC Base EG&G W. Shelton 2000 NETL Texaco
Cases J. Lyons
3. KRW Gasifier IGCC Base EG&G W. Shelton 2000 NETL KRW
Cases J. Lyons
4. Shell Gasifier IGCC Base EG&G W. Shelton 2000 NETL Shell
Cases J. Lyons
5. A single IGCC design for GE/Texac O’Keefe 2002 Texaco
variable CO capture o L.F.
2
Griffiths J.
6. Market-Based Advanced DOE 1999 DOE Destec
Coal Power Systems
7. Shift reactors and physical P. Chiesa 1999 Texaco
absorption for Low-CO S. Consonni
2
emission IGCCs
96

For the purpose of estimating the direct capital cost of the plant, the IGCC system is
divided into thirteen process areas as listed in the following table. The following section
gives the direct cost of each process area in a dollar value at 2000 year.
Table 3 - 12 IGCC system process areas
No. Cost section
1 Coal handling:
2 Oxidant feed
3 Gasification
4 LTGC
5 Selexol
6 Claus plant
7 Beavon-Stretford
8 Boiler feedwater treatment
9 Process condensate treatment
10 Gas turbine
11 HRSG
12 Steam turbine
13 General facilities
3.3.1. Oxidant Feed Section
This process section typically has an air compression system, an air separation unit,
and an oxygen compression system. The direct cost depends mostly on the oxygen feed
rate to the gasifier, as the size and cost of compressors and the air separation systems are
proportional to this flow rate. The direct cost model for the oxidant feed section is:
N T0.067 M
DC =196.2 T,OF a ( O,G,i)0.5618 (R2=0.86).....(3-1)
OF 1−η 0.073 N
ox O,OF
97

N N
where T,OF, O,OF = the total trains of ASU and the total operating trains of ASU,
separately.
T (0F)= Ambient air temperature; 20≤T ≤95; 0F
a a
M (lbmole/hr) = Gasifier oxygen inlet flow rate;
O,G,i
M
625≤ O,G,i ≤17000 lbmole/hr
N
O,OF
η = oxygen purity;0.95≤η ≤0.98
ox ox
This regression is based on the equation developed by Frey [Frey, 1993], and
revised using data from reports [3], [5-7]. Figure 3-13 gives the data points used for this
regression.
120000
100000
80000
60000
40000
20000
0
0 5000 10000 15000 20000
Oxidant feed section cost (k$ in 2000)
98
)rh/elom
bl(
etarwolf
telni
negyxo
reifisaG
Ref. 6
Ref. 7
Ref. 3
Ref. 5
Figure 3 - 13 Oxygen flow rate vs. oxidant feed section cost

3.3.2. Coal Handling Section and Slurry Preparation
Coal handling involves unloading coal from a train, storing the coal, moving the
coal to the grinding mills, and feeding the gasifier with positive displacement pumps.
Slurry preparation trains consist of vibrating feeders, conveyors, belt scale, rod mills,
storage tanks, and positive displacement pumps to feed the gasifier. Coal feed rate to
gasifier on as-received basis is the most common and easily available independent
variable. The direct cost model for the coal handling is based on the overall flow to the
plant rather than on per train basis.
DC =8.27M (R2=0.8) (3-2)
CH CF,G,i
where M (tons/day):Gasifier as-received coal feed flow rate; 2,800~25,000
CF,G,i
tons/day.
This regression is based on the equation developed by Frey [Frey, 1993], and
revised using data from reports [3-5], and [7]. Figure 3-14 gives the data points for coal
handling section cost analysis.
99

50000
45000
40000
35000
30000
25000
20000
15000
10000
5000
0
0 2000 4000 6000
Gasifier as-received coal feed flow rate
(ton/d)
100
)0002
ni
$k(
tsoc
noitces
gnildnah
laoC
Ref. 7
Ref. 3
Ref. 4
Ref. 5
Figure 3 - 14 Coal handling section cost vs. coal feed flow rate
3.3.3. Gasification Section
The Texaco quench gasification section of an IGCC plant contains gasifier, gas
scrubbing, gas cooling, slag handling, and ash handling sections. The direct capital cost
model is a function of the as-received coal flow rate.
DC = 24770N ln(M /N )−167453 (3-3)
G T,G CG,G,i O,G
where N N = the total trains of gasifier and the total operating trains of
T,G, O,G
gasifier, separately.
M (tons/day) = Gasifier as-received coal feed flow rate; 1,300~3,300
CF,G,i
tons/day.
This regression is based on data from reports [1] and [3]. The data points are given
in Figure 3-15.

40000
35000
30000
25000
20000
15000
10000
5000
0
0 1000 2000 3000 4000
Gasifier cost (k$ in 2000)
101
)d/not(
etar
wolf
laoc
deviecer-sa
reifisaG
Ref. 3
Ref. 1
Figure 3 - 15 Coal flow rate vs. gasifier cost
3.3.4. Low temperature gas cooling
The low temperature gas cooling section consists primarily of a series of shell and
tube heat exchangers. The syngas mass flow is assumed to be the major determinant of
the process area capital cost as in the original cost model.
0.9
⎛M ⎞
DC =0.0519N ⎜ syn,LT,i ⎟ (R2=0.92) (3-4)
LT T,LT⎜ N ⎟
⎝ O,LT ⎠
where N N = the total trains and the total operating trains of low
T,LT, O,LT
temperature gas cooling, separately.
M (lb/hr) = syngas inlet flow rate of low temperature gas cooling section,
syn,LT,i
⎛M ⎞
650,000≤⎜ syn,LT,i ⎟≤1,300,000
⎜ N ⎟
⎝ O,LT ⎠
This regression is based on the data from reports [3-5]. The data points are shown in
Figure 3-16.

25000
20000
15000
10000
5000
0
0 200000 400000 600000 800000 1000000 1200000 1400000
Syngas flow rate (lb/hr)
102
noitces
gnilooc
sag
erutarepmet
woL
Ref. 3
Ref. 4
Ref. 5
Figure 3 - 16 Low temperature gas cooling system cost vs. the syngas flow rate
3.3.5. Selexol Section
Hydrogen sulfide in the syngas is removed through counter-current contact with the
Selexol solvent. The cost of the Selexol section include the acid gas absorber, syngas
knock-out drum, syngas heat exchanger, flash drum, lean solvent cooler, regenerator air-
cooled overhead condenser, acid gas knock-out drum, regenerator reboiler, and pumps
and expanders associated with the Selexol process. The direct capital cost model for the
Selexol section is:
0.304N M
DC = T,S ( syn,S,i)0.98 (R2=0.94) (3-5)
S (1−η )0.059 N
S O,S
where N N = the total trains and the total operating trains of Selexol section
T,S, O,S
for H S capture, separately.
2
η S (%) = the H 2 S capture efficiency of Selexol system, 83.5%~99.7%.

M (lbmol/hr) = syngas inlet flow rate of Selexol section. 2,000~67,300
syn,S,i
lbmol/hr
This regression is based on the equation developed by Frey [Frey, 1993], and
adjusted with the chemical engineering price index.
3.3.6. Claus sulfur recovery Section
The Claus plant contains a two-stage sulfur furnace, sulfur condensers, and
catalysts. It cost is estimated as a function of the element sulfur outlet flow rate of the
Claus unit.
M
DC =6.96N ( S,C,o)0.668 (R2=0.97) (3-6)
C T,C N
O,C
where N N = the total trains and the total operating trains of Claus section
T,C, O,C
for sulfur capture, separately.
M (lb/hr) = the element sulfur outlet flow rate of the Claus, 695~18,100.
S,C,o
This regression is based on the equation developed by Frey [Frey, 1993], and
adjusted with the chemical engineering price index.
3.3.7. Beavon-Stretford Tail Gas Removal Section
The capital cost of a Beavon-Stretford unit is expected to vary with the volume flow
rate of the input gas stream and with the mass flow rate of the sulfur produced.
M
DC =63.3+72.8N ( S,BS,o)0.645 (R2=0.99) (3-7)
BS T,BS N
O,BS
103

where N N = the total trains and the total operating trains of Beavon-
T,BS, O,BS
Stretford for sulfur capture, separately.
M (lb/hr) = the element sulfur outlet flow rate of Beavon-Stretford, 75~1,200.
S,BS,o
This regression is based on the equation developed by Frey [Frey, 1993], and
adjusted with the chemical engineering price index.
3.3.8. Boiler Feedwater System
The boiler feedwater system consists of equipment for handling raw water and
polished water in the steam cycle, including a water mineralization unit for raw water, a
dimineralized water storage tank, a condensate surge tank for storage of both
dimineralized raw water and steam turbine condensate water, a condensate polishing unit,
and a blowdown flash drum. The cost model considers both raw water flow rate through
the demineralization unit and the polished water flow rate through the polishing unit. The
polished water includes steam turbine condensate and makeup water, and condensate
from the miscellaneous process users such as waste water treatment.
DC =0.16M0.307M0.435 (R2=0.99) (3-8)
BFW rw pw
where M (lb/hr) = the flow rate of raw water, 24,000~614,000.
rw
M (lb/hr) = the flow rate of polished water in the steam cycle,
pw
234,000~3,880,000
This regression is based on the equation developed by Frey [Frey, 1993], and
adjusted with the chemical engineering price index.
104

3.3.9. Process Condensate Treatment
The process condensate treatment area consists of strippers, air cooled heat
exchangers, and knock-out drums. It is expected that the process condensate treatment
direct cost will depend primarily on the scrubber blowdown flow rate.
M
DC =10670( SBD )0.6 (3-9)
PC 300000
where M (lb/hr)= the blowdown flow rate.
SBD
This regression is based on the equation developed by Frey [Frey, 1993], and
adjusted with the chemical engineering price index.
3.3.10. Gas Turbine Section
A number of design factors affect the cost of a gas turbine in an IGCC system. In
this study, the cost model for the gas turbine was developed for a GE Frame 7F gas
turbine.
DC =168MW (R2=0.92) (3-10)
GT e
where, MW = the net output of GE7F gas turbine (MW).
e
This regression is based on the data from reports [3] and [7]. The data points used
for regression are given in Figure 3-17.
105

70000
60000
50000
40000
30000
20000
10000
0
0 100 200 300 400 500
Gas turbine net output (MWe)
106
)0002
ni
$k(
tsoc
enibrut
saG
Ref. 7
Ref 3
Figure 3 - 17 Gas turbine cost vs. gas turbine net output
3.3.11. Heat Recovery Steam Generator
The HRSG is a set of heat exchangers in which heat is removed from the gas
turbine exhaust gas to generate steam, including the superheater, reheater, high pressure
steam drum, high pressure evaporator, and the economizers. The direct cost of the HRSG
is a simple regression model based on the high pressure steam flow rate to the steam
turbine.
M
DC = −5943+7.98×10−3N P1.526 ( hps,HR,o)0.242 (R2=0.96) (3-11)
LT T,HR hps,HR,0 N
O,HR
where N N = the total trains and the total operating trains of HRST,
T,HR, O,HR
separately.
P (lb/hr) = the high pressure steam mass flow rate of HRSG,
hps,HR,o
M
66,000≤( hps,HR,o)≤ 64,0000
N
O,HR

This regression is based on the equation developed by Frey [Frey, 1993], and
adjusted with the chemical engineering price index.
3.3.12. Steam Turbine
A typical steam turbine consists of the high-pressure, intermediate-pressure, and
low-pressure turbine stages, a generator, and an exhaust steam condenser. The cost model
is given by
DC =0.145W (R2=0.92) (3-12)
GT e
where W = the net output of gas turbine (kW), 200,000~500,000
e
This regression is based on the data from reports [6-7], which are shown in Figure
3-18.
40000
30000
20000
10000
0
0.E+00 5.E+04 1.E+05 2.E+05 2.E+05 3.E+05 3.E+05 4.E+05
Steam turbine net output (kW)
107
)0002
ni
$k(
tsoc
enibrut
maetS
Ref. 7
Ref. 6
Figure 3 - 18 Steam turbine cost vs. steam turbine net power output

3.3.13. General Facilities
The general facility section includes cooling water system, plant and instrument air,
potable and utility water, and electrical system. Most studies assume that the direct cost
of the general facilities is approximately 14%-17% of the direct costs of other sections. In
the present study the direct cost of the general facilities is assumed to be approximately
15% of the total direct cost of the above 12 sections. Based on the direct cost of each
section, the process facility cost of each section is estimated as 1.2 times of its direct cost
[Frey, 1993].
3.3.14. Total Capital Requirement of IGCC systems
The following cost and parameter estimation of IGCC systems follows the
principles given by the EPRI Technical Assessment Guide (1993), which is widely
considered the industry standard and has long been an authoritative source of cost and
performance information on advanced and conventional power generation, storage,
transmission and distribution.
The total process facilities cost (PFC) of the IGCC system is the summation of the
individual process facility costs. Based on the PFC, the engineering and home office
costs can be estimated. The engineering and home office costs include the costs
associated with: (1) engineering, design, and procurement labor; (2) office expenses; (3)
licensing costs for basic process engineering; (4) office burdens, benefits, and overhead
costs; (5) fees or profit to the architect/engineer. EPRI recommends that a value of 7 to
15 percent of the process facility cost as the engineering and home office cost.
Therefore, a value of 10 percent is used here as a default.
108

Project contingency costs reflect the expected increase in the capital cost estimate
that would result from a more detailed cost estimate for a specific site. Usually, project
contingency is assigned as a multiplier of the process facility cost. A typical value for the
project contingency for a preliminary level cost estimate, as defined by the EPRI
Technical Assessment Guide, is 20 percent.
Another major cost item is the process contingency. The process contingency is
used in deterministic cost estimates to quantify the expected increase in the capital cost of
an advanced technology due to uncertainty in performance and cost for the specific
design application. In the EPRI cost method, the process contingency is estimated based
on separate consideration of contingencies for each process section. The contingency is
expressed as a multiplier of the sum of the plant facility cost for each process area. The
process contingency decreases as the commercial experience with a process area
increases. For example, in a fully commercialized process that has been used in similar
applications, the process contingency may be zero. The ranges of process contingency
factors for IGCC systems are shown in Table 3-13.
109

Table 3 - 13 Process contingency of cost sections
Cost section Process contingency
Coal handling: 0.05
Oxidant feed 0.05
Gasification 0.15
LTGC 0
Selexol 0.1
Claus plant 0.05
Beavon-Stretford 0.1
Boiler feedwater treatment 0
Process condensate treatment 0.3
Gas turbine 0.125
HRSG 0.025
Steam turbine 0.025
General facilities 0.05
The total plant cost (TPC) is the sum of process facility cost, the engineering cost,
the process contingency, and the project contingency. An allowance for funds during
construction (AFDC) is calculated based on the TPC as a function of the amount of time
it would take to construct the plant. Methods for computing the AFDC are documented
elsewhere [EPRI, 1993] and are not repeated here. The total plant investment (TPI)
represents the sum of the total plant cost and the AFDC.
The final measure of the capital cost is the total capital requirement (TCR). The
TCR includes the total plant investment plus owner costs for royalties, startup costs, and
initial inventories of stock feed. Preproduction costs typically include one month of both
fixed and variable operating costs and two percent of total plant investment. Inventory
capital is estimated as 0.5 percent of total process capital excluding catalyst. The initial
catalyst cost requirement is estimated based on the unit price of the catalysts and their
110

volumes. The total capital cost and O&M cost calculation processes are given in Table 3-
14.
Table 3 - 14 Capital cost elements of an IGCC power plant
Capital cost elements Value
Total process facilities cost Sum of the PFC of each section
Engineering and home office 10% PFC
General facilities 15% PFC
Project contingency 20% PFC
Process contingency See Table
Total plant cost (TPC) = PFC+Engineering fee+General facilities+Project & Process
Allowance for funds during construction Calculated based on discount rate and
(AFDC) construction time
Royalty fees 0.5% PFC
Preproduction fees 1 moth fee of VOM&FOM
Inventory cost 0.5% TPC
Total capital requirement (TCR) = TPC+AFDC+Royalty fees+Preproduction fee+Inventroy
Fixed O&M cost (FOM)
Total maintenance cost 2% TPC
Maintenance cost allocated to labor 40% of total maintenance cost
Administration & support labor cost 30% of total labor cost
Operation labor $25/hour
Variable O&M cost (VOM)
Fuel cost Depends on coal type
Consumable See Table 3-15
111

The fixed operation and maintenance costs, including labor, administration and
support cost are estimated as a fraction of the total plant cost. The variable cost and
expenses associated with operating the plant include: the consumable and fuel cost. The
unit costs of consumable are given by Table 3-15.
Table 3 - 15 Unit costs of consumables (Source: IECM manual)
Material Unit cost Unit
Sulfuric acid 119.52 $/ton
NaOH 239.04 $/ton
Na2 HPO4 0.76 $/lb
Hydrazine 3.48 $/lb
Morpholine 1.41 $/lb
Lime 86.92 $/ton
Soda ash 173.85 $/ton
Corrosion Inh 2.06 $/lb
Surfactant 1.36 $/lb
Chlorine 271.64 $/ton
Biocide 3.91 $/lb
Selexol Solv. 1.96 $/lb
Claus catalyst 478.08 $/ton
B/S catalyst 184.71 $/ft^3
Fuel oil 45.64 $/bbl
Plant air ads. 3.04 $/lb
Water 0.79 $/Kgal
112

REFERENCES (CHAPTER 3)
1. IEA Greenhouse Gas R&D Program, 2003: Potential for improvement in gasification
combined cycle power generation with CO capture, IEA report, report number
2
PH4/19
2. Brdar R.D., Jones R.M., 2003: GE IGCC Technology and Experience with Advanced
Gas Turbines, GE Power Systems, GER-4207
3. Chase D.L., Kehoe P.T., 2003: GE Combined-Cycle Product Line and Performance,
GE Power Systems, GER-3574G
4. IEA, 2000: Modeling and simulation for coal gasification, IEA Coal Research 2000,
ISBN 92-9029-354-3
5. Foster A.D., Doering H.E., and Hilt M.B., 2003: Fuel flexibility in heavy-duty gas
turbines, GE Company, Schenectady, New York
6. IEA Greenhouse Gas R&D Program, 2003: Potential for improvement in gasification
combined cycle power generation with CO capture, IEA report, report number
2
PH4/19
7. Brdar R.D., Jones R.M., 2003: GE IGCC Technology and Experience with Advanced
Gas Turbines, GE Power Systems, GER-4207
8. Chase D.L., Kehoe P.T., 2003: GE Combined-Cycle Product Line and Performance,
GE Power Systems, GER-3574G
9. IEA, 2000: Modeling and simulation for coal gasification, IEA Coal Research 2000,
ISBN 92-9029-354-3
10. Foster A.D., Doering H.E., and Hilt M.B., 2003: Fuel flexibility in heavy-duty gas
turbines, GE Company, Schenectady, New York
11. Frey H. C., 2001: Probabilistic modeling and evaluation of the performance,
emissions, and cost of Texaco gasifier-based integrated gasification combined cycle
systems using ASPEN, Janu. 2001
12. Owens W., 2000: Evaluation of Innovative Fossil Fuel Power Plants with CO
2
Removal, 2000
13. Shelton W., Lyons J., 2000: Texaco Gasifier IGCC Base Cases, PED-IGCC-98-001,
last revision June 2000
14. Shelton W., Lyons J., 2000: NETL, KRW Gasifier IGCC Base Cases, PED-IGCC-98-
005, last revision June 2000
113

15. Shelton W., Lyons J., 2000: Shell Gasifier IGCC Base Cases, PED-IGCC-98-005,
last revision June 2000
16. O’Keefe L.F. Griffiths J., 2002: A single IGCC design for variable CO capture, Fifth
2
European Gasification Conference, April, 2002
17. Office of Fossil Energy, U.S. Department of Energy, 1999: Market-based advanced
coal power systems, Final report, May 1999
18. Chiesa P., Consonni S., 1999: Shift reactors and physical absorption for Low-CO
2
emission IGCCs, Journal of engineering for gas turbines and power, 121 (2): 295-305
APR 1999
19. Zhu, Yunhua, 2004: Evaluation of Gas Turbine and Gasifier-Based Power Generation
Systems, PhD Dissertation, North Carolina State University August 2004.
114

Chapter 4. PERFORMANCE AND COST MODEL OF WATER GAS SHIFT
REACTION SYSTEM
4.1. Introduction
The water-gas shift (WGS) reaction is an industrially important reaction, which is
also a key part of the CO capture system in an IGCC power plant, for it converts almost
2
all the CO in syngas into CO for CO capture before combustion. Without this
2 2
conversion via the water gas shift reaction, the pre-combustion CO capture from IGCC
2
would not be an attractive option due to the low CO partial pressure of CO in the raw
2 2
syngas. The reaction is given as follows [David, 1980].
CO + H 0 ↔ CO + H (4-1)
2 2 2
1
0.95
0.9
0.85
0.8
0.75
400 600 800 1000
Equilibrium temperature (F)
115
egatnecrep
noisrevnoc
OC
CO/H2O=1.5
CO/H2O=2
CO/H2O=2.5
CO/H2O=3
Figure 4 - 1 Effects of temperature and CO/steam on the CO conversion of the
WGS reaction (This figure is derived based on that the original molar
concentration ratios of CO to H O are 1.5, 2, 2.5, and 3, and the
2
original concentrations of CO and H equal zero)
2 2
This reaction is exothermic. Figure 4-1 shows the effect of the reaction temperature
of the water gas shift reaction on the equilibrium conversion of CO. Equilibrium will
favor CO conversion to CO at low temperatures. The equilibrium will also favor CO
2
conversion at high steam-to-CO ratios. The steam-to-CO ratio is determined by the

chemical process. For IGCC systems with CO capture, the steam required is
2
supplemented by existing upstream steam or water quench addition.
4.2. Effects of operation temperature and two-stage shift reaction system
Practically, the water gas shift reaction occurs in an adiabatic system with the
presence of a catalyst accelerating the reaction rate. In an adiabatic system, the CO slip is
determined by the exit temperature of the shift reactors, because low temperatures result
in low equilibrium levels of CO. On the other hand, favorable kinetics occurs at higher
temperatures. Either high steam-to-gas ratio or low temperature can improve CO
conversion percentage, but it also requires higher capital and operation cost. Hence, there
is a tradeoff between CO conversion percentage and costs.
Conversion in a single reactor is equilibrium limited. As the reaction proceeds, the
rise in temperature due to the exothermal reaction eventually restricts further reaction.
This limitation can be overcome with a two stage water gas shift reaction--a high
temperature shift reactor followed by a low temperature shift reactor. An inter-bed
cooling process is employed between the two reactors to keep the reaction occurring at
low temperature in the second reactor. Attainment of low equilibrium CO slip from the
low temperature reactor is critical to the efficient and economic operation of plants. A
typical CO variation in a two stage shift reactors is shown in Figure 4-2.
116

Figure 4 - 2 Typical CO variation in high temperature shift and low temperature
shift catalyst beds [Frank, 2003a]
4.3. Clean shift catalysts
Gases used in water gas shift reactors often contain sulfur component, such as H S
2
and COS. These sulfur components have a detrimental effect on the activation of some
shift catalysts, which will be poisoned and lose activation in the presence of sulfur
components. On the other hand, sulfur components are necessary to maintain the
activation of some other shift catalysts. For the former type of shift catalysts, sulfur
components must be removed from reaction gases before the water gas shift reaction.
Hence this type of catalysts is so-called “clean shift catalyst”. A schematic flowsheet of
coal gasification system with a clean water gas shift reaction is given in Figure 4-3. The
syngas from the gasifier is cooled down, and fed to the soot scrubber to remove the bulk
of the carbon. Then it is further cooled for sulfur removal. Before passing to the shift
reactors, steam is added to the syngas to meet requirements of steam-to-carbon ration.
The inlet temperature of the second stage of the shift reaction is controlled by the
feed/effluent heat exchanger.
117

Figure 4 - 3 Coal gasification system with a clean water gas shift reaction
As mentioned above, a low operating temperature will give the most favorable
thermodynamic equilibrium and hence the minimum slip of carbon monoxide. For a two-
stage shift reaction system, the ideal operation is the low temperature shift reactor with
the lowest possible inlet temperature. There are two boundaries which limit the operation
temperature of the low temperature shift reactor. One is the activity of the catalyst at
lower temperature; the other is the dew-point of the process gases because condensation
on shift catalyst will weaken the clean catalyst pellets at low temperatures [Frank, 2003].
It has been reported that a low pressure plant was able to operate the low
temperature shift reactor at an inlet temperature of only 340 °F, because of the low dew-
point of the process gas [Frank, 2003a]. The dew-point of the process gas increases with
the increase of pressure. Hence, for high pressure cases it is the dew point, not the
activity of the catalyst, is more likely to be an operating limitation. IGCC systems usually
operate at a pressure high enough to allow the low temperature shift reaction to be
operated close to the dew point of the process gas. A safety margin above the dew point
should be used to ensure complete evaporation of water droplets that may form in the
cooler. This is adopted as a design criterion for a water gas shift reaction in an IGCC
system with a clean shift reaction.
118

For a two-stage shift reaction with clean shift catalysts, the iron-based catalyst is the
common commercially available high temperature catalyst. The commonly used low
temperature clean shift catalysts are copper-based. Both high temperature and low
temperature catalysts require activation by in situ pre-reduction steps. Since both
catalysts burn up when exposed to air (pyrophoric), they must be sequestered during
system shutdown when only air flows through the system [Frank 2003a].
The lifetimes of Cu-based catalysts and Fe-based catalysts are determined by the
poison-absorbing capacity of the catalysts. These poisons are inevitably present in the
process gas, such as syngas from coal gasification, or introduced with steam. As
mentioned above, the key poison in syngas is sulfur. Hence a sulfur removal process is
required upstream of the water gas shift reaction.
4.4. Sulfur tolerance shift catalysts
The so-called sour shift catalysts are sulfur tolerant, and sulfur is required in the
feed gas to maintain the catalyst in the active sulphided state. This type of catalyst is
usually cobalt-based.
Figure 4-4 shows the schematic process of a gasifier system with a sour shift
reaction. The syngas from the gasifier is quenched, and then the saturated syngas is fed to
the soot scrubber, to remove the bulk of particles before passing to the sour shift reactors.
The inlet temperature of the second stage of the shift reaction is controlled by the cooling
process. After heat recovery, the cooled syngas from the second shift reactor is passed to
the sulfur removal system.
119

Figure 4 - 4 Schematic process of a gasifier system with a sour shift
The sour shift catalyst has demonstrated its high and low temperature performance,
ranging from 210°C to 480°C, and work properly up to a pressure as high as 1160 psia
[Frank, 2003b]. Because the catalyst is not impregnated with a water-soluble promoter it
can be operated closer to the dew point and will not lose activity when wetted
occasionally.
In a gasification plant, the average catalyst life in the first stage shift reactor was 2.5
years, and 5-8 years in the second reactor [Frank, 2003b]. The difference in catalyst life
in the two reactors is highly influenced by the gas quality. These data of catalysts’
lifetime are adopted for the estimation of the operation and maintenance cost of the water
gas shift reaction system.
4.5. Performance model of the water-gas shift reaction process
This section presents the performance model developed for the WGS reaction
process. This is a general performance model for a two-stage shift system with either
clean shift catalysts or sulfur tolerant shift catalysts. The purpose of the performance
model is to characterize the change in syngas composition and flow rate as a function of
inlet condition to the WGS reactor and key design parameters of the WGS system. The
performance model also characterizes the heat integration between the shift reaction
system and the steam cycle system.
120

A general water gas shift reaction process model is illustrated in Figure 4-5. The
black box in this figure includes a high temperature reactor, a low temperature reactor
and several heat exchangers for heat recovery. The performance of the shift reaction was
first modeled in the Aspen Plus. In this model, the syngas from a gasifier is mixed with
steam or quenched at a given temperature and pressure, and then fed into the high
temperature reactor. Most of the CO in the syngas is converted to CO in the high
2
temperature reactor at a fast reaction rate. Because the water gas shift reaction is
exothermic, the syngas from the high temperature reactor has to be cooled before being
fed into the low temperature reactor. Further CO conversion is achieved in the low
temperature reactor. The shifted syngas from the low temperature reactor is cooled down
again for subsequent CO capture in a Selexol process. Part of the heat from syngas
2
cooling is used to heat the fuel gas from Selexol process, and the other part of the heat is
integrated into the steam cycle.
In this model, the reactions in the two reactors are assumed to achieve equilibrium
states. On the other hand, the shift reaction in a real reactor only approaches an
equilibrium state. In order to compensate for the difference between the equilibrium state
assumption and the real state in a reactor, the approach temperature method is used to
adjust the model equilibrium temperatures. The difference between the model
temperature and the design reaction temperature is referred to as the approach
temperature. The approach temperature is determined through comparing model outputs
with practical data from shift reactors in the industry field. Thus, with the approach
temperature, the reactor model is assumed to reach an equilibrium state at a higher
121

temperature than the design temperature, which makes the CO conversion efficiency in
the model to match the realistic situation.
Figure 4 - 5 Mass and energy flow of the water gas shift reaction system
The Aspen model had been executed thousands of times with varying the inlet
temperature, pressure and syngas composition. The value ranges of these parameters are
given in Table 4-1 which covers the possible ranges of gasification operation. The inlet
temperature was varied in a step of 30 F, and the inlet pressure was varied by a step of
100 psia. At the same time, 50 different syngas compositions were used. A total of 9000
cases were run. Based on the Aspen simulation results, statistical regression methods
were then used to develop relationships between the inlet conditions and the final
products of the WGS reaction. Using these regression relationships, the entire water gas
shift reaction system can be treated as a “black box” when it is used in the IECM
framework.
122

Table 4 - 1 Range of model parameter values for the WGS reaction system
Parameter Inlet Inlet CO in H in CO in H O in CH in
2 2 2 4
temperature pressure the the the the the
(F) (psia) syngas syngas syngas syngas syngas
(vol%) (vol%) (vol%) (vol%) (vol%)
Value 440-755 150-1500 20-60 15-55 5-30 5-30 0.5-20
4.5.1. Input and output parameters of the WGS performance model
The input and outlet parameters of this model include the temperature, pressure, and
flow rates of the inlet and the outlet syngas as shown in Table 4-2. The input parameters
are used to calculate reaction rates and the composition changes after the reaction.
Table 4 - 2 Input and output parameters of the WGS reaction system
Input parameter Output parameter
Syngas Temperature (F) Shifted Temperature (F)
from syngas
Pressure (psia) Pressure (psia)
gasifier
Flow rate (lb-mole/hr) Flow rate (lb-mol/hr)
Molar concentrations of Molar concentration
CO, CO , H O, H , N , CH CO, CO , H O, H , N , CH
2 2 2 2 4 2 2 2 2 4
Steam/carbon molar ratio Reaction rate & Catalyst volume (ft3)
Feed Pressure (psia) HP & IP Temperature (F)
water steam
Temperature (F) Flow rate (lb-mol/hr)
4.5.2. Performance model output
This section discusses the performance outputs of this model. In this section, the
CO to CO conversion is defined and calculated using the chemical equilibrium constant.
2
The outlet temperatures and syngas composition of the two shift reactors are regressed
from Aspen model simulation results. The heat released from the syngas cooling is also
quantified for the energy balance calculation of the whole IGCC system. The detailed
calculation processes of CO conversion efficiency and catalyst volumes are given in
123

Appendix A and B. Appendix C shows the practical utilization of this model through a
case study.
Shifted syngas composition
The water gas shift reaction occurring in both the high and low temperature reactors
changes the concentration of syngas species and the temperature of the syngas. The CO
conversion efficiency (ξ) can be used to show how much CO is converted into CO
2
in
one reactor or in two reactors.
CO flowrate in(lb⋅mol/hr)−CO flowrate out(lb⋅mol/hr)
(4-2)
ξ =
CO flowrate in(lb⋅mol/hr)
A numerical model is set up to calculate the CO conversion in a shift reactor for
given inlet parameters. The detailed calculation process is given in Appendix A.
Based on the definition of the CO conversion and stoichiometric factors of the
reaction, the CO concentration of syngas exiting the high temperature reactor is given by,
[CO] =[CO] ⋅(1−ξ ) (4-3)
h,o 0 h
where [CO] = the molar concentration of CO in the syngas exiting the high
h,o
temperature reactor
[CO] = the molar concentration of CO in the syngas entering the high temperature
0
reactor
ξ = the CO conversion in the high temperature reactor
h
124

Based on the shift reaction (Eq. 4-1) and the definition of CO conversion, the molar
concentrations of H , CO and H O after the high temperature reactor are given by,
2 2 2
[CO ] =[CO ] +[CO] ⋅ξ (4-4)
2 h,o 2 0 0 h
[H ] =[H ] +[CO] ⋅ξ (4-5)
2 h,o 2 0 0 h
[H O] =[H O] −[CO] ⋅ξ (4-6)
2 h,o 2 0 0 h
Using the CO conversions definition and Equation (4-3), the CO concentration of
shifted syngas after the low temperature reactor is to be given by,
[CO] =[CO] ⋅(1−ξ ) (4-7)
l,o 0 tot
where [CO] = the molar concentration of CO in the syngas exiting the low
l,o
temperature reactor
ξ = the total CO conversion in the high and low temperature reactors
tot
Then the concentrations of H , CO and H O after the low temperature reactor are
2 2 2
given by,
[H ] =[H ] +[CO] ⋅ξ (4-8)
2 l,o 2 0 0 tot
[CO ] =[CO ] +[CO] ⋅ξ (4-9)
2 l,o 2 0 0 tot
[H O] =[H O] −[CO] ⋅ξ (4-10)
2 l,o 2 0 0 tot
125

Flow rate of high pressure saturation steam
In the following two sections, temperature changes and flow rates of water and
syngas are calculated, and then used for the following cost model.
Syngas from the high temperature reactor is cooled down to a temperature which is
determined by the dew point of syngas before it is fed into the low temperature reactor.
According to the heat integration design, heat from the exothermic reaction is recovered
to generate high pressure saturated steam for the steam cycle.
The temperature of the saturation steam is determined by the high pressure steam
cycle in the power block. Using the data from the ASME steam and water table (1967),
the temperature is given by the following regression equation:
T (F) =328.34+0.3565P −0.0002P2 +6⋅10−8P3 −7⋅10−12P4
sc sc sc sc
w,sat
(R2=0.99) (4-11)
where P (psia) = the pressure of steam cycle, (300 ~ 3000 psia)
sc
The heat released by the syngas after the high temperature reactor is determined by,
Q (Btu/hr) =q ⋅f (4-12)
HE1 HE1 SG,0
where f = the total molar flow rate of syngas entering the high temperature
SG,0
reactor (lb-mole/hr);
q = the heat released per lb-mole syngas after the high temperature reactor,
HE1
which is regressed and given by (Btu/lb-mole),
126

q (Btu /lbmol) = P0.0360T1.2874[CO]1.14347[CO ]−0.4734
HE1 0 0 0 2 0 (R2=0.95) (4-13)
[H O]0.3150[H ]0.0003[N ]0.0139
2 0 2 0 2 0
where P = the pressure of syngas entering the high temperature reactor (psia)
0
T = the temperature of syngas entering the high temperature reactor (F)
0
[i] =the molar concentration of species i entering the high temperature reactor
0
Based on the total heat available and the saturation temperature, the flow rate of the
saturation high pressure steam ( f , lb-mole/hr) can be calculated by the following
HPS
equation,
Q
f = HE1 (4-14)
HPS (h −h )
T T
w,sat 0
where h = the enthalpy of the steam at the saturated temperature (Btu/lb-mole)
T
w,sat
h = the enthalpy of high pressure feed water at the inlet temperature (Btu/lb-mole).
T
0
Flow rate and temperature of the intermediate pressure steam
The syngas from the low temperature reactor is cooled to 100 F for sulfur removal,
and the heat is recovered to generate the intermediate pressure steam. The total heat Q
tot
(Btu/hr) released when the syngas from the low temperature reactor is cooled down to
100 °F is given by,
127

Q =f (9.255⋅T −0.316⋅P −1386.1⋅[CO] −297.779⋅[CO ] −1485.34⋅[H ]
tot l,o l,o l,o l,o 2 l,o 2 l,o
+17595.87⋅[H O] −1439.29⋅[N ] −331.533⋅[CH ] )
2 l,o 2 l,o 4 l,o
(R2=0.95) (4-15)
where f = the molar flow rate of syngas exiting the low temperature reactor (lb-
l,o
mole/hr);
T = the syngas temperature at the outlet of the second reactor
l,o
P = the syngas pressure at the outlet of the second reactor
l,o
[i] = the molar concentration of species i at the outlet of the second reactor
l,o
In order to meet the approach temperature requirement in the superheater, the final
temperature of the intermediate pressure steam (T ) is set to be 10 F lower than the
HPS
outlet temperature of the syngas from the second shift reactor, and the feedwater
temperature is set to be 59 F. Hence the flow rate of the intermediate pressure steam
( f , lb-mole/hr) is given by,
IPS
(f + f )⋅(h −h )+ f ⋅(h −h ) =Q (4-16)
HPS IPS IP FW IPS IPS IP tot
sat sat
where f = the flow rate of the high pressure saturation steam (lb-mole/hr)
HPS
h = the enthalpy of the intermediate pressure saturation water at the inlet
IP
sat
temperature (Btu/lb-mole)
h = the enthalpy of the feedwater (Btu/lb-mole)
FW
128

h = the enthalpy of the final intermediate pressure steam (Btu/lb-mole)
IPS
4.6. Cost model of WGS reaction process
This section presents the economic model developed for the water gas shift reaction
process. The cost model is comprised of the capital cost model and the annual operating
and maintenance (O&M) cost model. The capital cost of the WGS reaction system
includes the following major process areas: the first stage shift reactor, the second shift
reactor and the cooling units. For each of these major areas, its process facilities cost
model is developed at first.
4.6.1. Process facility cost
The process facility cost of the reactor includes the reaction vessel, structural
supports, dampers and isolation valves, ductwork, instrumentation and control, and
installation costs. The reactor vessels are made of carbon steel. The process facility costs
of the shift reactors are estimated based on the reactor volumes, which is assumed to be
1.2 times the catalyst volume [Doctor, 1994]. The catalyst volume calculation process is
described in Appendix A.
Process facility cost of shift reactors
The process facility costs of the high and low temperature shift reactors are
regressed as a function of reactor volume and operation pressure using the data in Table
4-3.
1.2V
PFC = 0.9927 ⋅N [17.6487( cat.)0.4883P 2.028] (R2=0.9) (4-17)
R T,R N R
O,R
129

where PFC = the process facility cost of the reactor (US$ in 2000)
R
N = the total number of the reactor trains
T,R
N = the number of the reactor operating trains
O,R
V = the volume of catalyst (m3)
cat.
P = the operation pressure of the reactor (atm)
R
Table 4 - 3 Water gas shift reactor cost data adjusted to the dollar value in 2000
[Doctor, 1996]
Cost ($ in 2000) Reactor volume(m3) Pressure(atm)
82864.8 22.6 31.1
38692.2 34 18.7
59189.0 9.684 31.0
21495.0 11.553 18.7
Process facility cost of heat exchangers
In this model, two types of heat exchangers are used, which are the gas-liquid type,
and the gas-gas type. Generally, the cost of a heat exchanger depends on its heat
exchange surface, which is determined by the heat load of the exchanger and the
temperature difference between the hot and cold flows. To allow for variations in these
parameters, the process facility cost of the gas-liquid type heat exchanger was regressed
using the data in Table 4-4,
Q
PFC =1.0064⋅N ⋅[13.7528(dT )−0.6714( HE )0.6855] (R2=0.91) (4-18)
HE1 T,HE HE N
O,HE
130

where PFC = the process facility cost of the gas-liquid heat exchanger (US k$
HE1
in 2000)
N = the number of total train of the heat exchanger
T,HE
N = the number of the operating train of the heat exchanger
O,HE
Q = the heat load of the heat exchanger (kW)
HE
dT = the log mean temperature difference (C)
HE
Table 4 - 4 Gas-liquid heat exchanger cost data adjusted to the dollar value in 2000
[Doctor, 1996]
Log mean temperature
Cost (K$ in 000) Pressure (atm) difference (C ) Heat load (kW)
625.4 30.7 68.2 16421.6
615.0 30.7 90.8 21052.4
210.2 18.7 190.4 9298.0
168.2 19.4 148.6 5036.0
472.9 19.4 121.0 19534.9
315.3 19.4 13.7 1293.1
210.2 18.7 190.4 9298.0
99.8 19.4 153.5 2407.3
210.2 20.4 190.4 9298.0
634.6 68.1 52.0 12119.7
210.2 157.8 190.4 9298.0
Based on the data in Table 4-5, the process facility cost of the gas-gas type heat
exchanger is given by,
Q
PFC = 0.9927⋅N [24.4281⋅P0.2804(dT )−0.1143( HE2 )0.3881]
HE2 T,HE2 HE2 HE2 N
O,HE2
131

(R2=0.94 (4-19)
where PFC = process facility cost of gas-gas heat exchanger (US k$ in 2000)
HE2
N = the total train number of the heat exchanger
T,HE
N = the operating train number of the heat exchanger
O,HE
Q = the heat load of the heat exchanger (kW)
HE
dT = the log mean temperature difference in the heat exchanger
HE
Table 4 - 5 Gas-gas heat exchanger cost data adjusted to the dollar value in 2000
[Doctor, 1996]
Pressure Log mean
Cost (k$ in 2000) (atm) temperature (C ) Heat load (kW)
1757.3 30.7 98.0 17319.5
1757.3 30.7 90.7 16776.2
2205.4 19.4 10.0 42480.7
3131.2 30.7 318.4 100832.3
2606.0 31.6 340.4 95833.1
897.1 68.1 17.2 1223.6
2193.5 18.7 31.8 25641.0
1294.8 18.7 19.4 4034.0
644.3 20.4 69.1 2407.3
849.9 20.4 71.4 5036.0
692.1 20.4 57.5 2407.3
966.5 18.7 51.2 5036.0
132

4.6.2. Total capital requirement of WGS reaction system
The total process facilities cost of the water gas shift reaction system is the
summation of the individual process facility costs above plus the cost of initial catalyst
charge. This is added because it is also a large and integral part of the reaction system.
Following the EPRI Technical Assessment Guide (1993), the total capital requirement
and O&M cost of the WGS reaction system is given in the following table.
Table 4 - 6 Cost parameters of water gas shift process
Capital cost elements Value
Total process facilities cost Sum of the PFC of each equipment
Engineering and home office 10% PFC
General facilities 15% PFC
Project contingency 20% PFC
Process contingency 5% PFC
Total plant cost (TPC) = PFC+Engineering fee+General facilities+Project & Process
i
Allowance for funds during construction Calculated based on discount rate and
(AFDC) construction time
Royalty fees 0.5% PFC
Preproduction fees 1 month of VOM&FOM
Inventory cost 0.5% TPC
Total capital requirement (TCR) = TPC+AFDC+Royalty fees+Preproduction fee+Inventory cost
Fixed O&M cost (FOM)
Total maintenance cost 2% TPC
Maintenance cost allocated to labor 40% of total maintenance cost
Administration & support labor cost 30% of total labor cost
Operation labor 1 jobs/shift
Variable O&M cost (VOM)
High temperature catalyst $250/ft3, replaced every 2.5 years
Low temperature catalyst $250/ft3, replaced every 6 years
133

REFERENCES (CHAPTER 4)
1. Campbell J.S., 1970: Influences of catalyst formulation and poisoning on activity
and die-off of low temperature shift catalyst, Industrial & engineering chemistry
process design and development, 9(4): 588
2. Davis R.J., 2003: All That Glitters Is Not AuO, Science, Vol. 301, Issue 5635
3. Dmitrievich A., 2002: Hydrodynamics, mass and heat transfer in chemical
engineering. Taylor & Francis Press, New York
4. Doctor R.D., 1994: Gasification combined cycle: carbon dioxide recovery,
transport, and disposal, ANL/ESD-24, Argonne National Laboratory, Argonne, IL
5. Doctor R.D., 1996: KRW oxygen-blown gasification combined cycle carbon
dioxide recovery, transport, and disposal, ANL/ESD-34, Argonne National
Laboratory, Argonne, IL
6. Enick R.M. and Busfamante F., 2001: Very High-Temperature, High-Pressure
Homogenous Water Gas Shift Reaction Kinetics, 2001 AIChE Annual Meeting,
Reno
7. Frank P., 2003a: Low Temperature Shift Catalysts for Hydrogen Production,
Johnson Matthey Group
8. Frank P., 2003b: Sulfur Tolerant Shift Catalyst -Dealing with the Bottom of the
Barrel Problem, Johnson Matthey Group
9. Newsome D.S., Kellogg P., 1980: The Water-Gas Shift Reaction, CATAL. REV.-
SCI. ENG., 21(2)
10. Park J.N., Kim J.H., 2000: and Ho-In Lee, A Study on the Sulfur-Resistant
Catalysts for Water Gas Shift Reaction IV. Modification of CoMo/ g-Al2O3
Catalyst with K, Bull. Korean Chem. Soc. Vol. 21, No. 12
11. ASME steam table (saturation: pressure), http://www.e-
cats.com/databook/Page%2047.htm
12. Twigg M.V., 1989: Catalyst handbook, second edition, Wolfe publishing Ltd
134

Chapter 5. PERFORMANCE AND COST MODEL OF SELEXOL PROCESS
FOR CO CAPTURE
2
5.1. Introduction to the Selexol absorption process
The Selexol process uses a physical solvent to remove acid gas from the streams of
synthetic or natural gas. It is ideally suited for the selective removal of H S and other
2
sulfur compounds, or for the bulk removal of CO . The Selexol process also removes
2
COS, mercaptans, ammonia, HCN and metal carbonyls [Epps, 1994].
The Selexol process, patented by Allied Chemical Corp., has been used since the
late 1960s. The process was sold to Norton in 1982 and then bought by Union Carbide in
1990 [Epps, 1994]. The Dow Chemical Co. acquired gas processing expertise, including
the Selexol process, from Union Carbide in 2001. The process is offered for license by
several engineering companies—the most experienced of which with the process is
probably UOP [UOP, 2002].
The Selexol process has been used commercially for 30 years and has provided
reliable and stable operations. As of January 2000, over 55 Selexol units have been put
into commercial service [Kubek, 2000], which cover a wide variety of applications,
ranging from natural gas to synthetic gas. By now, Selexol process has been the dominant
acid-gas removal system in gasification project. Moreover, increasingly interests to
control CO emission in the world may lead to Selexol application widely, particularly for
2
coal gasification plants. Actually, the use of the Selexol solvent has a long history in
gasification process, and was chosen as the acid-gas removal technology for the
pioneering work in this area. Due to its outstanding record, the Selexol process continues
to be the preferred choice for acid-gas removal today, and has recently been selected for
135

several large projects around the world [Breckenridge, 2000]. Relevant experiences for
gasification are as follows [Kubek, 2000].
• About 50 Selexol units have been successfully commissioned for steam
reforming, partial oxidation, natural gas, and landfill gas. Of these, 10 have been
for heavy oil or coal gasifiers.
• The 100 MW Texaco/Cool Water (California) 1,000 t/d coal gasifier plant for
IGCC demonstration was operated continuously for about five years in the 1980s.
The Selexol unit performed extremely well. The process delivered H S-enriched
2
acid gas to a Claus plant while removing 20 to 25% of the CO and treating a high
2
CO /H S ratio feed gas.
2 2
• The TVA/Muscle Shoals (Alabama) 200 t/d coal gasifier demonstration plant was
operated continuously for about five years in the early 1980s. It employed a
Texaco gasifier, a COS hydrolysis unit, and a Selexol unit to convert coal to clean
synthesis gas, and CO as an alternative feed to an existing ammonia-urea plant.
2
The COS hydrolysis and Selexol units were stable and had a high on-stream
factor. The Selexol unit delivered an H S-enriched acid gas to elemental sulfur
2
production, a pure (< 1 vppm total sulfur) synthesis gas to NH synthesis, and
3
removed part of the CO to provide high-purity CO for urea production.
2 2
In this section, the technical background information of Selexol process is
reviewed. This information is used to provide a basis for the development of performance
models of Selexol systems for CO emission control of IGCC plants.
2
136

5.2. Selexol solvent property
The Selexol acid gas removal process is based on the mechanism of physical
absorption. The solvent used in the Selexol acid removal system is a mixture of dimethyl
ethers polyethylene glycol with the formulation of CH (CH CH 0) CH , where n is
3 2 2 n 3
between 3 and 9 [Epps, 1994]. The general properties of the glycol solvent is given in
Table 5-1 [Sciamanna, 1988; Newman, 1985].
Table 5 - 1 Property of glycol solvent
Property Value
Viscosity @25C,cp 5.8
Specific gravity@25C,kg/m^3 1030
Mole weight 280
Vapor pressure @25C, mmHg 0.00073
Freezing point C -28
Maximum operating Temp., C 175
Specific heat@25C Btu/lb F 0.49
The performance of a physical solvent can be predicted by its solubility. The
solubility of an individual gas follows the Henry’s law—the solubility of a compound in
the solvent is directly proportional to its partial pressure in the gas phase. Hence, the
performance of the Selexol processes enhances with increasing the partial pressures of
sour gases. This is one of the major advantages of physical solvents, such as Selexol, over
chemical solvents, such as methyldiethanolamine (MDEA), for acid gases removal from
the high pressure syngas. As shown in Figure 5-1, compared to physical solvents,
chemical solvents, such as methyldiethanolamine (MDEA) and diethanolamine (DEA),
have higher absorption capacity at relatively low acid gas partial pressures. However,
their absorption capacities plateau at higher partial pressures. The solubility of an acid
137

gas in physical solvents increases linearly with its partial pressure. Therefore, chemical
solvent technologies are favorable at low acid gas partial pressures and physical solvents
are favored at high acid gas partial pressures. Furthermore, the physical absorption allows
for the solvent to be partially regenerated by pressure reduction, which reduces the
energy requirement compared to chemical solvents.
Figure 5 - 1 Characteristics for Chemical and Physical Solvents [Sciamanna, 1988]
Higher partial pressure leads to higher solubility in physical solvents of all
components of a gas stream, but the attractiveness of the Selexol system is that it has a
favorable solubility for the acid gases versus other light gases. Comparing with some acid
gases, H and CO have much lower solubility in the solvent. For instance, as shown in
2
Table 5-2, CO is 75 times more soluble than H , and H S is 670 times more soluble than
2 2 2
H in Selexol.
2
138

Table 5 - 2 Relative solubility of gases in Selexol solvent [Doctor, 1994]
Gas CO H CH CO H S COS SO NH N H O
2 2 4 2 2 3 2 2
Solubility 1 0.01 0.0667 0.028 8.93 2.33 93.3 4.87 0 733
Table 5-3 shows the actual solubility of various gases at 25°C in the Selexol solvent.
The solubility data in Table 5-3 are based on single component solubility. It would be
expected that these values should be approximately the same for non-polar components
even in acid gas loaded solvents [Korens, 2003].
Table 5 - 3 Solubility of Gases in the Selexol Solvent [Korens, 2002]
Gas CO H CH CO H S COS HCN C H CH SH H O
2 2 4 2 6 6 3 2
Solubility,
Ncm2/g.bar 3.1 0.03 0.2 0.08 21 7.0 6600 759 68 2200
@25°C
The solvent may be regenerated by releasing the absorbed sour gases. The
regeneration step for Selexol can be carried out by either thermally, or flashing, or
stripping gas. In addition to its solubility, the Selexol solvent has some other positive
advantages to gasification applications [Kubek, 2000].
• A very low vapor pressure that limits its losses to the treated gas
• Low viscosity to avoid large pressure drop
• High chemical and thermal stability (no reclaiming or purge) because the solvent
is true physical solvent and do not react chemically with the absorbed gases
[Shah, 1988]
• Nontoxic for environmental compatibility and worker safety
139

• Non-corrosive for mainly carbon steel construction: the Selexol process allows for
construction of mostly carbon steel due to its non-aqueous nature and inert
chemical characteristics
• Non-foaming for operational stability
• Compatibility with gasifier feed gas contaminants
• High solubility for HCN and NH3 allows removal without solvent degradation.
• High solubility for nickel and iron carbonyls allows for their removal from the
synthesis gas. This could be important to protect blades in downstream turbine
operation.
• Low heat requirements for regeneration because the solvent can be regenerated by
a simple pressure letdown
5.3. Technical Overview Selexol process for acid gas removal
This section presents a technical overview of Selexol absorption processes for sour
gases removal, with particular focus on the effects of the sour remove requirements on
the design of Selexol process.
Although a Selexol process can be configured in various ways, depending on the
requirements for the level of H S/CO selectivity, the depth of sulfur removal, the need
2 2
for bulk CO removal, and whether the gas needs to be dehydrated, this process always
2
includes the following steps—sour gas absorption, solvent regeneration/sour gas
recovery, and solvent cooling and recycle. These general steps for the Selexol process for
acid gas removal are described by the following cases.
140

5.3.1. Selexol process for selective HS removal
2
Figure 5 - 2 Selexol Flow Diagram for Selective H S Removal [Kubek, 2000]
2
A typical Selexol flow diagram for selective H S removal is shown in Figure 5-2.
2
The feed gas and the lean solvent counter currently contact at high pressure and lower
temperatures in an absorber, where desired levels of H S, COS and CO are absorbed into
2 2
the solution. Regeneration of the acid gas rich solvent is fulfilled through a combination
of flashing and thermal regeneration. Acid gases absorbed in the solvent released first
from one or more flash tanks at reduced pressures, then from the stripper by thermal
regeneration with steam stripping at elevated temperatures and low pressure. A solvent
heat exchange is employed to cool down the solvent. The regenerator overhead vapors
(acid gas and steam) are routed to a condenser plus knockout drum, and the condensed
water is returned to the unit to maintain water balance. The high- pressure flash gas
vapors are compressed and returned to the absorber for greater H and CO recovery and
2
to provide H S-enrichment of the acid gas for the Claus plant.
2
141

5.3.2. Selexol process for HS and CO removal
2 2
Through taking advantage of the high H S to CO selectivity of Selexol solvent,
2 2
Selexol solvent processes can also be configured to capture H S and CO together with
2 2
high levels of CO recovery. This is usually accomplished by staging absorption for a
2
high level of H S removal, followed by CO removal. Figure 5-3 shows a Selexol process
2 2
layout for synthesis gas treating where a high level of both sulfur and CO removal are
2
required. H S is selectively removed in the first column by a lean solvent, and CO is
2 2
removed from the H S-free gas in the second absorber. The second-stage solvent can be
2
regenerated with air or nitrogen if very deep CO removal is required.
2
Figure 5 - 3 Selexol Process for Sulfur and CO Removal [Kohl, 1985]
2
A COS hydrolysis unit may be required if a high level of H S and COS removal is
2
required. At the Sarlux IGCC plant in Italy, which gasifies petroleum pitch, the Selexol
unit allows a COS hydrolysis step and gives an acid gas that is 50-80 vol.% H S to the
2
Claus plant. This acid gas composition is the result of an H S enrichment factor of about
2
142

2 to 3 through the Selexol unit. The H S content of the purified gas from the Selexol
2
absorber at that plant is about 30 ppmv [Korens, 2002].
5.3.3. An optimal design for Selexol process for sulfur and CO capture
2
from IGCC systems
A variety of flow schemes of Selexol processes permits process optimization and
energy reduction. The following is a description of an optimal design of a Selexol process
which removal sulfur and CO from syngas from IGCC systems. This optimal design is
2
based on revising a Selexol process, originally designed by UOP, for H S and CO
2 2
removal from syngas for the production of ammonia (UOP, 2002).
The H S Absorption flowsheet for the optimized configuration is shown in Figure
2
5-4. Syngas from the gas cooling section of the gasification process enters the H S
2
absorber where it is contacted with CO -saturated Selexol solvent from the CO -removal
2 2
portion of the facility. The pre-saturated solvent from the CO removal area is chilled
2
with refrigeration before fed into the absorber, which can increase the CO and H S
2 2
loading capacity of the solvent. The use of pre-loaded solvent prevents additional CO
2
absorption in the H S absorber, and it also minimizes the temperature rise across the
2
tower, which negatively affects the H S solubility and the selectivity of the solvent. H S
2 2
is removed from the syngas. The H S absorber overhead stream is mixed with the entire
2
solvent stream from the CO absorber. Therefore, significantly bulk CO is removed in
2 2
this pre-contacting stage which reduces the loading in the CO Absorber. The rich solvent
2
from the H S absorber is fed to the H S solvent regeneration facility.
2 2
143

Figure 5 - 4 Optimized Selexol absorption process for H S removal
2
Figure 5-5 presents a process flow diagram for the optimized H S solvent
2
regeneration section. The rich solvent from the H S absorber is pumped to high pressure
2
and heated in the lean / rich exchanger. The solvent then enters the H S solvent
2
concentrator, which operates at a pressure higher than the H S absorber, thus the recycle
2
gases can be recycled to the H S absorber without compression. Due to the relative
2
difference in solubility in Selexol solvents, CO is removed from solution preferentially
2
over H S, which results in an enriched H S concentration in the solvent. The CO
2 2 2
removed in the H S solvent concentrator is the majority of the recycle gases back to the
2
H S absorber. The enriched solvent from the H S solvent concentrator is flashed down to
2 2
lower pressure. The flash gas again contains a higher proportion of CO than H S. This
2 2
stream is also recycled back to the H S absorber. This recycle stream is relatively small
2
because much of the CO was removed at high pressure. The solvent from the flash drum
2
enters the Selexol stripper for regeneration.
144

Figure 5 - 5 Optimized H S Solvent Regeneration
2
The optimized CO absorption flowsheet is shown in Figure 5-6. In this
2
optimization design, the entire CO solvent flow is contacted with the H S absorber
2 2
overhead stream in the pre-contacting stage, which can unloads the CO absorber. The
2
heat of absorption is removed from this pre-contacting stage in a refrigeration chiller. The
relatively high temperature of this stream allows setting high temperature refrigeration,
which reduces the power consumption of the refrigeration system. The solvent is cooled
to optimum absorption temperatures when the pressure is reduced in the flash
regeneration portion of the facility. A portion of the rich CO solvent is returned to the
2
H S absorber as pre-saturated solvent. The remainder of the solvent is flash regenerated
2
which will be presented below. The top bed of the tower uses lean solvent from the H S
2
regeneration facility to contact the syngas. This allows for the CO to be removed to
2
levels lower than could be achieved using only flash regenerated (semi-lean) solvent.
145

Figure 5 - 6 Optimized Selexol process for CO absorption
2
Rich CO is flash regenerated as shown in Figure 5-7. The flash regeneration uses
2
one sump tank, one or two power recovery turbines, and three stages of flash. The CO
2
rich solvent leaving the bottom of the CO absorber is let down to the sump tank at a
2
reduced pressure, where most H and a tiny amount of CO captured in the Selexol are
2 2
released and recycled back to the pre-contacting stage.
Then the CO rich solvent with high pressure is let down to one or two hydraulic
2
power recovery turbines to recover the pressure energy before it is fed into three flash
drums, where CO is released at staged pressures to reduce the power consumption of
2
CO compression later.
2
146

Figure 5 - 7 Optimized Selexol regeneration through CO flash
2
A key limitation of Selexol systems is the operating temperature requirement. The
operating temperature for Selexol systems is typically approximately 100°F. Hence a
reasonable location of Selexol process in an IGCC system is at the down stream of
syngas cooling section.
5.4. Performance model of Selexol process
As a patented commercial solvent, the detailed characteristics of the Selexol solvent
are not available. Hence in this section, a semi-analytical, semi-regression performance
model of Selexol systems for CO capture is presented.
2
147

5.4.1. Performance model of Selexol process for CO capture
2
This section discusses the methodology of setting up a performance model of
Selexol process for CO capture. A cost model of the Selexol process is further developed
2
on the basis of this performance model.
Temperature effect on solubility of gases in Selexol
The solubility of a gas in Selexol depends on its partial pressure and temperature.
The solubility of CO as a function of temperature is regressed based on published data
2
[Doctor 1996, Black 2000] and given by,
χ =0.0908−0.0008⋅T
CO 2 (R2=0.95) (5-1)
where χ CO = the solubility of CO 2 in the Selexol (SCF/gallon-psia)
2
T = the temperature of solvent with a range of 30~77 °F
The solubility of other gases at different temperature is not available. Here the
relative solubility of other gases to CO at different temperature is assumed to be
2
constant.
Solvent flow rate of the Selexol process
The input and output parameters of this model are given in Table 5-4. For the
performance simulation, the first step is to calculate the flow rate of the solvent. In order
to do this calculation, the whole Selexol process can be simplified as Figure 5-8. Stream
1 is the syngas fed into the absorber at a given temperature, and α percent of CO is
2
removed from the syngas. Stream 4 is the lean solvent at a design temperature. Due to
148

heat transfer between the solvent and syngas and the absorption heat, the temperature of
the rich solvent (stream 3) will be increased by ∆T . For the given CO removal
2
percentageα, the flow rate of solvent, fuel gas and CO can be calculated as follows.
2
Table 5 - 4 Input and output parameters of Selexol model
Input parameter Output parameter
Flow rate Flow rate
(mole/s) f (mole/s) f
1 2
Pressure p Pressure p
1 2
Temperature T Temperature T
1 2
[CO] [CO]
1 2
[CO ] [CO ]
Syngas 2 1 Fuel gas 2 2
input [H ] output [H ]
2 1 2 2
Molar [CH 4 ] 1 Molar [CH 4 ] 2
concentrations concentrations
[H S] [H S]
2 1 2 2
[COS] [COS]
1 2
[NH ] [NH ]
3 1 3 2
[H O] [H O]
2 1 2 2
Flow rate
(mole/s) f
CO flow 5
2
CO 2 removal percentage Pressure P 5
Refrig. Comp.
power Power recovery power
149

Figure 5 - 8 Simplified Selexol process
As mentioned in the above section, the solubility of gases in Selexol is a function of
temperature. For calculating the flow rate of solvent, the first step is to estimate the
temperature change of solvent in the absorber. Assuming the flow rate of solvent is ωlb-
mol/hr, the temperature increase of solvent in the absorber is given by
∆T = ∆T +∆T (5-2)
1 2
where ∆T = the temperature increase of solvent in the absorber (°F)
∆T = solvent temperature increase caused by the heat transfer (°F)
1
∆T = solvent temperature increase due to the solution heat of gases (°F)
2
According to the amount of heat transferred between the syngas and solvent, and
the specific heat of the solvent, the temperature increase due to heat transfer is calculated
by
150

Q
∆T = 1 (5-3)
1 ω⋅MW ⋅C
Sel p,s
where MW = the molar weight of Selexol (280 lb/lb-mol)
Sel
C = the specific heat of Selexol (0.49 Btu/lb °F)
p,s
Q = the heat released by the syngas, which can be estimated according to the
1
energy balance and given by,
Q = (T −T )f {2.02⋅[H ] ⋅C +16⋅[CH ] ⋅C
1 SG,i SG,o SG,i 2 1 p,H 4 1 p,CH
2 4
+28⋅[CO] ⋅C +44⋅[CO ] ⋅(1−α)⋅C } (5-4)
1 p,CO 2 1 p,CO
2
+44⋅(T −T −∆T)⋅f ⋅α⋅[CO ] ⋅C
SG,i SG,o SG,i 2 1 p,CO
2
where T = the syngas temperature at the inlet of the absorber (°F)
SG,i
T = the syngas temperature at the outlet of the absorber (°F)
SG,o
f = the molar flow rate of syngas at the inlet of the absorber (lb-mole/hr)
SG,i
[i] = the molar concentration of species i in syngas at the inlet of the absorber
1
C = the specific heat of species i (Btu/lb °F), which is given in Table 5-5.
p,i
Table 5 - 5 Specific heat of gases in the syngas
Gas CO CO H CH Ar N H S NH
2 2 4 2 2 3
Specific heat 0.248 0.199 3.425 0.593 0.125 0.249 0.245 0.52
(Btu/lb F)
151

In Eq. 5-2, ∆T
2
is caused by the solution heat. Here only the solution heat of CO
2
is
calculated. The solution heat of other gases is negligible because the amount of other
gases captured by Selexol is much less than that of CO .
2
44f ⋅[CO ] ⋅α⋅ψ
∆T = SG,i 2 1 CO 2 (5-5)
2 ω⋅MW ⋅C
Sel p,Sel
where f = total flow rate of syngas entering the absorber (lb-mole/hr)
SG,i
α= CO
2
removed from the syngas (%)
ω= Selexol flow rate (lb-mole/hr)
MW = Selexol molecular weight (lb/lb-mole)
S
[CO ] = CO molar concentration at the inlet of absorber
2 1 2
ψ CO = solution heat of CO 2 in Selexol (Btu/lb-solute), and the solution heat of
2
several gases is given in Table 5-6 [Korens, 2002].
Table 5 - 6 Solution heat (Btu/lb-solute) of gases in the Selexol
Gas CO H S CH
2 2 3
Heat of solution (Btu/lb-solute) 160 190 75
In the flash tanks, the residual time is long enough to assume that equilibrium can
be achieved in these tanks. In the last flash tank, the solvent temperature is about
(30+∆T
1
), hence the volume and mass flow rate of the residual CO
2
in the lean solvent
(S4 stream in Figure 5-8) can be given by:
152

V (SCF/hr) =SV ⋅ω⋅p χ (5-6)
CO ,res sel CO CO
2 2 2
V
m (lb⋅mol/hr) = CO 2 ,res (5-7)
CO 2 ,res SV
CO
2
where SV = the specific volume of Selexol (32.574 gallon/lb-mol);
sel
SV = the specific volume of CO (377.052 SFC/lb-mol);
CO 2
2
ω = the flow rate of Selexol (lb-mol/hr);
p = the partial pressure of CO psia);
CO 2 (
2
χ CO 4 = the solubility of CO 2 in Selexol at temperature of 30+∆T 1 .
2,
According to the CO capture percentage in the absorber, the amount of CO that
2 2
need be captured by the solvent is,
V (SCF /hr) = SV ⋅ f ⋅[CO ] ⋅α (5-8)
CO ,abs CO SG,i 2 1
2 2
In the absorber, the equilibrium cannot be achieved due to the limited residual time.
The flow rate of solvent used in the absorber is larger than that of the solvent required to
capture α percentage of CO 2 at equilibrium. The ratio of the actual flow rate to the
equilibrium flow rate of the solvent was regressed based on published data [Doctor, 1994,
1996, Sciamanna, 1988].
1.26
γ= −0.0002p (R2 =0.8) (5-9)
(1−α)0.07 1
153

p
where 1= the pressure of syngas at the inlet of absorber (psia).
Then the flow rate of Selexol for capturing α percentage of CO 2 is given by
γ(V +V )
ω(lb⋅mol/hr) = CO 2 ,res CO 2 ,abs (5-10)
SV ⋅ p ⋅[CO ] ⋅χ
sel 1 2 1 CO ,1
2
V
where CO ,res= volume flow rate of residual CO in the lean solvent (lb-mole/hr)
2 2
V
CO ,abs = volume flow rate of CO captured in the absorber (lb-mole/hr)
2 2
χ CO 1 = the solubility of CO 2 in Selexol at temperature of 30+∆T (°F)
2,
Based on the above discussion, the calculation process for the flow rate of Selexol
is concluded as in the following. First assuming the temperature of the Selexol solvent in
the absorber is increased by (∆T
1
+∆T
2
), then the solubility of CO
2
at this increased
temperature can be calculated. Second the solubility of CO at the solvent in the last flash
2
tank is calculated at the temperature (30+∆T
1
). Given the amount of CO
2
needed to be
required, the flow rate of the solvent is calculated based on the solubility difference
between the solvent in the absorber and in the last stage flash tank. Then the new values
of ∆T and ∆T are computed using the calculated solvent flow rate of solvent. Such
1 2
calculation process continues until the flow rate of the solvent is convergent. This
calculation process is represented by Figure 5-9:
154

Figure 5 - 9 Calculation process for the flow rate of Selexol
Composition and flow rate of fuel gas
After CO capture, the syngas is converted into the fuel gas, the main component of
2
which is hydrogen. The composition and flow rate of the fuel gas can be calculated as
follows.
With knowing the Selexol flow rate and solubility of gases, the volume and mass
amount of species i which is captured by the solvent is:
V (SCF/hr)=SV ⋅ω⋅p ⋅χ (5-11)
i sel i i
V
m (lb⋅mol/hr) = i (5-12)
i v
i
where V = the volume flow rate of species i captured in the Selexol (SVF/hr);
i
SV = the specific volume of Selexol (gallon/lb-mol);
sel
v = the specific volume of CO (SFC/lb-mol)
i 2
ω = the flow rate of Selexol (lb-mol/hr);
p = the partial pressure of species i in the syngas (psia);
i
χ= the solubility of species i in Selexol at temperature of 30+∆T °F;
i
155

In the sump tank, most of the H , CH captured in the Selexol are released and
2 4
recycled to the absorber again. Because of the much higher solubility, only a tiny amount
of CO is released in the sump tank. The operating pressure of the sump tank is a design
2
parameter. For this study, the operating pressure is determined to keep the loss of H to
2
Selexol solvent no more than 1% of H in the syngas. The calculation process for the
2
sump tank is as the follows: assuming the operating pressure isp , the volume of
sump
species i released from the sump tank is V', then the partial pressure p can be given
i i,sump
by Eq. (5-13). According to mass conservation, the total volume of species i captured in
the absorber equals the volume released in the sump tank plus the volume retained in the
solvent in the tank, expressed as Eq. (5-14). Now recalling the Eq. (5-11), the volume of
species is retained in the solvent in the tank can calculated as Eq. (5-15). Iteratively
calculating Eq (5-13), (5-14), and (5-15) until the partial pressures are converged. If at
the given operating pressure, the H volume retained in the solvent does not meet the
2
design value, then the operating pressure is adjusted and the calculation is run again. The
calculation procedure is given by Figure 3-10.
V'
p = i p (5-13)
i,sump ∑V' sump
i
i
V =V +V' (5-14)
i i,sump i
V (SCF/hr)=32.574ω⋅p ⋅χ (5-15)
i,sump i,sump i
156

Figure 5 - 10 Calculation process for the operating pressure of the sump tank
Composition and flow rate of CO rich flow
2
At each stage of the flash tanks, the flash pressure is given. At this pressure, the
residual gases in the lean solvent can be calculated based on their solubility. Based on
mass conservation, the composition and flow rate of CO rich flow from the flash tanks
2
can also be calculated, and the calculation procedure is similar to that shown in Figure 5-
10.
5.4.2. Power consumption model of Selexol process
There is no heat duty in the Selexol process because the solvent is regenerated
through pressure flashing, but the power input is required to compress the recycling gas
from the sump tank, the lean solvent from the flash tank 3, and the CO rich product. At
2
the same time, some electricity can be generated through the power recovery hydro
turbine. The total power consumption is the difference between the power input and the
recovered power from the turbine.
Power recovery
In this performance model, the pressure of the high-pressure rich solvent from the
absorber is reduced and the energy is recovered through one or two hydro turbines.
157

According to the designs in other studies [Doctor, 1994, 1996, Sciamanna, 1988, Black,
2000], a thumb rule of design is concluded here. If the pressure of CO rich Selexol flow
2
is larger than 240psia, two power recovery turbines will be used. Otherwise, only one
power recovery turbine will be used. Generally, this outlet pressure (P , psia) of the
o,1
turbine can be determined based on the system pressure as following:
P = 0.0402P1.415 (5-16)
o,1 i,1
where P = the outlet pressure of power recovery turbine 1 (psia).
o,1
P = the pressure of the CO -rich Selexol at the inlet of turbine 1 (psia),
i,1 2
(150≤ p ≤1000).
i,1
If the pressure of the CO rich Selexol flow is larger than 240 psia, then the outlet
2
pressure of the second turbine is given by,
p =35.619ln(p )−169.88 (240≤ p ≤1000) (5-17)
o,2 i,1 1
where P = the outlet pressure of power recovery turbine 2 (psia)
o,2
P = the pressure of the CO -rich Selexol at the inlet of turbine 1 (psia),
i,1 2
(240≤ p ≤1000)
i,1
The power recovered from the liquid solvent is calculated from the following
expression [Doctor, 1994],
158

f
hp = H ⋅ Sel 2 ⋅η (5-18)
tur Sel 1714 tur
where hp = the power recovered through the power turbine (hp)
tur
H = the total dynamic head (lb/in2)
Sel
f = the flow rate of CO rich Selexol entering the turbine (gal/min)
Sel 2
2
η = the efficiency of the turbine
tur
The temperature change of the solvent in the turbine can be calculated based on the
change in enthalpy, which equals flow work, vdp. For the default efficiency of turbines,
∫
78%, the temperature can be given by,
dT =0.0047⋅dP −0.0715 (5-19)
tur tur
where dT = the decreased temperature of the Selexol in the power recovery
tur
turbine (°F);
dP = the decreased pressure of the Selexol in the power recovery turbine (°F)
tur
CO compression
2
There are three flashing pressure levels for CO release. The design of the flashing
2
pressures in the three flashing tanks is an optimal problem, but a preliminary study
showed that the effect of flashing pressures on the power consumption of the Selexol
processes is not considerable. Hence, some default values are adopted here for the
159

process design. If the system pressure is larger than 240 psia, the first flashing pressure
equals the outlet pressure of the second turbine. If the system pressure is less than 240
psia, the first flashing pressure is set to be 25 psia. The second flashing pressure is set to
be 14.7 psia, and the last flashing pressure is set to be 4 psia.
In each flashing tank, the gases released from solvent are calculated. CO released
2
from flash tank 2 and tank 3 is compressed to the flashing pressure of tank 1. The CO
2
stream is finally compressed to a high pressure (>1000psia) for storage using a multi-
stage, inter-stage cooling compressor. The power required by the CO compressors is
2
estimated by [Doctor, 1994],
0.00436 k P
hp = ⋅VF ⋅P ⋅( )⋅[( comp.,o) (k gas−1) k gas −1] (5-20)
comp. η gas comp,i k−1 P
comp. comp.,,i
where hp = the power consumption of the CO compressor (hp)
comp. 2
η = the overall efficiency of the compressor
comp.
VF = the inlet rate of the CO stream (ft3/min)
gas 2
P = the inlet pressure of the compressor (psia)
comp.,i
P = the outlet pressure of the compressor (psia)
comp.,o
C
k = p,gas .
gas C
v,gas
160

Solvent compression work
The CO -lean solvent is pumped back to the absorber operating pressure by a
2
circulation pump. The power required by the circulation pump is estimated in a similar
way as Eq. (5-18),
f
hp = H Sel (5-21)
pump s 1714η
pump
where H = the total dynamic head (psia)
s
f = the flow rate of CO lean Selexol (gal/min)
Sel 2
η = the efficiency of the pump
pump
Recycle gas compression work
The gases from the sump tank are recycled to the absorber. A compressor is used to
compress the gases to the operating pressure of the absorber. The power of the
compressor is estimated using Eq. (5-20).
Solvent refrigeration
Before the CO -lean solvent fed into the absorber, it has to be cooled down to the
2
absorber operating temperature (30F) by refrigeration. The refrigeration power is
estimated by [Doctor, 1994],
refrigeration load(Btu/hr)
W = (5-22)
ref. T
1000(9+ evap )
10
161

where W = the power consumption of the solvent refrigeration process (kW)
ref.
T = the evaporation temperature of the refrigerant (°F)
evap
Makeup of the Selexol solvent
The vapor pressure of the Selexol solvent is1.35×10−5 psia at 77F, which is very
low. The real vapor pressure is even lower because the operating temperature is usually
lower than 77F. Hence, the loss of solvent due to evaporation is negligible. On the other
hand, due to leakage, especially in the start on and turn off processes, a certain amount of
solvent is lost. Here the annual loss of solvent is assumed to be approximate 10% of the
total solvent in the system [UOP, 2003].
5.5. Cost model of the Selexol process
Similar to the cost model of the WGS reaction system discussed in Chapter 4, the
outputs of this cost model include the process facility cost, total plant cost, total plant
investment, total capital requirement, and O&M cost.
5.5.1. Process facility costs of the Selexol system for CO capture
2
The major process facility costs of the Selexol system for CO capture are
2
considered as in the following.
CO absorption column
2
Using the data in Table 5-7, the process facility costs of the absorption column is
regressed as a function of the operating pressure, the flow rates of the solvent and syngas,
PFC = N ⋅[−1375 .356 +16.536 P
abso . T,abso . abso ,i
+ 0.127628 (0.5 f Sel + 0.5 f SG )] (R2=0.90) (5-23)
162

where PFC = the process facility cost of the absorber(US k$ in 2000)
avso
N = the total train number of absorbers
T,abso
P = the inlet pressure of absorber (atm)
abso.,i
f = the flow rate of the Selexol(lb-mole/hr)
Sel
f = the flow rate of the syngas (lb-mole/hr)
gas
Table 5 - 7 Absorber cost data adjusted to the dollar values in 2000 [Doctor, 1996]
PFC (2000$) P(atm) Flow rate of syngas(lb- Selexol flow rate(lb-
mol/h) mol/hr)
6.3E+05 30.35 11771.88 11815.53
9.2E+05 10.21 12418.46 20802.84
1.5E+06 16.88 17614.58 23000
1.3E+06 68.05 17614.58 6900
Power recovery turbine
Based on the data in Table 5-8, the process facility cost of the power recovery
turbine is given by,
PFC = 219.086+0.080912⋅hp +0.020086P2 (R2=0.91) (5-24)
tur tur tur,o
where PFC = the process facility cost of power recovery turbine (US k$ in 2000)
tur
hp = power output of the turbine (hp)
tur
P = the outlet pressure of the turbine (atm)
tur,o
163

Table 5 - 8 Power recovery turbine cost data adjusted to the dollar value in 2000
[Doctor, 1996]
PFC (2000 k$) Outlet pressure Power output(hp)
277.23 13.60 649
235.64 3.40 404
246.66 5.10 293
263.21 3.40 451
246.66 1.70 293
317.14 51.03 567
317.14 6.80 567
Sump tank
The process facility cost of the sump tank is regressed as a function of the solvent
flow rate,
f
PFC = 2.0049⋅N ⋅( Sel )0.7446 (R2=0.87) (5-25)
slump T,slump N
O,slump
wherePFC = the process facility cost of the sump tank (US k$ in 2000)
sump
N = the total train number of sump tanks
T,sump
N = the operating train number of the sump tanks
O,sump
f = the flow rate of the CO -rich Selexol entering the sump tank (kg/s),
Sel 2
400~800/train
164

Table 5 - 9 Sump tank cost data adjusted to the dollar value in 2000 [Doctor, 1996]
PFC (2000 k$) Selexol flow rate (kg/s)
179.04 416.85
272.83 733.92
205.11 811.44
205.22 811.44
Recycle compressor
The process facility cost of the recycle compressor is given by,
PFC = 4.45519hp 0.7784 (R2=0.98) (5-26)
RC RC
where PFC = the process facility cost of the recycle compressor (US k$ in 2000)
RC
hp = the power consumption of the recycle compressor (hp)
RC
Table 5 - 10 Recycle compressor cost data adjusted to the dollar value in 2000
[Doctor, 1996]
PFC (2000 k$) Compressor capacity (hp)
576.64 537
361.19 259
212.55 151
212.55 151.3
Selexol pump
The process facility cost of the Selexol pump is given by,
PFC =1.2286hp 0.7164 (R2=0.92) (5-27)
SP SP
where PFC = the process facility cost of the Selexol pump (US k$ in 2000);
SP
hp = the power consumption of the Selexol pump (hp).
SP
165

Table 5 - 11 Selexol pump cost data adjusted to the dollar value in 2000 [Doctor,
1996]
PFC (2000 US k$) Pump capacity (hp)
301.52 2205
207.29 1282
326.63 2388
326633.3 2388
CO compressor
2
The process facility cost of the CO compressor is regressed as,
2
PFC = 7.0321hp 0.6769
comp1 comp (R2=0.83) (5-28)
where PFC = the process facility cost of the CO compressor (US k$ in 2000)
comp1 2
hp = the power consumption of the compressor (hp)
comp
Table 5 - 12 CO compressor cost data adjusted to the dollar value in 2000 [Doctor,
2
1996]
PFC (2000, US k$) Compressor capacity (hp)
323.1754 600.41
311.5061 255
216.2418 155.52
190.1031 120.54
1026.139 1086
576.6455 539.71
CO final product compressor
2
The process facility cost of the multi-stage CO compressor is given by,
2
PFC =13.0969hp 0.64 (R2=0.85) (5-29)
comp2 comp
166

where PFC = the process facility cost of the compressor (US k$ in 2000)
comp2
hp = the horse power consumption of the compressor (hp)
comp
Table 5 - 13 CO final compressor cost data adjusted to the dollar value in 2000
2
[Doctor, 1996]
PFC (2000 US K$) Compressor capacity (hp)
2162.421 2582
2851.544 2913
2565.347 3369
2382.109 3217
Refrigeration
The process facility cost of the refrigeration unit is regressed as,
f
PFC =1.0019⋅N ⋅[16.4796⋅( Sel )0.3618(∆T )0.4064] (R2=0.97) (3-30)
refr T,refr N Sel
O,refr
where PFC = the process facility cost of the refrigeration unit (US k$ in 2000);
refr
N = the total train number of the refrigeration unit;
T,reft
N = the operating train number of the refrigeration unit;
O,reft
f = the flow rate of the solvent entering the refrigeration unit (lb-mol/h),
Sel
70000~23000 /train;
∆T = the Selexol temperature difference between the inlet and outlet of the
Sel
refrigeration unit (°C ), 1~5 °C.
167

Table 5 - 14 Refrigeration unit cost data adjusted to the dollar value in 2000 [Doctor,
1996]
PFC (2000 k$) Solvent flow rate (lb-mol/h) Temperature
difference (C)
657.73 12000 2.171
613.81 20802 1.017
771.71 7016 4.706
771.71 23397 1.667
168

Flash tank
The process facility cost of flash tanks is given by,
f
PFC =0.9832⋅N ( Sel )0.8005 (R2=0.89) (5-31)
tank T,tank N
O,tank
wherePFC = the process facility cost of the flash tank (US k$ in 2000);
tank
N = the total train number of the flash tank;
T,tank
N = the operating train number of the flash tank;
O,tank
f = the flow rate of the Selexol entering the flash tank (kg/s), 400~800 /train.
Sel
Table 5 - 15 Flash tank cost data adjusted to the dollar value in 2000 [Doctor, 1996]
PFC (2000 $) Solvent flow rate (kg/s)
129745.5 416.85
197707.4 733.92
205227.8 811.44
5.5.2. Total Capital Requirement of the Selexol process
169

Here the default values for the capital cost calculation of the Selexol process for
CO capture are given by the following Table 5-16.
2
Table 5 - 16 Parameters for TCR of Selexol process
Total process facilities cost (PFC) Sum of PFC of the major units in the process
Engineering and home office 10% PFC
General facilities 15% PFC
Project contingency 15% PFC
Process contingency 10% PFC
Total plant cost (TPC) = sum of the above values
Interest during construction Calculated
Royalty fees 0.5% PFC
Preproduction fees 1 moth fee of VOM&FOM
Inventory cost 0.5% TPC
Total capital requirement (TCR) = sum of above values
Fixed O&M cost (FOM)
Total maintenance cost 2% TPC
Maintenance cost allocated to labor 40% of total maintenance cost
Administration & support labor cost 30% of total labor cost
Operation labor 2 jobs/shift
Variable O&M cost (VOM)
Selexol solvent $ 1.96/lb
170

REFERENCES (CHAPTER 5)
1. Black W.B., Pritchard V., Holiday A., Ong J.O. and Sharp C., 2000: Use of
SELEXOL Process in Coke Gasification to Ammonia Project By Presented at the
Laurance Reid Gas Conditioning Conference, The University of Oklahoma, Norman,
Oklahoma
2. Doctor R.D., 1994: Gasification combined cycle: carbon dioxide recovery, transport,
and disposal, ANL/ESD-24
3. Doctor R.D., 1996: KRW oxygen-blown gasification combined cycle carbon dioxide
recovery, transport, and disposal, ANL/ESD-34, 1996
4. Dow Chemical Company, 2004: Selexol solvent for gas treating, www.dow.com
5. Epps R., 1994: Use of Selexol Solvent for Hydrocarbon Dewpoint Control and
Dehydration of Natural Gas, presented at the Laurance Reid Gas Conditioning
Conference, Norman, OK
6. Gas Processes, 2002: Hydrocarbon Processing, UOP LLC, Des Plaines, Illinois.
7. IEA, 2003: Potential for improvement in gasification combined cycle power
generation with CO capture, Report number PH4/19
2
8. Newman S. A., 1985: Acid and sour gas treating processes: latest data and methods
for designing and operating today’s gas treating facilities, Gulf Publishing Co.
9. Kohl A.L. and Riesenfeld F.C., 1985: Gas Purification, Fourth Edition, Gulf
Publishing Company
10. Korens N., Simbeck D.R., Wilhelm D.J., 2002: Process Screening Analysis of
Alternative Gas Treating and Sulfur Removal for Gasification, Revised Final Report,
December 2002, Prepared by SFA Pacific, Inc. Mountain View, California
11. Personal communication with UOP, 2003
12. Sciamanna S. and Lynn S., 1988: Solubility of hydrogen sulfide, sulfur dioxide,
carbon dioxide, propane, and n-butane in poly(glycol ethers), Ind. Eng., Chem. Res.,
27
13. Shah V.A., 1988: Low-cost ammonia and carbon recovery, Hydrocarbon Process.,
67(3)
14. UOP, 2002: Use of SELEXOL Process in Coke Gasification to Ammonia Project,
UOP report
171

Chapter 6. GREENFIELD IGCC POWER PLANT WITH AND WITHOUT CO
2
CAPUTRE
Table 6 - 1 Technical design assumption of the IGCC power plant
Parameter Value
Design ambient temperature 59 °F
Design ambient pressure 14.7 psia
ASU oxygen purity 95%
Steam cycle 1400 psi/1000°F/1000°F
Condenser pressure 0.67 psia
Syngas sulfur removal efficiency 99%
NO control fuel gas moisturization
x
Gasifier operation conditions 615 pisa/2450 °F
Spare gasifier number 1
Fuel type Pittsburgh #8
Table 6 - 2 Economic and financial assumption of the IGCC power plant
Capacity factor 75%
Fixed charge factor 14.8%
Cost year 2000
Construction period 4 years
Lifetime 30 years
Fuel price 1.26 $/MBtu
For CO capture plant
2
CO capture efficiency 90%
2
CO product final pressure 2100 psia
2
CO transport and storage 10 $/tonne
2
This section applies the IGCC models in Aspen Plus to investigate factors
influencing the performance and costs of IGCC power plants with and without CO
2
capture. At first, the effects of the quality of coals are studied. Then effects of CO
2
172

capture, plant size, and capital structures are also studied. The general technical design
assumptions are given in Table 6-1 and the economic and financial assumptions are given
in Table 6-2
6.1. The effects of coal types on IGCC performance
For a Texaco gasifier, coal is prepared in a slurry form. The composition of the
slurry (for a given type of coal, the water percentage in the slurry by weight), may
influence the gasifier efficiency and the efficiency of a whole IGCC power plant. To
investigate the effects of water percentage in the slurry, an IGCC system with two GE
7FA gas turbines and two operating gasifiers was studied.
As an important factor determining the actual operation, as well as the economic
feasibility of using a gasifier system, the gasification efficiency is defined as,
H ⋅Q
η = g g ⋅100 (6-1)
gasifier H ⋅M
s s
where η = gasification efficiency (%)
gasifier
H = is heating value of the gas (kJ/m³);
g
Q = is volume flow of gas (m³/s);
g
H = is the heating value of gasifier fuel (kJ/kg);
s
M = is the gasifier solid fuel consumption (kg/s).
s
173

If the lower heating values of the syngas and the fuel are used in the above
equation, the gasification efficiency is the lower heating value gasification efficiency.
Otherwise, it is the higher heating value efficiency.
Texaco gasifiers require the coal to be prepared in a slurry form for transport. The
amount of water added depends on the composition of a coal, especially the carbon, ash
and moisture percent in the coal. At first, the effects of total water percent in slurry on the
performance of IGCC systems are studied. For Pittsburgh #8 coal, Figure 6-1 gives the
effects of water percentage in slurry by weight on the gasification efficiency, the net plant
thermal efficiency and the heat rate of the IGCC plant. The gasification efficiency is as
low as 45% if no extra water is added to the coal, because at a given gasification
temperature there is not enough oxygen to partially oxidize all the carbon in the
feedstock. With the increase of the water percentage in the slurry, the gasification
efficiency increases, and reaches the peak point, approximately 79%, at a total water
percentage of 27% in the slurry by weight. The gasification efficiency decreases with
further increasing the water percentage due to the increase of water content in the syngas.
The thermal efficiency of the whole IGCC system shows the same trend as the
gasification efficiency, which also shows that the gasification efficiency is a major factor
influencing the performance of IGCC systems.
174

80
70
60
50
40
30
20
5 10 15 20 25 30 35 40 45 50
Water (moisture+added) in slurry by weight (%)
175
)%(
ycneiciffE
16000
14000
12000
10000
8000
)hWk/utB(
etar
gnitaeH
Gasification
efficiency (%,
Coal: App MS, 5.05% H O 2 HHV)
Texaco quench
Gasification
T: 2450 F P: 615 psia efficiency (%,
LHV)
Thermal
efficiency (%,
HHV)
Heating rate
Figure 6 - 1 Effect of water percentage in slurry on IGCC performance
The effects of the water percentage in the slurry by weight on the total capital
requirement and the cost of electricity are given by Figure 6-2. It is not a surprise to find
that the there is an optimal water percentage for the COE and TCR of an IGCC power
plant, because COE and TCR are heavily depends on thermal efficiency. However, the
optimal value of water percentage in the slurry in this case is pure hypothetical and
without considering the requirement of the slurryability. The slurryability of a given type
of coal has a minimum requirement of water percentage in the slurry for transportation in
pipes and pumps. For instance, in order to ensure the slurryability for transportation, the
total water percentages in the slurry for Pittsburgh #8, Illinois #6, PRB and ND Lignite
should be no less than 34%, 37%, 44% and 50%, respectively [Breton, 2002]. The
hypothetical testing of all the four types of coal shows that the amount of water added in
the slurry should based on the minimum requirement of the slurryability to avoid that the
slurry composition is far away from the optimal value.

75
70
65
60
55
50
45
5 15 25 35 45
Total water in slurry by weight (%)
176
)hWM/$(
EOC
2000
1800
1600
1400
1200
)Wk/$(
RCT
COE
($/MWh)
TCR
($/kW)
Coal: Pittsburgh #8
Figure 6 - 2 Effect of water percentage in slurry on TCR and COE
Although an entrained flow gasifier, like the Texaco gasifier, is able to gasify all
types of coals regardless of coal rank, caking characteristics, or amount of coal fines, coal
rank may influence the performance of gasifiers and IGCC systems. Here four coals are
used to investigate this influence. These four coals represent bituminous coal, sub-
bituminous coal, and lignite. The compositions of these coals are given in Table 6-3. The
major feedstock parameters are carbon content, ash content, and oxygen content. The
primary energy of coal is from the carbon content, which is reflected in the heating value
of coal. Ash content in coal is a heat sink in gasification, and the oxygen content
influences the oxygen requirement of gasification process. All results derived here are
based on Aspen simulations of the gasifier performance; at this time there is a lack of
empirical data for alternative (low rank) coals.

Table 6 - 3 Compositions of the four coals and their water percentage in slurry
Dry basis
Pittsburgh#8 Illinois#6 Wyoming PRB ND Lignite
Coal rank Bituminous Bituminous Sub-bituminous Lignite
HHV (Btu/lb) 13965 12529 11955 8989
MOISTURE 5.05 13.00 30.24 33.03
ASH 7.63 12.64 7.63 23.77
CARBON 77.74 70.34 69.07 52.32
HYDROGEN 5.14 4.83 4.74 4.00
NITROGEN 1.50 1.33 1.00 1.15
CHLORINE 0.06 0.20 0.01 0.13
SULFUR 2.24 3.74 0.53 1.73
OXYGEN 5.70 6.92 17.02 16.89
Wet basis
MOISTURE 5.05 13.00 30.24 33.03
HHV 13260 10900 8340 6020
LHV2 12761 10381 7722 5431
ASH 7.24 11.00 5.32 15.92
CARBON 73.81 61.20 48.18 35.04
HYDROGEN 4.88 4.20 3.31 2.68
NITROGEN 1.42 1.16 0.70 0.77
CHLORINE 0.06 0.17 0.01 0.09
SULFUR 2.13 3.25 0.37 1.16
OXYGEN 5.41 6.02 11.87 11.31
Water percentage in slurry
Water% 34 37 44 55
2 LHV calculation is based on the following formula given by [George Booras, 2004]: LHV
= HHV – (91.1436 * H + 10.3181 * H O + 0.3439 * O), where H, H O, and O are on an as-
2 2
received basis.
177

Figure 6-3, using Pittsburgh #8 coal as the reference case, compares the gasification
efficiency, thermal efficiency and heat rate of the IGCC power plant using the four types
of coal. From this figure, it is clear that the rank of coal significantly influence the
gasification efficiency and the thermal efficiency of the power plant, which increase with
the increase of the heating value of coal. The heat rate of the IGCC power plant using
lignite coal (ND lignite with a high heating value of 6020 BTU/lb) is about 33% percent
higher than that of the IGCC plant using bituminous coal (Pittsburgh #8 with a high
heating value of 13260 BTU/lb).
1.4
1.3
1.2
1.1
1.0
6000 7500 9000 10500 12000 13500
Coal HHV (Btu/lb)
178
etar
gnitaeh
evitaleR
1.0
0.9
0.8
0.7
&
lamreht
evitaleR
ycneiciffe
noitacifisag
ND Lignite
Pittsburgh #8
Illinois #6
PRB
Relative Heat Rate Relative Efficiency Relative Gasification Efficiency
Figure 6 - 3 Effect of coal rank on the efficiency and heat rate of IGCC plants
The rank of coal also influences the economic factors of IGCC power plants. Figure
6-4 shows that low quality coal significantly increases the capital cost of an IGCC power
plant. For instance, the total capital cost ($/kW) of an IGCC power plant using ND coal is
about 68% higher than that of an IGCC power plant using Pittsburgh #8. On the other
hand, the lower quality coal has the lower fuel price (except ND lignite), which offsets
the effect of coal quality on the cost of electricity. For instance, the cost of electricity of

an IGCC using the PRB coal is only 8.6% higher than that of an IGCC using the
Pittsburgh #8 coal.
1.7
1.6
1.5
1.4
1.3
1.2
1.1
1.0
6000 7000 8000 9000 10000 11000 12000 13000 14000
Coal HHV (Btu/lb)
179
EOC
&
RCT
evitaleR
ND Lignite
Relative TCR
Relative COE
PRB
Illinois #6
Pittsburgh #8
Figure 6 - 4 The effect of coal rank on the TCR and COE of IGCC plants (For the
COE calculation, the coal price ratios based on the actual mine month
coal price are: Pittsburgh #8: Illinois #6: PRB: ND
Lignite=1:0.667:0.2:0.265)
The relative feed rates of oxygen and coal per MWh output of an IGCC using the
four coals are compared in Figure 6-5. For a unit power output, the oxygen flow rate of
the lower rank coal is bigger. For instance, the oxygen flow rate per MWh output of
Illinois #6, PRB, and ND lignite are 1.2, 1.3 and 2.2 times of that of Pittsburgh #8. The
relative flow rate of coal per MWh output shows the similar trend. The relatively higher
feed rates of stock and oxygen require more capital cost and auxiliary power
consumption for an IGCC power plant, which explain why lower rank coal deteriorates
the performance of IGCC plants.

3
2.6
2.2
1.8
1.4
1
6000 7500 9000 10500 12000 13500
HHV of Coal
180
etar
wolf
evitaleR
ND Lignite
PRB
Illinois #6
Pittsburgh #8
Relative O2 flowrate Relative coal flowrate
Figure 6 - 5 Relative oxygen and coal mass flow rate per MWh power generation
An IGCC power plant using the lower rank coal emits more CO because of its
2
lower energy efficiency Figure 6-6 shows that the CO emission rate (kg CO /MWh) of
2 2
an IGCC plant using ND lignite coal is more than 1.3 times higher than that of an IGCC
using the Pittsburgh #8 coal.
1.4
1.3
1.2
1.1
1
6000 7500 9000 10500 12000 13500
HHV of Coal
etar
noissime
2OC
evitaleR
ND
PRB
Illinious #6
Pittsburgh #8
Figure 6 - 6 Relative CO emission for per MWh power generation
2

6.2. Effects of CO capture efficiency
2
Many studies of CO capture from IGCC power plants typically assumed a constant
2
CO capture efficiency in a range of 75% to 92%. CO capture efficiencies used in these
2 2
studies were determined by the study authors, and no studies published investigate the
effect of different CO capture efficiency on the performance of IGCC power plants. In
2
this section, the performance of IGCC power plants, including the CO avoidance cost,
2
energy penalty, capital cost and cost of electricity, are studied with different CO capture
2
efficiencies. An optimal criterion is explored to determine the least-cost CO capture
2
efficiency for an IGCC power plant. The configuration of the IGCC system for this study
is based on one GE 7FA gas turbine and one operating gasifier.
This study is based on the two-stage Selexol process for sulfur removal and CO
2
capture described in Chapter 5. At the first stage, 99% of sulfur content well as 7% of
CO is removal and vented into the atmosphere at the sulfur removing unit. After a two-
2
stage shift reaction, there is approximately 0.5% CO not converted into CO , and this
2
additional amount is also emitted as CO when the fuel gas is burned in the combustor.
2
Hence, the maximum total CO removal efficiency is approximately 92.5%. Here the
2
total CO removal efficiency is defined as:
2
CO captured(mole)
CO
2
removal efficiency= 2
Total carbon in syngas from gasifier(mole)
For the CO captured, this study considers three situations: one is the CO captured
2 2
in the Selexol without compression; one is that the CO captured is compressed to 2100
2
181

psia; the last one is that the CO captured is compressed to 2100 psia, and transported and
2
stored with a cost of 10$/tonne CO .
2
Figure 6-7 shows the power requirement and capital cost of the Selexol process for
CO capture. The power consumption for CO capture varies slowly when the total CO
2 2 2
removal efficiency is lower than 80%. The power consumption rises quickly when the
total CO removal efficiency is higher than 80% because the total flow rate of Selexol
2
increases quickly for very high CO removal efficiency. Compared with the power
2
consumption for compressing the CO stream to 2100 psia, which is about 74 kWh/tonne-
2
CO , the power consumption of the Selexol process with 90% total CO removal
2 2
efficiency is about 44% of the power consumption for CO compression.
2
The capital cost (k$/tonne-CO captured per hour) of the Selexol process (excluding
2
CO compression) reaches the lowest value of 49.2 when total CO capture efficiency is
2 2
in a range from 85% to 90%. Out of this range, the capital cost increases sharply.
36
34
32
30
0.70 0.75 0.80 0.85 0.90 0.95
Total CO capture efficiency
2
182
tnemeriuqer
rewoP
)
OC
ennot/hWk(
2
54
53
52
51
50
49
tnemeriuqer
tsoC
)OC
ennot/$k(
2
Power
Cost
Figure 6 - 7 Power requirement and capital cost of Selexol process for CO
2
capture

The thermal efficiency of an IGCC power plant with CO capture is given in Figure
2
6-8. The thermal efficiency decreases with the increase of the total CO removal
2
efficiency. Compared with the thermal efficiency without CO compression, compressing
2
the captured CO to 2100 psia reduces the thermal efficiency by 2 percent points when
2
the total CO removal efficiency is 90%.
2
0.35
0.34
0.33
0.32
0.31
0.30
0.70 0.75 0.80 0.85 0.90 0.95
Total CO2 capture efficiency
183
ycneiciffe
lamrehT
Efficiency with
compression
Efficiency w/o
compression
Figure 6 - 8 Thermal efficiency of IGCC power plants with CO capture
2
Energy penalty is defined to study the influence of the CO capture on the energy
2
performance of an IGCC power plant as in the following,
reference plant efficiency−capture plant efficiency
EP =
reference plant efficiency
Figure 6-9 gives the energy penalty of an IGCC power plant with different total
CO removal efficiency. Without CO compression, the energy penalty is about 8% when
2 2
the total CO removal efficiency is 70%, and it rises to 10% when the total CO removal
2 2
efficiency is 90%. CO compression further increases the energy penalty. For instance,
2

when the total CO removal efficiency is 90%, the energy penalty including compression
2
is up 15%.
18
16
14
12
10
8
6
0.70 0.75 0.80 0.85 0.90 0.95
Total CO2 removal efficiency
184
)%(
ytlanep
ygrenE
Energy penalty
with CO2
compression
Energy penalty
w/o CO2
compression
Figure 6 - 9 Energy penalty for CO removal (The thermal efficiency of the IGCC
2
reference plant without in this case is 0.371)
The capital cost of an IGCC power plant is also significantly influenced by CO
2
capture. Figure 6-10 gives the total capital requirement (TCR) of an IGCC power plant
with CO capture. When the total CO removal efficiency is lower than 0.9, the total
2 2
capital requirement increases slowly with the increase of the CO removal efficiency.
2
When the total CO removal efficiency is 0.9, the total capital requirement without CO
2 2
compression is about 1800 $/kW, and it’s approximately 11% higher when CO
2
compression is considered.

2050
1950
1850
1750
0.70 0.75 0.80 0.85 0.90 0.95
Total CO2 capture efficiency
185
)Wk/$(
RCT
TCR with
compression
TCR w/o
compression
Figure 6 - 10 Total capital cost of an IGCC power plant with CO capture
2
Figure 6-11 shows the TCR increase percentage between the capture plant and the
reference plant. Without CO compression, the TCR is increased by 16% when the total
2
CO removal efficiency is 90%. The TCR would be increased by about 30% when the
2
captured CO is compressed up to 2100 psia after capture.
2
35
30
25
20
15
10
0.70 0.75 0.80 0.85 0.90 0.95
Total CO2 capture efficiency
)%(
esaercni
RCT
TCR increse
percen w/o
compression
TCR increse
percen with
compression
Figure 6 - 11Total capital cost increase percentage of IGCC power plants with CO
2
capture (The total capital requirement of the reference plant is 1547
$/kW in this study)

Cost of electricity (COE) is an essential factor to evaluate the economic
performance of a power plant. Figure 6-12 shows the COE increase percentage under the
three different situations. Compared to the COE of the reference plant, when the total
CO removal efficiency is 90%, the COE increase percentage without CO compression,
2 2
with CO compression, and with CO transportation and storage is 15%, 25% and 41%,
2 2
respectively.
45
40
35
30
25
20
15
10
0.70 0.75 0.80 0.85 0.90 0.95
Total CO removal efficiency
2
186
)%(
egatnecrep
esaercni
EOC
With S&T
With compression
W/O compression
Figure 6 - 12 COE increase percentage of IGCC plants with CO capture (In this
2
case, the COE of the reference plant is 56 $/MWh)
CO avoidance cost is used to evaluate the price paid for CO capture, which is
2 2
defined as:
COE of capture plant−COE of reference plant
reference plant CO emission rate−capture plant CO emission rate
2 2
Figure 6-13 shows the CO avoidance cost of an IGCC power plant. When the total
2
CO removal efficiency is 0.9, comparing to the case without CO compression, the CO
2 2 2
avoidance cost with CO compression is increased by 1.7 times. When the transportation
2
and storage cost is included, the CO avoidance cost is 2.7 times of the cost without
2

compression. It is also noticed that no matter with CO compression or storage and
2
transportation, the avoidance cost always reaches the lowest point when the total CO
2
removal efficiency is around 90%.
35
30
25
20
15
10
0.65 0.70 0.75 0.80 0.85 0.90 0.95
CO2 capture efficiency
187
)ennot/$(
tsoc
ecnadiova
2OC
With S&T With compression W/O compression
Figure 6 - 13 CO avoidance cost of IGCC plants
2
Figure 6-14 compares the CO emission rates of the capture plant. The relative CO
2 2
emission rate quasi-linearly decreases with the increase of the total CO removal
2
efficiency. When the total CO removal efficiency is 0.9, the CO emission rate of the
2 2
capture plant is 0.091kg/kWh for the capture only case and, it goes up to 0.097 kg/kWh
for the capture and compression case, which is about the 11.7% of the emission rate of
the reference plant.

0.40
0.30
0.20
0.10
0.00
0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95
CO2 capture efficiency
188
)hWk/gk(
etar
noissime
2OC
With compression
W/O compression
Figure 6 - 14 CO emission rate of the capture IGCC plant
2
6.3. Effects of plant size
Generally, the performance and cost of a power plant will vary with a change in the
size of the plant because in a certain range, relatively large plants will be benefit from
economy of scale and higher efficiency. This section shows the influence of the plant size
on IGCC systems and CO capture.
2
Here three sizes are investigated: one gasifier with one GE 7FA gas turbine, two
gasifiers with two GE 7 FA gas turbines, and three gasifiers with three GE 7FA gas
turbines. There is one spare gasifier for each plant. For the capture plant, the CO capture
2
efficiency is 90%, and the final CO product is compressed to 2100 psia.
2
The cost of electricity, thermal efficiency, total capital requirement and the net
output of each plant without CO capture are shown in Figure 6-15. The plant size has
2
notable influence on the total capital requirement. The capital requirement of the biggest
plant is about 280 $/kW less than that of the smallest one. Beside of the effect of
economy of scale on the equipment, the lower capital cost percentage of the spare gasifier

in the bigger IGCC plant is also a major reason for the lower capital cost. The thermal
efficiency is also improved with the increase of the plant size. For instance, the efficiency
of the biggest plant is about 0.5 percentage points higher than that of the smallest one.
Hence the cost of electricity also decreases with the increases of the plant sizes due to the
lower capital requirement and higher efficiency.
The effects of the plant size on the cost of electricity, thermal efficiency, total
capital requirement and net power output of IGCC plants with CO capture, which are
2
given in Figure 6-16, are similar to the effects shown in Figure 6-15.
60
55
50
45
40
35
250 350 450 550 650 750 850
Net Output (MW)
189
)%(
ycncieiffE
&
)hWM/$(
EOC
1600
1500
1400
1300
1200
)Wk/$(
RCT
COE ($/MWh) Thermal efficiency TCR ($/kW)
Figure 6 - 15 Cost of electricity, thermal efficiency and total capital requirement of
different size IGCC plants without CO capture
2

80
70
60
50
40
30
200 300 400 500 600 700 800
Net Capacity (MW)
190
&
)hWM/$(
EOC
)%(
ycneieiffE
2000
1900
1800
1700
1600
1500
)Wk/$(
RCT
COE ($/MWh) Thermal efficiency TCR ($/kW)
Figure 6 - 16 Cost of electricity, thermal efficiency, and total capital requirement of
different size IGCC plants with CO capture (the COE of the capture
2
plant includes the CO transportation and storage cost at a value of 10
2
$/tonne-CO )
2
The CO avoidance cost, as shown in Figure 6-17 slightly decreases with the
2
increase of the plant size. For example, the avoidance cost of the biggest plant is 29
$/tonne-CO captured, which is approximately $2 lower than that of the smallest one.
2
32
31
30
29
28
27
26
25
200 300 400 500 600 700 800
Net Capacity of IGCC (MW)
)ennot/$(
tsoC
ecnadiovA
OC 2
Figure 6 - 17 Effect of plant size on the CO avoidance cost
2
6.4. Finance analysis of IGCC systems
Although IGCC systems show advantages in energy efficiency and emissions,
investments to design and build commercial IGCC power plants in the world have not

solidly stepped forward due to financing, cost and risk concerns [Rosenberg, 2004]. One
of the major issues hindering the application of IGCC is difficulty with financing. A key
challenge with financing IGCC technology is that there is not enough information on
which to make comparisons, or not enough experience bases in the marketplace.
Due to the large capital investment required by an IGCC power plant, typically,
neither the manufacturer nor the owner can self-finance, or secure adequate financing
using their non-project assets. So, project financing with an affordable capital structure is
often the only way that IGCC technology can be built.
The term capital structure refers to the mix of debt and equity that is used to finance
projects. A typical capital structure for a utility company is given in the following Table
6-4.
Table 6 - 4 Capital structure of a typical power plant project (source: IECM
manual)
Title Units Value
Percent Debt % 45
Percent Equity (Preferred Stock) % 10
Percent Equity (Common Stock) % 45
Cost of capital refers to the weighted costs of common stock, preferred stock
(equity returns) and long term debt (debt interests) used to finance a project. For a project
financed by debt and equity, the average capital cost is given by [Ross, 2005],
S B
r = ( ) × r + ( )× r × (1 − T )
WACC S + B s S + B B C
191

where r = average cost of capital after tax for the project
WACC
S = the amount of equity
B= the amount of debt
r = the cost of equity
S
r = the cost of debt (borrowing rate)
B
T = the tax rate
C
Both the cost of equity and the cost of debt depend on the perceived risk of a
project. As an emerging technology for power generation, IGCC is generally viewed to
have higher risk than more mature power generation systems, such as PC power plants.
Hence IGCC faces higher financing cost in the absence of incentive policies.
In order to stimulate deployment of IGCC technology, a 3-Party Covenant has been
proposed, which is a financing and regulatory program aimed at reducing financing costs
and providing a technology risk-tolerant investment structure [Rosenberg, 2004]. The 3-
Party Covenant would be an arrangement between the federal government, state Public
Utility Commission (PUC), and equity investors. The proposal would work as follows
First, Federal legislation authorizes a federal loan guarantee to finance IGCC projects.
The terms of the federal guarantee require that a proposed project obtain from a state
PUC an assured revenue stream to cover return of capital, cost of capital, taxes and
operating costs. The state PUC provides this revenue certainty through utility rates in
states with traditional regulation of retail electricity sales. The equity investors (electric
192

utility or an independent power producer) negotiate performance guarantees to develop,
construct, and operate the IGCC plant. A fair equity return is determined and approved by
the state PUC before construction begins [Rosenberg, 2004].
In short, the function of this 3-Party Covenant is to adjust the capital structure (debt
to equity ratio) and reduce the interest rate of debt through federal guarantee. For
instance, a typical interest rate of a mid-grade utility debt ranked as BBB was 6.5 percent
in early 2004. With the federal guarantee, the debt would be ranked as AAA, and its
interest would be reduced to 5.5 percent [Rosenberg, 2004].
Six different capital structures are used here to investigate the influence of the
proposed 3-Party Covenant on the capital costs and energy costs of IGCC power plants,
which are given in Table 6-5. The capital structures and resulting cost of capital from
Case A to Case E reflect different debt-to-equity ratios. Case F gives a conventional
capital structure for a power plant project.
Table 6 - 5 Capital structures and cost of capital for IGCC financing
Title Unit Case A Case B Case C Case D Case E Case F
Real Bond Rate % 5.5 5.5 5.5 5.5 5.5 6.5
Real Equity Return % 11.5 11.5 11.5 11.5 11.5 11.5
Percent Debt % 50 60 70 80 90 45
Percent Equity % 50 40 30 20 10 55
Debt/Equity Ratio 1.0 1.5 2.3 4.0 9.0 0.8
Federal Tax Rate % 35 35 35 35 35 35
State Tax Rate % 4 4 4 4 4 4
Property Tax Rate % 2 2 2 2 2 2
Cost of Capital
(Before Taxes) % 8.50 7.90 7.30 6.70 6.10 9.25
Fixed Charge Factor (FCF) % 13.00 12.04 11.12 10.22 9.35 13.88
193

In the following simulation cases, the IGCC system has two GE 7FA gas turbines
and two operation gasifiers. For comparison, the performance and costs of a PC power
plant and a NGCC plant are also calculated using the IECM computer model. The PC
power plant is super-critical with in-furnace NO control, cold-side ESP for particulate
x
control, and a flue gas desulfurization system for SO control. The gross output of the PC
x
plant is 500 MW. The fuel for the PC plant is also the Pittsburgh #8 coal with a price of
1.27 $/MBtu. The NGCC power plant uses two GE 7FA gas turbines, and its steam cycle
heat rate is 9496 kJ/kWh. The natural gas price is 3.797$/GJ. The capacity factors for all
these three type plants are 75%.
Figure 6-18 shows the total capital requirement of the reference IGCC power plant
with the A to F capital structures and the total capital requirement of the PC plant with
the F capital structure. With the same capital structure F, the total capital requirement of
the IGCC plant is about 11% higher than that of the PC power plant. With the incentive
3-Party Covenant capital structures, the total capital cost of the IGCC plant reduces with
an increasing debt-to-equity ratio, because higher debt percentage in the capital structure
lowers the Allowance for Funds during Construction (AFDC).
194

1300
1250
1200
1150
1100
1050
1000
A - B - C - D - E - F - F -PC
IGCC IGCC IGCC IGCC IGCC IGCC
195
)Wk/$(
RCT
Figure 6 - 18 Total capital requirement of the IGCC and PC plant based on
different capital structures
The effect of the capital structure on the cost of electricity is show in Figure 6-19.
Among the IGCC, PC and NGCC plants with the same conventional capital structure
(Case F), the IGCC power plant has the highest COE, and NGCC has the lowest one.
However, the COE of the IGCC with the capital structure of Case A is 43.9 $/MWh,
which is almost break-even with that of the PC plant. When the debt-to-equity ratio in the
capital structure increases from Case A to Case B, the COE of the IGCC plant is even
lower than that of the NGCC plant.

50
45
40
35
30
25
20
A - B - C - D - E - F - F -PC F -
IGCC IGCC IGCC IGCC IGCC IGCC NGCC
196
)hWM/$(
EOC
Figure 6 - 19 Cost of electricity of IGCC plant with different capital structures
The IGCC plant shows its advantage if CO capture is included. From Figure 6-20,
2
it is clear that even with the common capital structure, the total capital requirement of the
IGCC capture plant is still lower than that of the PC capture plant.
2000
1900
1800
1700
1600
1500
1400
A - B - C - D - E - F -IGCC F -PC
IGCC IGCC IGCC IGCC IGCC
)hWM/$(
RCT
Figure 6 - 20 Total capital requirement of IGCC and PC capture plants under
different capital structures
With the same conventional capital structure, the COE of the IGCC capture plants,
as shown in Figure 6-21, is about 22 percent lower than that of the PC power plant, and
about 12 percent higher than that of the NGCC plant. When the debt-to-equity ratio

increases to 2.3, the COE of IGCC is the same as that of NGCC plant. However, it should
be noticed that the natural price used here is a relatively low value based on recent U.S.
gas prices. If the nature gas price goes up to 4.66 $/MJ, calculation shows that with the
same conventional capital structure, the COE of the NGCC capture plant will be same as
that of the IGCC capture plant. Considering the highly volatile price of natural gas in the
foreseeable future, even without any incentive policies an IGCC capture plant could be
competitive with an NGCC capture plant.
90
80
70
60
50
40
A - B - C - D - E - F - F -PC F -
IGCC IGCC IGCC IGCC IGCC IGCC NGCC
197
)hWM/$(
EOC
Figure 6 - 21 COE of IGCC, PC and NGCC capture plants with different capital
structures
In conclusion, many factors influence the performance and cost of IGCC power
plants. For the current commercial gasifier designs that employ slurry coal feeding, the
use of low rank coal significantly reduces the thermal efficiency of an IGCC plant. The
plant size also is an important factor influencing the total capital cost of an IGCC plant
due to the economy of scale. For CO capture, there is an optimal CO capture efficiency
2 2
that minimizes the CO avoidance cost. Based on the current CO capture procedure, this
2 2
optimal CO capture efficiency is in a range from 85% to 90%. Finally, without an
2

incentive financing approach, the IGCC power plant without CO capture is less
2
competitive than the PC and NGCC power plants in terms of both the total capital
requirement and the COE. An incentive financing policy for IGCC power plants, like the
3-Party Covenant proposed by Rosenberg [2004], can help IGCC power plants enter into
commercial operation more widely. Due to the advantages of IGCC plants for CO
2
capture, even without incentive financing policies IGCC capture plants are competitive
with PC and NGCC capture plants.
198

REFERENCES (CHAPTER 6)
1. Booras G., and Holt N, 2004: Pulverized Coal and IGCC Plant Cost and
Performance Estimates, Gasification technologies, Washington, DC, October 3-6,
2004
2. Breton D. L. and Amick P., 2002: Comparative IGCC cost and performance for
domestic coals, gasification technology conference, Oct., 2002, San Franscio
3. Rosenberg W.G., Alpern D.C., and Walker M.R., 2004: Deploying IGCC in This
Decade With 3-Party Covenant Financing, ENPR discussion paper, discussion
paper 2004-7, Harvard University, Cambridge, MA
4. Jaffe R.W., 2005, Corporate Finance, Seventh Edition, McGraw-Hill
5. IECM User Manual, 2005, Department of Engineering and Public Policy, Carnegie
Mellon University, Pittsburgh, PA
199

Chapter 7. IGCC REPOWERING WITH CO CAPTURE
2
North America has over 320,000 MWe of existing coal-fired power plants, which
accounts for 35% of the total installed capacity and 49.8% of the total annual power
generation in North America [Simbeck, 2001; Smock, 1990, EIA, 2004]. Most of the
existing coal-fired power plant capacities are pulverized coal (PC) boilers that are 25-35
years old. These existing coal-based power plants have the highest CO emission rate,
2
due to the use of high carbon fuel (coal) and a relatively low thermal efficiency. What is
the technical and economic potential to reduce CO emissions from these existing power
2
plants in the event that new environmental regulations place limits on carbon emissions?
One recent study looked at retrofitting plants with an amine scrubber, and found this to be
a costly measure that would substantially degraded plant performance [Rao, 2002].
However, IGCC repowering with CO2 capture offers a substantially different option to
this problem.
IGCC repowering can be defined as the integration of gasification units, gas turbine
generator units and heat recovery units into an existing steam power plant. Compared to
other repowering technologies, IGCC repowering without CO capture is usually
2
considered to be less attractive due to the expense of the gasification units [Brander,
1992]. However, it does present several advantages. IGCC repowering can substantially
increase the capacity and thermal efficiency of an old PC plant. The net output of a
repowered IGCC plant can be up to three times or more of the original PC plant’s output.
At the same time, the emissions of NO , SO , Hg and solid waste can be dramatically
x x
reduced [Daledda, 1995; Bajura, 1995]. Shorter construction time and re-use of existing
equipment (cooling system, steam turbine/generator units), infrastructure (road/railroad
200

connections, office building), and existing transmission capacity will reduce the capital
cost relative to a new IGCC plant. Furthermore, re-use of the existing plant land can
simplify the complicated site studies and authorization procedures [Makansi, 1994]. If the
purpose of repowering is to mitigate CO emissions, IGCC repowering can reduce CO
2 2
emissions while also improving capacity and efficiency.
This section provides an overview of the available options of using IGCC
technology for repowering PC power plants. Then the decision factors which should be
considered for an IGCC repowering project are discussed. Finally, the cost and
performance of IGCC repowering are preliminarily analyzed, and results are summarized
to show how IGCC repowering might be an attractive option for improving the
performance of existing power plants.
7.1. IGCC repowering options
There are four major approaches for IGCC repowering, which are site repowering,
feedwater heating repowering, boiler hot windbox repowering and heat recovery
repowering [Sullivan, 1994; Najjar, 1994; Stenzel, 1995]. Each of them is discussed
below.
7.1.1. Site Repowering
Site repowering is the simplest repowering option. It is to reuse the existing site to
construct a new IGCC power plant or other types of power plants after demolishing
existing units, except for keeping some reusable facilities, such as the cooling water
system, switchyard and buildings. Site repowering has the advantage of being able to
utilize the best available combined-cycle technology without having to make
201

compromises to match the older existing components or systems. When compared to
constructing a new unit on a new site, there can be savings in the permitting process,
transmission access, and socioeconomic considerations for the local area that can make
the site repowering a preferred option. The repowered plant performance would usually
be identical to a new unit.
7.1.2. Feedwater heating repowering
Feedwater heating repowering uses the gas turbine exhaust to heat feedwater in an
existing PC power plant. The steam previously extracted from steam turbines for
feedwater heating is used to generate more power in steam turbines if the existing steam
turbine design limits are not exceeded, or used to augment power output in the
combustion turbine. In order to increase the availability, existing feedwater heaters can be
retained to allow conventional operation when the combustion turbine or the gasifier is
out of service. Feedwater heating repowering can improve the efficiency of the steam unit
by about 15% [Brander, 1992].
7.1.3. Boiler windbox repowering
Windbox repowering utilizes the gas turbine exhaust as the combustion air for the
existing boiler. Boiler windbox repowering technologies can add up to 25% additional
capacity to the unit, improve the efficiency by 10-20%, improve the part load efficiency
and cycling capability, and reduce NO emissions, but windbox repowering appears to be
x
the highest degree of technical complexity of all the combustion-turbine-based
repowering options [Stenzel, 1995].
202

A variant to the boiler windbox repowering approach includes a HRSG to reduce
the temperature of the combustion turbine exhaust and produce additional steam. With
this approach the existing windbox can be retained but will need to be enlarged, or the
boiler will not produce the full steam output. This repowering configuration is commonly
known as warm-windbox repowering and is used primarily to achieve heat rate
reductions.
7.1.4. Heat recovery repowering
In the heat recovery repowering, the plant’s existing boiler is replaced by a gasifier,
combustion turbine and Heat Recovery Steam Generator (HRSG). Heat recovery
repowering uses the gas turbine exhaust to generate steam in a HRSG. High efficiency is
obtained by exchanging condensate, feedwater, and steam between the gasification
system and the heat recovery steam generator.
7.1.5. Evaluation of repowering options
The site repowering is somewhat like building a greenfield IGCC power plant,
which can be roughly estimated based on the performance and cost of a greenfield IGCC
plant. For the feedwater heating and boiler windbox repowering, the existing boilers have
to be kept, and it is necessary to control CO emissions from the existing boilers as well
2
as from the gasifier. Therefore, these two approaches do not fully take advantage of the
low CO capture cost of the gasification process. In the heat recovery repowering, the
2
existing boiler is completely replaced by a gasifier, which is the only source of CO .
2
Hence, for the goal of CO capture, only the heat recovery repowering approach is an
2
attractive choice for IGCC repowering with CO capture.
2
203

7.2. Decision factors for IGCC repowering
Evaluations for repowering projects must include a wide range of business aspects,
load growth forecasts, financial parameters, environmental regulations, fuel cost ranges,
fuel availability, legal issues and many other factors. A repowering analysis usually
follows steps similar to those summarized below [Stenzel, 1995; Weinstein, 1999]:
• Determining the generation system goals; e.g., the amount and value of the
needed additional power, emission reductions, fuel availability and costs,
transmission requirements and/or limitations, forecasted generation load
schedules, target electricity market price and/or other requirements and goals.
• Determining the existing plants that can be repowered to meet the generation
goals by identifying the important site restrictions (e.g., emission limits),
conditions of the existing equipment, and other important information.
• Identifying candidate repowering technologies and perform an initial analysis to
reduce the repowering options to the most competitive technologies.
• Developing the design, operation parameters, capital costs, schedules and
economics (the saving potential and simple pay-out time) for applicable
repowered plants and optional new plants.
• Selecting the best option(s) based on economics and other factors.
There are a number of significant differences in considering IGCC repowering
applications, which include the following.
204

Available space: Reusing old sites is one of the advantages of repowering, but
IGCC repowering with CO capture needs more equipment than other repowering
2
approaches. For an IGCC repowering, the area for new units, the distance from gas
turbine to existing steam turbines are important factors to consider. Hence, site space
could be at a premium for some locations, and installation costs may be increased due to
fitting new units in available space and more complicated layouts. Based on the space
availability, for heat recovery repowering, the existing boilers can be demolished to
provide more space for new units, or retired in place, or retained in standby for increased
reliability states [Weinstein, 1999].
Heat rejection capability: Although the heat rejection from the steam turbine cycle
is almost the same before and after the repowering, the low-energy, non-recyclable waste
heat from the air separation unit and gasification process increases the total amount of
heat rejection. In some cases this additional heat generated by gasification could exceed
the heat rejection limitation permitted for a plant where condenser cooling is provided
from a river, ponder or estuary. For cooling tower installations, this will result in an
increase in condenser pressure, circulation water temperature, and tower evaporation.
This system should be checked to assure that any cooling tower makeup water flow
limitations are not exceeded and that certain critical auxiliary cooling water users, such as
the generator coolers, do not exceed maximum temperature limits. Any such permitting
limitations should be evaluated [Sullivan, 1994].
Transmission constraint on bulk transmission system: IGCC repowering can triple
the capacity of an existing plant and the total capacity of the repowered plant may surpass
the capacity of the original switchyard and transmission system.
205

Demineralized water availability: For IGCC repowering, power augmentation from
the gas turbine and steam turbine is desired, steam or water is available with an
associated increase in the demineralized water requirements.
Air emissions: Emissions from IGCC systems are typically controlled to meet strict
environmental standards. Emissions limitations for the existing boiler can vary
significantly depending on the control technology used, local permitting requirements,
the age of the boiler, and other site specific conditions. Typically, IGCC emissions will
be less than that of the boiler being replaced. This reduction in total emissions will also
benefit the utility by allowing offsets in emissions at other sites.
Steam turbine capabilities: the conditions, capabilities, and limitations of the
existing steam turbine are the most significant factors in determining the feasibility of
IGCC repowering. Optimizing the existing steam turbine performance with the new
combined-cycle components is important for the repowered unit to be able to compete
with a new unit, even if it has lower capital costs. Selecting an appropriate size
combustion turbine to match an existing steam turbine is a key factor to reach the optimal
result. The following section will discuss this key issue: how to select and match a
combustion turbine to an appropriately sized steam turbine for IGCC repowering with
and without CO capture.
2
7.3. Heat recovery repowering design
For a PC power plant, steam is generated in a one, two, or three-pressure boiler for
delivery to a steam-generator. The boiler feed water is heated by steam extracted from the
steam turbine. Figure 7-1 gives the schematic process of a PC power plant with a single-
206

pressure, non-reheat system cycle. This is the simplest steam cycle that can be applied in
a PC plant. It results in a low installed cost. Although it does not produce the highest
combined-cycle thermal efficiency, it is a sound economic selection when fuel is
inexpensive.
Figure 7 - 1 One-pressure, non-reheat steam cycle with steam extraction for
feedwater heating
Multi-pressure (two or three) steam cycles are used to maximize energy recovery
from the boiler. Two or three-pressure steam cycles achieve better efficiency than the
single pressure systems, but their installed cost is higher. They are the economic choice
when fuel is more expensive or if the duty cycle requires a high load factor. Figure 7-2
shows a two-pressure, non-reheat steam cycle. Three-pressure, reheat steam cycle is
shown in Figure 7-3. This cycle can achieve the highest energy efficiency, but the capital
cost is also higher than other steam cycle options.
207

Figure 7 - 2 Two-pressure, non-reheat steam cycle with steam extraction for
feedwater heating
Figure 7 - 3 Three-pressure, reheat steam cycle with steam extraction for
feedwater heating
For a combined cycle power plant, like an IGCC plant or a NGCC plant, its steam
cycle is similar to the PC power plant. Depending on the design criteria, the steam cycle
could be a simple one-pressure style if the capital cost is more concerned than the thermal
208

efficiency (or fuel cost). It can also be a three-pressure, reheat style if the thermal
efficiency is more concerned than the capital cost.
Unlike steam turbines, gas turbines are only available in discrete sizes. For the
IGCC heat recovery repowering option, the capacity of the gas turbines and steam turbine
should match well to fully utilize the waste heat from the gasification process and the gas
turbine. For a greenfield power plant, it is not a problem to product a steam turbine with
an appropriate size to match a given gas turbine. For a repowering project, however, a
steam turbine has existed with a fixed maximum flow capability (power generation
capacity). Once this is reached, no further output capability exists at the site.
There is a range of the steam turbine power output that that can be repowered with a
given gas turbine. The range depends on the temperature and flow rate of the gas turbine
exhaust, the throttle pressure and loading limitation of the existing steam turbine, and the
heat recovery process employed. The low boundary of the range is achieved under the
most restrictive condition—the steam turbine limitations are so severe that the
repowering is only simple replacement of a non-reheat boiler by a gasifier, a gas turbine,
and a HRSG with no modification to either the steam turbine or the feedwater heating
system. This configuration is illustrated in Figure 7-4, which shows the repowered plant
configuration with all existing feedwater heaters in service. This represents the minimum
capital cost approach, which also results in the lowest output, lowest thermal efficiency
alternative.
209

Figure 7 - 4 IGCC repowering with all feedwater heaters (minimum repowering )
If sufficient steam turbine low-pressure section flow passing capability is available,
the low pressure feedwater heaters or all feedwater heaters can be removed from service
as shown in Figures 7-5. These systems require additional heat transfer surface to be
installed in the HRSG to heat the feedwater, which increases the capital cost. The
increased plant output and efficiency may justify the added expense [Brander, 1992].
The maximum power output is achieved under the most ideal condition---the
existing steam turbine has sufficient design margins, and the temperature of a gas turbine
exhaust is high enough so that it can incorporate a three-pressure, reheat HRSG and
eliminate all the feedwater heaters, as shown in Figure 7-6.
210

Figure 7 - 5 IGCC repowering with removing some feedwater heaters (medium
repowering)
Figure 7 - 6 IGCC repowering without feedwater heaters (maximum repowering
case)
7.4. IGCC repowering economic and performance analysis
As discussed above, a wide range of factors have to be considered when evaluating
the performance and cost of a repowering project at a given site. Due to the variability
211

from site-to-site, it is clear that there will be a wide range in the results of economic
evaluation. As an example, consider using a Texaco quench oxygen-blown gasifier and a
GE MS7001F gas turbine to repower an old PC plant using a steam turbine operating at
1400 psig throttle condition. Two simulation models are set up in Aspen Plus to evaluate
the repower range of this configuration. One model simulates the most restrictive
condition, or the minimum case—replacing the existing boiler with a gasifier, a gas
turbine and a HRSG and no modification to the steam turbine and the feedwater system.
In this case, the heat recovered from syngas cooling is only used to reheat and saturate
the syngas fed into the gas turbine. Another model simulates the most favorable
condition, or the maximum case—the steam turbine has sufficient design margins so that
it can be incorporated into a three-pressure reheat HRSG, and remove all the feedwater
heaters. In this case, part of the heat recovered from syngas cooling is used to reheat and
saturate syngas, and the left heat is used for steam generation. The two models are
further revised to incorporate the CO capture function.
2
For the cost analysis, all existing equipment is assumed to be fully amortized, and
the reusable utilities are assumed to be the coal handling facility, the dematerialized water
unit, the boiler feed water system, the steam turbine and the generator. Other assumptions
are given in Table 7-1.
Table 7 - 1 Economic and financial assumption for repowering studies
Fixed charge factor 14.8% Years of construction (yr) 3.5
Capacity factor 75% Lifetime (yr) 30
Fuel type Pittsburgh #8 Fuel price ($/MBtu) 1.27
CO transport and
2
storage ($/tonne) 10 CO final pressure (psia) 2100
2
212

The performance of the repowering cases is given in Table 7-2. A Texaco quench
gasifier and a GE MS7001F gas turbine without CO capture can satisfy the steam
2
requirements of a 60 MW steam turbine if a straight boiler replacement is done. If the
cycle can be optimized using three-pressure reheat HRSG, the corresponding steam
turbine size is approximately 110 MW. The total capital cost of the repowered plants
without CO capture ranges from $1201/kW (maximum case) to $1410/kW (minimum
2
case) as compared to $1547/kW of the greenfield plant. For the repowering plants with
CO capture, the capital costs range from $1656/kW (maximum case) to $2108
2
(minimum case) as compared to $1995/kW of the greenfield plant.
Table 7 - 2 Study results of IGCC repowering with and without CO capture
2
Net
ST plant Thermal CO
2
TCR COE power output efficiency emission
Case ($/kW) ($/MWh) (MW) (MW) (HHV) (kg/kWh)
Min. case 1410 57.5 60.1 225.5 31.1 0.986
Without Max. case 1201 48.8 110.3 274.4 36.7 0.835
CO
2
capture Greenfield 1547 55.7 112.1 276.1 36.9 0.830
Min. case 2108 92.7 60.5 192.1 24.2 0.126
With Max. case 1656 72.5 120.4 251.6 31.3 0.098
CO
2
capture Greenfield 1995 78.3 122.3 253.4 31.5 0.097
The repowering option with lower capital cost also has worse energy efficiency.
The energy efficiencies of the repowering plants without CO capture range from 31.1%
2
(minimum case) to 36.7% (maximum case) as compared to 36.9% of the greenfield plant.
Without CO capture, the COE of the minimum repowering case is slightly higher
2
than that of the greenfield IGCC power plant. However, the COE of the maximum
213

repowering case is around 12.3% lower than that of the greenfield plant. For the capture
plant, the maximum case also has the lowest COE, but the COE of the minimum
repowering case is much higher than the other two cases.
60 53
50
37
40
31
30 23 24
20
20
11 12
10 3
0
Full capture W/O T&S W/O comp.
214
)ennot/$(
tsoc
ecnadiova
2OC
Minimum case Maximum case Greenfield
Figure 7 - 7 CO avoidance cost of IGCC repowering plants (the greenfield IGCC
2
plant without CO capture is used as the reference plant to calculate
2
the CO avoidance cost. Full capture refers to CO capture,
2 2
compression, transport and storage; W/O T&S refers to CO capture
2
and compression without transport and storage; W/O comp. refers to
CO capture without transport, compression and storage)
2
Using the greenfield IGCC without CO capture as the reference plant, as shown in
2
Figure 7-7, the maximum repowering IGCC plant with full CO capture (capture,
2
compression, storage and transportation) reduces the CO avoidance cost from $31/tonne
2
to $23/tonne. On the other hand, the minimum repowering case raises the avoidance cost
to $53/tonne. For CO capture only without compression, the CO avoidance cost is only
2 2
$3/tonne.
According to the above discussion, IGCC repowering with and without CO capture
2
may be an economically attractive option for existing PC power plants. Compared to
building greenfield IGCC plants, IGCC repowering is less capital intensive and has a

shorter construction period. Hence it also provides an option for introducing new power
generation technology with lower risk to utilities. Under suitable conditions, IGCC
repowering may be a cost-effective and attractive option for reducing CO emissions
2
from existing coal-fired plants. However, the cost and feasibility of repowering is very
site specific. Hence, further research is needed to identify the most promising
applications of IGCC repowering based on detailed site-specific assessments.
215

REFERENCES (CHAPTER 7)
1. Simbeck D.R., CO Mitigation Economics for Existing Coal-Fired Power Plants,
2
the Eighteenth Annual International Pittsburgh Coal Conference, 4 December,
2001, Newcastle, NSW, Australia
2. Robert Smock, Performance improvement of old plants gains favor, Power
engineering, Nov. 1990
3. Rao, A.B. and Rubin, E.S. (2002). “A Technical, Economic and Environmental
Assessment of Amine-based Carbon Capture Technology for Power Plant
Greenhouse Gas Control,” Environ. Sci. Technol. 36(20), 4467-4475.
4. J. A. Brander, D. L. Chase, Repowering application considerations, Journal of
Engineering for Gas Turbines and Power, Oct. 1992, Vol. 144
5. Kenneth Daledda, Repowering cuts air pollution, improves station’s efficiency,
Power, April 1995
6. Rita A. Bajura and J. Christopher Ludlow, Repowering with coal gasification and
gas turbine systems: an acid rain control strategy option, Morgantown Energy
Technology Center, DOE
7. Jason Makansi, Repowering: options proliferate for managing generation assets,
Power, June 1994
8. T.M. Sullivan and M.S. Briesch, Repowering: a ready source of new capacity,
Energy Engineering, Vol. 91, No.2 1994
9. Y.S. H. Najjar and M. Akyurt, Combined cycles with gas turbine engines, Heat
recovery systems & CHP, Vol. 14, No.2, 1994
10. William C. Stenzel, Dale M. Sopocy, and Stanley E. Pace, Repowering Existing
Fossil Steam Plants
11. Richard E. Weinstein, Robert W. Travers Advanced Circulating Pressurized
Fluidized Bed Combustion (APFBC) Repowering Considerations
216

Chapter 8. PERFORMANCE AND COST UNCERTAINTY ANALYSIS OF
IGCC SYSTEMS
An IGCC plant is a complex chemical treatment and energy conversion system.
Large scale, commercial experience with IGCC and Selexol systems for CO capture is
2
still limited. Consequently, there are substantial uncertainties associated with using the
limited performance and cost data available to predict the commercial-scale performance
and cost of a new IGCC plant. There are several types of uncertainty associated with a
developing technology, such as the IGCC technology. These uncertainties include
statistical errors, systematic errors, variabilities, and the lack of an empirical basis for
concepts that have not been tested [Frey, 1994]. Uncertainties may apply to different
aspects of the process, including performance variables, equipment sizing parameters,
process area capital costs, requirements for initial catalysts and chemicals, indirect capital
costs, process area maintenance costs, requirements for consumables during plant
operation, and the unit costs of consumables, byproducts, wastes, and fuel. Model
parameters in any or all of these areas may be uncertain, depending on the development
state of the technology, the level of the performance and cost estimates, future market
conditions for new chemicals, catalysts, byproducts, and wastes, and so on.
Given limited performance and cost data, as well as uncertainties associated with
the complexity of IGCC systems, this chapter undertakes a systematic evaluation of
performance and cost uncertainties and a ranking of the importance of different factors in
terms of their potential contribution to the total uncertainty. In this study, the term
uncertainty is used loosely to include variability (for example, in nominal process design
values) as well as true uncertainty in the value of a particular parameter.
217

8.1. Methodology for uncertainty analysis
In this study, the parameter uncertainty analysis assumes that the total uncertainty
can be calculated from an estimate of uncertainty in each of the parameters used in the
performance and cost models. The technique of parameter uncertainty analysis provides a
quantitative way to estimate the uncertainty in model results. The general approach to
perform the parameter uncertainty analysis is given in the following steps [IAEA, 1989]:
• Define the assessment endpoint.
• List all uncertain parameters (include additional parameters if necessary to
represent uncertainty in model structure).
• Specify maximum range of potential values relevant for uncertain parameters.
• Specify a subjective probability distribution for values occurring within this
range.
• Determine and account for correlations among parameters.
• Using either analytical or numerical procedures, propagate the uncertainty in the
model parameters to produce a probability distribution of model predictions.
• Derive quantitative statements of uncertainty in terms of a subjective confidence
interval for the unknown value.
• Rank the parameters contributing most to uncertainty in the model prediction by
performing a sensitivity analysis.
218

• Present and interpret the results of the analysis.
According to the above procedure, to perform a quantitative uncertainty analysis,
the first step is to estimate uncertainties in specific process parameters, which involves
the following several steps:
• Review the technical basis for uncertainty in the process
• Identify specific parameters that should be treated as uncertain
• Identify the source of information regarding uncertainty for each parameter
Depending on the availability of information, the estimate of a parameter
uncertainty can be based on published judgments in the literature, published information
that can be used to infer a judgment about uncertainty, statistical analysis of data, or
elicitation of judgments from technical experts.
8.2. Probability distribution estimation of uncertainty parameters
For this study, reviewing the technical basis for uncertainty and identifying specific
parameters that should be treated as uncertain had been completed along with the
development of the technical and economic models. Then a probability distribution must
be assigned to each of the uncertain parameters. Some of the probability distributions of
parameters came directly from published judgments in the literature. Most of the other
probability distributions were estimated through statistical analysis of data from
reviewing published information. We note that using histograms of published literature
values can sometimes provide a misleading estimate of uncertainty because some
published literature values may have little bearing on how a system actually performs
219

once it has been deployed. With this in mind, much more attention was paid to collect
data from project reports and papers published by industrial companies with real-world
experience.
8.2.1. Data visualization
After data collection, the data set for each parameter was visualized through
plotting the data in figures. Specific techniques for evaluating and visualizing data
include calculating summary statistics, plotting empirical cumulative distribution
functions, representing data using histograms, and generating scatter plots to evaluate
dependencies between parameters. The purposes of visualizing data sets include [Frey,
2002]:
• evaluating the central tendency and dispersion of the data;
• visually inspecting the shape of empirical data distribution as a potential aid in
selecting parametric probability distribution models to fit to the data;
• identifying possible anomalies in the data set (such as outliers);
• identifying possible dependencies between variables.
8.2.2. Probability distribution selection
In choosing a distribution function to represent an uncertainty parameter, besides
the data visualization, prior knowledge of the mechanism that impacts a quantity plays an
important role. Probability distribution selection in this work was done in three steps.
220

As the first step, most of the probability distributions were represented by uniform
distributions or triangular distributions to screen the most important parameters. Uniform
probability is useful when it is possible to specify a finite range of possible values, but no
information is available to decide which values in the range are more likely to occur than
others. Triangular distributions also specify a range, but a mode is also specified. It is
useful when we can specify both a finite range of possible values and a most likely
(mode) value. For instance, for some input parameters, values toward the middle of the
range of possible values are considered more likely to occur than values near either
extreme. When this is the case, the triangular distribution provides a convenient means of
representing uncertainty [Morgan, 1998]. Uniform and triangular distributions are
excellent for screening studies and relatively easy to obtain judgments for relevant
values. In addition to being simple, the shape of the uniform and triangular distributions
can be a convenient way to send a signal that the details about uncertainty in the variable
are not well known. This may help to prevent over-interpretation of results or a false
sense of confidence in subtle details of model results [Morgan, 1998].
Once a particular distribution for an uncertainty parameter has been selected, a key
step is to estimate the parameters of the distribution. The most widely used techniques for
estimating the parameters are the method of maximum likelihood estimation (MLE), the
method of least squares, and the method of matching moments [Morgan, 1998]. MLE
was used in this study when a distribution more complicated than uniform and triangle is
employed.
The fitted parametric distributions may be evaluated for goodness of fit using
probability plots and test statistics. In this study, the empirical distribution of the actual
221

data set was compared visually with the cumulative probability functions of the fitted
distributions to aid in evaluating the probability distribution model that described the
observed data.
8.2.3. Distribution functions of uncertain parameters
During the model development process of IGCC system with CO capture, a
2
number of variables are determined as the uncertain parameters for preliminary
uncertainty screening, which are given in Table E-1, E-2 and E-3 of Appendix E. Several
of the parameters in the above tables were found to be correlated or expected to be
correlated. The probabilistic simulations were exercised both with and without
considering parameter correlations to determine if model results are sensitive to
parameter correlation. Simulations using parameter correlations produced only minor
effect on the results. Therefore, for convenience, the following case study presents the
results based on uncorrelated sampling.
After preliminarily investigating uncertainty ranges of these parameters and their
effects on performance and cost, this thesis focus on two key parameters, capacity factor
and fuel price, for the following reasons. First, preliminary study shows that the
uncertainties associated with these two factors have a significant influence on the CO
2
avoidance cost and on the cost of electricity (which is arguably the most important
criterion for a power plant). Second, uncertainties (including variability) associated with
most of the parameters of the IGCC process and the capture process would disappear or
shrink after the specific plant is designed and installed, but during the operation period
the capacity factor and the fuel price may still change frequently and widely due to
changes in load requirements and fuel price volatility, as described below.
222

Capacity factor distribution
IGCC plants, as other coal-fired power plants, typically provide base load service,
with nominal design capacity factor of 85% assumed in many recent studies (vs. the
historical average of 67% for U.S. coal plants). To consider the possible range of capacity
factors over the lifetime of IGCC plants, historical capacity factor data for power plants
with capacity larger than 250 MW and age less than 30 years were collected from the
DOE/NETL coal-fired power plant database, for the year 2000, and used to simulate the
capacity factor uncertainty of an IGCC power plant.
Using the methodology expressed above, a distribution function for the capacity
factor of an IGCC power plant was represented as a Weibull distribution. Table 8-1
compares the statistic properties of the data points with that of the fitted Weibull
distribution. The empirical cumulative distribution function of the data points and the
cumulative distribution function of the Weibull distribution are compared in Figure 8-1.
These comparisons show that the Weibull distribution is a suitable presentation of the
uncertainty (variability) associated with the capacity factor.
Table 8 - 1 Statistical description of power plant capacity factor data and the fitted
Weibull distribution
Dataset Mean Median Standard Deviation Skewness
Coal Plant Data
(>250 MW, <30 years old) 0.762 0.771 0.104 -0.712
Weibull distribution 0.764 0.775 0.106 -0.568
223

1
0.8
0.6
0.4
0.2
0
0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Capacity factor
224
rotcaf
yticapac
fo
FDC
Weibull Data
Figure 8 - 1 Empirical cumulative distribution functions of the capacity factor
data and the distribution of the Weibull(8.5, 0.81) with Trunc(0, 1)
Fuel price distribution
Figure 8-2 represents the historical Central Appalachian coal prices in the New
York Mercantile Exchange (NYMEX). From 1990 to 2000, coal prices decreased, but
after 2000 coal prices began to increase and price volatility became notably larger. The
historical coal prices shows the importance of considering the risk of an IGCC power
plant exposed to volatile coal prices. Modeling and predicting the future coal prices are
beyond the scope of this thesis. Rather, this thesis focuses on analysis of the effect of
uncertainty of coal prices on IGCC systems based on the historical coal prices in the
recent 15 years.

2.2
2.0
1.8
1.6
1.4
1.2
1.0
0.8
19901991 19921993 19941995 199619971998 19992000 20012002 20032004
Year
225
)utBMM/$(
ecirp
laoC
Figure 8 - 2 Central Appalachian coal price in the New York Mercantile Exchange
(The original coal prices were given for July of each year; the prices
shown here were inflation adjusted to the dollar value in 2000)
The distribution of coal prices is represented as a lognormal distribution. Table 8-2
gives the general statistical properties of the data points and the lognormal distribution.
The empirical cumulative distribution function of the data points and the lognormal
distribution are given in Figure 8-3.
Table 8 - 2 Statistic description of coal price data and the fitted lognormal
distribution
Dataset Mean Median Standard Deviation Skewness
Coal Price Data 1.14 1.02 0.38 2.35
Lognormal 1.17 1.14 0.27 0.64

1
0.8
0.6
0.4
0.2
0
0.5 1 1.5 2 2.5
Coal Price ($/MMBtu)
226
ecirp
laoc
fo
FDC
Data
Lognormal
Figure 8 - 3 Comparison of empirical cumulative distribution function of Central
Appalachian coal price data with the distribution of Lognormal(1.169,
0.273)
8.3. Uncertainty analysis results
In order to analyze uncertainties, a probabilistic modeling environment is required.
In this study, the uncertainty analysis was performed using the IECM computer model,
which employs Monte Carlo simulation for uncertainty analysis. In a Monte Carlo
simulation, a model is run repeatedly, using different values for each of its uncertain
inputs each time. The values of each of the uncertain inputs are generated based on the
probability distribution assigned to uncertain parameters, using Latin Hypercube
sampling.
The following simulation results are based on an IGCC capture plant with two GE
7FA gas turbines, two operation gasifiers and one spare gasifier. Other design parameters
and assumptions are the same as those in Chapter 6.
Figure 8-4 shows the uncertainties associated with the total capital requirement of
the IGCC capture plant. The deterministic total capital requirement in this case is 1714
$/kW. The value of the total capital requirement varies from 1660 to 1790 $/kW, with a

90% confidence interval of [1687, 1760] when the uncertainties due to the IGCC process
(parameters given in Table E-1) are taken into account. From this figure, it is clear that
most of the uncertainty in the total capital cost comes from the IGCC process, rather then
the capture process.
1
0.8
0.6
0.4
0.2
0
1650 1700 1750 1800
TCR($/kW)
227
RCT
fo
FDC
Det.
Unc. of cap.
process
Unc. of IGCC
All factors
Figure 8 - 4 Cumulative distributions of the total capital requirement of the IGCC
plant (Unc. of cap. process is given by Table E-2; Unc. of IGCC is
given by Table E-1 in Appendix E; All factors take into account the
uncertainties from Table E-1 and E-2)
Then, the effect of uncertainties of capacity factor and coal price on the cost of
electricity is given in Figure 8-5. The deterministic value of COE is 69.9 $/MWh. The
uncertainties associated with the fuel price cause the COE to vary from 65 to 79 $/MWh,
with a 90 percentile range of 67~76 $/MWh. If other parameters are fixed, there is a 63%
possibility that the IGCC plants would have a higher COE than the deterministic estimate
due to the assumed variability of the fuel price. Compared to the uncertainty of fuel
prices, the assumed uncertainty of the capacity factor contributes more to the volatility of
the COE. The capacity factor distribution makes the COE change from 59 to 106 $/MWh,
with a 90 percentile range of 63~94 $/MWh. The combined uncertainty of fuel price and

capacity factor causes the COE to change from 58 to 108 $/MWh, with a 90 percentile
range of 62 to 96 $/MWh. In this scenario, the possibility that the COE will be higher
than that of the deterministic result is as high as 65%. In this scenario, the weighted
average COE, which takes into account the value of COE and its probability, is 75.5
$/MWh. The weighted average COE is 5.6 $/MWh higher than the deterministic result.
Because the weighted average COE takes into account the potential operating
uncertainties of an IGCC plant, it maybe a more suitable measure of performance of the
IGCC plant than the deterministic result based on a static situation.
1
0.8
0.6
0.4
0.2
0
55 60 65 70 75 80 85 90 95 100
COE ($/WMh)
228
EOC
fo
FDC
CF
Fuel
CF&Fuel
Deterministic
Figure 8 - 5 Cumulative distribution of the cost of electricity of the IGCC plant
The distributions of CO avoidance costs are given in Figure 8-6. The distribution
2
of the avoidance cost values are calculated based on the deterministic COE of the IGCC
reference plant, and the probabilistic COE values of the IGCC capture plant. If both the
fuel price and the capacity factor uncertainties are taken into account, the range of CO
2
avoidance cost is from 13.4 to 78.6 $/tonne CO , with a weighted average cost of $36.6
2
(weighted average 1 in the figure).

It is interesting to compared this weighed average costs with two other CO
2
avoidance cost measures. One is the deterministic CO avoidance cost which is calculated
2
based on the deterministic COE values of the IGCC reference plant and the IGCC capture
plant. The other measure is a weighted average CO avoidance cost (weighted average
2
cost 2 in the figure) which is calculated based on the weighted average COE of the IGCC
reference plant and the IGCC capture plant. Hence, the difference between the three CO
2
avoidance cost is that the deterministic cost is calculated without considering
uncertainties in both the reference plant and the capture plant; the weighted average 1
cost is calculated with considering uncertainties only in the capture plant; and the
weighted average 2 cost is calculated considering uncertainties in both the capture plant
and the reference plant. It is found that the deterministic CO avoidance cost has the
2
lowest value ($29.5/ton), the weighted average 1 cost has the highest cost ($36.6/ton),
and the weighted average 2 cost has an intermediate cost of $30.9/ton. Because the
weighted average 2 cost takes into account the uncertain operating conditions in both the
reference and the capture plant, this value is arguably the most realistic CO avoidance
2
cost. Not considering the uncertainty in the reference plant and the capture plant (or just
considering the uncertainty in one of the two plants) will lead to either higher or lower
estimates of the CO avoidance cost.
2
229

1
0.8
0.6
0.4
0.2
0
10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85
CO avoidance cost ($/tonne CO)
2 2
230
tsoc
ecnadiova
OC
fo
FDC
2
CF
Fuel
CF&Fuel
Deterministic
Weighted average 2
Weighted average 1
Figure 8 - 6 Cumulative distribution of the CO avoidance cost
2
The uncertainty and variability in IGCC systems with CO capture come from the
2
limited experience in producing, constructing and operating IGCC power plants with CO
2
capture. Most of the uncertainties associated with the capital cost of an IGCC capture
plant come from the IGCC process itself. Assumptions about the fuel price and the
capacity factor (especially the capacity factor) can change the estimated cost of electricity
and the CO avoidance cost significantly. Hence, using the most realistic capacity factor
2
estimates to evaluate the performance of IGCC plants and CO capture is especially
2
important.

REFERENCES (CHAPTER 8)
1. Frey C., 1994: Probabilistic Performance, Environmental, and Economic
Evaluation of an Advanced Coal Gasification System, Proceedings of the 87th
Annual Meeting, Cincinnati, OH, June 19-24, 1994
2. International Atomic Energy Agency (IAEA). 1989. Evaluating the Reliability of
Predictions Made Using Environmental Transfer Models. IAEA Safety Series 100.
Vienna, Austria
3. Rubin E.S. and A.B. Rao, 2002: Uncertainties in CO capture and sequestration
2
costs, GHGT-6 paper, 2002
4. Frey H.C. and J.Y. Zheng, 2002: Quantification of variability and uncertainty in air
pollutant emission inventories: method and case study for utility NOx emissions,
Journal of the air & waste management association, Vol. 52, Sep. 2002
5. Cullen A.C., H.C. Frey, 1999: Probabilistic techniques in exposure assessment—a
handbook for dealing with variability and uncertainty in models and inputs, Plenum
Publishing Corporation, 1999
6. Morgan M.G., M. Henrion, M. Small, 1998: Uncertainty—a guide to dealing with
uncertainty in quantitative risk and policy analysis, Cambridge University Press,
1998
7. Marco K., Carlo W., 2004: Fuel Flexibility, the European Gasification Conference,
May 2004
8. McDaniel J.E., Hornick M., 2003: Polk Power Station ICGG 7th year of
commercial operation, Gasification technologies, San Francisco, California
9. Keeler C.G., 2003: Operating Experience at the Wabash River Repowering Project,
Gasification technologies, San Francisco, California
10. Ignacio M.V., 2003: Elcogas Puertollano IGCC Update, Gasification Technologies,
San Francisco, California
11. Yamaguchi M., 2004: First Year Operation Experience with the Negishi IGCC,
Gasification Technologies 2004, Washington DC
12. JGC Corporation, 2003: NPRC Negishi IGCC Startup and Operation, Gasification
Technologies, San Francisco, California
13. Daslay C., BrkicBrkic C., 2003: The Experience of Snamprogetti’s Four
Gasification Projects, Gasification Technologies, San Francisco, California
231

14. Kaptur C.J., 2004: Trends in U.S. Domestic Coal Markets Are Higher Prices and
Higher Price Volatility Here to Stay? Pinecock Perspectives, Issue No.58, Sep,
2004
232

Chapter 9. IGCC SYSTEMS WITH ADVANCED TECHNOLOGIES
While current IGCC power plants show relatively high energy efficiency and low
environmental emissions, there is still much room for improvement in the performance
and cost of IGCC plants. There are substantial R&D programs in the U.S. to improve the
efficiency and cost-effectiveness of IGCC technology. During the next decade or so,
IGCC technology is expected to make significant improvement in the following five
areas [Todd, 2002; O’Brien, 2004]:
• Advanced gasifier concepts with higher efficiency, reliability, and higher
operating pressure for more economic CO capture;
2
• Advanced air separation units with better thermal integration with IGCC systems;
• Syngas cleanup process with less expensive particulate removal systems or hot
gas filtration;
• Advanced gas turbines with high energy efficiency and capacity of burning
syngas and hydrogen-rich fuels;
• Optimal integration with new technologies and components.
In particular, two research areas are likely to produce significant improvements in
the performance and capital cost of the next generation IGCC power plants: advanced air
separation processes and advanced gas turbines. The following sections discuss these
novel technologies and their influence on the development and application of IGCC
technologies in the near future.
233

9.1. Ion Transportation Membrane (ITM)-Based Air Separation Unit
The use of oxygen instead of air for gasification removes excess nitrogen from the
gasifier and results in higher gasification efficiency, higher syngas heat value, lower
capital costs (of gasifiers, heat recovery and downstream gas cleanup systems),
substantially lower NO emissions, and better potential for CO capture. Cryogenic air
x 2
separation, pressure swing absorption, and polymeric membranes are common
commercially available technologies for oxygen production. After making numerous
refinements over a long time period, cryogenic air separation has now evolved as the
most efficient way to produce oxygen at large scale, and has become the typical air
separation process for oxygen-blown IGCC.
Current cryogenic air separation units of an IGCC system still account for about
15% of the plant capital cost, and consume about 10% of the gross power output [Stiegel,
2005]. Hence, reducing capital cost and increasing efficiency of ASU are important to
improve economic viability, and to stimulate commercial deployment of IGCC power
plants. However, the overall thermodynamic efficiency of cryogenic ASU is approaching
its theoretical limit. So few significant technical breakthroughs are expected that would
lead to dramatic oxygen cost reduction [Air Products, 2004].
A promising air separation alternative consists of highly selective and active
membranes with high flux and selectivity to oxygen. Oxygen can be recovered at high
temperatures by passing hot air over non-porous, mixed conducting ceramic membranes.
These membranes, known as ion transport membranes (ITM), utilize an oxygen partial
pressure differential across the membrane to cause oxygen ions to migrate through the
membrane [Air Products, 2002].
234

The separation mechanism of this technology is illustrated in Figure 9-1. Oxygen
molecules cling to the membrane surface on the high oxygen partial pressure side. Due to
the catalytic properties of the surfaces of specialized ceramic materials, oxygen atoms are
ionized by electrons. Then the oxygen ions diffuse across membrane due to the oxygen
partial pressure differential across the membrane. Oxygen ions diffused through the
membrane relinquish electrons and reform as oxygen molecules on the other side of the
membrane (low oxygen pressure) [Air Products, 2004].
Figure 9 - 1 Separation mechanism of membrane-based oxygen production
[Mathieu, 2002]
Due to the highly selective property of the membrane, impurities, such as nitrogen,
are rejected by the membrane. The product gas from the ceramic membrane systems is
virtually 100% pure oxygen. In addition, when ITM devices are built in practice, they
have three valuable properties from operating point of view. First, the ITM devices
require no moving parts, which lead to better reliability. Second, the ceramic membranes
are insensitive to supply air contaminants. All the other air separation technologies, such
as cryogenic air separation, suffer form sensitivity to moisture or the minor constituents
235

of air. Third, the deterioration and failure of a ceramic membrane can be readily detected
due to a fall-off in the pressure of the output oxygen pressure [Air Products, 2003].
100
80
60
40
20
0
236
)%(
ytirup
negyxO
Poly
Cryo PAS ITM
Mem
-200 25 40 800
Process temperature
Figure 9 - 2 Process temperature and oxygen purity of different air separation
technologies [Prasas, 2002]
When integrated with IGCC systems, ITM technology has another important
advantage to improve the energy efficiency of IGCC systems over other air separation
technologies. As shown in Figure 9-2, other air separation processes suffer from the lack
of thermal synergy between the low temperature oxygen production and the high
temperature gasifier operation. Oxygen produced from ITM is in the temperature range at
which coal gasifiers operate. Hence, IGCC processes can be developed so as to include a
significantly high level of thermal integration with air separation process. This will
increase the overall process efficiency and reduce the cost of electricity.
Presently, there is a keen competition among several manufacturers to develop the
membrane-based oxygen production technology. It is being developed under different
nametags by different players, such as ITM (Air Products), OTM (Praxair), COGS

(Litton Life Support). Currently, it appears that Air Products Inc. is holding a leading
position in this field.
With the support of the U.S. Department of Energy, Air Products has been leading a
R&D program for ITM process since 1998 [Richards, 2001]. The goal of the three-phase
program is to cut the cost of oxygen production by approximately one-third compared to
conventional technologies, and demonstrate all the necessary technical and economic
requirements for commercial scale-up. The research team has successfully addressed all
technical and economic requirements for scale-up ITM technology and demonstrated
over 2,300 hours of performance and stability of thin-film membrane structures in several
experiments [Air Products, 2004]. According to Phase III of this program, a pre-
commercial scale ITM process with approximately 25-50 ton-per-day (TPD) design
capacity will be demonstrated in year 2008. After Phase III, the process may be
introduced into the market at the 100’s-of-TPD scale. The technology is expected to be
ready for use in the large tonnage oxygen market (1000’s-of-TPD) within a decade [Air
Products, 2004].
9.2. GE H-class turbines
Improvement of the power block efficiency of IGCC system can further reduce the
cost of electricity. Hence, the next generation of gas turbines is expected to enhance the
economic competitiveness of IGCC plants. Key features of an advanced gas turbine
technology to improve economical power generation of IGCC plants are [Smith, 2001]:
low installed cost resulting from the capacity of the unit matching with a single large
gasifier; high efficiency which reduces fuel consumption and plant cost by reducing the
capacity of the gasification and cleanup system per unit of generation capacity
237

In 1995, GE introduced its new generation of gas turbines—the GE H System. This
H System technology is the first gas turbine to achieve 60% fuel efficiency (LHV basis).
Compared to the current gas turbines, like GE F-class turbines currently used in IGCC
plants, GE H system is a state-of-the-art turbine system. The H System’s pressure ratio is
23:1 which was selected to optimize the combined-cycle performance. This is a major
change from the GE F-class gas turbines, which used a 15:1 pressure ratio. The firing
temperature of H System is 2600 °F/1430 °C, which is about 200 °F/110 °C higher than
the firing temperature of F class turbines [Matta, 2000].
The unique feature of an H turbine is the integrated heat transfer system, which
combines the steam plant reheat process and gas turbine bucket and nozzle cooling
[Matta, 2000]. This feature allows the turbine to be operated at a higher firing
temperature and pressure ratio, which in turn produces dramatic improvements in fuel-
efficiency. However, higher temperatures in the combustor also increase NOx emission.
Using closed-loop steam cooling, GE H System solved the NO problem, and is able to
x
raise firing temperature by 200 °F over the current GE F class of gas turbines and keep
the NO emission levels at the GE F class levels.
x
In conventional gas turbines, the stage 1 nozzle is cooled with compressor
discharge air. This cooling process causes a temperature drop across the stage 1 nozzle of
up to 280 °F. In H System gas turbines, cooling the stage 1 nozzle with a closed-loop
steam coolant reduces the temperature drop across that nozzle to less than 80 °F [Matta,
2000]. This results in a firing temperature 200 °F higher, and with no increase in
combustion temperature.
238

An additional benefit of the H System is that the steam cooling the nozzle recovers
heat for use in the steam turbine, transferring the heat was traditionally waste heat into
usable output. The third advantage of closed-loop cooling is that it minimizes extraction
of compressor discharge air, thereby allowing more air to flow to the combustor for fuel
premixing [Matta, 2000].
Table 9-1 compares the performance of H class turbines and the F class turbines.
The technology improvements shown in the GE H turbines are expected to yield
substantial improvements in performance and significant reductions in the capital cost of
IGCC systems [Brdar, 2000].
Table 9 - 1 Performance characteristics of H-class and F-class turbines [Matta,
2000]
Gas turbine type 9FA 9H 7FA 7H
Firing Temperature, °F (°C) 2400 (1316) 2600 (1430) 2400 (1316) 2600 (1430)
Air Flow, lb/sec (kg/sec) 1376 (625) 1510 (685) 953 (433) 1230 (558)
Pressure Ratio 15 23 15 23
NGCC Net Output, MW 391 480 263 400
Net Efficiency, % (LHV basis) 56.7 60 56 60
NO (ppmvd at 15% O ) 25 25 9 9
x 2
9.3. IGCC systems with ITM oxygen production
In this section, a model to simulate the performance and cost of IGCC systems with
ITM process is set up based on a simple ITM operation model.
9.3.1. ITM performance model
The performance of an ITM process can be simulated on the basis of a set of
operating equations [Air Products, 2002]. As shown in Figure 9-3, compressed, hot air at
239

an absolute pressure P, temperature T, and with the compositionx passes through an
feed ,
ITM vessel. Oxygen permeates the membrane at the oxygen low pressure side and is
collected in the permeate stream at almost 100% purity and an absolute pressure, P .
perm
The oxygen-depleted non-permeate stream emerges out of the ITM unit with the
composition, x , and at an essentially unchanged pressure P. The device operates
np
isothermally at a temperature T.
Figure 9 - 3 Simplified schematic process of an ITM unit
The oxygen-depleted non-permeate gas stream composition (x ) can be calculated
np
from an overall mass balance on the ITM unit. The overall recovery (R) is defined as the
available fraction of oxygen recovered from the feed stream, which is shown as the
following equation,
F
R = perm (9-1)
x ⋅F
feed
where R= the overall recovery of the ITM unit
F = the molar flow rate of permeated oxygen (mole/hr)
perm
F = the molar flow rate of air fed into the ITM unit (mole/hr)
240

x = the molar concentration of oxygen in the air
feed
Theoretically, the overall recovery is ultimately limited by the driving force for
oxygen flux. The driving force is due to the partial pressure difference of oxygen on both
sides of the membrane. As the feed gas passes across the ITM device, the partial pressure
of oxygen decreases since the gas is depleted of oxygen. The theoretical overall recovery
is achieved when the oxygen partial pressure in the air falls as low as that in the permeate
stream. The theoretical overall recovery can be calculated as,
(1−x )P
R =1− feed perm (9-2)
T x (P−P )
feed perm
where R = the theoretical overall recovery of the ITM unit
T
P = the pressure of the permeated oxygen stream (psia)
perm
P= the pressure of the air stream fed into the ITM unit (psia)
x = the molar concentration of oxygen in the air feed
feed
Consistent with many industrial separation processes, from an economical point of
view, a commercial ITM separation process is best operated at 25% -85% of theoretical
recovery. Hence, the practical overall recovery of an ITM unit is,
R =η⋅R (9-3)
T
where R= the practical overall recovery of an ITM unit
= percentage of the theoretical recovery
η
241

According to experimental data from the Air Products, a useful heuristic for
calculating the separation performance of ITM is that the oxygen partial pressures in the
permeate and in the feed streams are related as,
P ≅ 7P (9-4)
O perm
2
where P = the partial pressure of oxygen in the air at the inlet of the ITM unit
O
2
P = the partial pressure of oxygen in the permeate side
perm
According to the mass balance, the molar concentration of oxygen in the non-
permeate gas stream is given by,
x ⋅F−F
x = feed perm (9-5)
O 2 ,np F−F
perm
Substituting Eq. 9-1 into the above equation, the molar concentration of oxygen in
the non-permeate gas stream depending on recovery is given by,
x (1−R)
x = feed (9-6)
O 2 ,np (1−R⋅x )
feed
Air Products has recommended the operating conditions of ITM units which are
summarized in Table 9-2.
Table 9 - 2 Recommended operating parameters for ITM oxygen process design
[Air Product, 2002]
Recommended operating parameters for ITM design Low High
T (°C) 800 900
Feed pressure, P (psia) 100 1000
242

Permeate pressure, P (psia) 1.9 100
perm
Feed O fraction 0.1 0.21
2
Percentage of theoretical recovery 25% 85%
As a new technology in the developing stage, there is no practical data available to
build up its capital cost model. Air products estimated that ITM would be 32% cheaper
than the conventional cryogenic technology [Air Products, 2004]. Hence the capital cost
of an ITM unit is estimated as 68% of the capital cost of a cryogenic ASU with the same
capacity.
9.3.2. IGCC designs with ITM air separation
Figure 9-4 represents a schematic of an IGCC system integrated with the ITM
oxygen production. In this design, the oxygen production process is fully integrated with
the gas turbine [Air Products, 2003]. Compressed air extracted from the gas turbine
compressor is heated by the oxygen-depleted non-permeated air from the ITM unit. Then
the compressed air is further heated by burning a portion of clean syngas to reach the
operating temperature of the ITM unit. The ITM unit is exothermically operated at an
essentially unchanged pressure. The oxygen stream from the ITM unit at a low pressure
and a high temperature is cooled down to produce steam for steam cycle, and then
compressed to a pressure suitable for gasifier operation. The heat from the hot oxygen-
depleted non-permeate air is used to pre-heat the inlet air of the ITM unit. The cooled
oxygen-depleted non-permeate air is then fed into the gas turbine combustor.
Figure 9-5 shows a revised design of IGCC system with ITM oxygen production. In
this design, the air fed into the ITM unit comes from a standalone compressor. This
243

design requires one more air compressor, but offers more flexible operation options. The
two designs are implemented in Aspen simulation model, and the design parameters of
the two cases are given in Table 9-3.
Table 9-3 gives the ITM operating conditions of two IGCC systems with the ITM
process. These two cases are used to investigate the influence of ITM on the performance
and cost of IGCC systems. Other technical and economic assumptions for these case
studies are the same as those given in Table 6-1 and 6-2.
Table 9 - 3 Design parameters of ITM units in the Aspen simulation models
ITM operating ITM air feed ITM percentage of
Case number Notes
temperature (F) pressure (psia) theoretical recovery
ITM-A 1500 250 80% Integrated with GT
ITM-B 1500 200 80% Standalone ITM
244

Steam
Hot O2-depleted air Cold O2-depleted air
Compressed air
Hot air
Water Heat exchanger
Clean syngas
Cooler ITM Burner
Air
O2 compressor
GT
compressor
Coal slurry Raw syngas LT syngas Acid gas
Gasification LTGC removal Power
GT
GT burner
Slag slurry Black water Acid gas
Exhaust
Exhuast to stack
Slag treatment Recycle water Black water Sulfur recovery Steam cycle
treatment Tail gas treatment Water
Condensated water
Slag Water Sulfur
Figure 9 - 4 Overview of an IGCC system fully integrating with the ITM oxygen production
245

Steam
Heat exchanger
Hot O2-depleted air Cold O2-depleted air
Compressed air
Heated air
Water
Cold O2 Hot Air Clean syngas Air
Hot O2
Cooler ITM Burner ITM compressor
Air
O2 compressor
GT
compressor
Coal slurry Gasification Raw syngas LTGC LT syngas A re c m id o g v a a s l Power
GT
GT burner
Slag slurry Black water Acid gas
Exhaust
Exhuast to stack
Slag treatment Recycle water Black water Sulfur recovery Steam cycle
treatment Condensated water Tail gas treatment Water
Slag Water Sulfur
Figure 9 - 5 Overview of an IGCC system with standalone ITM oxygen production
246

Table 9-4 shows the performance and cost of the two ITM cases and the
corresponding cryogenic ASU case. Comparing to the cryogenic ASU case, ITM cases
show significant improvement on the performance and cost of IGCC systems. For
example, the net efficiency of the IGCC plants with ITM increases approximately 2%
percentage points, an improvement of about 5.7% over the cryogenic case. The net power
output increases by 37 MW. The total capital requirement per kW reduces from $1311 to
$1240, and the cost of electricity also reduces by about 2.6 $/MWh. Corresponding to the
improvement of the net efficiency due to the ITM technology, the CO emission also
2
reduces by 5.5%.
Table 9 - 4 Performance and cost comparison of IGCC reference plants with ITM
Effic- Net ASU CO O ITM
TCR TCR COE 2 2
Case iency power TCR emission flowrate TCR
(M$) ($/kW) ($/MWh)
(HHV) (MWe) (M$) (kg/kWh) (TPD) (k$/TPD)
ITM-A 39.3 574.2 59.7 712.3 1240 45.71 0.78 3623.8 16.5
ITM-B 39.4 575.8 59.9 716.9 1245 45.84 0.78 3644.0 16.4
Cryo. 37.1 537.9 89.3 705.7 1311 48.40 0.83 3650.2 24.5
Next, the WGS reactor and Selexol process for CO capture are incorporated into
2
the Case ITM-B to study the effect of adopting ITM technology on the performance and
cost of the capture plant. Table 9-5 shows the performance improvement of IGCC power
plant with CO due to the ITM technology.
2
247

Table 9 - 5 Performance and cost comparison of IGCC capture plant with ITM
ITM Cryo. % Change
Net efficiency 33.6 32.0 5.2
Net power output (MW) 538.1 502.2 7.1
Plant TCR ($/kW) 1631 1714 -4.8
COE ($/MWh) 66.38 69.91 -5.0
CO emission (kg/kWh) 0.092 0.096 -4.8
2
9.4. IGCC systems using GE H turbine
Different from GE F gas turbine, GE H gas turbine uses a closed steam cooling
system, which requires a different gas turbine cooling and heat recovery system. Figure
9-6 shows an overview of the power block of an IGCC system using GE H turbine, which
is a three-pressure, reheat steam cycle and its integration with the gas turbine cooling
system. Gas turbine cooling steam is extracted from the high pressure steam turbine
exhaust to the closed circuit system that is used to cool the gas turbine stage 1 and 2
nozzles and buckets. The steam in the cooling circuit system is heated to approximately
the reheat temperature of the steam cycle, and returns to the immediate pressure steam
turbine.
A syngas heating system utilizes low grade energy from the HRSG to improve
combined-cycle thermal efficiency. Water extracted from the discharge of the HRSG IP
economizer is supplied to the syngas heater to pre-heat and saturate the syngas before it is
supplied to the combustion system. The water leaving the fuel heater is returned to the
cycle through the condensate receiver to the condenser.
248

Figure 9 - 6 Combined power block cycle with GE H turbine [Matta, 2000]
Due to the higher exhaust temperature from GE H turbine, the steam cycle can use
higher pressure and temperature to achieve better energy efficiency. The parameters of
this three-pressure, reheat steam cycle used in the simulation model are given in the
following table. The other general technical and economic parameters these case studies
are the same as those given in Table 6-1 and 6-2.
Table 9 - 6 Steam cycle parameters of the IGCC using GE H turbine
Parameter HP throttle Hot reheat LP admission
Pressure (psig/Bar) 2400/165 345/23.8 31/2.2
Temperature (°F/°C) 1050/565 1050/565 530/277
The capital cost of the H turbine is estimated with the gas turbine cost model
developed in Chapter 3, which is a function of the net power output the gas turbine.
Simulation results show that GE H gas turbines can greatly improve the performance of
IGCC power plants. As shown in Table 9-7, comparing to an IGCC with GE F turbine,
249

the utilization of GE H turbine can increase the net efficiency of IGCC systems by more
than 4 percentage points, reduce the capital cost per kilowatt by more than 4%, lower the
cost of electricity by more than 7%, and reduce the CO emission rate by about 10%. The
2
effects of the utilization of GE H turbine on the performance of CO capture plant are
2
given in Table 9-8.
Table 9 - 7 Performance and cost comparison of IGCC reference plants using
different gas turbines
Parameter H turbine F turbine % Change
Net efficiency 41.4 37.1 11.4
Net power (MW) 860.3 537.9 59.9
TCR ($/kW) 1256 1311 -4.2
COE ($/MWh) 44.82 48.40 -7.4
CO emission (kg/kWh) 0.74 0.83 -10.4
2
Table 9 - 8 Performance and cost comparison of IGCC capture plants using
different gas turbines
Parameter H turbine F turbine % Change
Net efficiency 36.2 32 13.1
Net power (MW) 814.6 502.2 62.2
TCR ($/kW) 1573 1714 -8.2
COE ($/MWh) 62.51 69.91 -10.6
CO emission (kg/kWh) 0.085 0.096 -11.7
2
9.5. IGCC system with ITM and H turbine
IGCC systems adopting ITM oxygen production and GE 7H turbine with and
without CO capture are also modeled and simulated. Table 9-9 presents the performance
2
of an IGCC employing both ITM and GE 7H gas turbine. This next generation IGCC
system with advanced technology expected to be available in the next decade, can
250

achieve a thermal efficiency as high as 42.3% on a higher heating value basis. The total
capital requirement of the IGCC plant with advanced technologies lowers to 1184 $/kW,
which is comparable to or lower than the capital cost of current PC power plants. Due to
the lower capital cost and higher energy efficiency, the cost of electricity of the next
generation IGCC power plant also is estimated to be slightly lower than that of the
current supercritical PC plants.
Table 9 - 9 Performance and cost improvement of the IGCC reference plant using
ITM and GE 7H turbine
Parameter ITM-H turbine Cryo-F turbine % Change
Net efficiency (%, HHV) 42.3 37.1 13.9
Net power (MW) 929.5 537.9 72.8
TCR ($/kW) 1184 1311 -9.7
COE ($/MWh) 42.30 48.40 -12.6
CO emission (kg/kWh) 0.73 0.83 -12.3
2
From Table 9-10, it is noticed that the energy efficiency of the next generation
IGCC system with CO capture is approximately 38.2%, which is higher than that of
2
current IGCC systems without CO capture. The total capital cost of the next generation
2
IGCC systems with CO capture is 1470 $/kW, which is only about 10% higher than that
2
of the current IGCC systems without CO capture.
2
The preliminary performance and cost analysis of IGCC systems with emerging
advanced technologies for oxygen production and gas turbine power generation are
expected to greatly improve the performance of IGCC systems. Simulation results show
that these new technologies will almost offset the influence of CO capture on the
2
performance and cost of current IGCC plants.
251

Table 9 - 10 Performance and cost improvement of the IGCC capture plant using
ITM and GE 7H turbine
Parameter ITM-H turbine Cryo-F turbine % Change
Net efficiency (HHV) 38.2 32.0 19.5
Net power (MW) 902.9 502.2 79.8
TCR ($/kW) 1471 1714 -14.2
COE ($/MWh) 58.6 69.9 -16.2
CO emission (kg/kWh) 0.081 0.096 -15.6
2
As with all cases involving advanced technologies, full-scale demonstrations and
commercialization are needed to verify the performance and cost assumptions employed
in this analysis. For example, while the H-class gas turbine is already offered
commercially, its design performance and cost when fired with syngas or hydrogen-rich
fuel gas (rather than natural gas) remain to be demonstrated and determined reliably.
Similarly, the scale-up and application of the ITM process to an IGCC also remains to be
demonstrated. Hence, the uncertainty characteristics discussed earlier in Chapter 8 apply
equally well to the advanced technologies discussed here.
252

REFERENCES (CHAPTER 9)
1. Air Products, 2002: Method for Predicting Performance of an Ion Transport
Membrane Unit-Operation, Advanced Gas Separation Technology, Allentown,
Pennsylvania
2. Air Products, 2003: The Development of ITM Oxygen Technology for Integration
in IGCC and Other Advanced Power Generation Systems
3. Air Products, 2004: ITM Oxygen for Gasification presented at: Gasification
Technologies 2004 Washington, D.C. 3-6 October 2004
4. Brdar R.D. and Jones R.M., 2000, GE IGCC Technology and Experience with
Advanced Gas Turbines, GER-4207
5. Matta R.K., Mercer G.D., and Tuthill R.S., 2000: Power Systems for the 21st
Century –“H” Gas Turbine Combined-Cycles, GER-3935B
6. Mathieu P., 2002: Private communication
7. O’Brien J.N., Blau J., Rose M., 2004: An Analysis of the Institutional Challenges
to Commercialization and Deployment of IGCC Technology in the U.S. Electric
Industry: Recommended Policy, Regulatory, Executive and Legislative Initiatives,
Final Report prepared for U.S. Department of Energy, National Energy Technology
Laboratory, Gasification Technologies Program and National Association of
Regulatory Utility Commissioners
8. Prasas R., Chen, J., Hassel, B., San, 2002: OTM-an advanced oxygen technology
for IGCC, Francisco, Oct 30, 2002, Gasification conference
9. Richards, R.E., 2001, Development of ITM Oxygen Technology for Integration in
IGCC & Other Advanced Power Generation Systems (ITM Oxygen), Technical
Progress Report for the period January – March 2001 for DOE
10. Stiegel, G.J., 2005: Overview of Gasification Technologies Global Climate and
Energy Project, Advanced Coal Workshop, March 15, 2005
11. Smith R.W., Polukort P., Maslak C.E., Jones C.M., and Gardiner B.D., 2001:
Advanced Technology Combined Cycles, GER-3936A
12. Todd D.M., 2002, The Future of IGCC, Gasification 5, Noordwijk, The
Netherlands
253

Chapter 10. CONCLUSION
The main objective of this research has been to perform a technical and economic
assessment of IGCC systems with and without CO capture. This chapter summarizes the
2
key points presented in this thesis.
10.1. Model development
Detailed engineering models of IGCC systems with oxygen-blown Texaco quench
gasifiers were developed in the Aspen Plus simulation software environment. A previous
cost model of this IGCC system developed at Carnegie Mellon was updated with more
recent data and coupled to the system performance model. To simulate CO capture,
2
performance models of the water gas shift (WGS) reaction system and the Selexol-based
CO capture process were derived using detailed chemical simulations, theoretical
2
analysis, and regression analysis. The cost models of the WGS reaction system and the
Selexol process for CO capture were coupled to (dependent upon) the input and output
2
parameters of the corresponding performance models. The CO capture system was
2
incorporated into the IGCC model in Aspen Plus with re-design of heat integration of the
whole plant. Since the cost models of IGCC systems with and without CO capture were
2
also linked with the plant performance model, all economic assessments reflected plant
design assumptions as well as economic and financial parameters.
The IGCC plant and the Selexol-based CO capture process models were also
2
implemented (in reduced form) in a general power generation modeling framework—
IECM. The probabilistic capability of the IECM was then applied to models of IGCC
systems with and without CO capture in IECM. Therefore, risk and uncertainty analyses,
2
which are important aspects of technical assessment and policy analysis, could be
254

performed. Thus, these models (performance and cost models in Aspen Plus and IECM)
provide an analytic environment and tools for technical and economic assessment of
gasification—based energy conversion systems with various CO capture options on a
2
systematic and consistent basis.
10.2. Model applications
As a developing technology, IGCC systems have shown advantages over traditional
combustion-based energy conversion technologies in terms of energy efficiency,
environmental emissions, and greenhouse gas control. First, the models developed in this
thesis were used to investigate the factors influencing the technical and economic
performance of greenfield IGCC systems with various CO capture options. Then the
2
technical feasibility and economic cost of repowering old PC power plants by IGCC
technology were investigated. The uncertainties associated with IGCC systems and with
the CO capture process were also studied. Finally, the models were extended to include
2
some emerging novel technologies, and used to assess the potential performance and
economic improvement of advanced IGCC systems in the near future.
10.2.1. Greenfield IGCC plants
Through case studies of an IGCC plant using an oxygen-blown Texaco quench
gasifier, the effect of factors including CO capture efficiency, coal type, plant size, and
2
capital structure were studied. Four coals, representing bituminous, sub-bituminous, and
lignite coals, were used to investigate the effects of coal quality on the performance and
cost of IGCC systems with and without CO capture. Although the Texaco gasifier
2
modeled in this study is able to gasify all coals regardless of coal rank, caking
characteristics, or amount of coal fines, the coal rank was found to significantly influence
255

the gasification efficiency, the thermal efficiency and capital cost of an IGCC power
plant. The water slurry feeding mechanism used in this plant design resulted in high (non-
optimal) total water input when utilizing low rank coal, like lignite. The relatively high
feed rates of coal and high oxygen requirements to maintain gasifier temperatures
resulted in increased capital cost and auxiliary power consumption relative to the nominal
plant design using bituminous coal.
The effect of different CO capture efficiencies on the power consumption, thermal
2
efficiency, capital cost, cost of electricity, and CO avoidance cost were studied. It was
2
found that the avoidance cost reaches the lowest point when the total CO removal
2
efficiency is in the range of 85%-90%. This indicates that the optimal CO capture
2
efficiency is also in this range.
Generally, the size of a plant will influence its performance and cost because a
relatively large plant will benefit from an economy of scale and higher efficiency. Three
IGCC systems with one, two, and three GE 7FA gas turbines, respectively, were studied
to show the influence of plant size on IGCC systems and CO capture. The plant size has
2
notable influence on the total capital requirement. The capital requirement of the biggest
plant is about 280 $/kW less than that of the smallest one. Thermal efficiency also
improves slightly with an increase of the plant size. The efficiency of the biggest plant is
about 0.5 percentage points higher than that of the smallest one. The CO avoidance cost
2
decreases slightly with an increase of the plant size. The avoidance cost of the biggest
plant is approximately $2/tonne lower than that of the smallest one.
256

One of the major issues hindering the application of IGCC is difficulty with plant
financing, since IGCC is perceived to be a riskier technology for power generation than
conventional combustion-based systems. Six different capital structures were studied to
investigate the influence of capital structures on the economic competitiveness of IGCC
power plants. Simulation results showed that the total capital requirement of the IGCC
plant reduces with an increase of the debt-to-equity ratio. Further study showed that
without an incentive financing approach, the IGCC power plant without CO capture is
2
less competitive than PC and NGCC power plants in terms of both the total capital
requirement and the cost of electricity (COE). An incentive financing policy for IGCC
power plants, like the 3-Party Covenant analyzed in this thesis, can improve the
competitive ability of IGCC power plants and accelerate their commercialization. Due to
the advantages of IGCC for CO capture, additional analysis showed that if CO capture
2 2
is required for power generation processes, IGCC plants without an incentive capital
structure would be competitive with PC and NGCC plants.
10.2.2. IGCC Repowering
In this thesis, two simulation models were set up in Aspen Plus to evaluate the
repowering cases. One model simulated the most restrictive condition, replacing the
existing boiler with a gasifier, a gas turbine and HRSG, and no modification to the steam
turbine and the feedwater system. Another model simulated the most favorable condition,
in which the steam turbine had sufficient design margins so that it could be incorporated
into a three-pressure reheat cycle with no feedwater heating. The two models were further
revised to incorporate the CO capture function. Simulation results showed that IGCC
2
repowering is less capital intensive and has a shorter construction period, but the
257

feasibility of repowering is very site specific. Under suitable conditions, IGCC
repowering with or without CO capture may be an economically attractive option for
2
existing steam power units. Repowering also provides an option for introducing new
power generation technology with lower risk to utilities.
10.2.3. Uncertainty analysis of IGCC systems
The uncertainty and variability in IGCC systems with CO2 capture come from the
limited experience in producing, constructing and operating IGCC plants with CO2
capture. This study investigated the influence of uncertainties and variability associated
with plants and process designs on the capital cost, cost of electricity and CO2 avoided
avoidance. After preliminary screening, this thesis focused on investigating the
uncertainties of two key parameters, capacity factor and fuel price. Considering the effect
of uncertainties of capacity factor and coal price, there was a significant possibility that
the COE of an IGCC capture plant could be higher than that of the deterministic
estimates found in many recent studies.
10.2.4. IGCC with advanced technologies
There are substantial R&D programs in the U.S. to improve the efficiency and cost
effectiveness of IGCC technology. This thesis studied the effects on performance and
cost of IGCC systems for two emerging advanced technologies—the ion transport
membrane (ITM) for oxygen production and the GE H-class gas turbine for power
generation.
The net efficiency of an IGCC system using ITM increased approximately 2
percentage points, while the total capital requirement of the IGCC plant fell from $1311
258

to $1240. It was also found that GE H-class gas turbines could significantly improve the
performance of IGCC power plants. Compared to IGCC plants using GE F-class turbines,
the utilization of GE H turbines can increase the net efficiency by more than 4 percentage
points, reduce the capital cost per kilowatt by more than 4%, and reduce the cost of
electricity by more than 7%.
This preliminary analysis found that an IGCC plant employing both ITM and GE
7H gas turbines could achieve a thermal efficiency as high as 42.3% on a higher heating
value basis, and that the total capital requirement and the cost of electricity of such an
IGCC plant would be slightly lower than those of current PC power plants. It was also
predicted that the energy efficiency of such an IGCC system with CO capture is
2
approximately 38.2%, which is higher than that of current IGCC systems without CO
2
capture. The total capital cost of the next generation IGCC systems with CO capture
2
would be about 1470 $/kW, which would be able to compete with current IGCC systems
without CO capture.
2
10.3. Some considerations about future work
This work may be furthered in several directions. First, the IGCC plant models
could be developed with greater consideration of optimal system design, especially when
the CO capture process is incorporated into IGCC plants. Studies of the optimal heat
2
recovery scheme, the optimal operation pressure and temperature of the gasifier and
HRSG, the optimal integration of oxygen production and the gas turbine system all would
provide a better understanding of the potential advantages of IGCC systems with CO
2
capture.
259

Second, the models for the water gas shift reaction system and Selexol-based CO
2
capture process could be refined with the availability of additional data. Another
direction of future work might be extending the CO capture process with different
2
commercial solvents, such as Rectisol and Ucarsol.
The IGCC models also could be extended by incorporating more technology
options. For instance, the models of IGCC systems with different gasifier types, such as
the Shell gasifier and E-Gas system. Different syngas cleanup processes, such as high
temperature cleanup processes, advanced CO capture systems, and options for combined
2
capture and sequestration of CO and H S could be studied to provide a more
2 2
comprehensive set of options for technical and economic assessment of CO capture from
2
IGCC systems.
Finally, additional analyses of uncertainties and their effect on performance and
cost estimates could be carried out, especially for many of the advanced technologies
currently under development.
260

APPENDIX A. CO CONVERSION EFFICIENCY OF THE WGS
REACTION
Recall the WGS reaction equation given by:
CO+H
2
O ⇔CO
2
+H
2
Using the definition of the chemical equilibrium constant, the chemical equilibrium
constant (K) for the water gas shift reaction can be given by,
[CO ][H ]
K = 2 2 (A-1)
[CO][H O]
2
where [i] = the molar concentration of species i at the equilibrium state.
Substituting Eq. 4-3, 4-4, 4-5, and 4-6 into Eq. A-1, then the equilibrium constant in
the high temperature reactor (K ) can be expressed as,
h
([CO ] +ξ [CO] )([H ] +ξ [CO] )
K
h
=
([CO]
2 0
−ξ [
h
CO] )
0
([H O
2
]
0
−ξ
h
[CO]
0
)
(A-2)
0 h 0 2 0 h 0
Treating the CO conversion in the high temperature reactor (ξ ) as an unknown
h
parameter, noting that the above equation is parabolic inξ , and then solving Eq. A-2, the
h
CO conversion at the high temperature reactor can be obtained and given by:
u − u2 −4w v
ξ = 1 1 1 1 (A-3)
h 2w
1
where,
u = K ([CO] +[H O] )+([CO ] +[H ] )
1 h 0 2 0 2 0 2 0
261

v = K ([CO] [H O] )−([CO ] [H ] )
1 h 0 2 0 2 0 2 0
w = K −1 (A-4)
1 h
In a similar way, the total CO conversion (ξ ) in the two reactors is given by
total
u − u2 −4w v
ξ = 2 2 2 2 (A-5)
tot 2w
2
where,
u = K ([CO] +[H O] )+([CO ] +[H ] )
2 l 0 2 0 2 0 2 0
v = K ([CO] [H O] )−([CO ] [H ] ) (A-6)
2 l 0 2 0 2 0 2 0
w = K −1
2 l
Furthermore, the equilibrium constants in the high temperature and low temperature
reactors can be calculated as a function of temperature as follows (Davis, 1980):
8240
K = exp( −4.33) (A-7)
h T +dT +459.67
h h
8240
K = exp( −4.33) (A-8)
l T +dT +459.67
l l
Where K and K are the equilibrium constants of shift reaction in the high and
h l
low temperature reactors with taking into account of the approach temperatures; dT and
h
dT are the Aspen approach temperatures (F) for the high and low temperature reactors,
l
262

respectively. T and T are the reaction equilibrium temperatures (F), which are the final
h l
temperatures when the WGS reaction reaches equilibrium states, at the high and low
temperature reactors, respectively. The two temperatures, T and T , can be calculated
h l
using the following regression equations based on ASPEN Plus simulations,
T = 0.0122 P + 0.8668T + 3297 .049[CO ] − 21.634[H O] +
h 0 0 2 0 2 0
356.234[H ] + 401.392[N ] + 2290 .608[CO] [H O]
2 0 2 0 0 2 0
(R2=0.99) (A-9)
T = −0.00136 P + 0.1031T +16608 .87[CO ] + 404.098[H O]
l 0 0 2 0 2 0
+331.976[H ] + 258.772[N ] −1198.036[CO] [H O] −
2 0 2 0 0 2 0
2105.116[CO ] [H ]
2 0 2 0
(R2=0.99) (A-10)
Here T and P are the temperature (F) and pressure (psia) of the syngas fed into the
0 0
high temperature reactor. [i] is the molar fraction of syngas composition i before fed into
0
the high temperature reactor.
According to the definition of CO conversion, the CO conversion in the low
temperature reactor is calculated from the CO conversion in the high temperature (ξ )
h
and the total CO conversion (ξ ) as in the following equation.
tot
1−ξ
ξ =1− total (A-11)
l 1−ξ
h
263

APPENDIX B. METHODOLOGY FOR CALCULATING THE CATALYST
VOLUME OF THE WGS REACTION
The volumes of catalyst, either clean shift catalysts or sour tolerance shift catalysts,
can be calculated as in the following steps.
The catalyst volume (V , ft3 ) can be given by,
cat
VF
V = (B-1)
cat. SV
where SV is the space velocity (1/hr) ; VF is the volumetric flow rate of syngas
(ft3/hr).
For a well mixed, constant volume batch reactor, the space velocity is related to the
fraction conversion of reactant (x) and the reaction rate (r) by the following equation
(Polyanin, 2002):
x dx
SV−1 = ∫ (B-2)
r
0
where x is the fraction conversion of CO to CO .
2
The reaction rate of the WGS reaction can be given by (Doctor, 1994),
⎡ ([CO ] + x)([H ] + x) ⎤
r = k ([CO] −x)([H O] −x)− 2 0 2 0 (B-3)
⎢ 0 2 0 K ⎥
⎣ ⎦
where k is the reaction rate constant of the water gas shift reaction; [CO] [H O]
0, 2 0,
[CO ] [H ] are the inlet molar concentration of CO, H O, CO and H , respectively; K
2 0, 2 0 2 2 2
is the equilibrium constant of the water gas shift reaction at the equilibrium temperature.
264

Equation (B-3) can be substituted into Equation (B-2) to produce the following
equation,
k 2K
⎪
⎧ 2wx−u− q −u− q
⎪
⎫
= ⎨ ln[ ]−ln[ ] ⎬
SV q
⎪
2wx−u+ q −u+ q
⎪
⎩ ⎭ (B-4)
where: w = K - 1
q = u2 −4wv
u = K([CO] +[H O] )+([CO ] +[H ] )
0 2 0 2 0 2 0 (B-5)
v = K([CO] [H O] )−([CO ] [H ] )
0 2 0 2 0 2 0
Using the above equations, the volume of high temperature catalyst (V ) is given
cat,h
by:
VF
V = h (B-6)
cat.,h SV
h
where
k h = K h,real ⎪ ⎨ ⎧ ln[ 2w 1 x 1 −u 1 − q 1 ]−ln[ −u 1 − q 1 ] ⎪ ⎬ ⎫ (B-7)
SV h q 1 ⎪ ⎩ 2w 1 x 1 −u 1 + q 1 −u 1 + q 1 ⎪ ⎭
q = u 2 −4w v
1 1 1 1
u = K ([CO] +[H O] )+([CO ] +[H ] )
1 h,real 0 2 0 2 0 2 0
265

v = K ([CO] [H O] )−([CO ] [H ] )
1 h,real 0 2 0 2 0 2 0
w = K −1 (B-8)
1 h,real
Recalling the equilibrium constant of the water gas shift reaction in Eq. (A-7), then
the equilibrium constant K calculated based on the equilibrium reaction temperature
h,real
in the high temperature reactor can be given by,
8240
K = exp( −4.33) (B-9)
h,real T +459.67
h
In a similar way, the volume of the low temperature catalyst (V ) is given by,
cat,l
VF
V = l (B-10)
cat.,l SV
l
where
k l = K l,real ⎪ ⎨ ⎧ ln[ 2w 2 x 2 −u 2 − q 2 −ln[ −u 2 − q 2 ] ⎪ ⎬ ⎫
SV l q 2 ⎪ ⎩ 2w 2 x 2 −u 2 + q 2 −u 2 + q 2 ⎪ ⎭
q = u 2 −4w v
2 2 2 2
u = K ([CO] +[H O] −2x )+([CO ] +[H ] +2x )
2 l,real 0 2 0 1 2 0 2 0 1
v = K [([CO] − x )([H O] − x )]−[([CO ] + x )([H ] + x )] (B-11)
2 l,real 0 1 2 0 1 2 0 1 2 0 2
w = K −1 (B-12)
2 l,real
266

Here, and the equilibrium constant K is calculated based on the equilibrium
l,real
reaction temperature in the low temperature reactor as:
8240
K = exp( −4.33) (B-13)
l,real T +459.67
l
For the iron-based catalyst, the reaction rate constant (k) is given by [Doctor, 1994],
k 3830
log( ) =6.947− (B-14)
A 0.85T +0.15T +459.67
p h 0
where T is the equilibrium temperature in the high temperature reactor (F); T is
h 0
the syngas temperature at the inlet of the high temperature reactor (F).
For the copper-based catalyst, the reaction rate constant (k) is given by [Campbell,
1970]:
k 3062
log( ) = 6.91− (B-15)
A 0.85⋅T +0.15⋅T +459.67
p l l,i
where T is the equilibrium temperature in the low temperature reactor (F); T is
l li
the syngas temperature at the inlet of the low temperature reactor (F).
Here A is pressure-dependent activity factors, which can be given by [Doctor
p
1994],
P ≤ 400psig ,A = 4⋅10−8P3 +10−5P2 +0.0092P+0.9984
p
P f 400psig ,A = 4 (B-16)
p
267

For a cobalt-based catalyst, the catalyst reaction rate constant is given by the
following equation, which is regressed using the published data [Park, 2000]:
107 95702
Rlnk =119.75+ − (R2=0.996) (B-17)
T2 T
where R is the gas constant; T is the reaction temperature in the reactor.
268

REFERENCES (APPENDIX B)
1. Campbell, J. S., “Influences of Catalyst Formulation and Poisoning on the
Activity and Die-Off of Low Temperature Shift Catalysts”, Ind. Eng. Chem. Proc.
Des. Dev., 9(4), 1970, pp. 588-595.
2. A. D. Polyanin, A. M. Kutepov, et al., Hydrodynamics, Mass and Heat Transfer in
Chemical Engineering, Taylor & Francis, London, 2002.
3. Doctor R.D., Molburg, J.C. Thimmapuram, P., Berry, G.F., and Livengood, D.C.
“Gasification Combined Cycle: Carbon Dioxide Recovery, Transport Disposal,”
ANL/ESD-24, Argonne National Laboratory (Sept. 1994)
4. Park J.N., Kim, J. H., Lee, H. I., A study on the Sulfur-Resistant Catalysts for
Water Gas Shift Reaction IV. Modification of CoMo/-Al O Catalyst with K,
2 3
Korean Chem. Soc. Vol.21, No.12 1239, (Oct. 2000)
269

APPENDIX C. CALCULATION PROCESS OF THE WGS REACTION
SYSTEM
This section illustrates the calculation process of the performance and cost model of
the WGS reaction system discussed in Chapter 4 through a case study. The input
parameters are as follows.
Table C - 1 Input parameters of the WGS model
Syngas to high temperature shift Molar Flow rate Volume
reactor concentration (lb-mol/hr) (cft/hr)
H S 0.000 0.029 0.468
2
CH 0.033 9.849 160.594
4
Ar 0.343 101.302 1656.494
COS 0.000 0.001 0.016
NH 0.000 0.043 0.699
3
N 0.429 126.627 2070.685
2
CO 19.841 5852.992 95708.543
H2O 60.179 17752.435 255451.049
CO 4.197 1238.133 20003.158
2
H 14.976 4417.884 71715.234
2
total 100.000 29499.294 446766.941
total flow rate (lb-mol/hr) 29499.295
Temperature(F) 450
Pressure(psia) 610
The first step is to calculate the CO conversion efficiency in the high and low
temperature reactor, which are given in Table C-2, and C-3.
270

Table C - 2 Calculation of the CO conversion efficiency in the high temperature
reactor
High temperature reactor Value Equations used
Equilibrium temperature at HT
reactor (F) 851.454 (A-9)
Equilibrium constant at HT reactor
temperature 7.062 (A-7)
Equilibrium constant at HT reactor
temperature taking into account
approach temperature 6.278 (B-9)
Middle variable u1 5.278
Middle variable v1 -5.216
Middle variable w1 0.743 (A-4)
CO conversion efficiency in HT
reactor 0.870 (A-3)
CO molar concentration change in
HT reactor 0.173
Table C - 3 Calculation of the CO conversion efficiency in the low temperature
reactor
Low temperature reactor Value Equations used
Equilibrium temperature at LT
575.040 (A-10)
reactor (F)
Equilibrium constant at LT
37.848 (A-8)
reactor temperature
Equilibrium constant at LT
reactor temperature taking into 33.777 (B-13)
account approach temperature
Middle variable u2 32.777 (A-6)
Middle variable v2 -27.220
Middle variable w2 4.027
Total CO conversion efficiency 0.971 (A-5)
271

With the CO conversion efficiency, the compositions of the syngas from the high
and low temperature reactors are given by Table C-4, and C-5.
Table C - 4 Syngas compositions from the high temperature reactor
Flow rate Volume
Molar
Syngas from HT reactor concentration (lb-mol/hr) (cft/hr) Equation used
H S 0.000 0.029 0.677
2
CH 0.033 9.849 232.447
4
Ar 0.343 101.302 2395.548
COS 0.000 0.001 0.023
NH 0.000 0.043 1.011
3
N 0.429 126.627 2994.502
2
CO 2.570 758.105 17927.399 (4-3)
H O 42.908 12657.548 274474.925 (4-6)
2
CO 21.468 6333.020 149086.154 (4-5)
2
H 32.247 9512.770 223837.105 (4-4)
2
total 100.000 29499.294 670949.793
total flow rate (lb-
mol/hr) 29499.295
Temperature(F) 851 (A-9)
Pressure(psia) 604
272

Table C - 5 Syngas compositions from the low temperature reactor
Flow rate Volume
Molar
Syngas from HT reactor concentration (lb-mol/hr) (cft/hr) Equation used
H S 0.000 0.029 0.547
2
CH 0.033 9.849 187.747
4
Ar 0.343 101.302 1935.779
COS 0.000 0.001 0.019
NH 0.000 0.043 0.817
3
N 0.429 126.627 2419.791
2
CO 0.581 171.405 3275.385 (4-7)
H O 40.919 12070.848 206971.530 (4-10)
2
CO 23.457 6919.720 131153.762 (4-9)
2
H 34.236 10099.471 191794.246 (4-8)
2
total 100.000 29499.294 537739.622
total flow rate (lb-
mol/hr) 29499.295
Temperature(F) 575.040 (A-10)
Pressure(psia) 591.882
273

Table C-6 and C-7 give the calculation steps of the catalyst volumes and the process
facility costs of the shift reactors.
Table C - 6 Calculation of catalyst volume and PFC of the high temperature reactor
Equation
Parameter Value used
Middle variable q1^0.5 3.721 (B-8)
Middle variable u1 5.843
Middle variable v1 0.837
Middle variable w1 6.062
Pressure-dependent activity
factors 4.000 (B-16)
Reaction reat in HT reactor 12584.716 (B-14)
SV in HT reactor 1625.458 (B-7)
Volume of HT catalyst 412.776 (B-6)
Volume of HT reactor 495.331
PFC of HT reactor 698.167 (4-23)
Initial HT catalyst cost 20.639
Table C - 7 Calculation of catalyst volume and PFC of the low temperature reactor
Parameter Value Equation used
Middle variable q2^0.5 16.240 (B-12)
Middle variable u2 17.750
Middle variable v2 0.348
Middle variable w2 36.848
Pressure-dependent activity factors 4.000 (B-16)
Reaction reat in LT reactor 23039.292 (B-15)
SV in LT reactor 2829.039 (B-11)
Volume of LT catalyst 67.795 (B-10)
Volume of LT reactor 81.354
PFC of LT reactor 277.444 (4-23)
Initial LT catalyst cost 16.949
274

The final step is to calculate the process facility costs of the heat exchangers, which
is given by Table C-8.
Table C - 8 Process facility costs of the heat exchangers
Parameter Value Equation used
Heat exchanger 1
Hot gas inlet T, F 851.454 (A-9)
Hot gas outlet T 450.000 Design value
Cold fluid inlet T 351.463 (4-20)
Cold fluid outlet T 580.153 (4-11)
Heat released by syngas, Btu/hr 53917730.708 (4-12), (4-13)
Heat released by syngas, kW 15797.895
Log mean temperature difference, C 94.768
PFC of heat exchanger 1 489.104 (4-24)
Heat exchanger 2
Hot gas inlet T, F 575.040 (A-10)
Hot gas outlet T 381.463 (4-17)
Cold fluid inlet T 57.000 Design value
Cold fluid outlet T 400.000 Design value
Heat released by syngas, Btu/hr 1.047E+08 (4-15), (4-16)
Heat released by syngas, kW 30687.447
Log mean temperature difference, C 134.508
PFC of heat exchanger 2 4605.725 (4-25)
Heat exchanger 3
Hot gas inlet T, F 381.463 (4-17)
Hot gas outlet T 100.000 Design value
Cold fluid inlet T 57.000 Design value
Cold fluid outlet T 351.463 (4-20)
Heat released by syngas, Btu/hr 2.416E+08 (4-18), (4-19)
Heat released by syngas, kW 70801.745
Log mean temperature difference, C 20.062
PFC of heat exchanger 3 3878.719 (4-26)
275

APPENDIX D. CALCULATION PROCESS OF THE SELEXOL SYSTEM
FOR CO CAPTURE
2
This section illustrates the calculation process of the performance and cost model
for the Selexol system discussed in Chapter 5 through a case study. The input parameters
are as follows.
Table D - 1 Selexol properties for calculation
Specific Vapor Specific CO Number Specific
2
Viscosity gravity Mole pressure heat solubility of volume
@25C,cp @25C, weight @25C, @25C SCF/US commerci (gallon/lb-
kg/m^3 mmHg Btu/lb F gal @25C al plants mol)
5.8 1030 280 0.00073 0.49 0.485 32 32.574146
Table D - 2 Properties of gases in syngas
Gas CO H CH CO H S COS Ar NH N
2 2 4 2 3 2
Relativly 1.000 0.013 0.067 0.028 8.930 2.330 0.000 4.870 0.000
Solubility
(scf/lb-mol) 377.05 379.50 378.46 379.17 376.08 374.53 379.01 375.88 379.23
Cp 0.199 3.425 0.593 0.248 0.245 0.125 0.520 0.249
(Btu/lb F)
Cv 2.440 0.450 0.172 0.399 0.176
(Btu/lb F) 0.152
K=Cp/Cv 1.310 1.400 1.320 1.410 1.310 1.310 1.600 1.310 1.400
Mole 44.010 16.043 28.010 34.082 60.074 39.948 17.031 28.013
weight 2.016
Solution 160.000 75.000 190.000
heat
(Btu/lb)
276

Table D - 3 Composition of syngas before CO capture
2
Syngas fed into heater exchanger Syngas out heater exchanger
Species
Molar flow rate Volume Molar flow rate Volume
conc. (lb-mol/hr) (cft/hr) conc. (lb-mol/hr) (cft/hr)
H S 0.02 2.77 29.49 0.02 2.77 28.68
2
CH 0.06 7.83 83.31 0.06 7.83 81.02
4
Ar 0.41 56.58 604.45 0.41 56.58 587.89
COS 0.01 1.39 14.81 0.01 1.39 14.40
NH 0.00 0.00 0.00 0.00 0.00 0.00
3
N2 0.68 94.25 1006.95 0.68 94.25 979.36
CO 0.98 136.31 1456.26 0.98 136.31 1416.37
H O 0.19 26.33 229.67 0.19 26.33 221.96
2
CO 33.33 4619.95 47871.78 33.33 4619.95 46479.79
2
H 64.32 8914.59 94165.06 64.32 8914.59 91555.39
2
total 100 13860 145462 100 13860 141365
Temperature (F) 70 70 70 55 55 55
Pressure (psia) 550 550 550 545 545 545
Table D - 4 Assumption for power consumption calculation
Efficiency Efficiency of Efficiency Efficiency
of power compressor of recycle Efficiency of three Evaporation
recovery for Selexol gas of CO stage CO temperature of
2 2
turibne compression compressor compressor compressor refrigeration(F)
0.78 0.8 0.82 0.82 0.82 10
Table D - 5 CO capture efficiency and flashing tank pressures
2
CO capture Flashing tank 1 Flashing tank Flashing tank3
2
efficiency pressure (psia) pressure 2 (psia) pressure (psia)
0.97 60 14.7 4
277

The calculation processes and output parameters of the Selexol system are as
follows.
Table D - 6 CO capture amount required by capture efficiency
2
extra selexol ratio 1.5 Eq. (5-11)
CO capture in absorber
2
(SCF/hr) 1689702.3
CO solution heat(Btu/hr) 31555552.2 Eq. (5-7)
2
Heat released from syngas 1594624.8 Eq. (5-6)
Table D - 7 Calculating the flow rate of Selexol solvent
Estimated Estimated Estimated CO in
2
Selexol Selexol the lean Selexol at
Estimated temperature temperature the last stage (SFC
Selexol flow increase due to increase due to Selexol
rate(lb-mol/hr) CO solution heat syngas cooling
2
10578.96 21.74 1.10 112203.81
Adjusted Selexol Adjusted Selexol Estimated CO in
2
Adjusted Selexol temperature temperature the lean Selexol at
flow rate(lb- increase due to increase due to the last stage (SFC
mol/hr) CO solution heat syngas cooling Selexol
2
9486.24 24.25 1.23 100457.65
Estimated CO in
Adjusted Selexol Adjusted Selexol 2
the lean Selexol at
Adjusted Selexol temperature temperature
the last stage (SFC
flow rate(lb- increase due to increase due to
Selexol
mol/hr) CO solution heat syngas cooling
2
9859.17 23.33 1.18 104466.45
Adjusted Selexol Adjusted Selexol Estimated CO in
2
Adjusted Selexol temperature temperature the lean Selexol at
flow rate(lb- increase due to increase due to the last stage (SFC
mol/hr) CO solution heat syngas cooling Selexol
2
9717.09 23.67 1.20 102939.17
Adjusted Selexol Adjusted Selexol Estimated CO in
2
Adjusted Selexol temperature temperature the lean Selexol at
flow rate(lb- increase due to increase due to the last stage (SFC
mol/hr) CO solution heat syngas cooling Selexol
2 Eq (5-3) ~
9769.18 23.54 1.19 103499.12 Eq. (5-12)
278

Table D – 7 continued
Adjusted Selexol Adjusted Selexol Estimated CO in
2
Adjusted Selexol temperature temperature the lean Selexol at
flow rate(lb- increase due to increase due to the last stage (SFC
mol/hr) CO solution heat syngas cooling Selexol
2
9749.80 23.59 1.19 103290.82 Eq (5-3) ~
Eq. (5-12)
Final Selexol Final Selexol Estimated CO in
2
Final Selexol temperature temperature the lean Selexol at
flow rate(lb- increase due to increase due to the last stage (SFC
mol/hr) CO solution heat Syngas cooling Selexol
2
9756.97 23.57 1.19 103367.90
Table D - 8 Calculation of the operating pressure of sump tank
Operating pressure of sump tank (psia) 180.322
H2 in recycle gas (SCF/hr) 29179.53
Eq. (5-14)
CO in recycle gas 27737.39 ~Eq.(5-17)
2
Table D - 9 Calculation the temperature change of Selexol due to CO release from
2
flash tank
Adjusted amount Estimated heat(Btu) absorbed due Selexol temperature
of CO captured to CO released from Selexol decrease
2 2
SFC/hr 1074956.316 17036816 12.7268
lb-mol/hr 2850.952396
Adjusted amount Estimated heat(Btu) absorbed due Selexol temperature
of CO captured to CO released from Selexol decrease
2 2
SFC/hr 1033634.983 13410930 10.0182
lb-mol/hr 2741.361752
Adjusted amount Estimated heat(Btu) absorbed due Selexol temperature
of CO captured to CO released from Selexol decrease
2 2
SFC/hr 1042429.258 14182615 10.59466
lb-mol/hr 2764.685547
279

Table D – 9 continued
Adjusted amount Estimated heat(Btu) absorbed due Selexol temperature
of CO captured to CO released from Selexol decrease
2 2
SFC/hr 1040557.603 14018380 10.47197
lb-mol/hr 2759.721625
Final amount of Final heat(Btu) abosrbed due to Final Selexol
CO captured CO released from Selexol temperature decrease
2 2
SFC/hr 1040955.941 14053333 10.49808
lb-mol/hr 2760.778079
Table D - 10 Gases retained in the solvent at the flash tank 1
Amount of gases captured in Selexol CO H CH CO H S
2 2 4 2
in first flash tank
SFC/hr 1040955.941 674.496 14.690 47.031 951.506
lb-mol/hr 2760.778 1.777 0.039 0.124 2.530
Table D - 11 Gases released from the solvent at the flash tank 1
Amount of gases released from CO H CH CO H S
2 2 4 2
first flash tank
SFC/hr 752114.26 44303.92 188.06 1434.28 90.98
lb-mol/hr 1994.72 116.74 0.49 3.78 0.24
volume flow(cubic feet/hr) 180304.10 10551.23 44.93 342.25 21.87
Table D - 12 Gases retained in the solvent at the flash tank 2
Amount of gases captured in Selexol CO H CH CO H S
2 2 4 2
in second flash tank
SFC/hr 293983.24 84.01 1.92 5.94 586.35
lb-mol/hr 779.68 0.22 0.005 0.015 1.55
280

Table D - 13 Gases released in the solvent at the flash tank 2
Amount of gases released CO H CH CO H S
2 2 4 2
from second flash tank
SFC/hr 746972.69 590.48 12.76 41.08 365.14
lb-mol/hr 1981.08 1.55 0.03 0.11 0.97
volume flow(cubic feet/hr) 714322.91 561.06 12.159 39.07 350.10
Table D - 14 Gases retained in the solvent at the flash tank 3
Amount of gases captured in CO H CH CO H S
2 2 4 2
Selexol in third flash tank
SFC/hr 103367.89 25.38 1.71 5.27 555.45
lb-mol/hr 274.15 0.07 0.004 0.01 1.47
Table D - 15 Gases released in the solvent at the flash tank 3
Amount of gases released CO H CH CO H S
2 2 4 2
from third flash tank
SFC/hr 190615.34 58.62 0.22 0.66 30.90
lb-mol/hr 505.54 0.15 0.0006 0.002 0.08
volume flow(cubic feet/hr) 492358.34 162.83 0.60 1.85 86.59
Table D - 16 Final product of CO from Selexol
2
CO H CH CO H S
2 2 4 2
SFC/hr 1689702.30 44953.03 201.04 1476.03 487.03
lb-mol/hr 4481.35 118.45 0.53 3.89 1.29
volume flow(cubic feet/hr) 433670.46 11463.08 51.43 377.10 125.39
281

Table D - 17 Power consumption calculation
Power recovery in turbine 1(hp) 594.74 Eq. (5-17)
Power recovery in turbine 2(hp) 586.43 Eq. (5-17)
Power consumption of solvent
compression(hp) 2105.39 Eq. (5-20)
Selexol temperature increase due to
compression 3.74 Eq. (5-21)
Power consumer of refrigeration(hp) 885.54 Eq. (5-22)
Calculation power of recycle gas
compressor
Average k=Cp/Cv 1.39
Power of recycle gas compressor(hp) 2965.07 Eq. (5-19)
Calcuation of power of CO compressor
2
in flash tank 2
Average k=Cp/Cv 1.31
Power of compressor(hp) 1555.53 Eq. (5-19)
Calcuation of power of CO compressor
2
in flash tank 3
Average k=Cp/Cv 1.31
Power of compressor(hp) 738.34 Eq. (5-19)
Calculation of power of CO product
2
compressor
Cold temperature(F) of CO product Design value
2
Average k=Cp/Cv 1.31
Power of compressor(hp) 6317.88 Eq. (5-19)
Total energy consumption of Selexol
(hp) 13386.61
total energy consumption (Kw) 9979.72
282

Table D - 18 Process facility cost of Selexol process
Cost model of Selexol
Cost of absorber per train(k$) 750.43 Eq. (5-23)
Cost of sump tank (k$) 155.24 Eq. (5-25)
Cost of recycle compressor (k$) 2246.19 Eq. (5-26)
Cost of power recovery turbine 1(k$) 275.75 Eq. (5-24)
Cost of power recovery turbine 2 ( k$) 266.87 Eq. (5-24)
Cost of flashing tank 1(k$) 107.33 Eq. (5-31)
Cost of flashing tank 2 (k$) 107.33 Eq. (5-31)
Cost of flashing tank 3 (k$) 107.33 Eq. (5-31)
Cost of CO compressor in flash tank 2 (k$) 1017.81 Eq. (5-28)
2
Cost of CO compressor in flash tank 3 (k$) 614.62 Eq. (5-28)
2
Cost of CO product compressor per stage (k$) 5263.78 Eq. (5-29)
2
Cost of refrigeration 3 (k$) 661.31 Eq. (5-30)
Cost of Selexol pump (k$) 295.29 Eq. (5-27)
Heat exchanger (k$) 1103.99 Eq. (5-32)
283

APPENDIX E. PRELIMINARY DISTRIBUTIONS OF UNCERTAIN
PARAMETERS
The basis of the probability distribution of model parameters (Table E-1, Table E-2,
and Table E-3) for the preliminary uncertainty screening in Chapter 8 is briefly explained
here. As mentioned in Chapter 8, these distributions take into account the data reported in
literatures, modeling approximations, and expert’s technical judgments. The parameters
and their distributions are given in Table E-1, E-2, and E-3.
Table E - 1 Distribution functions assigned to the parameters of the IGCC process
(the distribution functions in this table, except the distribution of the
fixed charge factor, mainly come from reference [1] and were updated
with data from reference [2] and [3])
Determinis
Parameter Unit Distribution function
tic value
Facility cost parameters
Fixed charged % 14.8 Triangular(7.1, 14.8, 17.4)
Engineering and
% of TPC 10 Triangular(7,10,12)
home office fee
Indirection
construction cost % of TPC 20 Triangular(15,20,20)
factor
Project uncertainty % of TPC 12.5 Uniform(10,15)
General facilities % of TPC 15 Triangular(10,15,25)
Process contingency
Oxidant feed % of PFC 5 Uniform(0,10)
Gasification % of PFC 10 Triangular(0,10,15)
Selexol % of PFC 10 Triangular(0,10,20)
Low temperature
% of PFC 0 Triangular(-5,0,5)
gas cleanup
Claus plant % of PFC 5 Triangular(0,5,10)
Beavon-Stretford % of PFC 10 Triangular(0,10,20)
284

Table E – 1 continued
Determinis
Parameter Unit Distribution function
tic value
Process condensate
% of PFC 30 Triangular(0,30,30)
treatment
Gas turbine % of PFC 12.5 Triangular(0,12.5,25)
Heat recovery
% of PFC 2.5 Triangular(0,2.5,5)
steam generator
Steam turbine % of PFC 2.5 Triangular(0,2.5,5)
General facilities % of PFC 5 Triangular(0,5,10)
Maintenance costs
Gasification % of TPC 4.5 Triangular(3,4.5,6)
Selexol for sulfur
% of TPC 2 Triangular(1.5,2,4)
remove
Low temperature
% of TPC 3 Triangular(2,3,4)
gas cleanup
Claus plant % of TPC 2 Triangular(1.5,2,2.5)
Boiler feed water % of TPC 2 Triangular (1.5, 2, 4)
Process condensate
% of TPC 2 Triangular(1.5,2,4)
treatment
Gas turbine % of TPC 1.5 Triangular(1.5,1.5,2.5)
Heat recovery
% of TPC 2 Triangular (1.5, 2, 4)
steam generator
Steam turbine % of TPC 2 Triangular(1.5,2,2.5)
Other fixed operating cost parameters
Labor rate $/hr 25 Triangle (17,25,32)
Variable operating cost parameters
Ash disposal $/ton 10 Triangular(10,10,25)
Sulfur byproduct $/ton 75 Triangular(60,75,125)
285

Table E - 2 Distribution functions assigned to Selexol-based CO capture process
2
Nominal
Performance parameter Unit value Distribution function
Mole weight of Selexol lb/mole 280 Triangular(265,280,285)
Pressure at flash tank 1 Psia 60 Uniform(40,75)
Pressure at flash tank 2 Psia 20 Uniform(14.7,25)
Pressure at flash tank 3 Psia 7 Uniform(4,11)
Power recovery turbine efficiency % 75 Uniform(70,80)
Selexol pump efficiency % 75 Uniform(70,80)
Recycle gas compressor efficiency % 75 Uniform(70,80)
CO compressor efficiency % 79 Triangular(75,79,85)
2
Cost parameter Unit Value Distribution function
WGS catalyst cost $/ft^3 250 Triangular(220,250,290)
Selexol solvent cost $/lb 1.96 Triangular(1.32,1.96,2.9)
% of
Process contingency of WGS system PFC 5 Triangular(2,5,10)
Process contingency of Selexol % of
system PFC 10 Triangular(5,10,20)
% of
Maintenance cost of WGS system PFC 2 Triangular (1, 2, 5)
% of
Maintenance cost of Selexol system PFC 5 Triangular(2,5,10)
Table E - 3 Distribution functions assigned to the fuel cost and capacity
Parameter Unit Deterministic Distribution function
Fuel price $/MBtu 1.3 Triangular(1.0,1.3,2.1)
Capacity factor % 75 Triangular(35, 75, 90)
The data sources of the parameters in the above tables are given in the following:
1. Fixed charge factor: Several studies reports different values, half of which range from
14.5% to 15%. Here a triangular distribution with a default mode value of 14.8% is
286

assigned to this parameter. Values of the fixed charge factor and their sources are
given in the following table.
Fixed charge factor (%) References
7.1 4
11.9 5
14.5~15 6, 7, 8
17.4 9
2. Fuel price: Fuel cost is the major variable operation cost of an IGCC power plant. The
lowest fuel price reported is 1.03 $/MBtu, and the highest price reported is 2.11
$/MBtu. For the uncertainty screening purpose, a rough triangular distribution is
assigned to the fuel price.
Fuel price ($/MBtu) References
1.03 8
1.3~1.5 2, 3, 5, 10
1.58 7
1.66 6
1.79 9
2.11 4
3. Capacity factor: For the uncertainty screening purpose, a triangular distribution with a
mode value of 75% is assigned to the capacity factor.
Capacity factor (%) References
35 11
51 12, 13
60~65 5, 6, 11, 12
65~70 11, 12, 14
70~75 11, 12, 15,
75~80 8, 11, 15
80~85 3, 9, 15
90 7, 16
287

4. Mole weight of Selexol: Selexol solvent is a mixture of dimethyl ethers of polyethylene
glycol with the formulation of CH (CH CH 0) CH , where n is between 3 and 9. Mole
3 2 2 n 3
weight of Selexol influences the calculation of the flow rate of solvent. Different mole
weights are reported. A triangular distribution is assigned to this parameter.
Mole weight of Selexol (lb/mole) References
265 17
280 18, 19
285 20
5. Pressures of flush tanks: Three flush tanks are used to release CO captured in the
2
solvent at reduced pressures. The flash pressure in each flash tank is a design
parameter, which influences the power consumption of CO compression and CO
2 2
capture efficiency. Due to limited data points, uniform distributions are assigned to the
three pressure parameters.
Flash pressure (psia) References
40 (flash tank 3) 21
75 (flash tank 3) 20
14.7 (flash tank 2) 21
25 (flash tank 2) 20
4 (flash tank 3) 21
11 (flash tank 3) 20
6. Power recovery turbine efficiency, Selexol pump and recycle compressor efficiency:
Power recovery turbine and pump are common mechanical devices used in industrial
fields. The efficiency of such devices may vary depending on the flow type and the
operating conditions. The efficiencies, typically, would be around 70-80%. Here a
uniform distribution (uniform(70,80)) is employed [22].
7. CO compressor efficiency: CO compressor is used to compress CO product to
2 2 2
desirable pressures. From the reported data, the compression efficiencies varies from
75% to 88%. Here a triangular is used for this parameter.
288

CO compressor efficiency (%) References
2
75 23
75~85 24
85 25
88 26
8. Selexol solvent cost: The cost of the sorbent depends on various market forces. Here a
triangle distribution is given to the solvent cost.
Selexol cost ($/lb) References
1.4 20
1.96 27
2.9 3
9. WGS catalyst cost: the deterministic value of the catalyst cost from reference [20].
Based on expert’s judgment, the range of the price fluctuation is around ±20%, so a
triangle distribution is given to the catalyst cost.
10. Process contingency of WGS and Selexol system: The deterministic value of the
process contingency came from reference [3]. The value range of the contingency
came from the recommendation of reference [28].
11. Maintenance cost: the maintenance cost is usually expressed as a fraction of the total
plant cost. This parameter depends on some design parameters as well as the operating
conditions [22]. Based on the recommended range of reference [28], as well as
expert’s judgments, triangular distributions are assigned to the maintenance costs of
WGS and Selexol processes.
289

REFERENCES (APPENDIX E)
1. Frey, H.C., and N. Akunuri, "Probabilistic Modeling and Evaluation of the
Performance, Emissions, and Cost of Texaco Gasifier-Based Integrated
Gasification Combined Cycle Systems Using ASPEN," Prepared by North
Carolina State University for Carnegie Mellon University and U.S. Department of
Energy, Pittsburgh, PA, January 2001.
2. Shelton W., Lyons J., 2000: Texaco Gasifier IGCC Base Cases, Process
Engineering Division, NETL, PED-IGCC-98-001
3. Foster Wheeler Ltd, 2003; Potential for Improvement in Gasification Combined
Cycle Power Generation with CO Capture,” IEA Greenhouse Gas R&D
2
Programme, Report Number PH4/19, May 2003
4. Hendriks, C. A., 1994: Carbon Dioxide Removal from Coal-Fired Power Plants.
Kluwer Academic Publishers, Dordrecht, the Netherlands
5. Condorelli P., Smelser, S. C., McCleary G. J., 1991 Engineering and Economic
Evaluation of CO Removal from Fossil-Fuel-Fired Power Plants. Volume 2:
2
Coal Gasification Combined-Cycle Power Plants. Electric Power Research
Institute; Report # IE-7365
6. Doctor R. D.; Molburg J. C., Thimmapuram P. R., 1997: Oxygen-Blown
Gasification Combined Cycle: Carbon Dioxide Recovery, Transport, and
Disposal. Energy Convers. Mgmt. Vol. 38, Suppl.
7. IEA Greenhouse Gas R&D Programme and Stork Engineering Consultancy B.V.,
1999: Assessment of Leading Technology Options for Abatement of CO
2
Emissions; December 1999.
8. Simbeck D., 1998: A Portfolio Selection Approach for Power Plant CO Capture,
2
Separation and R&D Options. Fourth International Conference on Greenhouse
Gas Control Technologies, Interlaken, Switzerland; 1998.
9. Chiesa P., Consonni S, 1998: Comparative Analysis of IGCCs With CO
2
Sequestration. Fourth International Conference on Greenhouse Gas Control
Technologies, Interlaken, Switzerland; 1998.
10. IECM User manual, 2005, www.iecm-online.com
11. McDaniel J.E., Hornick M., 2003: Polk Power Station ICGG 7th year of
commercial operation, Gasification technologies, San Francisco, California
12. Marco Kanaar, Carlo Wolters, 2004: Fuel Flexibility, the European Gasification
Conference, May 2004
290

13. IgnacioMéndez-Vigo, 2003: Elcogas Puertollano IGCC Update, Gasification
Technologies, San Francisco, California
14. Yamaguchi M., 2004: First Year Operation Experience with the Negishi IGCC,
Gasification Technologies 2004, Washington DC
15. Keeler C.G., 2003: Operating Experience at the Wabash River Repowering
Project, Gasification technologies, San Francisco, California
16. Daslav C., BrkicBrkic C., 2003: The Experience of Snamprogetti’s Four
Gasification Projects, Gasification Technologies, San Francisco, California
17. Epps R., 1994: Use of Selexol Solvent for Hydrocarbon Dewpoint Control and
Dehydration of Natural Gas, presented at the Laurance Reid Gas Conditioning
Conference, Norman, OK, February 27-March 2, 1994
18. Sciamanna S. and Lynn S., 1998: Solubility of hydrogen sulfide, sulfur dioxide,
carbon dioxide, propane, and n-butane in poly(glycol ethers), Ind. Eng., Chem.
Res., 27, 1988
19. UOP, 2000: Use of SELEXOL Process in Coke Gasification to Ammonia Project,
UOP report
20. Doctor R.D., etc., 1996: KRW oxygen-blown gasification combined cycle carbon
dioxide recovery, transport, and disposal, ANL/ESD-34, 1996
21. Chiesa P. and Consonni S., 1999: Shift Reactors and Physical Absorption for
Low-CO Emission IGCCs, Journal of Engineering for Gas Turbines and Power,
2
Vol. 121
22. Rao A.B., 2003, A technical, environmental, and economic assessment of Amine-
based carbon capture systems for greenhouse gas control, Ph.D thsis, Carnegie
Mellon University
23. Price, B.C., 1984: Processing high CO gas. Energy Progress, 1984, 4(3)
2
24. Bolland, O. and H. Undrum, 1998: Removal of CO from gas turbine power
2
plants: evaluation of pre- and post-combustion methods. Fourth International
Conference on Greenhouse Gas Control Technologies, 30 Aug-2 Sep., 1998,
Interlaken, Switzerland
25. Hendriks, C., 1994: Carbon dioxide capture from power stations, a report
published by IEA Greenhouse Gas R&D Programme, UK
26. Alston, 2001: Engineering feasibility and economics of CO capture on an
2
existing coal-fired power plant. Final report prepared by Alstom Power Inc.
Report no. PPL-01-CT-09
291

27. Personal communication with UOP.
28. EPRI Technical Assessment Guide, 1993
292
