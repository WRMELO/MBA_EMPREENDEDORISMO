# Coal_Comminution_Characterization_for_In

**Fonte**: Coal_Comminution_Characterization_for_In.pdf  
**Data de conversão**: 2025-07-30 15:07:13  
**Origem**: base_relevantes

---

Coal Comminution Characterization for Industrial Scale
Circulating Fluidized Bed
a Research Program in the frame of
the International Energy Agency implementing agreement
for co-operation in the field of fluidized bed conversion
of fuels applied to clean energy production
FINAL JOINT REPORT
Corrected version 30/01/02
Synthesis written by :
Arnaud Boëlle
Authors:
Arnaud Boëlle, Min Qian, Philippe Jaud,
Riccardo Chirone, Piero Salatino,
Franz Winter, Xin Liu,
Daniel Olsson, Lars-Erik Amand, Bö Leckner
Associated Authors :
Somchuer Brunello,
Yongjie Na,
Guangxi Yue

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 2
Circulating Fluidized Bed »
Contact List
Arnaud Boëlle, Min Qian, Philippe Jaud
EDF R&D, 6 quai Watier, 78400 Chatou, France
philippe.jaud@edf.fr
Riccardo Chirone
Istituto di Ricerche sulla Combustione, CNR, Piazzale V. Tecchio, 80, 80125 Napoli, Italy
chirone@irc.na.cnr.it
Piero Salatino
Dipartimento di Ingegneria Chimica, Università di Napoli Federico II, Piazzale V. Tecchio, 80,
80125 Napoli, Italy
piero@irc.na.cnr.it
Franz Winter, Xin Liu
Institute for Chemical Engineering, Fuel and Environmental Technology, University of
Technology Vienna, Getreidemarkt 9/159, 1060 Vienna, Austria
fwinter@fbch.tuwien.ac.at
Daniel Olsson, Lars-Erik Amand, Bö Leckner
Department of Energy Conversion, Chalmers University of Technology, SE-41296 Göteborg,
Sweden
energy.conversion@entek.chalmers.se
Somchuer Brunello
CERCHAR, rue Aimé Dubost, 62670 Mazingarbe, France
cerchar.mazin@wanadoo.fr
Yongjie Na
Institute of Engineering Thermophysics, Chinese Academy of Sciences, Beijing, China
nayj@public.east.cn.net
Guangxi Yue
Tsinghua University, Beijing, China
ygx-dte@mail.tsinghua.edu.cn
Acronym used in this report
EDF = Electricité de France
IRC-CNR = Istituto di Ricerche sulla Combustione, CNR
TU-VIENNA = Institute for Chemical Engineering, Fuel and Environmental Technology,
University of Technology Vienna
CHALMERS = Department of Energy Conversion, Chalmers University of Technology
IET = Institute of Engineering Thermophysics, Chinese Academy of Sciences
TSINGHUA = Tsinghua University
CUMT = China University of Mining & Technology

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 3
Circulating Fluidized Bed »
EXECUTIVE SUMMARY
The management of the bed solids inventory and particle size distribution in fluidized bed combustors
has long been recognized as a key factor for the efficient and trouble-free operation of industrial scale
fluidized bed combustors. From a coal particle to an ash particle getting out the circulating loop, the
particle size reduction factor can be hundred. Detailed pilot scale test observations related to the size
of circulating particles and ash particles, show very different behaviours for different coals. In order
to describe those behaviours related to a large particle size spectrum, a general frame work is
proposed based on several concepts. The key concept is represented by the Primary Ash Particle Size
Distribution (PAPSD). According to this concept, Primary Ash Particles are liberated from the carbon
matrix under the combined action of Combustion and Primary Attrition of the mother fuel particles.
By Primary Attrition it is meant here a complex of particle comminution phenomena closely
associated with the progress of reactions (devolatilization/char combustion), along pathways and with
mechanisms that are extensively discussed by Chirone et al. (1991). Further (Secondary) attrition of
ash particles can occur after char combustion is complete and is not associated with the parallel
progress of chemical reactions but to mechanical attrition only.
Those concepts are associated with coal characterization procedures in order to have information on
the size reduction of a coal particle and the final size distribution of ash. The measurement obtained
on a lab scale is validated by the analysis of some results of industrial-scale tests. In association with
procedure definition, a qualitative approach allows prediction and inter-coal comparison. A
modelisation work is also presented considering however that quantitative predictions of the particle
size distribution inside a CFBC is still a far objective.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 4
Circulating Fluidized Bed »
TABLE OF CONTENTS
1. INTRODUCTION........................................................................................................................................5
1.1 IMPORTANCE OF PARTICLE SIZE DISTRIBUTION..............................................................................................5
1.2 AIM OF THE RESEARCH PROGRAM..................................................................................................................6
1.3 LIST OF TESTED COAL....................................................................................................................................6
2. EXPERIMENTAL OBSERVATIONS ON CFBC PILOTS.....................................................................8
2.1 OVERVIEW OF PILOT TESTS............................................................................................................................8
2.2 SOLID CONCENTRATION.................................................................................................................................9
2.3 TEMPERATURE PROFILE...............................................................................................................................10
2.4 COMBUSTION STABILITY..............................................................................................................................11
2.5 FLY ASH RATIO............................................................................................................................................12
2.6 UNBURNT CARBON......................................................................................................................................12
3. CONCEPTS................................................................................................................................................13
3.1 PRIMARY FRAGMENTATION.........................................................................................................................13
3.2 CARBON ATTRITION....................................................................................................................................15
3.3 ASH FORMATION..........................................................................................................................................17
3.4 PRIMARY ASH.............................................................................................................................................20
3.5 SECONDARY ATTRITION..............................................................................................................................22
4. METHODOLOGICAL RESULTS : EXPERIMENTAL PROCEDURE.............................................23
4.1 PRIMARY FRAGMENTATION CHARACTERIZATION........................................................................................23
4.2 CHAR ATTRITION CHARACTERIZATION........................................................................................................23
4.3 PRIMARY ASH CHARACTERIZATION.............................................................................................................24
4.4 ASH ATTRITION CHARACTERIZATION...........................................................................................................26
5. QUALITATIVE RESULTS : A COAL COMMINUTION CLASSIFICATION SYSTEM................28
5.1 PAPSD PROCEDURE COMPARISON..............................................................................................................28
5.2 PAPSD COAL COMPARISON.........................................................................................................................29
5.3 PAPSD AND SECONDARY ATTRITION..........................................................................................................30
5.4 A PAPSD BASED COAL COMMINUTION CLASSIFICATION SYSTEM..............................................................32
6. TOWARDS QUANTITATIVE PREDICTIONS : MODELISATION PROCEDURE........................34
6.1 MODELISATION OF THE CIRCULATING LOOP.................................................................................................34
6.2 CARBON COMMINUTION..............................................................................................................................35
6.3 INERT COMMINUTION..................................................................................................................................36
6.4 SIMULATION RESULTS..................................................................................................................................37
6.5 MODELISATION CONCLUSION.......................................................................................................................41
7. CONCLUSION...........................................................................................................................................42
8. REFERENCES...........................................................................................................................................43

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 5
Circulating Fluidized Bed »
1. Introduction
1.1 Importance of particle size distribution
The management of the bed solids inventory and particle size distribution in fluidized bed combustors
has long been recognised as a key factor for the efficient and trouble-free operation of industrial scale
fluidized bed combustors. Merrick and Highley (1974) pioneered studies on the subject. They
highlighted that attrition phenomena, together with elutriation and fines recycle, play a key role in
establishing ash loading and particle size distribution at steady state in the combustor. Their work was
based on operating experience with a pilot scale bubbling fluidized bed combustor. Attrition of coals
during fluidized bed combustion received since then deeper consideration by several research groups.
The state-of-the-art on this subject and the analysis of the combined attrition-combustion pathways
determining the fate of carbon until burn-off have been surveyed by Chirone et al. (1991).
Even stronger is the impact of the management of bed solids on the overall performance of circulating
fluidized bed combustors. For any given solids hold up in the riser (which largely dictates the overall
pressure drop across the riser), the particle size distribution of bed material influences the axial
pressure profile, the solids concentration profile along the riser and, in turn, the bed-to-surface heat
transfer coefficients along the riser (Wu et al., 1991; Leckner and Andersson, 1992; Wirth, 1995;
Basu and Nag, 1996). Furthermore, the extent of axial solids mixing and, in turn, the degree of
temperature uniformity along the riser are affected accordingly.
The ash management facilities can also be affected by fuel characteristics. The size distribution of the
bed particles can be controlled to some extent by design measures, as have been clearly explained by
Herbertz et al. (1989): the small particle side of the size spectrum is determined by the fractional
efficiency of the gas-particle separator, whereas the coarse particle side of the spectrum is represented
by particles found in the bottom bed, which has to be adjusted by bed drainage. Various types of bed
material regeneration devices have been invented to remove the coarse inert particles and send the
fine fractions back to the bed at the same time as the loss of unburned particles is minimized. The
effective design of the cyclone is critically dependent on the ability to predict the particle size
distribution of bed inert material (Muschelknautz and Muschelknautz, 1999; Bursi et al., 1999).
The control of particle size distribution by design measures (gas-particle separator and bed material
regenerator) has to be complemented by information relative to the fuel. More knowledge on the
performance of the particles after feeding into the combustor is needed : fragmentation and attrition of

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 6
Circulating Fluidized Bed »
particles, and also the fuel dispersion. Such information should be gained under actual boiler
operation conditions to complete experiences made in the laboratory and to form a basis for the
validation of prediction models.
1.2 Aim of the research program
The present study deals with the assessment of the inventory and of the particle size distribution of
solids establishing at steady state in a circulating fluidized bed combustor under the hypothesis that
the bed consists of fuel ash only. The aim of this research program is to define a coal characterization
procedure for combustion in industrial scale CFB in order to have information on the size reduction of
a coal particle (comminution) and the final size distribution of circulating ash. The procedure is based
on existing procedures developed a few years ago by co-workers of this program. The validation is
done with the analysis of some results of industrial-scale tests. Associated with the procedure
definition, a test storage policy allow qualitative prediction and an inter-coal comparison.
1.3 List of tested coal
Several coals of different rank and from different countries have been tested in this research program :
• Datong = Chinese bituminous coal
• Dayan = Chinese lignite
• Gardanne = French lignite with a high ash content
• Pingzhuang = Chinese low bituminous coal
• Polish = bituminous
• South-African = bituminous
• Wangpingcun mix = mixture of gangue and Chinese anthracite
• Xiazhuang = Chinese anthracite
Their analysis are detailed in the following table. For some coals, two sets of experiments have been
done.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 7
Circulating Fluidized Bed »
Proximate Analysis U ltimate Analysis
Coal name (air-dried basis) (air-dried basis)
erutsioM
hsA
elitaloV
nobraC
xiF
)gk/JM(
VHH
C H O S N
Datong 1 2,5 12,7 27,4 57,5 28,9 71,5 4,1 7,4 1,1 0,8
Datong 2 4,5 15,1 24,6 55,7 27,1 67,1 3,7 7,7 1,2 0,7
Dayan 20,0 11,8 31,3 36,9 19,6 51,5 3,5 11,8 0,3 1,0
Gardanne 5,8 25,0 41,3 27,9 18,5 49,6 3,4 12,5 4,3 1,4
Pingzhuang 7,4 28,6 21,3 42,7 19,1 52,6 2,5 6,7 1,6 0,6
Polish 1 2,3 17,0 29,2 51,5
Polish 2 1,7 12,3 27,5 58,5 73,9 4,6 5,3 0,8 1,5
South African 2 7,3 14,6 22,6 55,5
Wangpingcun Mix 1,3 52,6 5,1 41,0 14,0 43,1 0,7 2,1 0,1 0,1
Xiazhuang 1,4 29,3 9,0 60,4 24,4 61,2 2,7 0,9 3,6 1,0
Those coals have been tested in a lab scale apparatus and in a pilot scale CFBC according to the
following list :
Coal name Lab scale test Pilot scale test
Datong 1 TSINGHUA, IRC-CNR, TU-VIENNA IET
Datong 2 TSINGHUA IET
Dayan TSINGHUA IET
Gardanne TSINGHUA CERCHAR
Pingzhuang TSINGHUA IET
Polish 1 IRC-CNR, TU-VIENNA CHALMERS
Polish 2 IRC-CNR, TU-VIENNA CHALMERS
South-African 2 IRC-CNR,TU-VIENNA CERCHAR
Wangpingcun mix TSINGHUA IET
Xiazhuang TSINGHUA, IRC-CNR, TU-VIENNA IET

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 8
Circulating Fluidized Bed »
2. Experimental observations on CFBC pilots
The analysis of coal comminution starts with experimental observations in industrial and pilot CFBC.
After a rapid overview of the tests conditions, major test observations are reported.
2.1 Overview of pilot tests
In this research program, three CFBC pilots have been involved in coal combustion tests :
1. IET 1.5 MWth
2. CHALMERS 12 MWth
3. CERCHAR 1 MWth
Experimental observations on particle size inventory require specific information on pilot equipment,
pilot measurements and test conditions. For a complete particle size analysis, the following
elements should been gathered :
1. Startup material : particle size distribution and mass
2. Coal : particle size distribution and mass flow rate
3. Limestone : particle size distribution and mass flow rate
4. Combustion chamber pressure drop
5. Bottom bed particle : particle size distribution
6. Riser particle analysis : particle size distribution
7. Circulating particle analysis (under cyclone) : particle size distribution
8. Fly ash : particle size distribution and mass flow rate
9. Bottom ash : particle size distribution and mass flow rate
Furnace particle sampling requires a sampling probe adapted to hot conditions. The sampling process
needs to be qualified to set the suction velocity, the probe head, etc. The duration of the combustion
test should be long enough to reach a solid equilibrium and to get a negligible influence of the start-up
material. The furnace hydrodynamic should be as simple as possible. For coals with a low ash content,
or with a high sulphur content, the mass of lime compared to the mass of ash present in the bed could
be high, which implies to analyse the limestone comminution at the same time as coal comminution. If
possible, a combustion test without any limestone would simplify greatly the analysis. Some of those
constraints are difficult to obtain especially in large pilots. Ash flow rate is difficult to measure.
That’s why several of the pilot tests done in the frame of this research program could not lead to a
complete particle size analysis. Most of the following observations are done on the IET pilot which

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 9
Circulating Fluidized Bed »
appears to be the most convenient pilot to do such tests.
2.2 Solid concentration
2.2.1 Solid concentration in bottom bed
The solid concentration could be derived from the pressure drop measurement. In Figure 1, the solid
concentration is reported for the combustion of five different coals ; the particle density is assumed to
be 2500 kg/m3. The smallest average ash concentration in the bottom part of the furnace is only 0.005,
which does not mean a dense bed at all, while the largest is over 0.2.
0,25
solid concentration
0,2 in the bottom bed
0,15
0,1
0,05
0
Dayan Pingzhuang Xiazhuang Datong Wangpingcun
Figure 1 : solid concentration in bottom bed for 5 coals (IET).
2.2.2 Solid concentration in the riser
The differences in the average ash concentrations in the upper part of the furnace among the tested
coals are very large. The smallest one is almost 8 times smaller than the largest one. The heat transfer
which depends on particle concentration is consequently largely affected. It can be observed that the
order of the five tested coals is almost the same as that of ash contents of the coals.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 10
Circulating Fluidized Bed »
0,008
0,007 solid concentration
in upper furnace
0,006
0,005
0,004
0,003
0,002
0,001
0
Dayan Datong Xiazhuang Pingzhuang Wangpingcun
Figure 2 : solid concentration in the upper furnace for 5 coals (IET).
2.2.3 Pressure drop ratio
Combining the two previous observations, it is convenient to define the pressure drop ratio as the
pressure drop in the upper furnace divided by the total pressure drop. For the experimental conditions,
the maximum of this ratio (homogeneous vertical distribution of solid) is 89 % which is nearly
reached by the Dayan coal.
80
70 pressure drop ratio
60
50
40
30
20
10
0
Datong Wangpingcun Xiazhuang Pingzhuang Dayan
Figure 3 : pressure drop ratio for 5 coals (IET).
2.3 Temperature profile
There are distinct differences among the temperature profiles of the tested coals. Temperature profiles
depend on not only combustion but also the ash concentrations and the ash sizes in the furnace.
Temperature profiles are more uneven in the lower part of the furnace since it is a part from a dense
bed where the secondary air is injected. The uniformity of the temperature profiles is in the order of

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 11
Circulating Fluidized Bed »
Pingzhuang coal, Dayan coal, Xiazhuang coal, Wangpingcun Mix coal and Datong coal.
(°C) Xiazhuang
Pingzhuang
900
Wangpingcun
Dayan
880 Datong
860
840
820
800
0 2 4 6 8 (m)
Figure 4 : vertical temperature profile for 5 coals (IET).
The temperature profile of Datong 900 ° and Datong 850 ° have the same shape which means that
the combustion processes at the two temperatures have the same characteristics.
(°C)
900 Datong 900 °C
Datong 850 °C
880
860
840
820
800
0 2 4 6 8 (m)
Figure 5 : the shape of the temperature profile is not influenced by the temperature (IET).
2.4 Combustion stability
Due to small thermal capacity of a pilot plant it is easy to see large differences of combustion stability
among the tested coals. Combustion stability is influenced by coalification and volatile contents of the
coal but also by ash concentration in the bottom of the furnace. The combustion stability order from
stable to unstable is basically opposite to the order of the average ash concentrations in the bottom
part of the furnace from large to small.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 12
Circulating Fluidized Bed »
2.5 Fly ash ratio
The fly ash ratio is defined as the flow rate of fly ash divided by the total ashes flow rate. There are
large differences of the ratio of fly ash to bottom ash among the tested coals.
100
90 fly ash ratio
80
70
60
50
40
30
20
10
0
Wang Xiazhuang Ping Datong Dayan Gardanne South
pingcun zhuang African
Figure 6 : fly ash ratio for several coals : IET (dark) CERCHAR (white)
2.6 Unburnt carbon
The differences of the carbon contents of fly ash among the tested coals are very large. Except Datong
coal, carbon content in fly ash is larger as the coalification of the coal is deeper and H, O, volatile and
inner moisture contents are smaller. Carbon content in fly ash of Datong coal is extremely large, so
that the above analysis is not applicable to Datong coal. It is necessary to search the relationship
between the characteristic of a coal and its combustion efficiency.
16
14 Combustion loss due to fly ash (%)
12
10
8
6
4
2
0
Dayan Pingzhuang Datong Xiazhuang Wangpingcun
Figure 7 : combustion loss due to fly ash (IET).

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 13
Circulating Fluidized Bed »
3. Concepts
The initial coal particle size entering a CFBC is approximately 5 mm. The particles coming out the
circulating loop could be a hundred times smaller. In the mean time, the particles could circulate in
the fluidized loop for a very long time. More than 90 % of those particles are inert. To describe and
predict the comminution phenomena, a general framework built from several concepts is proposed
hereunder.
1. Primary fragmentation
2. Carbon attrition
3. Primary ash
4. Inert attrition
3.1 Primary Fragmentation
The propensity of coals to break up upon injection into the bed is a consequence of internal stresses
due to devolatilization and thermal shock. On the one hand the degree of fragmentation is strongly
affected by the coal type and the coal particle size. On the other hand it is not affected by the
oxidizing/inert nature of the fluidizing gas. Also the fluidizing gas velocity plays a minor part. Even if
the emission of volatile is a necessary condition for the particle to fragment, the porosity of the
material, the strength of the coal and its char control the extent of particle fracture. The feature of
swelling coals to undergo a plastic stage during heat up is not able to relieve internal thermal stress or
internal overpressure as a consequence of possibility of the failure of the external resolidified layer.
However the shape of fragments, in particular the formation of spherical shaped fragments, is strongly
influenced by coal plasticity.
The average size of particles present in the bed at the devolatilization stage is rather similar for the
coals due to the compensating effects of a higher fragmentation probability and a smaller particle
multiplication factor.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 14
Circulating Fluidized Bed »
Nout/Nin
South African
50
Polish
Datong
40
Xiazhuang
30
20
10
Nout/Nin=1
0
0 2 4 6 8 10 12
do,mm
Figure 8 :Primary fragmentation. Particles multiplication factor vs initial particle size (IRC-CNR).
1
Sf
0.8
0.6
South African
0.4
Polish
Datong
0.2
Xiazhuang
0
0 2 4 6 8 10 12
do,mm
Figure 9 : Primary fragmentation. Fragmentation probability vs initial particle size (IRC-CNR).

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 15
Circulating Fluidized Bed »
10
8
6
4
2
0
0 2 4 6 8 10
do,mm
mm,mfd
South African
no fragmentation
Polish
Datong
Xiazhuang
Figure 10 - Primary fragmentation. Average size of particles present in the bed after devolatilization
stage vs initial particle size (IRC-CNR).
3.2 Carbon Attrition
When the carbon attrition rate is expressed per unit char particles external surface, a monotonically
increasing trend is observed : a very rapid increase to the specific attrition rate is observed at the
beginning ; a plateau is reached at intermediate carbon conversion degrees ; a final tail characterised
by further increase of specific attrition rate is observed at late burn-off. This phenomenology led to
the formulation of the Combustion-Assisted concept. According to this concept, attrition rate is
dramatically enhanced by the progress of combustion. Internal burning enlarges pores, regenerates
surface irregularities and, in turn, decreases the mechanical strength of the outer region of the particle,
making it increasingly prone to failure upon surface wear. One consequence of the Combustion-
Assisted Attrition mechanism is that the attrition constant k is a function of the oxidising conditions.
W
The validity of the equation E =k(U - U ) c relating the carbon elutriation rate to bed carbon
C mf
d
loading, has been proven with reference to a number of coals under bubbling fluidized bed
combustion conditions. The dependency of k on the size of bed inert material has been assessed. The
robustness of the experimental procedure for evaluation of the fuel-specific parameter k with respect

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 16
Circulating Fluidized Bed »
to the scale of the experimental apparatus has been positively checked. The same equation has been
proven to apply to circulating fluidized bed combustion of a subbituminous coal char. The attrition
rate constant k turned out to be dependent on the solids mass flux along the riser G.
s
The properties described here are illustrated by the following two figures where carbon attrition
curves are reported for the Polish and the South African coal under different oxidising conditions. The
curves have the same general trend. However some differences are : i) combustion efficiency is more
sensitive to oxygen concentration in the case of the South African coal ; ii) less regular curves have
been obtained in the case of Polish coal.
0.005
POLISH COAL
Char Particles = 4760 - 635m0m m
Silica Sand: 300 - 400m m m
0.004 Bed Temperature = 850°C
Ug = 0.4 m/s
O = 0.0%
2
0.003
1.5% Combustion efficiency 97.26%
4.5% Combustion efficiency 98.11%
Ec, g/min
0.002
0.001
0.000
0 20 40 60 80 100 120 140 160
time, min
Figure 11 : characteristic attrition curves for the Polish coal (IRC-CNR)

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 17
Circulating Fluidized Bed »
0.010
SOUTH AFRICAN COAL
Char Particles = 4760 - 635m0m m
Silica Sand: 300 - 400m m m
0.008 Bed Temperature = 850°C
Ug = 0.8 m/s
O = 1.5% Combustion Efficiency 94.16%
2
0.006
4.5% Combustion Efficiency 96.34%
0.004
Ec, g/min
0.002
0.000
0 20 40 60 80 100 120 140 160
time, min
Figure 12 : characteristic attrition curves for the South African coal (IRC-CNR).
3.3 Ash formation
The comparison between the inert content of a coal particle and the ash obtained after combustion of
that coal in a CFBC pilot brings some understanding on the ash formation mechanisms. The study
presented here includes the qualitative and quantitative analysis of main mineral matters under both
the reflected light and the transmitted light, using polarising light microscope and the X-ray
diffraction analysis. The following description is based on the analysis of five Chinese coals of
different rank before and after combustion.
In analysed coal particles, the minerals observed are mainly clay minerals, pyrite, quartz, carbonate
minerals, rutile. The occurrence of clay minerals with various size fractions are quite different. Those
less than 60 µm in size are predominately disseminated in organic matrix, the minerals with the size
range 60-100 µm normally filled the cell cavity or occurred as small nodules, minerals ranging from
100-300 µm occurred as large nodules or lenticules and the minerals more than 300 µm occurred as
large nodules long-bar shape or large irregular lumps. Pyrites are only observed in the small range
(typically 0-250 µm). The pyrites less than 60 µm in size are predominately distributed in clay
minerals while in the size range 50-100 µm and 90-250 µm, they occur as small and irregular lumps.
Quartz occurs in the form of excluded particles, normally less than 250 µm in size.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 18
Circulating Fluidized Bed »
Figure 13 : coal minerals : clay, reflected light, single polar (x160) (CUMT)
Obvious changes can be observed between the occurrence of the minerals in coal and the mineral
matter in ash after coal combustion, they can be described with the following aspects : after
combustion, the original minerals in coal did not occurred as single particles, but coalesced together.
In addition, rapid cooling normally caused the formation of glassy materials, and most particles are
composed of less amount of crystals and large amount of glassy materials, so the analysis of the
mineral of the ash samples was carried out by identification of the different particles. In this
experiment, under the transmitted light of polarising microscope, five kinds of particles were
recognised, namely clayey particles, quartz, mineral aggregate, ferruginous particles and unburnt
carbon. Mineral aggregate, glassy material and ferruginous particle are typically new materials.
After combustion, the original clay disseminated in coal matrix or filled in cell cavity has changed,
most of clayey particles occurred as irregular lumps, only a little of them was encapsulated into the
unburnt carbon. The percentage of mineral particles is not evenly distributed in each size fraction. The
number of the clayey particles and mineral aggregates in coarser fractions is more than that in finer
size fraction. The mineral aggregates are new material obtained after combustion. They are composed
by a great number of small particles such as quartz or clayey materials, maybe originated from the
coalescence of the disseminated minerals in coal during combustion. Quartz occurred as irregular

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 19
Circulating Fluidized Bed »
single particles. Due to clay minerals decomposition, the percentage of quartz particles in ash is more
than that of quartz particles in coal at the same size fraction. Ferruginous particles are an iron oxide
formed with pyrite lost sulfur after coal combustion. They enriched in finer fractions, normally less
than 120 µm occurred as small excluded round particles or distributed in clayey particles.
Figure 14 : Ash particles. left : unburnt carbon and quartz, right : mineral aggregate,
transmitted plainlight (x100) (CUMT)
Figure 15 : clayey particle transmitted plainlight (x100) (CUMT)

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 20
Circulating Fluidized Bed »
3.4 Primary Ash
The key concept in the proposed approach is represented by the Primary Ash Particle Size
Distribution (PAPSD). According to this concept, Primary Ash Particles are liberated from the carbon
matrix under the combined action of Combustion and of Primary Attrition of the mother fuel particles.
Primary Attrition means here a complex of particle comminution phenomena closely associated with
the progress of reactions (devolatilization/char combustion), along pathways and with mechanisms
that are extensively discussed by Chirone et al. (1991). The concept of Primary Ash can be defined as
ash obtained after complete combustion of coal particles and after a sufficient mechanical stress to get
ashes as individual particles. Primary ash is therefore a characteristic image of the inert content of
coal.
PAPSD of SOUTH AFRICAN coal
)I
retlif(
05
<
)II
retlif(
05
-
051
051
- 052
052
- 004
004
- 006
006
- 058
058
- 0811
0811
- 0071
0071
- 0632
0632
- 0533
0533
- 0674
0674
- 0536
0536
>
0.0040
0.0035
0.0030
0.0025
m(m m)^-1 0.0020
0.0015
0.0010
0.0005
0.0000
size m(m m)

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 21
Circulating Fluidized Bed »
PAPSD of POLISH coal
)I
retlif(
05
<
)II
retlif(
05
-
051
051
- 052
052
- 004
004
- 006
006
- 058
058
- 0811
0811
- 0071
0071
- 0632
0632
- 0533
0533
- 0674
0674
- 0536
0536
>
0.0009
0.0008
0.0007
0.0006
0.0005
m(m m)^-1
0.0004
0.0003
0.0002
0.0001
0.0000
size m(m m)
Figure 16: PAPSD of the Polish and South African (IRC-CNR)

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 22
Circulating Fluidized Bed »
3.5 Secondary Attrition
Secondary attrition of ash particles can occur after char combustion is completed and is not associated
to the parallel progress of chemical reactions but to mechanical attrition only.
0.55
0.50
0.45
0.40
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0.00
-0.05
0 61 90 125 180 200 225 275 300 325 350 500
noitcarf
ssaM
Sieving 10 min
Sieving 110 min
Size cut (micron)
Figure 17: Xiazhuang ash particle size distribution at different times (size cut: 0-450micron, sieving
amplitude: 3.0mm) - ( TSINGHUA).
An obvious mass shift, which is from large size component to small one, occurs with the time pass-by.
The previous text described the attrition phenomenon, showing that attrition resulted in a relatively
large mother particle and a group of fine particles. And for Xiazhuang coal sample, the change of the
mass fraction of mid size cuts (180-300 microns) could almost be ignored.
Moreover an important conclusion can be deduced from these figures. It can be observed that the
mass amount of mid size cut did not increase. Contrarily the middle size cut also contributes to the
generating of fines. This strongly supports the abrasive mechanism hypothesis of the attrition process
in a fluidized bed.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 23
Circulating Fluidized Bed »
4. Methodological results : experimental procedure
4.1 Primary Fragmentation Characterization
The characterization of raw fuels fragmentation upon fast heating up and devolatilization that follow
particle injection into the hot fluidized bed are based on devolatilization experiments in a bench-scale
basket-equipped fluidized bed reactor (40 mm I.D.) (Chirone and Massimilla, 1989). The reactor are
operated batchwise with respect to the fuel charge using nitrogen as fluidizing gas.
The primary fragmentation of each coal is studied by iterating several times (30 or more in order to
get statistically significant experimental results) the following sequence:
1. The wire mesh basket is immersed into the bed, resting on the gas distributor, before fuel
feeding;
2. One coal particle is fed to the combustor;
3. About three minutes after coal particle injection, the basket is raised about 40 cm above the bed
surface (that is in the relatively cold freeboard section). The devolatilized particles (mother
particle + fragments) are cooled down by injecting nitrogen to prevent combustion as particles
are exposed to ambient air.
4. Particles are extracted from the reactor by means of the basket. The number of residual
particles and their size are quantitatively characterized. The shape of fragments is qualitatively
classified.
Experiments are carried out under inert conditions, i.e. by fluidizing the bed with nitrogen, at a gas
velocity of 0.8 m/s. Coal particles belonging to the size ranges 9.5-6.35, 6.35-4.76 and 4.76-3.35 mm
have been tested. Silica sand in the size range 0.3-0.425mm (true density: 2560 kg/m3; minimum
fluidization velocity: 0.045 m/s @850°C) was used as inert bed material.
Experimental data have been worked out to calculate the primary fragmentation parameters : the
particle multiplication factor ; the probability that a particle would undergo fragmentation ; the mean
size of particles (unfragmented particles plus fragments) found in the bed after devolatilization.
4.2 Char Attrition characterization
Char attrition is characterized by feeding batches of pre-devolatilized char particles into a 40 mm ID
fluidized bed equipped with a special two-exit head to collect particulate in the flue-gas (Chirone et
al. 1985). Attrition is characterized in batchwise experiments by measuring the time-resolved carbon

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 24
Circulating Fluidized Bed »
elutriation rates. These are monitored by operation of the two-exit head, i.e. by connecting
alternatively the two exits. Using several filters in sequence, carbon emission within the combustion
time after char is charged into the bed, is obtained. To keep oxidizing conditions substantially uniform
during the combustion time batches of about 2g of fixed carbon are used in each run. Operative
conditions at which experiments are carried out are listed in the following table :
Operative variables of the combustor
Bed Temperature, °C 850
Fluidizing Velocity, cm/s 40, 80, 120
%O2 in Inlet Gas 0, 1.5, 4.5
Size distribution of the batches of char tested
Particle size, mm 6.35 - 4.76
Table 1 : experimental conditions for attrition characterisation.
4.3 Primary Ash characterization
4.3.1 Primary Ash characterisation in oven
An electrically heated oven and a cold sieving shaker are used to carry out the experiment. The
procedure uses 50 g of coal particles with a size range 2-2.5 mm. The coal is burnt at 850°C in an
oven in the absence of any external mechanical forces which might affect the formation of ash. The
shape of the ash particles obtained is similar to the original coal particles if they are kept untouched.
However, if any mechanical forces are active, these loose ash agglomerates were destroyed. Parts of
fine ash particles are found on the surfaces of larger ash particles.
The ashes produced in oven are put in the sieving machine for attrition tests. The sieving done at
certain sieving conditions only destroyed the loose ash agglomerates and separated the ash particles
from each other. A complete separation by sieving is not possible. Fine ash particles usually stick on
larger ones. However, the amount of mass might be low and the PSD obtained is still representative
for the coal. The sieving time is 30 minutes.
This procedure has been developed and applied by TSINGHUA and TU-VIENNA and is referred
hereafter respectively as PAPSD 1 and PAPSD 3.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 25
Circulating Fluidized Bed »
Mass fraction Mass fraction
0.55
0.30
0.50 min10
min5 min20
0.45 min10 0.25 min30
0.40 min15 min40
min20 min80
0.35 min25 0.20
0.30 min30
min40 0.15
0.25
0.20
0.10
0.15
0.10 0.05
0.05
0.00 0.00
0 20 61 90 125 160 280 450 0 20 61 90 125 160 280 450 600 1000 2000 3200 --
Size cut (micron) Size cut (micron)
Figure 18 : Gardanne coal, Size cut:0-450 microns. Sieving amplitude:1.5mm / Gardanne, Size
cut:2000-3200 microns. Sieving amplitude:1.5mm (TSINGHUA)
4.3.2 Primary Ash characterisation in a bubbling bed
A procedure for the experimental determination of the PAPSD in a bubbling bed is described
hereunder :
Apparatus: The apparatus consists of a 40 mm ID stainless steel combustor, 1 m high, electrically
heated. The lower section of the combustor is filled with ceramic rings and acts as gas preheater. The
gas distributor consists of a perforated plate with 55 holes of 0.5 mm diameter in a triangular pitch.
The combustor is equipped with sintered brass filters at the exhaust for collection of elutriated
particles. Monitoring of gas composition at the exhaust is accomplished by on line CO, CO and O
2 2
analyzers. Prior to the test, a cylindrical wire mesh basket (40 mm outer diameter, 400 m m mesh size)
is located just above the gas distributor. Then the combustor is charged with about 150 g of silica sand
in the size range 125-150 m m.
Procedure: The procedure consists of the following sequence of steps:
1. Devolatilization (in nitrogen) followed by combustion (in air) of a coal sample (about 3g) until
complete burnout. Gas superficial velocity is kept at the value U slightly larger than the
1
incipient fluidization velocity of the bed. Combustion is carried out at 850°C. Collection at the
exhaust and further characterization of fly-ashes is performed after this stage.
2. Elutriation of ashes from the bed at gas superficial velocity U larger that U but smaller than
2 1
the terminal velocity of bed inert material. Collection and further characterization of elutriated
material is performed after this stage.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 26
Circulating Fluidized Bed »
3. Extraction of coarser (d>400m m) bed ash by means of the wire mesh basket followed by
discharge of the remaining bed material (sand+ash). Separation of ash material from the sand
by sieving and its further characterization is performed after this stage.
In order to collect significative quantities of ash samples, steps 1-3 are iterated several times (typically
six), and both elutriated fines and material withdrawn from the bed cumulatively subjected to further
characterization.
The operating procedure is optimized considering the following requirements:
a) Limited surface wear is beneficial to overcome weak particle-to-particle forces (typically van
der Waals forces) that keep together fragments otherwise disconnected.
b) Surface wear must not be exceedingly large to give rise to extensive secondary attrition of ash
particles.
c) Combustion time must be small in order to minimize the occurrence of secondary attrition of
ash particles during burn off.
d) The coal/char particle temperature must not be high to the point of giving rise to ash sintering.
A trade off between conflicting needs a) and b) has been established by operating at moderate gas
superficial velocity during Step 1 (U =0.06 m/s) using relatively fine bed material (silica sand with
1
particle diameter in the size range 125-150 m m). At the same time U was selected in orders to
1
elutriate carbon fines smaller than the typical cyclone cut-off size in CFBC, thus removing fine
particles that would be rapidly lost in a real combustor. During Step 2 the combustor acts like an
elutriator, with the aim of collecting at the exhaust ash particles (not elutriated during Step 1) whose
sizes fall within the size interval of the bed inert material. At the same time, inert bed material must
not be elutriated to a significant extent (accordingly U was set at the value 0.2 m/s).
2
Constraints c) (which would call for severely oxidizing conditions) and d) (that would rather call for
mild oxidation) have been reconciled by operating in air at 850°C under conditions that apparently did
not bring about ash sintering.
This procedure has been developed and applied by IRC-CNR and is referred hereafter as PAPSD 5.
4.4 Ash attrition characterization
The procedure for the hot attrition test consists of oven combustion and CFBC tests.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 27
Circulating Fluidized Bed »
1. Coal particles are put into an oven to produce the ashes under the following operating
conditions : 100 g of coal is used for particles in the size range 2-2.5 mm, the oven temperature
is 850°C, the duration of the test is 5 hours in steady-state operation.
2. When the ash is cooled down, it is put on the sieving machine for 30 minutes to obtain primary
ash particle size distribution (PAPSD).
3. After the sieving the ash is fed into the CFBC under the following operating conditions : the
bed temperature is 850°C, isothermal along the riser ; the fluidizing gas is air with a superficial
velocity of 3 m/s ; the bed material is 200 g of silicon carbide particles in the size range 250-
280µm ; the operation time is 60 min.
4. After 60 min operation, the gas supply is switched off and simultaneously, the heating shells
are switched off. When the temperature of the CFBC falls down to the room temperature, all
bed material : the ash and the silicon carbide are collected from the CFBC to measure final ash
particle size distribution. Because the silicon carbide is a very hard and stable material, no
fragments are produced from the silicon carbide after high temperature CFBC operation. After
sieving, all silicon carbide is collected between 280m m and 250m m. All information about ash
attrition is obtained, except the size range (280-250m m) which is mixed with silicon carbide.
This data is estimated by averaging the data of the size range below (250-224m m) and above
(315-280m m). In CFBC operation the finest ash could not be collected since it escapes as fly
ash, so this ash mass loss is considered to belong to the size range which is smaller than 40m m
(the smallest size of the used sieve is 40m m).
This procedure has been developed and applied by TU-VIENNA and is referred hereafter as
PAPSD 4.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 28
Circulating Fluidized Bed »
5. Qualitative results : a Coal Comminution Classification
System
For a qualitative purpose, for example inter coal comparison relative to their comminution properties,
the Primary Ash concept could give enough information. Although an additional work for the
definition of a standard procedure is clearly needed, this concept is proved to be sufficiently robust to
serve as a basis for a Coal Comminution Classification System.
5.1 PAPSD procedure comparison
For the same coal, the PAPSD measured by the different procedures are significantly different. This is
observed in figure 19 and 20 where the PAPSD of the Datong coal and Xiazhuang coal are reported.
The first important reason why the differences are so large is the quality of the coal particles
sampling. Due to the development stage of those procedures, no regular sampling methods have been
applied before measurement. In current stage the procedure uses few number of particles which
induces a larger influence on the sampling. The second reason is the difficulty to measure the particle
size distribution of fine particles (below 50 µm) with sieves. The use of two different apparatus for
small and large particles would also lead to some difficulties. Finally, the different operating
conditions of the proposed PASPD measurement procedures are also responsible for discrepancies.
There is a need for the definition of one standard procedure.
1,00
Datong
0,75 PAPSD 1
PAPSD 3
0,50 PAPSD 4
PAPSD 5
0,25
0,00
1,E-05 1,E-04 size (m) 1,E-03 1,E-02
Figure 19 : PAPSD procedure comparison for Datong coal.
PAPSD 1 & 3 : procedure using an oven (TSINGHUA & TU-VIENNA)
PAPSD 4 : procedure using a hot CFBC (TU-VIENNA)
PAPSD 5 : procedure using a bubbling bed (IRC-CNR)

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 29
Circulating Fluidized Bed »
1,000
Xiazhuang
0,750
0,500
PAPSD 1
PAPSD 2
0,250 PAPSD 3
PAPSD 4
PAPSD5
0,000
1,E-05 1,E-04 1,E-03 1,E-02
Figure 20 : PAPSD procedure comparison for Xiazhuang coal.
PAPSD 1 & 3 : procedure using an oven (TSINGHUA & TU-VIENNA)
PAPSD 2 : procedure using an oven and a cold CFBC (TSINGHUA)
PAPSD 4 : procedure using a hot CFBC (TU-VIENNA)
PAPSD 5 : procedure using a bubbling bed (IRC-CNR)
5.2 PAPSD coal comparison
For different coals, the measured PAPSD are significantly distinct which means that the inert content
of different coals have different structure. However the curve shapes are quite similar for all the coals.
In the medium size range, 0.1-1 mm, the cumulative Primary Ash size distribution is approximately
linear with Log(size) with a coefficient similar for 4 coals. The Pingzhuang coal has a special
distribution with few fines but many medium size range inert particles. The Dayan coal has a
particularly high content of inert fines : 50 % of its inert content has a size below 100 µm.
1,00
PAPSD 1
0,75
0,50
Datong 1
Xiazhuang
0,25 Pingzhuang
Wangpingcun Mix
Dayan
0,00
1,E-05 1,E-04 1,E-03 1,E-02
Figure 21 : PAPSD coal comparison for the oven procedure (TSINGHUA).

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 30
Circulating Fluidized Bed »
In spite of the discrepancies observed between the measurement of PAPSD with different procedures,
the measured PAPSD are coherent. To assess this point, a comparison is made between the PAPSD
measured by TSINGHUA (figure 21) and the one by IRC-CNR (figure 22). In those two sets of
measurements, the Datong coal and the Xiazhuang coal are the same. The relative position of the two
curves is similar for the two graphs.
The previous remarks concerning the shape of the cumulative PAPSD are also valid for those results.
The South-African coal has a special inert content with many fines.
1,00
PAPSD 5
0,75
Datong 1
Xiazhuang
0,50 Polish 1
South African
Polish 2
0,25
0,00
1,E-05 1,E-04 1,E-03 1,E-02
Figure 22 : PAPSD coal comparison for the bubbling bed procedure (IRC-CNR).
5.3 PAPSD and secondary attrition
After Primary Ash formation, the secondary attrition leads to the production of a large amount of
fines. The classification between coals is not modified. The ability of PAPSD to serve as a coal
classification scale is thus confirmed.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 31
Circulating Fluidized Bed »
1
PAPSD 3
0,75
0,5
Polish 1
Datong 1
0,25 Xiazhuang
South African
Polish 2
0
1,E-05 1,E-04 1,E-03 1,E-02
Figure 23 : PAPSD coal comparison for the oven procedure (TU-VIENNA).
1
PAPSD 4
0,75
0,5
Polish 1
Datong 1
0,25 Xiazhuang
South African
Polish 2
0
1,E-05 1,E-04 1,E-03 1,E-02
Figure 24 : PAPSD coal comparison for the hot CFBC procedure (TU-VIENNA).

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 32
Circulating Fluidized Bed »
5.4 A PAPSD based Coal Comminution Classification System
The PAPSD contains many information, some of them could be extracted to serve as a comminution
classification system.
For a one-number classification system, an example with PAPSD-200, the proportion of Primary Ash
whose size is below 200 µm, is detailed. The following table includes some information obtained on
both lab and pilot scale for different coals. The coals are ordered from the coal which gives the
coarsest Primary Ash (Polish 1) to the coal which gives the finest one (South-African 2). It can be
observed that :
1. The order given by PAPSD-200 is roughly similar to the one given by the fly ash ratio.
2. The order given by PAPSD-200 is roughly similar to the order given by the pressure drop ratio.
3. It is not possible to make a link between PAPSD-200 and the carbon in fly ash. Although the
loss of ignition from fly ash should depend on both the coal rank and the size of carbon fines,
the first parameter appears to be dominant.
4. Detailed information on the relative position of fly ash ratio and pressure drop ratio can be
obtained from PAPSD : the high pressure drop ratio for the Pinzhuang coal could be explained
by the particular curve of its PAPSD (cf. §5.2). A one number classification system could not
characterize this.
Lab Scale Pilot & Industrial Scale
eman
laoC
002-1DSPAP 002-
3DSPAP
002-5DSPAP
tinU
)%(
oitar
hsa
ylF
)%(
oitar
pord
erusserP
)%(
hsa
ylf
eht
ni
C
Polish 1 25 5 Chalmers
Gardanne 40 Provence 4 58 29 < 5
Gardanne 40 Cerchar 46
Xiazhuang 43 25 5 IET 78 42 25
Polish 2 38 5 Chalmers
Pingzhuang 42 IET 85 62 2
Datong 52 43 20 IET 96 39 23
Wangpingcun Mix 57 IET 45 39 26
Dayan 71 IET 100 78 1
South-African 2 85 40 Cerchar 91
Figure 25 : Example of a one-number comminution classification system with both lab-scale and
pilot-scale results.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 33
Circulating Fluidized Bed »
It is also possible to use a three-numbers classification system to get a more complete description of
the comminution behavior of a coal. Three different size classes (0-100 µm, 100-800 µm; 800-6000
µm) are defined according to their potential fluidization characteristics : fly ash, circulating ash, dense
bed particles respectively. Each coal revealed a certain amount of ash in those size classes.
23%
32%
41%
Polish 1 Datong 51% Polish 2
56%
12%
65%
12%
8%
5%
26%
25%
Dense bed particles
Xiazhuang South African 2 Circulating particles
Fly ash
63%
11%
70%
Figure 26 : Example of a three-number comminution classification system. Results based on
PAPSD 4 measured in a lab-scale hot CFBC at TU-VIENNA.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 34
Circulating Fluidized Bed »
6. Towards quantitative predictions : modelisation
procedure
The main goal of this modelisation work is to study the relative importance of the concepts previously
introduced. Quantitative predictions of the particle size distribution inside a CFBC is still considered
as a far objective.
6.1 Modelisation of the circulating loop
The circulating loop is considered here as one unique system to avoid to modelise the transfers
between zones controlled by complex two-phase flow hydrodynamics and to focus on particle
balance. Therefore the modelised system has one inlet which is the coal feeder and two outlets which
are the cyclone exit and the bottom bed drain. The outlets are controlled by design and operation
parameters (cyclone and bed drain efficiency) and by the internal circulation flow rate.
This simple approach has several drawbacks including to neglect the vertical segregation of particles
regarding to their size and to suppose a uniform system for the modelisation of combustion. In spite of
the evidence of extensive axial solids segregation, no established equation is available in the literature
except correlation for the transport regime (Geldart, 1981).
In CFBC, the modelisation of the internal circulation rate is a difficult task since it needs detailed
information on turbulent two-phase hydrodynamics with a large range of particle sizes. Here, a basic
model is used for the circulation flow rate of particles of size d which is supposed to be equal to the
weight W f(d) of particles of size d divided by a characteristic time of circulation t (d). Introducing the
c
cyclone efficiency h (d), the cyclone outlet can be modelized by :
c
E (d)=Wh (d)f(d)/t (d) (1)
c c c
f(d) is the particle size distribution, W is the total weight of the carbon particles. The modelisation of
the circulation time is only needed for particle which could effectively get out the circulating loop by
the cyclone.
For bed drainage, the same basic model is used, where the emphasis is this time on large particles
which are preferably collected. For those particles, the characteristic circulating time should be
interpreted as the circulation time in the dense bed.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 35
Circulating Fluidized Bed »
E (d)=Wh (d)f(d)/t (d) (2)
d d d
In this model, to study the influence of coal comminution characteristics on the particle population
balance, the bed drainage efficiency is considered as a constant and the problem is solved to get the
population balance inside the circulating loop. In real systems, the bed drain is an operation control
parameter used to adjust the internal mass of circulating particles.
6.2 Carbon comminution
Considering the previous remarks and the previous work on that subject (see Chirone 1991 for a
review), the carbon comminution equation for CFBC could be written as follows :
d(f(d)R(d)) h (d) h (d)
W = E f (d)- Wf(d) c - Wf(d) d
dd 0 0 t (d) t (d)
c d
3W dmax
- [ (cid:242) f(s )Rs( )y (d,s )sd - f(d)R(d)] (3)
d a
d
dmax
- W[ (cid:242) f(s )Rs( )sFj ( s) s(d, )d - f(d)R(d)F(d)]
d
With the boundary condition
f(d)R(d)=0 for d =d (4)
max
R(d) is defined as the comminution rate. Following the assumption of Arena et al. (1983), R(d) is
made of additive contribution of the rate of shrinkage due to attrition and combustion.
dd
R(d)= = R (d)+R (d) (5)
dt a c
The right hand terms of equation (5) are respectively feed, cyclone and bed drain outlet, comminution
gain and loss due to combustion and attrition, comminution gain and loss due to fragmentation. y (d,s )
and j (d,s ) are the distribution functions of fines and fragments produced by attrition and
fragmentation.
The attrition comminution rate is modelled by :
k
R =- a (U- U ) (6)
a mf
3
In CFBC, the fines produced by attrition may stay in the circulating loop regarding their size. Without
precise knowledge on this size, all the fines are put in the finer class modelised y (d ,d)=1 .
min

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 36
Circulating Fluidized Bed »
The combustion model uses the combustion rate per surface q given by the competition between
kinetics and diffusional mechanisms (Basu and Fraser, 1991)
q=k c [ O 2 ] g ( 1- k [ O q ] )n (7)
d 2 g
The combustion constants (k ,n) are taken from the same reference. The combustion rate is modelled
c
by :
q
R =- 2 (8)
c r
c
The fragmentation model uses the similarity hypothesis and the constants reported in Salatino (1987).
6.3 Inert comminution
The modelisation of inert behaviour during the whole combustion phase is an other difficult task since
the particles are very different from the beginning of combustion to the end. A first distinction can be
made between external or structural inert material and internal inert material. The characteristic size
of the first type is of the same order as the initial coal particle ; therefore those ashes should go out the
coal particle structure in the first stage of combustion. The second type of coal inert material could be
seen as mineral inclusions inside the coal structure. Those ashes are liberated at the same time as the
combustion occurs. But this behaviour has not been taken into account here.
The size of the liberate ashes is obviously a major parameter of coal comminution in CFBC. To
answer this question the concept of Primary Ash Particle Size Distribution (PAPSD) introduced
previously is used. The concept of Primary Ash can be defined as ash obtained after the complete
combustion of coal particles and after a sufficient mechanical stress to get ashes as individual
particles. Primary Ash is therefore a characteristic image of inert content of coal.
Considering those elements, an equation similar to equation (4) is written to describe the
comminution of inert (see also Li et al. 1997) :
d(f'(d)R'(d))
W' = E' f' (d)
dd 0 PAPSD
h (d) h (d)
- W' f'(d) c - W' f'(d) d
t c (d) t d (d) (9)
3W' dmax
- [ (cid:242) f'(s )R's( )y '(d,s )sd
d
d
- f'(d)R'(d)]

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 37
Circulating Fluidized Bed »
where W’ is the total mass of inert and f’(d) the size distribution function. R’(d) is the comminution
rate of inert particles. From Primary Ash, inert attrition is supposed to be the only effective
mechanism. The inert attrition model will be discussed later.
6.4 Simulation results
6.4.1 Base case definition
To set up the parameters of the model, a pilot test of the 1.5 MWth CFBC of the Institute of
Engineering Thermophysics in Beijing is used (Qian et al., 2000). The set of data needed to run and to
validate the model is listed bellow :
Carbon parameters :
• Fixed carbon,
• Initial coal size distribution (after devolatilisation and primary fragmentation),
• Comminution constants in particular combustion and attrition constants,
• Carbon in fly and bed ash.
Ash balance analysis :
• Coal ash content,
• PAPSD,
• PSD of circulating particle [result],
• PSD of fly ash [result],
• PSD of bottom ash [result],
• fly ash over total ash ratio [result].
Operating and design parameters :
• Coal feed rate
• Oxygen concentration after volatile combustion,
• Characteristic circulation times,
• Efficiency of cyclone and bottom bed extraction.
The following figure shows, in cumulated form, the size distribution of circulating particle, the
PAPSD and the size distribution of fly and bottom ash. The sample circulating particles were
extracted from the cyclone return leg. The PAPSD was measured by IRC-CNR.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 38
Circulating Fluidized Bed »
From experimental values, it is possible to solve equation (9) for the cyclone and the bed extraction
efficiency. For example, if we suppose that R’(d)=0, the resulting particle size distribution of fly and
bottom ash is equal, in their size range, to f’ . From figure 27, we can deduce that this hypothesis
PAPSD
gives good indication on the particle size distribution of fly and bottom ash. It should be noted that
those distributions are independent of t (d) and t (d). The cyclone and bed drain efficiencies here
c d
obtained are used in the rest of the study.
Figure 27: (left) experimental particle size distributions. (right) comparison between model and
experimental fly and bottom ash with the assumption that the inert attrition rate is null.
6.4.2 Main simulation results
The main simulation results are listed below :
1. mass of circulating particles (furnace pressure drop)
2. particles size distribution in circulation loop
3. fly ash over total ash ratio
4. carbon concentration per class
5. carbon in fly ash
6. carbon in bed ash
Main Model Results
Furnace pressure drop 4.7 kPa
Mean ash diameter 290 µm
Carbon fraction 0.5 %
Inert fly ash ratio 10 %
Carbon fraction in fly ash 0.01 %
Carbon fraction in bottom ash 30 %
Table 2 : results of the reference case
The resulting particles size distribution of carbon and inert content is shown in figure 28.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 39
Circulating Fluidized Bed »
Figure 28 : equivalent size distribution of carbon and inert content of circulating particles.
6.4.3 Fly ash to total ash ratio
The fly ash to total ash ratio measured on the pilot (85 %) is different from the predicted one (10 %).
This discrepancy could have several origins. On the one hand, on the pilot, the bed extraction
operation is discrete while this operation is modelled as continuous. On the other hand, the resulting
fly ash over total ash ratio may be interpreted as the relevance of an inert attrition mechanism.
Following Pis et al. (1991), we can modelled the inert attrition rate by :
k'
R'(d)=- a (U- U )d (10)
mf
3
with k =1.6 10-7 s-1. The attrited fines are distributed through the y ’ function to the size ranges bellow
a
50 µm. The relative importance of inert attrition versus cyclone or bed drain extraction could be
estimated by computing a ratio of the characteristic times :
W' f'(d)
r(d)= k' (U - U ) (11)
a mf
E' f' (d)
0 PAPSD
Since r(d)<1 we can assume that this modelled attrition mechanism has little significance in our
context. This analysis is confirmed by the simulation.
To study the influence of attrition, we use the model described by equation (6). With this model,
attrition is very effective for small particles and the inert balance is significantly modified. For

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 40
Circulating Fluidized Bed »
example, the evolution of the equivalent furnace pressure drop and the mean circulating particles size
distribution with the inert attrition constant have been reported in figure 29. When the attrition
constant is increased, we observe an important decrease of the furnace pressure drop, since a large
amount of mass of particle leaves the circulating loop by the cyclone. Therefore the fly ash over total
ash ratio increases.
Nevertheless it has not been possible to find a set of model parameters coherent with experimental
values. Our knowledge on inert attrition is insufficient to reach the experimental observations.
Figure 29 : the influence of attrition constant on furnace pressure drop and mean circulating particle
diameter (cf. equation 7).
6.4.4 Carbon in ash
The carbon load in the circulating particles is low (0.5 % of the total mass) which is representative of
experimental observations. Nevertheless, the predictions of carbon in ash are far from experimental
values.
The carbon load in bottom-ash is over-estimated. In the present model, the kinetic of carbon
combustion is used while the kinetic of Primary Ash formation is ignored : those two mechanisms
should be coupled. As a consequence, the inert bed extraction is calculated on an equilibrium inert
distribution while the carbon bed extraction is calculated on a distribution controlled by comminution.
Too many big "carbon" particles are extracted.
The carbon load in bottom-ash is under-estimated. This discrepancy could have several origins. The
carbon attrition could be responsible for a high level of carbon in fly ash. However, increasing the
attrition constant has no influence on that value since fines would burn very quickly. This analysis is

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 41
Circulating Fluidized Bed »
confirmed by simulation cases where the oxygen concentration is decreased : the carbon in fly ash
increases sharply. The need for a model on char reactivity is therefore enlighten.
6.5 Modelisation conclusion
From this analysis, we can conclude that the present model could serve as a basis for a complete
comminution model which would take into account the carbon and the inert content of coal. The use
of the Primary Ash concept allows to predict favourably the size distribution of fly and bottom ash.
However several disagreements between experimental and model data are observed. While the
discrepancy concerning carbon-in-ash could be explained, the difference concerning the fly over total
ash ratio is not fully understood.

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 42
Circulating Fluidized Bed »
7. Conclusion
The research program « Coal Comminution Characterization for Industrial Scale Circulating Fluidized
Bed » aimed at defining a coal characterization procedure for combustion in industrial scale CFB, in
order to get information on the size reduction of a coal particle and the final size distribution of ash.
This goal has been approached with the help of the concept of Primary Ash and with the associated
definition of a coal characterization procedure on lab scale apparatus. Also effectively usable, the
definition of the experimental procedure still needs to be improved to get results more independent of
unspecified operating conditions. For a qualitative analysis, the obtained results have proven to be
enough accurate to make an inter-coal classification. Furthermore this classification can be favorably
compared to pilot scale measurements such as fly ash or pressure drop ratios. For a quantitative
analysis, the prediction of the particle size in the circulating loop is still considered as a far objective.
Figure 30: The ash formation mechanism and the concept of primary ash particle size distribution
(PAPSD) and final ash particle size distribution (TU-VIENNA).

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 43
Circulating Fluidized Bed »
8. References
Arena, U., Chirone, R., D’Amore, M., Miccio, M. and Salatino, P., Some issues in modelling bubbling
and circulating fluidized-bed coal combustors, Powder Tech., 82 (1995)
Arena, U., D’Amore, M. and Massimilla, L., Carbon attrition during the fluidized combustion of a
coal, AIChE J., 29 (1983)
Arena, U., Cammarota, A., Massimilla, L., Siciliano, L., and Basu, P., Combust. Sci. and Tech., 73,
383 (1990)
Basu, P., Fraser, S., Circulating fluidized bed boilers, Ed. Butterworth-Heinemann (1991)
Basu, P., and Nag, P.K., Chem. Engng Science, 51, 1 (1996)
Bursi, J.M., Lafanechere, L., and Jestin, L., Proc. of 1999 Int. Conf on FBC, Savannah (GA), ASME
(NY), paper FBC99-0045 (1999)
Chirone, R., Massimilla, L. and Salatino, P., Comminution of carbons in fluidized bed combustion,
Prog. Energy and Comb. Sci., 17, 4 (1991)
Geldart, D., Behavior of Fine Particles in a Fluidized Bed of Coarse Solids, Electric Power Research
Institute, Palo Alto (CA) Final Report EPRI CS2094 (1981)
Haider, A., and Levenspiel, 0., Powder Technol., 58, 63 (1989)
Hajicek, D.R., Mann, M.D., Moe, T.A., and Henderson, A.K., Proc. of 1993 Int. Conf on FBC, San
Diego (CA), ASME (NY), p. 99 (1993)
Herbertz H., Lienhard H., Barner H.E., Hansen P.L., Effects of fuel quality on solids management in
CFB boilers, 10th Int. Conf. On FBC, Ed A. M. Manaker, ASME, New York, pp 1-6 (1989)
Johnsson F. and Leckner B., Vertical distribution of solids in a CFB furnace, 13th Int. Conf. On FBC,
Ed. K.J. Heinschel, ASME, New York, pp 671-679 (1995)
Leckner,B., and Andersson, B.A., Powder Technol. 70, 303 (1992)
Levenspiel, O., Kunii, D. and Fitzgerald, T., Powder Tech., 2, 87 (1968)
Li, Z., Ni, W., Yue, G., Sun, X. and Wei, Z., A general mathematical model for the total ash mass
balance of CFBC, ASME-FBC (1997)
Lyngfelt A., Amand L-E., Leckner B., Progress of Combustion in the Furnace of a Circulating
Fluidized Bed Boiler, 26th Symposium (international) on Combustion pp 3253-3259 (1996)
Merrick,D., and Highley, J., AlChE Symp. Ser., N. 137, Vol. 70, p. 366 (1974)
Muschelknautz, U., and Muschelknautz, E., "Circulating Fluidized Bed Technology VI", J. Werther
(Ed.), Dechema, Wuertzburg, pp 761-767 (1999)

EDF Synthesis of the research program
HP-43/00/046/A
R&D « Coal Comminution Characterization for Industrial Scale Page 44
Circulating Fluidized Bed »
Nowak, W., Bis, Z., Gajewski, W., Matsuda, H., and Hasatani, M., "Circulating Fluidized Bed
Technology V", M. Kwauk and J. Li (Eds.), Science Press, Beijing (1997)
Olsson D., Techniques for in-situ measurements of combustible content in CFB combustors, Dept of
Energy Conversion CTH, Internal Report I99-39 (1999)
Pis, J., J., Fuertes, A., B., Artos, V., Suarez, A. and Rubiera, F., Attrition of coal ash particles in a
fluidized bed, Powder Tech., 66 (1991)
Qian, M., Boëlle, A., Jaud, P., Yue, G., and Tang, Z., Experimental investigation on the coal ash size
formation in CFB combustion, IEA-FBC (2000)
Qian, M., Boëlle, A., Jaud, P., Na, Y., Lu, Q., Bao., S., Cui, P., Jiao, W., Zhao, H., Influence of coal
nature and structure on ash size formation characteristic and related pollutant emissions during CFB
combustion, Thermal and Fluid Sciences (2000)
Salatino, P., Proc. of the XVIII Conf. On the use of computers in Chem. Engng-CEF (1987)
Werther J., and Reppenhagen J., Catalyst attrition in Fluidized Bed system, AiChE J., 45, N°9 (1999)
Winter, F., Liu, X., Ash formation under CFBC conditions, IEA-FBC (2000)
Wirth, K.-E., Chem. Engng Sci., 50, 2137 (1995).
Wu, R.L., Lim, C.J., Grace, J.R., and Brereton, C.M.H., Int. J Heat Mass Transfer, 14, 2019 (1991)
Yue, G., Lan, W., and Xuyi, Z., Ash size formation characteristics in CFB coal combustion, 4th Int.
Conf. FBC (1993)
Zhang, J., Jiang, P., and Fan, L.-S., Ind Eng. Chem. Res., 37,1499 (1998)
