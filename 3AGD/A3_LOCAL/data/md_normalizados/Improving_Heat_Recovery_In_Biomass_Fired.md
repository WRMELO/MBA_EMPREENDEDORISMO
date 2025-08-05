# Improving_Heat_Recovery_In_Biomass_Fired

**Fonte**: Improving_Heat_Recovery_In_Biomass_Fired.pdf  
**Data de conversão**: 2025-07-30 15:06:03  
**Origem**: base_relevantes

---

ORNL/TM-2013/276
IMPROVING HEAT RECOVERY IN
BIOMASS-FIRED BOILERS
July 31, 2013
Prepared by
James R. Keiser, ORNL, Principal Investigator
W. B. A. (Sandy) Sharp, SharpConsultant
Douglas L. Singbeil, FPInnovations
Preet M. Singh, Georgia Institute of Technology
Laurie A. Frederick, FPInnovations
Joseph F. Meyer, Georgia Institute of Technology
1

DOCUMENT AVAILABILITY
Reports produced after January 1, 1996, are generally available free via the U.S. Department of
Energy (DOE) Information Bridge.
Web site http://www.osti.gov/bridge
Reports produced before January 1, 1996, may be purchased by members of the public from the
following source.
National Technical Information Service
5285 Port Royal Road
Springfield, VA 22161
Telephone 703-605-6000 (1-800-553-6847)
TDD 703-487-4639
Fax 703-605-6900
E-mail info@ntis.gov
Web site http://www.ntis.gov/support/ordernowabout.htm
Reports are available to DOE employees, DOE contractors, Energy Technology Data Exchange
(ETDE) representatives, and International Nuclear Information System (INIS) representatives from
the following source.
Office of Scientific and Technical Information
P.O. Box 62
Oak Ridge, TN 37831
Telephone 865-576-8401
Fax 865-576-5728
E-mail reports@osti.gov
Web site http://www.osti.gov/contact.html
This report was prepared as an account of work sponsored by an
agency of the United States Government. Neither the United States
Government nor any agency thereof, nor any of their employees,
makes any warranty, express or implied, or assumes any legal
liability or responsibility for the accuracy, completeness, or
usefulness of any information, apparatus, product, or process
disclosed, or represents that its use would not infringe privately
owned rights. Reference herein to any specific commercial product,
process, or service by trade name, trademark, manufacturer, or
otherwise, does not necessarily constitute or imply its endorsement,
recommendation, or favoring by the United States Government or
any agency thereof. The views and opinions of authors expressed
herein do not necessarily state or reflect those of the United States
Government or any agency thereof.
2

ORNL/TM-2013/276
Advanced Manufacturing Office
IMPROVING HEAT RECOVERY IN BIOMASS-FIRED BOILERS
Authors:
James R. Keiser, ORNL
W. B. A. (Sandy) Sharp, SharpConsultant
Douglas L. Singbeil, FPInnovations
Preet M. Singh, Georgia Institute of Technology
Laurie A. Frederick, FPInnovations
Joseph F. Meyer, Georgia Institute of Technology
Date Published: July 31, 2013
Prepared by
OAK RIDGE NATIONAL LABORATORY
Oak Ridge, Tennessee 37831-6283
managed by
UT-BATTELLE, LLC
for the
U.S. DEPARTMENT OF ENERGY
under contract DE-AC05-00OR22725
3

Contents
LIST OF FIGURES ........................................................................................................................ 6
LIST OF TABLES .......................................................................................................................... 9
ACKNOWLEDGMENTS ............................................................................................................ 10
ACRONYMS ................................................................................................................................ 11
EXECUTIVE SUMMARY .......................................................................................................... 12
1. INTRODUCTION AND BACKGROUND ............................................................................. 14
2. RESULTS ................................................................................................................................. 18
2.1 ASSESSMENT OF ALTERNATE TECHNOLOGIES ..................................................... 18
2.1.1 Design Modifications to Inhibit Superheater Corrosion .............................................. 18
2.1.2 Process Modifications to Inhibit Superheater Corrosion ............................................. 29
2.1.3 Superheater Corrosion Produced By Biomass Fuels ................................................... 33
2.1.4 Energy Sources ............................................................................................................ 34
2.1.5 Alloys Resistant to High Temperature Corrosion ........................................................ 34
2.1.6 Corrosion Mechanisms in Biomass Boiler Superheater Environments ....................... 36
2.1.7 Corrosion of Biomass Boiler Superheater Materials ................................................... 39
2.2 LABORATORY CORROSION STUDIES ........................................................................ 45
2.2.1 Introduction .................................................................................................................. 45
2.2.2 Experimental Procedure ............................................................................................... 45
2.2.3 Results and Discussion ................................................................................................ 49
2.2.3.1 Overview ................................................................................................................... 49
2.2.4 Comparison to Field Data ............................................................................................ 57
2.2.5 Summary and Conclusions .......................................................................................... 58
2.3 SOLUBILITY OF METAL OXIDES IN MOLTEN SALT .............................................. 61
2.3.1 Background .................................................................................................................. 61
2.3.2 Experimental ................................................................................................................ 62
2.3.3 Results and Discussion ................................................................................................ 64
2.3.4 Conclusions from Molten Salt Solubility Studies ........................................................ 65
2.4 FIELD CORROSION STUDIES ........................................................................................ 67
2.4.1 Experimental Procedure ............................................................................................... 67
2.4.2 Results .......................................................................................................................... 70
2.4.3 Summary ...................................................................................................................... 83
2.5 ECONOMICS ..................................................................................................................... 85
2.5.1 Calculation Methods .................................................................................................... 85
4

2.5.2 Components of the Steam Power Cycle Calculation Module ...................................... 86
2.5.3 Boiler Systems Analyzed ............................................................................................. 89
2.5.5 Economic Calculations ................................................................................................ 93
2.5.6 Issues Raised By Simplifying Assumptions ................................................................ 96
2.5.7 Environmental Benefits of Higher Steam Conditions ................................................. 98
2.5.8 Discussion and Conclusions ........................................................................................ 99
3. BENEFITS ASSESSMENT AND COMMERCIALIZATION ............................................. 101
4. ACCOMPLISHMENTS ......................................................................................................... 103
5. CONCLUSIONS AND RECOMMENDATIONS ................................................................. 104
REFERENCES ........................................................................................................................... 105
5

LIST OF FIGURES
Fig. 1. Type 310H stainless steel tube exposed 36 months in a wood-fired power boiler. .......... 14
Fig. 2 Corrosion rate as a function of temperature for type 310 stainless steel exposed to low
melting temperature deposits. ....................................................................................................... 15
Fig. 3: Schematic drawing of Iglesta CHP boiler at, Södertälje, Sweden [6] ............................... 19
Fig. 4. General arrangement of Schweinfurt waste-to-energy boiler [10] .................................... 20
Fig. 5. “Chlorine trap” and Horizontal Wash System in Schweinfurt boiler [9] .......................... 21
Fig. 6. Accumulation of low-melting temperature deposits on Schweinfurt low temperature
screen tubes [12] ........................................................................................................................... 21
Fig. 7. Foster Wheeler INTREX loop seal superheater [15] ......................................................... 22
Figure 8: Metso CYMIC biomass boiler with loop seal superheater [16] .................................... 23
Fig. 9. Lurgi design for superheater in external “ash” cooler [19] ............................................... 23
Fig. 10. Arrangement of Fluidized Bed Heat Exchanger in recirculated ash system [13] ........... 24
Fig. 11. Ensted EV3 biomass boiler with separate wood-fired superheater connected to steam
system of coal-fired unit [20] ........................................................................................................ 25
Fig. 12. Boiler 15 at E.ON Händelö waste-to-energy cogeneration plant, Norrköping, Sweden
([22]............................................................................................................................................... 25
Fig. 13. City of Amsterdam waste-fired power plant [23] ............................................................ 26
Fig. 14. Effects of increasing superheater tube temperature on concentrations of potential
corrosives [25] .............................................................................................................................. 27
Fig. 15. Metso tube containing a thermally-insulating layer to raise its surface temperature ...... 27
above the dew point of NaCl vapor [28] ....................................................................................... 27
Fig. 16: Graphic representation of the three salt compositions used in this work. ....................... 46
Fig. 17. Alloy Set 1 laid out in preparation for insertion to a furnace, showing the reproducibility
of the initial salt packing and surface height. The pre-oxidized coupons in the third and last rows
from the right are darker than the remaining as ground coupons. Blank “guard” pots placed at the
gas inlet are also visible. ............................................................................................................... 49
Fig. 18. Six coupons embedded in epoxy with their support pins. The mount on the right has not
been machined square yet. The mount on the left has been dry sectioned. .................................. 49
Fig. 19. A mosaic image of a cross-section after analysis. Inset shows top right corner in more
detail. The outer red circle is the original circumference of the coupon. The green lines indicate
the depth measured for metal loss, and the blue lines indicate the total affected metal
measurement for each of the 24 arcs around the circumference. The average of the 24 total
affected metal measurements is defined as the TAM of the coupon. ........................................... 50
Fig. 20. Shows variation with salt colour relating to corrosion of the coupon. Red circles indicate
coupons of pre-oxidized HR214 (Alloy FP) in RB salts at 625 °C. Note that the only Alloy F
coupon not to show substantial spalling is the one with the yellow-shaded salt. ......................... 51
Fig. 21. Variation of average TAM with time in PB2 salts at 650 °C (T14, T15, T16), in microns.
....................................................................................................................................................... 53
Fig. 22. Test data from alloys exposed to PB2 salts for 1000 hrs at 650 °C. Alloys are listed in
order of increasing nickel content left to right with the last four on the right being the alumina
formers (E, EP, F, FP). Metal loss is blue portion of bar, TAM is green portion of bar. ............. 53
Fig. 23. Test data from alloys exposed to RB salts for 1000 hrs at 625°C. Metal loss is blue
portion of bar, TAM is red portion of bar. The alloys are listed in order of increasing nickel
content left to right with the alumina formers at the right (E, EP, F, FP). .................................... 54
6

Fig. 24. Corrosion results for Alloy Set 3 after exposure to recovery boiler salts at (a) 530 °C and
(b) 625 °C for 1000 hours in the standard atmosphere plus 50 ppm SO . .................................... 55
2
Fig. 25. Comparison of average TAM for the alloys that were in recovery boiler 1000 hour tests,
without and with the addition of 50 ppm SO . (a) 530°C; (b) 625°C .......................................... 56
2
Fig. 26. The average TAM in microns for each alloy exposed to the PB2 environment at 650 °C.
Alloy performance is color coded as acceptable (green), intermediate (yellow) and unacceptable
(red). .............................................................................................................................................. 60
Fig. 27. The average TAM in microns for each alloy exposed to the recovery boiler environment
at 530 °C. Alloy performance is color coded as acceptable (green), intermediate (yellow) and
unacceptable (red). ........................................................................................................................ 60
Fig. 28. The average TAM in microns for each alloy exposed to the recovery boiler environment
at 625 °C. Alloy performance is color coded as acceptable (green), intermediate (yellow) and
unacceptable (red). ........................................................................................................................ 60
Fig. 29. Schematic of a negative solubility gradient throughout the molten salt that continually
precipitates out to form an unproductive scale[112] ..................................................................... 63
Fig. 30. Schematic of experimental apparatus .............................................................................. 63
Fig. 31. Average solubility of metal oxides in a recovery boiler salt exposed for 8 hours at 750oC
....................................................................................................................................................... 65
Fig. 32. Average solubility of alumina in the presence of an additional metal oxide during 8
hours of exposure .......................................................................................................................... 66
Fig. 33. Left) Schematic of the corrosion samples, center) Photo of samples tack welded with
thermocouples protruding from the surface of the samples, and right) Photo of samples welded
together and with shim stock welded in place to hold thermocouples on the surface of the
samples. ......................................................................................................................................... 68
Fig. 34. Typical corrosion probe showing the arrangement of samples as they were assembled
on the probe................................................................................................................................... 71
Fig. 35. Photo of the 30 samples removed from one of the corrosion probes. Samples #6 and
#10 still contain the spacers used to position the support rod in the center of the probe. Several
other samples still contain the remnants of the thermocouple that was attached to the outer
surface of most samples. ............................................................................................................... 71
Fig. 36. Average daily temperatures for each of the ten thermocouples on the deposit sampling
probe. ............................................................................................................................................ 73
Fig. 37. Typical example of thermocouple temperatures from the corrosion probe exposed in the
Covington recovery boiler. Note that the orange line shows the temperature of thermocouple
#23 which was being used to control the flow of cooling air and thus the probe temperature. .... 73
Fig. 38. Average daily temperatures of thermocouples in the Covington recovery boiler .......... 74
Fig. 39. Total affected material as a function of exposure temperature for samples exposed for
2,000 hours on the corrosion probe in the Covington recovery boiler. ........................................ 74
Fig. 40. Total affected material versus exposure temperature for individual alloys exposed for
2,000 hours on the corrosion probe in the Covington recovery boiler. ........................................ 75
Fig. 41. Results of X-ray diffraction measurements of deposits collected from the bottom of 7
samples on the corrosion probe in the Crofton hogged fuel boiler. .............................................. 76
Fig, 42. Daily average temperature of thermocouples exposed about 2,160 hours on the
corrosion probe in the Crofton hogged fuel boiler. ....................................................................... 77
Fig. 43. Total affected material as a function of exposure temperature for samples exposed for
2,160 hours on the corrosion probe in the Crofton hogged fuel boiler. ........................................ 77
7

Fig. 44. Total affected material versus exposure temperature for individual alloys exposed for
2,160 hours on the corrosion probe in the Crofton hogged fuel boiler. ........................................ 78
Fig. 45. Photo of the corrosion probe in the Gadsden power boiler just prior to its removal (photo
courtesy of Billy Zemo, Southern Company). .............................................................................. 80
Fig. 46. Average daily temperatures of thermocouples on the corrosion probe exposed about 2,
540 hours in the coal and wood co-fired Gadsden power boiler. ................................................. 80
Fig. 47. Total affected material as a function of exposure temperature for samples exposed for
2,540 hours on the corrosion probe in the Gadsden power boiler. ............................................... 81
Fig. 48. Average daily temperatures of thermocouples on the corrosion probe exposed about
2,830 hours in the Port Mellon hogged fuel boiler. ...................................................................... 81
Fig. 49. Total affected material as a function of exposure temperature for samples exposed about
2,830 hours on the corrosion probe in the Port Mellon hogged fuel boiler. ................................. 82
Fig. 50. Total affected material versus exposure temperature for individual alloys exposed for
2,830 hours on the corrosion probe in the Port Mellon hogged fuel boiler. Note the higher
amount of material lost in the 400-430°C temperature range for most alloys. ............................. 83
Fig. 51. Process mass and energy streams included in the software model. ................................. 86
Fig. 52. Types of steam turbine used in calculations of costs and benefits of increasing
superheater steam temperature. ..................................................................................................... 89
Fig. 53. Increase of specific enthalpy of steam with temperature at 50 and 100 bars pressure (725
and 1450 psi). ................................................................................................................................ 91
Fig. 54. Increase of specific entropy with temperature at 50 and 100 bars pressure (725 and 1450
psi)................................................................................................................................................. 92
Fig. 55. Increase in specific available energy in steam with increasing steam temperature at
constant pressure. .......................................................................................................................... 92
8

LIST OF TABLES
Table 1. The test matrix for the laboratory program. Cover gas for all experiments contained
5%O , 10%CO , 20%H O, bal. N . Makeup of Alloy Sets is shown in Table II ......................... 45
2 2 2 2
Table 2. Alloys used in each alloy set. Due to limited space for data in tables and graphs, codes
are used throughout the report to represent the alloys .................................................................. 47
Table 4. Standard deviation in average TAM for alloys for all the test environments. The data is
separated into Vapor Phase and Under-Deposit results and sorted by the average of those results
....................................................................................................................................................... 52
Table 5. Composition of alloys selected for exposure in the corrosion probes ............................ 69
Table 6. Arrangement of samples on the corrosion probe and location of thermocouples .......... 70
Table 7: Components of boiler sub-module .................................................................................. 87
Table 8: Components of the steam turbine sub-module ............................................................... 87
Table 9: Components of exhaust steam condenser sub-module ................................................... 87
Table 10: Components of condensate transfer sub-module .......................................................... 88
Table 11: Components of the deaerator sub-module .................................................................... 88
Table 12: Components of the boiler feedwater pump sub-module ............................................... 88
Table 13: Components of the combustion air sub-module ........................................................... 88
Table 14 Steam system parameters for the five boilers studied .................................................... 93
Table 15: Value of increased energy production in the two example recovery boilers ................ 94
Table 16: Value of increased power that could be produced by raising exit steam temperatures by
50 and by 100 Celsius degrees in the three example wood-fueled boilers. .................................. 95
Table 17: Summary of calculated value of additional power generated by raising exit steam
temperatures by 50 and 100 Celsius degrees ................................................................................ 95
Table 18: Calculations of redirected steam flows in the steam turbines of Recovery Boilers B and
M as the inlet steam temperature is raised by 50 and by 100 Celsius degrees. ............................ 97
Table 19: Calculations of steam flow reductions in the steam turbines of Biomass-Fueled Boilers
C, H and M as the inlet steam temperature is raised by 50 and 100 Celsius degrees. .................. 98
Table 20: Cumulative energy benefits from using additional energy produced in improved
biomass-fired boilers to displace energy from fossil (natural gas) fired boilers ........................... 98
Table 21: Cumulative environmental benefits from using additional energy produced in
improved ....................................................................................................................................... 98
biomass-fired boilers to displace energy from fossil (natural gas) fired boilers ........................... 98
Table 22: Cumulative energy benefits from replacing natural gas fired boilers with biomass-fired
boilers ............................................................................................................................................ 99
Table 23: Cumulative environmental benefits from replacing fossil fuel (natural gas) fired boilers
with biomass-fired boilers............................................................................................................. 99
9

ACKNOWLEDGMENTS
This research was sponsored by the U.S. Department of Energy, Office of Energy Efficiency and
Renewable Energy, Advanced Manufacturing Office, under contract DE-AC05-00OR22725 with UT-
Battelle, LLC, and was funded under the American Recovery and Reinvestment Act as CPS project
18991. The project was led by Oak Ridge National Laboratory and supported by in-kind contributions
from the following project partners:
Ǻbo Akademi University, participant
Andritz Oy, cost sharing partner
Babcock & Wilcox, cost sharing partner
Catalyst Paper, cost sharing partner
Chalmers University, participant
Domtar Corporation, cost sharing partner
FM Global, cost sharing partner
FPInnovations, participant and cost sharing partner
Foster Wheeler, cost sharing partner
Georgia Institute of Technology, participant and cost sharing partner
Haynes International, cost sharing partner
Howe Sound Pulp and Paper, cost sharing partner
International Paper, cost sharing partner
MeadWestvaco, cost sharing partner
Metso Power, cost sharing partner
OutoKumpu, cost sharing partner
Rolled Alloys, cost sharing partner
Sandvik Materials Technology, cost sharing partner
SharpConsultant, participant and cost sharing partner
Southern Company, cost sharing partner
Special Metals, cost sharing partner
ThyssenKrupp VDM, cost sharing partner
University of Toronto, participant
Vattenfall Power Consultant, cost sharing partner
Weyerhaeuser Company, cost sharing partner
Particular thanks are due to Hiram Rogers for his help in preparation, review and editing of this
manuscript and to John D. Andrews, Jr. (MeadWestvaco) and to D. William Francis (FPInnovations) for
helpful comments on the economic assessment. Adam Willoughby led the effort to assemble the probes
and the data collection system. For the corrosion probe samples, Tyson Jordan and Hu Longmire carried
out the metallographic sample preparation and light microscopy examinations, Tracie Lowe conducted
the scanning electron microscope examinations, Robbie Meisner performed the X-ray diffraction and
Maggie Connatser the Raman examinations of the deposits. Employees of all four of the facilities where
probes were exposed assisted with installation and removal of the probes as well as help in
troubleshooting several problems that arose. In particular, the help provided by Curtis Clemmons at
Covington, Bob Erickson at Crofton, Billy Zemo at Gadsden and Peter Hildering at Port Mellon is
appreciated. Neville Stead of FPInnovations provided considerable help in installation, maintenance and
removal of the Crofton and Port Mellon corrosion probes. Material for the corrosion samples was
provided by Haynes International, Rolled Alloys, Sandvik Materials Technology, Special Metals and
Thyssen Krupp VDM.
10

ACRONYMS
ACS American Chemical Society
BC British Columbia
BFB Bubbling fluidized bed
Btu British Thermal Unit
CFB Circulating fluidized bed
CHP Combined heat and power
DOE Department of Energy
EDX Energy Dispersive X-ray Analysis
DTA Differential Thermal Analysis
FMT First melting temperature
HT/HP High temperature/high pressure
HP High Pressure
HVOF High velocity oxy fuel
ICP Inductively Coupled Plasma-optical Emission Spectroscopy
ID Inner Diameter
LP Low Pressure
MFC Mass flow controller
mm Millimeter
MP Medium Pressure
Mpa Mega Pascal
MW Mega watt
MWh Mega watt hour
NACE National Association of Corrosion Engineers
ORNL Oak Ridge National Laboratory
P Pressure
ppb parts per billion
ppm parts per million
psi pounds per square inch
SCR Selective catalytic reduction
T Temperature
TAM Total affected metal
TAPPI PEER Technical Association of the Pulp and Paper Industry – Pulping, Engineering,
Environmental, Recycling and Sustainability
TC Thermocouple
UK United Kingdom
UNS Unified numbering system
US United States
WTE Waste to energy
11

EXECUTIVE SUMMARY
Combustion of biomass has been used by industry to produce steam and power for many years, but new
technologies are being introduced to better recover the energy from biomass as well as to produce a
synthetic gas (syngas) that can be used as a starting point in the production of automotive and diesel fuels
as well as higher value chemicals. It is of significance that operating temperatures in combustion and
gasification systems are often restricted by materials limitations resulting from the degradation of
materials in the highest temperature areas. For systems recovering heat and/or generating steam,
operating limits are often imposed by degradation of the superheater tubes that recover heat from the
combustion gases at the highest temperatures.
The steam temperature of biomass fueled boilers is limited by high temperature corrosion of superheater
alloys in the ash deposit/flue gas environment. During visits with European researchers and boiler
manufacturers and operators, it was learned that advanced European biomass boilers combine design
modifications, process changes and corrosion resistant alloys to achieve substantially higher steam
temperatures and efficiencies than U.S. biomass boilers. Design modifications to reduce superheater
corrosion include adding an “empty pass” between the furnace and the superheater, installing cool tubes
to trap low melting temperature chlorine deposits ahead of the superheater, heating the final superheater
in the recirculated fluidizing medium of a circulating fluidized bed boiler, operating with a slagging
superheater, designing superheaters for quick replacement, raising the superheater temperature above the
dew point of the most corrosive deposits and installing an external superheater fired by a less-corrosive
fuel. Process changes include diluting corrosive biomaterials with less-corrosive fuels, adding high sulfur
fuels to convert alkali chlorides to lower melting temperature sulfates before they reach the superheater,
washing chlorides out of agricultural residues and adding chemicals that convert alkali chlorides to
aluminosilicates.
Another approach to enabling biomass boilers to operate at higher temperatures is to use superheater tube
alloys that are resistant to corrosion in the ash deposit/flue gas environment. Alkali salts are generally the
most aggressive components in the deposits that develop during combustion of biomass fuels. They can
cause corrosion directly by fluxing the Cr O layer, and they can reduce the ash FMT, either causing
2 3
agglomeration and fouling or forming corrosive molten deposits. Lead and zinc impurities in demolition
wood are very corrosive, primarily because they form very low melting temperature ash components.
A laboratory corrosion study was conducted to assess and compare the corrosion that occurs above and
below deposits on the same coupon in simulated fireside superheater environments. Tests were
conducted with three different salt environments that were selected on the basis of analysis of deposits
collected from probes exposed in three boilers of interest. Tests were conducted at three temperatures,
510, 530 and 625°C, which were chosen to be just below, just above and well above the first melting
point of some of the salts of interest. Samples were selected from eleven different alloys that were
included in the testing program. Exposure times ranged up to 1000 hours, and samples were evaluated
through thorough examination of the cross-sections. Performance of the alloys varied considerably as a
function of test conditions; under the most severe conditions none of the alloys was considered acceptable
while all alloys tested were considered acceptable in the least aggressive environments. Overall, alloy
N06025 was one of the top two alloys in terms of corrosion resistance in almost all the test conditions
used.
Alkali metal salts and particularly molten salts are recognized as playing a major role in degradation of
superheater tubes, and consequently, in limiting the maximum steam outlet temperature. Since nearly all
metallic alloys depend on an oxide layer to limit corrosion rates, a study was conducted to determine the
solubility of metal oxides that would be associated with common structural alloys in a molten salt typical
12

of a biomass-fired boiler. A salt mixture of 73.9wt% Na SO , 10.2wt% KCl, 11.5wt%Na CO , and
2 4 2 3
4.4wt% K SO was used in this study and the solubility of metal oxides was found to be NiO <Fe O <
2 4 2 3
Cr O = Al O < SiO where NiO was the least soluble, SiO the most soluble, while Cr O and Al O had
2 3 2 3 2 2 2 3 2 3
roughly equivalent solubility.
Corrosion probes containing multiple specimens of nine different alloys were exposed for at least 2,000
hours in the superheater area of three biomass boilers where the deposits were determined to be enriched
in potassium or chlorine. Similar specimens were also exposed in a boiler co-firing coal and wood. For
the probes, specimen temperatures ranged from a low of less than 400°C to temperatures above 600°C for
all but one case. Following exposure, a section was taken from each specimen and examined using light
microscopy and scanning electron microscopy. Results of the examination of these specimens showed
some alloys performed considerably better than others, and the performance was a function of the
environment. For the potassium-rich environment, alloys S21500 and S34709 showed the greatest
corrosion resistance at a temperature 100 Celsius degrees above the maximum boiler temperature. For the
chloride-rich environment, alloys N08120, S21500 and S34709 showed the least amount of affected
material at 100 Celsius degrees above the maximum boiler temperature.
In the fourth task of this project the relationship between the temperature of superheated steam produced
by a boiler and the quantity of power that it can generate was addressed. Thermodynamic analysis
determined the amount of additional power that could be generated by operating with higher superheated
steam temperatures. Calculations were made for five plants that produce both steam and power two of
which were powered by black liquor recovery boilers and three by wood-fired boilers. Steam generation
parameters for these plants were supplied by industrial partners. Calculations using thermodynamics-
based plant simulation software showed that the value of the increased power that could be generated in
these units by increasing superheated steam temperatures by 100 Celsius degrees above current operating
conditions ranges between $2,410,000 and $11,180,000 per year. The costs and benefits of achieving
higher superheated steam conditions in an individual boiler depend on local plant conditions and the price
of power. However, the magnitude of the increased power that can be generated by increasing
superheated steam temperatures is so great that it appears to justify the cost of corrosion-mitigation
methods such as installing corrosion-resistant materials costing far more than current superheater alloys,
redesigning biomass-fueled boilers to remove the superheater from the flue gas path, or adding chemicals
to remove corrosive constituents from the flue gas. The most economic pathways to higher steam
temperatures will very likely involve combinations of these methods. Particularly attractive approaches
include installing more corrosion-resistant alloys in the hottest superheater locations, and relocating the
superheater from the flue gas path to an externally-fired location or to the loop seal of a circulating
fluidized bed boiler.
13

1. INTRODUCTION AND BACKGROUND
Utilization of biomass is emerging as a promising approach to produce fuels and chemicals because it
reduces the dependence of the United States on petroleum, and particularly petroleum imported from
foreign countries whose political stability is uncertain. The U.S. has been highly dependent on foreign
sources of petroleum, and there are well-publicized efforts underway in the U.S. to reduce that
dependence through use of the extensive coal and natural gas resources as well as the development of
technology and infrastructure to better utilize biomass and other renewable resources. For biomass
utilization, several routes are available: combustion, torrefaction, liquefaction and gasification. This
project addressed materials issues related to combustion of biomass or by-products derived from biomass.
Experience in North America and Europe with conventional fuels has shown the vulnerability of
superheater tubes to a variety of corrosion mechanisms, and the upper operating temperature is generally
limited by the corrosion rate of the superheater tubes. The limit is generally associated with the melting
point of deposits that accumulate on tubes, and potassium and chlorine components of these deposits
reduce their first melting point temperature. An example of superheater tube degradation in a wood waste
power boiler is shown on the left side of Figure 1 [1].
As the use of biomass fuels becomes more common and as the variety of fuel sources increases,
additional corrosion problems are anticipated. Extensive use of other plant and animal materials as well
as municipal waste and refuse derived fuel will likely add sulfur, chlorine, additional alkali metals, and,
possibly heavy metals, to the list of elements in the fuel that can cause corrosion problems. An indication
of the magnitude of the increase in corrosion rate around the deposit melting temperature is shown on the
right side of Figure 1where the weight loss of a fairly corrosion resistant alloy, type 310 stainless steel, is
shown as a function of temperature.
Energy prices are a critical component of manufacturing costs in North American process industries and
these prices along with the increasing emphasis on greenhouse gas reduction are presenting a challenge to
energy intensive industries that currently consume large amounts of fossil fuels. In response, companies
are looking to non-traditional fuels based on biomass to help address these critical issues and allow them
to remain competitive in a global marketplace.
Fig. 1. Type 310H stainless steel tube exposed 36 months in a wood-fired power boiler.
14

50
40
30
20
10
0
600 700 800 900 1000 1100 1200
Temperature, F
15
gm
,ssoL
thgieW
Figure 2 Corrosion rate as a function of temperature for type 310 stainless steel exposed to low melting
temperature deposits.
However, relative to coal and natural gas, biomass-based fuels are extremely inhomogeneous and contain
significant impurities, such as chlorides, alkali metals and heavy metals that deposit on heat transfer
surfaces. While these deposits may reduce the overall energy efficiency of the boiler, their principal effect
is to cause rapid corrosion of heat transfer surfaces that approach, or exceed, the first melting point of the
deposits. As a consequence, boilers burning biomass have largely been limited to operating with
superheater steam temperatures of less than 510°C (950°F) and steam pressures of less than 11 MPa
(1600 psi). Most existing biomass boilers in North America operate at substantially lower steam
temperatures and pressures, particularly those utilized as waste utility boilers. In contrast, the most
modern utility boilers burning coal are intended to operate at 26 MPa (3800 psi) with 615°C (1140°F)
superheated steam temperatures, and research programs are in-place to help design and build even more
efficient boilers by the year 2015.
While small, incremental gains in energy efficiency can be met by improving operation of existing
biomass-fired boilers, much larger gains could be obtained by designing and building biomass boilers that
operate with substantially higher pressures and superheater steam temperatures (HT/HP) than is the
current practice. To gain this enhanced energy efficiency and retain operational reliability, challenging
materials problems in the areas of high temperature strength and environmental degradation must be
overcome, particularly at temperatures near or above the first melting point of the superheater tube
deposits. Within the design envelope of existing biomass-based boilers, the use of higher chromium
content ferritic tube alloys such as 1¼Cr-½Mo or 2¼Cr-1Mo has controlled wastage in mildly corrosive
conditions at operating temperatures below the first melting point. Under more corrosive conditions at
temperatures close to the first melting point of deposits, austenitic tube alloys such as 304H, 310H, 316H,
321H and 347H have been used. For temperatures at or just above the first melting point of deposits, the
iron-nickel-chromium alloys such as 800H, 800HT or nickel-chromium-molybdenum alloys like 625
have also been used, but with mixed success. However, no alloys have yet been found that would allow
biomass-fueled boilers to approach the energy efficiency of coal or gas utility boilers.
This project provided a completely new approach with a potential for significant benefit. The research
identified superheater materials and superheater designs that could survive molten or partially molten
deposits and thus increase the energy derived from biofuels (and/or reduce other fuel requirements) as
well as enabling use of more contaminated (more corrosive) fuels. Improved superheater materials could
improve the energy efficiency of chemical plant boilers recovering heat from process wastes,
municipalities producing electricity from garbage incineration and tire-derived fuel boilers as well as the
forest products industry’s biomass-fueled black liquor recovery boilers and hogged fuel boilers.
Currently, this represents a very significant market, and it most certainly is going to expand with the

growing emphasis on decreasing the production of greenhouse gases and with the potential for increasing
prices of imported fossil fuels.
The overall project sought to address environmental performance improvements of superheater tube
materials for enhanced heat recovery, reliability and competitiveness in biomass-fueled steam generating
systems. The challenge to obtaining increased energy efficiency was to clearly identify all operative
corrosion mechanisms in the superheaters when operating at temperatures 100 Celsius degrees above
current temperatures which likely means above the first melting point of the deposits, and then addressing
solutions to each of these mechanisms in turn. This was achieved by a program that combined
thermodynamic analyses, laboratory studies, and in situ probes to explore and expand the operating
envelope of future biomass-fueled steam generating systems.
This project had the goal of recovering more energy from biomass fuels by operating superheater tubes
with a maximum temperature 100 Celsius degrees higher than current maximum temperatures. To
achieve this higher temperature the project considered the use of alternate superheater tube materials,
alternate superheater designs, and/or techniques to remove from the gas stream the components causing
tube degradation. In addition, a separate task addressed the financial benefits of operating boilers with
higher superheater temperatures as well as the cost of the alternate technologies.
The studies conducted in this project were divided into four primary tasks. The first task consisted of
conducting a critical review of the status of biomass combustion technologies and corrosion of
superheater tube materials in biomass-fired boilers. Because of taxes and incentives being used in Europe
to discourage greenhouse gas production and to encourage utilization of renewable fuels, a greater effort
is being made there to utilize biomass resources. This includes development of new technologies and
improvements on existing technologies. Consequently, team members visited many research and
operating facilities and met with corporate staff members of utilities and equipment manufacturers to
learn about and collect information on research efforts, evaluations of alternate materials and processes in
operating systems and practical experience from unique systems.
A second task consisted of well-controlled laboratory studies to evaluate alternate superheater tube
materials in environments simulating the conditions of particularly aggressive environments.
An extensive testing program was defined using alloys selected by a team of the research partners, the
alloy producers and the boiler manufacturers. The test environments were selected to simulate the
environments in several types of biomass-fired boilers. The temperatures, times and environments (salt
deposits and cover gases) were selected on the basis of the information collected during the
aforementioned critical technology review as well as in consideration of the results from the analysis of
deposits collected from sampling probes exposed in several biomass-fired boilers.
A more basic aspect of the laboratory testing program was a determination of the solubility of various
alloy oxides (Cr O , Al O , SiO ) in molten salts of approximately the same compositions as the deposits
2 3 2 3 2
collected from one of the biomass boilers.
As part of a third task, deposit sampling probes were used to collect superheater deposits from three
biomass boilers whose fuel had the potential to create particularly corrosive environments. Analysis of
the deposits from these probes provided information for selection of the environments for the laboratory
corrosion testing as well as information on the environments to which the corrosion probes were to be
exposed.
Air-cooled, controlled temperature corrosion probes (like those developed and used in a previous project
on superheater corrosion) [2] were used to measure corrosion rates on candidate materials in four boilers.
The goal was to expose the corrosion probes to conditions such that the coolest samples were just below
16

what was assumed to be the first melting temperature of the deposits, while other samples were at a
temperature where the deposits were partially, but not fully, molten and the hottest samples were exposed
under slagging conditions, e.g. with a goal of operating around 30 Celsius degrees above the temperature
at which the deposits are fully molten. Corrosion probes were built from materials likely to be able to
survive the test conditions, for example the most advanced alloy currently serving in superheaters and
advanced Na SO /NaCl-resistant gas turbine alloys that rely on different types of barrier oxides for
2 4
corrosion protection (e.g. Al O -formers as well as Cr O -formers). Selection of candidate alloys was
2 3 2 3
made in consultation with the advanced alloy manufacturers, other researchers as well as boiler
fabricators and operators represented in the Industrial Partners.
In order to facilitate commercialization, another task in this project provided calculations to determine the
extent to which the energy benefits of operating modified superheaters at much higher temperatures
would pay for much more expensive tube materials, for alternate superheaters designs, or for the removal
of the fuel contaminants that cause the low the first melting temperature of the deposits. The original idea
was to develop software to calculate the energy benefits (or fuel savings) that could be achieved by
increasing the steam outlet temperature of any given boiler. However, it was determined that suitable
software already existed although it had not been used with the same objective in mind. Data on boiler
operating parameters were collected from operators and designers of biomass boilers, and this information
was used with the selected software to determine whether the savings that could be achieved by operating
boiler superheaters at temperatures 50 or 100 Celsius degrees hotter. After inputting costs to replace
superheater pendants, it was possible to determine the per foot cost that could be paid for superheater
tubing made from advanced materials (for specified superheater service lives and specified future energy
prices) that would be justified by increased steam temperatures. The software was also used to determine
whether the cost of removing low melting temperature fuel constituents could be justified by increased
thermal efficiencies available by raising the deposit first melting point temperature.
Results from each of these tasks are described in detail in the following sections.
17

2. RESULTS
2.1 ASSESSMENT OF ALTERNATE TECHNOLOGIES
The information presented in this subsection was taken from three recent publications for which Sandy
Sharp was the lead author [3-5].
2.1.1 Design Modifications to Inhibit Superheater Corrosion
Rather than trying to increase the efficiency of biomass boilers by operating with superheater tube
temperatures above the melting temperature of fly ash deposits, European operators use conventional
austenitic superheater tube materials such as Type 347HFG (UNS S34710), Sanicro 28 (UNS N08028)
and AC66 (UNS S33228). They have explored many design modifications to reduce the corrosivity of
the environment where the superheater tubes are installed and this review will discuss seven of these
modifications. Many boilers remove ash deposits upstream of the superheater and/or remove the final
superheater from the flue gas stream, a few operate with molten deposits dripping off the outer surface of
the tubes, a few use rapidly-replaceable superheater units and at least two operate with superheater tube
temperatures above the dew point of the corrosive ash deposits. We will discuss each of these design
modifications in turn.
2.1.1.1 Remove ash deposits upstream of the superheater by adding an empty pass
Extending the length of the passage between the furnace and the superheater or adding a separate radiant
pass (empty chamber) between them has two benefits. It allows more time for the completion of chemical
reactions in the flue gas (e.g. to convert chlorides to lower melting temperature sulfates) and it allows
undesirable ash components to fall out of the flue gases before they reach the superheater. This design is
particularly appropriate in waste-fired boilers where the superheater would otherwise suffer severe
fouling and corrosion.
Figure 3 shows a boiler with this type of radiant pass [6,7]. It is a Circulating Fluidized bed (CFB) boiler
designed by Foster Wheeler for the Igelsta power plant of Söderenergi AB, located in Södertälje south of
Stockholm, Sweden and started up in March 2010. It is designed to co-fire either mixtures of biomass
(mainly wood residues) with up to 25% of recycled fuel pellets (i.e. municipal waste) or up to 70%
recycled wood with other biomass. The Igelsta boiler has an output of 92 kg/s (73,000 lbs/hour) of steam,
at 90 bar (1,305 psi) and 540 ºC (1,004°F). It produces 73 MW of electricity and 219MW of district
heating, with a plant efficiency of nearly 110 % (LHV) or >90% (HHV). To avoid fouling and corrosion
the unit has:
• Its final superheater located in the recirculated fluidizing medium, rather than in the flue gas
environment of the convective pass.
• An empty pass to increase residence time for the flue gases to cool and clean themselves before
reaching the convective superheaters
• Water cannons on the sides of the empty pass to clean the walls of this empty pass and spring
hammers to remove deposits from the convective superheaters
• Addition of sulfur granules [7] to raise the first melting temperature (FMT) of the superheater ash
• Hanging austenitic superheaters that are easily replaceable through the roof
To control the emissions from this unit, ammonia is added to control NO , sodium bicarbonate to capture
x
sulfur, activated carbon to capture mercury and a bag filter to capture dust.
18

Fig. 3. Schematic drawing of Iglesta CHP boiler at, Södertälje, Sweden [6]
A similar empty “radiation pass” between the furnace and the superheater, designed into a waste-to-
energy plant at Norrköping, Sweden has been described by Enestam, Lehtonen and Heikne [8].
2.1.1.2 Remove ash deposits upstream of the superheater by adding a “Chlorine Trap”
Another approach to removing ash deposits upstream of the superheater tubes was implemented after
intensive field studies in a waste-to-energy boiler at the GKS power plant in Schweinfurt, Germany [9].
The arrangement of this boiler is shown schematically in Figure 4 [10]. It operates with steam parameters
of 65 bars and 435°C (943 psi and 815°F). The boiler faces substantial fouling and corrosion problems
because its waste fuels contain high chloride concentrations. The fuel is fired on a grate. After reaching
the top of the furnace the flue gases turn downwards through an empty pass like that described above in
the Södertälje boiler. As the flue gases turn to flow upwards at the bottom of this empty pass they
encounter a section of cool furnace screen tubes, shown schematically in Figure 5. Low melting
temperature ash components that remain in the flue gases after the empty pass condense on the cool
furnace screen tubes and form the massive deposits shown in Figure 6. Because these deposits are
enriched in chlorine, the low temperature screen tube section has been named a “chlorine trap” by its
inventor Ragnar Warnecke. The low temperature screen tubes operate at temperatures between 300 and
400°C (572 to 752°F). Massive deposits accumulate with molten material on their outer surface. These
deposits are removed by sootblowing only once each day. Operating personnel suggest that the molten
ash on the fireside of the deposits may block the inward diffusion of chlorine-containing gases released by
the sulfation of alkali metal chlorides in the flue gas stream and thus reduce the corrosion rate of the
underlying tubes [11].
A similar shield of cool tubes was installed to protect the superheater of a CHP plant at Grenå, The
Netherlands [13]. This plant has a capacity of 18 MW of electricity and 60 MW of heat. It burns coal
containing up to 60 % straw – or coal alone. The fuel is mixed in the boiler furnace with an inactive
material (sand or ash) and combusts at a relatively low and uniform temperature (850°C) to reduce NO
x
emissions and to allow desulfurization to take place in the furnace. Although firing straw would have
produced rapid corrosion, co-firing straw with coal reduced corrosion to manageable rates except in the
external ash cooler, which receives recycled “ash” (fluidizing medium) from the cyclones and contains
the hottest superheaters (removed from the convective pass to avoid corrosion). Unfortunately, the
recycled “ash” included unburned particles that contained enough chlorine to corrode the superheaters.
19

Resulting design changes included keeping metal temperatures in the convective pass below about 450°C
(842°F). As at Schweinfurt, this was achieved by increasing the residence time between the furnace and
the first superheater and by installing a low temperature evaporator tube bundle immediately ahead of the
first superheater tubes in the convective pass. Heat recovered in this evaporator section helped to
compensate for the restriction of heat transfer by thick refractory coatings on the waterwalls. The final
superheater at Grenå was located outside the convective pass, as will be described in Section 7.
2.1.1.3 In CFB boilers, move the final super heater out of the flue gas stream into the recirculated
fluidizing medium or recirculated ash
Fluidized bed boilers burn solid fuel particles suspended on upward-blowing air jets. The tumbling action
within the fluidized bed provides excellent mixing and air for combustion. This quickly heats the fuel
particles to the bed temperature and promotes the completion of combustion reactions. Fluidized bed
boilers can typically burn a wide variety of fuels. Limestone particles can be added to the bed to react
with SO to reduce sulfur emissions and to improve conductive heat transfer to the wall tubes. Fluidized
x
bed boilers are of two types, bubbling fluidized bed boilers and circulating fluidized bed boilers.
Bubbling fluidized bed boilers (BFBs) are normally used to burn lower-quality fuels that contain
substantial volatile matter. Operating them with sub-stoichiometric amounts of combustion air pyrolizes
the fuel in the furnace prior to complete combustion. Most of the fluidizing medium remains in the
Fig. 4. General arrangement of Schweinfurt waste-to-energy boiler [10]
furnace. The inorganic ash that remains after the organic components are burned either falls into a hopper
at the bottom of the furnace or is carried forward with the flue gases as fly ash particles. Some of this fly
ash will be collected in hoppers under the economizer and air heater tubes and the rest will be removed by
electrostatic precipitators or bag filters.
Circulating fluidized bed boilers (CFBs) are different. Their combustion gases propel fluidizing particles
(e.g. sand) out of the furnace. The sand and the ash are separated by the difference in their specific
20

Fig. 5. “Chlorine trap” and Horizontal Wash System in Schweinfurt boiler [9]
Fig. 6. Accumulation of low-melting temperature deposits on Schweinfurt low temperature screen tubes [12]
gravity and particle size. Most of the ash is carried forward into the convection section of the boiler with
the flue gas while almost all the sand particles fall into a cyclone and are returned to the bottom of the
furnace. The flue gases, prevented from recycling to the bottom of the furnace both by the pile of hot
sand in the bottom of the cyclone and by a loop seal device, pass on through the convective passages of
the boiler. Because the sand particles cool only very slightly before returning to the boiler, it is possible
to locate the final superheaters in the recirculated fluidizing medium between the loop seal and the bottom
of the boiler. Five to ten times more heat per unit area is transferred to these immersed superheater tubes
than to tubes in a conventional superheater [14]. Also, the superheater tubes have much less exposure to
alkali metal salts and corrosive gases like HCl and water vapor than they would have in the convective
passage. CFB designs with the final superheater located between the loop seal and the furnace bottom
have been commercialized in Foster Wheeler’s INTREX design [15] and in Metso’s CYMIC boilers [16],
21

shown in Figures 7 and 8. Many of the most recently built biomass boilers use this approach to control
superheater corrosion.
Erosion damage in these relocated superheaters is not rapid because the sand velocities are low. Nafari
and Nylund [17] measured thinning rates of superheater tubes installed in the loop seal of a small wood-
fired CFB boiler in Nässjö, Sweden that produces 5MW of electricity plus 20 MW of district heat. The
steam temperatures at the inlet and outlet of the superheater were 470 and 540°C (878 and 1004°F), and
the authors anticipated that the tube surface temperatures would be 50 to 100 Celcius degrees (90 to 180
Fahrenheit degrees) higher than these values. Tube thinning rates increased with tube temperature, but
tubes exposed for about 16 months showed no more wastage than tubes exposed for about 7 months. The
corrosion products consisted of an inner layer of Cr and Fe oxides beneath an outer Fe-rich oxide.
Chlorides, potassium and sulfur accumulated near the alloy/scale interface. Average material losses on
Esshete 1250 (UNS S21500) and Type 347H (UNS S34710) were comparable and just slightly greater
than those on Alloy AC66 (UNS S33228), although AC66 showed the most severe internal oxidation.
Fig. 7. Foster Wheeler INTREX loop seal superheater [15]
A second publication by Nafari and Nylund [18] reported additional tests of the same alloys and various
coatings in the same loop seal location. Tube temperatures ranged from 510 to 550°C (950 to 1022°F)
and the loop seal ash contained 13% Ca, 9% K, 0.9% Na, 800 ppm sulfate and 100 ppm chloride. Even
the uncoated alloys suffered little corrosion during boiler operation. The fact that the degradation was no
worse after two firing seasons than after one indicated that corrosion, rather than erosion, is the dominant
deterioration mechanism. Austenitic steels suffered some internal oxidation and grain boundary attack.
Although some coatings delaminated, 8 of the 17 coatings tested were unaffected by the exposure. Even
the thickest oxides, on a 9% Cr alloy, were only about 150μm (0.006”) thick after about 7 months in
service.
In boilers burning high-ash fuels, a bottom ash cooler can be added for additional heat recovery. A design
by Lurgi Lentjes Energie, suitable for high ash fuels, moves the final superheater into the coolers that
receive recycled CFB “ash” from the cyclones [13]. This is shown schematically in Figure 9.
22

Figure 8: Metso CYMIC biomass boiler with loop seal superheater [16]
Fig. 9. Lurgi design for superheater in external “ash” cooler [19]
Using this type of external Fluidized Bed Heat Exchanger enabled the small-scale CHP plant in Grenå,
Denmark to operate with a final steam temperature of 580°C (1076°F) while firing coal with straw
containing up to 1% chloride, although the temperatures of superheaters within the convective path had to
be restricted to 450°C (842°F) because of corrosion [13]. A pre-chamber was added to increase the time
available to complete the removal of chlorides from unburned particles in recycled ash from this
coal/straw-fired CFB. The solids separated by the cyclones are returned to the combustor via loop seals at
the combustor exit temperature of 850 to 900°C (1562 to 1652°F). The portion of the solids from the
23

Fig. 10. Arrangement of Fluidized Bed Heat Exchanger in recirculated ash system [13]
seal pots that goes to the Fluidized Bed Heat Exchangers is returned to the combustor at 500 to 600°C
(932 to 1112°F). Changing the portion directed to the heat exchanger provides some additional control of
the combustor temperature, which is useful for handling changing fuel compositions and low loads. The
Lurgi design of external heat exchangers includes a fluidized empty chamber to increase the residence
time and smooth the “ash” flow, followed by one or two heat exchanger chambers including the final
superheater (Figure 10). The average “ash” residence time in these external superheaters varies between 3
and 20 minutes at full load operation [13].
2.1.1.4 Move the final superheater out of the flue gas altogether and heat it with a less corrosive fuel
In cases where a biofuel would produce particularly corrosive conditions on the superheater tubes some
boiler designers have relocated the superheater tubes to a separate space outside the boiler cavity where
they are heated by a less-corrosive fuel. As an example, we will consider the straw-fired boiler started up
in 1998 at the Ensted power station of Sønderjyllands Højspændingsværk in the Danish city of Åbenrå
[20]. Jensen and others showed that straw burning in this type of small grate boiler produced more rapid
deposition and more severe corrosion than coal combustion [21]. Analysis of superheater deposits from
the straw-fired boiler at Ensted found that underneath external iron oxides there was an intermediate layer
of melted KCl with Ca- and Si-rich inclusions over an inner layer of iron oxides and potassium sulfate.
Longer exposures produced thicker and denser inner layers of pure KCl and K SO . The authors
2 4
concluded that a damaging cyclical corrosion mechanism called “active corrosion” occurred at the
deposit/tube interface even when the deposit was several centimeters thick.
Because the straw burning was so corrosive, the maximum steam temperature in the Ensted biomass
boiler had to be limited to 470°C and 210 bar (3,046 psi). However, the steam produced in the straw-
fired boiler was piped to an external superheater (Figure 11) where it was heated to the 542°C required
for the steam turbine in a small furnace fired by much less corrosive wood chips. When steam raised by
the biomass plant was connected in to the rest of the power plant (Figure 11), the overall plant efficiency
was maintained at 40% - exceptional for this type of boiler. The two-unit boiler produces 37.5MW from
its 78% straw/22% wood chips fuel. The first boiler burns bales of straw on a water-cooled vibrating
grate. The superheater portion feeds wood chips onto another vibrating water-cooled grate. The ash
produced by biomass combustion is later spread as fertilizer on the farms where the trees were grown, as
is done at Nässjö.
24

Fig. 11. Ensted EV3 biomass boiler with separate wood-fired superheater connected to steam system of coal-
fired unit [20].
2.1.1.5 Design superheater units for very rapid replacement
Another approach to enabling high steam conditions in boilers with corrosive superheater environments is
to design the superheater units for rapid and simple replacement. This can enable a plant either to use
lower cost alloys that have a limited life or to use high alloys that achieve a very high final steam
temperature but also have a short life. An example is the CFB waste-to-energy boiler in E.ON’s waste to
energy (WTE) plant at Norrköping, Sweden. This boiler produces steam at about 450°C (842°F). Figure
12 shows the horizontal final superheater units, mounted in the loop seals downstream of each of the two
cyclones, which were designed for easy replacement [8].
Fig. 12. Boiler 15 at E.ON Händelö waste-to-energy cogeneration plant, Norrköping, Sweden ([22].
25

Similarly, the heat exchanger units in the recirculated “ash” cooler of the coal/straw-fired boiler in Grenå,
Denmark described above (Figure 10) were reported to be “designed for easy change at appropriate
intervals” [13].
Another example of this approach is the 67 MW waste-fired boiler operated by the City of Amsterdam
[23], one of the largest waste-to-energy facilities in the world. This unit, shown in Figure 13, produces
steam at 440°C (824°F) and 125 bar (1,813 psi) and achieves an electrical efficiency of 30%. Although
the superheaters are located in the flue gas passage, they follow three empty passages (see Section 1
above) so that the flue gas temperature has time to cool and some entrained deposits have time to fall out
before reaching the superheaters. The spacious furnace reduces flue gas velocities, reducing fouling rates.
The superheaters are fabricated from heat resistant steel (15/16Mo3 and 13CrMo44) rather than
corrosion-resistant alloys, but are designed to be replaced as a unit within 72 hours. One recent
replacement was achieved in 48 hours, fire-to-fire.
A substantial corrosion monitoring program [24], including real-time electrochemical corrosion
monitoring probes, indicates that current superheater corrosion rates in this unit are 0.1 to 0.2 mm/year
(0.004 to 0.008” per year). The ability to change out the superheater in 48 hours would make even
substantially higher corrosion rates tolerable.
2.1.1.6 Operate superheater at a temperature above the dew point of corrosive ash deposit
A novel approach to limiting superheater corrosion is to use composite superheater tubes with an
insulating layer between the inner pressure-bearing layer and the outer corrosion-resistant layer. Metso
has patented this method for increasing superheater surface temperatures above the dew point temperature
of alkali chloride salts. Figure 14 shows the effects of increasing superheater tube surface temperatures
on the concentrations of potentially corrosive species [25].
KEY
1: Grate 5: 1st empty chamber
2: 1ary air 6: 2nd empty chamber
3: 2ary air 7: 3rd empty chamber
4: 3ary air 8: Superheaters
9: Economizer
Fig. 13. City of Amsterdam waste-fired power plant [23].
26

Fig. 14. Effects of increasing superheater tube temperature on concentrations of potential corrosives [25].
The data presented in Figure 14 indicate that alkali metal chlorides will not condense at the surface
temperature of the superheater tubes containing an insulating layer (660°C; 1220°F). However, we
cannot assume that alkali chlorides are non-corrosive above their dew point temperature. KCl vapors in a
flue gas react with the Cr O formed on the surface of corrosion-resistant tubes and form K CrO .
2 3 2 4
Segerdahl and others reported that this caused local oxide failure on an 11% Cr martensitic steel that led
to the formation of non-protective Fe O [26].
2 3
Petterson, Svensson and Johansson studied a corrosion-resistant superheater alloy (UNS N08028) at
600°C under conditions where the dew point temperature of KCl was 590°C [27]. KCl vapors reacted
with Cr O on the surface of the alloy, forming K CrO . Although this increased the oxidation rate, it did
2 3 2 4
not cause a sudden failure (breakaway oxidation). The distribution of K CrO on the alloy surface
2 4
depended on the gas flow rate, indicating that the rate of chromate formation was limited by the rate of
arrival of KCl at the surface. No alkali chlorides were found on the alloy surface.
To prevent this condensation, Metso developed a new type of composite tube containing an internal
insulating layer [8] to raise the surface temperature above the dew point temperature of NaCl. Figure 15
shows the thermally insulating layer between the pressure-bearing carbon steel tube and the outer
corrosion-resistant stainless cladding. The equilibria presented in Figure 14 show that the increase in
surface temperature changes the composition of the deposited ash from molten NaCl to NaCl and KCl
vapors with HCl gas and solid Na SO [25].
2 4
Fig. 15. Metso tube containing a thermally-insulating layer to raise its surface temperature above the dew
point of NaCl vapor [28].
Skog and others reported that full-scale testing of these tubes has given “promising” results [25], and a
publication by Enestam, Lehtonen and Heikne provides more information about this testing [8]. Enestam
27

begins by listing design innovations implemented in E.ON’s CFB waste-to-energy boiler at Händelö, near
Norrköping, Sweden, including:
Fuel residence time of 2 seconds at 850°C (1562°F) to promote complete combustion
Flue gases cooled in an empty “radiation pass” ahead of the lower temperature superheater sections
Final superheater located in the loop seal, as a fluidized bed heat exchanger
Tube banks designed for rapid replacement
Although the loop seal final superheater was made from “the best austenitic material”, the waste fuel
caused superheater corrosion that was traced to the condensation of alkali chlorides (primarily sodium
chloride) on these tubes [8]. The corroded superheater tubes were replaced by tubes “that include a
pressure bearing component and additional protective layers (Patent pending)” – evidently the tubes with
the insulating layer described above. Although the higher surface temperature of the new final
superheater tubes will reduce the heat transfer per unit area, this can be compensated for by adding
additional heating surface in the tube bank design phase. Palonen and others [28] have reported that
similar insulating composite tubes are installed in the final (loop seal) superheater in a CFB power boiler
at the Stora Enso paper mill in Langerbrugge, Belgium.
2.1.1.7 Operate superheaters with molten deposits
It was noted in Section 2 that deposits on “chlorine trap” tubes in the Schweinfurt WTE boiler grow thick
enough to be molten at the ash/flue gas interface. It seems possible that this molten layer provides
protection to the underlying tube by slowing the delivery of corrosive species to the tube surface [11].
Žbogar, Frandsen and others studied the shedding of fireside ash deposits from superheater tubes in a
straw-fired grate boiler at Avedøre in Denmark [29]. They used video recording, measured probe mass
gain and probe heat uptake. The Avedøre 2 unit, which can burn natural gas, oil, straw and wood pellets,
operates with a high flue gas temperature (900-1100°C; 1652-2012°F) a high steam temperature 580°C
(and a low deposit melting temperature. The main shedding mechanism in this boiler is the flow of
molten material off the outer surface of the deposit. The rate at which these deposits are shed depends on
the percentage of molten material in the deposit and therefore on the flue gas temperature.
Results from Maribø and Avedøre 2 power plants in Denmark show that the presence of molten phases on
the fireside surface of a superheater deposit does not in itself cause a major corrosion problem. Corrosion
is controlled by the environment and temperature at the tube surface.
Thermographic measurements by Montgomery and others [30] in the Maribø Sakskøbing boiler
confirmed the insulating properties of biomass ash deposits by showing that the superheater surface
temperatures increased substantially when the tubes were covered with deposits. The effects of increased
flue gas temperature are complex because they can simultaneously affect the thickness, composition and
morphology of the deposit and the degree of deposit sulfation. When the surface temperature of the
deposit exceeded 950°C (1,742°F) molten deposits ran off them. Later, test sections of candidate alloys
were installed in the superheaters of straw-fired CHP boilers at both Maribo Saskøbing and Avedøre 2
[30]. Tube samples removed from the boilers were covered with deposits of KCl, K SO and some iron
2 4
oxide. Such oxides as remained on the tube surfaces were porous and spalled easily. The outer portion
was an iron-rich oxide. The inner portion was an iron-chromium-rich oxide. Chromium was
preferentially attacked where it was accessible at grain boundaries in the tube surface. The authors
concluded that the overall corrosion reaction was “active oxidation” (a cyclical corrosion mechanism
involving the formation of iron chloride at the tube surface). Tube thickness data projections suggested
that the average worst case tube thickness loss after 100,000 hours (11.5 years) service in the hottest
superheater bank would be about 3.9 mm (0.15”). Note that, despite the presence of molten phases on the
28

outside of the ash deposits, the annualized thinning rate of Type 347H (UNS S34709) tubes was a
tolerable 0.34 mm per year (0.013” per year).
2.1.2 Process Modifications to Inhibit Superheater Corrosion
2.1.2.1 Dilution of corrosive biofuels with less corrosive fuels
The simplest way to reduce superheater corrosion caused by fuel contaminants is to dilute the corrosive
biomass with a less-corrosive fuel such as a clean coal or wood pellets. In countries where biofuel
combustion is mandated, other fuels may be co-fired to achieve this dilution. Small amounts of biomass
added to existing coal-fired boilers typically do not cause corrosion, although they may present materials
handling issues. Thus, without new policies to reduce U.S. carbon dioxide emissions and further limit
other gaseous emissions, coal is likely to retain its position as the primary fuel for U.S. power stations,
co-fired with small amounts of biomass where this is economically attractive.
Kilgallon, Simms and Oakey have reported that mixing 20% wheat straw with wood or with coal
produced flue gas compositions well within the ranges predicted for firing different coals [31]. They
concluded that adding up to 20% of biomass into a coal fuel would cause superheater corrosion rates
similar to those produced by firing 100% coal or 100% wood.
2.1.2.2 Leaching of corrosives from biofuels
Fuels that contain more alkali and chlorine release more HCl, KCl, and NaCl when they burn. Dayton
and others [32] have shown that water leaching typically removes >80% of the potassium and sodium and
>90% of the chlorine from biomass fuels. It removes smaller proportions of sulfur and phosphorus.
Therefore washing biomass fuels with water reduces or eliminates the release of corrosive alkali metal
salts and chlorides when the fuels are later burned. Bench scale measurements of the volatile inorganic
species evolved during the combustion of leached and unleached rice straw, wheat straw, switchgrass,
power plant wood fuel, fuel crop banagrass and sugarcane bagasse confirmed that leaching could mitigate
undesirable effects of biomass combustion ash.
In related research, Jensen and others [33] used water leaching to extract potassium and chlorine from
straw fuels after pyrolyzing them at 550°C (1022°F) for subsequent co-firing with coal. In this case the
primary goal was to remove potassium that would otherwise deactivate SCR catalysts used for NO
x
reduction. Potassium and residual chlorine were than leached out of the char by counter-current washing.
In later work [34], the same authors made a more detailed study of this extraction of potassium and
chlorine from the pyrolysis char. Three forms of potassium were dissolved in turn. The first 35–58%
dissolved very rapidly, followed by a slow release that was strongly influenced by particle size, water
temperature, char type and water KCl content. The last 5–10% of the potassium could not be removed by
water leaching.
2.1.2.3 Use of additives that convert chloride ash deposits to sulfates
Co-firing corrosive biomass fuels with high sulfur fuels not only dilutes the corrosive fuel but also
converts salts that would form alkali chloride fuel ash deposits into alkali sulfates. Johansson and others
studied fine fly ash particles (<1 μm) formed in a CFB boiler [35]. Adding sulfur to the biomass fuel
changed the fly ash particles from mostly KCl to mostly K SO . K SO deposits are much less corrosive
2 4 2 4
than KCl [25], primarily because of their higher melting temperature - 770°C (1418°F) compared to
1069°C (1956°F) for KCl. In related work they found that adding kaolin or co-firing with sewage sludge
also increased the concentration of coarse (>1 μm) fly ash particles and reduced the deposition rate on ash
collection probes.
29

Skog and others [25] have described the addition of SO to a 75MW waste-fired boiler at Händelö (near
2
Norrköping, Sweden) to produce reactions of the type
2KCl(s) + SO (g) + ½ O (g) + H O → K SO (s) + 2HCl(g) (1)
2 2 2 2 4
Additions of SO calculated to convert all the alkali chlorides in the superheater into alkali sulfates
2
increased the S/Cl ratio in the deposit. Although alkali chloride formation was not entirely suppressed,
the SO additions eliminated the destruction, by chromate formation, of the chromium-rich protective
2
oxide on stainless steel in tests at 550°C (1022°F). Without the SO addition, chromate formation was
2
detected even on alloy Sanicro 28. The results also indicate that the HCl vapor was less corrosive to the
superheater tubes than the KCl or NaCl deposits.
In 2002 the Swedish-based utility Vattenfall AB patented the use of reagents such as (NH ) SO ,
4 2 4
NH HSO , H SO and FeSO [36] for avoiding corrosion and fouling in boilers firing chlorine-containing
4 4 2 4 4
fuels. Most subsequent Vattenfall publications about this approach focused on results obtained with
ammonium sulfate. The system, marketed as ChlorOut® [37], uses the concentration of alkali vapors and
fine particles in the flue gases measured by an on-line surface ionization technique [38] to control the
addition of ammonium sulfate. The alkali sensor can measure concentrations as low as about 1ppb and as
high as about 10ppm. The ammonium sulfate decomposes to produce SO that converts the alkali
3
chlorides to sulfates:
(NH ) SO → SO + 2NH + H O (2)
4 2 4 3 3 2
A study by Vattenfall and others [39] exposed a range of alloys in long-term superheater probe tests in
two wood-fired boilers with and without sulfating additives. One test boiler was the 540°C (1004°F)
steam CHP unit in Nyköping and the other was a 98MW, 480°C (896°F) steam, bark-fired boiler at
Munksund, also in Sweden. The results showed that the ammonium sulfate additions reduced the KCl
levels not only in the flue gases but also in fly ash deposits on superheater tubes and specifically at the
tube/scale interface. The additives substantially reduced the deposition rates and halved the corrosion
rates of superheater materials.
An independent evaluation of the ChlorOut® technology was performed by Broström and others [40].
The tests were performed in a 96MW(thermal)/ 25MW(electricity) circulating fluidized bed (CFB) boiler
burning bark with a chlorine-containing waste. Test probes showed that spraying ammonium sulfate into
the flue gases reduced the KCl concentration from more than 15 ppm to about 2 ppm, decreased ash
deposition rates and decreased corrosion rates. When ammonium sulfate was added, the deposit
contained significantly more sulfur and almost no chlorine, confirming that the additive was sulfating KCl
to K SO .
2 4
Aho and others have studied the alkali-capturing power of aluminum and ferric sulfates in a pilot-scale
fluidized bed biomass reactor [41] and patented the use of these compounds for sulfation [42]. They note
that many other competing reactions can take place in addition to the simple sulfation of alkali chlorides
by SO released by sulfate salts. Water-soluble sulfates can decompose over a wide range of
3
temperatures and the rate at which they release SO can be catalyzed or inhibited by other species. The
3
S/Cl ratio required for complete sulfation of chloride ashes depends not only on the chloride
concentration in the ash, but also on the concentrations of species such as Ca and Mg oxides that compete
with alkali chlorides to react with the available SO and on the concentration of alkali hydroxides, which
3
can consume SO as well as convert HCl produced by sulfation reactions back to alkali chlorides [41].
3
Although a greater volume of ferric sulfate than of aluminum sulfate is required to achieve sulfation,
ferric sulfate is less expensive and more soluble in water unless the pH is lowered to increase the
30

solubility of aluminum sulfate. While ferric and aluminum sulfate additions can convert chloride fly ash
particles into less-corrosive sulfates, they do not offer the additional NO emission reduction provided by
x
ammonium sulfate which releases ammonia gas when decomposing. The sulfation reactions do not
usually have a substantial effect on SO emissions, although HCl emissions increase slightly.
2
A thermodynamic study of the effects of ammonium sulfate additions published by Becidan and others
confirmed the benefits of this treatment. Thermodynamic equilibria were used to study the primary and
interactive effects of sodium, potassium, sulfur and chlorine in municipal waste incinerators [43]. The
effectiveness of ammonium sulfate additives was studied with the same model to investigate direct and
interactive effects of alkali (Na and K) species and of trace metals that form very low melting temperature
salts (i.e. Pb and Zn).
2.1.2.4 Use of additives that convert alkali salts to silicates
Coda and others [44] studied the vaporization of chlorine species and the formation of alkali deposits
during combustion of biomass and waste in pilot-scale BFB reactors that simulated the particle residence
times in full-scale boilers. The fuels burned (softwood and bark, paper mill sludge and blends of wood
with agricultural waste or plastic waste) had low sulfur concentrations (i.e. <0.5 wt. %), but their chlorine
and potassium concentrations ranged widely (0.02-3.2 w/o for Cl and 0.07-3.1 w/o for K). Cl was found
in the fly ash samples but not in the furnace bed ash. The addition of Al-containing materials - bauxite
and fly ash from a pulverized coal plant - increased the HCl in the flue gas and reduced the concentration
of Cl in the fly ash. Al-Si-based additives such as kaolin (hydrous 40:60 wt% Al O .SiO ) reacted with
2 3 2
alkali chlorides to form alkali aluminum silicates found in coarse fly ash particles. In contrast, limestone
additions (which, after being calcined, react with SO in the boiler to form calcium sulfate) increased the
2
chlorine concentration in coarse flue gas particles.
Henriksen, Blum and Larsen studied the effects of silica and kaolinite additions on superheater corrosion
in the external ash cooler of the Grenå CFB boiler which co-fires straw and coal [13]. Probes installed in
the loop seal, which had a similar environment to that in the ash cooler, showed that this corrosion was
caused by chlorine. Corrosion rates were lower in the ash cooler than in the convective pass, probably
because most of the corrosive ash particles had been removed in the cyclone. Side stream experiments in
a pilot plant indicated that the rate at which KCl arrived at the test probe fell when silica or kaolinite was
blown in to the test chamber. Increasing the residence time to give the additives more time to react
reduced the KCl flux by two orders of magnitude. The authors quoted preliminary data suggesting that
oil-contaminated soil could provide a cheap and efficient substitute for these more expensive additives.
Davidsson, Steenari and Eskilsson studied the effects of kaolin additions to the loop seal of a 35MW CFB
boiler fired with forest residues [45] and concluded that these additions reduced superheater deposition
and corrosion. As the kaolin passed through the boiler, it removed alkali and raised the agglomeration
temperature of the bed material. The authors concluded that alkali aluminum silicates had been formed
because the additives increased the alkali concentration in the fly ash but decreased the solubility of alkali
in the fly ash. The high melting temperature of alkali silicates would make them unlikely to form sticky
deposits on superheater tubes. In a separate effect, a small portion of the kaolin remained in the furnace
bed as a thin layer on the sand particles where it reduced furnace ash agglomeration.
2.1.2.5 Discussion
-Advanced European biomass boilers use a combination of design modifications, process modifications
and corrosion-resistant alloys to maximize their steam temperature, and therefore their fuel efficiency.
This approach typically begins with a boiler design optimized for biomass fuels. Such designs can
include
31

-Include at least one empty (radiation) pass to ensure that flue gas reactions such as sulfation go to
completion and that flue gases cool to temperatures tolerable by the superheater materials. In some
boilers this cooling is achieved by installing an economizer immediately upstream of the first superheater.
-Install low temperature screen tubes immediately ahead of the superheaters where low melting
temperature ash constituents can condense
-Remove the final superheater from the convection pass to the recirculated fluidizing medium or the
recirculated ash system in a CFB boiler, or out of the boiler envelope altogether where it can be heated by
a less-corrosive fuel
-Design the superheater tube banks for easy and very rapid replacement
Other design modifications that claim success in multiple full-scale applications include collecting low
melting temperature ash constituents from the flue gas on to rarely cleaned cool tubes ahead of the
superheater and using composite superheater tubes that contain an internal insulating layer to raise their
fireside temperature above the dew point of corrosive potassium chloride in the ash.
The most profound of these developments is that of removing the final superheater from the flue gas
passage. Separating the superheater from most of the corrosive flue gases and their entrained particles
enables substantially higher steam temperatures to be achieved within the corrosion resistance of
conventional alloys. If the final superheater remains in the flue gas passage, the steam temperature must
usually be restricted to 450-470°C (842-878°F). However, if the superheater is moved to the loop seal,
the steam temperature can be raised to at least 540-580°C (1,004 to 1,076°F). This substantially increases
the boiler efficiency.
In addition to using a boiler design suitable for the biomass fuel, European practice is to make additional
efforts to reduce the corrosivity of the biomass combustion environment. Process modifications widely
used for this purpose include
-Dilute corrosive biomass fuels with less-corrosive fuels
-Co-fire corrosive biomass with a high sulfur fuel that will convert corrosive (low melting temperature)
alkali chloride deposits to (higher melting temperature) alkali sulfates
-Use sulfate-bearing additives to convert alkali chlorides to alkali sulfates
-Use silicate or aluminosilcate additives to convert corrosive alkali salts to (high melting temperature)
alkali silicates or alkali aluminum silicates that pass through the convective pass as coarse fly ash
particles.
After having used appropriate design and process modifications, the maximum steam temperature can be
set to achieve the lowest life-cycle cost of produced energy. A critical part of this decision is the choice
of alloy for the final superheater. This review of European technology shows that design and operational
modifications practiced in Europe enable biomass-fired boilers to operate with substantially higher steam
temperatures and therefore substantially higher efficiencies than U.S. biomass boilers. All these
technological advances are available for implementation in U.S. biomass boilers. Even higher steam
efficiencies might be achievable by using chemical additives to inhibit corrosion by materials recycled
through the loop seal with the fluidizing particles, e.g. by sulfating alkali chlorides and absorbing SO .
x
The most corrosion-resistant alloys for biomass superheaters are typically FeCrNi alloys containing
between 20% and 28%Cr. Although many of these alloys contain other additions, there is no coherent
theory of the alloying required to resist the combination of high temperature salt deposits and flue gases
that is found in biomass boiler superheaters. A major challenge in choosing a superheater alloy is that,
although the environment at a superheater tube surface is initially that of the first-to-arrive deposits, the
environment and temperature at the tube surface typically change as the deposits mature.
32

It is widely thought that superheater tube alloys cannot survive in contact with molten deposits.
However, although molten deposits are more corrosive than frozen deposits, increasing superheater tube
temperatures through the first melting point of fly ash deposits does not appear to produce a step increase
in corrosion rate. The corrosion rate typically begins to accelerate at temperatures significantly below the
first melting temperature.
In this section we have mentioned several biomass boilers that operate with superheater deposits so thick
that the fireside surface of their ash deposits is molten. It is important to note the presence of molten
species on the outside of a tube deposit does not imply that molten deposits are in contact with the tube
surface.
2.1.2.6 Conclusions
-Design and operational modifications practiced in Europe enable biomass-fired boilers to operate with
substantially higher steam temperatures and therefore substantially higher efficiencies than U.S. biomass
boilers. Even higher fuel efficiencies might be achievable by using chemical additives to reduce
corrosion by flue gas constituents carried through the loop seal with the fluidizing material.
-The technological improvements that enable higher energy efficiency when firing biomass fuels are
available to U.S. energy companies. The most important design advance is the removal of the final
superheater from the flue gas/ fly ash environment, which enables substantial increases in steam
temperature and consequent increases in boiler efficiency.
-Several advanced boilers are operating superheaters with molten material on the outside of the ash
deposits without experiencing excessive corrosion.
In a subsequent paper, Sharp and associates reviewed the corrosion of superheater tubes in boilers burning
biomass fuels [4]. Sharp first addressed issues in black liquor recovery boilers then he reviewed the
issues with other types of biomass-fired boilers. That work is described in the next section.
2.1.3 Superheater Corrosion Produced By Biomass Fuels
Industrial boilers could, in principle, fire renewable biomass fuels instead of fossil fuels like natural gas,
coal, and fuel oil. However, biomass fuels often contain elements such as chlorine, potassium, sodium and
sulfur that deposit in ash on the superheater tubes that heat the steam to its maximum temperature.
Because many components of these ash deposits and the surrounding flue gases are corrosive, operators
have historically limited the temperatures of biomass boiler superheater tubes substantially below those of
fossil-fuel-fired boilers to avoid accelerated corrosion. Unfortunately, lower steam temperatures reduce
the energy derived from the fuel and produce boiler efficiencies far below those of advanced fossil-fuel-
fired boilers. A previous report [3] reviewed improvements in biomass boiler design and operation
developed in European countries that signed the 1997 Kyoto Protocol. Advanced European biomass
boilers combine design modifications, process changes and corrosion-resistant alloys to achieve
substantially higher steam temperatures and efficiencies than U.S. biomass boilers. In order to gain an
understanding of tube material considerations used in designing and fabricating boilers used in Europe,
the role of corrosion-resistant alloys in increasing superheater temperatures was reviewed.
The energy extracted from a boiler fuel depends on the difference between the maximum and minimum
steam temperatures in the steam cycle. The maximum steam temperature is typically limited by the
corrosion resistance or strength of the boiler tube alloy. The minimum temperature is set by the condenser
conditions. Superheater temperatures in coal-fired boilers have historically been limited to about 565°C
(1,049°F) and condenser temperatures to about 30°C (85°F). Although this offers a theoretical maximum
fuel efficiency of about 63%, the best coal-fired power stations achieve efficiencies of only about 45%.
33

2.1.4 Energy Sources
Plant-derived biomass fuels store carbon only for months or years, unlike fossil fuels, which store carbon
for millions of years. Carbon dioxide removed from the air by the next crop of fuel plants balances the
carbon dioxide released by the burning of the previous generation of plants. This capture-and-release
cycle cannot be duplicated with fossil fuels. Although the harvesting and delivery of biomass uses a little
electricity for harvesting, baling or chipping operations and a little petroleum-based fuel for
transportation, making energy by burning recently-grown biomaterials is much more nearly carbon
neutral than making energy by burning fossil fuels.
Biomass fuels available in the US include agricultural wastes, forest and wood plant residuals, as well as
energy crops [46]. Because municipal wastes contain a significant proportion of biomass, they are often
categorized as biomass fuels also. Without the incentives and penalties established to reduce CO
2
emissions that have been enacted in Europe, US utilities continue to pursue a lowest-cost approach to
electricity generation that relies primarily on fossil fuels. Consequently, available data show that only 8%
of the total energy consumed in the US in 2010 was generated from renewable sources [47]. In contrast,
Europe generated 11.6% of its 2009 power consumption from renewables and plans to increase this to
20% by 2020.
2.1.5 Alloys Resistant to High Temperature Corrosion
It was noted above that high temperature corrosion limits the efficiency of biomass-fueled boilers. If
superheater temperatures produce unacceptably high corrosion rates on carbon steel, boiler designers turn
to alloys that form more protective oxides. Stott [48] has documented the role of common alloying
additions in high temperature alloys based on iron, nickel and cobalt. Chromium is generally the most
important of these alloying elements. It reacts with oxygen in the flue gas to form a protective oxide
(Cr O ) that provides reasonable corrosion protection in air or oxygen at temperatures up to about 900°C
2 3
(1,652°F). At higher temperatures the Cr O tends to volatilize in the presence of water vapor. Therefore
2 3
alloys designed to serve at higher temperatures often contain aluminum or silicon as well as chromium.
Such alloys protect themselves by forming Al O or SiO . Although binary Fe-Al, Ni-Al or Co-Al alloys
2 3 2
need to contain 6-12% aluminum to form continuous Al O scales, Fe-Cr alloys need less. An Fe-15% Cr
2 3
alloy can establish an Al O layer with the addition of only 3-4% aluminum. Additions of silicon to Fe-
2 3
Cr alloys form internal SiO particles that grow and coalesce into a continuous layer. For example Fe-15-
2
30%Cr-Si alloys initially form Cr O , but this gives way to an outer layer of iron oxides over an inner
2 3
Cr O scale with a healing layer of SiO at the alloy/oxide interface. Stott points out that the differential
2 3 2
expansion stresses that cause oxide spallation during thermal cycling are more severe on austenitic than
on ferritic alloys and that Al O tends to spall more than Cr O . Strengthening elements such as Ti, Mo
2 3 3 3
and Nb have little effect on the corrosion resistance of Cr O -forming alloys [48].
2 3
2.1.5.1 Corrosion of Recovery Boiler Superheater Materials
Black liquor recovery boilers generate steam from the combustion of organic materials dissolved out of
wood chips by pulping liquors. Inorganic materials in the black liquor either flow out of the furnace
bottom as a stream of molten Na S and Na CO , or are carried through the boiler as fly ash. Although the
2 2 3
most corrosive constituents of the ash are generally alkali chlorides and carbonates, it has not been
possible to develop unique rankings for recovery boiler superheater alloys because the tube surface
environment depends not only on the pulping process but also on the waste streams recycled into the
liquor system. The corrosion resistance of recovery boiler superheater tube materials typically increases
with the chromium content of the alloy. Alloys used [49] include: carbon steel (no added Cr), UNS
K11587 (1% Cr - T11), UNS K21590 (2.25% Cr steel - T22), UNS S30409 and UNS S34709 (19% Cr
34

stainless steels - Type 304H and Type 347), UNS S31000 (25% Cr - Alloy 310) and UNS N08028 (27%
Cr - Alloy 28).
Crowe and Youngblood [50] have pointed out that the ferritic steels UNS K11587 (T11) and UNS
K21590 (T22) are only useful at temperatures substantially below the first melting temperature (FMT) of
superheater ash deposits. Using higher alloys, corrosion in recovery boiler superheaters is manageable
while exit steam temperatures remain below about 450°C (842°F) [51]. Higher steam temperatures
require austenitic stainless steels. At steam temperatures close to or just above the FMT, iron-nickel-
chromium alloys such as UNS N08810 (Alloy 800H) and nickel-chromium-molybdenum alloys such as
UNS N06625 (Alloy 625) have been used [52], although the corrosion rate increases dramatically at the
FMT.
Figure 2 presents corrosion data from probe tests by Estes [53] indicating that the corrosion rate of UNS
S310009 (Alloy 310) coupons in a recovery boiler superheater increased 4- or 5-fold as a result of a 3-6
Celsius degree (5-10 Fahrenheit degree) increase in metal temperature.
As a result of the acceleration in corrosion rate that occurs near and above the FMT, most recovery boiler
operators establish steam temperature limits that keep the temperature of fireside ash deposits
comfortably below their melting point [51, 53-56]. Kish noted that all North American recovery boiler
steam temperatures are below 500°C (932°F) [57].
Because austenitic stainless steel superheater alloys would be vulnerable to waterside stress-corrosion
cracking if chloride-contaminated feedwater entered them under upset conditions, some mills have
installed composite superheater tubes with a high alloy outer layer extruded over a pressure-bearing
carbon steel inner tube. Pulp mills confident they will eliminate chloride contamination have installed
less-expensive solid tube materials like UNS S34709 (Alloy 347H).
Vakkilainen and Pohjanne [58] recently reviewed alloys to consider for recovery boiler superheaters
operating at temperatures of up to 520°C (932°F). Their candidates include UNS S34709 and S31009
(Alloys 347H and 310), UNS S32238 (Alloy AC-66), Sumitomo alloy HR2M®, UNS S31042 (Alloy
310HCbN), Nippon alloy YUS 170®, UNS 08028 (Alloy 28), Sanicro alloys 63® and 67® and
Sumitomo Super 625®. Vakkilainen and Pohjanne suggest UNS 08028 (Alloy 28) or UNS N06625
(Alloy 625) for the highest temperatures.
Although the maximum steam temperature in Scandinavian recovery boilers is now about 480°C (896°F),
Mäkipää and others [55] have suggested that 25% chromium alloys could serve at temperatures of up to
about 525°C (977°F). Their laboratory and field tests evaluated alloys such as UNS 34709 (Alloy 347H),
UNS S32238 (Alloy AC-66), UNS 08028 (Alloy 28), Sumitomo HR-11N®, UNS N06045 (Alloy 45TM),
Alloy YUS 170®, UNS N06625 (Alloy 625) and Alloy 67®. The most resistant alloys in alkali chloride
environments were nickel-based alloys like UNS N06625 (Alloy 625). Alloys containing a few percent of
molybdenum suffered localized corrosion, apparently from molten chlorides. The authors noted that,
because water vapor promotes the volatilization of chromium species from alloy surfaces, [59] the
operation of recovery boiler sootblowers may increase corrosion rates on high-chromium superheater
alloys.
Nippon Alloy MN25R® (Type 309LMoN) was developed for increased strength at high temperatures and
increased intergranular corrosion resistance in recovery boiler superheater environments [60]. It contains
25% Cr and is claimed to be suitable for temperatures of up to 540°C (1004°F) [61].
Skrifvars, Westén-Karlsson, Hupa and Salmenoja recently reported laboratory test data for 6 recovery
boiler superheater alloys [62]. These alloys UNS K21590 (T-22), UNS K90901 (T-91), the 6% Mn alloy
35

UNS S21500 (Esshete 1250®), UNS 08028 (Alloy 28), HR11N® and Alloy 63®) were pre-oxidized in
air for 24 hours at 200°C (392°F). Mixtures of Na SO , K SO and NaCl, chosen to have FMTs ranging
2 4 2 4
from 522 to 884°C (972 to 1623°F), were applied to each alloy for one-week tests at 450 to 600°C (842 to
1112°F). Pure Na SO deposits corroded only the lowest alloy UNS K21590 (T-22). However, when as
2 4
little as 0.3 w/o chlorine was added, corrosion appeared below the FMT of the synthetic ash on UNS
K21590, K90901 and S21500 (T-22, T-91 and Alloy 1250®). 1.3 w/o chlorine initiated corrosion below
the FMT on UNS 08028 (Alloy 28). Substituting 10% of the KCl with NaCl in the 0.3 w/o chlorine salt
produced much thicker corrosion products. Because the test environment did not contain water vapor,
these data are likely to underestimate corrosion in real environments where water vapor promotes the
volatilization of chromic oxide. In related work, Backman, Hupa and others [63] showed that increasing
the proportion of molten phases in salt layers of constant chloride concentration produced higher
corrosion rates both on a 1% Cr, 0.5% Mo steel and on UNS 31009 (Alloy 310).
A second paper by Skrifvars, Westén-Karlsson, Hupa and Salmenoja [64] reported that differences
between the corrosion resistance of alloys UNS K21590, S21500 and N06625 (T-22, Alloy 1250® and
Alloy 625) under synthetic alkali chloride deposits were apparent within one-week laboratory tests.
Chlorine-free Na and K salts did not corrode any of these steels. The effects of chloride additions
depended on whether or not they depressed the FMT below the surface temperature of the test sample. At
temperatures above the FMT, deposits containing Na and K chlorides corroded all the steels. Chloride-
containing salts also corroded UNS K21590 and S21500 (T-22 and Alloy 1250®) at temperatures below
the FMT. The presence of porous iron oxide deposits on the outside of the oxide layer and on salt
particles suggested that iron had volatilized from the alloy, possibly as iron chloride. At 575°C,
indications of condensed chromium and nickel oxides were also found in tests on UNS 06625 (Alloy 625)
which was the most corrosion-resistant of the alloys tested.
2.1.5.2 Summary
The corrosivity of kraft recovery boiler superheater environments varies according to the associated pulp
manufacturing process, because many of the most corrosive species arrive in waste streams recycled into
the black liquor. It has been known since the early 1980s that recovery boiler superheater tubes corrode
rapidly in contact with molten deposits and that the best-performing alloys are usually high-chromium
austenitic stainless steels and nickel-chromium-molybdenum alloys. In light of the hazards associated
with recovery boiler operation, operators typically keep the final steam temperature at least 30 Celsius (50
Fahrenheit) degrees below the FMT. Experience suggests that it is more cost-effective to raise the FMT
of the deposits by purging chlorides out of the system than to install high alloys and run with superheater
temperatures close to a lower FMT.
2.1.6 Corrosion Mechanisms in Biomass Boiler Superheater Environments
2.1.6.1 Corrosives in biomass fuels
Tillman and others [65] note that the corrosion problems caused by biomass fuels generally arise from the
chlorine and alkali metals (specifically K and Na) they contain. With the exception of wood and a handful
of other fuel crops, biomass fuels contain significantly higher concentrations of chlorine than coal. [65]
Field crops, with the exception of nut shells, pits and switchgrass, contain more chlorine than woody
materials. Tables of typical chlorine and moisture concentrations in 20 biomass fuels [66] showed that
chlorine concentrations, expressed as lb/106 Btu, ranged from 0.012 for willow, poplar and almond shells
to 0.894 for rice straw and 0.923 for corn stover. All the biomass fuels contained more chlorine than coal
samples from 9 representative US coalfields.
36

Salmenoja and Mäkelä’s overview of superheater corrosion in biomass boilers [67] also identified Cl ,
2
HCl and alkali chlorides as the dominant corrosives. Hiltunen, Barišić and Coda Zabetta [68] concluded
that alkali salts released by biomass fuels, in particularly alkali chlorides, cause superheater corrosion
both by lowering the FMT of superheater ash and by releasing chlorine when they react with sulfur
compounds to form sulfates. Alkali salts can form low melting temperature eutectics with other ash
materials or can themselves be molten on the tube surface, depending on the superheater temperature.
KCl is more corrosive than NaCl and has a lower melting temperature. As in recovery boilers, the
presence of molten phases at the tube surface causes accelerated corrosion. So biomass boiler operators
similarly keep tube temperatures well below the FMT of fireside deposits to avoid rapid corrosion. The
release of chlorine by the sulfation of ash deposits can produce active corrosion which will be discussed
later.
Pinder’s 2008 summary of materials challenges in biomass combustion [69] emphasized the value of
achieving good energy efficiency in biomass combustion. Except in Denmark, conversion efficiencies
have generally been low and steam temperatures limited because of fouling and corrosion concerns.
Pinder pointed out that even the most energy-efficient straw-burning plants in Sweden achieve conversion
efficiencies of only about 29% and are restricted to superheater temperatures of 540°C/92 bar
(1,004°F/1,334 psi), compared with current targets for coal-fired plants of 650°C/300 bar (1,202°F/4,350
psi).
Ten years of research at Chalmers University of Technology, summarized by Johansson, Skog and others,
[25,70] indicate that alloys that rely on Cr O for corrosion protection are vulnerable to failure by fluxing
2 3
and by vaporization.
2.1.6.2 Fluxing of otherwise-protective Cr O
2 3
Alkali chlorides can react with the Cr O that would otherwise protect the alloy surface by forming alkali
2 3
metal chromates:
Cr O (s) + 4KCl(s) + 2H O(g) + 3/2 O (g) → 2K CrO (s) + 4HCl(g) (3)
2 3 2 2 2 4
If the rate of this fluxing reaction exceeds the rate of supply of chromium from the bulk of the alloy, the
Cr O scale gives way to an unprotective (Fe,Cr) O spinel beneath an outer layer of Fe O [25]. The
2 3 3 4 2 3
inward penetration of chlorine-containing gases though the spinel forms FeCl , which migrates outward
2
towards the higher oxygen partial pressures at the ash/gas interface, where it decomposes to Fe O and
2 3
Cl . The Cl penetrates back through the porous oxide to form more metal chlorides at the alloy surface,
2 2
completing a cycle first called active oxidation by Lee and McNallan [71] and later studied in detail by
Grabke and co-workers [72]. The difference between the oxidizing environment at the gas/scale interface
and the reducing environment at the tube/scale interface is illustrated by experiments by Salmenoja and
Mäkelä [67]. HCl produced by biomass combustion did not corrode superheater tubes in oxidizing
environments where the tube temperature was below 600°C (1,112°F). However, in reducing (low
oxygen partial pressure) conditions, corrosion of biomass boiler superheater tubes, indicated by metal
chloride formation, began at about 450°C (842°F).
Pettersson, Svensson and Johansson [73] also showed that the KCl-induced corrosion of UNS S30400
(Type 304 stainless steel) in an O -H O environment accelerated rapidly with increasing temperature
2 2
within the range 400-600°C (752-1,112°F). At 600°C (1,112°F) the addition of KCl increased the
corrosion rate more than an order of magnitude [74]. Pettersson, Svensson and Johansson also compared
the corrosivity of KCl, K CO and K SO towards UNS S30400 (Type 304) [59]. KCl deposits caused
2 3 2 4
rapid attack in laboratory tests [75] during the first 24 hours of exposure. The corrosion products were
outward-growing sesquioxides – Fe-rich (Fe ,Cr ) O on Type 304 and mixed(Fe ,Cr ) O on UNS
0.9 0.1 2 3 0.5 0.5 2 3
37

N08028 (Alloy 28) - over inward-growing (Fe,Cr,Ni) O spinels. The formation of K CrO allowed rapid
3 4 2 4
corrosion when chromium oxides gave way to non-protective iron-rich oxides. The chlorine in the KCl
was converted to gaseous HCl. Although UNS N08028 (Alloy 28) contained a sufficient reserve of
chromium to form a healing Cr O layer where KCl deposits had been applied, Petterson and her co-
2 3
authors pointed out that the continuous supply of KCl in an operating biomass boiler would present a
much more severe challenge to this alloy [75]. Short-term thermogravimetric tests in O + H O at 600°C
2 2
(1,112°F) showed that fluxing is also produced by K CO :
2 3
½ Cr O (solid) + K CO (solid) + ¾ O (gas) → K CrO (solid) + CO (gas) (4)
2 3 2 3 2 2 4 2
The amount of K CrO formed did not account for allthe chlorides or carbonates that were introduced,
2 4
[59] suggesting that KCl and K CO may also be lost by vaporization. In the presence of water, solid
2 3
K CO vaporizes as KOH, which may itself cause corrosion.
2 3
In contrast, K SO does not react with Cr O to form K CrO [76]. This difference in reactivity is
2 4 2 3 2 4
exploited in many approaches to control superheater corrosion by increasing the molar ratio of available
sulfur to chlorine in order to convert corrosive potassium chloride to less reactive potassium sulfate:
2KCl(solid) + SO (gas) + 1/2O (gas) + H O(gas) → K SO + 2HCl(gas) (5)
2 2 2 2 4
The practical use of sulfating additions for corrosion control has been discussed in our previous paper [3].
Although the release of chlorine by sulfation reactions on the tube surface causes active corrosion where
the Cr O barrier has failed, [68] the release of HCl into the flue gas by upstream sulfation reactions is not
2 3
sufficient to cause active oxidation. Folkeson, Johansson and Svensson [77] showed that adding HCl
vapor to moist oxygen-nitrogen mixtures accelerated the oxidation of UNS S31009 (Alloy 310) at 500°C
(932°F) but did not show the concentration of chlorides at the scale/metal interface that is characteristic of
active oxidation.
Although K SO deposits did not accelerate the corrosion of UNS S30400 (Type 304) by reacting with
2 4
Cr O , K CO -K CrO and K CO -K SO eutectics have relatively low melting temperatures - as low as
2 3 2 3 2 4 2 3 2 4
788 and 658°C (1,450 and 1,216°F), respectively [59].
2.1.6.3 Vaporization of otherwise-protective Cr O
2 3
Oxide breakdown can also be caused by volatilization of Cr O . High temperatures, humid atmospheres
2 3
and rapid gas flow remove Cr O as a chromium oxy-hydroxide vapor:
2 3
Cr O (solid) + 2H O(gas) + 3/2 O (gas) → 2CrO (OH) (gas) (6)
2 3 2 2 2 2
Paul, Clark and Eckhardt reported this type of corrosion rate increase when adding 2 v/o of water vapor to
a simulated coal-fired combustion environment [78]. If the rate of volatilization of chromium exceeded
the rate of resupply from the bulk of the alloy, the Cr O scale failed and was replaced by an unprotective
2 3
(Fe,Cr) O spinel beneath an outer layer of Fe O .
3 4 2 3
Pettersson and others [75] compared the volatilization behavior of UNS N08028 (Alloy 28) and UNS
S30400 (Type 304). Both alloys formed protective, chromium-rich oxides in dry oxygen at 600°C
(1,112°F). However, adding water vapor caused rapid oxidation of UNS S30400 (Type 304), but not of
UNS 08028 (Alloy 28). The greater availability of chromium in UNS 08028 (Alloy 28) apparently
delivered chromium to the surface fast enough to maintain the protective Cr O . However, the limited
2 3
availability of chromium in UNS S30400 (Type 304) to replace Cr O lost by chromate formation or
2 3
chromic acid volatilization produced a thick layer of Fe O over an unprotective (FeCrNi) O spinel [59].
2 3 3 4
38

The non-protective spinel could be penetrated by chlorine species, and active oxidation ensued. Because
the imperfect structure in grain boundaries accelerates the delivery of reactive elements where grain
boundaries intersect an alloy surface, [75] the UNS S30400 (Type 304) corroded preferentially in the
center of surface-breaking grains.[59] This also accelerated the formation of K CrO above surface grain
2 4
boundaries in UNS N08028 (Alloy 28).
Note that, at superheater temperatures, fluxing caused by even small concentrations of KCl and K CO is
2 3
typically much more damaging than volatilization caused by environments containing oxygen and water
vapor.
2.1.7 Corrosion of Biomass Boiler Superheater Materials
Coleman, Simms, Kilgallon and Oakey[79] reported laboratory testing of potential superheater tube
materials for boilers burning fast-growing energy crops that contain high concentrations of K and Cl.
Five alloys were studied: 1% Cr steel (UNS K11597; T11), 2.25% Cr steel (UNS K40712; T23), 9% Cr
steel (UNS K90901; T91), 12% Cr steel (UNS S41000, i.e. X20CrMoV121 or Type 410), a stainless
steel, UNS S34710 (Type 347HFG) and a nickel-base alloy, UNS N06625 (Alloy 625). 1000-hour tests
were carried out at temperatures between 450 and 600°C (between 842 and 1,112°F) with synthetic gas
compositions and deposits (refreshed by re-coating) simulating biomass combustion conditions.
Corrosion was assessed by thermogravimetry and by dimensional metrology. The best performing alloy
in all the tests was the nickel-based UNS N06625 (Alloy 625). It formed a protective Cr O scale. The
2 3
iron-based Alloy UNS S34710 (Type 347HFG) also produced a Cr O -rich scale, but suffered localized
2 3
and internal corrosion in many of the exposure conditions. Alloys containing less chromium showed
much more damage. In gaseous environments, higher S/Cl ratios produced higher damage rates,
suggesting that increased amounts of SO stabilized the molten deposit (by sulfation reactions that
3
released chlorine, caused active oxidation and formed low melting temperature chloride deposits) as well
as being directly corrosive. The molten deposits increased the corrosion rates [80].
Field testing of candidate materials for biomass boiler superheaters by Mäkipää, Baxter, Sroda and Oksa
showed that whenever corrosion was found, the ash deposits were sulfated [81]. The authors concluded
that HCl released in these sulfation reactions was causing active oxidation [71].
Pinder [69] reported that UNS S34709 (Type 347H) superheater tubes in a UK straw-fired power station
need to be replaced every 5 years, but that reducing the steam temperature by 10°C (18°F) would nearly
triple their service life.
Pettersson, Flyg and Viklund [82] tested the corrosion resistance of superheater alloys in a synthetic gas
mixture established by the European PREWIN network to simulate waste incinerators. 2% and 9% Cr
steels (UNS K21590 and K90901), stainless steel UNS 30400 (Type 304) and high temperature alloy
UNS S30815 (Outokumpu Alloy 253MA®) were evaluated in 960-hour exposures at 550 and 700°C
(1,022 and 1,292°F) under KCl-K SO deposits in 13% CO , 5% O , 15% H O, 0.02% HCl environments.
2 4 2 2 2
The eutectic temperature of this salt mixture is 690°C (1,274°F). UNS S30815 (Alloy 253MA®) was the
best performer. The authors concluded that its 1.5% Si had formed a partial layer of SiO at the
2
alloy/scale interface that limited the formation of metal chloride reaction products.
Salmenoja and Mäkelä [67] surveyed ash deposits on biomass boiler superheater tubes. These deposits
had FMTs as low as 530°C (986°F). Molten phases produced superheater corrosion rates exceeding
10mm/year (nearly 0.4” per year) [83].
Many modern biomass boilers use CFB designs in which the superheater is located in the recirculated
fluidizing medium. Our previous paper [3] noted that this reduces the exposure of the superheater to alkali
39

metal salts and corrosive flue gases. Nafari and Nylund [17] measured erosion-corrosion of loop seal
superheater tubes in a 30MW CFB boiler fired with coal and forest residues at Nässjö, Sweden. Thinning
rates increased with tube temperature. Steam inlet and outlet temperatures were 470 and 540°C (878 and
1,004°F), and the authors suggested that the tube surface temperatures would be 50 to 100 Celsius
degrees (90 to 180 Fahrenheit degrees) higher than these values. The corrosion products consisted of an
inner layer of Cr and Fe oxides beneath an outer Fe-rich oxide. Chloride was present at the alloy/scale
interface, with K and S. Average material losses on UNS S21500 (Alloy 1250®) and on UNS S34709
(Type 347H) were comparable and were slightly greater than on UNS S32238 (Alloy AC-66), although
the UNS S32238 showed more severe internal oxidation.
Later work by the same authors presented additional results from the same superheater with tube
temperatures between 510 and 550°C (950 and 1,022°F) [18]. The loop seal ash contained 13% Ca, 9%
K, 0.9% Na, 800 ppm sulfate and 100 ppm chloride. Even the uncoated alloys suffered little corrosion
during boiler operation. The fact that the degradation was no worse after two firing seasons than after one
indicated that corrosion, rather than erosion, was the dominant deterioration mechanism. Although
recirculated fluidizing particles are abrasive, their velocity is low and erosion is not normally a problem.
The thickest oxides, on a 9% Cr alloy, were only about 150μm (0.006”) thick after about 7 months in
service. Austenitic steels suffered some internal oxidation and grain boundary attack. Although some
coatings delaminated, 8 of the 17 coatings tested were unaffected by the exposure.
2.1.7.1 Protective coatings
Both robotically-applied weld overlay and thermally-sprayed coatings have been used to protect biomass
boiler superheater tubes from corrosion. The most widely used overlay material in waste-to-energy
(WTE) boilers is UNS N06625 (Alloy 625). The maximum service temperatures recommended for these
coatings range from 400-420°C (750-790°F) [84] to 540°C (1004°F) [85]. Pinder noted that UNS
N06625 (Alloy 625) overlay provided the best protection in a boiler firing straw and waste wood where
high alloy austenitic steels suffered severe localized and internal attack.[69] For recovery boiler
environments, Vakkilainen and Pohjanne have suggested applying weld overlay coatings of UNS S31009
(Type 310) or UNS N06052 (Alloy 52) [58].
With regard to thermally-sprayed coatings, Uuistalo and others reported that a high-chromium, nickel-
based HVOF coating (Ni-57CrMoBSi) showed good resistance in an erosion-corrosion rig simulating a
CFB combustor even when chlorides were added [86]. Chromized coatings and chromium carbide
coatings did not survive. Because large platelets in thermal spray coatings are difficult to dislodge by
erosive particles, the authors concluded that HVOF thermal spray coatings for these applications ought to
be dense with a large splat size.
Tuurma and a large group of co-workers [87] recently evaluated the use of corrosion-resistant coatings in
a biomass boiler. They found no visible corrosion on thermally sprayed HVOF coatings containing 16%,
25% and 27% Cr after one year’s service on superheater tubes in a WTE boiler. Like Uuistalo, Tuurma
concluded that the performance of these coatings depends on their application quality, coating adhesion
and coating density. Amorphous coatings and fused-in-place coatings cracked before the test was
complete.
2.1.7.2 Corrosive impurities in demolition wood
Demolition wood is a low-cost biomass fuel, but it sometimes contains lead and/or zinc impurities that
form extremely low melting temperature ashes which cause rapid corrosion on low alloy tube materials.
Much of the research on corrosion by lead and zinc impurities has been done for municipal waste
incinerators. Spiegel [88] showed that, if HCl is present in the flue gases, temperatures above about
40

400°C (752°F) can convert ZnSO and PbSO to volatile chlorides even if the partial pressure of SO is
4 4 2
relatively high. These volatile chlorides condense on fly ash particles and on superheater tubes, forming
molten or sticky deposits or eutectics like KCl-ZnCl . Spiegel reported that these molten chloride
2
eutectics caused rapid corrosion on UNS K21590 (T-22) tubes [88]. In contrast, UNS S32238 (Alloy
AC-66) formed PbCrO and ZnCr O at 600°C, although the presence of an inner spinel layer and
4 2 4
chlorides at the alloy/scale interface indicated active oxidation. However, when the temperature was
reduced to 500°C (932°F), its corrosion rate was only two or three times higher than in a simple oxidizing
environment.
Otero and others [89] simulated a waste incineration environment with a molten eutectic of 52% PbCl -
2
48% KCl. The corrosion rate on UNS N09910 (Incoloy 800) decreased with time, suggesting that a
protective reaction product was thickening, but the rate on a 12CrMoV ferritic steel did not [90].
Li, Niu and Wu [91] described laboratory studies of the corrosion of several Fe-based alloys and of pure
Fe, Cr and Ni at 450°C (842°F) beneath ZnCl -KCl deposits in flowing O . Alloys tested included carbon
2 2
steel, a 5CrMo steel (UNS K90901, T91), UNS S31009 (Type 310) and Kubota alloy HP®. Adding a
55/45 (mole fraction) mixture of ZnCl /KCl (melting temperature only 250°C (482°F)) accelerated the
2
corrosion of all these alloys by forming thick and porous oxides enriched in chlorine at the alloy/scale
interface. Corrosion resistance increased with the nickel content of the alloy and decreased with the
chromium content because high-Cr alloys produced less-adherent corrosion products. The authors [91]
suggested that the molten salts had fluxed the oxide (i.e. reacted with Cr O to form ZnCr O and FeCl ).
2 3 2 4 2
They also pointed out that loss of ZnCl from the molten salt eutectic by volatilization of ZnCl or by
2 2
ZnCr O formation could raise the FMT above the experimental temperature. Thus, unless a fuel supply
2 4
continuously supplied ZnCl to a tube surface, the ash would gradually change from ZnCl to KCl, raising
2 2
the FMT and slowing the corrosion.
Pan, Zeng and Niu [92] later studied the corrosion of 9% and 11% Cr steels and UNS S30400 (Type 304)
stainless steel under ZnCl -KCl deposits at 400-500°C (752-932°C) in a reducing CO -2%H -0.5%HCl
2 2 2
gas mixture. This work and a subsequent study [93] confirmed that alloys containing more chromium
showed greater corrosion resistance in reducing environments. However, even UNS S30400 (Type 304)
had unacceptable corrosion resistance under a ZnCl -KCl deposit at temperatures between 400 and 500°C
2
(752 and 932°F), and showed active oxidation.
Bankiewicz, Yrjas and Hupa [94] studied the performance of UNS K21590 (T-22), UNS S34709 (Type
347) and UNS N08028 (Alloy 28) in synthetic salt mixtures simulating deposits in furnaces burning
wastes containing zinc (K SO , K SO -KCl and K SO -ZnCl ). The FMT of the K SO -ZnCl salt
2 4 2 4 2 4 2 2 4 2
mixtures was about 400°C (752°F) and the test temperatures were between 350 and 500°C (between 662
and 932°C). UNS N08028 (Alloy 28) performed well, except at 600°C (1,112°F) which produced oxide
thicknesses of 12-30 μm (0.0005-0.001”) on UNS S34709 and N08028 (Type 347 and Alloy 28). Tests
in chloride salts produced active oxidation, and pitting attack on N08028 (Alloy 28).
Related corrosion studies by Ruh and Spiegel [95] investigated the corrosion of Fe, Ni and Cr beneath a
eutectic mixture of 50% KCl, 50% ZnCl . Iron chloride is soluble in this eutectic, so FeCl diffuses
2 2
through the molten deposit to be oxidized at the deposit/gas interface in the active oxidation cycle. In
contrast, nickel and chromium have very limited solubility in the molten eutectic. Because chromium
dissolves in the melt as chromate, it would appear that superheater tube materials in boilers burning fuels
that can contain zinc should not rely on chromium to form protective oxides, but on aluminum or silicon
instead [95].
Li and Spiegel [96] studied the performance of Fe-Al and Ni-Al alloys in simulated Zn-contaminated
wood environments at 400 to 450°C (752 to 842°F). Corrosion resistance increased with increasing Al
41

content in binary Fe-Al alloys containing 10 to 45% Al and in Ni-Al alloys. The alloy that showed the
least mass loss was a 50%Ni-50%Al alloy. Although Al-free materials corroded by an oxide fluxing
mechanism, alloys of intermediate Al content reacted with ZnCl to form volatile AlCl (melting
2 3
temperature only 178°C (352°F)) and metallic Zn. This metallic Zn reacted with the Al-rich surface of
45% Al alloys to form an Al-Zn eutectic.
2.1.7.3 Modeling of superheater corrosion rates in biomass boilers
Two European boiler suppliers and a UK consortium have developed models to predict fouling and
corrosion in biomass boilers. These programs are used not only to select tube materials for new boilers
but also to predict where corrosion is likely to appear first in a particular boiler firing a particular fuel
mixture.
Foster Wheeler’s model [97,98] is designed to be used by experts as an advisory tool. Its first module
evaluates the probability of agglomeration and fouling promoted by the formation of low melting
temperature compounds by alkali (Na and K) and alkaline earth (Ca and Mg) salts and inhibited by the
removal of these compounds by reaction with kaolinate materials. The second module assesses the release
of chlorine from the fuel and its capture by sulfur oxides or kaolinite minerals. If the fouling tendency is
low, corrosion rates will be low, but if the fouling tendency is high, corrosion rates will depend on how
much chlorine is released by the fuel. The corrosion module uses fuzzy logic to estimate the corrosion
rate produced by a particular fuel on a particular alloy at a particular temperature using a data base of over
10,000 fuel materials and over 1,000 operational tests with austenitic and nickel-based tube materials in
about 150 CFB boilers. An example of the use of this model cited by Coda Zabetta and others [97,98]
refers to a boiler firing mixtures of coal, rice husks and eucalyptus bark. Corrosion rates estimated for
two extreme fuel mixtures (a low proportion of rice husks and high proportion of eucalyptus bark and the
reverse ratio) correlated reasonably well with tube thinning rates measured in an operating boiler.
Metso Power has developed its own predictive model. Enestam, Niemi and Mäkelä report that this tool,
called STEAMAX, [99] estimates the corrosivity of fuel mixtures and recommends maximum steam
temperatures for candidate tube materials. From the analysis of a proposed fuel or fuel mixture,
thermochemical equilibrium calculations predict the melting behavior of the fuel ash. Species considered
include C, H, N, O, S, Cl, Ca, Mg, Na, K, Al, Si, Fe, P, Pb and Zn, 12 solid compounds, 2 solid solutions,
2 liquid solutions and a gas phase. As in the Foster Wheeler program, corrosivity is estimated from the
amount of chlorine in the flue gas at different temperatures and boiler locations. The maximum allowable
temperature for given tube alloys is estimated from an empirical database based on superheater data from
20 biomass-fuelled and black liquor recovery boilers. The risk of corrosion by a molten deposit is
estimated from the difference between the tube surface temperature and the FMT of the ash. The program
recommends a maximum operating temperature for individual candidate alloys, considering solid
chlorine-induced corrosion, gas phase chlorine-induced corrosion and molten phase corrosion.
UK models of fireside corrosion in coal-fired boilers have been extended by Kilgallon, Simms and Oakey
to predict rates of corrosion in biomass-fired boilers [31]. Their model applies to UNS S41000 (i.e. Alloy
X20CrMoV121 - Type 410), UNS S34710 (Type 347HFG) and UNS N06625 (Alloy 625) in superheater
conditions. The fuel is coal with up to 20% of biomass. Data from a matrix of 1,000 hour corrosion tests
were used to develop an empirical model. The tests were made in various mixtures of KCl, K SO and
2 4
pulverized coal fly ash based on deposit compositions found in Danish biomass-fuelled and co-fired
boilers. The deposits were re-applied to the coupons every 100 hours. The gas atmospheres consisted of
more and less oxidizing mixtures of O , CO , H O, CO, SO and HCl. The model shows effects of deposit
2 2 2 2
composition (K+, Cl- and SO 2-), gas composition (SO and HCl) and the test temperature 560 or 600°C
4 x
(1,040 or 1,112°F). Measured corrosion damage correlated quite well with predicted corrosion damage,
although the model was not verified using a data set different to that on which it had been trained.
42

2.1.7.4 Summary
Despite the economic benefits of increased superheater temperatures in biomass boilers, little systematic
research has been done to indicate which alloys would be the best choice for extreme steam conditions.
The corrosion resistance of superheater alloys in biomass boilers depends on their maintaining a
protective surface layer of Cr O . If this oxide is fluxed by alkali salts, or volatilized, faster that it can be
2 3
re-formed by chromium diffusing from the bulk of the alloy, the resulting non-protective oxides will be
penetrated by chlorine species that cause further acceleration of the corrosion rate by active oxidation.
Iron-based alloys containing at least 25%Cr and nickel-based alloys typically perform best and additions
of silicon have been shown to be beneficial. Some alloys that have performed well also contain additions
of rare earth metals.
Alkali salts are generally the most aggressive components in biomass fuels. They can cause corrosion
directly by fluxing the Cr O and they can reduce the ash FMT, either causing agglomeration and fouling
2 3
or forming corrosive molten deposits. Lead and zinc impurities in demolition wood are very corrosive,
primarily because they form very low melting temperature ash components.
Even where corrosion data are available, their use to select cost-effective alloys for superheater tubes in
particular boilers is difficult for at least three reasons. First, the operator might decide to burn a different
fuel years after the tube materials were chosen. Second, although laboratory test data may be available,
inconsistencies between methods used by different laboratories make it difficult to develop general
conclusions from different data sets. Third, it is difficult to make quantitative comparisons of field data
from different sources because boiler tube environments and temperatures are rarely well-characterized.
Corrosion of Superheater Materials in Boilers Co-Firing Biomass with Coal
In the absence of policies to promote the use of renewable fuels for power generation, coal will remain
the lowest cost, easy-to-burn fuel for US utilities. Corrosion problems are manageable at steam
temperatures that offer conversion efficiencies up to 50%. Coals containing corrosive contaminants such
as alkali chlorides and sulfates are diluted with less problematic fuels to avoid corrosion problems.1 As
superheater temperatures are increased to maximize energy recovery from coal fuels, it appears that high
temperature creep limits may be reached before corrosion limits are reached. Wood is co-fired with coal
either to dilute corrosive impurities in the coal or to take advantage of incentives that promote the use of
renewable fuels.
Co-firing wood with coal
The issues involved when converting a large coal-burning power plant to co-fire biomass have been
reviewed by Fuller, Maier and Scheffknecht.[100] This review includes a detailed case study of a 250
MW coal-fired plant in Ghent, Belgium that modified its fuel milling system and burner locations to co-
fire up to 100% wood pellets. The wood firing did not produce substantial operational problems.
Corrosion tests of candidate alloys at metal temperatures between 640 and 670°C (1,184 and 1,238°F) in
Swedish boilers co-firing biomass with coal and firing 100% biomass have been reported by Henderson
and others [101]. Corrosion rates were generally higher when burning 100% biomass than when co-firing
coal with the biomass. Alloys with the highest chromium content generally showed the lowest corrosion
rates, although there were some exceptions. For example, the manganese additions in UNS S21500 (Alloy
1250®) seemed particularly beneficial.
Co-firing straw with coal
In Denmark, straw is widely burned as an energy fuel in large and efficient boilers. Frandsen has made
detailed studies of the combustion chemistry of straw co-fired with coal.[102,103] Although straw fuels
contain high concentrations of chlorine, Tillman and his co-authors reported [65] that co-firing 10% of
43

straw in a Danish power station produced little, if any, corrosion attributable to chlorine. At 20% co-
firing, the corrosion rate increased by a factor of 2 or 3, but was still considered manageable. The authors
suggested that good mixing and careful deposit control might permit higher straw substitution in coal-
fired plants.
Anderson and others [104] described ash formation in a 150 MW pulverized coal utility boiler converted
to burn 20% (on an energy basis) of straw. Fe-rich deposits formed during coal combustion gave way to
Ca- and Si-rich deposits when straw was co-fired. Because of good mixing during the combustion
processes, no chlorine was found in combustion deposits, indicating that active oxidation had been
avoided. Potassium from the straw reacted with Al silicates to form harmless, high-melting-temperature
potassium aluminum silicates.
To simulate superheater conditions in straw-fired boilers, Nielsen, Frandsen and Dam-Johansen [105]
coated ferritic boiler tubes and UNS S34709 (Type 347) tubes with synthetic (KCl and/or K SO ) and real
2 4
deposits, and exposed them for between 1 week and 5 months under a synthetic flue gas at 550°C.
Sulfation reactions released Cl and HCl, causing rapid active oxidation of the tubes. Also, KCl formed a
2
low melting temperature eutectic with K SO and various iron compounds at the tube surface that caused
2 4
rapid corrosion when the tube surface temperature exceeded the FMT.
Liu, Maier and Hein [106] studied the kinetics of fireside corrosion in ashes formed from the combustion
of straw, wood and lignite coals in a 0.5 MW pulverized fuel boiler. The test gas environment contained
HCl, H O, SO , O and N . A ferritic 2¼% Cr alloy (UNS K30736, T-24), a ferritic-martensitic 12% Cr
2 2 2 2
alloy (UNS K91271, T122) and an austenitic 20% Cr-25% Ni alloy (UNS S31009, Nippon NF709®) all
suffered active oxidation that began as pitting corrosion. The corrosion morphologies produced on
ferritic, martensitic and austenitic boiler steels were described in a second paper [107]. The low Cr
content of the ferritic steels allowed the formation of thick and porous corrosion products. The 12% Cr
martensitic steel suffered isolated corrosion in alloy grain centers. The 20% Cr austenitic stainless steel
suffered deep grain boundary attack under chlorine-rich deposits at 650°C (1,202°F). The morphology of
corrosion was related to carbide attack. Carbides in the austenitic steel were segregated to the grain
boundaries, while carbides in the martensitic steel were finely-dispersed.
Summary
Co-firing up to about 20% of clean wood in a pulverized coal utility boiler offers benefits of renewable
power without significant operational or corrosion challenges. Although straw contains high
concentrations of chlorine, 10 or 20% of straw can be co-fired with coal with manageable increases in
corrosion rate. Higher substitutions of corrosive fuels, such as rice straw, corn stover, or demolition wood
introduce severe corrosion problems that are typically addressed by chemical additives or by lowering
steam temperatures [3].
44

2.2 LABORATORY CORROSION STUDIES
2.2.1 Introduction
Biomass is increasingly looked on as a cost-effective, environmentally friendly alternative to coal and
petroleum-based fuels in the generation of energy. However, relative to coal and fuel oils, biomass-based
fuels are inhomogeneous and they also contain significant impurities, such as chlorides, alkali metals and
heavy metals that deposit on heat transfer surfaces. While these deposits may reduce the overall energy
efficiency of the boiler, their principal effect is to cause rapid corrosion of heat transfer surfaces that
approach, or exceed, the first melting point of the deposits. As a consequence, boilers burning biomass
have largely been limited to operating with superheater steam temperatures of less than 510°C (950°F)
and steam pressures of less than 11 MPa (1600 psi). The bulk of existing biomass boilers in North
America operate at substantially lower steam temperatures and pressures, particularly those utilized as
waste utility boilers. A laboratory-based program was designed to evaluate candidate alloys for
superheaters operating temperatures substantially higher than currently used in practice for biomass and
chemical recovery boilers.
2.2.2 Experimental Procedure
2.2.2.1 Overview
A test matrix was developed to evaluate materials in simulated superheater deposit environments based on
the analysis of deposits from the three operating boilers used in the program – one recovery boiler and
two biomass-fired boilers. A total of 25 tests were completed over the course of the program, ranging in
length from 100 to 1000 hours (Table 1). Complete experimental details can be obtained from the final
program report [108] and a recent publication [109]; what follows is a brief synopsis of the important
details.
Table 1. The test matrix for the laboratory program. Cover gas for all experiments
0B
contained 5%O , 10%CO , 20%H O, bal. N . Makeup of Alloy Sets is shown in Table II
2 2 2 2
Simulated Deposits
RB PB1 PB2
Hours 510°C 530°C 625°C 650°C 650°C
Alloy Set 1 100 T1 - T5 T9 T13
200 T2 - T6 T10 T14
500 T3 - T7 T11 T15
1000 T4 T17 T8 T12 T16
Alloy Set 2 1000 T2 0 T2 4 T2 1 T2 2 T2 3
Alloy Set 3 1000 T2 7* T2 8* T2 9*
*cover gas for these tests included 50 ppm SO
2
2.2.2.2 Test temperatures
The principal established for selecting the test temperatures was to set a target for metal temperature of
100 C° higher than the current maximum operating superheated steam temperature for the type of boiler.
This was anticipated to provide a challenging, but realistic stretch target for alloys and new boiler design.
45

Since tube surface temperatures are higher than the steam temperature in service, this implies less than
100 C° increase in steam temperature.
In the case of the recovery boiler, a very few boilers world-wide operate with superheater steam
temperatures of 525°C, and so the maximum test temperature was chosen to be 625 °C. Additional tests
were conducted at 510°C – a temperature below the first melting temperature (FMT) of the synthetic
deposit, and 530°C – just above the FMT of the deposit. Some European wood-fired boilers operate with
550°C superheated steam [3], so the maximum test temperature for those tests was chosen to be 650°C.
The FMT for the bark-fired power boiler deposits was greater than 700°C. This is much higher
temperature than the boilers could reasonably be expected to operate, even during upset conditions.
Consequently, no tests were carried out at the FMT of the biomass boiler deposits.
2.2.2.3 Deposit chemistry
The synthetic salts used for the bark-fired boiler tests were based on analyses of deposits from air-cooled
probes installed in the model biomass-fired boilers [110]. One was considered to be very aggressive, with
high levels of chloride and potassium, while the other was representative of a much cleaner fuel. The
recovery boiler salt composition was tailored to provide a salt with a FMT of 525°C. It is the same as that
used in previous work by FPInnovations and was based on analyses of superheater deposits in several
boilers, including the recovery boiler from the pulp mill used as the host for the long-term corrosion probe
work [110]. Figure 16 shows the composition of the simulated deposits as elemental mole fraction.
Batches of the salts were made in bulk using ACS reagent grade salts when available. The mixtures of
compounds were placed into a porcelain milling jar and tumbled with high purity alumina balls for 45-60
minutes. The resultant powder was passed through a 100 mesh screen and the FMT checked by
Differential Thermal Analysis (DTA) before being accepted for use.
0.30
0.25
0.20
0.15
0.10
0.05
0.00
Cl S Ca Si K Na Al Mg P Mn
Fig. 16. Graphic representation of the three salt compositions used in this work.
2.2.2.5 Cover gas composition
The gas mixture used for all but three tests was 5 vol% O , 10 vol% CO and 20 vol% H O. The balance
2 2 2
was N . A small amount of SO (50 ppm) was added to the cover gas for the final three tests. The flow of
2 2
46
noitcarF
eloM
RECOVERY BOILER POWER BOILER 1 (Low Cl-) POWER BOILER 2 (High Cl-)
Mixture Components

each gas, except for water vapour, was controlled by a mass flow controller (MFC). The total of 200
standard cm3 produced a linear flow rate of 5 cm/m through the furnace tube. The accuracy of the
controllers was ±3-5% of the setpoint, depending on the gas and capacity of the MFC. The flow of
distilled water was controlled by a precision peristaltic pump, and the water was added directly into the
gas inlet end of the furnace tubes. Tests showed that the water vaporized before reaching the tube wall.
The water flow varied as the pump tubes aged and had to be monitored daily and adjusted on occasion.
Analysis of the daily water usage data showed the volume % H O normally ranged between ±5 vol% of
2
the setpoint.
2.2.2.6 Alloys
The choice of alloys was based on consultations with boiler manufacturers and alloy suppliers
participating in this project as industrial partners, as well as consideration of the literature and experience
with these alloys in other types of service. The alloys are listed in Table 2 by Alloy Set – each set being
the alloys exposed together in a single test. Nominal composition of the alloys is shown in Table 3, along
with the single letter code adopted for use in all documentation.
Table 2. Alloys used in each alloy set. Due to limited space for data in tables and graphs, codes
1B
are used throughout the report to represent the alloys
Code Alloy Alloy Set 1 Alloy Set 2 Alloy Set 3
A Esshete 1250 X X
B 310H X X X
C Sanicro 28 X
D HR120 X X X
E 602CA X X
EP 602CA pre-oxidized X X
F HR214 X
FP HR214 pre-oxidized X
G A33 X
H AC66 X X
I HR160 X X
J A59 X
K A690 X X
Peg coupons were produced from each alloy with dimensions 25 mm long by 5 mm diameter, with a 0.4
to 1.6 micron Ra ground finish. A notch was cut in one or both ends of each peg coupon to act as an
indicator of coupon orientation relative to the direction of gas flow in the furnace. The coupons were
cleaned and dried with blowing hot air. The diameter of each peg coupon was measured with a
micrometer (+2.5 micron) at three points around either end and in the middle of the cylinder. These
measurements were averaged for each location and used respectively as the “before exposure” diameters
during post exposure analysis. The peg coupons were stored in plastic containers until use.
2.2.2.7 Exposures
Peg coupons were placed in alumina crucibles and synthetic salts packed around the circumference
(Figure 17). The pegs were taller than the crucibles, and hence permitted exposure of each specimen to
both the gas phase within the furnace (including corrosive vapours) and to coverage by a bed of synthetic
salt. Twelve crucibles at a time (with at least two of each alloy) were placed onto an alumina “D” support
47

platform, and placed in the centre of a horizontal tube furnace. Coupon orientation on the “D” was noted
and remained consistent from test to test. More alloys were evaluated than space allowed in a single test,
so sets of coupons were independently exposed to the same test conditions in some cases. Once the
coupons were sealed in the furnace under flowing nitrogen, the temperature was ramped slowly to the
Table 3: Nominal composition of alloys evaluated in the test program
48

setpoint. When it was reached, the test gases and water were introduced into the furnace. At the
conclusion, the coupons were allowed to cool in the furnace with flowing nitrogen as a cover gas.
2.2.2.8 Analysis
Coupons were photographed immediately on removal from the furnace, then carefully pried from the
crucible with the salt layer as intact as possible. Six coupons at a time were fitted to a jig, and embedded
in an epoxy metallographic mount for sectioning and cross-sectional polishing (Figure 18). Each mount
was sectioned at a point above and below the level of the salts in the crucible. Sections were then dry-
polished to a 3 micron diamond finish and the surface of each coupon photographed at 10X magnification
in an automated Zeiss AxioVision microscope. In total, more than 350 coupons were exposed in the test
program – leaving some 700 surfaces to analyze. For coupons with more than 20 microns of corrosion, a
customized image analysis program was used to segment the coupon into 24 arcs, and measure both the
maximum metal loss and total-affected-metal (TAM) in each arc (Figure 19). Metal loss was determined
at the interface between the scale and sound metal, while the TAM was defined as the average of the
deepest visible penetration of corrosion into the interior of the coupon on the 24 arcs. The accuracy of the
measurement was estimated to be ±3 microns.
Fig. 17. Alloy Set 1 laid out in preparation for insertion to a furnace, showing the reproducibility of the initial
salt packing and surface height. The pre-oxidized coupons in the third and last rows from the right are
darker than the remaining as ground coupons. Blank “guard” pots placed at the gas inlet are also visible.
Fig. 18. Six coupons embedded in epoxy with their support pins. The mount on the right has not been
machined square yet. The mount on the left has been dry sectioned.
2.2.3 Results and Discussion
2.2.3.1 Overview
49

An example of the general appearance of the coupons after exposure is shown in Figure 20. These
coupons were exposed to the recovery boiler salts at 625 °C. Yellowing at the surface of the salts was
observed in many tests, but to a far greater extent in the recovery boiler salts. EDX analysis of yellow and
white salts confirmed that the yellow color was associated with chromium. Sodium chromate (Na CrO )
2 4
is an intense yellow salt that appears the most likely to have been formed. On several occasions, and for
more than one alloy, it was noted that when one of a pair of coupons within a given test had corroded
significantly more than the other, the salts had remained white for the corroded coupon and had yellowed
for the more resistant.
The complex test environment presented many experimental challenges, both in the set up and operation,
as well as for the analyses of the coupons afterwards. Throughout the test program, steps and checks were
put in place to determine how consistent conditions were from test to test, and to enable data to be
compared and normalized across tests. This was achieved by putting two baseline coupons of S31009
(alloy B) in the same locations of the furnace in every test, exposing duplicate coupons of every alloy, and
duplicating some alloys (S31009 (alloy B), N06025 pre-oxidized (alloy E), S21500(alloy A)) between
identical tests.
Fig. 19. A mosaic image of a cross-section after analysis. Inset shows top right corner in more detail. The
outer red circle is the original circumference of the coupon. The green lines indicate the depth measured for
metal loss, and the blue lines indicate the total affected metal measurement for each of the 24 arcs around the
circumference. The average of the 24 total affected metal measurements is defined as the TAM of the coupon.
50

It is clear from an examination of the data that conditions within the furnaces were not always identical,
and neither were conditions in duplicate tests. Nonetheless, the data proved to be reasonably consistent
within, as well as between tests. A few tests produced highly variable data that was almost certainly
caused by artifacts in the test environment. The stochastic nature of corrosion was also demonstrated as
greater variability was found in the shorter-term tests due to the randomness of initiation events on the
coupons. Results in the longer-term tests were more uniform.
500 hr
Fig. 20. Shows variation with salt color relating to corrosion of the coupon. Red circles indicate coupons of
pre-oxidized HR214 (Alloy FP) in RB salts at 625 °C. Note that the only Alloy F coupon not to show
substantial spalling is the one with the yellow-shaded salt.
A total of fifty S31009 (alloy B) coupons were exposed over the entire program, giving 100 sections to be
analyzed (half in the vapour phase and half under-deposit). Data was analysed from the 50 individual
S31009 sections for which the TAM was greater than 25 microns [108]. The standard deviation of the 24
TAM measurements around the circumference as a percent of their average was calculated for each
coupon. It ranged from 7% to 62% above the salts with an average of 15%, and from 5% to 30% below
the salts with an average of 18%. The overall average of the above for S31009 is 16%.
For the balance of the alloys, the standard deviation for any given set of measurements in duplicate tests
fell between 15 and 25% of the average TAM for the alloy, consistent with the S31009 result. Only three
materials fell outside of this range – those with the most severe corrosion and those with the least
corrosion (Table 4).
2.2.3.2 Power Boiler I (PB1) tests
The PB1 salt was representative of deposits produced by clean, uncontaminated fuel. There was minimal
corrosion on all coupons exposed to this salt, even for tests that lasted 1000 hours. The average TAM was
far less than 25 microns for all coupons.
51

2.2.3.3 Power Boiler 2 (PB2) tests
The PB2 salt was representative of deposits produced by fuel that is highly contaminated with chloride.
Even so, the depths of corrosive attack on all coupons were much less than 25 microns after 100 hours.
Only coupons from test exposures 200 hours and longer were subjected to the full standard analysis.
Corrosion as a function of time is shown in Figure 21 while results for the 1000 hour tests are shown in
Figure 22, plotted in order of increasing nickel content in the alloys. The most extensive corrosion in
these tests occurred underneath the layer of salt; there was very little corrosion above the salt layer. There
is also a clear correlation between increased resistance to corrosion and greater nickel content of the alloy.
Conversely, there was no correlation when the same data was plotted as a function of chromium content.
The results from the test conducted at 500 °C appear anomalous and a review of the data showed higher
than average variation in TAM on several coupons. No reason for this variation was discovered.
Table 4. Standard deviation in average TAM for alloys for all the test environments. The data is
2B
separated into Vapor Phase and Under-Deposit results and sorted by the average of those results
Std Dev as % of Average TAM
Code Alloy Vapour Phase Under-Deposit Average
H AC66 14% 17% 16%
B 310H 18% 14% 16%
C San28 18% 20% 19%
A Esshete 1250 24% 20% 22%
J A59 - 22% 22%
D HR120 24% 24% 24%
K A690 26% 23% 25%
EP 602CA pre-oxidized 24% 26% 25%
E 602CA 34% 32% 32%
F HR214 38% 28% 33%
FP HR214 pre-oxidized 42% 29% 33%
I HR160 29% 38% 34%
Average StdDev%: 26% 24%
2.2.3.4 Recovery boiler tests
Negligible corrosion was observed on the alloys in tests conducted at 510°C – the greatest TAM
measured was only 17 microns for N06025 (alloy E). This temperature is below the FMT of the salt
deposits. More substantial corrosion was observed at both higher temperatures, and two alloys completely
disintegrated in the 1000 hour test at 625°C. These were N07214 (alloy F) and N06059 (alloy I). Data for
the 1000 hr tests at 625 °C is shown in Figure 23. The correlation between corrosion and nickel content is
not apparent in these tests; nor does the corrosion correlate with chromium content of the alloys. Of
significance in these tests was the observation that corrosion in the gas phase was nearly as severe as
underneath the salt deposits. Especially in the vapour phase, internal penetration accounted for a larger
proportion of the TAM. A measureable increase in corrosion was noted for many of the alloys when SO
2
was added to the cover gas (Figures 24 and 25).
52

ABOVE SALTS BELOW SALTS
Fig. 21. Variation of average TAM with time in PB2 salts at 650 °C (T14, T15, T16), in microns.
ABOVE SALTS BELOW SALTS
500
450
400
350
300
250
200
150
100
50
0
A B C G H I D J K E EP F FP
Fig. 22. Test data from alloys exposed to PB2 salts for 1000 hrs at 650 °C. Alloys are listed in order of
increasing nickel content left to right with the last four on the right being the alumina formers (E, EP, F, FP).
Metal loss is blue portion of bar, TAM is green portion of bar.
53
)snorcim(
noisorroC
500
450
400
350
300
250
200
150
100
50
0
A B C G H I D J K E EP F FP
Avg Avg Metal Loss Internal
)snorcim(
noisorroC
Avg Avg Metal Loss Internal

ABOVE SALTS BELOW SALTS
500
450
400
350
300
250
200
150
100
50
0
A B C G H I D J K E EP F FP
Fig. 23. Test data from alloys exposed to RB salts for 1000 hrs at 625°C. Metal loss is blue portion of
bar, TAM is red portion of bar. The alloys are listed in order of increasing nickel content left to right with the
alumina formers at the right (E, EP, F, FP).
2.2.3.6 Alloy performance and ranking
Evaluation of alloy performance was based on the results of 1000 hr tests, and compared the average
TAM from all coupons of the same alloy in each environment, as well as visual and microscopic
observation of the coupons. An arbitrary scale was used to rank the alloys. An average TAM of less than
20 microns was considered acceptable, between 20 and 100 microns was intermediate, and greater than
100 was considered unacceptable performance. For reference, linear corrosion at 20 microns/1000 hrs
would extrapolate to 1.8 mm over 10 years and 50 microns/1000 hrs would represent a loss of nearly 4.4
mm over a 10 year life. The ranking of alloys was different for each environment, and also varied by
temperature in the same environment.
In the PB1 environment, all alloys performed well enough to fit into the acceptable category. In the PB2
environment at 650 °C, only two alloys fell into the acceptable performance range – N06025 (alloy E)
and the pre-oxidized N07214 (alloy FP). N06059 (alloy J) was the only other alloy amongst the group to
fit into the intermediate category for both above and below the deposit (Figure 26). A number of other
alloys performed moderately well in the vapour space above the salts, but did much more poorly
underneath the deposits. Most notable amongst these were R20033 (alloy G) and S33228 (alloy H). These
two alloys were in the group of four alloys with the lowest nickel content. The other alloys in this group
included S31009 (alloy B) and S21500 (alloy A), both of which also fared quite poorly in these tests.
In the recovery boiler environment at 510°C, all alloys provided acceptable corrosion resistance. At
530°C, the only alloy to provide acceptable service both above and below the salt level was N06059
(alloy J). A few other alloys – notably N06025 (alloy E & EP) and N07214 (alloy F) were acceptable in
the vapour space, but not beneath the salts. N06690 (alloy K) and N12160 (alloy I) fell into the
intermediate category above the salts, and N06025 (alloy E) was the only alloy to fit into the intermediate
category beneath the salts. The worst alloys in this service were S31009 (alloy B), S21500 (alloy A) and
S33228 (alloy H).
54
)snorcim(
noisorroC
500
450
400
350
300
250
200
150
100
50
0
A B C G H I D J K E EP F FP
Avg Avg Metal Loss Internal
)snorcim(
noisorroC
Avg Avg Metal Loss Internal

ABOVE SALTS BELOW SALTS
500
450
400
350
300
250
200
150
100
50
0
A B H I D K E
H H H H H H H
(a) 530 °C
ABOVE SALTS BELOW SALTS
(b) 625 °C
Fig. 24. Corrosion results for Alloy Set 3 after exposure to recovery boiler salts at (a) 530 °C and (b) 625 °C
for 1000 hours in the standard atmosphere plus 50 ppm SO .
2
55
)snorcim(
noisorroC
500
450
400
350
300
250
200
150
100
50
0
A B H I D K E
X X X X X X X
Metal Loss Internal
)snorcim(
noisorroC
Metal Loss Internal
500
450
400
350
300
250
200
150
100
50
0
A B H I D K E
H H H H H H H
)snorcim(
noisorroC
500
450
400
350
300
250
200
150
100
50
0
A B H I D K E
X X X X X X X
Metal Loss Internal
)snorcim(
noisorroC
Metal Loss Internal

STANDARD ATMOSPHERE +50 ppm SO
2
500
450
400
350
300
250
200
150
100
50
0
A B H I D K E
(a) 530 °C
STANDARD ATMOSPHERE +50 ppm SO
2
(b) 625 °C
Fig. 25. Comparison of average TAM for the alloys that were in recovery boiler 1000 hour tests, without and
with the addition of 50 ppm SO . (a) 530°C; (b) 625°C
2
As expected, the recovery boiler environment at 625°C was extremely aggressive and no alloy fit into
either the acceptable or intermediate categories. Corrosion rates above and below the salt level were
similar. N06025 (alloy E) was the best of the alloys, along with S21500 (alloy A) and N06690 (alloy K).
Two alloys failed catastrophically in the recovery boiler environment at 650 °C – N06059 (alloy J) and
56
)snorcim(
noisorroC
500
450
400
350
300
250
200
150
100
50
0
A B H I D K E
Above Salts Below Salts
)snorciM(
noisorroC
Above Salts Below Salts
500
450
400
350
300
250
200
150
100
50
0
A B H I D K E
)snorcim(
noisorroC
500
450
400
350
300
250
200
150
100
50
0
A B H I D K E
Above Salts Below Salts
)snorciM(
noisorroC
Above Salts Below Salts

N07214 (alloy F). The failure of N06059 (alloy J) was unexpected, given its extremely good performance
in the same environment at the lower temperature. This alloy stands out from the others due to the very
high molybdenum content and it is likely that this is the contributing factor to the failure. N07214 (alloy
F), in contrast, contains little molybdenum, but contains the second least amount of chromium (next to
S21500 (alloy A)). Chromium is well known to enhance corrosion resistance in Kraft recovery
environments, so the failure of N07214 (F) was not unexpected. In contrast, the relatively good
performance of the S21500 (alloy A) coupons in this environment was surprising, given the low
chromium content of this alloy. While it might be argued that the manganese content of this alloy
imparted some level of protection, there remains the possibility that it too might have failed
catastrophically had the test been prolonged.
The ranking of alloys in the SO -containing cover gas were similar to the equivalent results in tests
2
without SO . Only 7 of the alloys were exposed in this environment, and they were chosen as the best of
2
the previous tests. 602CA (alloy E) displayed by far the best corrosion resistance in this test. There
appeared to be little difference in corrosion above or below the salt level. S21500 (alloy A) and S31009
(alloy B) were the worst of the limited set of alloys exposed to the SO -containing environment. Given
2
that the standard deviation of these experiments varies between 15-25 percent, the performance of the
balance of the other alloys could be described as similar.
2.2.4 Comparison to Field Data
Laboratory experiments are typically well-controlled and provide more reproducible results than field
exposures, where temperature, deposit flux and composition, and other critical parameters vary
dramatically as a function of time. The intent of laboratory experiments is to provide comparable data in
less time, with useful results. Oftentimes, they also fail to replicate critical aspects of the corrosive
environment, and consequently under- or over-estimate the real rate of corrosion in-service. One unique
aspect of this particular program is the strong linkage between field and laboratory tests [110,111]. The
salt deposits chosen for the laboratory tests were meant to mimic the real deposits collected from the one
recovery boiler and two power boilers boilers involved in the program. The equivalent field tests, in this
case, typically ran for about 2000 hours.
Overall, the general trends between field and laboratory trials matched well in the case of the in situ
recovery boiler trials. N07214 (alloy F), N08028 (alloy C) and S31009 (alloy B) all performed poorly in
the field. These alloys were also amongst the worst performers in the laboratory trials, particularly the
N07214 (alloy F) at higher temperatures. The alloys that performed best in the in situ probes were
N12160 (alloy I) and S21500 (alloy A), both of which fared reasonably well in the laboratory tests as
well. Although N06025 (alloy E) was clearly the best alloy in the laboratory tests, it did not fare as well at
the higher temperatures in the field probe.
The correlations between laboratory and field results were less clear for the power boilers, because of the
temperature differences. The laboratory trials were conducted at significantly higher temperatures than
could be reached in the locations where the field probes were installed, and consequently, there is no
directly comparable data. In the case of the PB1 tests (Port Mellon boiler in the field trials), the maximum
exposure temperature did not exceed 480°C in the field probe. Overall, the conditions in this boiler were
much less corrosive than was the case in the PB2 boiler (Crofton). This matches the laboratory
experience. However, an interesting note is that the most rapid corrosion in the field trial in PB1boiler
occurred at temperatures between 400 and 450°C. This was attributed to the presence of Zn and Pb in the
deposits, which form low-melting eutectic compounds at those temperatures. This is a good example of
not replicating the critical corrosive environment in a laboratory test. These elements were not included
in the synthetic salts, nor was the test temperature in the appropriate range for this corrosion mechanism.
57

For the PB2 boiler, the maximum exposure temperature in the field was about 550°C. The best
performing alloys in the field were N08120 (alloy D) and S21500 (alloy A), neither of which did
particularly well at the higher temperature laboratory tests. N06025 (alloy E) was also not a good
performing alloy in the field trials, despite doing well in the laboratory tests.
Across all three boilers, corrosion in the field trials was roughly of the same order of magnitude, but
somewhat higher than those measured in the laboratory experiments. This is a good correlation, given the
longer exposure times in the field trials. Cyclic temperatures and heat flux are also known to be strong
accelerators for corrosion in high temperature conditions, and neither of these was present in the
laboratory experiments. The difference in corrosion behavior for N06025 (alloy E) between the laboratory
and field trials was surprising and merits further investigation, given the good performance of this alloy in
the laboratory.
2.2.5 Summary and Conclusions
A laboratory test was developed that allows for assessment and comparison of corrosion that occurs
above and below deposits on the same coupon in simulated fireside superheater environments.
In these tests, the rate of corrosion in the gas phase of simulated power boiler environments was
substantially lower than for corrosion that occurred underneath deposits. This observation may have
strong practical implications for companies that practice risk-based inspection in biomass-fired boilers.
Under the test conditions employed, rates of corrosion above and underneath deposits were similar in a
simulated Kraft recovery boiler environment.
In terms of best corrosion resistance, Alloy N06025 was ranked either first or second out of all the alloys
evaluated in all laboratory test environments. The order of ranking of other alloys depended on the test
environment, whether the corrosion was measured above or underneath the synthetic salt, and
temperature.
In an environment simulating a chloride-contaminated biomass-fired boiler, the alloy ranking at 650°C
from most corrosion resistant to least was (roughly equivalent performance alloys ranked together):
R20033
N07214 (pre-
N06025 oxidized)
N08120
N06025 (pre- N12160
Above salts: < < S21500
oxidized) S33228
S31009
N06059 N07214
N06690
N08028
N08120
N06025
N12160 S21500
N06025 (pre- N06059
N08028
Below salts: oxidized) < N07214 <
S31009
N07214 (pre- N06690
S33228
oxidized)
R20033
• In an environment simulating a kraft recovery boiler, the alloy ranking at 530°C from most corrosion
resistant to least was(roughly equivalent performance alloys ranked together):
58

N06059 N12160
N08028
N07214 N07214 (pre-oxidized)
Above salts S33228
N06025 < N06690 <
(no SO ): S21500
2 N06025 (pre- N08120
S30109
oxidized) R20033
N12160
Above salts N06690 S33228
< N08120 <
(with SO ): N06025 S21500
2
S31009
N12160
N06059 N07214 (pre-oxidized)
Below N07214
N06025 N08028
salts < S21500 <
N06025 (pre- S31009
(no SO ): N06690
2 oxidized) S33228
R20033
N08120
N12160
Below
N06690 S21500
salts N06025 < <
N08120 S33228
(with
S31009
SO ):
2
• In an environment simulating a kraft recovery boiler with 625°C superheater tube temperature, all
alloys were ranked as providing unacceptable performance. Based on these results, it is unlikely that a
recovery boiler could be designed to operate at such a high temperature in the superheater. The alloy
ranking at 625°C from most corrosion resistant to least was (roughly equivalent performance alloys
ranked together):
N12160
N06690
N06025
N08120 N06059
Above salts N06025 (pre-
< S33228 < N07214
(no SO ): oxidized)
2 S31009 N07214 (pre-oxidized)
S21500
N08028
R20033
N12160
N06690
Above salts
N06025 < N08120 < S21500
(with SO ):
2 S31009
S33228
59

N08120
N06025 (pre-
N12160
oxidized) N06059
Below salts S31009
N06025 < < N07214
(no SO ): S33228
2 N06690 N07214 (pre-oxidized)
N08028
S21500
R20033
S31009
N08120
Below salts
N06025 < N06690 < S33228
(with SO ):
2 N12160
S21500
E EP J G FP I H F K C D A B
18 18 23 31 31 35 36 41 44 47 59 65 71
E EP FP J F K D I A C B H G
10 12 20 38 63 89 151 154 271 283 303 316 385
Fig. 26. The average TAM in microns for each alloy exposed to the PB2 environment at 650 °C. Alloy
performance is color coded as acceptable (green), intermediate (yellow) and unacceptable (red).
Fig. 27. The average TAM in microns for each alloy exposed to the recovery boiler environment at
530 °C. Alloy performance is color coded as acceptable (green), intermediate (yellow) and unacceptable (red).
Fig. 28. The average TAM in microns for each alloy exposed to the recovery boiler environment at
625 °C. Alloy performance is color coded as acceptable (green), intermediate (yellow) and unacceptable (red).
60
evobA
woleB
stlas
stlas
PB2 650°C
RB 530°C
J F E EP I FP K D G C H A B
12 13 15 15 25 42 44 54 62 127 133 140 272
J E EP I F A K G D FP C H B
14 27 39 59 61 81 87 99 115 159 169 185 194
evobA
woleB
stlas
stlas
K E D I H A B
47 47 83 154 168 198 260
E K D I A H B
41 91 118 151 160 199 301
evobA
woleB
stlas
stlas
RB 530°C +SO2
EP E A I K D H B C G J F FP
55 76 137 201 209 210 211 242 282 355 2000 2000 2000
EP E K A D I B H C G J F FP
65 92 133 134 211 217 219 230 278 347 2000 2000 2000
evobA
woleB
stlas
stlas
RB 625°C
E I K D B H A
12 144 165 182 195 201 295
E K B D H I A
46 103 179 184 215 241 255
evobA
woleB
stlas
stlas
RB 625°C +SO2

2.3 SOLUBILITY OF METAL OXIDES IN MOLTEN SALT
The presence of alkali metal salts, particularly chloride salts, is well recognized as a major factor in the
degradation of superheater tubes and, consequently, a significant contributor to the limit on superheater
steam outlet temperatures. These salts are an especially important consideration as temperatures approach
the first melting point of the salts, and the solubility of the normally protective metal oxides in the salts
becomes a concern. Consequently, a study of the solubility of metal oxides in a typical salt was initiated
at Georgia Institute of Technology as a master’s degree project under the supervision of Prof. Preet Singh.
A thesis resulted from this project, and the following text has been taken from the paper presented by
Joseph Meyer at the 2013 NACE Corrosion conference.
2.3.1 Background
The recovery boiler is an important part of the Kraft cycle that converts black liquor into green liquor and
steam. The efficiency of the recovery boiler then determines the amount of recoverable white liquor and
steam that is available to the mill for continued operations. The major limitation for converting the energy
into steam efficiently is that the increased steam temperature may also increase the corrosion rate
dramatically. Depending on the fuel used and the operating parameters, the first melting temperature
(FMT) of the ash deposits on the superheater tubes is near 520oC while the steam temperature is limited to
around 500oC.[57] If the salt deposits melt, then the corrosion rate can increase 4-5 fold while the metal
temperature increases as little as 3-6CO [4]. Using tube materials that contain more protective alloying
elements might reduce the corrosion rate to an acceptable level even with higher steam conditions.
Molten salt corrosion is similar to aqueous corrosion in that the salt acts as an electrolyte that allows for
quick diffusion of ions [112]. The salt behaves like water where it can be described as a combination of
an acid and base (e.g. Na O and SO for Na SO and H+ and OH- for H O). The activity or basicity of
2 3 2 4 2
Na O is similar to a pOH scale (where pOH is the base 10 logarithm of the activity of OH- ions in the
2
solution) and how corrosive the salt is will be determined by its basicity [113]. Most oxides are
amphoteric and will have an acidic or basic reaction with the salt according to its basicity.
The amount of corrosion is dependent on the solubility of oxide in the salt. As the solubility limit is
reached, the oxide/salt reaction rate will begin to decrease to maintain equilibrium. An oxide with a low
degree of solubility will be more protective because it will take less oxide dissolution to reach saturation
than one with a larger solubility limit [112]. A plot of oxide solubility against the basicity of the salt will
be is linear and has a slope that is easily determined theoretically. For example, if we consider the
solubility of NiO in Na SO , Equations 7 and 8 show the reaction and slope for the acidic reaction and
2 4
Equations 9 and 10 show the reaction and slope for the basic reaction [114].
Acidic reaction : 2NiO + Na O+ ½ O (g) = 2NaNiO (7)
2 2 2
Slope: log(NaNiO )/log(Na O) = -1/2 at fixed P for this reaction (8)
2 2 O2
Basic reaction: NiO + Na SO = NiSO + Na O (9)
2 4 4 2
Slope = log (NiSO )/log(Na O) = 1 (independent of the oxygen partial pressure) (10)
4 2
The major interest is in determining the oxide concentration at the solubility minimum (where the
acid/base reactions meet) and the value of basicity where minimum solubility for a particular oxide
occurs. If the value of basicity at the solubility minimum is known and the slopes are verified
experimentally, the solubility of an oxide under a given condition can be calculated and its solubility
relative to other oxides can be calculated.
If multiple salts are present, the basicity will be controlled by the conjugate acid partial pressures [113].
Thus the basicity of Na SO will be controlled by the partial pressure of SO while the basicity of
2 4 3(g)
NaOH will be is controlled by the partial pressure of water vapor. To evaluate the effects of multiple salts,
61

the partial pressures of the conjugate acids all need to be controlled independently rather than just the
activity of Na O. Simply changing the Na O concentration would produce reactions with both conjugate
2 2
acids.
Despite the usefulness of the solubility measurement, it does not take into account variations in the
solubility of oxides through the thickness of a molten salt layer on an oxidized metal. The solubility is not
expected to remain constant throughout the salt layer and can either increase or decrease between the
metal oxide/salt and salt/flue gas interface. An increase in solubility with distance from the metal oxide
(positive solubility gradient) would be preferred because after a given period of time, the salt adjacent to
the oxide will become saturated with dissolved oxide [115]. A negative solubility gradient is a problem
because it favors the diffusion of dissolved oxide away from the tube towards the salt/flue gas interface.
As more oxide diffuses towards the flue gas, the oxide solubility will decrease and the oxide will begin to
precipitate. Figure 29 shows a schematic of a negative solubility gradient where the precipitated oxide
forms a diffuse film of non-protective particles at the salt/flue gas interface. The diffusion gradient is still
maintained because the concentration of dissolved oxide near the tube is greater than away from the tube
despite the precipitated oxide. Because the diffusion gradient may never be satisfied and the system may
never reach an equilibrium, the corrosion reaction will then proceed until the all the tube metal is
dissolved. Even if an oxide is considered protective based on its solubility, a negative solubility gradient
will inevitably produce a high corrosion rate.
2.3.2 Experimental
Solubility measurements were taken by dissolving 1 gram of oxide in 200 grams of salt mixture. The salt
was contained in an alumina double crucible to prevent leaks. A schematic of the experimental setup is
given in Figure 30. Ultra-pure nitrogen gas was passed through the apparatus to fix the Na O activity. A
2
salt mixture of 73.9wt% Na SO , 10.2wt% KCl, 11.5wt% Na CO , and 4.4wt% K SO was used. The salt
2 4 2 3 2 4
composition was the same as the recovery boiler field study where superheater deposits were collected on
a probe and analyzed at FPInnovations, Vancouver [111]. At the test temperature of 750oC, the salt
mixture was completely liquid.
There are advantages and disadvantages of using a temperature above the solid-liquid two phase region
for this salt mixture in this experiment. The advantage was that the salt composition was fixed. Also, if
the salt is completely liquid; it can help to alleviate any local changes in composition due to improper
mixing. Other advantages include reduced sampling errors. If the tests were conducted at a lower
temperature in the liquid-solid two phase region, the composition of the molten salt would depend on the
temperature of the salt mixture. Temperature fluctuations could then change the composition during a test.
The oxide was added to the salt after the test temperature was reached to allow the salt to reach
equilibrium with the atmosphere and to prevent the possibility of the basicity or solubility changing
significantly with temperature. If the salt was not completely molten, the oxide would float on top of the
salt and contaminate the samples removed for solubility measurements. Oxide added to the molten salt
mixture would sink to the bottom of the crucible and undissolved oxide would remain there for the rest of
the experiment. Another problem is that sampling when the salt is not completely molten; it is possible to
catch solid salt in the sample. This would dilute the measurement because the solid salt would not contain
any oxide. Lastly, accidentally adding too much oxide or using a temperature close to the FMT can
freeze the salt and prevent sampling.
The disadvantage of using a temperature above the liquidus line is that is the results may not replicate
what happens on the tube surface at temperatures near the FMT. The composition of the salt that melts
first can be very different than the average composition of the mix. The solubility will change as the
temperature increases and the composition moves. The basicity is a function of temperature like with pH
62

Fig. 29. Schematic of a negative solubility gradient throughout the molten salt that continually precipitates
out to form an unproductive scale[112].
Fig. 30. Schematic of experimental apparatus.
in water. Even if the composition was somehow held constant, the solubility due to the basicity would
vary even from the liquidus to the experimental temperature.
The salt was held at temperature for two days to allow for the salt to equilibrate with the atmosphere and
the crucible. The crucible was made of alumina and significant concentrations of alumina were measured
in every melt. After the oxide was added, care was taken to prevent disturbing the melt. An alumina rod
was used to sample the melt and was inserted until it was approximately 1-2 cm from the bottom of the
crucible to prevent oxide contamination. The salt removed on the alumina rod was allowed to cool before
dissolving it into a known mass of water to prevent any changes in mass after sampling due to absorption
of water vapor. The major concern of error is during sampling because it is difficult to guarantee the same
sampling location and amount of melt for each measurement. If the solubility of the salt is location-
63

dependent, it would be difficult to get a reliable measurement. Samples were taken every hour after the
oxide was introduced up to 8 hours. This allowed enough time to find the saturation point and time to
saturation for each oxide.
Every sample was analyzed by inductively coupled plasma – optical emission spectroscopy (ICP). The
oxides evaluated were Al O , Fe O , Cr O , NiO, and SiO . Fe O , Cr O , and NiO are the oxides of the
2 3 2 3 2 3 2 2 3 2 3
major alloying elements in stainless steels. Al O and SiO were chosen to verify any effect the dissolved
2 3 2
oxide from the crucible had on the experiment and they are also considered as protective oxides in some
applications. ICP allows for parts per million to parts per billion resolutions and the amount of water
added to the salt when it is dissolved helped to keep the concentration of dissolved oxide within
operational range. Most of the samples measured were between 1ppm to 30ppm before dilution was taken
into account. ICP only measures metal concentrations instead of molecules so if equal weights of FeO and
Fe O were dissolved in water, the Fe concentration would be higher in the Fe O sample. This effect is
2 3 2 3
limited to the experiments with NiO and SiO . The other oxides were M O compounds and not subject
2 2 3
to this uncertainty.
2.3.3 Results and Discussion
From the results obtained from the present study, the oxides can be ordered from least soluble to most
soluble in the synthetic superheater deposit as: NiO <Fe O < Cr O = Al O < SiO . Figure 31 shows the
2 3 2 3 2 3 2
average solubility from 3 samples collected every hour for each oxide during the 8 hours of each
experiment. All of the oxides reached saturation within 1-2 hours and did not vary in concentration by
more than 1 order of magnitude except SiO which did so in 8 hours. The increased saturation time for
2
SiO is likely due to how much more SiO had to dissolve compared to the other oxides. Based solely on
2 2
the saturation curves, Ni-based alloys that form continuous NiO oxides would be the most corrosion-
resistant. Considering that Al O and Cr O have similar solubility in this salt, alloys relying on Cr O and
2 3 2 3 2 3
on Al O for corrosion protection should be roughly equivalent in corrosion resistance. Carbon steel
2 3
seems to be an economical choice because Fe O has an adequate amount of solubility and is the cheapest
2 3
alloy. However, oxidation resistance of carbon steel under recovery boiler superheater conditions is not
adequate. An important consideration is that saturation tests do not take into account the effects of
changes in solubility in the salt. If a negative saturation gradient is present, then the saturation limit is
irrelevant and SiO could actually be the most protective. Exposure tests under similar conditions can
2
indicate if a negative solubility gradient is present, because a negative solubility gradient would have
excessive corrosion despite an oxide’s low solubility.
2.3.3.1 Effect of presence of other oxides on solubility of alumina
The dissolved alumina from the crucible was measured during the oxides test to see what effect the
additional oxide could have on its solubility. If no effect exists then the solubility should be similar
between the tests. An advantage of using ICP is that it can measure all of the elements in parallel and this
analysis can be done without additional experiments. Figure 32 shows the changes of aluminum
concentration during the tests. Considering the solubility tests in Figure 31, the alumina concentration
should be between 100ppm and 1000ppm for all of the tests. Adding another oxide with the Al O
2 3
depressed the solubility of the Al O to between 1 and 100ppm. This is unusual because if the alumina
2 3
reacted with another metal oxide it would either increase the solubility and/or decrease the time to
saturation. This synergistic reaction occurs when one oxide undergoes an acidic reaction while the other a
basic reaction. The reactions would use up or produce Na O and thereby encourage the reaction. A
2
possible reason for the depressed alumina solubility is that the dissolved alumina is reacting with
something in the experiment like the added metal oxide or any dissolved species and precipitating out.
64

100000
10000
1000
100
10
1
0 2 4 6 8
0.1
Fig. 31. Average solubility of metal oxides in a recovery boiler salt exposed for 8 hours at 750oC
The crucible is fairly smooth and may not replenish the dissolved alumina as fast as it is precipitated. The
best way to test this hypothesis would be to check the compounds formed in the salt to see if the alumina
reacted with any of the other metal oxides. This would verify if any unexpected reactions are taking place.
It is important to consider the effects of multiple oxides on the surface of an alloy because commercial
alloys can form combinations of multiple oxides. Also, oxides that form during boiler operation have a
composition that varies with exposure time. A common effect, when the recovery boiler salt is not
molten, is chromium depletion in the surface of the alloy where the protective chromium has been used up
to form Cr O . If the Cr O film fails, the chromium composition in the alloy surface may be insufficient
2 3 2 3
to re-form a Cr O film, so that a less protective Fe O film is formed. If this effect is localized, then
2 3 2 3
adjacent areas of the alloy might be covered with Cr O and Fe O . Alternately, during maintenance, the
2 3 2 3
oxide may fracture or scale off revealing new metal. In both cases, adjacent dissimilar oxides would be
exposed, increasing or decreasing the corrosion rate.
A well-known issue with multiple oxides is a synergistic reaction that increases the corrosion rate in a
given molten salt environment. Equations 7 and 9 indicate that one reaction produces Na O while the
2
other consumes it driving the reaction [116]. This effect only occurs when the basicity are between the
solubility minimum for both oxides but cannot be overlooked. The data in Figure 31 suggest that it may
be possible to reduce an oxide’s solubility. From a design perspective, if the effect of multiple oxides is
taken into account, it might be possible to avoid unexpected corrosion or boost an alloy’s corrosion
resistance.
2.3.4 Conclusions from Molten Salt Solubility Studies
Molten salt corrosion of alloys is controlled by thermodynamic and kinetic factors. Based on the acid/base
reaction equilibrium Na O concentration and oxide solubility are important factors in determining the
2
thermodynamic effects of corrosion. Solubility is useful under a positive solubility gradient where molten
salt corrosion is controlled by thermodynamics. A negative solubility gradient on the other hand is
kinetics controlled and is not limited by solubility. The solubility of NiO, Fe O , Cr O , Al O , and SiO
2 3 2 3 2 3 2
in a mixture of Na SO , KCl, K SO , and Na CO indicates that NiO is the least soluble. Cr O and Al O
2 4 2 4 2 3 2 3 2 3
65
)mpp(
noitartnecnoC
Average Solubility of Metal Oxides in Recovery Boiler Salt
Cr
Fe
Ni
Al
Si
Time (Hours)

had similar solubility while SiO had the greatest solubility of the group. Fe O was shown to have the
2 2 3
second-lowest solubility of the group but carbon steels may not have adequate oxidation resistance for
superheater environments. However, this information should be used along with kinetic data to determine
the most protective oxide and alloy for these conditions. If a negative solubility gradient exists, the most
soluble oxide can become the most protective.
1000
100
10
1
1 2 3 4 5 6 7 8
Fig. 32. Average solubility of alumina in the presence of an additional metal oxide during 8 hours of exposure.
66
)mpp(
noitartnecnoC
Average Solubility of Alumina Mixed with other
Oxides in Recovery Boiler Salt
Pure Al
Al-Cr
Al-Fe
Al-Ni
Al-Si
Time (Hours)

2.4 FIELD CORROSION STUDIES
As a complement to the laboratory corrosion studies, field studies with specially designed corrosion
probes were used to measure the corrosion rates of alternate superheater tube alloys in four particularly
aggressive biomass-fired boiler environments at temperatures as much as 100 Celsius degrees above the
normal maximum superheater tube temperature.
Before exposing the corrosion probes, in order to get an indication of the composition of the superheater
deposits, air-cooled sampling probes were exposed in three of the four environments. These sampling
probes were exposed for a relatively short time – generally 7-10 days – and care was taken in recovering
the deposits from the top and bottom surfaces of the probes. Results obtained from analysis of these
deposits helped determine the test compositions for the laboratory studies.
In order to assess the performance of the selected alloys under the most severe environments that might
be encountered during combustion of biomass, four boilers were selected as examples of what would be
expected to be particularly hostile biomass boiler environments. These environments include a recovery
boiler in Covington, Virginia, that processes black liquor derived primarily from hardwood thus yielding
deposits particularly high in potassium content. A hogged fuel boiler in Crofton, British Columbia, that
primarily burns bark obtained from seawater-floated logs was expected to have deposits that are high in
chlorine content. Another hogged fuel boiler in Port Mellon, British Columbia, burns fuel consisting
primarily of wood from beetle-killed pine trees, but also uses bark from seawater-floated logs and
construction and demolition (C & D) waste which together could result in superheater deposits containing
some heavy metal as well as some chlorine. The fourth environment was a power boiler in Gadsden,
Alabama, that normally burns coal but supplemented the coal with wood for the period of these studies.
This resulted in an environment containing sulfur from the coal as well as the alkali metal salts from the
wood. This paper summarizes the results from the four corrosion probes that were exposed in the boiler
superheater areas of particularly hostile but significantly different boiler environments.
2.4.1 Experimental Procedure
2.4.1.1 Deposit sampling
Deposit sampling probes were exposed in the recovery boiler and the two hogged fuel boilers. The
sampling probes in the two hogged fuel boilers were prepared, exposed and analyzed by the
FPInnovations collaborators. The sampling probe exposed in the Covington boiler was air cooled and
had ten thermocouples spaced every 15 cm (six inches) along the length of the probe. These
thermocouples alternated between the “top” and “bottom” of the probe so temperatures measured on the
bottom of the probe reflected the effects of radiant heating while temperatures measured on the top are
more representative of the gas temperature. At the end of the approximately one week exposure period,
the deposit sampling probe was removed from the boiler, allowed to cool and then wrapped with plastic
wrap to keep the deposits in place on the surface of the probe. Once the probe was safely returned to Oak
Ridge, samples of the deposits were removed from both the top and bottom of the probe for analysis.
2.4.1.2 Corrosion probe design
Each air-cooled corrosion probe was designed to contain 30 samples each 5.08 cm (2 inches) long
fabricated from 1½ inch schedule 40 pipe or the equivalent. The samples were fabricated so that they
were interlocking and each had a slot machined in the surface to accommodate a 1/16 inch diameter
sheathed thermocouple. Temperatures were measured by twenty-four thermocouples so that four of every
five samples had a thermocouple attached. These thermocouples were fed through the inner diameter
(ID) of the corrosion probe. The corrosion sample design, which is shown in Figure 33, provides for
67

Fig. 33. Left) Schematic of the corrosion samples, center) Photo of samples tack welded with thermocouples
protruding from the surface of the samples, and right) Photo of samples welded together and with shim stock
welded in place to hold thermocouples on the surface of the samples.
about 1 cm of the thermocouple be in contact with the outer surface of the sample. This design was
intended to minimize the cooling effect on the thermocouples of the air flowing through the probe thus
making the measured temperature representative of the temperature of the outer surface of the samples.
To assure that each thermocouple maintained full contact with the sample surface, a piece of 0.78 mm
(0.031 inch) stainless steel shim stock was welded to the sample so that the shim stock held the
thermocouple tightly against the sample. Pictures of the thermocouple arrangement without and with the
shim stock are also included in Figure 33. Besides showing the shim stock that was welded in place over
each thermocouple, this figure also shows the tack welds that were used to position and align the samples
before application of the circumferential welds that rigidly connect adjacent samples. To provide
additional support for the probe which extended at least 2.1 meters (7 feet) from the boiler wall, a ½ inch
diameter stainless rod ran the length of the probe inside the corrosion samples (along with the
thermocouples). A stiff spring was placed between the rod and the outside base of the corrosion probe in
order to allow for thermal expansion that was expected to differ between the array of welded samples and
the stainless steel support rod that was cooled by the air flowing through the probe.
For the laboratory corrosion study, eleven alloys were exposed to synthetic environments similar to those
encountered in the biomass-fired boilers. The three co-investigators and the project participants selected
eight of these alloys plus 347H stainless steel for exposure in the corrosion probe. These alloys and their
compositions are listed in Table 5. Nominal compositions are given for three of the alloys while the other
compositions are from actual heat analyses. The selected alloys included two alumina-forming alloys as
well as seven more traditional chromia-forming alloys. Alloy S31009 was chosen because it is currently
used in the hottest areas of the Covington recovery boiler’s superheater. Two other alloys (S21500 and
S34709) were chosen because of good experience from similar superheater studies conducted in Europe.
The two alumina-forming alloys were preoxidized at 1000°C to promote formation of the alumina layer
while the chromia-forming alloys were not given any pretreatment. Prior to assembly into the corrosion
probe, the wall thickness of each sample was measured in several locations around the circumference.
The thirty samples on each corrosion probe were arranged in a repeating pattern so that samples of all but
two of the materials (N06690 and N12160) were exposed to a range of temperatures. Four samples of
68

each of the other seven alloys were positioned so that one sample of each material was near the hotter end
of the probe, one sample was near the cooler end and the other two samples of each material experienced
intermediate temperatures. In addition to the effect resulting from a sample’s position on the corrosion
Table 5. Composition of alloys selected for exposure in the corrosion probes
Product UNS Fe Ni Cr Mo Co Mn Al Si Ti C Others
name number
310H SS S31009 Bal 19.10 24.30 0.25 1.17 0.55 0.045
Haynes 214 N07214 3.56 Bal 16.08 0.03 0.21 4.22 0.12 0.04 Y=0.004,
Zr=0.011
Sanicro N08028 35 31 27 3.5 1.8 0.2 0.01
28*
602CA N06025 9.60 62.20 25.30 0.02 2.30 0.03 0.10 0.170 Y=0.07,
Zr=0.09
HR160 N12160 0.63 Bal 28.00 0.27 30.20 0.48 2.75 0.48 0.056
Inconel N06690 9 62 29 0.02
690*
HR120 N08120 36.26 36.68 24.74 0.07 0.11 0.68 0.16 0.73 0.057 N=0.21
Esshete S21500 72 10 15 1 6.3 0.5 0.1 Nb=1, V=0.25,
1250* B=0.006
347H SS S34709 Bal 9.02 17.21 1.31 0.57 0.048
*Nominal values
probe, the temperature of a sample varied from “top” to “bottom” in that one side was heated by the
incident gas, and in some cases radiant heat from the lower boiler, so, in one case, it was observed that
one side was as much as 80 Celsius degrees hotter than the other side. The arrangement of samples on the
corrosion probe and the identification of thermocouple locations are shown in Table 6, and Figure 34
shows a typical corrosion probe with alloy locations identified. Instrumentation for data collection and
process control along with a computer were provided with the corrosion probe. A variable flow valve
controlled air flow to the corrosion probe and the setting of the variable flow valve was determined by
computer software which adjusted the flow to maintain the temperature of a particular thermocouple in a
selected range. Generally, a thermocouple experiencing one of the highest temperatures was selected for
this control function, and this was usually a thermocouple on the bottom side near the hot end of the
probe. In addition to enabling the remotely-located operator to select the reference thermocouple, the
computer’s display panel also permitted the operator to select the control range for this thermocouple and
the data collection rate.
Although the computer software permitted the operator to select the data collection rate, all four
computers were set to record the temperature of each thermocouple once a minute during their entire
operating periods. On a daily basis, the temperatures and valve setting data were transferred via a
telephone connection from the on-site computer to a computer in Oak Ridge. Plots of each day’s
temperature data were made and evaluated to be certain there were no operational issues. About once a
week, the temperature plots were sent to the boiler operators.
At the completion of the exposure, the probe was removed from the boiler with as little loss of the
deposits as was possible. Once the probe had cooled, the portion of the probe with the thirty samples was
wrapped tightly with plastic to retain as much of the deposits as possible. When the probe was received at
the laboratory, the orientation was carefully noted, then samples of the deposits were collected and each
metal sample was cut off the probe. An example of the thirty samples is shown in Figure 35. For the
metallographic examination, a complete ring was cut from the approximate center of each sample and its
orientation during exposure was noted. So that the exposed cross-section would be representative of the
true thickness of the sample, every effort was made to make the cuts perpendicular to the axis of each
69

sample. Any error introduced if cuts were not perpendicular would result in the remaining thickness
being overestimated; thus any error would be on the conservative side. Using the micrographs from the
metallographic examinations, the thickness of remaining unaffected metal was determined for the top and
bottom of each sample. Scanning electron microscopy was used to determine the extent of subsurface
degradation and to collect compositional information for the reaction products on and near the surface,
particularly for the samples exposed at the highest temperatures.
Table 6. Arrangement of samples on the corrosion probe and location of thermocouples
Position UNS number/Alloy TC # (on top of sample) TC # (on bottom of
sample)
1 S31009/310H SS 24
2 N07214/Haynes 214 23
3 N08028/Sanicro 28 22
4 N06025/602CA 21
5 N12160/HR160 20
6 N06690/Inconel 690
7 N08120/HR120 19
8 S21500/Esshete 1250 18
9 S34709/347H SS 17
10 S31009/310H SS
11 N07214/Haynes 214 16
12 N08028/Sanicro 28 15
13 N06025/602CA 14
14 N08120/HR120
15 S21500/Esshete 1250 13
16 S34709/347H SS 12
17 S31009/310H SS 11
18 N07214/Haynes 214
19 N08028/Sanicro 28 10
20 N06025/602CA 9
21 N08120/HR120 8
22 S21500/Esshete 1250
23 S34709/347H SS 7
24 S31009/310H SS 6
25 N07214/Haynes 214 5
26 N08028/Sanicro 28
27 N06025/602CA 4
28 N08120/HR120 3
29 S21500/Esshete 1250 2
30 S31009/310H SS 1
2.4.2 Results
Results from examination of samples from the various corrosion probes are summarized in the following
section. The order of presentation is the order in which the probes were inserted in the respective boilers.
2.4.2.1 Covington recovery boiler deposit probe
Figure 36 shows the average daily temperature of the ten thermocouples over the approximately eight day
exposure period of the deposit sampling probe in the Covington recovery boiler. The measured
temperatures ranged from about 300°C to about 600°C [111]. Analysis of the deposits using X-ray
70

diffraction provided results which indicated the potassium-rich compound, K Na(SO ) , was among the
3 4 2
components of the deposit [111].
Fig. 34. Typical corrosion probe showing the arrangement of samples as they were assembled on the probe.
Fig. 35. Photo of the 30 samples removed from one of the corrosion probes. Samples #6 and #10 still contain
the spacers used to position the support rod in the center of the probe. Several other samples still contain the
remnants of the thermocouple that was attached to the outer surface of most samples.
71

2.4.2.2 Covington recovery boiler corrosion probe
The deposit sampling probe and the corrosion probe were inserted through a port on the rear wall (the side
opposite the bull nose and the smelt spouts) on the 14th floor of the boiler which was about 20 feet (6
meters) below the roof of the boiler. This location was high enough in the boiler that the temperature
could be controlled in the desired range with a reasonable air flow, and, because this location was well
away from the superheater tubes, there were no sootblowers in the vicinity to affect or disrupt the
accumulation of deposits on the probe. As noted previously, deposits from the sampling probe exposed in
the Covington boiler confirmed the presence of significant amounts of potassium in the deposits.
The corrosion probe was exposed for 2,000 hours (12 weeks), and the boiler operated under reasonably
normal conditions for the great majority of that time. An example of the data collected for one day early
in the exposure period is shown in Figure 37. Unfortunately, several thermocouples failed during the
latter part of the exposure period, so temperatures shown for some thermocouples do not cover the full
2,000 hours. At the conclusion of the probe exposure, the arithmetic mean temperature for each
thermocouple on each day was calculated, and these results are shown in Figure 38. From a plot of these
average temperatures an estimate was made for the average top and bottom temperature for each sample.
Clearly, during the 2,000 hour exposure the temperature of every sample varied considerably from the
average value, so the meaning of exposure temperature is much different between the field exposures and
the well-controlled laboratory tests.
In order to determine the performance of each alloy as a function of average exposure temperature and to
compare the performance of all the alloys, the depth of affected material (a sum of thickness loss and
extent of subsurface attack) was plotted versus the estimated average temperature. Results for all the
alloys exposed in the Covington boiler are shown in Figure 39 and results for selected individual alloys
are shown in Figure 40. These results show there are several alloys that did not perform very well in this
environment at and above 570°C (N07214, N08028 and S31009) while N12160 and S21500 were among
the better performers. Alloy N06025 showed a very low rate of material affected around 590°C, but
considerably higher rates at 560 and 615°C.
As a means to compare the results of the corrosion probe exposure with actual boiler experience, it is
important to note that S31009 has performed well under the current boiler operating conditions –
presumably at a tube temperature of about 470°C. If it is assumed that the degradation rate observed at
470°C for S31009 exposed on the probe is acceptable, then it would seem reasonable that any alloy that
demonstrates approximately the same rate at 570°C would be suitable for use at that temperature. On that
basis, N12160 and S21500 would be expected to perform satisfactorily if used in a “high potassium”
boiler operating with superheater tube temperatures around 570°C.
2.4.2.3 Crofton hogged fuel boiler
As previously noted, the hogged fuel boiler in Crofton, British Columbia, was selected because bark from
the seawater floated logs would result in a fuel with high chloride content. X-ray diffraction analysis of
deposits collected from the surface of several corrosion probe samples showed a high concentration of
NaCl. Figure 41 shows the results of examination of several samples.
The corrosion probe in the Crofton boiler was inserted through a manway door in the superheater area
less than an estimated 2 meters below a sootblower. Consequently, some cleaning of the tube surface
possibly occurred on a fairly regular basis. The probe was exposed for a total of about 2160 hours, but
the exposure was interrupted and the probe removed from the boiler because of a planned shutdown and
water washing of the boiler about midway through the exposure period.
72

Deposit Sampling Probe Covington Virginia
Fig. 36. Average daily temperatures for each of the ten thermocouples on the deposit sampling probe.
Fig. 37. Typical example of thermocouple temperatures from the corrosion probe exposed in the Covington
recovery boiler. Note that the orange line shows the temperature of thermocouple #23 which was being used
to control the flow of cooling air and thus the probe temperature.
73
)C°(
erutarepmeT

Fig. 38. Average daily temperatures of thermocouples in the Covington recovery boiler
650
600
550
500
450
400
350
300
0 0.5 1 1.5
Fig. 39. Total affected material as a function of exposure temperature for samples exposed for 2,000 hours on
the corrosion probe in the Covington recovery boiler.
74
)C°(
erutarepmeT
erusopxE
650
600
550
500
450
400
350
300
250
1 3 5 7 9 11131517192123252729313335373941434547495153
Total Material Loss By Samples
On Covington Corrosion Probe
S31009
Goal N07214
N08028
N06025
Current
N08120
max T
S21500
S34709
N12160
N06690
Material Affected (mm)
)C°(
serutarepmeT
elpuocomrehT
TC1
Daily Average Temperatures
TC2
Corrosion Probe Covington Virginia TC3
TC4
TC5
TC6
TC7
TC8
TC9
TC10
TC11
TC12
TC13
TC14
TC15
TC16
TC17
TC18
TC19
TC20
TC21
TC22
TC23
TC24
Operating Days

700
600
500
400
300
0 1 2 3 4
Fig. 40. Total affected material versus exposure temperature for individual alloys exposed for 2,000 hours on
the corrosion probe in the Covington recovery boiler.
75
erutarepmeT
erusopxE
)Cº(
N07214
700
600
500
400
300
0 0.5 1 1.5
Material Affected (mm)
erutarepmeT
erusopxE
)Cº(
N08028
Material Affected (mm)
700
600
500
400
300
0 0.2 0.4 0.6 0.8 1
erutarepmeT
erusopxE
)Cº(
S31009
700
600
500
400
300
0 0.2 0.4 0.6 0.8 1
Material Affected (mm)
erusopxE
)Cº(
erutarepmeT
N06025
Material Affected (mm)
700
600
500
400
300
0 0.2 0.4 0.6 0.8
erutarepmeT
erusopxE
)Cº(
N08120
700
600
500
400
300
0 0.2 0.4 0.6
Material Affected (mm)
erutarepmeT
erusopxE
)Cº(
S34709
Material Affected (mm)
700
600
500
400
300
0 0.1 0.2 0.3 0.4 0.5
erutarepmeT
erusopxE
)Cº(
S21500
Material Affected (mm)

NaCl
1. 30 Bottom
2. 26 Bottom
NaCl
3. 21 Bottom
4. 16 Bottom
5. 11 Bottom
6. 6 Bottom
7. 1 Bottom
KCl
Fig. 41. Results of X-ray diffraction measurements of deposits collected from the bottom of 7 samples on the
corrosion probe in the Crofton hogged fuel boiler.
Figure 42 shows the average daily temperatures for the 24 thermocouples on the corrosion probe that was
exposed in the Crofton boiler. The computer software was set to control the flow of cooling air on the
basis of the temperature of thermocouple #24, but it is clear from Figure 42 that the temperature of
thermocouple #24 frequently dropped below the desired range. In these cases, the air flow was already
reduced to a minimal level, so this resulted in the significant fluctuations in temperature shown in Figure
42. An average value for the temperature of each sample was calculated, but it should be recognized that
each sample experienced significant variations around the calculated value.
Figure 43 shows the measured thickness of affected material versus exposure temperature for the samples
exposed on the Crofton boiler probe. With the current maximum superheater tube temperature at about
415°C, the goal was to identify the materials with the lowest degradation rate at 515°C. This figure
shows that most of the alloys had a fairly low degradation rate at 500°C, but many of the alloys showed
rapid increases in degradation at slightly higher temperatures. This pattern is more clearly shown in the
plots for individual alloys displayed in Figure 44. The two alumina forming alloys, N07214 and N06025,
along with N08028 showed this type of behavior while S34709, N08120 and S21500 didn’t appear to
show such rapid increases when exposed to average temperature at and above 525°C.
2.4.2.4 Gadsden power boiler
One of the boiler manufacturers participating in this project suggested that the coal fired boiler at
Southern Company’s power plant in Gadsden, Alabama, be considered for inclusion in the project
because the boiler had previously been used for co-firing coal and biomass – both wood and switchgrass.
After a description of the project was presented to power plant and administrative personnel, the power
plant operators agreed to participate in the project and to operate the boiler continuously for an extended
time with a blend of coal and wood. The original goal was to operate with up to 15% biomass, but that
goal could not be achieved. The actual amount of biomass included in the coal-wood blend ranged from
8 to 15%.
76

650
600
550
500
450
400
350
300
250
200
1 6 11 16 21 26 31 36 41 46 51 56 61 66 71 76 81 86
Fig, 42. Daily average temperature of thermocouples exposed about 2,160 hours on the corrosion probe in
the Crofton hogged fuel boiler.
Fig. 43. Total affected material as a function of exposure temperature for samples exposed for 2,160 hours on
the corrosion probe in the Crofton hogged fuel boiler.
77
)C°(
erutarepmeT
elpuocomrehT
Daily Average Temperatures TC 1
TC 2
Corrosion Probe Crofton British Columbia
TC 3
TC 4
TC 5
TC 6
TC 7
TC 8
TC 9
TC 10
TC 11
TC 12
TC 13
TC 14
TC 15
TC 16
TC 17
TC 18
TC 19
TC 20
TC 21
TC 22
TC 23
TC 24
600
550
500
450
400
350
0 0.2 0.4 0.6 0.8 1 1.2 1.4
)C°(
erutarepmeT
erusopxE
Operating Days
Total Material Loss By Samples
On Crofton Corrosion Probe
S31009
N06025
N08120
Goal
N07214
N12160
S21500
Current N08028
max T
N06690
S34709
Material Affected (mm)

575
525
475
425
375
0 0.5 1 1.5
Fig. 44. Total affected material versus exposure temperature for individual alloys exposed for 2,160 hours on
the corrosion probe in the Crofton hogged fuel boiler.
78
erutarepmeT
erusopxE
)C°(
N06025
575
525
475
425
375
0 0.5 1 1.5
Material Affected (mm)
erutarepmeT
erusopxE
)C°(
N08028
Material Affected (mm)
575
525
475
425
375
0 0.5 1 1.5
erutarepmeT
erusopxE
)C°(
N07214
575
475
375
0 0.1 0.2 0.3 0.4
Material Affected (mm)
erutarepmeT
erusopxE
)C°(
S31009
Material Affected (mm)
575
525
475
425
375
0 0.2 0.4 0.6
erutarepmeT
erusopxE
)C°(
N08120
575
525
475
425
375
0 0.1 0.2 0.3 0.4
Material Affected (mm)
erutarepmeT
erusopxE
)C°(
S21500
Material Affected (mm)
575
525
475
425
375
0 0.1 0.2 0.3
)C°(
erutarepmeT
erusopxE
S34709
Material Affected (mm)

This corrosion probe was inserted in a sootblower lane between superheater tube platens and is shown in
Figure 45 just before it was removed. Deposits on the probe were a reddish color and were fairly limited
in terms of the amount accumulated. Although there were a couple interruptions in boiler operation
during the early stages of the exposure, as shown in Figure 46, the temperatures were far more constant
than observed in the other three boilers that were studied. The total exposure period lasted for about 123
days, but the first several days were during a start up period when temperatures were low, and there were
two short periods, clearly evident in Figure 46, where the boiler briefly cooled, in one case to near room
temperature. The probe was actually exposed to normal operating conditions for about 106 days or 2,540
hours.
The average temperatures for the top and bottom of each sample were calculated from the daily average
temperatures. From these calculations, it was evident that the tops of the samples were 60-80 Celsius
degrees hotter than the bottom of the samples. This is not the pattern generally seen in superheater tubes,
but the boiler operators confirmed that this was the pattern to be expected for this location.
After the probe and the supporting structure were returned to the lab, preparations were made to dispose
of the portion of the probe that was just inside the boiler wall but did not include any samples. In making
the routine but required check for evidence of radioactivity on the structure, it was found that low levels
of lead and bismuth isotopes were present. These isotopes are decay products of uranium, and it is
reasonable to assume that the low concentration of uranium in the coal resulted in deposition of these
isotopes on the cooler portion of the corrosion probe. As a result, the nine samples on the cooler end of
the probe could not be removed and examined. Deposits were removed from the samples on the hotter
end of the corrosion probe, and the analyses identified mullite, quartz, cristobalite, hematite and magnetite
as the major components.
The 21 samples that could be examined were sectioned in the customary way and the reduction in
thickness determined as well as the subsurface attack. Results of those measurements are plotted as a
function of exposure temperature in Figure 47. These results show that the degradation of the alloys in
the coal-wood-fired environment was significantly less than seen for most of the alloys in the boilers fired
exclusively with biomass. As can be seen from the figure, several alloys had losses in the 0.20 to 0.25
mm range for this exposure period.
2.4.2.5 Port Mellon hogged fuel boiler
The fourth probe was inserted in a hogged fuel boiler in Port Mellon, BC, with the expectation that the
boiler would be, like the Crofton boiler, firing bark from seawater floated logs. However, the infestation
of pine beetles resulted in a ready availability of beetle-killed pine trees. Consequently, at the time of the
corrosion probe exposure, the mill was using wood from beetle-killed pine trees, bark from seawater
floated logs along with occasional barge loads of C & D waste from Vancouver. The latter of these three
sources of biomass may have ultimately contributed some unexpected, but very interesting, results.
This boiler was converted to a fluidized bed system and this delayed insertion of the corrosion probe, so
this was the last of the exposures to be started. Once the probe was inserted there was a problem with the
variable flow valve that made it impossible to reduce the flow of cooling air to less than the fully open
position. This made it impossible to control the probe temperature, and consequently, these temperatures
stayed well below the desired level. Eventually, the variable flow valve was replaced, and this permitted
better control of the temperature. However, the site available for insertion of the probe was less than 30
cm (12 inches) above the bullnose, and this proximity to a water cooled surface apparently prevented the
probe temperatures from reaching the desired levels. The average daily temperatures are shown in Figure
48, and it is obvious that the temperatures stayed low until about the 70th day when the variable flow
valve was replaced. Even after the valve replacement, for many days the highest temperatures were not
79

Fig. 45. Photo of the corrosion probe in the Gadsden power boiler just prior to its removal (photo courtesy of
Billy Zemo, Southern Company).
Fig. 46. Average daily temperatures of thermocouples on the corrosion probe exposed about 2, 540
hours in the coal and wood co-fired Gadsden power boiler.
80

650
600
550
500
450
400
0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45
Fig. 47. Total affected material as a function of exposure temperature for samples exposed for 2,540 hours on
the corrosion probe in the Gadsden power boiler.
Fig. 48. Average daily temperatures of thermocouples on the corrosion probe exposed about 2,830 hours in
the Port Mellon hogged fuel boiler.
81
)C°(
erutarepmeT
erusopxE
Total Material Loss By Samples
On Gadsden Corrosion Probe
S31009
N06025
Goal
N08120
N07214
N12160
Current S21500
max T
S34709
N08028
N06690
Material Affected (mm)
700.0
600.0
500.0
400.0
300.0
200.0
100.0
0.0 Days
)C°(
serutarepmeT
elpuocomrehT
1 11 12 13 14 15 16 17 18 19 101 111 121 131 141 151 161 171 181
Daily Average Temperatures TC 14
TC 1
Corrosion Probe Port Mellon British Columbia TC 2
TC 3
TC 4
TC 5
TC 6
TC 7
TC 8
TC 9
TC 10
TC 11
TC 12
TC 13
TC 15
TC 16
TC 17
TC 18
TC 19
TC 20
TC 21
TC 22
Operating Days

much above 500°C. This resulted in not having sufficient data to predict degradation rates at and above
500°C. The exposure time at the higher temperature levels was about 118 days or about 2830 hours.
Figure 49 shows the depth of affected material versus temperature for the various samples exposed in the
Port Mellon boiler. In addition to the fact that the highest temperatures were lower than desired, it was
particularly of interest to note that most of the alloys showed a higher than expected degree of
degradation in the 400-430°C temperature range. Note the data points inside the red oval in Figure 49.
The deviation from the expected degradation pattern is more evident in the plots in Figure 50 which show
the variation in affected material versus temperature for six of the alloys exposed in this boiler.
In an effort to determine why higher rates of degradation were seen at relatively low temperatures, more
thorough analysis were undertaken on deposits collected from the samples exposed in the particular
temperature range. Both X-ray diffraction and Raman scattering were used to try to identify components
of the deposits that might be responsible for low melting point compounds that might cause accelerated
degradation in a fairly low temperature range. Results of the X-ray and Raman studies indicate the
presence of Zn (II) and/or Pb (II) either one of which could form relatively low melting point compounds.
A more detailed review of the analysis results of the deposits collected from the sampling probe exposed
by FPInnovations revealed zinc concentrations on the order of 0.2% and lead concentrations of about a
third that level [117]. Studies conducted in Finland at Åbo Akademi have shown that heavy metal salts or
oxides containing zinc and/or lead can cause accelerated corrosion of superheater tube alloys like 2¼Cr-
1Mo steel and 347H stainless steel [118]. Based on this information, it appears likely that the higher
degree of degradation seen in the 400-430°C range on the corrosion probe samples is due to the presence
of these heavy metals that almost certainly were introduced into the boiler in the C & D waste. It will be
of interest to learn if the lower temperature superheater tubes and the tubes in the bull nose of the Port
Mellon boiler experience accelerated corrosion.
525
500
475
450
425
400
375
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
Fig. 49. Total affected material as a function of exposure temperature for samples exposed about 2,830 hours
on the corrosion probe in the Port Mellon hogged fuel boiler.
82
)C°(
erutarepmeT
erusopxE
Total Material Loss By Samples
On Port Mellon Corrosion Probe
Goal
S31009
N07214
N09028
N06025
N08120
Current S21500
max T
Material Affected (mm)

470
450
430
410
390
370
0 0.2 0.4 0.6 0.8
Fig. 50. Total affected material versus exposure temperature for individual alloys exposed for 2,830 hours on
the corrosion probe in the Port Mellon hogged fuel boiler. Note the higher amount of material lost in the 400-
430°C temperature range for most alloys.
2.4.3 Summary
Four corrosion probes each containing a total of 30 metallic samples of 9 different alloys were each
exposed in a boiler firing biomass. Three of the boilers were selected because of the extreme
environment that was expected in each, and the fourth was chosen because it burned a mixture of coal and
biomass.
83
)C°(
erutarepmeT
erusopxE
602CA
470
450
430
410
390
370
0 0.2 0.4 0.6 0.8
Material Affected (mm)
)C°(
erutarepmeT
erusopxE
N07214
Material Affected (mm)
470
450
430
410
390
370
0 0.2 0.4 0.6 0.8
)C°(
erutarepmeT
erusopxE
S21500
470
450
430
410
390
370
0 0.2 0.4 0.6
Material Affected (mm)
)C°(
erutarepmeT
erusopxE
N08120
Material Affected (mm)
470
450
430
410
390
370
0 0.2 0.4 0.6
)C°(
erutarepmeT
erusopxE
N08028
470
450
430
410
390
370
0 0.1 0.2 0.3 0.4
Material Affected (mm)
)C°(
erutarepmeT
erusopxE
S31009
Material Affected (mm)

The temperatures measured by the 24 thermocouples on each probe showed very significant variations
during the exposures that had durations of at least 2,000 hours.
In the potassium-rich environment of the Covington probe two alloys (N06690 and S21500) seemed to
demonstrate corrosion resistance that would suggest they would likely perform satisfactorily in a
potassium-rich environment at a temperature 100 Celsius degrees above current operating temperatures.
For the chloride-rich environment of the Crofton boiler, essentially all alloys showed fairly low
degradation rates when exposed at temperatures below about 500°C, but the six alloys that had samples
exposed above about 525°C all showed greatly accelerated rates above that temperature. Both alumina
forming alloys (N06025 and N07214) performed very well below about 510°C, but, as noted, both alloys
had much higher rates above 525°C.
The environment of the Gadsden probe likely showed small variations as the amount of wood varied, but
that variation was probably considerably less than that of the environment in the other boilers studied
because of the expectation of consistent steam production from this power boiler. All samples exposed in
the Gadsden boiler showed relatively low degradation rates, possibly because of the absence of significant
amounts of alkali metals and chlorides.
The presence of zinc and/or lead in the environment of the Port Mellon boiler was not expected when the
exposure sites were selected, but this provided some very interesting results. Essentially all the alloys
(except S31009) showed higher degradation rates in the 400-430°C range, and this very likely can be
attributed to the presence of Zn and/or Pb in the deposits. Even though the average sample temperatures
on this corrosion probe were well below the desired range, enough information was collected to note that
degradation rates for almost all alloys tended toward higher values even at 40 or more Celsius degrees
below the temperature goal.
It is generally expected that the corrosion resistance of an alloy will improve with increasing chromium
content. However, that was not a pattern that fits the results of the corrosion probe studies. Alumina
forming alloys are sometimes an alternative to chromia forming alloys because of an improved resistance
in some aggressive environments, but the alumina forming alloys did not consistently perform well on
these corrosion probes. It is worth noting that the alumina forming alloys often perform better at
considerably higher temperatures, and the temperatures to which the probes were exposed may not have
been high enough to get the best features of the alumina forming alloys.
84

2.5 ECONOMICS
The 1997 Kyoto Protocol set the goal of stabilizing greenhouse gas concentrations in the atmosphere at a
level that would avoid dangerous climate change by obliging industrialized countries to reduce such
emissions. European countries that ratified this protocol have adopted systems of incentives and penalties
to reduce greenhouse gas emissions. Many have developed and implemented technologies that improve
the efficiency with which steam and power can be generated from biomass fuels. Biomass fuels are
attractive for power generation because they are renewable and almost carbon-neutral. However, the
combustion of biomass produces superheater ashes that contain corrosive elements like chlorine,
potassium and sodium. When climate change and renewable fuels were of less concern, outlet steam
temperatures of biomass-fueled boilers were kept low to avoid fireside corrosion of superheater tubes
and/or pluggage in the convective sections. Such temperature limitations restricted the power that could
be generated from biomass fuels.
As part of the project to evaluate corrosion mitigation strategies that would enable biomass-fueled boilers
to operate with higher superheater steam temperatures this task analyzed the economic impacts of higher
superheater temperatures in biomass-fueled boilers [119]. Boiler performance and process conditions
were estimated using proprietary thermodynamics-based plant simulation software. We present financial
calculations of the benefits of increased superheated steam temperatures based on the analysis of steam
and power production in five example boilers burning biomass. These financial benefits are compared
with the additional costs of alloys that could resist corrosion at the higher superheater temperatures.
Where the financial benefits exceed these costs, using more corrosion-resistant alloys to enable higher
steam temperatures offers a net financial benefit to the boiler operator. Second, we compare the financial
benefits of higher steam temperatures with the cost of fuel treatments or additives [3] applied to reduce
the concentration of corrosives in the superheater ash. Third, we compare the financial benefits with the
cost of boiler redesign, e.g. of constructing a circulating fluidized bed (CFB) boiler with the superheater
in the loop seal [3] instead of in the convective pass.
2.5.1 Calculation Methods
The primary tool used for these calculations is a thermodynamic software program developed by the
second author of this paper. This program, called StmPowr®1, models Combined Heat and Power (CHP)
0F
systems that supply process steam to an adjacent plant (or sell it for district heating) and simultaneously
generate electricity for plant use or external sale. For example, in a pulp and paper mill, a typical steam
turbine would supply high-, medium- or low-pressure steam to dry paper, evaporate water from black
liquor and heat process units such as pulp digesters. It would also generate electrical power.
StmPower® calculates the net electrical power and process steam generated from a Rankine cycle power
plant. Almost all power plants use the Rankine cycle as their heat engine. This cycle has four
components. First, the working fluid (boiler feedwater) is pressurized by a pump. The high pressure
water is heated at constant pressure to become a dry saturated vapor (steam). This dry steam expands
through a steam turbine, generating power and lower pressure process steam. The remaining turbine
exhaust steam is condensed immediately or later to a saturated liquid. The working fluid (condensate) is
recirculated and heated to become boiler feedwater, continuing through a closed condensate – boiler
feedwater – steam loop.
Required inputs to the software model include the rate of fuel input, the fuel characteristics (elemental
composition, gross heating value, and temperature) and process and equipment parameters for various
1 Available from Table Mountain Consulting, 1024 Tucker Gulch Drive, Golden, CO 80403;
http://tmcjimfred.com/TMCLLC/Welcome.html
85

unit operations that will be described below. The software uses the flow rate, temperature and pressure of
the inlet steam and turbine efficiency parameters to predict the temperature, pressure and flow rates of the
steam extracted from the turbine and the power generated. Figure 51 shows the configuration and the
process mass and energy streams included in the model. The StmPowr® software calculates the flow
rates and conditions of the process streams that cross the process boundary (red dashed line) in this figure.
Fig. 51. Process mass and energy streams included in the software model.
The Rankine cycle analyzed by the StmPower® model consists of seven unit processes:
Boiler
Steam turbine
Exhaust steam surface condenser
Condensate transfer pump
Deaerator
Boiler feedwater pump
Combustion air preheater
We will discuss each of these unit processes in turn.
2.5.2 Components of the Steam Power Cycle Calculation Module
2.5.2.1 Boiler
The boiler sub-module calculates the net rate of high-pressure steam generation at specified steam
conditions (T, P) and other specified parameters from the fuel input rate, as shown in Table 7. The steam
rate calculation is based on the heat loss method (120, 121).
86

Table 7: Components of boiler sub-module
Specified input conditions Specified exit conditions Calculated parameters
Fuel input rate and temperature, gross Temperature and pressure Thermal efficiency of
heating value of dry fuel, fuel moisture of the superheated steam boiler
content and elemental composition produced
Combustion air input rate, temperature and Blowdown rate Rate of generation of
moisture content high pressure,
superheated steam
Boiler feedwater temperature and pressure Boiler feedwater input
rate
Internal steam used for air heating and Flue gas exit composition
sootblowing (pressures, temperatures and
flows)
Correlation between flue gas exit Ash output rate
temperature and fuel input rate
2.5.2.2 Steam Turbine
The steam turbine sub-module calculates the power generated by the calculated flow of superheated steam
generated by the boiler. The turbine operates at its own specified isentropic efficiency. The power
generated is calculated from the temperature, pressure steam and flow rate of the steam flowing to the
turbine, the temperatures, pressures and flow rates of process steam extracted from the turbine and the
temperature, pressure and flow rate at the turbine exhaust, as shown in Table 8.
Table 8: Components of the steam turbine sub-module
Specified input conditions Specified exit conditions Calculated parameters
Flow rate of high pressure Pressures and flow rates of Power generated for the steam
superheated steam to the process steam extracted from the conditions specified
turbine inlet turbine
Temperature and pressure of Temperatures of process steam
steam delivered to the turbine extracted from the turbine
Isentropic efficiency of the
turbine
2.5.2.3 Exhaust Steam Condenser
For condensing turbines, this sub-module calculates the cooling water flow required to condense the
exhausted steam at its specified temperature, pressure and flow rate as summarized in Table 9. This
condensate returns to the deaerator for reuse as boiler feed water.
Table 9: Components of exhaust steam condenser sub-module
Specified input conditions Specified exit conditions Calculated parameters
Temperature, pressure and flow Temperature and pressure of Flow of cooling water required to
rate of turbine exhaust steam condensate condense exhausted steam
Temperature and pressure of Inlet temperature of cooling
steam extracted to the deaerator water
Feed water make-up rate and Outlet temperature of cooling
temperature water
87

2.5.2.4 Condensate transfer pump
The condensate transfer pump moves the condensate from the turbine steam condenser sump to the
deaerator. Components of the sub-module are shown in Table 10.
Table 10: Components of condensate transfer sub-module
Specified input conditions Specified exit conditions Calculated parameters
Temperature, pressure and flow Deaerator pressure Power required by condensate
rate of condensate from the transfer pump
condensate sump
Pump and motor efficiency
2.5.2.5 Deaerator
Boiler makeup feedwater is added to the condensate in the deaerator. This combined feedwater is heated
to the saturation temperature at the deaerator pressure by steam extracted from the turbine. The
components of the deaerator sub-module are listed in Table 11.
Table 11: Components of the deaerator sub-module
Specified input conditions Specified exit conditions Calculated parameters
Temperature, pressure and flow Boiler feedwater temperature Flow rate of steam extracted
rate of condensate return to from the turbine to the deaerator
deaerator at the specified temperature and
pressure
Temperature and flow rate of
boiler feedwater make-up
Temperature, pressure and flow
rate of steam used for deaerator
heating
2.5.2.6 Boiler Feedwater Pump
The boiler feedwater pump raises the pressure of the boiler feedwater from the pressure in the deaerator
up to the boiler inlet pressure, as shown in Table 12.
Table 12: Components of the boiler feedwater pump sub-module
Specified input conditions Specified exit conditions Calculated parameters
Temperature, pressure and flow Pressure of feedwater at boiler Power required by boiler
rate of boiler feedwater flow inlet feedwater pump
from deaerator
Efficiency of the feedwater
pump and motor
2.5.2.7 Combustion air preheater
The combustion air preheater is a heat exchanger that uses turbine extraction steam to heat the outside air
from ambient temperature to the temperature required for fuel combustion, as summarized in Table 13.
Table 13: Components of the combustion air sub-module
Specified input conditions Specified exit conditions Calculated parameters
88

Temperature and pressure of Temperature of combustion air Required flow rate of steam
steam extracted from turbine to entering boiler extracted from turbine to heat
heat combustion air combustion air
Temperature of ambient air
entering preheater
2.5.3 Boiler Systems Analyzed
To determine the magnitude of the economic costs and benefits of higher superheater steam conditions,
we asked industrial collaborators in the project to supply data from typical biomass-fueled boilers.
Calculations were made with data from five boilers – two recovery boilers and three boilers burning
hogged wood. Hogged fuel is produced from waste bark or wood that has been processed by a
disintegrator, or hog, that processes the wood into chips or shreds of practically uniform size. The boilers
used for the calculations are as follows. Data for Recovery Boiler B were supplied by a boiler
manufacturer as part of a software model of a recovery boiler in a typical pulp mill where process steam
is extracted from the turbine. The steam data for Recovery Boiler M came from a WinGEMS2 software
1F
model of a 1000 oven-dried tons per day unbleached pulp mill with a recovery boiler operating at 1450
psi. These two recovery boilers produced power outputs of 52 and 53.6 MW with conventional steam
conditions.
All the biomass boilers were real units. Biomass Boiler C operates on the Pacific Coast and is fired by
hogged fuel produced from sea-floated logs. Biomass Boiler H also operates on the Pacific Coast, but
fires about 2/3 beetle-killed pine, about 1/3 sea-floated logs and a small amount of wood from
construction waste. Biomass Boiler M is a biomass boiler recently converted to bubbling fluidized bed
operation by a boiler manufacturer. It burns hogged wood.
Figure 52 illustrates the difference between the two types of steam turbine that are used in the calculations
that will follow. Condensing CHP turbines are shown schematically in Figure 52(a). Steam used to turn
(a) Condensing CHP turbine (b) Non-condensing CHP turbine
Fig. 52. Types of steam turbine used in calculations of costs and benefits of increasing superheater steam
temperature.
the rotor is extracted at high, medium and low pressures (or sometimes at only two pressures). Any
remaining steam is then condensed in water-cooled tubes in a surface condenser. Non-condensing (back-
2 Now available as Metso Process Simulator from Metso Automation USA, Norcross, GA.
89

pressure) turbines, shown schematically in Figure 52(b), extract all the steam used to turn the turbine rotor
as process steam to be used in an adjacent plant.
Both of the example recovery boilers deliver their steam to condensing turbines while all three wood-fired
boilers deliver their steam to non-condensing turbines. Condensing turbines use all the steam supplied by
the boiler to turn the turbo-generator rotor and generate power. Steam that has passed through the full
length of the turbine is condensed on water-cooled tubes in a surface condenser. This condensation
decreases the volume of the steam by about 1,800 times and creates a vacuum in the condenser. Surface
condensers can produce pressures of 90 to 100 kilopascals (13 to 14.5 psi) below atmospheric pressure.
Creating this vacuum allows the steam supplied by the boiler to expand much more, producing a larger
enthalpy change through the turbine and increasing the turbine efficiency. For this reason, utility boilers,
where efficiency is of primary importance, always use condensing turbines. Note that the vacuum
pressure developed by the surface condenser depends on the temperature of the cooling water, which
could be subject to seasonal changes, and on the partial pressures exerted by non-condensable gases
accumulated in the feedwater. Because the turbine efficiency increases as the condenser vacuum
increases, accumulated non-condensable gases should be stripped out and the condensing temperature
should be kept as low as possible. The steam condensate, stripped of non-condensable gases, is returned
to the boiler as feed water.
The simplest non-condensing (back-pressure) steam turbine would extract all the steam used to drive the
turbo-generator rotor as process steam at a series of decreasing pressures. “Back-pressure” simply
indicates that the steam is extracted at pressures above atmospheric. The process steam flows are
extracted at the pressure(s) required by the process operations regardless of the load on the turbine. This
is achieved by controlling the steam flows at the extraction points. The extraction pressures are chosen to
suit the particular process steam requirements of the plant where the boiler is located. The extracted
steam can be used in an adjacent process plant (e.g. a pulp and paper mill or chemical plant) or for district
heating. The steam condensate is later augmented by make-up boiler water, deaerated and returned to the
boiler.
Once saturated steam has been generated in a boiler, relatively little additional fuel energy is required to
raise its temperature and pressure to the superheat required to provide more efficient power generation.
Therefore if a process plant already needs a substantial amount of process steam, adding a non-
condensing turbine offers a simultaneous supply of relatively inexpensive power without the need for the
substantial volumes of cooling water that would be required to operate a surface condenser in a
condensing turbine. However, the capacity of a turbine to generate power falls substantially when
process steam is extracted at appreciable pressure instead of being expanded into a vacuum in a surface
condenser.
The biomass-fueled boilers studied in the current project all produce a combination of heat and power
(CHP). All of them provide process steam to an adjacent plant and all of them generate power. All are
once-through turbines that do not take advantage of the efficiencies of reheating the steam in the boiler
between various turbine stages.
2.5.4 The Thermodynamic Basis for the Increasing Value of Steam with Increasing Temperature
The principle that underlies the work described in this paper is that the availability of energy in steam
increases as the temperature of the steam increases. Availability, also called available energy, is a
thermodynamic property like enthalpy. Gibbs introduced this concept in 1873 [122] by defining
"capacity for entropy" as the amount by which the entropy of a body can be increased without changing
the energy of the body or increasing its volume. For steam, the available energy is the maximum amount
90

of mechanical work that can be obtained from it in an ideal engine by bringing it to the temperature and
pressure of a reference atmosphere without allowing heat to pass into it or out of it, i.e.:
Available energy = Enthalpy of steam – (Entropy of steam) x (Temperature of surroundings)
More rigorously:
a = h – T s (11)
0
where:
a = specific available energy, kJ/kg
h = specific enthalpy, kJ/kg
T = absolute temperature of the surroundings, °K
0
s = specific entropy, kJ/kg
Consider the effect of increasing temperature on the steam parameters in this equation. Figure 53 shows
that, as the temperature of a unit mass of steam at constant pressure increases, its specific enthalpy
increases. Figure 54 shows that the specific entropy of the steam also increases with the steam
temperature at constant pressure.
4000
3500
3000
400 500 600 700
Fig. 53. Increase of specific enthalpy of steam with temperature at 50 and 100 bars pressure (725 and 1450
psi).
The availability of energy from the steam increases with increasing temperature because the specific
enthalpy of steam increases proportionally more with temperature than does the specific entropy of steam.
This conclusion is demonstrated in Figure 55, which shows the temperature dependence of the specific
available energy of steam at boiler pressures of 50 bars (725 psi) and 100 bars (1,450 psi) within the
temperature range of interest in this work. These data lead to the practical conclusion that, for a turbine to
derive the most energy from the steam produced by a boiler fuel, the boiler should be designed to produce
steam at the highest temperature that its superheater metallurgy allows.
It is important to note that the volume of a given mass of steam heated by burning a given amount of fuel
to heat will fall as the final temperature of the steam increases. In the data presented in Figure 54, raising
the steam temperature from 500°C to 600°C without changing the fuel input to the CHP plant reduces the
volume of steam produced by 6.6% at a pressure of 50 bars (725 psi) and by 7.2% at a pressure of 100
bars (1450 psi). Whether or not this reduction in steam volume presents a problem in plant operation will
depend on the process steam requirements and the turbine design. In a condensing turbine, the smaller
91
,maets
fo
yplahtnE
cificepS
gk/jk
1450 psi
725 psi
Steam Temperature, °C

7.4
7
6.6
6.2
400 500 600 700
Fig. 54. Increase of specific entropy with temperature at 50 and 100 bars pressure (725 and 1450 psi).
Fig. 55. Increase in specific available energy in steam with increasing steam temperature at constant pressure.
volume of steam produced at a higher temperature could, in principle, be redistributed among the
extraction stages by controlling the steam flows at the extraction points. However, in a back-pressure
turbine, it may not be possible to maintain the process steam flows if the steam volume is reduced by
heating the steam to a higher final temperature.
Table 14 lists the steam parameters for the two recovery boilers and the three wood-fired boilers studied
in the economic calculations. The boiler parameters were supplied by project partners. Three of these
example boilers used for the calculations were also used for field tests to measure the corrosion resistance
of candidate alloys in higher temperature superheater environments.
The steam extraction temperatures used in the calculations were recalculated from the extraction
pressures using standardized turbine stage efficiencies to determine the entropy of the steam extracted.
The condensate temperatures were adjusted to those of saturated condensate at atmospheric temperature.
These calculations used the procedures proposed by Ulrich [123], although similar calculation procedures
are presented in other engineering thermodynamics and process design texts. The turbine stage
efficiencies used for the recovery boiler calculations were provided by an Industrial Partner [124] and the
92
,maets
fo
yportnE
cificepS
gk/jk
725 psi
1450…
Steam Temperature, °C
1800
1600
1400
1200
400 500 600 700
,ygrenE
elbaliavA
cificepS
gk/Jk
725 psi
1450 psi
Temperature, °C

turbine stage efficiencies used for the biomass boiler calculations were estimated from data presented by
Ulrich (Reference 123, page 87).
Table 14 Steam system parameters for the five boilers studied
Recovery Boiler Biomass (wood)-Fired Boiler
Boiler type and identifier code
B M C H M
Steam Production, kg/sec 91.8 101.68 119.7 59.98 60.48
Steam Pressure, bar 61.22 99.66 41.84 89.63 89.63
Steam Temperature, °C 465.6 471.1 399.0 482.2 480.0
HP Steam Pressure, bar N/A N/A N/A N/A 28
HP Steam Temperature, °C N/A N/A N/A N/A 328.2
HP Steam Enthalpy, kJ/kg 2933.74 2838.42 3132.56 3146.11 3069.18
HP Steam Extraction Flow, kg/sec 0 0 0 0 15.12
MP Steam Pressure, bar 12.75 12.75 11.22 12.75 12.75
MP Steam Temperature, °C 247.8 190.86 335.2 330.2 287.4
MP Steam Enthalpy, kJ/kg 2923.63 2814.46 3124.03 3110.13 3016.76
MP Steam Extraction Flow, kg/sec 8.82 39.31 15.12 15.00 6.05
LP Steam Pressure, bar 5.10 5.10 4.15 4.15 4.15
LP Steam Temperature, °C 152.60 152.60 177.1 175.9 167.9
LP Steam Enthalpy, kJ/kg 2768.81 2756.43 2811.52 2808.91 2791.51
LP Steam Extraction Flow, kg/sec 63.76 48.26 104.58 44.99 39.31
Exhaust Steam Pressure, bar 0.14 0.14 N/A N/A N/A
Exhaust Steam Temperature, °C 100 100 N/A N/A N/A
Exhaust Steam Enthalpy, kJ/kg 2715.63 2711.29 - - -
Exhaust Steam Flow, kg/s 19.22 14.11 0 0 0
Condensate Flow, kg/s 72.58 87.57 119.7 59.98 60.48
Condensate Pressure, bar 18 18 1.24 1.24 1.24
Adj. Condensate Temperature, °C 108.5 108.5 100 100 100
Intrinsic turbine stage efficiencies:
High pressure stage 0.890 0.890
Medium pressure stage 0.459 0.459
0.813 0.813 0.813
Low pressure stage 0.887 0.887
Exhaust stage 0.650 0.650
2.5.5 Economic Calculations
Many different approaches could be taken to calculations of the effects of increasing the outlet steam
temperatures of a biomass-fueled boiler. Different sets of constraints could be applied to evaluate the
effects of specific local factors such as changing needs for process steam, opportunities to sell high-priced
power or a decision to install a new high-efficiency turbine. The purpose of the current project was to
estimate the economic benefits that would accrue to a boiler operator if a biomass-fueled boiler could be
operated with substantially higher exit steam temperatures. To make these estimates, calculations were
made with the data from Table 14. The value of the increased steam and power production that would be
obtained by increasing the steam temperature by 50 and by 100 Celsius degrees was calculated for each of
the five example boilers, using the following assumptions:
93

The existing turbine could operate with the higher temperature steam
The heat produced by the combustion of the fuel would be unchanged when the final steam temperature
was increased
The product of specific steam enthalpy and steam flow would be unchanged when the final steam
temperature was increased
The amount of steam extracted from the turbine to meet process heating requirements would remain
unchanged when the final steam temperature was increased
We will first review the results of calculations made with these assumptions and later discuss the
uncertainties associated with these assumptions.
Table 15 shows the value of the increased power that would be produced in the two example recovery
boilers that would accrue to the owners of these boilers if they could increase the exit steam temperature
by 50 or 100 Celsius degrees above the current operating temperature. Because the value of electrical
power varies both with location and with time, the value of the additional power generated was calculated
for power prices of both $40/MWh and $80/MWh. Current power prices typically lie within this range.
Table 15: Value of increased energy production in the two example recovery boilers
Recovery Boiler
Type of boiler and identifier
B M
Condition/data
Current power generation 52.0MW 53.6MW
Power generated with 50°C higher steam temperature 56.4MW 60.8MW
Additional power generated +4.4MW +7.2MW
+8.4% +13.4%
Value of this additional power @$40/MWh +$1.54m/y +$2.52m/y
Value of this additional power @$80/MWh +$3.08m/y +$5.05m/y
Power generated with 100°C higher steam temperature 59.0MW 66.3MW
Additional power generated +7.0MW +12.7MW
+13.4% +23.7%
Value of this additional power @$40/MWh +$2.45m/y +$4.45m/y
Value of this additional power @$80/MWh +$4.91m/y +$8.90m/y
In related work, three types of virtual turbine were studied to evaluate the effects of higher steam
conditions in Recovery Boiler M. In the first case, the turbine generator was optimized for the original
(conventional) steam conditions and was therefore less efficient at the higher steam temperatures. In the
second case it was assumed that the turbine generator used for higher steam conditions was optimized for
these conditions, i.e. that the turbine efficiency remained constant as the steam conditions were increased.
In the third case a reheater was added between the high pressure and medium pressure turbine extractions.
These calculations showed that increasing the isentropic efficiencies of the various turbine stages towards
the maximum attainable efficiency increases the amount of power generated as much as increasing the
steam temperature. This shows the value of using a steam turbine designed for higher steam conditions
when redesigning a boiler to produce higher temperature steam.
Table 16 shows the value of the increased power that would be produced in the three example wood-fired
boilers assuming that the isentropic efficiency of the steam turbine was maintained at the higher input
steam temperature.
Table 17 summarizes the calculated economic benefits of increased exit steam temperatures in all five
example boilers under the previously-stated assumptions. These results indicate that very substantial
94

economic benefits would accrue if biomass boilers could be designed to operate with higher superheater
steam temperatures.
Table 16: Value of increased power that could be produced by raising exit steam temperatures by 50 and by
100 Celsius degrees in the three example wood-fueled boilers.
Wood-fired Boiler
Type of boiler and identifier
C H M
Parameter 42.8MW 27.5MW 27.4MW
Current power generation 42.8MW 27.5MW 27.4MW
Power generated with 50°C higher steam temperature 51.2MW 31.3MW 31.0MW
+8.4MW +3.8MW +3.6MW
Additional power generated
+19.6% +13.8% +13.1%
Value of this additional power @$40/MWh +$2.94m +$1.33m/y +$1.26m/y
Value of this additional power @$80/MWh +$5.87m +$2.66m/y +$2.52m/y
Reduced volume of steam generated with 50°C higher steam 3.22 kg/s 2.18 kg/s 2.2 kg/s
temperature
Power generated with 100°C higher steam temperature 58.8MW 34.9MW 34.3MW
Additional power generated +16.0MW +7.4MW +6.9MW
+37.3% +26.9% +25.1%
Value of this additional power @$40/MWh +$5.59m/y +$2.59m/y +$2.41m/y
Value of this additional power @$80/MWh +$11.18m/y +$5.17m/y +$4.82m/y
Reduced volume of steam generated with 100°C higher steam
8.09 kg/s 4.15 kg/s 4.2kg/s
temperature
Table 17: Summary of calculated value of additional power generated by raising exit steam temperatures by
50 and 100 Celsius degrees
Recovery Boilers Biomass Boilers
Parameter
B M C H M
+50°C steam
Increased value @$40/MWh +$1.54m +$2.52m/y +$2.94m/y +$1.33m/y +$1.26m/y
Increased value @$80/MWh +$3.08m +$5.05m/y +$5.87m/y +$2.66m/y +$2.52m/y
+100°C steam
Increased value @$40/MWh +$2.45m/y +$4.45m/y +$5.59m/y +$2.59m/y +$2.41m/y
Increased value @$80/MWh +$4.91m/y +$8.90m/y +$11.18m/y +$5.17m/y +$4.82m/y
The magnitude of the increased power generated at higher temperatures in these calculations is similar to
that published by groups in Sweden [125] and Denmark [126]. Stålenheim and Henderson [125] have
presented similar plots of the increase of electrical efficiency with final steam temperature at various
steam pressures in advanced steam cycle units. Kamuk ([126] commented that the electrical efficiency of
biomass-fueled boiler systems is typically limited to about 35%, compared to about 49% for coal fired
boiler systems, because of superheater corrosion. She also noted that achieving higher steam conditions
is the key to raising electrical efficiency.
The most attractive route to achieving higher steam temperatures appears to be to identify new
superheater alloys or composite tube materials that can resist corrosion and creep in the flue gas and fuel
ash environment around superheater tubes in biomass boilers. If suitable tubing were installed in the
hottest portions of a biomass-fueled boiler’s superheater, the boiler owner would make a net profit if the
additional cost of this tubing did not exceed the value of the additional steam generated. For example, if
5 meters of high alloy tubing were installed in each of ten superheater loops in 45 platens (for a total of
2,250 meters) and served for 5 years before being replaced, tubing costs of less than $5,378 to $24,911
95

per meter would more than pay for a 100 Celsius degree increase in steam temperature. Current costs of
superheater tubing are about two orders of magnitude lower than the lowest of these estimates of the
justifiable cost. To gain the full financial advantage of tubes designed for a five-year replacement life, it
would be useful to also design the superheater for rapid replacement. It was noted in an earlier
publication [3] that the superheater of a 67 MW waste-fired boiler operated by the City of Amsterdam,
which had been designed for rapid replacement, was recently replaced in 48 hours, from fire-to-fire.
A second route to enabling higher steam conditions would be to chemically treat the biomass fuel to
remove corrosive components before or during combustion. This could involve diluting a corrosive
biomass fuel with a less-corrosive fuel, leaching corrosives out of biofuels3 or using additives (such as
2F
ammonium sulfate or SO ) that convert alkali chlorides to less corrosive sulfates, or additives such as
2
kaolin (40-60 wt% Al O .SiO ) that convert alkali salts to less-corrosive silicates. More details about
2 3 2
these approaches is available [3]. If the corrosivity of the biomass fuel could be reduced by pre-treatment
or by combustion additives, the fuel processing would have to cost less than $2,420,000 to $11,210,000
per year to justify the increased value of the power generated by producing steam 100 Celsius degrees
hotter than current values.
Other approaches to enabling higher steam conditions that have been implemented in Europe [3] involve
re-designing biomass-fueled boilers to maximize the service life of superheater tubes by separating the
superheater tubes from the corrosive fly ash (either by adding an empty pass between the furnace and the
superheater or by condensing the fly ash on low temperature tubes in a “Chlorine Trap”), by increasing
the superheater temperature above the dew point temperature of corrosive components of the fly ash, by
moving the superheater of a circulating fluidized bed boiler (CFB) out of the flue gas passage into the
recirculated fluidizing medium and by using an external superheater fired by a less-corrosive fuel. With
the current abundance and relatively low cost of natural gas in the United States, this last approach
appears particularly attractive. To justify the financial benefit of the increased power production provided
by a 100 Celsius degree steam temperature increase within 5 years, the capital costs of boiler design
changes would have to be less than $12,000,000 to $56,000,000. The magnitude of these financial gains
associated with increased steam temperatures appears to justify substantial boiler redesign or fuel
treatment.
2.5.6 Issues Raised By Simplifying Assumptions
We will now review the credibility of the simplifying assumptions that were used to calculate the
potential benefits of increased steam conditions. The first assumption, that the existing turbine could
handle the higher temperature steam, is probably not true. Steam turbines have designs and materials of
construction optimized for particular steam conditions and the calculations described above for Recovery
Boiler M indicate that the efficiency of an existing turbine would be substantially lower if it operated with
a steam temperature 100 Celsius degrees higher than its design conditions. Substantial infusions of
capital could be required to simultaneously upgrade both biomass-fueled boilers and their turbines to take
advantage of the increased power generation potential of hotter steam. However we have shown above
that the value of the additional steam generated would more than justify the cost of any foreseeable
corrosion-resistant alloy tubing and that the increased cost of a turbine designed to handle higher
temperature steam could probably be paid off by the value of the additional steam generated in one or two
years. New biomass-fueled boilers are being built every year and will very likely be designed for
efficient combustion and efficient steam generation, following the approaches discussed here.
3 Although water leaching is claimed to remove >80% of the potassium and sodium and >90% of the chlorine from
some biomass fuels, the process is not yet economic because of the cost of subsequent drying of the fuel (1).
96

The second assumption in the calculations is that the heat produced by the combustion of the fuel remains
unchanged. This assumption appears reasonable. The firing of the fuel in the furnace and the volume of
water supplied to the boiler would not be changed, but the steam would be heated to a higher final
temperature in the superheater. The final steam temperature would be raised by extracting more heat in
the superheater, most likely by redesigning the superheater to add more heat transfer surface. Increasing
the heat transfer surface in the superheater would require installing additional tube platens or extending
the existing platens. Although the costs of this type of rebuild are highly plant-specific, the financial
calculations suggest that these capital costs could be paid for by two to five years of additional power
production. The third assumption – that the product of the steam enthalpy and the steam flow would be
unchanged – is closely related to the second. This assumes that the amount of heat transferred to the
steam is unaffected by raising the final temperature of the steam. This assumption also seems reasonable.
The fourth assumption in the calculations is that the amount of steam extracted from the turbine for
process heating would remain constant. The provision of process steam is a critical function of CHP
turbine generators. However, we noted above that raising the final temperature of steam in a boiler
reduces the total volume of the steam produced. In condensing turbines, it may be possible to adjust the
extraction flows so as to maintain the existing requirements for process steam while reducing the steam
flow to the surface condenser. Table 18 shows calculations of the steam flows in the turbines used by
Recovery Boilers B and M as the temperature of the steam delivered by the boiler is raised by 50 and by
100 Celsius degrees above current operating conditions. The total volume of steam produced falls by
6.6% in boiler B and by 7.2% in boiler M as the temperature is raised by 100 Celsius degrees.
Fortunately, for both of these boilers, it would be possible to maintain the flows of medium and low
pressure steam from the turbine by reducing the volume of steam exhausted to the surface condenser
(Table 25).
Table 18: Calculations of redirected steam flows in the steam turbines of Recovery Boilers B and M as the
inlet steam temperature is raised by 50 and by 100 Celsius degrees.
Steam Flow, kg/sec
Recovery
Boiler HP MP LP
Case Exhaust Total
Extraction Extraction Extraction
B Current operation 0 8.82 63.76 19.22 91.80
B + 50°C steam 0 8.82 63.76 16.04 88.62
B +100°C steam 0 8.82 63.76 13.12 85.70
M Current operation 0 39.31 48.26 14.11 101.68
M + 50°C steam 0 39.31 48.26 10.27 97.84
M + 100°C steam 0 39.31 48.26 6.82 94.39
The three wood-fueled boilers in this study all use non-condensing, back-pressure turbines. These have
no exhaust flow to make up for the reduced volume of hotter steam that would be produced if their final
steam temperature was increased. The steam flow calculations for these turbines presented in Table 19
are similar to those for the condensing recovery boiler turbines in Table 18. As with the recovery boilers,
the total volume of steam produced falls as the final steam temperature is raised. This would reduce the
total steam flow by 6.76% in boiler C, by 6.93% in boiler H and by 6.94% in boiler M. The steam flows
from the various turbine extraction points would be correspondingly reduced. Although a pulp and paper
mill that has implemented substantial energy savings since its non-condensing turbine was installed might
be able to operate with these reduced flows of process steam, this will generally not be possible.
However, three other approaches could be used to maintain the volumes of process steam while still
obtaining the benefits of increased power generation. Probably the most economic would be to
attemperate the steam either by a water spray or by passing some of it through a heat exchanger cooled by
97

boiler feedwater. Other approaches would be to fire slightly more wood fuel in the boiler or to purchase a
small amount of make-up steam from another source.
Table 19: Calculations of steam flow reductions in the steam turbines of Biomass-Fueled Boilers C, H and M
as the inlet steam temperature is raised by 50 and 100 Celsius degrees.
Steam Flow, kg/sec
Biomass
Boiler HP MP LP
Case Exhaust Total
Extraction Extraction Extraction
C Current operation 0.00 15.12 104.58 0.00 119.70
C + 50°C 0.00 14.59 100.89 0.00 115.48
C +100°C 0.00 14.10 97.51 0.00 111.61
H Current operation 0.00 15.00 44.99 0.00 59.99
H + 50°C 0.00 14.45 43.35 0.00 57.80
H + 100°C 0.00 13.96 41.87 0.00 55.83
M Current operation 15.12 6.05 39.31 0.00 60.48
M +50°C 14.57 5.83 37.88 0.00 58.28
M +100°C 14.07 5.63 36.58 0.00 56.28
2.5.7 Environmental Benefits of Higher Steam Conditions
Increasing the energy efficiency of biomass-fueled boilers would directly improve energy efficiency in all
industries that use biomass fuels. In addition, improvements in energy efficiency would make renewable
fuels more attractive as replacements for fossil fuels.
Assuming there are at least 500 biomass-fired boilers in the U.S. that could be converted within a ten-year
period to operate with final steam temperatures 100 Celsius degrees above current conditions and that the
additional energy generated would replace energy currently produced from fossil fuels. The cumulative
savings resulting from use of biomass instead of a natural gas for this incremental increase in energy
would be as shown in Tables 20 and 21. These calculations assume that power production would increase
25% with a 100°C increase in final steam temperature, based on the increases calculated in Tables 14 and
15 above.
Table 20: Cumulative energy benefits from using additional energy produced in improved biomass-fired
boilers to displace energy from fossil (natural gas) fired boilers
Year 2020 Year 2025
Total primary energy displaced 268 trillion Btus 1,406 trillion Btus
Cumulative economic benefit $1.5 billion/yr $8.5 billion/year
Table 21: Cumulative environmental benefits from using additional energy produced in improved
biomass-fired boilers to displace energy from fossil (natural gas) fired boilers
Year 2020 Year 2025
CO emissions displaced (C equivalent) 5.3 million tons 27.4 million tons
2
NO reductions 47,000 metric tons 243,000 metric tons
x
Replacing fossil fuel boilers with renewable fuel boiler would also bring substantial economic benefits.
Assuming that state-of-the-art biomass-fired boilers could economically replace fossil fuel units, then for
500 installed units with a 2% growth rate per year, an ultimate potential accessible market of 90% and a
likely technical market share of 90%, there could be 21% market penetration in 2020 and 71% penetration
98

in 2025. The savings shown in the Table 22 and 23 are based on the replacement of fossil fuel (natural
gas) fired boilers.
Table 22: Cumulative energy benefits from replacing natural gas fired boilers with biomass-fired boilers
Year 2020 Year 2025
Total primary energy displaced 160 trillion Btus 866 trillion Btus
Cumulative economic benefit $774 million/yr $4,300 million/yr
Table 23: Cumulative environmental benefits from replacing fossil fuel (natural gas) fired boilers with
biomass-fired boilers
Year 2020 Year 2025
CO emissions displaced (C equivalent) 2.31 million tons 12.5 million tons
2
NO reductions 17,000 metric tons 92,000 metric tons
x
2.5.8 Discussion and Conclusions
It was noted earlier that biomass-fueled boilers typically operate with electrical efficiencies about 35%,
substantially lower than that those of coal-fired units [126] because their final steam conditions are
limited in order to restrict fireside corrosion of the superheater tubes. In Europe, where the development
of power from renewable fuels has been defined as a strategic priority by many nations, innovative
approaches have been developed to improve the efficiency of biomass-fueled boilers, not only by
identifying alloys with greater corrosion resistance [4], but also by using combinations of design
modifications, process modifications and corrosion-resistant alloys to enable higher steam conditions [3].
The calculations presented here using data from two recovery boilers and three wood-fired boilers suggest
that the value of the increased power that could be generated if the steam in a biomass-fired boiler could
be heated 50 Celsius degrees above current operational temperatures would be worth between about
$1,260,000 and $5,890,000 per year. If the steam could be heated 100 Celsius degrees above current
operational temperatures, the increased value of the power generated would be between about $2,420,000
and $11,210,000 per year. Gains for other biomass-fueled boilers would depend on local plant conditions
and the price of power. The calculations indicate that the increased steam value could justify the use of
corrosion resistant alloys costing orders of magnitude more than current superheater alloys if the use of
more corrosion-resistant alloys were coupled with the introduction of superheater designs that allowed
very rapid superheater replacement.
Most modern wood-fired boilers in Europe also incorporate design improvements to remove corrosive fly
ash before it reaches the superheater, or to remove the superheater from the flue gas path altogether.
Given the likelihood of relatively low natural gas prices for many years, the option of installing an
external superheater fired by this less-corrosive fuel seems a particularly attractive route to higher
superheated steam temperatures. To achieve a five-year payback, a boiler redesign and rebuild to
achieve a 100 Celsius degree steam temperature increase would have to cost less than $12,000,000 to
$56,000,000. A wood-fired boiler at Nässjö near Jönköping in Sweden, which has its superheater located
in the loop seal, already operates with a steam temperature of 540°C and another boiler with a loop seal
superheater at Avedøre in the suburbs of Copenhagen, Denmark which fires coal with straw containing up
to 1% chloride, already operates with a steam temperature of 580°C [3].
Another approach used widely in Europe to achieve higher superheated steam temperatures in biomass-
fueled boilers without excessive corrosion is the use of combustion additives to convert (corrosive)
potassium chloride into less-corrosive sulfates or silicates. The increased value of higher steam
conditions could offset the cost of such corrosion control additives.
99

Although the costs and benefits of achieving higher superheated steam conditions in specific biomass-
fueled boilers depend on local conditions, the magnitude of the increased power that can be generated by
increasing superheated steam temperatures are so substantial that ongoing studies of technical pathways
to achieving substantial steam temperature increases (such as the 100 Celsius degree increase studied in
the current project) are likely to pay substantial dividends. The most economic pathways to higher steam
temperatures will almost certainly involve combinations of more corrosion-resistant alloys and either
boiler redesign or the removal of the superheater from the flue gas path.
100

3. BENEFITS ASSESSMENT AND COMMERCIALIZATION
The objective of this project was to determine if there are approaches that could be used to make it
technically and economically feasible to operate biomass-fired boilers at temperatures 100 Celsius
degrees higher than the maximum temperature at which they are currently being operated. In Europe, the
need to meet emission requirements and disposal restrictions has forced evaluation and introduction of
alternate boiler designs that operate at higher efficiencies. In North America, regulations are less
demanding, and, consequently, boiler operators have not been forced to aggressively pursue ways to get
more efficient boiler operation.
The results of this project establish that there are alternate superheater designs as well as alternate alloys
that would permit construction of biomass-fired boilers that would operate at higher than current
temperatures. This would result in more efficient boiler operation. Calculations show that, even without
strict emission regulations and disposal restrictions, there is a strong financial incentive for boiler
operators to consider modifications of current biomass boilers and to utilize design modifications and/or
alternate superheater alloys in any new biomass boilers.
For the results of this study to be put into commercial practice, it is essential to get this information to
boiler designers, fabricators and operators as well as tube/alloy producers. The four boiler fabricators,
eight boiler operators and six alloy/tube producers have been involved in the project from the beginning
through the completion of the project. They participated in the selection of sample materials and test
conditions for the laboratory tests, they provided guidance and recommendations for the selection of
sample materials and exposure sites for the field tests, and they provided data for the calculations of
economic benefits. In addition they participated in the project’s annual review meetings and received
copies of the quarterly reports. Consequently, these project partners were very knowledgeable about what
was being done on the project. In addition, wider distribution of the project’s results has been made
through the papers which have been presented at conferences and published in conference proceedings.
The calculations made for two recovery boilers and three wood-fired boilers show the value of the
increased power that could be generated if the steam in a biomass-fired boiler could be heated 50 Celsius
degrees above current operational temperatures would be worth between about $1,260,000 and
$5,890,000 per year. If the steam could be heated 100 Celsius degrees above current operational
temperatures, the increased value of the power generated would be between about $2,420,000 and
$11,210,000 per year. Gains for other biomass-fueled boilers would depend on local plant conditions and
the price of power. These calculations indicate that the increased steam value could justify the use of
corrosion resistant alloys costing orders of magnitude more than current superheater alloys. The financial
gains could, alternatively, be used for use of more corrosion-resistant alloys coupled with the introduction
of combustion additives as well as use of an alternative superheater design such as one that allowed very
rapid superheater replacement.
Adoption of the results of this project will probably not be rapid. For any new boiler, designers would
need to consider the type of contaminants in the fuel as well as the facility’s steam requirements. In
addition, the capacity and temperature limitations of the turbine can be addressed. For retrofits, each
facility’s steam requirements and turbine limitations will have to be considered. There are clear financial
benefits to making changes that would enable operation at 100 Celsius degrees higher temperature, but an
investment would have to be made in the alternate technologies or materials before the benefits could be
realized.
Although the costs and benefits of achieving higher superheated steam conditions in specific biomass-
fueled boilers depend on local conditions, the magnitude of the increased power that can be generated by
increasing superheated steam temperatures are so substantial that ongoing studies of technical pathways
101

to achieving substantial steam temperature increases (such as the 100 Celsius degree increase studied in
the current project) are likely to pay substantial dividends.
102

4. ACCOMPLISHMENTS
The accomplishments associated with this project include nine conference presentations/publications
including one paper that received the conference’s Best Paper Award. In addition, the thesis “Recovery
Boiler Superheater Corrosion – Solubility of Metal Oxides In Molten Salt” was submitted in partial
fulfillment of the requirements for a Master’s Degree.
Publications
- W.B.A. (Sandy) Sharp, “Superheater Corrosion In Biomass Boilers: Today’s Science and Technology”,
ORNL/TM-2011/399, September 30, 2010.
- W.B.A. (Sandy) Sharp, D.L. Singbeil and J.R. Keiser, “Energy from Biomass – Lessons from European
Boilers” Proceedings of 2011 TAPPI PEERS Conference, Portland, OR, published by TAPPI Press,
Atlanta, GA 2011.
- W.B.A. (Sandy) Sharp, Douglas L. Singbeil and James R Keiser, “Superheater Corrosion Produced By
Biomass Fuels”, Paper No. C2012-0001308, published by NACE International, Houston, TX, 2012.
- James R. Keiser, W. B. A. (Sandy) Sharp, Douglas L. Singbeil, Laurel A. Frederick, and Curtis
Clemmons, “Performance of Alternate Superheater Materials in a Potassium-rich Recovery Boiler
Environment”, Proceedings of 2012 TAPPI Peers Conference, Savannah, GA, October 2012, published
TAPPI Press, Atlanta, GA, 2012.
- Douglas L Singbeil and Laurie Frederick, “Improving Heat Recovery in Biomass-Fired Boilers –
Corrosion of Superheater Tube Materials for High Temperature Black Liquor and Bark-fired Boilers”,
Final Report ORNL Subcontract 4000089243, December 2012.
- James R Keiser, W.B.A. (Sandy) Sharp and Douglas L. Singbeil, “Performance Of Alternate
Superheater Tube Materials In Extreme Boiler Environments”, presented at the 8th International Black
Liquor Colloquium: Black Liquor and Biomass to Bioenergy and Biofuels, Belo Horizonte, Brazil, May,
2013.
- Douglas L Singbeil, Laurie A Frederick, James R Keiser, and W.B.A. (Sandy) Sharp, “Could Biomass-
Fueled Boilers Be Operated At Higher Steam Temperatures? 1. Laboratory Evaluation Of Candidate
Superheater Alloys” Proceedings of 2013TAPPI PEERS Conference, Green Bay, WI, September, 2013.
- James R. Keiser, W.B.A. (Sandy) Sharp and Douglas L. Singbeil, “Could Biomass-Fueled boilers be
Operated at Higher Steam Temperatures? 2. Field Tests of Candidate Superheater Alloys,” to be
published by TAPPI Press, Atlanta, GA 2011 in Proceedings of 2013 TAPPI PEERS Conference, Green
Bay, WI, September, 2013.
- W.B.A. (Sandy) Sharp, W. J. (Jim) Frederick, James R Keiser and Douglas L Singbeil, “Could
Biomass-Fueled Boilers Be Operated At Higher Steam Temperatures? 3. Initial Analysis Of Costs And
Benefits” Proceedings of 2013TAPPI PEERS Conference, Green Bay, WI, September, 2013.
Best Paper Award
The paper presented at the 2012 TAPPI conference (James R. Keiser, W.B.A. (Sandy) Sharp, Douglas L.
Singbeil, Laurie A Frederick and Curtis Clemmons, “Performance Of Alternate Superheater Materials In
A Potassium-Rich Recovery Boiler Environment” Proceedings of 2012 TAPPI PEERS Conference,
Savannah, GA, October, 2012) received the Joseph Wolf Founders Best Paper Award. As a result, this
paper is scheduled for publication in the July 2013 issue of TAPPI Journal.
Thesis
A Master’s Degree thesis titled “Recovery Boiler Superheater Corrosion – Solubility of Metal Oxides In
Molten Salt” was submitted by Joseph Meyer in partial fulfillment of the requirements for a Master of
Science Degree in Materials Science and Engineering from the Georgia Institute of Technology.
103

5. CONCLUSIONS AND RECOMMENDATIONS
The objective of this project was to determine what would be the financial benefits and superheater
materials issues from operating biomass-fired boilers with outlet steam temperatures 100 Celsius degrees
higher than currently used.
The laboratory and field corrosion studies showed there are materials that appear capable of operating
under the particularly hostile conditions used in these studies. The two studies did not always agree on
which were the most suitable alloys for specific environments. However, it has to be recognized that the
laboratory tests were conducted at well controlled temperatures in a carefully controlled environment
selected to simulate field conditions as much as possible. In the field tests the environments were realistic
but did not remain constant, and significant temperature variations occurred very frequently.
Consequently, some difference in results between the two test methods should not be surprising.
Nevertheless, it is clear that alloys with sufficient corrosion resistance are available.
Calculations of the financial benefits of higher steam temperatures were made using conditions of five
biomass boilers, and these calculations showed that very substantial gains could be realized in power
recovered and, therefore, in monetary benefits. The magnitude of this increased power that can be
generated by increasing superheated steam temperatures are so substantial that ongoing studies of
technical pathways to achieving substantial steam temperature increases (such as the 100 Celsius degree
increase studied in the current project) are likely to pay substantial dividends. The most economic
pathways to higher steam temperatures will almost certainly involve combinations of more corrosion-
resistant alloys and either boiler redesign or the removal of the superheater from the flue gas path.
A next step that should be considered is the installation of tubes of selected alloys in the superheater area
of one of these “hostile” boilers using the configuration of the current superheater tubes but with cooling
of the experimental tubes controlled so that the tube temperatures remain at about 100 Celsius degrees
above the temperature of the other tubes. A demonstration of this type would provide more evidence to
boiler designers, manufacturers and operators of the corrosion resistance of alternate tube alloys.
104

REFERENCES
1.Craig Reid, Acuren, personal communication to Joey Kish and Doug Singbeil, April, 2007.
2. James R Keiser, Joseph R Kish, Laurie A Frederick, Adam W Willoughby, Limberly A Choudhury,
Douglas L Singbeil, François R Jetté and J Peter Gorog, “Recovery Boiler Superheater Corrosion
Studies”. Proceedings of International Chemical Recovery Conference, Quebec City, Quebec, May 29-
June 1, 2007.
3. W.B.A.(Sandy) Sharp, D.L. Singbeil and J.R. Keiser, “Energy from Biomass - Lessons from European
Boilers”, Proceedings of 2011 TAPPI PEERS Conference, Portland, Oregon, October, 2011, published
TAPPI Press, Atlanta, GA, 2011.
4. W.B.A. (Sandy) Sharp, Douglas L. Singbeil and James R Keiser, “Superheater Corrosion Produced By
Biomass Fuels”, Paper No. C2012-0001308, published by NACE International, Houston, TX, 2012.
5. W.B.A. (Sandy) Sharp, “Superheater Corrosion in Biomass Boilers: Today’s Science and Technology”,
ORNL/TM-2011/399, September 30, 2010.
6. Timo Jantti, Juha Sarkki and Harry Lampenius, “The utilization of CFB technology for large-scale
biomass-firing power plants, presented at Power-Gen Europe 2010, Amsterdam, The Netherlands, June 8
– 10, 2010 and available at http://www.fwc.com/publications/tech_papers/files/TP_CFB_10_03.pdf
7.Marko Natunen, “Co-firing of REF and biofuels in a CFB plant with advanced steam parameters and a
high efficiency in Igelsta plant, Sweden, presented at Power-Gen Europe 2010, Amsterdam, The
Netherlands, June 8 – 10, 2010 and available at
http://www.fwc.com/publications/tech_papers/files/TP_CFB_10_01.pdf.
8.Sonja Enestam, Pekka Lehtonen and Bengt Heikne, “Operating experience of the novel FBHE
superheater at Norrköping energy-from-waste facility”, presented at 9th International Conference on
Circulating Fluidized Beds, in conjunction with 4th International VGB Workshop “Operating experience
with fluidized bed firing systems”, May 13-16, 2008, Hamburg, published TuTech Innovation, Hamburg,
Germany.
9.Ragnar Warnecke, Bernd Benker, Christian Deuerling, Ferdinand Haider, Siegried Horn, Jürgen
Maguhn, Volker Müller, Hermann Nordsieck, Barbara Waldmann and Ralf Zimmermann, “The
mechanisms of corrosion and how to avoid them”, presented at 5th ISWA Beacon conference on Waste-
to-Energy. October 25-26, 2007, Malmö, Sweden and available at http://www.beacon-
wte.org/fileadmin/avfallsverige/Documentation_2007/0940_Ragner_Warnecke.pdf
10.From GKS website: http://www.gks-
sw.de/index.php?option=com_content&task=view&id=26&Itemid=42
11.Anders Hjörnhede, Vattenfall Power Consultant, Racksta, Sweden, Private communication, June 28,
2010.
12.Ragnar Warnecke, “Beläge und Korrosion, Verfahrenstechnik und Konstruction in Chlor-belasteten
thermischen Anlagen”, presented at VDI-Wissensforum seminar, Frankfurt, June 12-13, 2007 and
available at http://www.gks-sw.de/images/stories/vdi_tagung_2007/19-vdi-wf-07-korrosionsmodell%20-
%20warnecke%20-%20manu.pdf
13.Niels Henriksen, Rudolph Blum and Ole Hede Larsen, “Investigations of the possibilities of
influencing the corrosive environment in an external ash cooler”, pages 271 to 294 in TOTem 24
conference “Challenges in the development of high efficiency combustion - the excess enthalpy
combustion project”, Velsen Noord, the Netherlands, 19 March 2003, published International Flame
Research Foundation, Livorno, Italy Available at: ftp://www.ifrf.net/pub/pdf/JOF3-CT95-0024-pdf-
files/JOF3-CT95-0024-06-Henriksen-ElsamP.pdf
14.P.J. Henderson, P. Ljung, P. Kallner and J. Tollin, “Fireside corrosion of superheaters in a wood-fired
circulating fluidized bed boiler”, EUROCORR 2000 conference, September 10-14, 2000, London, U.K.,
published Institute of Materials, Minerals and Mining, London, 2000.
15.“Supercritical steam comes to CFBs”, Materials and Components in Fossil Energy Applications,
published U. S. Department of Energy's Office of Fossil Energy Advanced Research Materials Program,
Winter 2003, No. 161, pages 6-7.
105

16.Reijo Simonen, “Under Control”, published Metso, Tampere, Finland, September 23, 2009 and
available at http://www.metso.com/automation/results_articles_ep.nsf/WebWID/WTB-091119-22570-
6EE29?OpenDocument&mid=294A0747A7A03CA6C22570C8003BF464
17.Anna Nafari and Anders Nylund, “Erosion corrosion of tubes in the loop seal of a biofuel boiler fired
CFB plant”, 7th Liege Conference on Materials for Advanced Power Engineering, Liege, Belgium,
September 30 – October 2, 2002, published as Materials for advanced power engineering 2002 Schriften
des Forschungszentrum, Jülich, Germany, 2002.
18.Anna Nafari and Anders Nylund, “Field study on superheater tubes in the loop seal of a wood-fired
CFB plant”, Materials and Corrosion, 55 (12), 909-920, 2004.
19.S. Rajaram, “Next Generation CFBC”, Chemical Engineering Science, 54, pages 5565-5571, 1999.
20.Dong Energy, “The Enstedværket CHP Plant”, available at
http://www.dongenergy.com/SiteCollectionDocuments/business_activities/generation/Enstedværket_UK[
1].pdf
21.Peter A. Jensen, Flemming J. Frandsen, Jern Hansen, Kim-Dam-Johansen, Niels Henriksenand Stefan
Hörlyck, “SEM investigation of Superheater deposits from biomass-fired boilers”, Energy Fuels, 18 (2),
378-384, 2004.
22.“Boiler 15: an investment in cogeneration for sustainable energy solutions”, published E.ON Värme
Sverige, Sweden and available at http://www.eon.se/upload/eon-se-2-0/dokument/broschyrarkiv/in-
english/H%C3%A4ndel%C3%B6%20cogeneration%20plant.pdf
23.“Value from waste: waste-fired power plant – the new standard for recovery of sustainable energy,
metals and building materials for urban waste,” published Afval Energie Bedrijf, Amsterdam, the
Netherlands, 2006.
24.Frans Lamers, “Corrosion experiences after two years operating the Amsterdam plant”, presented at
ISWA Beacon Conference 2009, Malmö, Sweden, November 24, 2009, published International Solid
Waste Association, Vienna, Austria, 2009. Available at http://www.beacon-
wte.org/fileadmin/avfallsverige/Documentation_2009/F_Lamers.pdf
25.E. Skog, L-G. Johansson, J-E. Svensson, J. Petterson, C. Petterson, N. Folkeson, “Why does bio-mass
and waste cause severe corrosion of superheater tubes?”, 33rd International Technical Conference on
Clean Coal & Fuel Systems, Clearwater, FL, June 2008, published Coal Technologies Associates, North
Potomac, MD, 2008.
26.K. Segerdahl, J. Pettersson, J-E. Svensson and L-G. Johansson, “Is KCl(g) corrosive at temperatures
above its dew point? Influence of KCl(g) on initial stages of high temperature corrosion of 11% Cr Steel
at 600°C,” Materials Science Forum, 461-464, 109-116, 2004.
27.C. Pettersson, J-E, Svensson and L-G Johansson, “Corrosivity of KCl(g) at temperatures above its dew
point – Initial stages of the high temperature corrosion of Alloy Sanicro 28 at 600°C”, Materials Science
Forum, 522-523, pp 539-546, 2006.
28.Marko Palonen, Pekka Lehtonen and Tero Luomaharju, “Increase of steam data with challenging
fuels”, October 8, 2009. Available as www.processeng.biz/iea-fbc.org/upload/59_3_Palonen.pdf.
29.Ana Žbogar, Peter A. Jensen, Flemming J. Frandsen, Jern Hansen and Peter Glarborg, “Experimental
investigation of ash deposit shedding in a straw-fired boiler”, Energy Fuels, 20 (2), 512-519, 2006.
30.M. Montgomery, Søren A. Jensen, Annette Hansson, Ole Biede and Tommy Vilhelmsen, “High
temperature corrosion testing at Maribo Sakskøbing and Avedøre straw firing power plants”, Manuscript
associated with poster SS 2-P-7984 at EUROCORR European Corrosion Congress, Nice, France, 6-10
September, 2009.
31.Paul Kilgallon, Nigel Simms and John Oakey, “Modeling corrosion in biomass-fired power plants”,
Paper 05318 at NACE International CORROSION/2005 conference, April 3-7, Houston, TX, published
NACE, Houston, TX, 2005.
32.D.C. Dayton, B.M. Jenkins, S.Q. Turn, R.R. Baker, R.B. Williams and D. Belle-Oudry and L.M. Hill,
“Release of inorganic constituents from leached biomass during thermal conversion”, Energy Fuels, 13
(4), 860-870, 1999.
33.P.A. Jensen, B. Sander and K. Dam-Johansen, “Pretreatment of straw for power production by
106

pyrolysis and char wash”, Biomass and Bioenergy, 20 (6), 431-446, 2001.
34.P.A. Jensen, B. Sander and K. Dam-Johansen, “Removal of K and Cl by leaching of straw char”,
Biomass Bioenergy, 20 (6), 447-457, 2001.
35.Linda S. Johansson, Bo Leckner, Claes Tullin, Lars-Erik Åmand and Kent Davidsson, “Properties of
particles in the fly ash of a biofuel-fired circulating fluidized bed (CFB) boiler”, Energy Fuels, 22 (5),
3005-3015, 2008.
36.C. Andersson, “A method for operating a heat-producing plant for burning chlorine-containing fuels”,
Patent WO 02059526, August 1, 2002.
37.“Chlorout”, published Vattenfall Business Services Nordic AB, August, 2005. Available as
www.vattenfall.com/en/file/chlorout_8459980.pdf.
38.Kent O. Davidsson, Klass Engvall, Magnus Hagström, John G. Korsgren, Benny Lönn and Jan B.C.
Pettersson, “A surface ionization instrument for on-line measurements of alkali metal components in
combustion: instrument description and applications”, Energy Fuels, 16 (6), 1369-1377, 2002.
39.P. Henderson, P. Szákalos, R. Pettersson, C. Andersson, J. Hogberg, “Reducing superheater corrosion
in wood-fired boilers”, Werkstoffe, und Korrosion – Weinheim, 57 (2), 128-134, 2006.
40.Markus Broström, Håkan Kasseman, Anna Helgesson, Magnus Berg, Christer Andersson, Rainer
Backman and Anders Nordin, “Sulfation of corrosive alkali chlorides by ammonium sulfate in a biomass
fired CFB boiler”, Fuel Processing Technology, 88 (11-12), 1171-1177, 2007
41.Martti Aho, Pasi Vainikka, Raili Taipale and Patrik Yrjas, “Effective new chemicals to prevent
corrosion due to chlorine in power plant superheaters”, Fuel 87, 647-654, 2008.
42.M. Aho, “Method for preventing chlorine deposition on the heat transferring surface of a boiler”,
Finnish Patent FI117631B, December 29, 2006.
43.Michaël Becidan, Lars Serum, Flemming Frandsen and Anne Juul Pedersen, “Corrosion in waste-fired
boilers: a thermodynamic study”, Fuel, 88 (4), 595-604, 2009.
44.Beatrice Coda, Martti Aho, Roland Berger and Klaus R.G. Hein, “Behavior of chlorine and enrichment
of risky elements in bubbling fluidized bed combustion of biomass and waste assisted by additives”,
Energy Fuels, 15 (3), 680-690, 2001.
45.K.O. Davidsson, B-M. Steenari and D. Eskilsson, “Kaolin addition during biomass combustion in a
35MW circulating fluidized bed boiler”, Energy Fuels, 21 (4), 1959-1966, 2007.
46. Greg F. Weber and Christopher J. Zygarlicke, “Barrier issues to the utilization of biomass”,
Semiannual Technical Progress Report on US DOE Contract DE-FC26-00NT41014.
47.“Renewable energy consumption and electricity: preliminary statistics 2010”, U.S. Energy Information
Administration, Office of Coal, Nuclear, Electric and Alternative Fuels, U.S. Department of Energy,
Washington D.C., published June, 2011.
48. F.H. Stott, “Influences of alloy additions on oxidation”, Materials Science and Technology, August
1989, 5, pages 734-740.
49. W.B.A.(Sandy) Sharp, “Corrosion and Cracking in Chemical Recovery Equipment”, 2011 Kraft
Recovery Course, Published TAPPI Press, Atlanta, Georgia, 2011.
50. D.C. Crowe, W.C. Youngblood, “Recovery Boiler Superheater Corrosion,” Preprints of 9th
International Symposium on Corrosion in the Pulp and Paper Industry, CPPA, Montreal, PQ, pages 225-
230, 1998.
51. T.N.Adams, W.J. Frederick, T.M. Grace, M. Hupa, K. Iisa, A.K. Jones and H.N. Tran, editors, “Kraft
Recovery Boilers”, TAPPI Press, Atlanta, GA, 1997.
52. D. W. Reeve, D. C. Pryke and H. N. Tran, “Corrosion in the closed cycle mill”, Pages 85-90 in
Proceedings of the Fourth International Symposium on Corrosion in the Pulp and Paper Industry,
published by Swedish Corrosion Institute, Stockholm, Sweden, as “Pulp and Paper Industry Corrosion
Problems, Volume 4, 1983.
53. Matthew J. Estes, Institute of Paper Chemistry, Atlanta, GA, Private communication, 1989.
54. F. Bruno, “Thermochemical Aspects on Chloride Corrosion in Kraft Recovery Boilers”, Paper No.
01426 at NACE International CORROSION/2001 conference, Houston, TX, published NACE, Houston,
2001.
107

55. M.Mäkipää, E, Kauppinen, T. Lind, J. Pyykönen, J. Jokiniemi, P. McKeough, M. Oksa, Th. Malkow,
R.J. Fordham, D. Baxter, L. Koivisto, K. Saviharju, E. Vakkilainen, “Superheater tube corrosion in
recovery boilers,” 10th International Symposium on Corrosion in the Pulp and Paper Industry, Volume 1,
published VTT, Espoo, Finland: 157-180, 2001.
56. J. Tuiremo, K. Salmenoja, “Control of superheater corrosion in black liquor recovery boilers” 10th
International Symposium on Corrosion in the Pulp and Paper Industry, Volume 1, published VTT, Espoo,
Finland: 181-200, 2001.
57. Joseph R. Kish, “Superheater corrosion and alloy performance in current generation high pressure
recovery boilers”, pages 53 to 59 in Final Technical Report: Materials for Industrial Heat Recovery
Systems, project period 04/01/2004 to 03/30/2007, by James R. Keiser, Joseph. R. Kish, Gorti R. Sarma,
Jerry Yuan, J. Peter Gorog, Laurie A. Frederick, Francois R. Jetté, Roberta A. Meisner and Douglas L.
Singbeil, December 31, 2007.
58. Esa K. Vakkilainen and Pekka Pohjanne, “Selecting the right material for recovery boiler
superheaters”, Baltica VIII Conference on Life Management and Maintenance for Power Plants, Vol. 2,
pages 37-51, published VTT, Espoo, Finland, 2010.
59. J. Pettersson, J-E. Svensson and L-G. Johansson, “Alkali-induced corrosion of 304-type austenitic
stainless steel at 600°C; comparison between KCl, K CO and K SO ”, Materials Science Forum, 595-
2 3 2 4
598, 367-375, 2008.
60. H. Tran, Y. Arakawa, “Recovery Boiler Technology in Japan,” Paper 12-6 at TAPPI 2001
Engineering/Finishing and Converting Conference, Published TAPPI Press, Atlanta, GA, pages 49-62,
2001.
61. John L. Clement and Thomas M. Grace, “Investigation of superheater design and performance - Part
1, TAPPI Engineering, Pulping and Environmental Conference, October 11-14, 2009, Memphis, TN, 27
pages, published TAPPI Press, Atlanta, GA, 2009.
62. B-J. Skrifvars, R. Backman, M. Hupa, K. Salmenoja and E. Vakkilianen, “Corrosion of superheater
steel materials under alkali salt deposits Part 1: The effect of salt deposit composition and temperature”,
Corrosion Science 50, 1274-1282, 2008.
63. Rainer Backman, Mikko Hupa, Juha Lagerbom and Toivo Lepisto, “Influence of partially molten
alkali deposits on superheater corrosion in black liquor recovery boilers”, 10th International Symposium
on Corrosion in the Pulp and Paper Industry, Volume 1, pages 137-155, published VTT Technical
Research Center of Finland, Espoo, Finland, 2001.
64. B-J. Skrifvars, M. Westén-Karlsson, M. Hupa and K. Salmenoja, “Corrosion of super-heater materials
under alkali salt deposits. Part 2: SEM analyses of different steel materials”, Corrosion Science 52, 1011-
1019, 2010.
65. David A. Tillman, Dao Duong, Sheila Figueroa and Bruce Miller, “Chlorine in solid fuels fired in
pulverized coal boilers – sources, forms, reactions and consequences: a literature review”, Fuel
Conference, Banff, Canada, September 28 – October 3, 2008. Energy Fuels, 23 (7), 3379-3391, 2009.
66. Dao N.B. Duong and David A. Tillman, “Chlorine issues with biomass co-firing in pulverized coal
boilers: sources, reactions and consequences – a literature review”, 34th International Technical
Conference on Coal Utilization and Fuel Systems, Clearwater FL, May 31 – June 4, 2009.
67. K. Salmenoja and K. Mäkela, “Prevention of superheater corrosion in the combustion of biofuels”,
Paper 00238 at NACE International CORROSION/2000 conference, published NACE, Houston, 2000.
68. Matti Hiltunen, Vesna Barišić and Edgardo Coda Zabetta, “Combustion of different types of biomass
in CFB boilers”, 16th European Biomass Conference, Valencia, Spain, June 2-6, 2008.
69. Len Pinder, “Materials challenges in biomass combustion”, MATUK Energy Materials Working
Group Conference, Loughborough UK, 09-10/10/2008.
70. Lars-Gunnar Johansson, Jan-Erik Svensson, Erik Skog, Jasper Pettersson, Carolina Pettersson,
Nicklas Folkeson, Henrik Asteman, Torbjörn Jonsson and Mats Halvarsson, “Critical corrosion
phenomena on superheaters in biomass and waste-fired boilers”, Proceedings of the Sino-Swedish
Structural Materials Symposium, 2007, pages 35-39.
108

71. Y.Y.Lee and M.J. McNallan, “Ignition of nickel in environments containing oxygen and chlorine”,
Metallurgical Trans. A, 18 (6), 1099-1107, 1987.
72. Armin Zahs, Michael Spiegel and Hans J. Grabke, “Chloridation and oxidation of iron, chromium,
nickel and their alloys in chloridizing and oxidizing atmospheres at 400-700°C”, Corrosion Science 42,
1093-1122, 2000.
73. J. Pettersson, J-E. Svensson and L-G Johansson, “KCl-induced corrosion of a 304-type austenitic
stainless steel in O and in O + H O environment: The influence of temperature”, Oxidation of Metals,
2 2 2
72 (3-4), 159-177, 2009.
74. J Pettersson, H. Asteman, J-E. Svensson and L-G. Johansson, “KCl-induced corrosion of a 304-type
austenitic stainless steel at 600°C; the role of potassium”, Oxidation of Metals 64 (1-2), 23-41, 2005.
75. C. Pettersson, J. Pettersson, H. Asteman, J-E. Svensson and L-G. Johansson, “KCl-induced high
temperature corrosion of the austenitic Fe-Cr-Ni alloys 304L and Sanicro 28 at 600°C”, Corrosion
Science, 48 (6), 1368-1378, 2006.
76. J. Pettersson, C. Pettersson, N. Folkeson, L-G. Johansson, E. Skog and J-E. Svensson, “The influence
of sulphur additions on the corrosive environment in a waste-fired CFB boiler”, Materials Science Forum,
522-523, 563-570, 2006.
77. N. Folkeson, L-G. Johansson and J-E. Svensson, “Initial stages of the HCl-induced high-temperature
corrosion of Alloy 310”, J. Electrochem. Soc., 154 (9), C515-C521, 2007.
78. L. Paul, G. Clark and M. Eckhardt, “Laboratory and Field Corrosion Performance of a High
Chromium Alloy for Protection of Waterwall Tubes from Corrosion in Low NOx Coal Fired Boilers,”
Paper No. 06473 at NACE International CORROSION/2006 conference, published NACE, Houston, TX,
2006.
79. K.E. Coleman, N.J.Simms, P.J. Kilgallon and J.E. Oakley, “Corrosion in biomass combustion
systems”, Materials Science Forum, 595-598, 377-386, 2008.
80. Paul J. James, E.ON Engineering Group, Ratcliffe-on-Soar, UK, Private Communication, August 18,
2010.
81. M. Mäkipää, David J. Baxter, S. Sroda and M. Oksa, “Laboratory testing for evaluation of steels and
alloys used in superheater area of boilers for biomass fuels”, Materials Science Forum, Volumes 461-464,
(High temperature corrosion and protection of materials), pages 989-998, 2004.
82. Rachel Pettersson, Jasper Flyg and Peter Viklund, “High temperature corrosion under simulated
biomass deposit conditions”, Paper 09168 at NACE International CORROSION/2009 conference, March
22-26, 2009, Atlanta, GA, published NACE, Houston, 2009.
83. K. Salmenoja, K. Mäkelä, M. Hupa and R. Backman, “Superheater corrosion in environments
containing potassium and chlorine”, Journal of the Institute of Energy, 69 (480). 155-162, 1996.
84. Shang-Hsiu Lee, Nickolas J. Themelis and Marco J. Castaldi, “High temperature corrosion in waste-
to-energy boilers”, Journal of Thermal Spray Technology, 16 (1), 1-7, 2007.
85. A. Wilson, U. Forsberg and J. Noble, “Experience of composite tubes in municipal waste
incinerators”, Paper 97153 at NACE Corrosion/97 conference, published NACE International, Houston,
TX, 1997.
86. M. Uusitalo, M. Kaipiainen, P. Vuoristo and T. Mäntylä, “High temperature erosion-corrosion of
superheater materials and coatings in chlorine-containing environments”, Materials Science Forum, 369-
372, 475-482, 2001.
87. Satu Tuurna, Tommi Varis, Kimmo Ruusuvuori, Stefan Holmström, Jorma Salonen, Pertti Auerkari,
Tuomo Kinnunen, Partik Yrjas, Risto Finne, Matti Nupponen, Ulla McNiven, Hannu Ahonen and Ari
Kapulainen, “Managing corrosion in biomass boilers: benefits and limitations of coatings”, Baltica VIII
Conference on Life Management and Maintenance for Power Plants, Vol. 2, pages 22-36, published VTT,
Espoo, Finland, 2010.
88. M. Spiegel, “Salt melt induced corrosion of metallic materials in waste incineration plants”, Materials
and Corrosion, 50, 373-393, 1999.
109

89. E. Otero, A. Pardo, M.C. Merino, M.V. Utrilla, M.D. Lopez and J.L. dePeso, “Corrosion behavior of
IN-600 superalloy in waste-incineration environments: hot corrosion by molten chlorides”, Oxidation of
metals, 31 (516), 507-525, 1999.
90. E. Otero, A. Pardo, F.J. Pérez, M.V. Utrilla and T. Levi, “Corrosion behavior of 12CrMoV steel in
waste incineration environments: hot corrosion by molten chlorides”, Oxidation of Metals 49 (516), 467-
484, 1998.
91. Y.S. Li, Y. Niu and W.T. Wu, “Accelerated corrosion of pure Fe, Ni, Cr and several Fe-based alloys
induced by ZnCl -KCl at 450°C in oxidizing environment”, Materials Science and Engineering A345, 64-
2
71, 2003.
92. T.J. Pan, C.L. Zeng and Y. Niu, “Corrosion of three commercial steels under ZnCl -KCl deposits in a
2
reducing atmosphere containing HCl and H S at 400-500°C”, Oxidation of Metals, 67 (1/2), 107-127,
2
2007.
93. W.M. Lu, T.J. Pan, K. Zhang and Y. Niu, “Accelerated corrosion of five commercial steels under a
ZnCl -KCl deposit in a reducing environment typical of waste gasification at 673-773°K”, Corrosion
2
Science 50, 1900-1906, 2008.
94. Dorota Bankiewicz, Patrik Yrjas and Mikko Hupa, “High temperature corrosion of superheater tube
materials exposed to zinc salts”, Energy Fuels, 23 (7), 3469-3474, 2009.
95. Andreas Ruh and Michael Spiegel, “Thermodynamic and kinetic consideration on the corrosion of Fe,
Ni and Cr beneath a molten KCl-ZnCl mixture”, Corrosion Science 48, 679-695, 2006.
2
96. Y.S. Li and M. Spiegel, “Models describing the degradation of FeAl and NiAl alloys induced by
ZnCl -KCl melt at 400-450°C”, Corrosion Science 46, 2009-2023, 2004.
2
97. Edgardo Coda Zabetta, Vesna Barišić and Brad Moulton, “Foster Wheeler references and tools for
Biomass- and waste-fired CFBs”, 34th International Technical Conference on Coal Utilization and Fuel
Systems, Clearwater FL, May 31 – June 4, 2009, published Coal Technology Association, Gaithersburg,
MD, 2009.
98. Vesna Barišić, Edgardo Coda Zabetta and Juha Sarkki, “Prediction of agglomeration, fouling and
corrosion tendency of fuels in CFB co-combustion”, 20th International conference on Fluidized Bed
Combustion, Xi’an, China, May 18-20, 2009.
99. S. Enestam, J. Niemi and K. Mäkelä, “STEAMAX – a novel approach for corrosion prediction,
materials selection and optimization of steam parameters for boilers firing fuel and fuel mixtures derives
from biomass and waste”, 33rd International Technical Conference on Clean Coal and Fuel Systems”,
Clearwater, FL, June 6-10, 2008, published Coal Technology Association, Gaithersburg, MD, 2010.
100. Aaron Fuller, Jörg Maier and G. Scheffknecht, “Impact of co-combustion on emission behavior and
ash quality by co-firing high shares of biomass and residues”, 35th International Technical Conference on
Clean Coal and Fuel Systems”, June 6-10, 2010, Clearwater, FL, published Coal Technology Association,
Gaithersburg, MD, 2010.
101. P.J. Henderson, T. Eriksson, J. Tollin and T. Abyhammar, “Corrosion testing of superheater steels
for 600°C steam in biomass/co-fired boilers”, Proceedings of conference on advanced heat resistant steels
for power generation, San Sebastian, Spain, April 27, 1998, published Maney Publishing, Leeds, UK,
1999.
102. Flemming J. Frandsen, “Utilizing biomass and waste for power production – a decade of
contributing to the understanding, interpretation and analysis of deposits and corrosion processes”, Fuel
84, 1277-1294, 2005.
103. Fleming J. Frandsen, “Ash research from Palm Coast, Florida to Banff, Canada: Entry of biomass in
modern power boilers”, Energy Fuels 23 (7), 3347-3378, 2009.
104. Karin H. Andersen, Flemming J. Frandsen, Peter F.B. Hansen, Kate Wieck-Hansen, Ingvar
Rasmussen, Peter Overgaard and Kim Dam-Johansen, “Deposit formation in a 150MWe utility PF boiler
during co-combustion of coal and straw”, Energy Fuels 14 (4), 765-780, 2000.
105. Hanne-P. Nielsen, Flemming J. Frandsen and Kim Dam-Johansen, “Lab-scale investigation of high
temperature corrosion phenomena in straw-fired boilers”, Energy Fuels, 13 (6), 1114-1121, 1999.
110

106. Xiaoyang Liu, Joerg Maier and Klaus R.G. Hein, “The kinetics of fireside corrosion in biomass
combustion system and the influence from gas and deposit ash chemistry”, Electrochemical Society 201st
Meeting - Philadelphia, PA, May 16, 2002.
107. Xiaoyang Liu, Joerg Maier, Klaus R.G. Hein, “The kinetics and influence factors on chlorine-
induced fireside corrosion in biomass combustion system. Part 3: Corrosion morphology of chlorine
corrosion”, 15th International Corrosion Congress, Granada, Spain, September 22-27, 2002. Proceedings
edited by Manuel Morcillo, published 2002.
108. Douglas L Singbeil and Laurie Frederick, “Improving Heat Recovery in Biomass-Fired Boilers –
Corrosion of Superheater Tube Materials for High Temperature Black Liquor and Bark-fired Boilers”,
Final Report ORNL Subcontract 4000089243, December 2012.
109. Douglas L Singbeil, Laurie A Frederick, James R Keiser, and W.B.A. (Sandy) Sharp, “Could
Biomass-Fueled Boilers Be Operated At Higher Steam Temperatures? 1. Laboratory Evaluation Of
Candidate Superheater Alloys” Proceedings of 2013TAPPI PEERS Conference, Green Bay, WI,
September, 2013.
110. James R. Keiser, W.B.A. (Sandy) Sharp and Douglas L. Singbeil, “Could Biomass-Fueled boilers be
Operated at Higher Steam Temperatures? 2. Field Tests of Candidate Superheater Alloys,” Proceedings of
2013 TAPPI PEERS Conference, Green Bay, WI, September, 2013.
111. James R. Keiser, W.B.A. (Sandy) Sharp, Douglas L. Singbeil, Laurie A Frederick and Curtis
Clemmons, “Performance Of Alternate Superheater Materials In A Potassium-Rich Recovery Boiler
Environment” Proceedings of 2012 TAPPI PEERS Conference, Savannah, GA, October, 2012.
112. Rapp, R., Zhang Y.S. “Hot Corrosion of Materials: Fundamental Studies” JOM p. 47-55,
1994.
113. D. Inman, D.M. Wrench, “Corrosion in Fused Salts” Brit Corros. J., Vol 1, p. 246,1966.
114. R. Rapp.”Hot corrosion of materials: a fluxing mechanism?” Corrosion, Vol 22 Iss. 2 p. 209-221,
2002
115. Rapp, R. Goto, K. Braunstein, J. Selman, J. “Hot Corrosion of Metals by Molten Salts, Molten Salts
1, Electrochem. Soc. p. 159 1981.
116. Hwang, Y. Rapp, R. “Synergistic Dissolution of Oxides in Molten Sodium Sulphate” J.
Electrochem. Soc., vol 137 p. 1276 (1990).
117. Private communication, Laurie A Frederick, FPInnovations
118. D. Bankiewicz, S. Enestam, P. Yrjas and M. Hupa, “Experimental Studies of Zn and Pb Induced
High Temperature Corrosion of Two Commercial Boiler Steels”, Fuel Processing Technology, 2012.
119. W.B.A. (Sandy) Sharp, W. J. (Jim) Frederick, James R Keiser and Douglas L Singbeil, “Could
Biomass-Fueled Boilers Be Operated At Higher Steam Temperatures? 3. Initial Analysis Of Costs And
Benefits” Proceedings of 2013TAPPI PEERS Conference, Green Bay, WI, September, 2013.
120. K.E. Heselton, “Efficiency”, pages 100-105 in Boiler Operator’s Handbook, published Fairmont
Press, Lilburn, GA, 2005. Also available at
http://books.google.com/books?id=8y0qRQl7XDEC&pg=PA101&lpg=PA101&dq=heat+loss+method+b
oiler+efficiency&source=bl&ots=Rdm1iVHNe1&sig=QQX9-
ouWVLetjl9fQ8KQjuzaOj4&hl=en&sa=X&ei=s_PVUPKeFMjxigL6lYD4DQ&sqi=2&ved=0CFIQ6AE
wAg#v=onepage&q=heat%20loss%20method%20boiler%20efficiency&f=false
121. T.N. Adams, page 26, tables 1 to 8 in “Kraft Recovery Boilers”, published TAPPI Press, Atlanta,
GA, 1997.
122. J.W. Gibbs, "A Method of Geometrical Representation of the Thermodynamic Properties of
Substances by Means of Surfaces", Transactions of the Connecticut Academy II, pages 382-404,
December, 1873.
123. Ulrich, G.D. A Guide to Chemical Engineering Process Design and Economics. John Wiley & Sons,
New York, 1984, pp. 87 and 90-91.
124. John D. Andrews, MWV, Charleston, WV.
125. A. Stålenheim and P. Henderson, “ Materials for higher steam temperatures
111

(up to 600°C) in biomass and waste fired plant - a review of present knowledge”, Report M08-833
published by Varmeforsk Service AB, Stockholm, Sweden, 2011.
126. B. Kamuk, “Technical, economical, operating consequences by operating at extreme steam
parameters”, Waste-to-Energy Research and Technology Council, 2010 Annual Meeting, Brno, Czech
Republic. Also available at http://www.admas.vutbr.cz/files/wtert-prezentace/Kamuk_-
_Technical_economical_operating_consequences_by_operating_at_extreme_steam_parameters.pdf
112
