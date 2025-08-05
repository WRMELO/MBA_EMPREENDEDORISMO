# 2_Functional_and_Operational_Control_of

**Fonte**: 2_Functional_and_Operational_Control_of.pdf  
**Data de conversão**: 2025-07-30 15:05:37  
**Origem**: base_relevantes

---

I.
2 Functional and Operational Control of Thermal Power Plants
2.1.1 Operation control
Since safe and economical operation is carried out at thermal power stations while carefully
checking environmental problems, there are many points that operators must judge to take
appropriate measures. Therefore, a large load is applied to operators in case of an emergency.
Therefore, it is necessary to automate emergency manual operations to be taken against faults, as
well as to automate normal manual operations in order to minimize operators’ judgments. To keep
the final protection of the plant, it is absolutely required to take appropriate measures for the plant
facilities.
A unit protection device is installed to protect each unit if a fault occurs in any unit and it
becomes difficult to continue safe operation of the unit. This unit protection device is called the
“unit trip interlock.” Basically, the unit trip interlock is classified into the boiler protection
interlock (MFT), turbine protection interlock (MTS), and generator protection interlock (86G).
These interlock systems may vary depending on the manufacturer’s design. In principle,
however, the once-through unit boiler, turbine, and generator are mutually interlocked. Figure 35
shows an example of the trip interlock system.
2.1.1.1 Boiler protection interlock (MFT)
This boiler protection interlock is intended to shut down the fuel supply to stop the boiler if it
becomes difficult to continue stable combustion of the boiler. The conditions for tripping of this
interlock may vary slightly depending on the type of boiler, that is, whether it is drum boiler or a
once-through unit boiler. Generally, these conditions are fuel pressure drop, high furnace pressure,
stopping of two ventilating fans, protection of the reheating unit, supply water flow rate drop, and
drum level drop. In addition to these conditions, unit emergency stop and turbine/generator trip
conditions are interlocked. According to the boiler model, further conditions are interlocked.
2.1.1.2 Turbine protection interlock (MTS)
If it becomes difficult to continue stable operation of the turbine, the solenoid is operated to stop
the turbine. The conditions for tripping of this interlock are turbine overspeed, thrust error,
bearing hydraulic pressure drop, and degree of vacuum drop, etc. In addition to these conditions,
the unit emergency stop, turbine manual stop, and generator trip conditions are interlocked.
Basic interlock circuit
Problem on Generator trip
generator side
Problem on Turbine trip
turbine side
Fire extinguishing
of boiler
epyt
A
Description A-type interlock circuit
If a problem occurs on the
turbine side and the turbine is Problem on generator Generator trip
tripped (each turbine valve is side Any of the thrust, hydraulic opened), the generator and boiler pressure, or exhaust speed is faulty.
are stopped conditionally. This Problem s i o d n e turbine Turbine trip Conditions for protection of
system is that the T-G and T-B are the reheater
n n o o t t s t a r t i i p s p fi e e d d . i f the conditions are Problem on boiler side Fire ext b in o g il u e i r s hing of
This system is mainly used for
units designed by Ebasco.
Description B-type interlock circuit
If a problem occurs on the
turbine side and the turbine is Problem on generator Generator trip
tripped (each turbine valve is side
opened), the generator and boiler
are stopped immediately. Problem on turbine Turbine trip side
In this group, a circuit to
i b m oi m le e r d i i f a t a e l p y r o ex b t l i e n m g u o is c h c u f r ir s e o i n n t t h h e e Problem on boiler side Fire ext b in o g il u e i r s hing of
generator side is added.
Description C-type interlock circuit
If a problem occurs in any of the
boiler, turbine, or generator, Problem on generator Generator trip
mutual interlock is activated to side
trip the unit completely.
This interlock where the turbine Problem on turbine Turbine trip
side
is tripped immediately if a
p ch ro a b ra le c m ter i o s c ti c c u rs i f n e a t t h u e r e b , oile w r h i i s c h a Problem on boiler side Fire ext b in o g il u e i r s hing of
cannot be seen in the A type or B
type.
epyt
B
epyt
C
Problem on
boiler side
Fig. 35 Examples of trip interlock systems
12

2.1.1.3 Generator protection interlock (86G)
A status where stable operation of the generator or transformer is difficult is detected by the
protective device or protective relay. After this, the generator is disconnected from the system and
the turbine is tripped to stop the generator at the same time. The conditions for detection of the
protection are ratio differentiation of the generator, loss of excitation, ratio differentiation of the
ground fault or transformer, impulse hydraulic pressure, overexcitation, etc. In addition to these
conditions, the high/low frequency of the system and the protection of the bus-bar are interlocked.
2.1.1.4 Protection device tests during operation
The important point during plant operation is that the plant can be stopped safely in case of an
emergency. To maintain this safety, it is necessary to periodically check the operation status of
various safety prevention apparatus installed for protection of the plant. Table 3 shows examples
of the protection device tests.
Table 3 Examples of protection device tests
Inspection test item Frequency Contents of test
Main turbine Valve tests
(1) Main steam stop valve Twice/week The valves are manually opened or closed one by one from the central control
room to check the valve operation and open/closed indication lamp operation.
(2) Intercept valve, reheated Twice/week The valves of each system are manually opened or closed from the central
steam stop valve, combined control room to check the valve operation and open/closed indication lamp
reheat valve operation.
Protection device tests
(1) Lock-out Once/week After the operation of the emergency shutdown device has been removed, the
(Oil trip) test handle is operated to check the operation of the oil trip mechanism.
(2) Thrust failure protection trip Once/week After the operation of the thrust failure protection device has been removed,
the test handle is operated to check the operation of the thrust bearing wear
trip mechanism.
Extraction check valve test Twice/week Valves are manually opened or closed with the test handle or switch to check
the valve operation and open/closed indication lamp operation.
Oil pump automatic starting test Once/week The hydraulic pressure is decreased using the testing equipment in the
simulated mode to check the automatic startup at the set hydraulic pressure
levels of the auxiliary oil pump, emergency oil pump, and turning oil pump.
Main oil tank oil level alarm test Once/week The indication rod of the oil gauge is moved up or down to check the alarm
operation.
Turbine Valve test Once/week The high-pressure and low-pressure steam stop valves are opened or closed
driven feed manually to check the operation of the valve and open/close unit.
pump Protection device tests
(1) Overspeed trip Once/month After the trip circuit has been removed, the RPM is increased in the simulated
mode to check the overspeed trip set hydraulic pressure level.
(2) Bearing hydraulic pressure Once/month After the trip circuit has been removed, the bearing oil pressure is decreased
drop trip in the simulated mode to check the trip set hydraulic pressure level.
(3) Thrust failure protection trip Once/month After the trip circuit has been removed, the thrust position is moved in the
simulated mode to check the trip set hydraulic pressure level.
Oil pump auto starting test Once/month The hydraulic pressure is decreased using the testing equipment in the
simulated mode to check the automatic startup at the set hydraulic pressure
levels of the extra main oil pump and emergency oil pump.
Spare feed water pump (motor Once/month The pump is manually started at the work site, and a load is applied to check
drive) starting test the operation of the auxiliary oil pump and minimum flow recirculating valve.
Seal oil Emergency pump automatic Once/week The discharge pressure and differential pressure of the seal oil are decreased
equipment starting test using the testing equipment in the simulated mode to check the alarm
(Seal oil discharge pressure, low operation and auto startup at the set hydraulic pressure level.
differential pressure alarm test)
Vacuum drop alarm test of Once/month The vacuum level is decreased using the testing equipment in the simulated
vacuum tank mode to check the alarm operation.
13

I.
2.1.2 Boiler operation control during normal operation
It must be strongly attempted to find the error status early and to prevent problems during
normal unit operation in order to maintain stable operation status.
The actions to be actually taken are basically classified into the inspection at the work field, and the sampling and
evaluation of the operation records. It is important to take these actions daily in order to check status change in
the early phase, and this leads to appropriate actions and measures being taken in a timely manner.
2.1.2.1 Inspection at the work field
As a rule, the inspection interval must be every work shift. Walkaround inspection of the boiler
main unit parts and boiler auxiliary devices is carried out. The inspection results must be kept.
If any problem symptom is observed, it is necessary to grasp any status change as time elapses.
Generally, walkaround inspection is carried out according to the checklist. In addition to this
inspection, further inspection points, such as unusual noise, unusual odor, or discoloration must
also be inspected.
The combustion status inside the furnace must also be checked during walkaround inspection.
However, if the type of coal to be used is changed, the inspection must be carried out with special
attention.
One of the points to inspect the status of clinker and ash sticking to each heat transfer surface
inside the furnace is to check whether or not excessive development or accumulation exists. The
other point is that the contamination status of each heat transfer surface is checked with the
secular change in the operation data stated on the next page to appropriately operate the soot
blower or wall deslagger. When the type of coal to be used is changed, these points become
particularly important.
2.1.2.2 Sampling and evaluation of operation records
To grasp the secular change in the boiler static characteristics and to evaluate performance,
records of the boiler operated at its rated output are sampled periodically.
In daily operation, it is basically checked whether or not the balance among the feed water flow
rate, fuel flow rate, and air flow rate is correct.
As deviation of the boiler input command to the output command and deviation of the water/fuel
ratio and air/fuel ratio are checked, it is possible to judge whether or not the balance is correct.
Additionally, it must be strongly attempted to check changes in the make-up water quantity in
order to find any boiler tube leak in the early phase.
In the coal-fired boiler, the characteristics of the boiler may change greatly according to the coal
properties. The heat absorption distribution of the furnace, SH, and RH is changed according to
the combustibility of the coal or slagging/fouling ability. According to the contamination degree of
the heat transfer surface, the exhaust gas temperature increases and it adversely affects the boiler
efficiency. Therefore, the heat absorption status of each heat transfer surface is grasped by
checking the following points.
(cid:120) Changes in control parameters using the RH temperature control or SH temperature control
(cid:120) Changes in the gas temperature of each part of the rear gas duct including the gas temperature at the
outlet of the ECO.
The soot blower and wall deslagger can be operated at efficient intervals.
Since changes in coal properties may affect the characteristics of the exhaust gas (NOx, unburned matter in ash,
etc.), it is necessary to grasp the characteristics if the type of coal to be used is changed.
If an imbalance occurs in the metal temperature distribution of each part of the furnace, SH, and RH or in the
steam temperature distribution of each part of the SH and RH, it is thought that changes in combustion status may
be the cause. Therefore, it is necessary to check the damper opening of the wind box at the work field.
Since an increase in the AH differential pressure may greatly affect the drive power of the ventilating equipment
or the operation tolerance, it is important to grasp the secular change.
Normally, the AH soot blower is operated at intervals of work shifts (three times/day). If the AH differential
pressure increases, appropriate measures to shorten the interval are taken.
14

If the AH differential pressure becomes excessively large (normally, the reference level is the
planned value multiplied by “1.5”) or if the ventilating equipment capacity reaches its limit, it must
be investigated whether to water wash the AH.
For the pressure loss of the water and steam systems (particularly pressure loss of the furnace),
the increased speed caused by the secular change is grasped and it is used as a factor to judge the
chemical washing timing, etc.
2.1.2.3 Others
It is important to strictly control the water quality during boiler operation including startup
according to the standard for water treatment.
2.1.3 Auxiliary units of the boiler
Generally, the auxiliary units of the boiler are the feed water, ventilation, and fuel systems.
This section describes the ventilating equipment, air preheater, and coal pulverizer of the coal-fired
boiler plant.
2.1.3.1 Ventilating equipment
In the coal-fired boiler, a balanced air ventilation system is generally utilized to achieve the
following purposes.
1) The furnace pressure is maintained at a constant level to maintain combustion stability.
2) The furnace pressure is maintained at atmospheric pressure or lower in order to prevent coal ash from leaking
outside.
A centrifugal type or an axial flow type ventilating equipment (fan) is utilized. The control
system of the centrifugal ventilating equipment is the inlet damper control, inlet vane control, RPM
control, or a combination of them. The control system of the axial-flow ventilating equipment is
the moving blade variable control, inlet vane control, RPM control, etc. With these controls, the
process values for an object are controlled. The following lists up cautions operation.
Axial flow type: According to the characteristics of the ventilating equipment, there is a surging area. If the
operation point enters this surging area, the pressure and gas volume are changed rapidly
accompanied by vibration, causing damage to the unit.
Centrifugal type: There is no clear operation impossible area as described for the axial flow type. However,
the operation may become unstable in a low-load area, causing vibration or noise of the
duct.
(1) Induced draft fan (IDF)
This fan is intended to keep the furnace pressure at a constant level of atmospheric pressure or lower. To
prevent wear caused by coal ash, a dust removal equipment (EP, etc.) is installed downstream. Basically,
the PID control is used to control the furnace pressure. In many induced draft fans, the air flow rate signal
is used as an advance signal.
(2) Forced draft fan (FDF)
This fan is intended to feed the combustion air (secondary air) to the boiler. The air flow rate for
combustion is controlled by the combustion volume command from the boiler control unit and the
correction signal from the O2 control of the exhaust gas at the outlet of the boiler.
When two systems, that is, the ventilation system and air pre-heater, are installed in the boiler, the IDF is
interlocked with the FDF in the same system. There are many examples where the other fans are also
stopped if one fan is stopped.
This interlock is intended to prevent overheating of the gas temperature at the outlet of the air pre-heater
and decreasing in the air temperature at the outlet since an imbalance occurs between the air volume and
gas volume passing through the air pre-heater if the IDF or FDF is stopped.
(3) Primary air fan (PAF)
This fan is intended to feed the air (primary air) used to transfer the coal from the coal-pulverizing
machine to the burner.
15

I.
Boiler Boiler
Gas
Secondary
air
Mill
Primary air
Mill
Fig. 9 Cold primary air system Fig. 10 Hot primary air system
Moving vane auto Moving vane auto Moving vane auto
operation command operation command operation command
of A-induction fan of A-forced draft fan of B-induction fan
A-air pre-heater B-air pre-heater A-induction fan A-forced draft fan B-induction fan
startup startup startup startup startup
60s 60s 60s
Moving vane of
A-induction fan fully Auto operation of Auto operation of
closed moving vane of moving vane of
A-induction fan A-forced draft fan
Moving vane of Moving vane of
A-induction fan fully B-induction fan fully
closed closed
Moving vane auto
operation command
of B-forced draft fan
B-forced draft fan Ventilation system
startup startup completion
Auto operation of Auto operation of
moving vane of moving vane of
B-induction fan B-forced draft fan
Moving vane of
B-forced draft fan
fully closed
Fig. 11 Example of ventilation system startup sequence
Moving vane of A-induction Moving vane of B-induction Ventilation system
A-induction fan fully fan stop B-induction fan fully fan stop stop completion
closed 30s closed
Moving vane of A-forced draft fan Moving vane of B-forced draft fan
A-forced draft fan stop B-forced draft fan stop
fully closed fully closed
Fig. 12 Example of ventilation system stop sequence
The primary air also has the purpose of drying raw coal to allow easy pulverizing of raw coal to be
loaded into the coal-pulverizing machine in addition to the purpose of transferring the pulverized
coal.
The primary air temperature at the inlet of the coal-pulverizing machine is 180°C to 250°C. The
fan installation places and the number of fans to be installed in the cold primary air system are
different from those of the hot primary air system.
In the cold primary air system, one or two fans are installed on the upstream side of the air
pre-heater regardless of the number of coal-pulverizing machines. This fan is intended to control
the primary air duct pressure. On the other hand, in the hot primary air system, one fan specific
to one coal-pulverizing machine is installed on the downstream side of the air pre-heater. This fan
16

is intended to control the primary air flow rate.
Figures 9 and 10 show an outline of each system. Additionally, Figs. 11 and 12 show examples of
the startup sequence and stop sequence of the ventilation system, respectively.
2.1.3.2 Air pre-heater (GAH)
This air pre-heater is intended to increase the combustion air temperature and to collect the heat
of the exhaust gas at the outlet of the boiler. Generally, a regeneration-type air pre-heater is
utilized where hot gas and air are alternately made to contact the heat transfer materials called
“elements” to exchange the heat. There are two kinds of systems available: the Ljungstrom system
in which the elements are rotated, and the Rothemuhle system in which the elements are fixed and
an air duct called a “hood” is rotated.
Figures 13 and 14 each show GAH, respectively. Normally, the GAH is separated into two sections, that is, the
hot gas-passing section and the combustion air-passing section.
In the coal-burning boiler with the cold primary air system, the air side is separated into the primary and
secondary sections. The following describes cautions on operation of the regeneration-type air pre-heater.
1) Air leak
Center section on
high-temperature side
Sector plate on high-temperature side Primary air outlet
Gas inlet Guide bearing Secondary air outlet
Lubricant circulation
high S - o te o m t b p l e o r w at e u r r e o n s ide unit Sensor drive unit
Rotor drive unit
Heating element
Soot blower on low-temperature side
Main pedestal
Side pedestal
Connecting duct
Rotor
Pin rack Gas
outlet
Center section on low-temperature side
Rotor post Primary air Support bearing Seco i n n d le a t ry air
inlet
Fig.13 Example of Ljungstrom-type GAH
Secondary air outlet
Gas inlet
Primary air outlet
Collar seal
Soot blower
Primary air hood
Sealing frame
Secondary air hood
Stator Hood drive unit
Heat transfer surface
Main shaft Pin rack
Secondary gas outlet
Primary gas outlet
Primary air inlet
Secondary air Rotation unit
inlet
Fig. 14 Example of Rothemuhle-type GHA
In the regenerative air pre-heater, air leaking to the gas side cannot be avoided due to its structure.
17

I.
Therefore, it is required to adjust the seal appropriately.
Recently, as the capacity of the unit becomes large, the element diameter also becomes large. Additionally,
the thermal deformation volume becomes large. The leak volume cannot be suppressed by the fixed seal.
Therefore, an automatic seal adjustment unit is installed. If the air leak volume is too large, it’s necessary
to be cautious that the FDF, PAF, and IDF are overloaded.
Additionally, if the gap of the seal mechanism is made excessively narrow, the seal mechanism may make
contacts, causing current value hunting or overload of the GAH motor.
2) GAH differential pressure
If the temperature at the low-temperature part of the element decreases to a level close to the sulfuric acid
dew point, ash and SO3 chemical compounds are accumulated and the element is blocked. Additionally,
as the operation time elapses, the GAH differential pressure increases. It is difficult to remove the ash and
SO3 chemical compounds by the soot blow. Therefore, water washing is needed. It is very important to
always keep the temperature of the low-temperature part over appropriate temperature level or more.
(The temperature is controlled by the steam type air pre-heater.)
3) Fire of GAH element
If any combustible materials (used cables at the factory, wood chips, soot including unburned matter, etc.)
exist on the GAH element, a fire may occur due to the oxygen concentration and atmospheric temperature.
The risk of fire is the highest when a boiler with high oxygen concentration is started up or during boiler
banking.
Great attention should be taken since past cases also occurred while these two timings.
The following describes fire prevention measures.
1) No combustible materials shall be put on the element.
2) The element shall always be kept clean by the soot blow.
Additionally, it is also important to establish operation procedures if a fire occurs in the GAH.
2.1.3.3 Coal-pulverizer (Mill)
This coal-pulverizer is designed to pulverize coal to a fine particle size diameter necessary to burn
it by the burner. Generally, this machine is called “mill.” In the coal-burning boiler, this mill is
one of the important auxiliary units that greatly affect the operation characteristics of the plant.
The mill is classified into two types of the coal-pulverizing method, that is, the vertical mill (roller
mill, etc.) and the horizontal mill (tube mill, etc.).
Figures15 and 16 show overall diagrams of typical mills. The mill is composed of a duct, damper,
primary air chamber, seal unit, pulverizing unit, separator, pyrite emission unit, and pulverized
fuel pipe. In any mill, raw coal is dried, pulverized, coarse grain is separated, and transferred
continuously inside the mill.
Generally, the combustion volume is adjusted by changing the feed coal volume to be loaded into
the mill in the vertical mill. Additionally, the combustion volume is controlled by changing the
primary air flow rate passing through the mill in the horizontal mill. In the horizontal mill, the
feed coal volume is controlled to keep the coal seam level inside the mill drum at a constant level.
The following describes cautions on operation.
1) Remaining coal stop
In the normal mill stop cycle, after the temperature inside the mill has been lowered, the coal feed is
stopped and the coal remaining inside the mill is purged in that order.
18

Pulverized coal outlet
Coal
feed
port
Motor for rotary classifier
Rotary classifier
Housing
Reject chute
Coal feed pipe
Roller pressurizing unit
Roller
Table segment
Primary air port
Table
Primary air inlet
Motor
Speed reducer
Fig. 15 Example of vertical mill (Roller mill)
Coal feed
Pulverized pipe
Pulverized fuel pipe coal outlet
Coarse grain separator
Primary air inlet
Pulverized fuel pipe
Coal feed pipe
Motor
Mill drum
Fig. 16 Example of horizontal mill (Tube mill)
If the mill is stopped in case of an emergency, the above steps cannot be performed correctly. Pulverized
coal and raw coal exist inside the mill in relatively high-temperature status. Therefore, great caution shall
be taken since nature conservation or mill explosion may occur. This risk increases as the volatile
components included in the raw coal are large.
To prevent a fire inside the mill or to extinguish a fire, inert gas (inert steam) injection equipment or
fire-extinguishing water injection equipment are often installed. It is necessary to establish procedures if
the mill is stopped in case of an emergency.
2) Mill motor overload
When using coal (coal with low HGI) with poor grindability in the roller mill, the mill motor may be
19

I.
overloaded. In this case, the coal feed volume needs to be limited.
3) Temperature at mill outlet
If surface moisture of raw coal that is stored in an outdoor coal yard is high due to rain or other factors, raw
coal drying, pulverizing, and transfering processes are not performed smoothly. As a result, an accident
occurs which the inside of the mill is filled with coal. This phenomenon occurs if the mill differential
pressure increases. (In the tube mill, the current value of the mill motor is lowered.)
In the initial indication, it is shown that the temperature at the mill output is decreased.
If the temperature at the mill output decreases excessively and it cannot be maintained, appropriate
measures are needed to limit to the coal feed volume.
4) A/C
The weight ratio of the primary air volume that is the air for transfer of the pulverized coal to the
pulverized coal volume is called “A/C (Air/Coal).” Generally, the mill is operated at an A/C range of
approximately 1.8 to 3.0. If the A/C becomes high (the concentration of the pulverized coal is thin), the
naturalness of the pulverized coal is lost, causing an accidental fire.
Recently, a burner that allows stable combustion even though the A/C is high is put into practice.
However, if the A/C becomes high when using a burner other than such a burner, it is necessary to perform
combustion aid using the pilot ignition burner.
5) Flow velocity inside the pulverized coal pipe
The flow velocity inside the pulverized coal pipe from the mill to the burner shall satisfy the following
conditions.
1. This flow velocity shall be the flame propagation velocity. (The flame propagation velocity is
determined by the A/C and the volatile components included in the coal.)
2. This flow velocity shall be faster than the level at which pulverized coal is not subsided or accumulated
inside the pipe.
3. This flow velocity shall be slower than the level at which the inside of the pipe wears out.
Therefore, a velocity ranging from 18 to 30 m/s is generally used. The flow velocity inside the pipe is
almost determined by the primary air flow rate. However, the primary air flow rate shall not be
excessively decreased.
Mill system startup Mill system Mill system stop
conditions satisfied startup
Lubricant unit startup Pilot ignition Cool air damper open
Rotary classifier startup burner ignition Hot air damper closed Pilot ignition burner Cool air damper open
Roller pressurizing unit ignition Hot air damper closed
startup
Coal gate open
Mill inlet temperature
below specified value
Mill stop coal feed volume Mill outlet temperature
All mill outlet dampers open/Mill seal air damper open below specified value
Primary air shut-off/Regulation damper open
Mill warning Coal gate close/Coal feeder stop
Seal differential pressure/Primary air volume/Waiting for mill
temperature conditions satisfied
Mill purge
Mill motor startup
Coal supply Mill outlet Mill motor/roller pressurizing unit/rotary classifier stop
volume above Coal feeder startup temperature above
specified value specified value
Primary air shutoff/Regulation damper close All mill outlet dampers
close
Initial coal feed completion
Mill inlet seal air damper close
Pilot ignition burner OFF
Pilot ignition burner Auto operation of coal feeder
fire-extinguishing command SS
Fig. 17 Example of vertical mill startup Fig. 18 Example of vertical mill stop
Since the combustion volume rather than the primary air volume is controlled in the horizontal mill, the
auxiliary air damper is opened to keep the minimum flow velocity inside the pipe if the flow velocity
decreases.
6) Coal feed volume and coal consumption volume
When the mill is operated at a constant load, a relationship is established in which the coal feed volume is
equivalent to the coal consumption volume (combustion volume). However, this relationship is not
established when the mill is started or stopped or when the mill load varies.
Precise grasping of the combustion volume is an essential condition for boiler control. In particular, it is
20

absolutely necessary to control the steam temperature in the once-through boiler. Generally, the
combustion volume is measured by the coal supply machine. However, when the mill is started up, the
coal supply start does not meet the coal consumption start.
In the control system, when the mill is started up or stopped, the simulated coal consumption signal is used
as combustion volume in order to adjust the coal consumption close to the coal consumption characteristics
suitable for actual conditions. The coal consumption characteristics may vary depending on the type of
coal. Changes in steam temperature and exhaust gas O2 may occur when the mill is started up or stopped.
Therefore, these points must be taken into consideration.
7) Mill pyrite
Rocks or other foreign objects other than the raw coal supplied to the mill are discharged to the outside of
the mill without being pulverized. These discharged foreign objects are called “pyrites.” In the
horizontal mill, such foreign objects are not discharged to the outside and they are accumulated as materials
for pulverizing. In the vertical mill, pyrites are snapped from the primary air port inside the mill to the
primary air chamber, and then they are discharged to the outside. If this processing unit malfunctions,
pyrites and coal are accumulated in the primary air chamber. As a result, a fire may occur by the hot
primary air. Therefore, it is important to check that the pyrite-processing unit functions correctly.
According to the circumstances, the mill needs to be stopped.
Figures 17 and 18 show examples of the vertical mill startup sequence and stop sequence.
21

2.2 Power Supply Operations
Electric power demand is not always constant and it varies greatly depending on the season or time zone.
Since the daily electric power demand varies as time elapses as shown in the daily load curves stated in Fig. 27,
it is necessary to supply electric power corresponding to the demand that varies every moment.
Additionally, since the economy and followingness of each power generation method differ from each other, it
is also necessary to generate electric power with an appropriate combination of power generation methods by
taking their features into consideration. When the daily load is classified into the base load, middle load, and
peak load, each load is classified into the relevant power generation method as described below.
Pumping-up hydraulic power
Adjustable
hydraulic
power
kaeP Pumping-up
hydraulic
power
)rewop
cirtcelE(
Oil fired power
(Energy)
elddiM
LNG fired power
esaB Run-off-river Nuclear power Coal fired
hydraulic power power
(Time)
Fig. 27 Example of daily load curves and combination of power generation methods by time zone
(1) Base load
Since the variation in load is small and the utilization factor is high, large capacity thermal power, nuclear
power, and run-off-river hydraulic power, which can be operated continuously for an extended period of time and
has an excellent efficiency, are operated.
(2) Middle load
This middle load has intermediate characteristics between the base load and peak load. Since electric energy
larger than that of the peak load is required, the middle capacity thermal power, which is relatively economical
and has excellent start/stop characteristics, is used.
(3) Peak load
Since the load varies greatly in the peak load range, the excellent adjustment capability of electric power
generation and frequent start/stop ability are required.
Additionally, it is necessary that the operation time is short and the utilization factor is small.
Therefore, even though the efficiency is slightly sacrificed, pondage type hydraulic power or reservoir type
hydraulic power having less construction cost, or pumping-up hydraulic power or gas turbine having excellent
peak characteristics can be operated.
The following describes the typical operation method of a thermal power plant during daytime and nighttime.
2.2.1 Output adjustment by load dispatching operation
Since the electric power demand is changed every moment as described previously, it is necessary to supply
electric power corresponding to this demand. Since changes in electric power demand cannot be adjusted by
hydraulic power alone, it is also necessary to adjust the output using the thermal power generation plant. The
operation is performed using the following auto control together with the output adjustment based on the power
supply command.
(1) Automatic frequency control (AFC)
The system frequency varies due to an unbalance between electric power generation and demand. Therefore,
the generator output is adjusted so that the frequency of the electric power system is kept within the specified
value.
(2) Economical load dispatching control (ELD or EDC)
The load is dispatched so that the general power generation cost for each power generation unit becomes the
22

lowest price.
2.2.2 Minimum load operation
As nuclear power generation is used for the base load operation to the daily electric power demand, the
minimum load operation of the thermal power plants is conducted to adjust the supply capacity to the electric
power demand during daytime and nighttime. Therefore, this minimum load operation becomes important, as
well as stop operation during nighttime. In particular, it is required to enable lower minimum load operation of a
large capacity plant and to improve the power generation efficiency in a low load area.
The minimum load may vary depending on the fuel, capacity, main machine, and/or auxiliary machines of the
plant. However, the minimum load is generally 10 to 40% of the rated output.
The following describes the typical subjects and considerations related to the turbine during minimum load
operation.
(1) Steam flow rate
If the steam flow rate decreases, a local overheating problem occurs due to an unbalance of the flow rate
between the boiler overheating unit and reheater. Therefore, the steam temperature, gas temperature, and
evaporation tube wall temperature need to be considered. In the case of a once-through boiler, it is necessary to
keep a supply water volume of 25 to 30% or more of the maximum evaporation volume in order to ensure the
stable flow inside the evaporation tube constituting the water wall of the furnace.
(2) Wetness of turbine exhaust chamber
If the reheating steam temperature drops or the vacuum degree of the condenser increases during low-load
operation, the wetness of the exhaust chamber may increase. Since this wetness may corrode the vane in the
final stage of the low-pressure turbine, it is absolutely necessary to conduct the operation by taking the wetness
into consideration.
(3) Temperature of turbine exhaust chamber
The vacuum degree of the condenser tends to be high during low-load operation. This may cause the
temperature of the exhaust chamber to lower and adversely affect the vibration and differential expansion.
Furthermore, the steam flow rate may decrease at an extremely low output ranging from 5 to 10% of the rated
output. Therefore, the temperature of the turbine exhaust chamber may increase due to windage loss.
Generally, to prevent this problem, the water is continuously sprayed into the exhaust chamber to decrease the
temperature.
However, the continuous water spray may corrode the vane at the final stage. Therefore, great care should be
taken for this point.
(4) Drain control of feed water heater
The drain from the feed water heater must be collected to the feed water heater at the lower stage as much as
possible in order to improve the thermal efficiency. Therefore, the pressure inside the feed water heater
decreases in the low-load operation area and the pressure difference inside each feed water heater decreases. If
the pressure difference inside the unit among the feed water heaters decreases, it becomes difficult to discharge the
drain to the feed water heater at the lower stage. To prevent such a problem, great care should be taken, such as
switching of the collection destination to the condenser, etc.
(5) Control of boiler feed water pump
Since the supply water flow rate decreases during low load operation, the discharge flow rate of the boiler feed
water pump also decreases. If the supply water flow rate of the boiler becomes less than the re-circulation flow
rate of the pump, the operation enters a status whereby the minimum flow rate of the pump is maintained by the
re-circulation control valve. Therefore, great care should be taken since the control valve is damaged if the
pump is operated for an extended period of time in the above status. Additionally, when using the turbine driven
feed water pump, great care should be exerted so that the pump is not operated at a speed close to its critical
speed.
2.2.3 Leading power factor operation
In recent power systems, as the capacity of the extra-high voltage power transmission line or power
transmission line increases and the difference in generated power during daytime greatly differs from that during
nighttime, the leading power factor operation of the reactive power control is conducted so that the operation is
performed by changing the tap of the inductive phase modifying equipment (reactor or synchronous phase
modifier) or by operating the synchronous generator using the advancing power factor.
The leading power factor operation of the generator means that the field current of the generator decreases by
utilizing the characteristics of the synchronous machine and the operation is performed using the advancing power
factor to absorb the reactive power of the power system. The following describes the problems and notes when
23

performing the leading power factor operation of the generator.
(1) Stability drop due to low excitation
When the leading power factor operation is performed, the internal induced voltage becomes small.
As a result, the internal phase angle increases and synchronizing power decreases, causing the stability to lower.
The stability is determined by the terminal voltage and reactance of the generator, as well as the external
impedance. Therefore, when performing the leading power factor operation, it is necessary that the under
excitation limit (UEL) of the automatic voltage regulator (AVR) is set at a position where both the allowable limit
by the possible output curve of the generator and the static stability limit of the system are satisfied to prevent the
loss of synchronism.
(2) Temperature increase of iron core and mechanical part
If the leak magnetic flux entering the iron core end part of the stator increases, the temperature increases due to
the eddy current induced by the elements making up the iron core end part. Therefore, even though the stator
end part of the turbine generator uses a structure that suppresses the temperature increase, it is necessary to
conduct the operation with the possible output curve area of the generator by taking changes in the stator iron core
temperature, stator coil temperature, and cooling gas temperature into consideration.
Figure 29 shows an example of the generator output curve.
Curve AB: Limited by magnetic field temperature.
Curve BC: Limited by armature temperature.
Curve CC: Limited by armature iron core end temperature.
24
yaleD
]up[
rewop
evitcaeR
Active power (pu)
Under excitation limit (UEL)
ecnavdA
Fig. 29 Generator output curve

2.3 Start-up and Stop Operation Control
2.3.1 Start pattern
Electric power demand changes not only throughout the year, but also weekly and daily.
A thermal power unit start or stop in order to adjust its output to flexibly correspond to changes in power demand.
The unit has the following start patterns from unit stop to unit start.
(1) Cold start
The unit is started after it has been stopped for an extended period of time, such as for periodic inspection.
(2) Weekly start and stop (WSS)
In WSS, the unit is stopped at nighttime on a Friday or on a Saturday when the electric power demand
decreases, and then it is started early on Monday morning when the electric power demand starts increasing.
The stop time is 12 to 36 hrs. Figure 2 shows an example of this schedule.
Output
Main steam
temperature
Main steam
pressure
Fig. 2 Weekly start and stop schedule
(3) Daily start and stop
The unit is stopped at midnight, and then started the next morning so that the power generation corresponds to
differences in electric power demand between daytime and nighttime. The stop time is from 6 to 12 hrs. Figure
3 shows an example of the daily start and stop schedule.
This daily start and stop is necessary because efficient operation of the power system is achieved by increasing
the base load units, such as nuclear or large capacity thermal power generation.
In this daily start and stop operation, the adverse effects on the unit service life and supply reliability should be
considered. In the first case, thermal stress on the turbine rotor is a particularly problem.
Fig. 3 Daily start and stop schedule
25
ffo-lella
raP
noitingI tratS lellaraP
Output
Main steam
temperature
Main steam
pressure
lellaraP
ffo-
noitingI tratS lellaraP

(This thermal stress is caused by differences in temperature between the steam and turbine rotor when the unit
is started. Normally, this temperature difference is called “mismatch temperature”.) According to the low cycle
fatigue index (LCFI) of the turbine rotor, the number of yearly start and stop cycles is limited to take measures
against this problem. In the second case, the start and stop time is short and the operation reliability needs to be
kept at a high level.
To solve these problems, it is necessary to take appropriate measures, such as improvement of the unit
reliability, omission of operation steps, and/or review of standards.
(4) Quick start
This quick start is used to restart the unit after it has been stopped for a short time (about less than 6 hrs.) due to
system problems or power control. Normally, the quick start is called “very hot start”.
In this case, the thermal stress of the turbine requires special attention.
The metal temperature of each part meets the steam temperature immediately before the trip. However, since
the boiler and piping after restarting are cooled as the stop time elapses, the steam temperature is mismatched with
the metal temperature due to decrease of the steam temperature and throttle of the control valve. Therefore, it is
preferable that the steam temperature is increased to a high temperature level and the speed is increased rapidly,
and the parallel and load are increased.
2.3.2 Starting of unit
Figure 4 shows an outline of the start steps of the coal burning supercritical pressure voltage transformation
once-through plant. The following describes the operating procedures and provides notes on each start step.
(1) Determination of start schedule
The period of time required to start the unit is determined by the boiler or turbine status. As described in
Table 1, the unit start mode is determined by the metal temperature at the first stage of the turbine. As the time
required for each event is added, the overall time required for the start process is calculated.
In the start schedule, the parallel schedule time is determined to the base point. Based on the start time
required described above, the schedule time, such as boiler ignition, turbine start, and full load achievement is
determined.
Main steam Output
pressure
RPM
Water quality check
Fig. 4 Unit start steps (Cold start)
26
trats
tinu
rof
snoitaraperP
esaercni
muucav
dna
punaelc
retaw
desnednoC
punaelc
erusserp-woL
punaelc
erusserp-hgiH
punaelc
dloc
relioB
noitingi
reliob
rof
snoitaraperP
noitingi
relioB
punaelc
toh
relioB
/esaercni
erutarepmeT
esaercni
erusserp
trats
enibrut
rof
snoitaraperP
pu deeps/trats
enibruT
rof snoitaraperP lellarap trats
gnigrahc
laoC
revo-egnahc
T/M
PFB
revo-egnahc
yrd/teW
Parallel/ Output Output
output increase II increase III
increase 1
trats
noitamrofsnart
egatloV
gnirif
leuf
elgnis
laoC
kcehc
ytilauq
retaW
ylppus
rewoP
noitubirtsid

Table 1 Example of start modes
Start type Very hot start Hot start Warm 2 start Warm 1 start Cold start
Item Unit (Stopped for 2 hrs.) (Stopped for 8 hrs.) (Stopped for 32 hrs.) (Stopped for 56 hrs.) (Stopped for 150
hrs.)
Metal temperature at 1st stage °C 460 - 390 – 460 340 – 390 230 – 340 - 230
Main steam pressure MPa 8.5 8.5 8.5 8.5 8.5
Main steam temperature °C 510 470 410 410 400
Reheating steam °C 505 480 377 289 200
temperature
Steam temperature at 1st °C 438 391 315 315 301
stage
Metal temperature at 1st °C 494 453 368 326 216
stage
27
trats
ta
seulav
dennalP
Mismatch temperature °C -56 -62 -53 -11 +85
Turbine speed up ratio rpm/min. 300 300 150 150 100
Low-speed heat soak time min. 0 0 0 0 20
High-speed heat soak time min. 0 0 0 0 55
Initial load volume % 3 3 3 3 3
Initial load holding time min. 0 0 15 15 60
The boiler start mode is determined by the fluid temperature at the inlet of the water separator, and it is then
used for the fuel program for start or start by-pass valve control.
(2) Preparations for unit start
Inspect and check each part so that the work during unit stop is completed and there is no obstacle hindering the
start.
Confirm that units related to common facilities are being operated correctly or that they are ready for operation.
Confirm that the interlock, alarm device, and monitoring instrument function correctly, and that the fuel and
demineralized water necessary to start are maintained.
(3) Pre-boiler cleanup
In the once-through boiler, it is necessary to supply high purity water from the start.
Therefore, cleanup is carried out to remove impurities (particularly, iron content) from each system prior to the
ignition.
In the pre-boiler cleanup, the vacuum in the condenser is increased, and then the condenser system,
low-pressure supply water system, and high-pressure supply water system are cleaned up from the upstream side
in order.
In each system, the circulation operation is carried out through the condensate demineralizer so that the water
quality becomes the standard value or less after the standard to pass the water to the condensate demineralizer has
been satisfied using the blow outside the system.
Additionally, the turning operation of the turbine is performed to prevent deflection of the turbine rotor before
increasing the vacuum.
(4) Boiler cold cleanup
When the water quality in the pre-boiler satisfies the boiler passing water standard, the water is fed to the boiler
to perform the cleanup at a normal temperature. Table 2 shows the water quality standard when the once-through
boiler is started.
After the boiler has been filled with water (this work is not needed when the boiler filled with water has been
stored), the blow outside the system is performed through the drain system of the water separator. After the
water quality of the blow water has satisfied the standard for the water passed to the condensate demineralizer, the
circulation operation is performed until the water quality is the standard value or less through the condensate
demineralizer.
(5) Preparations for boiler ignition
The supply water system is changed from the cleanup status to the boiler ignition status.
The ventilation system is started to purge the furnace. The remaining unburnt gas is purged at a specified air
flow rate for a specified period of time in order to prevent explosion in the boiler furnace. (Example, 30% MCR
flow rate for 5 min.)
The fuel system for start (oil or gas) is started up to check the system for leak.
Generally, light oil is used for the start.
(Note) Cleanup is essential for a cold start. The cleanup is usually omitted for the WSS or DSS start. The operation often
enters the ignition preparations from the low-pressure cleanup circulation status during unit stop.
(6) Boiler ignition and hot cleanup
After the boiler has been ignited, the temperature is increased to the target temperature of the hot cleanup (fluid
temperature at the outlet of the furnace is approx. 150°C.). The temperature is kept at this cleanup target

temperature. If the water quality becomes the standard value or less, the temperature increase is restarted.
(7) Temperature increase and pressure increase
The temperature increase and pressure increase of the boiler are performed to achieve the steam conditions at
turbine start determined by the turbine start mode. By adjusting the fuel charging volume, the start bypass valve
and drain valve in the steam system, the temperature increase and pressure increase are completed within the
target time.
The feed water flow rate and air flow rate are controlled to their minimum flow rates. At this time, the
re-heater protection (prevention of burning) and the thick wall part protection (relaxing of thermal stress) exist as
limitation items when started. The former is limited by the gas temperature at the outlet of the furnace, as well
as the fuel charging volume. The latter is limited by the temperature increase ratio at the inlet of the water
separator and the outlet of the super heater.
(8) Preparations for turbine start
In the cold start, the metal temperature of each turbine part decreases to a level close to room temperature.
When starting the turbine in this status, thermal stress occurs as a result of the difference in temperature when
compared to the steam.
Table 2 Water quality at starting of once-through boiler (When the volatile substance process applies.)
Temperature increase/pressure
Circulation before ignition Load operation
Process (Boiler cold cleanup) increase circulation [1/2MCR (42) or less] (Boiler hot cleanup)
28
ssalC
Greater than Greater than Greater than
Greater than Greater than Greater than
Max. operating pressure (MPa) 15 and 20 or 15 and 20 or 15 and 20 or
20 20 20
less less less
Economizer pH (at 25°C) 8.5 – 9.6 (19) 9.0 – 9.6 8.5 – 9.6 (19) 9.0 – 9.6 8.5 – 9.6 (19) 9.0 – 9.6
inlet Electric conductivity (mS/m) (11)(19) (at 25°C) 0.1 or less 0.1 or less 0.1 or less 0.1 or less 0.1 or less 0.1 or less
(µS/m) (11)(19) (at 25°C) 100 or less 100 or less 100 or less 100 or less 100 or less 100 or less
Dissolved oxygen (µgO/l) 40 or less (36) 20 or less (38) 10 or less 10 or less 7 or less 7 or less
Iron (µgFe/l) 200 or less 100 or less 100 or less 50 or less 30 or less 30 or less
Copper (µgCl/l) 20 or less 20 or less 20 or less 10 or less 5 or less 5 or less
Hydrazine (µgN2H4/l) 20 or more (38) 20 or more (38) 20 or more 20 or more 10 or more 10 or more
Silica (µgSiO2/l) 30 or less 30 or less 30 or less 30 or less 30 or less 30 or less
Electric conductivity (mS/m) (11)(19) (at 25°C) 0.1 or less 0.1 or less 0.1 or less 0.1 or less - -
(µS/m) (11)(19) (at 25°C) 100 or less 100 or less 100 or less 100 or less - -
retaw
deeF
Furnace
water wall
outlet Iron (µgFe/l) 300 or less 300 or less 200 or less (40) 100 or less (41) - -
Note (38) This value becomes the target according to the boiler shape.
(39) When starting the unit after it has been stopped for a long period of time, it is preferable to adjust the hydrazine concentration to a higher level in order to promote forming
of a protective coat inside the system.
At this time, the hydrazine is dissociated in the water and it exists as the hydrazinium ion (N2H5 +).
(40) The target concentration of the iron is 100µgFe/l or less.
(41) The target concentration of the iron is 50µgFe/l or less.
(42) This shows an abbreviation of the maximum continuous rating that means the maximum continuous load.
To reduce this thermal stress, the warming of the casing and control valve must be carried out before starting
the turbine.
Additionally, it is important to check for faulty parts, such as the shaft position or eccentricity using the turbine
monitor instruments before starting the turbine through turning.
(9) Turbine start and speed up
Items to be considered most at turbine start are thermal stress and vibration problems.
Therefore, the warming (heat soak) is performed until the rotor temperature reaches the transition temperature
[temperature, at which the mechanical properties of the material lower rapidly (becomes fragile)] to prevent the
fragility of the turbine rotor from being broken or to reduce the thermal stress of the rotor surface and the stress at
the center of the rotor.
This heat soak is classified into two groups. The first group is the low-speed heat soak in which the turbine is
started with low-speed RPM kept in order to prevent the turbine rotor from being broken. The second group is
the high-speed heat soak in which the turbine is started at a rated RPM to prevent excessive thermal stress of the
rotor as the parallel and output increase.
As described above, the heat soak time and speed up rate are determined by considering the thermal stress in
order to control the service life of the rotor.
Additionally, it is necessary to determine a start schedule most suitable for the turbine so that vibration is
minimized.
To determine this turbine start schedule, the start load operation chart (mismatch chart) is provided. The heat
soak time and speed up rate are usually determined by the metal temperature at the first stage, as well as the main
steam temperature and pressure when the turbine is started up.
Table 1 shows examples of the speed up rate and heat soak time in each start mode. It is important that the
turbine is started according to the schedule created based on this chart and the operation is performed while
carefully checking the steam temperature so that the difference in temperature between the internal and external

metal surfaces of each turbine part and the steam temperature change ratio do not exceed their limit values.
The vibration and expansion difference are monitored during increasing of the turbine RPM.
Great care should be taken as the amplitude tends to be large at a speed close to the critical speed of the rotor.
In the boiler, as the turbine speed increases, the fuel charging volume is adjusted to keep the necessary steam
volume. For a cold start, the fuel charging volume is minimized before starting the turbine in order to reduce the
thermal stress applied to the turbine. It is also necessary to prevent excessive increase of the main steam
temperature by suppressing the increase of the fuel charging volume during speed up to the minimally required
level.
(10) Preparations for parallel
If heavy oil facilities are provided, light oil is changed to heavy oil before starting parallel output. Variations
in main steam temperature and main steam pressure are checked when changing light oil to heavy oil.
It must be checked that the ash processing facility, desulfurization facility, and denitration facility have been
started and they are in standby mode before charging the coal after parallel output has been started.
If the coal on the belt of each coal supply machine is discharged, each coal supply machine needs to be put in
coal on status.
(11) Parallel, output increase 1
When the turbine reaches the rated RPM, the generator voltage is increased to its rating, and then the turbine is
synchronized with the system to put in parallel status.
After the initial output is kept using the initial output volume corresponding to the turbine start mode, the
output increases to 20%ECR.
In the output increase process, the turbine valve is changed, the low-pressure/high-pressure feed water heater is
started, and the coal burner at the first stage is started.
Variations in main steam pressure in the process utilizing the bleed air and in the coal charging process are
checked carefully while the output is increasing. Additionally, it is also necessary to carefully check the NOx
and SOx control after the coal has been charged.
After the output has reached approx. 20%ECR, the boiler supply water pump is changed from the electric drive
(M-BFP) to the turbine drive (T-BFP). After that, the power at the station is changed (start transformation →
station transformation).
(12) Output increase II
The output increases to 50%ECR. The wet/dry of the boiler is changed at an output of approx. 25%ECR (the
boiler status is changed from recirculation to once-through status and the control system is also changed to
once-through control). By changing the wet/dry of the boiler, the boiler circulation pump (BCP) is stopped.
According to the voltage transformation mode, the main steam pressure starts increasing at an output of approx.
30%ECR. This operation is controlled by the boiler input command. However, in the output and main steam
pressure increase process after the wet/dry has been changed to “dry”, it is necessary to carefully check the
balance between the feed water flow rate and fuel flow rate, as well as variations in the steam temperature of each
part.
As the output increases, the coal burners are ignited in order and the oil burners are turned off to burn only coal.
Additionally, the second T-BPP unit is put in the service in status.
After the output has reached 50%ECR, the stable operation of the unit is checked and the water quality of each
part is checked. When the water quality satisfies the standard value, the drain is collected from the high/low
pressure supply water heater.
(13) Output increase III
The output increases to 100%ECR. As the output increases, the coal burners are ignited in order.
After the output has reached 100%, the operation status of the unit is checked and the patrol inspection is
performed at the work field to check that no errors exist. After that, load dispatching ferry is done.
2.3.3 Stopping of unit
When stopping the unit, the output is decreased sequentially according to the stop schedule in which the stop
period, heat radiation cooling during this period, and operation conditions for next start are taken into
consideration.
The stop method is classified into four groups as described below. Figure 5 shows an outline of the stop steps.
1) Normal turbine stop & boiler hot bank
This stop method is used to stop the unit according to the standard (normal) stop schedule, such as the
weekly start and stop and the daily start and stop.
29

2) Boiler forced cooling stop
This stop method is used to cool the boiler in a short time to ensure work safety during boiler related repair
work (in-furnace work or repair of pressure resistant parts, etc.).
The normal operation is performed until the units are put in the parallel-off status. After the units have
been put in the parallel-off status, water and air are fed continuously to cool the boiler.
3) Turbine forced cooling stop
This stop method is used to cool the turbine in a short time to ensure work safety if repair work needing the
turbine oil pump stop is needed.
The main steam pressure is normally kept at a higher level than the normal level corresponding to the
output drop, and the main steam temperature and reheating steam temperature are decreased to a lower
level than the normal target temperature to stop the units. Figure 6 shows a typical stop pattern.
In this case, boiler forced cooling needs to be performed for safety reasons.
4) Boiler & turbine forced cooling stop
This stop method is used to cool both the boiler and turbine when stopping the unit accompanying the
periodic inspection.
The following describes the operating procedures and cautions for the stop step.
(1) Preparations for unit stop
After the unit stop schedule has been determined, heavy oil warming and steam type air pre-heater (SAH) are
started when using heavy oil.
Output
snoitaraperp
fo
gnitratS
pots
tinu rof
revo-egnahc
tew/yrD
Fig. 5 Unit stop steps (Normal turbine stop)
30
trats
pord
tuptuO
trats
noitamrofsnart
egatloV
Output
Output drop I Output drop II drop III
noitingi
renrub
liO
revo-egnahc
M/TPFB
gnirif
leuf elgnis
laoC
ffo-lellaraP pirt
enibruT
ffo
relioB
Vacuum Boiler hot bank retention
Boiler forced cooling Vacuum
break

Pressure
Load Temperature
Re-heating steam temperature
Main steam
Load temperature
Main steam
pressure
RPM 1%/min.
RPM
0.5%/min.
Time
Load drop start Parallel-off.
360 min
Fig. 6 Example of turbine forced cooling stop
Additionally, the preparations for auxiliary steam supply from another boiler or a boiler in the plant are
performed.
(2) Output drop I
The output drops to 50%ECR.
When the output is approximately 95%ECR, the main steam pressure starts dropping according to the voltage
transformation mode. According to the output drop, the coal burners are turned off sequentially.
(3) Output drop II
The output drops to 20%ECR.
According to the output drop, the oil burners are ignited and coal burners are turned off.
Additionally, the first T-BFP unit is put in the service out status.
The drain tank level of the water separator increases when the output is approximately 25%
ECR. The BCP is started to change-over the dry/wet.
After the M-BFP has been put in the service in status, the second T-BFP is put in the service out status.
The output reaches 20%ECR. The transition to heavy oil single fuel firing is completed and the power
change-over in the plant (station transformation → start transformation) is completed.
(4) Output drop III, parallel-off
The output is dropped to the parallel-off target value (5%ECR).
The high-pressure/low-pressure supply water heater is stopped according to the output drop.
Additionally, oil burners are turned off in order.
When the output reaches the parallel-off target value, the parallel-off is performed.
(5) Turbine trip, boiler off
After completion of parallel-off, the turbine is tripped. After checking that the auxiliary steam is changed to
another boiler or a boiler in the plant, all oil burners are turned off.
When the burner purge is completed after the final burner has been turned off, the MFT is then operated to
check that all fuels are shut off completely.
After the MFT has been operated, the furnace purge is performed for 5 min.
2.3.4 Stopping of boiler
There are two kinds of boiler stop methods after parallel-off, that is, boiler hot bank stop and boiler forced
31

cooling stop.
The above stop methods are carried out according to the schedules even though there is a difference between
the plan stop and work stop. In addition to the above stop methods, there is a stop method by the MFT operation
during unit operation.
(1) Normal stop
When the unit stop schedule is determined, heavy oil warming or SAH is started according to the output drop
schedule time. The preparations are made so that the auxiliary steam can be supplied from another boiler or a
boiler in the plant.
When the output drop is started, the coal burners are turned off in order according to the decrease of the fuel
flow rate. When the output is approximately 95%ECR, the main steam pressure also drops according to the
voltage transformation program.
In particular, the balance among the supply water, fuel, and air (boiler input command, water-fuel ratio, air-fuel
ratio) should be checked carefully.
The heavy oil burners are ignited in order when the output becomes 50% or less. If the preparations for
ignition of the heavy oil burners are not in time, the output is kept at 50%ECR.
When the output becomes approximately 25%ECR, the drain tank level of the water separator increases. As
the BCP is started, the dry/wet is changed over.
The output reaches 20%ECR. Check that the transition to heavy oil single fuel firing is completed and the
power change-over in the plant (station transformation → start transformation) is completed. After checking the
above, the output drops to the parallel-off target value (5%ECR).
After the output has reached the parallel-off target value, the parallel-off is performed, and then the turbine is
tripped.
After checking that the auxiliary steam is changed to another boiler or a boiler in the plant, all oil burners are
turned off.
When the burner purge is completed after the final burner has been turned off, the MFT is then operated to
check that all fuels are shut off completely. After the MFT has been operated, the furnace purge (after purge) is
performed for 5 min.
(2) Stopping of boiler hot bank
After the MFT has been operated and the furnace purge has been completed, the ventilation system and
water/steam system are sealed to minimize the heat loss of the boiler as preparations for restart.
The contents of the stop operation are described in clause 1.3-(5).
The result data of the boiler pressure drop rate and steam temperature drop rate during hot bank is grasped. If
the drop rate is excessively fast, check whether any leak comes from the start bypass valve, or the main
steam/super-heater drain valve.
Heat or pressure remains in the boiler during hot bank. As a rule, the operation and adjustment of the boiler
system valve, and the inspection and work of the equipment leading to the boiler system valve, and the opening of
the manhole must not be performed.
(3) Boiler forced cooling stop
Before conducting the inspection work or periodic inspection work related to the boiler, forcibly cool the boiler
to stop it in order to enable safe work on the turbine side.
The contents of the stop operation are described in clause 1.3-(6).
After forced cooling has been completed, the boiler storage status may vary depending on the stop purpose.
Table 6 shows examples of storage methods (except for plant that the oxygen process applies to the water
process).
Actually, water filled status or nitrogen disused status often occurs. In this case, the boiler water is blown
completely after the forced cooling has been completed, and then the boiler is stored in the dry status.
(4) Measures for MFT operation
The operators must understand the causes of the MFT operations fully. If MFT occurs, check that the
protection interlock functions properly. Additionally, the boiler must not be restarted until the cause of the MFT
has been located and corrective action has been taken.
The following describes the measures to be taken after the MFT has been activated when the operation of the
auxiliary machine in the ventilation system is continued.
1) Check items after MFT
(cid:120) The fuel shut-off valve, burner valve, and SH/RH spray valve are closed.
(cid:120) The auxiliary machines are tripped. (Mill, coal supply machine, PAF, and RFP, etc.)
32

(cid:120) The mill hot air gate and damper are closed.
(cid:120) The burner complete off alarm signal send items through the television set inside the furnace.
2) The air flow rate is the furnace purge air flow rate (normally, 30% of MCR flow rate). The furnace is
purged for 5 min. or longer.
3) The auxiliary steam supply is changed to another boiler or a boiler in the plant.
4) To prevent fire caused by spontaneous ignition, the air is flown at the minimum air flow rate to purge
the flammable contents of the coal remaining in the mill and pulverized coal pipe in order to cool the
inside of the mill (volatile purge). If a mill inert system is provided, the mill is made inert to prevent a
fire.
5) Each part of the boiler is inspected visually to check that no faults exist. In particular, when the MFT
is operated from the high-output, the solenoid escape valve (PCV) may be activated. Therefore, it is
necessary to check that no leak exists after activation.
6) After the cause of the MFT has been found and corrective measures have been taken, the operation is
restarted. At this time, if it takes long to locate the cause, it is possible to stop main auxiliary machines
in the ventilation system, but the damper in the gas duct is put in the natural ventilation status (to purge
the volatile content).
7) After the pilot torch has been ignited, oil remaining in the trip burner is purged.
8) Coal remaining in the mill is purged after parallel. Additionally, if the mill clearing system is provided,
the remaining coal is processed by the clearing when the preparations for pyrite processing unit are
completed.
Table 6 Example of storage methods in case of once-through boiler stop
Stop period 1 2 3 4
48 hrs. or less 48 hrs. to 1 week 1 week or more to 1 month 1 month or more
Item
Boiler main body Hot banking Nitrogen sealing storage or Nitrogen sealing storage or Nitrogen sealing storage or
From economizer to (Valve is closed with water filling storage water filling storage water filling storage
outlet of water normal operation kept.) NH 50 – 100 mg/λ NH 100 – 300 mg/λ NH 300 – 500 mg/λ
2 4 2 4 2 4
separator
Super-heater and Same as above. Same as left. Nitrogen sealing storage Nitrogen sealing storage
re-heater (Re-heater: Dry storage) (Re-heater: Dry storage)
If the auxiliary machine in the ventilation system is tripped, the furnace must be purged after the damper in the
gas duct has been put in the natural ventilation status. Additionally, when all power supplies are lost, it is
checked that the fuel is shut-off and the back-up operation of the AH is performed by the air motor and that the
damper in the gas duct is put in the natural ventilation status.
(5) Operation of Soot Blower When Unit Is Not Used 〜Boiler clinker removal〜
When working inside the furnace during the suspension of boiler operation, it is necessary to conduct clinker
removal before paralleling off in order to ensure safety against clinker fall.
2.3.5 Concept of turbine start
Thermal power generation facilities in Japan were originally positioned for adjustment of the load. However,
thermal power generation actually comprises approximately 60% of all capacity, and this output will continue to
be important in the future. Additionally, thermal power generation facilities are considered increasingly
important for stable energy supply.
Thermal power generation facilities are classified into two groups, combined power generation facilities having
high efficiency and excellent operability, and conventional power generation facilities utilizing various fuels and
having rich operation results. Continuing the operation of conventional power generation facilities is important
in order to maintain a range of energy sources, and there are plans worldwide to construct thermal power
generation plants mainly using coal. Since coal is dispersed worldwide and its deposits are abundant,
conventional thermal power generation plants are being constructed.
It is desirable to increase the capacity of conventional power generation facilities and to improve their
efficiency levels in order to reduce greenhouse gas emissions. In 2000, commercial operation started of
Tachibana Bay Plant, controlled by Electric Power Development Co., Ltd. This state-of-the-art large capacity
plant (1,050MW) has a main steam pressure level of 25MPa and a temperature of 600 °C, and utilizing high steam
conditions with a re-heating steam temperature of 610 °C.
However, the turbine has many small gaps and is rotated at high speed and high temperature. Therefore,
rubbing or excessive thermal stress occurs, causing damage to the unit.
For this reason, utilization of the proper operation method and monitoring method is more important by
considering extension of the periodic inspection, which has been utilized recently.
As the number of new plant being constructed in Japan is decreasing rapidly, and the construction and
maintenance of power generation plants are shifting overseas, the remote monitoring service business is started.
33

The following items can be monitored by the manufacturers in their own country.
2.3.5.1 Reduction of thermal stress
Thermal stress occurs inside the steam turbine caused by differences between the temperature of each steam
turbine part and the steam temperature to be ventilated.
The cautions on the turbine start plan is that this thermal stress occurring in the rotor and casing is reduced.
The thermal stress of the high-pressure rotor operated under the severest conditions is monitored to control the
LCFI (Low Cycle Fatigue Index). To monitor this thermal stress, the metal temperature at the outlet of the first
stage of the turbine is determined as a representative measurement point. This measured metal temperature
value is used to make the judgment.
According to the metal temperature at the first stage achieved by natural cooling during the stop time and the
turbine plan ventilation temperature, which has been adjusted with the boiler side beforehand, the start mode is
classified into those described in Table 7. As the stop time is longer, the start time also becomes longer.
Table 7 Examples of start mode classifications and stop time levels
Start mode Stop time Remarks
Very hot start Stopped for up to 4 hrs. from
immediately after turbine trip.
Hot start Stopped for 8 to 11 hrs. DSS: Parallel-off at midnight and parallel-in the next
morning.
Warm start I Stopped for 32 hrs. WSS I: Parallel-off at midnight on Saturday and parallel-in on
Monday morning.
Warm start II Stopped for 56 hrs. WSS II: Parallel-off at midnight on Friday and parallel-in ion
Monday morning.
Cold start Stopped for 150 hrs. or longer Stopped for 1 week or longer.:page 15
RPM: 3600 rpm Load: 100%
Vacuum degree
Main steam pressure
(Vacuum pump start) (Preparations for ignition M - BFP start/Ignition) (Parallel-in (initial
(Condensate water cleanup) (Low-pressure cleanup) (Turbine start) load holding))
(High-pressure cleanup) (Rub check) (M/T change-over)
(Boiler cold cleanup) (Low-speed heat soak) (2nd T-BFP turn ON)
(Boiler hot cleanup) (Speed up start)
Fig. 19 Example of typical start
As described above, the natural cooling is started and the rotor temperature is changed according to the turbine
stop time. The typical start mode is classified into various typical classes because the operation mode is
classified into patterns by operation style. To relax the thermal stress that occurs as a result of the difference in
temperature between the main steam and rotor, it is necessary to adjust the start method.
As described above, since the time needed for the start is different from the stop time, it is important to grasp
the start time for the power supply plan.
Figure 19 shows the events in the typical cold start processes. The following introduces the main monitoring
items in the start process.
(1) Pre-warming
In the cold start in which the turbine is started from almost room temperature, warming of the high-pressure
turbine is needed to reduce the thermal stress. The metal temperature after the first stage is controlled. This
pre-warming is intended to reduce the brittleness of the rotor even though it depends on the material.
(2) All-around flow operation
To reduce the thermal stress of the construction, casing close to the nozzle at the first stage or nozzle during
ventilation, the all-around flow operation (full-arc operation) is performed. When using the machine control
method (MHC), the sub-valve of the MSV is opened to perform.
When using the individual oil tube method using the electric control method (EHC), all control valves are opened
slightly to perform this method. At approximately 7% of the load after starting, the partial insertion operation is
started. Figure 20 shows the relationship between the opening of the control valves and load during this partial
34

insertion operation as an example of the voltage transformation operation.
maets
niaM
sevlav
lortnoC
erusserp
gninepo
Fully opened.
4th valve
1st to 3rd
valve
Load
Fig. 20 Example of pressure and control valves opening during voltage transformation operation
(3) Low-speed heat soak operation
In the cold start, the heat soak operation is performed by the steam passing through the turbine in the status that
the heat transfer effect is high. This operation is performed by taking the critical RPM of the generator having
the lowest critical speed into consideration. This RPM is generally about 800 rpm.
(4) High-speed heat soak
When the RPM reaches the rated RPM, the heat soak operation is started to further heat up the turbine evenly.
At this time, since the heat transfer effect becomes high together with the stream flow rate, the initial load holding
time may be extended.
2.3.5.2 Other limited factors related to start
Important items to be monitored other than factors related to the thermal stress are those related to the vibration
and elongation difference. The following shows items related to the vibration.
(1) Eccentricity
In an example 700MW-plant, the maximum diameter of the steam turbine shaft is approximately 500mm, a
large diameter. The span between the bearings is approximately 6m. Therefore, to suppress the bend of the
rotor, it is necessary that the turning is generally performed for approximately 10 hrs. or more to set the
eccentricity to the standard value or less.
Table 8 Vibration control values
Detection location Shaft Bearing Remarks
Detection RPM 3000rpm/3600rpm 1500rpm/1800rpm 3000rpm/3600rpm 1500rpm/1800rpm
Rated speed or
12.5 17.5 6.2 8.7
more
Alarm value
Less than rated
15 21 7.5 10.5
speed
Stop value 25 35 12.5 17.5
(2) Vibration limit value
The turbine speed must pass through various critical speed ranges including the generator until the turbine
reaches the rated RPM. Additionally, since the turbine is a large high-speed rotating unit, the vibration may
increase due to the eccentricity and bearing lubrication status or small imbalance.
Therefore, it is necessary to set the alarm value and stop value, which are the control value or less as shown in
Table 8 according to “Technical standard for thermal power generation facilities” and “Electric technical standard
for steam turbine for thermal power generation and standard for generator vibration”.
Furthermore, the control is used by which the vibration amplitude and vibration increase rate are determined as
parameters and the control is classified into the safe zone, alarm zone, and trip zone. In this control, the
previously described three zones are classified into “critical speed range or less”, “critical speed range”, and
“critical speed or more” by the RPM range to control the turbine vibration by computer.
35

Start
erutarepmet
liO
Continuous
turning
Turning α RPM of Rated Control valve
disengagement rating RPM change-over
Stop
Fig. 21 Example of bearing lubricant oil temperature setting and monitoring
(3) Oil temperature
It is important to control the lubricant oil temperature in order to form a stable lubricant film, to protect the
bearing, and to prevent oil whip. The temperature width shown in Fig. 21 is set to change the control value
according to the turbine operation status (RPM).
(4) Metal temperature
It is important to monitor the bearing metal temperature for protection of the bearing metal. The temperature
monitoring conditions may vary depending on the bearing shape, such as thrust bearing, oval journal bearing, or
tilting pad journal bearing. Additionally, it is also important to monitor rapid changes in metal temperature.
(5) Vacuum degree in exhaust chamber
If the vacuum degree is much higher than the design value (pressure inside the condenser is too low), the
low-pressure casing is deformed, causing rubbing to occur. Additionally, as the vacuum degree decreases, the
vibration stress at the final stage increases.
(6) Temperature in exhaust chamber
It is further important to control the temperature around the final stage as the vane at the final stage is made
longer. Measures for protection of the final stage, such as use of casing spray are taken so that flexibility of the
operation is not lost.
(7) Limitations on wetness
Monitoring is important for protection of erosion on the vane at the final stage. Even though the wetness at
the outlet of the final stage is generally controlled in a range of 8 to 12%, it is necessary to take appropriate
measures or to perform the monitoring in a range exceeding this wetness range. The start point of the expansion
curve of the re-heating part, that is, the pressure and temperature of the re-heating steam must be monitored.
Figure 22 shows a conceptional diagram of the typical wetness limitation curve expressed by the equivalent
re-heating steam pressure line that indicates the re-heating steam conditions for wetness of 12%. The lower
portion of each re-heating pressure curve shows the operable range.
36
erutarepmet
liO Continuous turning
Equivalent to control valve Turbine α RPM of Turning
change-over load trip rating start

The lower portion of each re-heating steam pressure shows
the operable range.
eerged
muucaV
Equivalent re-heating steam
pressure line
Re-heating steam temperature
Fig. 22 Concept of wetness limit curve
Under the operation conditions, the motion that comes and goes between the wet area and dry area is called
“dry and wet alternation”. However, it is important that coming and going between the wet area and dry area are
eliminated at the final stage or L-1 (stage one before the final stage). Impurities in the steam may accumulate in
the nozzle and on the vane due to dry and wet alternation, causing corrosion to occur.
37
emit
elbawollA
Frequency
Fig. 23 Concept of frequency limit curve (example of rating 3600rpm)
(8) Frequency limit value
The principal vibration of the vane at the final stage is designed so that it is separated well properly to the rated
RPM. However, the operation may be performed with the principal vibration beyond the rated RPM as the effect
on the system side is received.
Figure 23 shows the frequency limit curve. The control of the service life is “Σtf/Tfo ≤ 1.0” and the operation
needs to be performed without exceeding this formula.
t f : Cumulative operation time at frequency (f).
Tf0 : Allowable operation time at frequency (f).

High and medium pressure rotor
expansion direction Low pressure rotor expansion direction
High pressure expansion Thrust bearing Low pressure expansion difference meter
differencemeter
High Medium Low pressure A Low pressure B
pressure pressure
High and medium
High and medium pressure casing (Second bearing base)
pressure bearing base Combined with low pressure Low pressure A Low pressure B
on front casing casing casing
High and medium pressure and low pressure A Low pressure B expansion
expansion direction direction
Fig. 24 Example of casing and rotor expansion directions
(9) Expansion difference
The rotor is warmed earlier than the casing at startup, on start.
Figure 24 shows a concept of the rotor and casing moving directions as a typical example of three casing types.
The difference in expansion between the rotor and casing may become the biggest on the anti-generator side of the
high pressure turbine and the generator side of the low pressure B turbine. The elongation difference meter is
provided on these parts as shown in the drawing to monitor them.
Figure 25 shows an example of the monitoring method. Rotor long means that the rotor is extended longer
than the casing. Rotor short is opposite to rotor long. The green mark shows the status that the turbine rotor is
kept pushed against the front side in the cold condition.
The red band shows the area causing contact in the axial direction.
As the rotor is rotated, it is pulled by centrifugal force in the circumferential direction and it is then shortened.
38
deR kram neerG kram
Orange
Red band band Red band
tniop
mrala
ts1
tniop
mrala
dn2
Max. rotor short
Max. rotor long
Fig. 25 Example of limitations on expansion difference
That is, even though the rotor does not enter the red band on the long side during operation, it is extended as it
is released from the centrifugal force in the stop process.
As a result, the rotor may enter the red band area.
On the contrary, when the rotor is started in a status close to the short side before the RPM is increased, it may
advance toward the rotor short side as the RPM is further increased.
This width shows the portion between the red mark and the first alarm point, and the orange band.

2. 4 Performance Management
2.4.1 Grasping of performance
In the performance control of thermal power plants, the constant, accurate grasping of unit operation, and
working to improve thermal efficiency are most important.
As a method to grasp performance, the deviation from the desired value which can be expected as long as the
equipment is operated normally including the acceptance performance test results etc., and also initial design
values at the start of operations are controlled. This desired value comprises operation status values such as the
temperature and pressure of each part, and performance values such as unit efficiency and boiler efficiency. The
latter performance values change by external conditions and therefore revision of the same conditions is necessary
for making comparisons. Setting of coefficients for revision may be performed by theoretical calculation or by
testing.
Next, in order to reasonably maintain facility performance in thermal power plants, in general, daily control is
made so that appropriate measures may be taken by monitoring the operation status. By monitoring the necessary
control items by instruments, daily operation log, calculators, etc., abnormal conditions are detected early and by
conducting operation and maintenance properly, efforts are made to perform reference value operations.
On the other hand, every day operation conditions are grasped from operation records and typical items which
affect performance (condenser vacuum degree deviation, exhaust gas temperature, exhaust gas O ) are plotted by
2
day, ten days, month in graphs, and the trend controlled. Especially, in regard to power plants with coal energy and
such where coal quantity, quality cannot be grasped in real time, the plant situation is grasped by trend control.
Also, to evaluate performance and thermal efficiency improvement measures at the time of regular inspection,
performance test items (high pressure turbine internal efficiency, air preheater efficiency, feed water heaters, etc.)
were grasped and simultaneous records taken on the overall unit for detailed control.
2.4.2 Grasping of equipment performance
To control performance changes of the unit, unit performance tests were conducted regularly, and efficient
operation, maintenance and improvement of facilities are being undertaken.
In general, performance tests were conducted with minimum output, 2/4 output, 3/4 output and rated output and
items such as plant thermal efficiency are being measured.
2.4.2.1 Heat input and output of a thermal power plant
An example of fuel, electric output, and various losses of a thermal power plant is shown in Fig. 2.4.2.1. The major part
of fuel consumed in boiler combustion is used for the generating of steam. This steam is sent to the turbine but a
little over ten percent of the heat quantity are discarded into the atmosphere as exhaust gas. Steam that flows into
the turbine expands inside the turbine and works to rotate the generator to generate electric power. During this
time, a part of the work becomes mechanical loss such as by bearings, etc. and also becomes generator loss. The
steam which has expanded with the turbine exhaust pressure flows into the condenser where it is cooled to
become condensed water while the heat quantity possessed by the steam is discharged into the cooling water of
the condenser.
Heat loss by exhaust gas
Mechanical
Cycle loss loss Generator
loss In-station
motive
power
Turbine end Gross electric Net electric output (F)
Boiler fuel output (D) output
(A) Turbine room heat (E)
input
(B) Heat discharge
loss (G) to
condenser
Boiler auxiliary
steam (C)
Fig.2.4.2.1
39

With oil fired thermal power use boilers, furnaces into which air is forced drafted by a force draft fan are widely
adopted. With this system, operation is performed with the pressure inside of the furnace or flue higher than the
atmospheric pressure and therefore caution must be exercised on leakage of gas and measures taken. Also, in the
case of coal fired boilers, blast furnace gas or coke oven gas burning boilers, a balanced draft system in which the
gas pressure inside the furnace is maintained slightly lower than the atmospheric pressure by an induced draft fan
is mainly adopted.
The reason for this is that with coal fired boilers, consideration is made for ash leakage and with blast furnace
gas and coke oven gas fired boilers, the fuel gas containing a large amount of CO is hazardous and the supplied
pressure of fuel gas is low.
With boiler capacity becoming greater, the consumed motive power of force draft fans and induced draft fans also
becomes greater and therefore it becomes necessary to restrain the draft loss of the convective heat transfer
surface to a suitable value. Table 2.4.2.1 shows an example of draft loss of respective parts of a large capacity
boiler of the coal fired balanced draft system.
Table 2.4.2 .1Example of draft loss of a boiler (Calculated values at maximum continuous load)
Draft loss
Items
kPa
Air (secondary) side pressure loss
Forced draft fan inlet air duct and silencer 0.54
Forced draft fan outlet air duct 0.43
Air preheater 1.37
Air preheater outlet - Burner wind box inlet air duct 0.59
Burner wind box 1.47
Total 4.40
Gas side pressure loss 1.37
Superheater - Economizer 1.03
NOx remover 1.52
Air preheater 1.59
Gas, gas heater, and electrostatic precipitator 0.84
Economizer outlet - Induced draft - fan inlet flue and silencer 1.06
Induced draft fan outlet flue and chimney
Total 7.41
Total pressure loss of air and gas 11.81
40

2.4.2.2 Boiler
When calculating boiler efficiency, it is necessary to clarify whether the standard of the fuel calorific value is of
a high level calorific value containing latent heat of vaporization at the time the moisture from hydrogen in the
fuel becomes steam or whether it is of a low level calorific value in which latent heat of vaporization is deducted
from the high level calorific value.
In this chapter, explanation is provided with high level calorific value as the standard.
As a method to obtain boiler efficiency, the quantity of heat which is transferred to the feed water in the boiler
and used to generate steam is compared with the heat quantity which should be generated by the combustion of
the fuel fed to the furnace. This is called the heat input output method and is expressed by the following
equation.
W (h -h)
s 0 l
Boiler efficiency= ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(1)
G H
f h
Where WS is the boiler steam quantity kg/h, h , h is the generated steam and feed water enthalpy kJ/kg, G is
0 1 f
the fuel consumed quantity kg/h, and H is the high level calorific value of fuel kJ/kg.
h
As another method, the boiler heat loss is calculated from the exhaust gas temperature and the exhaust gas
amount after passing the entire generating surface of the boiler, (the outlet if there is an air preheater) and by
deducting this from 100%, the boiler efficiency is obtained. This is called the heat loss method and is calculated
by the formula mentioned later. The heat loss becomes less as the exhaust gas temperature is lowered and boiler
efficiency rises but for this a larger air preheater generating surface is required and facility expenses increase.
Additionally, in the case where fuel containing sulfuric
content is used, the problem of low temperature corrosion (sulfuric corrosion) occurs and therefore it is important
to select a suitable exhaust gas temperature in planning the boiler. In current boilers, the exhaust gas temperature
is set at 130 - 150°C with coal and heavy oil (crude oil) fuel, at 165°C with high sulfuric content heavy oil, etc,
and around
100°C with gas fuel but with certain fuels, normally an environment preserving device (Electric dust collector,
desulfurizing equipment) is installed for the back wash and therefore it is necessary to optimize the exhaust gas
temperature in the entire facility including this.
(1) Dry exhaust gas loss L
1
Out of the heat loss by the exhaust gas discharged from the outlet of the boiler (air preheater), when the portion
by latent heat of dry gas is assumed to be:
G : Dry gas amount per 1 kg of fuel kg/kg
dry
C : Average specific heat of dry gas ≒１.0 kJ/kg°C
g
t : Air preheater outlet exhaust gas temperature °C
g
t : Boiler efficiency standard temperature °C
o
G C (t -t )
dry s s o
L
1
= ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(2)
H
h
(2) Loss L by hydrogen moisture in the fuel
2
Out of the heat loss by the exhaust gas exhausted from the boiler (air preheater) outlet, the loss caused by
evaporation of the moisture produced from hydrogen in the fuel and the contained moisture during combustion of
the fuel and moreover the loss caused by heating up to the temperature of exhaust gas and discharged:
Where;
M : Moisture produced from hydrogen in 1 kg of fuel and the moisture kg/kg contained in the fuel
f
∆ : Latent heat of vaporization contained in moisture ≒ 2,500 J/Ks
hR
C : Average specific heat of steam ≒ 1.9 J/kg°C
m
C : Specific heat of water at reference temperature ≒4.2kJ/kg°C
w
M (∆ +C -t -C -t)
f hR m s w s
L
2
= ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(3)
H
h
41

(3) Loss L by moisture in the air
3
Out of the heat loss by the exhaust gas which is discharged from the boiler (air preheater) outlet, the loss caused
by latent heat of moisture contained in the air for combustion is assumed to be:
M : Moisture contained in air for combustion per 1 kg of fuel, whereby:
A
M C (t -t )
a a s o
L
3
= ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(4)
H
h
(4) Loss L4 by radiation heat
It is difficult to accurately obtain the heat loss radiated into the atmosphere from the peripheral walls of the
boiler and appurtenant facilities. This loss becomes proportionally smaller with large capacity boilers because
their surface area becomes relatively smaller and also because the radiation heat amount is roughly constant
irrespective of the load; the proportion of loss becomes smaller as the load becomes larger.
(5) Loss L5 by unburned fuel gas
This is the heat loss due to the combustible gas remaining such as CO in the fuel gas because of incomplete
combustion.
23,700×C (CO)
L
5
= × ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(5)
H (CO )+(CO)
h 2
Where;
23,700 : Lost heat amount kJ/kg when carbon becomes CO by incomplete combustion of
carbon in the fuel
C : Combusted carbon amount kg/kg in 1 kg of fuel
(CO, CO ) : CO and CO density vol. % in exhaust gas
2 2
Besides the above, there is combustible gas loss by unburned hydro-carbons and H but these are of minute
2
amounts which can be neglected in current commercial use boilers.
(6) Loss L by combustion residue
6
This is heat loss mainly by unburned carbon in the combustion residue by combustion of solid fuel.
33,900×C'
L
6
= ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(6)
H
h
Where
33,900 : Combusted heat amount KJ/Kg of carbon
C’ : Unburned carbon amount KJ/Kg per 1 kg of fuel
This heat loss in liquid and gaseous fuel is negligible.
(7) Other loss L
7
Besides the above, there are small losses such as by carrying out of combusted ash or steam atomizing or heat
losses which cannot be measured or for which the cause is unknown and these are treated as other losses. Errors
of measuring instruments may be included in this loss.
From the above heat losses, boiler efficiency may be expressed by the following equation
7
Boiler efficiency=100−∑Li⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(7)
l=1
Table 2.4.2.2 shows examples of boiler efficiency and heat loss of commercial use boilers for exclusive firing
of heavy (crude) oil, of natural gas and of coal.
With natural gas, the hydrogen content during combustion is approximately double that of heavy (crude) oil and
therefore the loss by hydrogen moisture content during combustion is great. Since the exhaust gas temperature is
low, dry exhaust gas loss is small but boiler efficiency becomes approximately 2% lower compared with heavy
(crude) oil. Also with coal, the hydrogen content during combustion is even less than that of heavy (crude) oil and
therefore even when loss by unburned carbon is considered, boiler efficiency tends to become the highest among
the three fuels. However, coal characteristics will differ greatly by origin and caution must be exercised in the
evaluation of its efficiency.
42

Table 2.4.2.2 Examples of heat loss by boiler efficiency (Calculated values by rated loads)
Heavy (crude) oil Natural gas Coal exclusive
exclusive boiler exclusive boiler boiler
Exhaust gas temperature °C 140 99 135
(Air preheater outlet)
Excessive air factor 1.14 1.16 1.20
(Air preheater outlet)
Boiler heat loss
Dry exhaust gas loss % 4.33 2.70 4.31
Loss by hydrogen content during % 6.53 10.19 4.03
combustion
Loss by moisture content in air % 0.07 0.05 0.09
Loss by radiation heat % 0.17 0.17 0.17
Loss by unburned fuel gas % 0.00 0.00 0.00
Loss by combustion residue % 0.00 0.00 0.52
Other losses % 1.00 1.00 1.50
Total % 12.10 14.11 10.62
Boiler efficiency % 87.90 85.89 89.38
(Higher calorific value standard)
43
)%(
)dradnats
eulav
cifirolac
rehgiH(
ycneiciffe
relioB
Coal fired boiler
Heavy (crude) oil firing boiler
Natural gas fired boiler
Boiler load (%)
Fig. 2.4.2.2 Relation between boiler efficiency and boiler load
Also, in general, with heavy (crude oil) fired boilers, the air preheater low temperature end average metal
temperature is controlled by a steam type air preheater and as a result, the lowering of exhaust gas temperature at
low load is small and boiler efficiency becomes maximum between the rated load where excessive air factor is
low to 75% load.
On the other hand, with exclusive natural gas fired boilers and exclusive coal fired boilers, the exhaust gas
temperature drops greatly with lowering of load and therefore boiler efficiency tends to become maximum with a
load of around 50 to 75%. At loads lower than this, boiler efficiency tends to drop because of the increase in dry
exhaust gas loss by the increased excessive air factor and increase in radiation loss. (Fig. 2.4.2)

2.4.2.3 Steam Turbine
Turbine performance (turbine room performance, turbine plant performance) is expressed with the use of the
terms, heat rate, thermal efficiency, internal efficiency, etc.
(1) Heat rate, thermal efficiency, steam consumption ratio
Turbine heat rate is the quantity of heat required to produce 1 kWh of electricity and is expressed by the
following equations.
1. In the case of non-reheat turbines
Q G i −G i −G i
s s w w e e
H
R
= = ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(1)
L L
s s
2. In the case of reheat turbines (Fig. 2.4.2.3-1)
H
R
= Q = G s i s −G w i w +G r (i r −i r ')−G e i e ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(2)
L L
s s
Boiler
LP turbine Turbine HP turbine
Boiler auxiliary
steam etc.
Condens
er
#1 Heater 2 Heater #3 Heater Deaerator #5 Heater #6 Heater
Condenser pump
Low pressure pump Feed water pump
Fig. 2 .4.2.3-1 Turbine reheat cycle
Where:
H : Turbine heat rate (kJ/kWh)
R
Q : Quantity of heat consumed by the turbine (kJ/h)
L : Generator end electric output (kW)
g
G : Turbine inflow steam quantity (kg/h)
S
i : Turbine inflow steam enthalpy (kJ/kg)
S
G : Feed water quantity to boiler (kg/h)
W
i : Feed water enthalpy to boiler (kJ/kg)
w
G : Quantity of steam to outside of turbine plant such as boiler auxiliary steam (kg/h)
o
i : Steam enthalpy to outside of turbine plant such as boiler auxiliary steam
o
G : Quantity of reheated steam
r
i : Medium pressure turbine flow in steam enthalpy (kJ/kg)
r
i’ : High pressure turbine outlet steam enthalpy (kJ/kg)
r
The definition of turbine heat rate may be expressed in two ways, either gross or net, depending on whether
feed water pump drive motive power is considered or not.
44

a. In the case of feed water pump electric drive
Q
Gross Heat Rate= ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(3)
L
s
Q
Net Heat Rate= ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(4)
L L
s− BFP
b. In the case of water feed pump turbine drive
Q
Gross Heat Rate= ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(5)
L L
s+ BFP
Q
Net Heat Rate= ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(6)
L
s
Where L : Motive power required for feed water pump
BFP
Turbine thermal efficiency η is expressed by the following equation.
t
3,600
η
t
= ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(7)
H
R
According to Fig. 1, this is
(E)
η
t
= ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(8)
(B)−(C)
Moreover, the following definitions are used to express efficiency of the generation plant.
(E)
Gross plant thermal efficiency= ×100%⋅⋅⋅⋅⋅(9)
(A)
(F)
Net plant heat efficiency= ×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(10)
(A)
The two factors which affect turbine heat rate and thermal efficiency are steam conditions of boiler steam
production, condenser vacuum degree, feed water temperature and feed water heating steps, etc. namely the heat
cycle conditions are the performance of the turbine itself. Fig.2.4.2.3-2 shows the trends of unit capacity and
thermal efficiency of commercial use reheating turbines.
Vacuum degree 5.1 kPaa (722 mmHg)
45
)%(
ycneiciffe
lamreht
enibruT
31 MPa class
24 MPa class
16.6 MPa
class
12.5 MPa class
10 MPa class
Output (MW)
Fig. 2.4.2.3-2 Unit capacity and turbine thermal efficiency

(2) Turbine internal efficiency, turbine efficiency
To express the performance of the turbine itself, turbine internal efficiency and turbine efficiency are used.
Internal efficiency ηi is expressed by the ratio between steam adiabatic heat drop Ho (Theoretical work load of
zero loss steam) and heat drop Hg effectively used.
ηi = H
g
/H
o
×100%⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(11)
Figure 2.4.2.3-35 shows the steam condition (Pressure, enthalpy functions) in the case of the reheating turbine
and the internal efficiency of the high pressure turbine, medium pressure turbine and low pressure turbine are
expressed by the following quotation.
Pressure:
P: Turbine main steam check valve inlet
x
P 0 : 1st step nozzle inlet Saturation line
P: High pressure turbine outlet
1
P: Before medium pressure turbine reheat
r
stop valve
P: Medium pressure 1st step inlet
2
P: Medium pressure turbine outlet
3
P: Low pressure turbine inlet
4
P: Low pressure exhaust (Condenser inlet)
5
∆EL : Exhaust loss
Fig.2.4.2.3-3 5 Reheating turbine steam expanded diagram (i-s diagram)
High pressure turbine
H i −i'
η = eH = s r ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(12)
IH
H i −i
oH s 1
Medium pressure turbine
H i −i
η = el = r 4 ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(13)
It
H i −i
ol r 3
Low pressure turbine
H i −i
η = eL = 4 6 ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(14)
IL
H i −i
oL 4 5
Turbine efficiency is the ratio between theoretical work and effective work, and is the product of internal
efficiency and mechanical efficiency. The relation between the turbine efficiency ηr of a back pressure turbine or
a simple condenser turbine and the steam specific consumption S (Kg/kWh) is as follows:
R
G 3,600
S
S
R
= = ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(15)
P Hηη
S e t s
Where:
G : Inflow steam quantity (Kg/h)
S
P : Generator output (KW)
g
H : Adiabatic heat drop inside turbine (KJ/kg)
o
η : Generator efficiency
g
46

(3) Heat balance (Heat balance diagram) Steam expanded diagram
Figure 5 is an example of a reheating turbine heat expanded diagram. The pressure, temperature, enthalpy or
quantity of steam of each part of the turbine, based on the expanded diagram shown in the diagram are called the
heat balance diagram. Figure 2.4.2.3-4 shows a 1,000,000 kW heat balance diagram. The manner of steam
expansion, the condition of steam at each part, turbine extraction, etc, are normally obtained by performance
calculation by turbine makers. The heat balance around the feed water heater periphery is calculated by the
following procedures.
High
p tu r r e b s in su e r e M pr e e d s i s u u m re turbine Lo tu w r b p in re e s ( s A u ) re
Fig. 2.4.2.3-4 Example of 1,000 MW supercritical pressure turbine heat balance
(1) Piping pressure drop from the turbine extraction point to the feed water heater is normally maintained at
around 5% of the pressure (2.5 - 12%).
(2) Temperature inside the feed water heater becomes the saturation temperature of the extraction pressure.
(3) The feed water heater outlet feed water temperature is selected to be 2.5 to 5°C lower than the saturation
temperature inside the heater and feed water heater to be designed. (In the case of a direct contact type such
as a deaerator, the outlet feed water temperature is to be the same as the saturation temperature and also in
the case where the extraction temperature is fairly higher than the saturation temperature in reheating steam
turbines, etc., this temperature may be utilized with a superheat reducing section provided inside the feed
water heater with the feed water selected to be 0 - 3°C higher than the saturation temperature. (Refer to
Chapter 2, Clause 3.4)
(4) When a drain cooler is provided in the water feed heater, the drain outlet temperature is designed to be 5 to
10°C higher than the water feed temperature.
(5) Taking the No. 5 heater in Fig. 2 as an example, the extraction amount necessary for the water feed heater
is obtained by the following procedure. (However, the heat discharge loss is to be neglected.)
G (i -i ) = G (i -i )-G (i -i )
x x 14 w 12 11 d 13 14
Where:
G : Extraction quantity (Heated steam quantity)
x
i : Extraction enthalpy
x
G : Feed water quantity
w
i : Feed water heater inlet feed water enthalpy
11
i : Feed water heater outlet feed water enthalpy
12
G : Inflow drain quantity
d
i : Inflow drain enthalpy
13
i : Outflow drain enthalpy
14
47
relioB Low pressure turbine (B)
Condenser
Make up water
Condenser
BFP turbine pump
Grand steam
condenser
Condensate
booster pump
Boiler feed water pump Feed water booster pump Drain pump

2.4.2.4 generator
(1) Available output curve
Figure 2.4.2.4-1 shows an example of available generation output curve. This curve is divided into parts (A),
(B), and (C).
48
esahp
gniggaL
esahp
gnidaeL
Fig. 2.4.2.4-1 Available output curve
(A) Range restricted by rotor coil temperature
(B) Range restricted by stator temperature
(C) Range restricted by stator core end part temperature
1) Range restricted by rotor coil temperature
The restrictions by rotor coil temperature may be obtained under the conditions of a constant field current.
Namely, this may be obtained by the V curves shown in Fig. 2.4.2.4-2 36, whereas a line parallel to the axis of the
ordinate is drawn through field current 1f at the rated load and rated power factor, and the intersecting point of the
line with the respective V curve power factor is plotted on the MW-MVAR coordinate to obtain the restriction by
rotor coil density.
Terminal
voltage=Rated Voltage
)AVM(
tuptuO
Field current (A)
Fig. 2.4.2.4-2 V curve
2) Range restricted by stator coil temperature
Restriction by the stator coil temperature may be obtained from constant conditions of the stator current. It
becomes a circle which passes through rated point P with the origin point as the center of the circle.

3) Range restricted by the stator core end part temperature
The cause for increasing of temperature of the stator core end part in the leading phase range is that the
composite magnetic flux from the magnetic flux by stator coil end magnetomotive force and the magnetic flux by
rotor coil end magnetomotive force increase with a lower excitation (leading power factor) and the eddy current of
the core end part becomes greater. This upper limit is higher with machines with a larger short circuit ratio but
with recent large capacity machines with large electrical charge, the end part temperature increase tends to become
large and therefore overheating is prevented by core end magnetic shield, core end slit, core end stage,
non-magnetic finger plate, non-magnetic rotor coil retaining ring, etc.
(2) Resistance capacity to short period overload
Loads exceeding the available output curve even though for short periods will result in a rapid increase of
temperature and therefore repeated overload operation is not desirable because the service life of the generator
coil will be shortened, but there is a permissible range in which the insulation is not greatly affected. Table
2.4.2.4-12 shows the overload permissible limit specified by ANSI C50-13.
Table 2.4.2.4-1 Short period overload resistant amounts
Time (seconds) 10 30 60 120
Armature current (%) 226 154 130 116
Field voltage (%) 208 146 125 112
(3) Continuous unbalanced load resistance
When a generator is operated under unbalance load or by single phase load, a negative phase current flows in
the stator coil and as a result, the revolving field which revolves in the opposite direction at the same speed turns
off the rotor and an eddy current of double frequency flows on the surface of the rotor and the rotor wedge and the
rotor overheats. Especially in the part in which the eddy current concentrates, if the unbalance becomes serious,
burning may result by local overheating.
The permissible limit of continuous unbalanced load is greatly affected by the material and structure of the
equipment and cannot be specified in one manner. Table 2.4.2.4-2 shows the permissible limit proposed
recently by ANSI where limitations are made more severe with large capacity machines.
Table 2.4.2.4-2 Unbalanced load resistance
Continuous unbalanced Short period unbalanced load
load I t*
2
I (%)
2
Indirect cooling loss 10 30
Direct cooling loss 8 10
- 800 MVA
801 – 960 MVA I t
2
951 – 1,200 MVA 6 = 10 – 0.00625 (MVA – 800)
1,201 – 1,500 MVA 5
*I (P.U.) t (Seconds)
2
(4) Short period unbalanced load resistance
At the time of short period unbalance load such as by one-line ground and line short circuit, the double
frequency eddy current flows on the rotor surface and the rotor overheats for the same reason mentioned in clause
6.3. The most severe failure by rotor overheating is line short circuiting.
Where the negative phase current is /2, a failure continuation time of 1 second, the temperature rise of the rotor
is proportional to t 2 tdt but with consideration of equivalent negative phase current/ which gives the same
∫ / 2SQ
o 2
temperature rise in t seconds, adopting of /22sqt as the scale is widely accepted.
With large capacity machines, the rotor is of light weight compared with the capacity, and therefore the
reduction of relative thermal capacity was considered and i22t<30 for indirect cooling machines and i22t/≤10 was
generally adopted but with the recent super large capacity generators, the limitations shown in Table 3 have been
proposed to ANSI.
(5) Efficiency
Generator loss consists of core loss, mechanical loss, stator I2R loss, stray load loss, and world magnetic I2R
loss.
49

1. Core loss
If the used material is assumed to be the same, core loss relates to magnetic flux density, frequency, and stator
core weight, and with their increase, core loss increases.
2. Mechanical loss
Mechanical loss consists of bearing friction loss and windage loss. Since windage loss is proportional to gas
density, the windage loss of hydrogen cooling machines is extremely smaller than that of air cooling machines.
This is one of the advantages of the hydrogen cooling machine. Bearing friction loss increases in an exponential
function manner with increases in revolutions and journal diameter.
3. Stator I2R loss and stray load loss
Stator I2R loss is proportional to the square of the stator current and stator coil average length/coil cross
sectional area. In addition, surface loss is affected by void length and winding pitch, becoming smallest with a
5/6 winding pitch and loss decreases as void length increases.
4. Field I2R R Loss
Field I2R Loss is proportional to the square of the field current and field resistance but as shown in the V curve
of Fig. 36, more field current becomes necessary with the same output as the power factor becomes lower and loss
increases.
Figure 2.4.2.4-3 shows the generator efficiency and changes in efficiency by partial load of a typical capacity
generator. As shown in this figure, in general, in the case of standard specification generators, efficiency tends to
become better with larger capacity. Also, in regard to partial load, core loss and mechanical loss are constant and
therefore efficiency rapidly worsens with low load but in the case of hydrogen cooling machines, lowering of gas
pressure inside the machine and operating at low load is possible and as a result, windage loss decreases and
normally, the maximum efficiency rate is displayed at 70 - 80% load.
50
)%(
ycneiciffe
rotareneG
Load (%)
Fig. 2.4.2.4-3Generator efficiency curve
2.4.2.5 Condenser facilities
Vacuum degree control of condenser facilities, causes of vacuum degree lowering and their judgment, as well as
restoring means and the appropriate number of circulating pumps to be operated are decided.
(1) Desired value of vacuum degree
In regard to the daily desired vacuum degree of condensers, a control value is set against the design value when
the respective units are installed.
Figure 2.4.2.4-4 shows the philosophy on desired values. The control width of the vacuum degree is set with
consideration of accuracy of instrumentation, cleanliness of tubing, and dispersion of the performance record.
With an increase in the vacuum degree when the cooling water temperature is low, turbine specific heat changes

from decreasing to increasing and since there is a risk of problem occurrence in the facilities, the vacuum degree
is controlled so that it does not exceed the efficiency limit vacuum degree.
(2) Facility control
By the frequency of operation and data measurements of the respective facilities, difference control of the
desired value of the vacuum degree is being conducted.
The following shows the general control items.
(cid:120) Operation control of the ball cleaning device
(cid:120) Control of electrolytic protection device
(cid:120) Measuring of vacuum pump extraction quantity
(cid:120) Control of instrumentations
(cid:120) Tubing brushing cleaning
(cid:120) Cleaning of the inlet channel and circulating pump chamber
(3) Disposition to adopt when deviation is seen from the desired value of the vacuum degree
First, check to see if there is any abnormal condition of instrumentation and when confirming, pay attention to
the following points.
(cid:120) Drain accumulation in the detection piping
(cid:120) Temperature compensation if the standard temperature differs between the mercury vacuum gauge and
the atmospheric pressure gauge.
(cid:120) Difference between the atmospheric pressure compensated vacuum degree and the transmitter side.
(cid:120) Whether there is any abnormal condition in the correlation between the atmospheric compensation value
of the mercury vacuum degree gauge and the respective temperatures of the exhaust room and hotwell.
(cid:120) Any abnormal condition of the mercury vacuum degree and atmospheric temperature gauge at the time
of periodic checking.
51
muucaV
eerged
Upper limit of
vacuum degree
Efficiency limit vacuum
degree Vacuum degree
desired value
Lower limit of
vacuum degree
Turbine specific heat consumption Sea water temperature (°C)
correction coefficient (%)
Area A--- Desired value (Design value ± α)
Area B --- Area in which checking of the vacuum degree related instruments
should be checked.
Area C--- Area in which cause should be investigated and measures
conducted.
Fig. 2.4.2.4-4 Philosophy on desired value of vacuum degree.
(4) Investigation method of cause for deviation of vacuum degree from the desired value
When a deviation seen from the vacuum desired value is found with measuring instruments in a normal state, in
general, investigate the following.
1.Increase in leak in quantity of air
The lowering of the vacuum degree occurs when leak in exceeds the extraction capacity of the vacuum pump.
2.Lowering of cleanliness of tubing
With no increase in the leak in air amount and with the vacuum pump found to be normal, the cause of lowering
of the vacuum degree is often caused by the lowering of cleanliness of the tubing.
3.Lowering of the cooling water volume
When the cooling water volume drops, an increase of difference in the cooling water inlet, outlet temperature
((cid:85)T), increase of CWP discharge pressure, and lowering of the condenser water chamber level occurs, and an
abnormality of the condenser side (tubing clogging, siphon cut-off, etc.), abnormality of the CWP side ‘CWP

performance lowering, CWP chamber water level lowering, check washing valve seat leak, etc. are conceivable.
4.Abnormality of the vacuum pump
When an abnormality of the vacuum pump is seen, conduct changeover testing with a spare machine and
compare the respective air extraction amount and vacuum degree.
Also, since the seal water relations of the vacuum pump greatly affect the vacuum degree, pay attention to the
following points.
a. Increase in seal water temperature by contamination of the seal water cooler, increase of bearing
cooling water temperature.
b. Shortage of seal water by abnormality of the seal water pump, clogging of the discharge strainer of
the pump, etc.
c. Lowering of water level by malfunctioning of float valve for seal water tank water level adjustment
5.Increase of condenser heat load
The desired value of the vacuum degree is calculated from the design heat load, cooling water amount, and
heating surface, etc. and if the heat load increases above the design value, even if the cooling water volume and
others are in accordance with designed values, the vacuum degree decreases. Especially, with the once-through
boiler unit, leakage of the respective bypass valves from the start-up bypass system to the condenser causes
lowering of thermal efficiency and care should be exercised.
(5) Performance curve
The vacuum degree of the condenser is affected by the condenser load, cooling water inlet temperature, and
cooling water volume. Condenser pressure is obtained from saturation steam temperature t.
s
Q t −t
t =t + =t1+ 2 1 (1)
s 1 1 1
G ×c ×γ×(1− ) 1−
c p ep ep
Where
A×K
p = (2)
G ×c ×γ
c p
Figure shows an example of the condenser performance curve. The condenser pressure change at the time of
changes in condenser heat load and cooling water inlet temperature when the cooling water volume is constant is
shown. When the condenser pressure is recorded by the elapse of time in this curve, the contamination coefficient,
etc. of the cooling pipe may be assumed. This curve is a straight line at the time of no load to a certain load. When
the condenser load is small or the inner pressure is low, the condenser pressure is restricted by the performance of
the air extraction device and there are cases where the pressure to be obtained by equation (1) cannot be obtained.
52

Fig. 2.4.2.4-5 Assumed performance curve of the condenser
2.4.2.6 High pressure water feed heater
In a condition with a constant rated output, to measure the water feed outlet terminal temperature difference
(T.D.) as well as the drain outlet temperature difference (D.C.), the following data items are collected, evaluated
and countermeasures executed.
(cid:120) Water feed temperature (inlet, outlet) of the respective high pressure water feed heater
(cid:120) Extraction temperature, pressure of the respective high pressure water feed heater
(cid:120) Drain outlet temperature of the respective high pressure water feed heater
(cid:120) Inner pressure of the respective high pressure water feed heater
(cid:120) Drain flow rate of the respective high pressure water feed heater
(cid:120) Drain level of the respective high pressure water feed heater
(cid:120) Drain water level adjusting valve opening of the respective high pressure water feed heater
(cid:120) Water feed pressure loss
The water feed outlet terminal temperature difference (T.D.) and the outlet temperature difference (D.C.) are
obtained from the following equations
T. D=T -T (OUT)
S W
D.C= T -T (IN)
d W
Where
T.D. : Water feed outlet terminal temperature difference (°C)
D.C. : Drain outlet temperature difference (°C)
T : Saturation temperature (°C) to water feed heater inlet steam pressure
S
T (OUT) : Water feed outlet temperature (°C)
W
Td : Drain outlet temperature (°C)
T (IN) : Water feed outlet temperature (°C)
W
(1) The effect by the water feed heater performance on the turbine cycle
a. The number of water feed heater units and temperature increase
Although decided with consideration of the heater output and economy, in general, from an economical aspect,
6 to 8 heaters are installed for 200 MW and over. There is a close connection between the number of water feed
heaters and temperature increase and in regard to water feed temperature rise per unit of water feed heater, it is
53

desirable to raise the temperature evenly with heaters of less than the reheating point in the one step reheating
cycle. From the aspect of performance, it is optimal to plan to increase the average temperature rise at the low
pressure feed water heater rather than to increase the temperature of the feed water reheater by extraction from the
reheating pump.
This temperature rise is restricted by the thermal stress, etc. of the water chamber and normally, the increase is
suppressed to around 20 to 75°C.
(2) Effect by terminal temperature difference (T.D.) change
To obtain the effect on turbine heat rate by T.D. changes, the extraction quantity changes to the respective water
heat heater T.D. change are calculated, and with the turbine inlet steam quantity kept constant, the heat rate may
be obtained from the extraction quantity change and output quantity change. The following shows an example of
calculation in regard to a high pressure feed water heater.
a. Trial calculation data
Subject unit 600MW
At rated output, when T.D. is +3°C
b. Trial calculation results
(cid:120) Decrease of extraction quantity by T.D. increase
EXT
(cid:120) Turbine room input heat increase by reheated steam quantity increase by extraction quantity decrease by
T.D increase
(cid:120) Exhaust quantity increase by extraction quantity decrease by T.D. increase
(cid:120) Increase of exhaust loss heat quantity by exhaust quantity increase
(cid:120) Output heat decrease from the turbine room by feed water temperature decreasing
(cid:120) Increase of turbine room consumption (cid:85)Q
54

Condenser
G : Flow rate kg/h
T : Temperature °C
I : Enthalpy kcal/kg
CRH, HRH : Low, high temperature
reheated steam
EXT : Extraction
EXH : Exhaust
FW : Water feed
I, O : Inlet, outlet
COND : Condensed water
(cid:120) Output change
(increase)
(cid:120) Turbine room thermal efficiency HRʼ after T.D. increase
Reference heat
consumption
Reference output
Reference specific heat Reference
consumption (HR) output
Reference output
(cid:120) Heat rate change ratio
(cid:120) Gross thermal efficiency change quantity
2.4.2.7 Boiler exhaust gas control
Together with the reduction of boiler exhaust gas loss and saving of fuel expenses, to reduce the running costs
of boiler operation and maintenance expenses, and repair expenses, and attempt to improve overall efficiency,
control values are set on the AH low temperature part average temperature, exhaust gas temperature control
exhaust gas O value, and AH air leakage ratio and control are executed.
2
(1) AH low temperature average temperature control
In accordance with the sulfuric contents in the used fuel, the optimum value is set for each boiler with sulfuric
55

acid dew point measurement etc. as a reference and upon confirming the corrosion situation of the AH element,
etc. staged lowering is attempted. It is desirable to set the average temperature control value at the maximum
point of sulfuric acid condensation quantity in accordance with the sulfur contents of the used fuel but reduction
should not be made in one stroke but in stages with consideration of the following points and confirming that
there are no problems.
(cid:120) Deviation of the theoretical value and actual record value of the sulfuric acid dew point
(cid:120) The relation between the sulfur contents in the fuel and produced SO3 density.
(cid:120) Local metal temperature drop by unbalance of gas temperature distribution
(2) Exhaust gas temperature control
The AH outlet exhaust gas temperature differs greatly by boiler according to the boiler and AH structure, and
the kind of fuel and since it fluctuates greatly by factors such as load and atmospheric temperature and air leakage
of AH, it is difficult to set a standard but it is set upon executing of countermeasures on temperature decrease of
exhaust gas by each boiler, conducting an actual machine test with the AH element in the best condition, with the
air leakage in the minimum condition and based on these results, with exhaust gas control data as a reference and
with the atmospheric pressure as the parameter. The deviating trend to the control value is grasped and when the
deviation is large and continuous, the following deviation factors are analyzed and appropriate measures are to be
taken.
(cid:120) Lowering of exhaust gas temperature by increase in AH air leakage amount
(cid:120) Aging deterioration by corrosion, wear of AH, and rising of exhaust gas temperature by lowering of AH
performance by staining of the heating surface, etc.
(cid:120) Increase of exhaust gas temperature incident to dry gas quantity increase by Combustion gas O (Excess
2
air factor)
(cid:120) Those by characteristic changes of the fuel.
(3) Control of exhaust gas O
2
The Eco outlet combustion gas O differs by each boiler, depending on the boiler, combustion method, and type
2
of fuel. Therefore, a combustion test is to be made after improvement of combustion facility or after periodic
inspection as required, O distribution is to be measured, abnormality of instruments, inappropriateness of
2
detection point, faulty combustion, etc., deviation factors from control values are to be analyzed, and if a large
deviation situation continues, the O meter, burner tip, and body, and damper are to be checked for combustion air
2
or exhaust gas O distribution is to be measured and suitable measures taken.
2
(4) AH air leakage ratio
The temperature of the gas which passes the boiler will differ depending on the boiler condition (cold boiler hot
boiler, etc.) which in turn effects changes in the amount of heat deformation. Therefore, to prevent leakage of
AH air, the setting of respective seals is calculated in advance and the gap value is set in a cold boiler condition so
that the clearance becomes minimum in rated load operation but a certain amount of leakage is unavoidable.
However, with the new type AH, with the improvement of the seal plate supporting method and additions to the
seal section, direct leakage from the seal gap has been improved compared with the old type. Furthermore, to
reduce leakage from the high temperature side radial seal which was the greatest leakage factor during operation,
a sensor drive system of the high temperature side sector plate has been developed. With this system, the rotor
shaft side that controls the gap between the sector plate and seal to a minimum under any boiler operation
condition is structured so that it constantly follows the contraction-expansion of the rotor, and control is conducted
so that only the gap of the rotor periphery and sector plate outer end section gap becomes minimum.
56

2.5 Example of Operation Control and Performance Management (Hokkaido Electric Power Co., Inc)
2.5.1 Overview of Hokkaido Electric Power Co., Inc.
Hokkaido Electric Power Co. Inc. was established in May 1951 to supply electricity in the Hokkaido region.
With an area of about 83,500km2 and a population of 5.7 million, Hokkaido is flourishing in agriculture, fishery and
tourism. The capital city, Sapporo, with a population of 1.7 million, located at 45 degrees at north latitude, once hosted
the winter Olympics in 1972, and has held “Sapporo Snow Festival” every February visited by numerous visitors
including those from foreign countries.
Hokkaido Electric Power Co., Inc., established on May 1, 1951, has the headquarters in Sapporo and has been
engaged in electric power generation, transmission and distribution by about 5,800 employees. Table 2.5.1-1shows the
electric energy sale, the supply facilities and transmission and distribution facilities.
Electric energy demand Total 30,833 GWh
Year 2005 Electric light 11,540 GWh
Electric power 2,218 GWh
Specific scale 17,075 GWh
Supply facilities Total 66 places 6,505 MW
Hydro-electric power station 53 places 1,231 MW
Thermal power station 12 places 4,115 MW
Nuclear power station 1 place 1,158 MW
Transmission and distribution facilities Transmission distance 8,230 km
Transforming station 369 places 19,300 MVA
Distribution line distance 66,753 km
Table 2.5.1-1
The company has 12 thermal power stations. The breakdown is shown in Table 2.5.2.
Steam power station 6 places 3,900 MW
Gas turbine power station 1 places 148 MW
Internal combustion power station 4 places 17.4 MW
Geothermal power station 1 places 50 MW
Table 2.5.1-2
Fig. 2.5.1 Thermal Power Stations of Hokkaido Electric Power Co. Inc.
Okhotsk Sea
Japan Sea Sunagawa
power station
Naie power station
Onbetsu power station
Date power station Sapporo
Tomatouatsuma power station
Tomakomai power station
Mori power station
Pacific Ocean
Shiriuti power station
57

2.5.2Overview of Coal Thermal Power Station
The steam power stations are six places include seven units of coal thermal power stations in three places. The outline of the facilities of these seven units is shown in Table 2.5.3.
Start of Authorized Boiler Turbine Unit
Main steam Reheat steam Boiler type
operation output efficiency efficiency efficiency
Name Fuel
Pressure Temperature Temperature
Date MW
(MPa) (℃) (℃)
No.1 unit Oct., 1980 350 16.6 566 538 Natural circulation 87.28 45.03 39.41
No.2 unit Oct., 1985 600 Foreign 24.1 538 566 Supercritical once-through 87.91 47.70 41.93
Tomatouatsuma
coal Ultra supercritical
No.4 unit Jun., 2002 700 25.0 600 600 88.73 49.83 44.21
once-through
No.1 unit May, 1968 175 16.6 566 538 Natural circulation 87.08 45.14 39.26
Naie
No.2 unit Feb., 1970 175 Domestic 16.6 566 538 Natural circulation 87.08 45.55 39.40
No.3 unit Jun., 1977 125 coal 12.5 538 538 Natural circulation 85.72 43.63 37.41
Sunagawa
No.4 unit May, 1982 125 17.7 538 538 Subcritical once-through 86.27 45.40 39.16
Table 2.5.2
2.5.3Practice in Tomatouatuma Power Station
2.5.3.1 Organization and Service
This power station is operated by 102 personnel in three divisions. The operation of environmental facilities has been outsourced to the affiliated companies. Fig. 2.5.3-1 shows the
organization and service.
58

Power Station Organization and Operation /Management System
Fig.2.5.3-1 Operation /Management of Power Stations
Power Station Organization
For operation of power stations, the following shall be conducted under the supervision based on the
regulations and policies stipulated by the head office (Thermal Power Dept.)
Station manager
1. Oversight, communication, PR related power station management
Deputy manager 2. Operation/ management of generation facilities (except Environment Engineering related)
Business staff
3. Management of fuel
4. Compilation, analysis, management of operation history data
5. Investigation, test planning and execution for operation/performance of facilities
Generation Div. Management staff 6. Press release and public hearing
7. General affairs, emergency/disaster office, PR, document control, administration
8. Personnel affairs, education, labor, welfare, safety and health
Operation staff 9. Accounts, land management
10. Other items not supervised by other divisions
1. Supervision, communication, PR, investigation planning/execution of environmental conservation
Environment matters
Engineering Staff 2. Operation/management of smoke, feed/waste water, ash handling facilities, environment
Environment
Engineering Div. monitoring facilities.
3. Investigation, test planning and execution for operation/performance of facilities
Environment
4. Treatment/management, utilization planning/execution of waste after generation
FacilityStaff
5. Analysis management, chemical investigation of fuel, boiler water, etc
6. Accident prevention/safety for hazardous materials
Machinery staff
Planning and management of maintenance, repair of facilities and daily maintenance as well as
Maintenance
repair and maintenance works
Div.
Electrical
Measurementstaff
Main generation related operations outsourced to other companies
・Cleaning, greening, security, port management
・Coal stock, transportation, ash handling work
・Operation and monitoring of smoke, feed/waste water facilities
・Chemical analysis work
・Daily maintenance / inspection work
59

2.5.3.2 Operation System
The power station consists of two rooms: the central control room where the boiler, turbine and generator are operated,
and the centralized management room where the environmental facilities are operated. The detail is shown in Fig.
2.5.3-2
Generation manager Environment
engineering manager
Administration Central control unit Engineering assistant Facility assistant manager
deputy manager manager
+ + +
Operation
7 personnel 4 personnel 6 personnel
assistant
Control of BTG × 5 groups Operation Operation management of
manager +
generation facilities management of environmental facilities
Operators (8 environmental facilities
people)
Operation of BTG
Centralized management
generation facilities
room (operation is
outsourced to affiliated
companies)
Daytime shift (11
personnel)
+
Team
× 4 groups
leader + 8
operators
Operation of
environmental facilities
Fig. 2.5.3-2
2.5.4. Management for Operating Power Station
Various kinds of managements have been carried out in accordance with the standards set forth in “Steam Power
Generation Facilities Maintenance and Service Manual”.
2.5.4.1 Operation Management
The “Steam Power Generation Facilities Maintenance and Service Manual” stipulates the operation management
standard (Table 2.5.4-1), setting standard for control and permissible values for trial operation (Table 2.5.4-2), etc.
In addition to usual monitoring by operators, the plant operation conditions are input into computers (see Fig. 2.5.4-3:
System Configuration) for proper control.
〇 Examples of management documents
- Daily report (Table 2.5.4-4):One hour value (24 points), maximum-, minimum-, average values, and
one-day energy amount for the management items
- Monthly report (Table 2.5.4-5):Boiler and turbine maintenance logs, month-end generation records, etc.
60

Table 2.5.4-1 Operational Management Standard
Measure location Record frequency
Control values
Measure
Operation management items Unit under normal Indicator 1/ 1/ 1/ As Remarks
values Recorder
operation day month year needed
office Site
Daily and Paralle – parallel off (Start sending air – stop for
Operation time Hrs/min. monthly (cid:123) (cid:123) house boiler)
totals
Daily and Rated output ×
Generated energy MWh monthly 24 hours (cid:123) (cid:123) (cid:123) (cid:123)
totals
Generator output MW Max value Rated output (cid:123) (cid:123) (cid:123) Maximum value within 1 hour
Main stop valve steam Max value Rated value × Sum up monthly the operation time 5% over rated
MPa (cid:123) (cid:123) (cid:123)
pressure 1.05 pressure
Main stop valve steam Max value Rated value + Sum up monthly the operation time at 8°C, 14°C,
°C (cid:123) (cid:123) (cid:123)
temperature 8°C 28°C over rated temperature.
Reheat stop valve steam Max value Rated value ×
MPa (cid:123) (cid:123) (cid:123)
pressure 1.05
Reheat stop valve steam Max value Rated value + Sum up monthly the operation time at 8°C, 14°C,
°C (cid:123) (cid:123) (cid:123)
temperature 8°C 28°C over rated temperature.
Max value Smaller one of
Main steam flow rate t/h the MCR or (cid:123) (cid:123) (cid:123)
turbine intake
Condenser vacuum mmHg Min value Min operation (cid:123) (cid:123) (cid:123) (cid:123) Atmospheric pressure corrected value
Coal (humidity) t
Crude oil kl
Heavy oil kl
Orimulsion t leuF
noitpmusnoC
Monthly
total
(cid:123) (cid:123) (cid:123) For generation
Diesel oil kl
Max value JEAC3717 Bearing * Over rated
Turbine vibration amplitude 1/100mm caution value* (cid:123) (cid:123) (cid:123) No. Shaft Under 12.5
Amplitude Bearing Under 6.25
61

Measure location Record frequency
Control values
Measure
Operation management items Unit under normal Indicator 1/ 1/ 1/ As Remarks
values Recoder
operation day month year needed
office Site
pH (25°C) Average Water quality (cid:123) According to “thermal power station water
Boiler
Silica µgSiO/l value standard value (cid:123) management manual”
water 2
Electric
quality µS/cm (cid:123)
conductivity
pH (25°C) (cid:123)
Silica µgSiO/l (cid:123)
Feed water 2
Electric
quality µS/cm (cid:123)
conductivity
Dissolve O µgO/l (cid:123)
2
RBOT minute - Over 70 mins. (cid:123) According to “turbine oil management manual”
All oxidization mgKOH/g Under 0.3 (cid:123)
Lubricate Impurities mg/100ml Under 10 (cid:123)
oil for Kinetic viscosity mm2/s (New oil
(cid:123)
turbine (40°C) standard) ± 10%
Water content mg/l Under 500 (cid:123)
Color phase ASTM Under 4 (cid:123)
Unit Gross % Calculate
(cid:123)
efficiency Net value
Boiler drum water level mm Highest, Warning value
(cid:123) (cid:123)
lowest
Boiler drum pressure MPa Maximum Rated × 1.05 (cid:123) (cid:123) (cid:123)
Superheater spray flow rate t/h Maximum Max operation (cid:123) (cid:123) (cid:123)
Reheater spray flow rate t/h Maximum Max operation (cid:123) (cid:123) (cid:123)
Turbine ejector pressure MPa Maximum Rated × 1.05 (cid:123) (cid:123) (cid:123)
Turbine ejector temperature °C Maximum Rated + 8°C (cid:123) (cid:123) (cid:123)
Bearing inlet oil pressure MPa Minimum Warning value (cid:123) (cid:123) (cid:123)
Bearing outlet oil pressure °C Maximum Warning value (cid:123) (cid:123) (cid:123)
Turbine contro oil pressure MPa Minimum Warning value (cid:123) (cid:123) (cid:123)
62

Measure location Record frequency
Control values
Measure
Operation management items Unit under normal Indicator 1/ 1/ 1/ As Remarks
values Recorder
operation day month year needed
office Site
Control valve opness % Maximum Max operation (cid:123) (cid:123) (cid:123) Also possible with cum angel
mm Maximum Managed by difference expansion warming value
Expansion of turbine shaft (cid:123) (cid:123) (cid:123)
for more than 2 casings
Expansion of turbine shaft mm Maximum (cid:123) (cid:123) (cid:123)
Expansion of turbine shaft, mm Maximum Warning value
(cid:123) (cid:123) More than 2 casings
casing
Turbine speed rpm Maximum Rated × 1.05 (cid:123) (cid:123) (cid:123)
63

Table 2.5.4-2
Setting Standard for Control and Permissible Values for Trial Operation
(Boiler)
Control value standard setting Permissible value standard
Items Unit Remarks
for trail operation setting for trail operation
Generator load MW Rated output Rated output ↓
(referred to as “rated” (referred to as “rated”
hereafter) hereafter)
Economizer inlet feed water MPa Design pressure for rated Design pressure for rated × ↓ (cid:13)
1.05
Superheater inlet or main steam Steam pressure for rated Steam pressure for rated × ↓ (cid:13)
1.05
64
erusserP
Reheater outlet steam Design steam pressure for Design steam pressure for ↓
rated rated × 1.05
Economizer inlet feed water °C Design temperature for rated MCR or max operation value ↓ (cid:13)
Superheater inlet or main steam Design temperature for rated Design temp for rated + 8°C <
erutarepmeT
Reheater outlet steam Design temperature for rated Design temp for rated + 8°C <
Main steam t/h Design flow rate for rated MCR or turbine intake amount ↓ (cid:13)
Feed water Design flow rate for rated MCR ↓
Superheater spray Design flow rate for rated MCR or max operation value ↓ (cid:13)
etar
wolF
Reheater spray Design flow rate for rated MCR or max operation value ↓ (cid:13)
Drum water level mm Design water level for rated Warning value ↓ ↑ (cid:13)
Economizer gas oxygen % Object value for rated Warming value (low) ↑
concentration
Furnace kPa Design value for rated Warning value ↓ ↑
Forced fan outlet pressure Design value for rated Fan rated value ↓ (cid:13)
Pulverizer inner pressure (For vertical Design value for rated Minimum flow speed (For ↑ (cid:13)
mill, pressure difference of primary vertical mill, mill pressure
fan) difference corresponding to
min. flow speed)
Pulverizer coal surface Design value for rated Tube mill: Warning value ↑ or (cid:13)
↓ ↑
Wind box Design value for rated Equilibrium: lower limit, ↑ (cid:13)
pressureized: MCR
Gas mixing fan Design value for rated MCR ↓ (cid:13)
Gas recirculating fan Design value for rated Fan rated value ↓ (cid:13)
Induced fan inlet pressure Design value for rated Fan rated value ↓ (cid:13)
tfarD
Air preheater gas outlet/inlet Design value for rated MCR or max operation value ↓ (cid:13)
difference
Reheater inlet °C Design value for rated MCR ↓ (cid:13)
(superheater outlet)
Air preheater inlet Design value for rated MCR or max operation value ↓ (cid:13)
C°
sag
noitsubmoC
Air preheater outlet Design value for rated MCR or max operation value ↓ (cid:13)
Air preheater outlet °C Design value for rated MCR or max operation value ↓ (cid:13)
Pulverizer inlet Design value for rated Max operation value ↓ (cid:13)
C°
riA
Pulverizer outlet Design value for rated Warning value ↓ (cid:13)
Auxiliary equipment motor A Rated current of motor Rated current of motor ↓
Auxiliary equipment bearing temperature °C Operation value for rated Warning value or max ↓ (cid:13)
operation value

Inlet feed water temperature °C Design value for pump Highest operation value ↓
Feed water flow rate t/h Design value for pump Pump rated value ↓ (cid:13)
Feed water inlet pressure MPa Design value for pump NPSH or minimum value ↑
(Booster inlet pressure:
NPSH)
65
deef
nevird
enibruT
Feed water outlet pressure MPa Design value for pump Rated value or warning value ↑
(whole pumping process +
pump inlet: MCR)
Control value standard setting Permissible value standard
Items Unit Remarks
for trail operation setting for trail operation
Boiler water circulating pump inlet/outlet MPa Design value for pump Warning value (low) ↑
pressure differential
Rotation speed rpm Design value for rated Design turbine rotation ↓ ↑ (cid:13)
Feed water flow rate t/h Design value for rated Pump rated value ↓
Feed water outlet pressure MPa Design value for rated Warning value or min ↑
operation value
Steam inlet pressure MPa Design value for rated Turbine design pressure × 1.05 ↓ (cid:13)
pmup
deef
nevird
enibruT
Steam inlet temperature °C Design value for rated Turbine design temperature + < (cid:13)
8°C
Coal consumption t/h Design value for rated Rated value for pulverizer ↓ (cid:13)
Burner pressure MPa Design value for rated Warning value ↑ (cid:13)
Temperature °C Design value for rated Warning value ↓ (cid:13)
leuF urc/yvaeH
lio
ed
Flow rate t/h Design value for rated MCR or facility’s max ↓ (cid:13)
capacity
pmup
leuF
Fuel pump outlet pressure MPa Design value for rated Pump rated value ↓ (cid:13)
Explanation of signs in “Remarks” column
↓: To be operated at or under permissible value (For warning value only, under permissible value)
↑: To be operated at or over permissible value (For warning value only, over permissible value)
↓↑: To be operated within the range of permissible value
(cid:13): No description as control value is necessary required
<: To be operated under the permitted level

(Turbine)
Control value standard setting Permissible value standard
Items Unit Remarks
for trail operation setting for trail operation
Generator load MW Rated output Rated output ↓
(referred to as “rated” (referred to as “rated”
hereafter) hereafter)
Main steam MPa Steam pressure for rated Steam pressure for rated × ↓
1.05
First stage outlet Design steam pressure for Design pressure for rated × ↓ (cid:13)
rated 1.05
High-pressure turbine outlet Design steam pressure for Design pressure for rated × ↓ (cid:13)
rated 1.05
66
erusserP
Reheater outlet steam Design steam pressure for Design pressure for rated × ↓
rated 1.05
Main steam °C Steam temperature for rated Steam temperature for rated + <
8°C
High-pressure turbine Design steam temperature for Design steam temperature for < (cid:13)
rated rated
Reheat steam Steam temperature for rated Steam temperature for rated + <
8°C
erutarepmeT
Exhaust room Saturation steam temp for Warning value ↓
design vacuum
Control oil MPa Design oil pressure for rated Warning value ↑ (cid:13)
liO
Bearing oil Design oil pressure for rated ↑
Control valve operness (cum angle) % (deg) Design openness for rated Max operation value ↓ (cid:13)
Condenser vacuum kPa Design vacuum Max operation value ↑
Difference expansion mm Design difference expansion Warning value ↓ (cid:13)
for rated
Thrust bearing °C Supply oil temperature Warning value ↓
+ 20°C
lio
nruter
gniraeB
Radial bearing Supply oil temperature Warning value ↓
+ 20°C
Vibration (shaft / bearing) 1/100 At or under warning value Caution value in JEAC3717 ↓
mm
Pressure MPa Design pressure for rated Maximum operation value ↓ (cid:13)
deelb
riA
Temperature °C Design temperature for rated ↓ (cid:13)
Explanation of signs in “Remarks” column
↓: To be operated at or under permissible value (For warning value only, under permissible value)
↑: To be operated at or over permissible value (For warning value only, over permissible value)
↓↑: To be operated within the range of permissible value
(cid:13): No description as control value is necessary required
<: To be operated under the permitted level

Fig 2.5.4-3
Appendix 3- 2
Schematic of Thermal Performance / Heat Management System
Head Office Calculation Center
Power Station
Thermal Power Dept
Input from other depts.
Input for unsystemized power stations
Data link to other depts.
Plant control system Performance management system Heat management system
Performance Performance B usiness transaction
Unit calculator management system management system automation calculators Large computers
Temperature sensor Heat managem ent
Pressure sensor Data statistic data
Lsw, etc
transmission
Unit calculator process functions
(1)Operation history
(2)Operation condition monitor (1)Heat management data check
(3)Plant efficiency analysis (2) Compilation, calculations
(4)Start/stop loss management Performance management Business terminal Business terminal Performance management (3) Report output
(5)Equipment management terminal terminal
(6)Turbine thermal stress calculate
(7)Unit start/stop
Displaycurrent Output various Distribution
Ex. Tomato-Atsuma Unit No.2 output of each monthly reports
(1) Operation history generator
(2)Operation condition search (1) Heat management data check output Subm
a
i
g
t
e
t
n
o
c
g
ie
o
s
v ernment
(3)Plant efficiency analysis
(2) Monthly report output (Specified formats)
Boiler/turbine maintenance diary (4)Start/stop loss management
(5)Auxiliary equipment
preparation
operation time,
start/stop times
67

Table 2.5.4-4
68

69

70

71

72

Monthly Report (Table 2.5.4-5)…..Boiler and Turbine Maintenance Log, Month-end Generation Record, etc
73

April, 2004
Month Eng Generation Record
Items This month After last inspection Cumulative total
Hr – Min (B) 15837 – 35
Generation time 720 – 00 18821 - 02
(T) 15837 - 35
MWh 447,775 (B) 10,853,339 12,348,254
Generated output
(T) 10,853,339
0 (B) 6 34
Startup times times
(T) 6
Fuel Coal (w) t 144,001 3,558,145
Consumption Diesel oil kl 16.3 1,650.4
Gross efficiency % 42.64
Net efficiency % 40.70
This month After last inspection
Items
Main steam Reheat steam Main steam Reheat steam
Time operated with steam pressure hours - (B) 0- 01
0 - 00
5% over rated pressure min (T) 0- 01
Time operated with steam temp hours - (B) 0- 00 (B) 0- 00
0 - 00 0 - 00
8°C over rated temperature min (T) 0- 00 (T) 0- 00
Time operated with steam temp hours - (B) 0- 00 (B) 0- 00
0 - 00 0 - 00
14°C over rated temperature min (T) 0- 00 (T) 0- 00
Time operated with steam temp hours - (B) 0- 00 (B) 0- 00
0 - 00 0 - 00
28°C over rated temperature min (T) 0- 00 (T) 0- 00
Water Quality Management Record
Items
Control value Measured value
CWT
8.5 – 9.0 (cid:21) 8.82
operation
pH (25°C)
AVT
9.3 – 9.5 (cid:21) -
operation
Silica µgSiO/l 20 ↓ 3
2
CWT
0.2 ↓ 0.05
Electric operation
µS/cm
conductivity AVT
0.3 ↓ -
operation
CWT
20 – 200 ↓ 100.0
Dissolved operation
µgO/l
oxygen AVT
7 ↓ -
operation
74

2.5.4.2 Management System by Computer
(1) Functions of unit computer
(cid:120) Input of unit operation conditions, and display and print-out of necessary data
(cid:120) Output of daily reports needed for daily management
(cid:120) Data collection and efficiency calculation needed for performance management
(cid:120) Calculation of turbine thermal stress
(cid:120) Start/stop of the unit
(2) Functions of performance management system
(cid:120) Tabulation of statistical thermal management data and transmission of them to the headquarters
(cid:120) Collection of performance test data and thermal efficiency calculation
(cid:120) Accumulation of major operation condition values of the unit
→ Retrieval of operation condition values and trend monitoring are available
→ Turbine efficiency calculation, condenser cleanliness calculation, management of heat exchanger
operation conditions, management of major equipment operating hours, etc
(cid:120) Management of start/stop loss
(cid:120) Document-output aid in the designated form
(3) Plant management system
(cid:120) Tabulation of operation data from all the power stations
(cid:120) Output of various monthly and yearly reports in and out of the company
(Major report data: generated energy, thermal efficiency, in-station ratio, utilization ratio, fuel
consumption performance, etc)
2.5.4.3 Other Management
(1) Start/stop loss management
The start/stop loss, which does not serve for generation, is properly managed because the fuel, in-house
electricity and supplementary steam amount used for start/stop largely affect the efficiency and costs.
(2) Periodical Equipment Tests
Protection devices and other equipment are periodically tested to check for correct operation.
(cid:120) Turbine-valve stick prevention test
(cid:120) Protection device operation test (oil pump automatic startup and thrust wear test, emergency speed
governor lockout test)
(cid:120) Startup test of emergency power supply device (gas turbine)
(cid:120) Periodical switching to backup machine
2.5.4.4 Daily Inspection of Facilities (patrol)
The patrol of facilities, items and the patrol method are stipulated in Table 2.5.8. Usually, daily and priority patrols are
carried out by the operator once per shift. Also the patrol by managers and the safety-focused patrols are carried out as
needed.
(cid:123) Shift time and patrol time
22:00 8:00 16:00 22:00
Shift 1 Shift 2 Shift 3
Patrol (cid:83) (cid:83) (cid:83)
Specific patrol (cid:85) (cid:85) (cid:85)
75

Daily Inspection Standard
Frequency
Facilities Items Method Remarks
1 / day 3 / day
Drum safety valve, superheater
Boiler Tentacle, visual,
safety valve, reheater safety Leakage (cid:123)
safety valve hearing
valve, etc
Defects in hangers (cid:123) Visual
Main Main steam, reheat steam, feed
Vibration (cid:123) Tentacle, hearing
piping water, condenser pipings, etc
Leakage (cid:123) Visual, hearing
Combustion
(cid:123) Visual
Furnace Inside furnace condition
Situations inside (cid:123) Visual, hearing
Forced draft fan, induceddraft Vibration, unusual Heavy oil pump for power
(cid:123) Tentacle, hearing
Main fan, gas recirculating fan, gas sound stations using such fuel,
rotating mixing fan, boiler water pump, Temperature rise, orimulsion for Shiriuchi PS
Tentacle, smell,
machine feed water pump (MD, TD), oil surface, oil (cid:123) only
visual
(excluding pulverizer, heavy oil pump, leakage
steam orimulsion pump, circulating
Leakage from
turbine) water pump, condenser pump, (cid:123) Visual
gland part
condenser booster pump, etc
Vibration, unusual
(cid:123) Tentacle, hearing
sound from valve
Main stop valve, control valve,
Main Steam leak from
reheat stop valve, intermediate (cid:123) Visual, hearing
valves valve gland
prevention valve
Abnormality in
(cid:123) Tentacle, hearing
working
Vibration unusual
(cid:123) Tentacle, see, hear
sound, temperature
Steam leak from
(cid:123) Visual, hearing
casing
Steam turbine
Oil drain from
(cid:123) Visual
bearing
Loosening of nut,
(cid:123) Visual, tentacle
bolt
Main heat Feed water heater, deaerator, Leakage (cid:123) Visual, hearing
exchanger cooling tower, etc Water level (cid:123) Visual
Usual sound,
Main body, collector ring, Visual, hearing,
Generator vibration, (cid:123)
excitation board, etc tentacle, smell
smell
Auto voltage adjuster, relay Usual sound,
Relays (cid:123) Visual, hearing, smell
board, power board, etc smell
Usual sound,
Breaker C/C, L/C, MCS (cid:123) Visual, hearing, smell
smell
Usual sound,
Hydrogen
Hydrogent cooler, seal oil vibration, Visual, hearing,
seal oil (cid:123)
equipment, etc smell, tentacle, smell
equipment
leaking
Armature Usual sound,
Visual, hearing,
cooling Amature cooling equipment vibration, (cid:123)
tentacle, smell
equipment smell
Usual sound,
Main Main, house, startup, vibration,
(cid:123) Visual, hearing, smell
transformer transformers smell,
leaking
Table 2.5.4-6
76

d. Performance Management
2.5.5 Efficiency management on a daily basis
(1) Maintenance of proper operation by condition monitor, equipment patrol, record meters, diary record.
Observe whether the output, pressure, temperature, flow rate of steam, condenser vacuum, fuel consumption are
properly maintained.
(2) Operation for performance maintenance
・ Condenser vacuum is maintained by reflecting the cleanliness management in the operation of backwashing,
a ball washing equipment.
・ Reduction of exhaust gas loss is improved as heat collection of each section is promoted by operation of
boiler as well as preheater soot blower.
2.5.5.2 Performance test
(1) Objective
Operation data and thermal efficiency is to be obtained after unit is kept constant, eliminating as many external factors
as possible for affecting the efficiency fluctuations so as to compare the against changes and conditions before/after
periodic inspection. (See Appendix 2.5-1Steam Power Station Performance Test Manual)
(2) Frequency
Before periodical inspection 100% load
After periodical inspection 100% load or needed for operation
(3) Management items
1. Thermal efficiency (measured value, corrected value)
・ Gross thermal efficiency
・ Net thermal efficiency
・ Auxiliary power ratio
・ Boiled room efficiency
・ Turbine room efficiency
2. Boiler room heat loss
Heat loss is calculated by adding various losses, such as, dry gas loss, loss caused by water and hydrogen
content in fuel, unburned matter loss, etc
3. Efficiency correction
Test results are kept in a constant condition by adjusting the values such atmospheric temperature, steam
temperature/pressure, condenser vacuum and etc to design values.
4. Preparation of control charts
Test results are displayed in charts and, for significant changes, analysis is done.
(4) Results of performance test
The results and records of the performance test conducted at Tomato-atsuma coal fired power plant are shown in table
2.5.5-1. Additionally an actual example of performance control chart administrated at the same power plant is shown
in table 2.5.2-2.
77

Table 2.5.5-1
78

79

80

81

82

Maintenance Division Environmental Engineering Division Electricity Power Generation Division
Deputy Deputy Manager Deputy Manager Deputy Manager person
Director
Director Manager Steam Steam
Computer
Manager Environmental Environmental Manager
operation management
in (Central control room)
Drum Equipment Facilities Engineering charge A B C D E
(cid:123)Transition in Thermal Efficiency (Generating End) in 2007 [for December]
The thermal efficiency of each unit has no problem within the control range.
No. 1 Unit control chart (3σ method)
Utilization Previous
factor fiscal year Thermal under survey
efficiency (thermal efficiency)
upper limit 38.65
average value 37.88
lower limit 37.10
T va h r e ia rm tio a n l efficiency L c u o o s e e w f ficient of e B M E f e n i f d i d g c d i i n e le n n i c n y g (mo 3 3 3 3 n 8 8 8 8 th . . . . 0 6 1 2 ) 3 1 9 8 ( u a a v p m e p r e o a r u g l n e im t v o it a f l c u h e a ng 0 0 e . . ) 9 9 5 6
Year
No. 2 Unit
Utilization Previous
factor fiscal year
Thermal efficiency
efficiency (month)
B M e id g d in le n ing 4 4 4 1 0 0 . . . 6 6 7 8 3 4 ( u t p h p e e rm r l a im l e it f ficienc 4 y 1 ) .19
End 39.96 average value 40.43
lower limit 39.68
T va h r e ia rm tio a n l efficiency bowl cleansing stop t u c o o s v e e a ff c ic u ie u n m t d o o f wn ( u a a v p m e p r e o a r u g l n e im t v o it a f l c u h e a ng 0 0 e . . ) 9 2 3 8
Year
No. 4 Unit
Utilization Previous
factor fiscal year
(thermal efficiency)
Thermal efficiency upper limit 43.78
average value 42.98
lower limit 42.18
efficiency (month)
43.73 (amount of change)
Variation of thermal efficiency B M E e n id g d d i n le n ing 4 4 4 3 3 3 . . . 6 9 7 0 0 0 u av p e p r e a r g l e im v it a lue 0 0 . . 9 3 8 0
periodical check
Year
Table 2.5.5-2
83

Appendix 2.5-1
Q-1-7
Steam Power Stations Performance Test Manual
April 1, 1995
Revised June 1, 2004 (First revision)
(Jurisdiction) Thermal Power Department
(Contents)
I. General
1. Objective of Performance Test
2. Implementation of Performance Test
II. Methods for Performance Test
1. Operational Condition for Testing
2. Measurement of Test Data
3. Measuring Equipment
4. Measurement Data and Calculation Methods
Ⅲ. Analysis of Test Data
1. Calculation Processing and Control charts
2. Preparation of charts
Attachment
1. Steam Power Generation Steam Schematic
2. Thermal Efficiency Calculation Equations
3. Performance Test Results (Actual)
84

Q-1-7
Steam Power Stations Performance Test Manual
This manual is to introduce standardized procedure for performance test methods for steam power stations based on
"Thermal Power Station Operation and Maintenance Regulations."
I. General
(1) Objective of Performance Test
The objective of performance test is to grasp the performance of each steam power station, to use such information in
daily operation and maintenance and to improve the energy efficiency in heat and electricity generated.
2. Implementation of Performance Test
(1) Responsibility for Implementation
Planning, implementation, consideration for performance test is done by each steam power station.
(2) Time and Number of Tests
a. Test time and number are shown in the table below. As for the load needed for operation, appropriate load
is be set based on the operational condition of each unit.
b. In the event a question arises against test results, re-test shall be conducted.
c. Flexible operation shall be done in case a test cannot be conducted in a certain load condition due to load
dispatching reasons and others, conducting such test on next occasion.
Test load
4/4 load Load needed for operation (minimum)
Test time
Before periodic inspection (Note) One time -
After periodic inspection (Note) One time One time
Note: Periodic inspection means regular maintenance company inspection and intermediate inspection.
(3) Performance Test
Calculation methods of various efficiency indexes for grasping performance of steam power stations are as shown in
the table below, whereas heat input-output methods are primarily applied for heavy/crude oil, bituminous mixture and
PFBC thermal units and loss methods for coal-fired thermal units.
Additional calculation methods are to be used as secondary methods, for reference in consideration of efficiency.
Items Test name Boiler room Turbine room Gas turbine room
Plant efficiency
Plant applied (Primary) efficiency efficiency efficiency
-
Heavy/crude oil Heat
Heat input/output Heat input/output
Bituminous mix input/output
method
Heat
method
PFBC method standard Heat input/output
input/output
method (Boiler room
Coal-fired Loss method efficiency) ×
Loss method -
thermal power standard (Turbine room
efficiency)
(4) Measurement of Data
For testing, the main fuel is to be exclusively combusted and measurement of data is to be conducted after the
operational condition has become steady.
For more details, "II Methods for Performance Test;1.Operational Condition for Testing and 2.Measurement of Test
85

Data" is to be referred to. For measuring equipment largely affecting the test results, required precision needs to be
ensured. (Confer II Methods for Performance Test;3.Measuring Equipment)
(5) Analysis of Measured Data
Each thermal efficiency indexes are calculated from measured data and their results are analyzed using control charts.
(6) Report and Response to Test Results
Test results are to be immediately reported related authorities along with considerations. In the event any major
performance decrease is observed, necessary measures are taken.
II. Methods for Performance Test
1. Operational Condition for Testing
(1) Main fuel is to be exclusively combusted and operational condition shall be steady.
(2) Load shall be controlled to be constant by load limiter or the openness of control valve.
(3) The same burner is to be used for the same testing load.
(4) Auxiliary steam extraction to other units shall be stopped.
(5) Soot blower needs to be completed before test, otherwise efficiency correction for steam extraction is to be
done.
(6) Furnace bottom ash need be cleared before test if such affects the results.
(7) Pure water supply to make-up tank shall be stopped.
(8) Other matters are the same as normal operation.
2. Measurement of Test Data
(1) One hour before measurement, operational condition is to be set in testing load, confirming the steady
condition of each part, measurement is to be commenced.
(2) Measurement of record is conducted for 2 hours, every 30 minutes. Measurement of fuel consumption,
however, is to be conducted for 4 hours for obtaining precise values.
(3) Measurement of Fuel Consumption
• Coal··········Sum of measurements of each coal scale, not taking into consideration the changes in coal
level in the hopper.
• Fuel oil·····See flowmeter.
(4) Sampling of Fuel
• Coal··········Considering the coal consumed in one test as 1 log, sample out 60 units of 500g specimen for
1 lot using auto-sampler of each coal scale (or equal time interval) and prepare 1
specimen for one test.
In case specimen sampling is impossible due to structural reasons for coal scale such
as sealed type, sampling is done using other proper methods.
• Fuel oil·····Sample out 1 specimen for one test from lines after the tank outlet.
(5) Measurement of generator output is done using signals from the generator input into the plant management
system. (When such plant management system in not installed, integrated power meter in central control
room is to be used)
(6) Sampling of Ash (Only for coal-fired thermal power plant)
1 specimen for one test is sampled out from EP representing hopper or furnace bottom. In case, unburned
matter for MC or PC collected ash cannot be ascertained by EP ash, sample should be taken from MC and
PC.
86

(7) Sampling of exhaust gas is to be done at Eco outlet and designated point of AH outlet for analysis by Orsat
method or corresponding methods.
For PFBC unit, analysis is conducted between boiler outlet and gas turbine inlet.
(8) Items for Specimen Analysis are as follows;
Analysis of specimen is based on “Fuel Quality Test Manual.”
Type of fuel Coal Heavy Bituminous mix Remarks
Analysis items crude oil
Calorific value (cid:99) (cid:99) (cid:99) High standard
Density - (cid:99) (cid:99)
Humidity (cid:99) - -
Moisture (cid:99) (cid:85) (cid:85) Industrial analysis
87
leuF
Ash content (cid:99) - -
Carbon (cid:99) (cid:85) (cid:85) Elemental analysis
Hydrogen (cid:99) (cid:85) (cid:85) ″
Nitrogen (cid:99) (cid:85) (cid:85) ″
sisylanA
Combustive sulfur (cid:99) (cid:85) (cid:85) ″
CO (cid:99) (cid:85) (cid:85) Orsat corresponding methods
2 Eco
CO (cid:99) (cid:85) (cid:85) ″
Outlet
O (cid:99) (cid:85) (cid:85) ″
2
AH outlet O (cid:99) (cid:85) (cid:85) ″
2
sisylana
sag
detsuahxE
Boiler outlet O (cid:99) - - PFBC Unit
2
Furnace clinker (cid:99) - -
EP ash (cid:99) - -
MC ash (cid:133) - -
PC ash (cid:133) - -
sisylana
rettam
denrubnU
(Note) (cid:99) : Items to be analyzed
(cid:85) : Items analyzed when loss method is applied
(cid:133) : Items analyzed as necessary
− : Items not analyzed
(9) Test procedure
It is as shown below:

Test Procedure
Time 0 1H 2H 3H 4H 5H 6H
Test load
Record
Coal sampling
Fuel consumption record
Heavy/crude oil, ash sample
Gas analysis
3. Measurement Equipment
(1) Precision of Meters
Measuring equipment shall be arranged according to the table, grasping its precision.
Input minimum
Measuring Precision /
Measurement items Unit value (min. meter Remarks
position tolerance
reading)
Carbon % − 0.01% 0.03% No water base
Hydrogen ″ − 0.01% 0.15% ″
Nitrogen ″ − 0.01% 0.06% ″
88
sisylana
leuF
… … … … … …
AH outlet gas temp °C − (Central 1°C ±0.5°C
control)
FDF inlet air temp (dry ball) ″ ″ ″ ″
relioB
… … … … … …
− (Central ±0.005Mpa
Main steam MPa 0.01Mpa (1atg)*
control) (±0.5atg)*
Reheat steam ″ ″ ″ ″
erusserP
… … … … … …
°C − (Central 1°C ±0.5°C
Main steam
control)
Reheat steam ″ ″ ″ ″
enibruT
.pmeT
… … … … … …
*The brackets show the minimum reading values of equipment for power stations requiring meter reading.
(2) Correction of Measuring Equipment
The following correction shall be done to measuring equipment.
a. Until testing time conducted after periodic inspection
All measuring instruments used for measurement
b. Until other testing time
Coal scale and other instruments deemed necessary

4. Measurement Data and Calculation Methods
For calculation of each thermal efficiency figure, the measurement data and calculation methods shown in Appendix 5
are to be used. No irrelevant data need be used for calculation.
III. Analysis of Test Data
1. Data Processing and Control charts
The measured data are to be filled in and gathered in Performance Test Measurement Record (Appendix 4), and each
thermal efficiency figure in Performance Test Results (Appendix 1). In addition, Control charts (Appendix 2) are to be
prepared for consideration of each unit’s performance.
2. Preparation of Control Charts
Control charts are prepared to determine whether the plant is in a steady condition or not, using JIS Z-9021,
“Shewhart Control chart.”
(1) Application of Control chart
a. Applied to 4 items, namely, gross efficiency, boiler room efficiency, turbine room efficiency, auxiliary
power ratio.
b. Control charts are prepared for each item above for load profile of 4/4 and needed.
(2) Control Limit
For control limit used for control charts, 3 sigma method (allowing 3 times of standard deviation range above and
below expected value) is to be adopted.
• Upper Control Limit (UCL) = Expected value + (3×Standard deviation)
• Lower Control Limit (LCL) = Expected value – (3×Standard deviation)
In order to obtain control values, test needs to be conducted a few times, and the estimated value from the
results can be used.
(3) Judgment by Control Chart
Control chart is useful for recognizing unit’s deviation from controlled condition. Generally, when the measured
values are within the control limit lines, units are considered as normal. If these are beyond the limit lines, it is viewed
as abnormal, requiring clarification. The following cases need caution.
a. One point is located beyond the control limit.
b. 9 points are on the same side of the center line.
c. 6 points have increased or decreased.
d. 14 points are rising and falling alternately.
e. Of the consecutive 3 points, 2 points are in the domain of 2 σ and 3 σ or beyond.
f. Of the consecutive 5 points, 5 points are in the domain of σ and 2 σ or beyond.
g. Consecutive 15 points are in the domain of ± σ.
h. Consecutive 8 points are in the domain beyond ± σ.
The conventional control lines (center line and control limit line) can be insufficient as a standard in case unit
condition changes. In such a case, a new control line needs to be provided using the recent data as auxiliary
data.
89

90

<Thermal Efficiency Calculation Equation> Appendix - 2
1. Definition of boiler room efficiency, turbine room efficiency, unit thermal efficiency
(1) Boiler room efficiency (η)
B
Diagram 1 From unit thermal equilibrium line diagram, boiler room efficiency is defined as follows. Also,
auxiliary input heat into boiler system Q is defined as input heat or negative output heat in some cases. Here, the
EX
latter concept is adopted, viewing only fuel combustion heat as input heat.
QTS (Output heat) QRS (Output heat)
QG
Turbine heat generating
QO (Output heat) Qf (Fuel combustion heat)
Boiler system
system
(Generator output)
QEX (Boiler auxiliary heat input)
QTL (Heat loss) QBL (Heat loss)
Diagram 1 Unit Heat Equilibrium
Boiler room efficiency can be calculated as follows based on heat equilibrium of boiler system;
Q + Q = Q + Q + Q
f EX O BS BL
Q – Q = Q + Q – Q
f BL O BS EX
Boiler room efficiency η B =(1- Q Q B f L) = Q O +Q Q BS -Q EX
f
Loss method Heat input-output method
(2) Turbine room efficiency (η )
T
Consider turbine room input heat as boiler room output heat Q , focus only on generator output as turbine room
O
efficiency.
Turbine room efficiency can be calculated as based on heat equilibrium of turbine system;
Q =Q +Q +Q
O G TS TL
Q −Q −Q =Q
O TS TL G
Q Q
TL G
Turbine room efficiency η T =(1 ) =
Q -Q Q -Q
O TS O TS
Loss method Heat input-output method
(3) Unit Thermal Efficiency (η )
P
91

Unit thermal efficiency is the product of boiler room efficiency multiplied by turbine room efficiency.
Q +Q -Q Q
O BS EX T
Unit thermal efficiency η P =η B ×η T = ×
Q Q -Q
f O TS
(Heat input-output standard method)
Q Q +Q -Q
G O BS EX
= × ··································(1)
Q Q -Q
f O TS
(Note) Conventionally, Unit thermal efficiency by heat input-output method has been calculated as
Q
G
η
P
=
Q
f
However, the steam generated in the unit system is used outside, the heat value of such steam must be incorporated
into the calculation. Therefore, Equation (1) can represent the heat input-output method unit thermal efficiency.
Theoretically, heat input-output method and loss method should compute out the same results.
(4) Boundary of Boiler and Turbine Systems
Boundary of boiler and turbine systems are shown in Diagram 2.
Turbine system Boiler system
W (cid:120)
MS iMS
W (cid:120)
Ej iEj SH
W (cid:120)
SS iSS
WSD (cid:120) iSD
W (cid:120)
HR iHR Qf (cid:120) QEX
W (cid:120) RH
RS iRS
Heat loss
W (cid:120)
LR iLR
Drain
Heavy oil Heavy oil
heater
W FW (cid:120) iFW AH Atomize
steam
Exhaust gas
W SAH (cid:120) iSAH SAH Combusted air
W SAH (cid:120) iSAHD Heater
W SC (cid:120) iSC SC (qsc)
W (cid:120)
SC iSCD
Diagram 2 Boundary of Boiler and Turbine Systems
92

2. Calculation Method of Boiler Room Efficiency
(1) Heat input-output method boiler room efficiency (η )
Bi
Q +Q -Q
O BS EX
η
Bi
= ×100[%] Qf = H
f ⋅
M
f
Q
f
Q :Fuel combustion heat [kJ/h]
f
Q :Boiler auxiliary input heat [kJ/h]
EX
Q :Boiler room output heat (For generation) [kJ/h]
O
Q : ″ (Heating, etc) [kJ/h]
BS
H :Fuel higher heating value [kJ/h]
f
M :Fuel consumption [kg/h]
f
Q =W · +W · W · –W · –W · –W · –W ·
O MS iMS HR Ej iEj SS iSS RS iRS LR iLR FW
–W ( – )–W ( – )–Q
iFW SAHiSAH iSAHD SCiSC iSCD EX
W : Main stop valve inlet steam flow rate [kg/h]
MS
: ″ enthalpy [kJ/kg]
iMS
W : High temp reheat steam flow rate [kg/h]
HR
: ″ enthalpy [kJ/kg]
iHR
W : Ejector driving steam flow rate [kg/h]
Ej
: ″ enthalpy [kJ/kg]
iEj
W : Superheater spray water flow rate [kg/h]
SS
: ″ enthalpy [kJ/kg]
iSS
W : Reheater spray water flow rate [kg/h]
RS
: ″ enthalpy [kJ/kg]
iRS
W : Low temp reheating steam flow rate [kg/h]
LR
: ″ enthalpy [kJ/kg]
iLR
W : Final feed water heater outlet flow rate [kg/h]
FW
: ″ enthalpy [kJ/kg]
iFW
W : SAH heating steam flow rate [kg/h]
SAH
: ″ enthalpy [kJ/kg]
iSAH
: SAH drain enthalpy [kJ/kg]
iSAHD
W : SC heating steam flow rate [kg/h]
SC
: ″ enthalpy [kJ/kg]
iSC
: SC drain enthalpy [kJ/kg]
iSCD
93

( ) ( )
Q
BS
= qsc
2
− qsc
1
(qsc) : Heating value brought by feed water at SC inlet [kJ/h]
1
(qsc) : Heavy oil heating and atomizing steam generated at SC [kJ/h]
2
Q
EX
= W
SAH
(Note)
(
-
)
+W
(Note)(
-
)
iSAH iSAHD SC iSC iSCD
(Note) W and W show steam flow from other units, own unit being 0.
SAH SC
Main Stop Valve Inlet Steam Flow Rate (W )
MS
1
W = W +W -W -W -W - W
MS FW SS Ej BD BS 2 CL
W = W -W -W
CL MU BD BS
W : Boiler air ejecting heater etc. flow rate [kg/h]
BS
W : Cycle leak rate [kg/h]
CL
W : Continuous blow rate [kg/h]
BD
W : Make-up water [kg/h]
MU
Low Temp Reheat Steam Flow Rate (W )
LR
W = W -W -ΣW
LR MS HL Hi
W : High pressure turbine leak [kg/h]
HL
W : Leakage from low temp reheat steam pipe [kg/h]
Hi
High Temp Reheat Steam Flow Rate (W )
HR
W = W +W
HR LR RS
94

(2) Loss Method Standard Boiler Room Efficiency (η )
B1
Q
η =1− BL −L −L −L −L
B1 Q CL BD AT EX
f
Σ : Boiler heat loss total [kJ/kg · fuel]
Li
Σ = L +L +L +L +L +L +L +L
Li g w as ASH co Rd UB AH
a. Lg Dry gas heat loss
L = C ⋅ { M + (m−1)M }( t −t )
g g gt at g a [kJ/kg · fuel]
C : Dry gas specific heat 1.38 [kJ/m3N · K]
g
M : Theoretical combustion gas amount [m3N/kg · fuel]
gt
m : Eco outlet air excess coefficient
M : Theoretical air amount [m3N/kg · fuel]
at
t : AH outlet gas temperature [°C]
g
t : Air temperature (FD inlet temperature) [°C]
a
b. L Loss due to Water Content, Hydrogen Combusted Water in Fuel
w
L = (W +W )( i −t ) [kJ/kg · fuel]
w w h g a
W : Water content in fuel [kg/kg · fuel]
w
W : Hydrogen combusted water in fuel [kg/kg · fuel]
h
i : Steam enthalpy at steam pressure 10.1kPa, t (AH outlet gas temperature) °C
g g
[kJ/kg]
t : Air temperature [°C] (same value as water enthalpy [kJ/kg]=t)
a a
c. L Loss due to air humidity
as
( )
L =1.29Z⋅m⋅M t −t [kJ/kg · fuel]
as at g a
Z : Absolute humidity [kg/kg]
Cs : Steam specific heat 1.88 [kJ/kg · K]
95

d. L Ash sensible heat loss
ASH
( )
L =C ⋅ A ⎨ ⎧P BOT ( 800−t ) + 100−P BOT ( t −t ) ⎬ ⎫ [kJ/kg · fuel]
ASH ASH 100⎩100 a 100 g a ⎭
C : Ash specific heat 1.05 [kJ/kg · K]
ASH
A : Ash content in fuel [%]
P : Furnace bottom ash falling rate [%]
BOT
e. L Heat loss due to unburned fuel
co
[ ]
L = H ⋅ { M + (m−1)M } ⋅ CO [kJ/kg · fuel]
co co gt at 100
H : CO combustion heat [kJ/m3N]
co
[CO] : Volume ratio of CO [%]
(Orsat analysis value at Eco outlet)
f. L Heat loss due to radiation
Rd
(According to A.M.B.A. Standard Radiation Loss Chart in ASME Power Test Code)
g. L Heat loss due to unburned matter in ash
UB
A u
L = Hc⋅ ⋅ [kJ/kg · fuel]
UB 100 100−u
Hc : Carbon heating value 33,900 [kJ/kg]
u : Average unburned matter in ash [%]
h. L Heat loss due to AH air leakage
AH
L = C (1+1.61Z) ⋅ ε ⋅ { M + (m−1)M }( t −t ) [kJ/kg · fuel]
AH a 100 gt at g a
C : Specific heat of air (=C ) 1.30 [kJ/m3N · K]
a S
ε : AH inlet gas amount standard air leaking ratio [%]
96

i. LCL Cycle Leakage Heating Value Loss
( )
1 W −t
L = ⋅ CL iFW a
CL 2 Q
f
W : Cycle leakage flow rate [kg/h]
CL
: Final feed water heater outlet feet water enthalpy [kJ/kg]
iFW
j. L Heat loss due to continuous blow
BD
( )
W −t
L = BD iFW a
BD Q
f
W : Continuous blow amount [kg/h]
BD
: ″ enthalpy [kJ/kg]
iBD
k. L Heat loss due to atomizing steam
AT
( )
W −t
L = AT iFW a
AT Q
f
W : Atomizing steam flow rate [kg/h]
AT
l. L Other heat loss
EX
In case any loss is found other than a.~k., it is totaled and considered as other heat loss as a whole.
Theoretical air Mat
1 ⎧ ⎛ o′⎞ ⎫
Mat = ⎨8.89c′+26.7⎜h′− ⎟+3.33s′⎬ [m3N/kg · fuel]
100⎩ ⎝ 8 ⎠ ⎭
( )
100− u
c′=c⋅ W1 −A⋅ Combustion carbon amount [%]
100 100−u
( )
100−
h′= h⋅ W1 [%]
100
( 100− ) ⎛ 100A ⎞
o′=o⋅ W1 [%] o =100−⎜c+h+n+ ⎟ [%]
⎜ ⎟
100 100−
⎝ ⎠
W1
( )
100−
s′=s⋅ W1 [%]
100
97

c : Carbon
h : Hydrogen
Fuel elemental analysis value (No water basis) [%]
n : Nitrogen
s : Combustive sulfur
o : Oxygen [%]
: Fuel inherent moisture [%]
W1
Air Excess Coefficient m
21
m =
⎧(
O
)
−0.5
(
CO
)⎫
21−79⎨ 2 ⎬
( )
N
⎩ ⎭
2
In this regard, however,
(N)=100−{(CO )+(CO)+(O )}
2 2 2
(O) :
2
(CO) :
2 Indicating volume ratio in dry combustion gas
(CO) : [%]
(N
2
) : O2, CO2, CO are Orsat analysis
Theoretical Dry Gas Amount M
gt
1 ⎧ ⎛ o′⎞ ⎫
M = ⎨8.89c′+21.1⎜h′− ⎟+3.33s′+0.8n′⎬ [m3N/kg · fuel]
gt 100⎩ ⎝ 8 ⎠ ⎭
( )
100−
n′= n⋅ W1
100
Hydrogen combustion moisture in fuel W and water content in fuel W
h W
9h′
W = [kg/kg · fuel]
h 100
W = W1 + W2 [kg/kg · fuel]
W 100 100−
W2
: Surface humidity of coal [%]
W2
98

Absolute Humidity Z
P
( )
Z=0.622⋅ s [kg/kg] P = P − 0.0008 ⋅P ⋅ T − T
s W a d W
P −P
a s
P : Atmosphere pressure [kPa]
a
P : Steam pressure [kPa]
s
P : Saturated steam pressure for wet-bulb temperature [kPa]
W
T : Dry-bulb temperature (=T) [°C]
d a
T : Wet-bulb temperature [°C]
W
AH Air Leakage Ratio ε (Eco outlet gas amount basis)
( ) ( )
O out− O in
ε= 2 2 ⋅100 [%]
( )
21− O out
2
(O) out : AH outlet O [%]
2 2
(O) in: Eco outlet O [%]
2 2
3. Calculation Method of Turbine Room Efficiency
Q
η = G ⋅100 [%]
T Q −Q
O TS
Q : Generator output (=860 · P ) [kJ/h]
G G
P : ″ [kWh]
G
Q : Turbine output heat [kJ/h]
TS
4. Calculation Method of Unit Thermal Efficiency
(1) Gross unit thermal efficiency (η )
P
a. Unit thermal efficiency based on heat input-output method (η )
Pi
Q
η = G ⋅K⋅100 [%]
Pi Q
f
K : Modification coefficient (See IV, exposition, “calculation processing”)
Q +Q −Q
K = O BS EX
Q −Q
O TS
b. Unit thermal efficiency based on heat loss method (η )
P1
η =η ⋅η /100 [%]
P1 B1 T
99

(2) Auxiliary Power Ratio (α)
P
P + G ⋅P
GH ∑P CM
α= G ⋅100 [%]
P
G
P : House transformer power [kWh]
GH
ΣP : Total of generator output of each unit [kWh]
G
P : Common auxiliary power [kWh]
CM
(Note) Auxiliary power consists of the common auxiliary power proportionately divided by each unit’s generator
output added by house transformer power.
(3) Net Unit Efficiency (η ’)
P
′ ⎛ α ⎞
η =η ⋅⎜1− ⎟ [%]
P P ⎝ 100⎠
5. Correction of Calculated Thermal Efficiency
The following correction is conducted for calculated thermal efficiency.
(1) Boiler room efficiency (η )
B
a. Atmosphere temperature correction
b. Fuel surface humidity correction
c. Fuel hydrogen content correction
d. Fuel inherent moisture correction
(2) Turbine room efficiency (η )
T
e. Main steam pressure correction
f. Main steam temperature correction
g. Spray water correction
h. Reheat system pressure loss correction
i. Reheat steam temperature correction
j. Condenser vacuum correction
k. Generator power factor correction
100

6. Various Constants in Calculation
(1) Thermal efficiency is calculated with higher heating value standard.
(2) Standard temperature for thermal efficiency is FDF inlet and atmosphere temperature.
(3) Dry gas specific heat shall be 1.38 kJ/m3N · K from JIS B-8222.
(4) Specific heat for dry air and air shall be 1.30 kJ/m3N · K from JIS B-8222.
(5) Enthalpy for exhaust gas steam shall be calculated with steam partial pressure as 10.1kPa.
(6) Heating value of carbon shall be 33,900kJ/kg from JIS B-8222.
(7) Heating value of carbon monoxide shall be 12,610 kJ/kg from JIS B-8222.
(8) Specific heat of steam shall be 1.88 kJ/kg · K from “Heat Management Handbook.”
(9) Specific heat of ash is 1.05 kJ/kg · K from “Heat Management Handbook.”
(10) Cycle leakage loss shall be equally shared by boiler and turbine system, finally leaked to the outside of system at
final feed water heater outlet.
(11) Make-up water, air sensible heat and fuel sensible heat shall be 0.
7. Calculation Standard for Main Steam Flow Rate
In this manual, feed water flowmeter standard shall be adopted. Other standards can be used provided sufficient
precision is ensured. (Grounds for adopting feed water flowmeter standard is as mentioned below)
Moreover, for grasping the deviation error of feed water flowmeter standard, it is desired that main steam flow
rate for high pressure turbine first-stage pressure standard, condenser flowmeter standard, etc is used as reference.
The calculation method of main steam flow rate using high pressure turbine first-stage pressure standard by means
of regression line will be explained later.
(1) Calculation Standards for main steam flow rate are as follows;
a. Main steam flowmeter standard
b. Condenser flowmeter standard
c. Feed water flowmeter standard (Adopted in JIS B-8222 and this manual)
(2) Comparison of each calculation standard
a. Main steam flowmeter standard has a weaker reliability than other methods since steam itself is compressive
fluid.
b. Condenser flowmeter standard ensures high precision due to its low temperature and pressure when used, but
the feed water heater drain flow rate needs to be calculated with low-precision flowmeter or heat balance
calculation, thus showing lower reliability.
c. Feed water flowmeter standard has a problem of deviation error caused by scale attaching to the flowmeter’s
flow nozzle, but precision is thought to be higher than the aforementioned standards.
8. AH Air Leakage
According to the boiler boundary in Diagram 2, exhaust gas analysis is done at AH outlet, but in reality, to
eliminate the influence of combustion air leaking in, it is done at Eco outlet.
Along with this, AH air leakage ratio is measured to obtain the heat loss due to AH air leakage.
101

9. Calculation Method of High Pressure Turbine First-Stage Pressure Standard Steam Flow Rate by
Regression Line
(1) Preparation Procedure
a. At each generator output, high-pressure turbine firs-stage pressure (P) and feed water flowmeter standard main
steam flow rate (W ) are measured.
MS
(Note 1) High-pressure turbine firs-stage pressure is measured with meters capable of reading minute fluctuations
such as expanded pressure meter, transmitter output voltage.
(Note 2) Main steam flow rate is calculated after density correction of each flow rate.
b. Regression line for high-pressure turbine firs-stage pressure (P) and feed water flowmeter standard main steam flow
rate (W ) are calculated.
MS
This regression line is applied to performance tests conducted from this point on, calculating main steam flow
rate.
(2) Calculation Example
Example of measurement results
Main steam flow
rate (W
MS
)
Generator High-pressure Main steam
SH spray
(W )
SS output turbine flow rate WMi
firs-stage [t/h]
pressure Pi
[MPa]
MCR 13.0 580.470
4/4 11.4 514.760
W =W −W
MS FW SS
3/4 8.4 370.680
2/4 5.8 242.880
Feed water flow
Minimum 3.5 152.810
rate
(W
FW
)
Calculation procedure
a. Calculate S=Σ Pi2−(Σ Pi)2/n. S =60.928
1 1
b. Calculate S=Σ (W )2−[Σ (W )]2/n. S =128,557.61
2 Msi Msi 2
c. Calculate S=Σ Pi (W )− Σ Pi (W )/n. S =2,796.953
3 Msi Msi 3
d. Calculate P=Σ Pi/n. P = 8.42
e. Calculate W =Σ (W )/n. W =372.32
MS Msi MS
f. From above,
S ⎛ S ⎞
W = 3 P+⎜W − 3 P⎟ W =45.9059P−14.2074
MS S ⎜ MS S ⎟ MS
⎝ ⎠
1 1
Calculating regression line.
g. Calculating the correlation function γ,
1
⎛ S 2 ⎞2
γ=⎜ 3 ⎟ γ =0.9994
⎜ ⎟
S ⋅S
⎝ 1 2 ⎠
102

2.6 COMBUSTION OF COAL
Because coal has a variety of physical and chemical properties compared with other fossil fuels (heavy oil or
gas) according to the difference in generation conditions, the burning process (ignition and combustibility) and
exhaust-gas composition after combustion vary with the type of coal.
In this seminar, pulverized coal combustion is described generally: how coal properties affect combustion, the
concept of combustion, combustion equipment, and the development of combustion technology.
2.6.1 How Coal Property Affects Pulverized Coal Combustion
For the preliminary evaluation of coal as fuel, we generally conduct a proximate analysis, an ultimate analysis
and an ash content analysis of coal. The detailed analyses of coal are described in “II-1 Coal”. This section
discusses how the coal properties relate to combustibility, grindability, slagging/fouling and abrasion
characteristics, etc. when coal is evaluated as a fuel burned in pulverized coal burning boilers.
2.6.6.1 Relation of Coal Property to Ignitability and Combustibility
Certain items are used to evaluate the ignitability and combustibility of coal: the fuel ratio and coal rank, the
volatile matter and calorific value, the adhesiveness and agglomeration, etc.
(1) Fuel Ratio and Coal Rank
The fuel ratio has traditionally been used as the simplest standard to evaluate the ignitability and combustibility
of coal. The fuel ratio means the weight ratio of fixed-carbon to the volatile matter. Generally speaking, the higher
the fuel ratio of coal, the poorer the ignitability and the slower the combustion speed. It can be said that coal with
a fuel ratio 2.5-3.0 is preferable for pulverized coal burning boilers in order to lower unburned losses.
The coal rank means the degree of coalification, which is classified according to the physical and chemical
properties of coal.
As shown in Table 1, the coal rank is categorized into brown coal, sub-bituminous coal, bituminous coal and
anthracite coal according to the order of coalification, on the basis of a calorific value, fixed carbon amount,
volatile matter amount, and agglomeration characteristic.
Table 1 Coal Rank (ASTM Standard)
Item Range of fixed Range of volatile Range of calorific value Agglomeration
carbon matter (constant wet characteristic
Class Group (dry coal/no-mineral (dry coal/no-mineral coal/no-mineral base
base %) base %) kcal/kg)
I. Anthracite coal 1. High anthracite coal 98 ≤ ≤ 2 -
2. Anthracite coal 92 ≤ / <98 2 < / ≤ 8 - Not exist
3. Semi-anthracite coal 86 ≤ / <92 8 < / ≤14 -
II. Bituminous coal 1. Low volatile 78 ≤ / <86 14 < / ≤ 22 -
bituminous coal
2. Semi-volatile 69 ≤ / 78 22 < / ≤ 31 -
bituminous coal
3. A High volatile < 69 31 < 7,780 ≤
bituminous coal Generally, exist
4. B High volatile - - 7,220 ≤ / <7,780
bituminous coal
5. C High volatile - - 6,390 ≤ / < 7,220
bituminous coal 5,830 ≤ / < 6,390 Exist
III. Sub-bituminous 1. A Sub-bituminous - - 5,830 ≤ / < 6,390
coal coal
2. B Sub-bituminous - - 5,280 ≤ / < 5,830 Not exist
coal
3. C Sub-bituminous - - 4,610 ≤ / < 5,280
coal
IV. Brown coal 1. A. Brown coal - - 3,500 ≤ / < 4,610
Not exist
2. B. Brown coal - - < 3,500
103

Anthracite refers to coal with non-agglomeration characteristics, low volatile matter, and a fuel ratio of more
than 6, and it is poor in ignitability and combustibility. Sub-bituminous coal and brown coal, whose fuel ratio is
less than 1, are excellent in ignitability and combustibility, but poor in mill grindability (explained later) and have
slagging/fouling characteristics. Therefore, bituminous coal, whose fuel ratio is intermediate, is generally used in
pulverized coal burning boilers. The bituminous coal is classified into five types as below, and the higher the rank
the poorer in ignitability and combustibility.
(1) Low volatile matter bituminous coal (the fuel ratio is approx. 4)
(2) Medium volatile matter bituminous coal (the fuel ratio is approx. 2.8)
(3) A high volatile matter bituminous coal (the fuel ratio is approx. 1.5)
(4) B high volatile matter bituminous coal (the fuel ratio is approx. 1.2)
(5) C high volatile matter bituminous coal (the fuel ratio is approx 1.1)
(2) Volatile Matter and Calorific Value
Ignitability evaluation of coal itself is generally performed in accordance with the volatile matter amount and
the calorific value contained in coal. In general, when the volatile matter amount is less than 20%, it is necessary
to consider some methods to stabilize the ignitability. The following expression has traditionally been used as the
ignitability index:
[(raw coal calorific value kcal/kg) - 81 x (fixed carbon %)]
Ignitability index =
(volatile matter %) + (moisture %)
The ignitability index, which can be used as a judgment criterion of the ignition difficulty of coal with much
surface moisture, indicates discharged moisture and a calorific value of volatile matter. When the ignitability
index is 35 or less, it is said some measures for ignitability improvement should be taken.
(3) Adherence and Agglomeration Characteristics
Coal adherence means a property of the cake-like expansion of coal when it is heated, and is usually judged by
a button index. Coal with a high button index requires special attention because fuel-fines adhere to or clog in a
burner nozzle or unburned hydrocarbon increases due to fuel-fines blended in the process of combustion. For coal
with a button index of 6-7 or more, it is necessary to consider special designs to prevent these problems.
2.6.1.2 Relation of Coal Property to Grindability and Dryness
In general, pulverized coal combustion is characterized by pulverizing coal to 50-100µm and drying and
burning it. The point of this combustion lies in the selection of the coal pulverization degree so that the coal can
be burned out in a combustion chamber. As aforementioned, the coal combustibility greatly varies with the coal
rank. The following shows the type of coal and the grading required for combustion.
(1) Anthracite coal <10-15% (200 mesh = 74µm residual amount)
(2) Bituminous coal <15-35% (-ditto-)
(3) Semi-bituminous coal <35-45% (-ditto-)
(4) Brown coal <45-55% (-ditto-)
The difficulty in coal grinding is usually evaluated by the HGI (Hardgrove Grindability Index) and the moisture
based on the ASTM standard.
(1) HGI
Because linking the coal component analytical values to the HGI tends to have many errors, it is preferable to
directly measure the HGI to gauge coal grindability. The rough standard of grindability is as follows. The higher
the HGI, the easier the grinding.
(1) Coal with a fuel ratio of approx. 1.0 is 35-45 in HGI
(2) Coal with a fuel ratio of approx. 2.0 is 45-75 in HGI
(3) Coal with a fuel ratio of approx 3.0 is 75-100 in HGI
Because the smaller the HGI, the poorer the grindability and because large-sized mills are required, a HGI of
more than 40 is preferable.
(2) Moisture
The mill grinding capability is affected by total moisture including surface- and inherent moisture.
High-moisture content causes a lack of dryness in the mill, decreases the classification efficiency in the mill and
accordingly lowers the mill grinding capability. From this viewpoint, the total moisture contained in coal is
preferably 20% or less.
2.6.1.3 Slagging Characteristic and Ash Property
Slagging is a phenomenon whereby coal ash (slag) melted in the boiler furnace adheres to the radiant
heat-transfer surface in the furnace, and is cooled, solidified, and built-up. The following coal properties relate to
104

the degree of slagging:
(1) Ash Melting Temperature
Slagging results from the fact that coal ash melted in the furnace bumps against the heat-transfer surface and
adheres to it before solidifying. Slagging is judged by whether the ash melting temperature is higher or lower than
the gas temperature in the proximity of the heat-transfer surface. Such a problem is rarely seen with coal with a
melting temperature exceeding 1300℃ in pulverized coal burning boilers.
(2) Ash Content
In the case of coal with strong slagging characteristics, the slag accumulation amount is proportional to the ash
amount input into the furnace. Because the ash amount input into the furnace is proportional to the ash-content
amount per coal calorie, the coal with high ash-content and low calorie requires more attention.
(3) Ash Alkaline Ratio
The ash alkaline ratio is defined by the following expression using the figures showing the ratio of the basicity
component to the acidic component in ash.
(Fe O +CaO+MgO+ Na O+K O)
2 3 2 2
Ash alkaline ratio =
SiO +Al O +TiO
2 2 3 2
The large ash alkaline ratio means an increased slagging characteristic because low-melting oxides and
compound salt are easily generated. It is generally said that the slagging characteristic is small if the ash alkaline
ratio is 0.5 or less.
This is also identified by the color of ash: much SiO and Al O show white, much CaO shows yellow, much
2 3 3
Fe O shows red, and much Fe O and CaO show pink to purple. That is to say, as the ash color changes from
2 3 2 3
white to reddish, the ash slagging characteristic becomes stronger.
(4) Fe O /CaO Ratio and S-content in Coal
2 3
When the ratio of Fe O to CaO in ash is approx. 0.3-3, low-melting compounds tend to be generated. This fact
2 3
can become a supplementary judgment criterion of the ash alkaline ratio.
Also, when the S-content in ash is large, Fe generates basicity components and low-melting sulfuric acid complex
salt, increasing the slagging characteristic. The S-content in ash is preferably 2% or less for preventing slagging
problems.
2.6.1.4 Fouling and Ash Property
Fouling means a phenomenon whereby coal ash in the gaseous or melting state condenses, adheres to and
builds up on the convective heat-transfer surface of the superheater or the reheater at the rear of the furnace. The
following coal content affects fouling:
(1) Basicity component in Ash
The most influential on fouling is basicity substances including Na. Sufficient care should be taken over coal
with a large content of Na O, K O, Cl, CaO, etc., especially that with a large Na O content.
2 2 2
(2) S-content in coal
S-content in coal develops the occurrence of fouling by generating basicity components and low-melting
sulfuric acid complex salt.
2.6.1.5 Abrasion and Coal Properties
Pulverized coal burning boilers will cause the abrasion of grinders (mills) or pulverized coal pipes, and also of
the backside convective heat-transfer surface by fly ash.
The influential mineral matter causing mill abrasion is quartz, pyrite, etc. When judged from the analytical values,
the content of quartz, Fe O and S-content become its criterion.
2 3
The abrasion degree by fly ash is largely affected by the hardness, density and granularity of fly ash. When
judging the abrasion degree based on the coal properties, the following mineral matter in ash should be focused
on:
(1) Quartz (α-SiO : Mohs hardness = 7)
2
(2) Cristobalite (SiO : Mohs hardness = 7)
2
(3) Mullite (3Al O & SiO : Mohs hardness = 7.5)
2 3 2
(4) Hematite (Fe O : Mohs hardness = 6)
2 3
(5) Anorthite (CaAl Si O : Mohs hardness = 6)
2 2 3
105

2.6.2 Concept of Pulverized Coal Combustion
When coal is pulverized in the grinder (mill) and float-fired in the pulverized state, the ignition time and
combustion time are extremely shortened and the burner combustion can become just like heavy oil or gas fuel is
being burned. This is the greatest characteristic of pulverized coal combustion. In the following section, the
combustion mechanism and characteristics of pulverized coal are explained.
2.6.2.1 Combustion Mechanism of Pulverized Coal
The model of pulverized coal burning flames is shown in Fig. 1.
The primary air and pulverized coal blown into the furnace from the coal compartment are heated by radiant
heat from both the surrounding flames and the high-temperature slag adhering to the furnace wall, and then start
igniting and burning, forming a primary combustion area. The primary combustion area is mainly an area where
volatile matter in coal is burned. And there, CH , H , CO etc. volatized from coal grains are mixed with oxygen in
4 2
the primary air diffused from the surroundings, forming flames around the grains. The secondary burning area is
mainly a char burning area, where unburned gases and chars flowing from the primary combustion area are
burned by a diffusive mixture with a secondary air blown from the supplementary air compartment.
Large grain size
Ash + unburned
hydrocarbon
Small grain size
Ash
Coal grainsVolatile matter burning areaChar burning area C co o m m p b le u t s io tio n n
Volatile matter Primary burning area Secondary burning area
discharge (Volatile matter Char burning area
Supplementary air burning area)
compartment
Fig. 1 Model of pulverized coal burning flame
Char burning means the combustion of oxygen and carbon diffused from the surfaces or fine pores of chars, and
the burning velocity is extremely slow compared with that of volatile matter. Therefore, char burnout time
accounts for approx. 80-90% of the total coal burnout time.
In the flame model in Fig.1, the points of pulverized coal combustion we must note are the ignitability, burnout
characteristic and NOx generation characteristic.
These points are closely related to the performance and operability of pulverized coal burning boilers. The
ignitability and burnout characteristic are discussed in this section and the NOx generation characteristic is
discussed in Section 2.3.
(1) Ignitability
The ignition difficulty in pulverized coal greatly varies with the coal properties. According to the individual
coal properties, we will evaluate the burner type, selection of burner design specifications, necessity of auxiliary
burners, and a minimum load which can completely burn coal.
The surface temperature of pulverized coal blown into the furnace rises by its own flame and by the radiant heat
from other high-temperature heat sources in the furnace, and after it reaches a certain level, the coal is ignited, as
commonly explained in the radiant ignition theories. This temperature causing ignition is defined as radiant
ignition temperature. Coal with a higher ignition temperature needs radiant heat from a higher temperature heat
source, and hence stable ignition in the furnace is difficult, causing unstable combustion or increased unburned
hydrocarbon due to the fluctuation of the ignition point. Therefore, special design consideration is required.
106
noitingI
Ignitability NOx generation Burnout
characteristic characteristic
Primary burning area
Qpd [Primary air/coal ratio]
Secondary burning area
QS = [Q total = Qp] Q : Burning quantity

107
)C°(
erutarepmet
noitingi
tnaidaR
Mora
Newlands
Daido
Warkworth
Drayton
Mirror blend
Optimum
Miike
The
Pacific
Ocean
Volatile matter (ash-free basis) (%)
Fig. 2 Relation between volatile matter and radiant ignition temperature
Figure 2 summarizes the relation between the volatile matter in coal and the radiant ignition temperature, when
a small amount of pulverized coal is forcibly fed into the electric furnace in which the temperature can be freely
changed, and is ignited instantly raising shining flames where the ignition temperature is defined as the radiant
ignition temperature.
As shown in the Fig., the radiant ignition temperature drops along with the increase of volatile matter content.
Though the coal with the same amount of volatile matter content shows a variation in ±30°C of the radiant
ignition temperature, this variation is considered to be attributed mainly to the difference in the quality of the
volatile matter or calorific values.
The rate of the volatile matter content in domestic coal used in thermal power stations in our country and of
imported coal ranges from 30-50% based on the ash-free basis whereas the radiant ignition temperature ranges
from 600-700°C. From our past experiences, ordinary pulverized coal burning boilers have almost no problem
with the combustion of coal whose radiant ignition temperature is 750°C or less.
Figure 2 shows the comparison of ignitability among coal with different properties, but actual pulverized coal is
transferred by the primary air and continuously blown into the furnace, as shown in Fig.1.
Now let’s consider the ignition of pulverized coal grain assemblages which float and flow with minute intervals
in the primary air flow. The coal grain assemblages in the pulverized coal plume are initially ignited by an igniter.
After the igniter goes off, the grains temperature rises with a time lapse under the heat balance, where the sum of
the calorific value of own flame, the radiant heat from other heat sources and the chemical reaction in the coal
grain assemblages is equivalent to the calorific value which can raise the temperatures of coal grain assemblages
and the primary air around it.
Symbol Brand (2 P 00 u / l m ve e r s iz h e d p a c s o s a e l s)
Pacific Ocean coal
Daido coal
Amount of coal
supply )m/m(
ecnatsid
noitingI
1. Air temperature Normal
temperature
Air flow rate
Temperature in furnace (°C)
Fig. 3 Relation between temperature in furnace and ignition distance

When the surface temperature of the grains in a coal grain assemblage exceeds the coal radiant ignition
temperature, they are ignited, and this position is called the ignition distance from the burner. Because the smaller
the grain intervals in the coal grain assemblage (the grains density is high), the larger the radiant heat from other
burning coal grains, and the smaller the air heat capacity around the coal grains, so the coal grain temperature is
apt to rise and the ignition distance becomes shorter. On the other hand, if the intervals among coal grains are too
small (the coal grains density is too high), it is difficult for the radiant heat from other heat sources to penetrate the
core, and because the oxygen consumption of the grain assemblage exceeds the oxygen amount supplied in the
primary air, it is difficult for the combustion to continue. So the ignition distance, on the contrary, becomes larger.
Thus, the pulverized coal assemblage in the primary air flow has the optimum ignition point for the coal grain
density (the inverse number of primary air/coal ratio).
Also, as you understand easily, pulverized coal ignition is strongly affected by ambient temperature.
As shown in Fig.3, the ignition distance of coal with lower volatile matter drastically increases along with the
ambient temperature drop, compared with that of coal with high volatile matter.
This ignition distance increases due to the ambient temperature drop coinciding with the fact that the lower the
load on the pulverized coal burning boiler, the worse the ignition stability.
108
)S2mc/g(
*K
tneiciffeoc
yticolev
gninruB
H coal
G coal
A coal D coal
B coal
Ambient gas temperature = 1,200°C
Ambient oxygen density = 0.04 ala
Fuel ratio (-)
Fig. 4 Relation between burning velocity coefficient and fuel ratio
(2) Burnout Characteristic of Pulverized Coal
The burnout characteristic of pulverized coal is important data to predict the amount of unburned hydrocarbon
generated in pulverized coal burning boilers, to select the degree of necessary coal fineness to maintain unburned
hydrocarbon at a low level, and to determine the furnace dimensions. The burnout characteristic of pulverized coal
greatly varies with coal properties.
Figure4 shows the result when coal grains with various properties are suspended with platinum wire in an
electric furnace, and their combustion-decrease characteristics are measured by microbalance under the condition
of constant oxygen density and gas temperature.
The combustion velocity coefficient K* is represented in the following expression:
(W −W )
o E
K*= ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(1)
nπD 2T
o
K*:combustion velocity coefficient (g/cm2•s)
W: grain weight (g)
D: grain size (cm)
T: combustion period (s)
n: the number of grains (pieces)
Suffixes: O: before combustion E: after combustion
In this figure the larger the coal fuel ratio (the ratio of fixed carbon to volatile matter), the smaller the
combustion velocity coefficient. The coefficient of the coal with a high fuel ratio is approx. 1/2-1/5 that of the coal
with a low fuel ratio.

Because, in actual pulverized coal burning boilers, the gas/coal grain temperature and oxygen density change
when coal moves from the burner exit to the furnace exit, and the combustion is largely rate-controlled by
diffusion resistance in the higher temperature area, as well as by chemical reaction resistance in the lower
temperature area. So it is not appropriate to use the burning velocity coefficient K*, which has been measured
under a certain condition, for the calculation of the burnout in the boiler furnace.
The combustion of pulverized coal grains in the furnace is as per the following expression, where the grain size
is Dp:
d ⎛roπ ⎞
⎜ D 3⎟=−πD 2 •K•P⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(2)
⎜ P ⎟ P
dθ 6
⎝ ⎠
1 1 1
= + ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅(3)
K K K
O f
Where, the signs are as follows:
K: general combustion velocity coefficient (g/cm2(cid:120)s)
Kf: combustion velocity coefficient when the oxygen diffusion density in
the gas film is dominant (g/cm2(cid:120)s)
Kc: combustion velocity coefficient when the chemical reaction rate of
the grain surface is dominant (g/cm2(cid:120)s)
P: oxygen pressure (atm)
Dp: coal grain size (cm)
ro: specific gravity of coal grain (g/cm3)
θ: burning time (s)
The general burning velocity coefficient ‘K’ varies depending on the coal properties in addition to the grain size
and burning area gas temperature. Therefore, in order to lower unburned losses in a pulverized coal burning boiler,
we must know the characteristics of pulverized coal grain’s K, coal grain size Dp (coal fineness), in-furnace
retention time θ, and gas temperature distribution and oxygen density distribution in the furnace, and then
determine the furnace dimensions or pulverized coal facilities.
Figure 5 shows the trajectory of the flame axis obtained by simulations of heat-transfer flow in the furnace
using the aforementioned expressions (2) and (3), and the calculation results of the unburned hydrocarbon by
applying the calculation of the gas & oxygen density distribution. The combustion rapidly proceeds in the area
approx. five meters high above the burner toward the furnace exit, but it becomes slower in the area approx. 10
meters high, and the combustion reaction almost does not proceed in the area exceeding 20 meters high due to the
gas temperature drop. Therefore, this suggests that in order to improve the burning efficiency of pulverized coal, it
is more effective to reduce the coal grain size by increasing the coal fineness rather than to lengthen the retention
time in the furnace.
2.6.2.2 Combustion Calculation
(1) Coal Calorific Value
The coal calorific value means calories (kcal) generated when a unit amount (1kg) is completely burned out,
and is defined as two types below:
(1) High heating value (HHV) or gross calorific value (GCV)
(2) Low heating value (LHV) or net calorific value (NCV)
109

Fuel ratio
Fig. 5 Relation between coal fineness and unburned hydrocarbon
The coal calorific value generally means a high heating value, and the measuring method is stipulated in JIS M
8814.
The high heating value includes the steam-condensing latent heat (approx. 600kcal/kg) generated by burning
water (W) and hydrogen (H) in coal. However, because in the actual combustion in boilers, this steam is
discharged from the stack without condensing, the latent heat cannot be utilized and the actual coal calorific value
reduces by this amount. The calorific value from which this latent heat has been subtracted is called a low heating
value, and is calculated by the following expression without relying on the actual measurement. (H and W are
wt%)
LHV = HHV – 6(9H + W) (kcal/kg)
The calorific value is a very important item for combustion calculation. Especially, when it comes to coal, the
calorific values and individual components vary largely with the type of coal - even the same type of coal varies
with the mining layers. So, we must use the results from the same sample for combustion calculation and for all
analytical values.
Many types of calculation formulas can be considered to obtain the calorific value using the coal analytical
values, but those formulas may have omitted complex, chemically-bound heat during coal combustion, or been
determined by natural experiences. So they cannot be applied to every type of coal with high accuracy. Their
values should only be utilized temporarily when the calorific value has not been calculated yet.
Table 2 Component characteristics related to combustion
Molecular weight
Molecular Specific weight Specific constitution
Component symbol Approx. Exact value kg/Nm3 Nm3kg
value
Carbon C 12 12.011 - -
Hydrogen H 2 2.016 0.08997 11.12698
2
Sulfur S 32 32.064 - -
Oxygen O 32 31.999 1.42897 0.69980
2
Nitrogen N 28 28.013 1.25041 0.79974
2
Water vapor HO 18 18.015 0.80374 1.24419
2
Sulfur dioxide SO 64 64.053 2.92659 0.34169
2
Air - 29 28.964 1.29298 0.77341
Carbon dioxide CO 44 44.010 1.97682 0.50586
2
The following expressions are typical examples of calorific value calculation in the ultimate analysis and
proximate analysis of coal.
1. Dulong’s expression (from the result of the ultimate analysis of coal)
HHV = 81C + 342.5(H-O/8) + 22.5S (kcal/kg)
Where, C, H, O and S show the wt% of carbon, hydrogen, oxygen and sulfur, respectively.
2. Kosaka’s expression (from the result of proximate analysis of coal)
HHV = 81Cf + (96 - α (cid:121) W) (cid:121) (Vm + W) (kcal/kg)
Where, Cf, W and Vm show the wt% of fixed carbon, moisture, and volatile matter, respectively, and α is
the coefficient of moisture and is used as the following values:
110
renrub
eht
fo
retnec
eht
morf
thgieH
Air Primary 82°C/secondary 312°C
temperature
Coal fineness
(200 mesh pass / 100 mesh
residuum)
Unburned carbon ratio

When W<5.0 α = 6.5
When W≥5.0 α = 5.0
(2) Combustion Air Flow Rate and Combustion Gas Flow Rate
In order to burn fuel completely, it is necessary to supply necessary and adequate air (oxygen) for combustion.
In actual combustion, air and fuel are not mixed ideally and it is difficult to burn fuel completely by the
theoretically necessary combustion air flow rate alone, hence a proper combustion air flow rate is supplied as an
excess air flow rate depending on the fuel in addition to this theoretical combustion air flow rate. Especially, for
pulverized coal burning, a more excessive air flow rate is needed (for bituminous coal with high volatile matter, it
is approx. 1.2-1.25 in the air ratio) because the combustion characteristic is poorer than that of heavy oil or gas
due to the larger-sized, solid grains with the slow combustion velocity.
Though the major components of coal consist of carbon (C), hydrogen (H), oxygen (O), nitrogen (N), sulfur (S)
etc., the combustible components are carbon, hydrogen and sulfur, each of which is completely burned to become
carbon dioxide (CO ), water vapor (H O), and sulfur dioxide (SO ), respectively. The entire oxygen in coal is
2 2 2
considered to become water (water vapor) by combining with hydrogen during the combustion.
Table 3 List of Component Combustion Values
Theoretical dry air flow rate Theoretical
Combustion Moisture
dry gas flow
Component O N Air product amount
2 2 rate
Upper row: kg/kg Lower row Nm3/kg
Carbon C (CO2)
2.67 8.83 11.50 3.67 12.50 -
1.87 7.02 8.89 1.87 8.89 -
Hydrogen H
2
(H2O)
8.00 26.48 34.48 9.00 26.48 9.00
5.60 21.06 26.66 11.19 21.06 11.19
Oxygen O -1.00 -3.31 -4.31 - -3.31 -
2
-0.70 -2.63 -3.33 - -2.63 -
Sulfur S (SO2)
1.00 3.31 4.31 2.00 5.31 -
0.70 2.63 3.33 0.69 3.33 -
Nitrogen N - - - - 1.00 -
2
- - - - 0.80 -
Moisture W - - - - - 1.00
- - - - - 1.24
1. Calculation expressions of combustion air- and gas-flow rates in the ultimate analysis of coal
The combustion air flow rate needed for coal combustion and the generating combustion gas flow rate can
be calculated by the ultimate analysis using the list of component combustion values shown in Table 2. The
calculation results of component combustion are summarized in Table 3.
In this case, it is assumed that air consists of oxygen and nitrogen in a weight ratio of approx. 23.2% and
76.8% each and in a volume ratio of approx. 21% and 79% each.
The following shows the calculation process of the combustion air- and gas- flow rates regarding carbon
in the list, as well as regarding other components.
1 mol C + 1mol O = 1mol CO
2 2
12 kgC + 32 kgO = 44 kgCO
2 2
Necessary O for C 1kg is:
2
32 2.667
=2.667kgor =1.867Nm3
12 1.429
CO generation by combustion of C 1kg is:
2
44 3.667
=3.667kgor =1.867Nm3
12 1.977
The theoretical dry air flow rate of C 1kg is:
100
2.667× =11.496or
23.2
100
1.867× =8.891Nm3
21
N in C 1kg of the theoretical dry air is:
2
111

76.8
2.667× =8.829or
23.2
79
1.867× =7.024Nm3
21
Theoretically generating combustion gas flow rate of C 1kg is:
CO + N = 3.667 + 8.829 = 12.496 kg
2 2
Or = 1.867 + 7.024 = 8.891Nm
3
From the component combustion values shown in Table 2, the theoretical dry air flow rate (Ado) per kg is
represented in the following expression:
⎡ 0⎤
Ado =11.50C+34.5 H− +4.31•S (kg/kg)
⎢ ⎥
⎣ 8⎦
⎡ 0⎤
Ado'=8.89•C+26.7 H− +3.33•S (Nm3/kg)
⎢ ⎥
⎣ 8⎦
Likewise, the theoretical dry gas flow rate (Gdo) is obtained by the following expression:
⎡ 0⎤
Gdo=12.50C+26.5 H− +5.31S+N (kg/kg)
⎢ ⎥
⎣ 8⎦
or,
⎡ 0⎤
Gdo'=8.89C+21.1 H− +3.33S+0.80N (Nm3/kg)
⎢ ⎥
⎣ 8⎦
Supposing that the moisture included in the burning air is Xa (absolute temperature, kg/kg and dry air),
the water vapor flow rate (Wa) is represented in the following expression:
Wa =Xa (cid:121) Ado (kg/kg) or
Wa’ = 1.61Xa (cid:121) Ado’ (Nm3/kg)
The generating water vapor flow rate (Wf) by the combustion of moisture and hydrogen during burning is
represented in the following expression:
Wf = 9H + W (kg/kg) or
Wf’ = 11.19H + 1.244W (Nm3/kg)
The theoretical wet gas flow rate (Gwo) by which the theoretical dry gas flow rate and the entire water
vapor flow rate are added up is obtained from the following expression:
Gwo = Gdo + W + Wa (kg/kg) or
Gwo’ = Gdo’ + Wf’ + Wa’ (Nm3/kg)
Supposing that the aforementioned air ratio (actual combustion air flow rate plus excess air/theoretical air
ratio) is m, the actual wet air flow rate (Aw) is represented in the following expression:
Aw = m(1 + Xa)Ao (kg/kg) or
Aw’ = m(1+1.61Xa)Ao’ (Nm3/kg)
The actual dry gas flow rate (Gd) and wet gas flow rate (Gw) are obtained from the following expression:
Gd = Gdo + (m-1) (cid:121) Ado (kg/kg) or
Gd’ = Gdo’ + (m-1) (cid:121) Ado’ (Nm3/kg)
Gw = Gd + Wf + m (cid:121) Wa (kg/kg) or
Gw’ = Gd’ + Wf’ m (cid:121) Wa’ (Nm3/kg)
2. Exhaust gas component
As aforementioned, if O 1mol is supplied to C 1mol, CO 1mol is generated. However, if air is supplied,
2 2
exhaust gas consisting of 21% of CO and 79% of N generates if C is completely burned because the air
2 2
consists of 21% of O and 79% of N (volume ratio). Thus, if the fuel is C alone, the upper limit of CO in
2 2 2
the exhaust gas becomes 21% theoretically.
However, in fuel combustion, the exhaust gas component increases while the ratio of CO is relatively
2
smaller due to the other components (S, N, etc) or the excess air flow rate (O , N ). In this case, the
2 2
theoretical CO content ratio (CO max) and the actual CO content ratio are obtained by the following
2 2 2
expression. Here, CO is 0, and also what has been taken into account in the actual gas analysis (liquid
absorption method) is that SO gas is absorbed together with CO and quantified.
2 2
CO = (1.867C + 0.69S)/Gdo’ × 100 (dry vol%)
2max
CO = (1.867C + 0.69S)/Gdo’ × 100 (dry vol%)
2
Also, the other composition in the actual burning gas is obtained from the following expression:
O = 21(m-1)Ado’/Gd’ (dry vol%)
2
N = (0.8N + 0.79m (cid:121) Ado’)/Gd’×100 (dry vol%)
2
112

H O = (Gw’-Gd’)/Gw’×100 (wet vol%)
2
2.6.2.3 Generation Mechanism of Nitrogen Oxide
As shown in previous Fig. 1, the pulverized coal burning area is divided into the primary combustion area,
where coal volatile matter is burned, and the secondary combustion areas, where mainly chars are burned. Each
area contains Thermal NOx (NOx which is defined in the Zeldvich mechanism), Prompt NOx (NOx, which is
oxidized after airborne nitrogen combines with hydrocarbon to become NHi compound, and then generates), and
Fuel NOx (NOx which generates by the oxidization of N in fuel). These NOx, which generate in the above
mentioned areas, have the potential to become an NHi compound and to be partially reduced to N under the
2
intervention of hydrocarbon in the insufficient oxygen area at the rear of the combustion area.
113
)noisrevnoc
fad
:%(
tnetnoc
N
Australian G
coal
Japanese A
coal
Chinese D coal
Raw
coal
Reactor temperature (°C)
Fig. 6 Relation between the residual nitrogen content in chars and the primary reactor temperature
Symbol
Base condition
Coal Japanese A coalChinese D coal
Air ratio in the primary reactor = 0.41
Residual O = 3%
2
Reactor temperature (%)
Fig. 7 Relation between NOx generation amount and reactor temperature
Reactor temperature = 1,350°C South African
Air ratio in the primary reactor= coal
0.41 O1.56%N
Residual O2 =3%
Japanese B
coal
1.1%N Canadian F
coal
Chinese D 1.03%N
Australian coal
Japanese A C coal 0.85%N
coal 1.59%N
1.09%N
Fuel ratio (-)

Fig. 8 Relation between NOx generation amount and coal properties
Japanese A coal
Residual O2 = 3%
Secondary reactor temperature =
1,350°C
Air ratio in the primary reactor =
0.41
Primary reactor temperature (°C)
Fig. 9 Relation between Nox generation amount and primary reactor temperature
Thus, the NOx generation characteristic of coal fuel, which includes much organic nitrogen, has an extremely
complex reaction pattern compared with conventional gas or oil fuel. In this section, we will consider the NOx
generation mechanism of fundamental pulverized-coal in the reactor pipe.
First, Fig. 6 shows the volatile matter of organic nitrogen included in coal and its content ratio to char.
According to this Fig., the organic nitrogen ratio included in carbonized char is almost the same as that in raw
coal. This means that both the volatile matter in coal and the char include organic nitrogen almost evenly. Also,
the following shows the investigation result of NOx generation characteristics when pulverized coal is burned in
the primary- and secondary combustion areas separately with two electric-heating-type magnetic reactive pipes
connected by a quartz joint.
Figure 7 shows the comparison of NOx generation amounts in these areas by using (Ar+O ) and (N +O ) as
2 2 2
combustion carrier gas.
This difference in both areas can be considered to be Thermal NOx (Prompt NOx is included). From the figure,
it is considered that almost all generation is accounted for by Fuel NOx when the reactor temperature is below
1400°C while 25-30% is accounted for by Thermal NOx when the reactor temperature is 1600°C.
Figure 8 shows the comparison of NOx generation amounts when the type of coal is changed under the
primary- and secondary reactorsʼ temperature of 1350°C.
The relation between the type of coal and the NOx generation amount cannot be determined by the organic
nitrogen content alone in coal. Rather, it seems to be more understandable by the fuel ratio.
Figure 9 shows the relation between the primary reactor temperature and the NOx generation amount, where
the primary reactor air ratio is set to 0.41.
According to this figure, in the volatile matter burning area of the primary reactor, the higher the reactor
temperature, the lower the NOx generation amount. This phenomenon is seen only in an air-short reductive
atmosphere. Because, generally, the higher the temperature, the greater the volatile amount of carbon hydride and
organic nitrogen in coal, it is considered that when the actual air ratio in the burning area of the primary reactor
further decreases, the NOx generation amount will be lowered.
Japanese A coal
Residual O2 = 3%
Secondary reactor temperature =
1,350°C
Air ratio in the primary reactor =
0.41
Retention time (S) in primary reactor
Fig. 10 Relation between Nox generation amount and retention time in primary reactor
114

Symbo
l
Coal Japanese A Char
coal
Residual O2 = 3%
Reactor temperature = 1,350°C
Air ratio (-) in primary reactor
Fig. 11 Comparison of NOx generation amounts between coal and char
Figure 10 shows the variation of the NOx generation amount by setting the air ratio in the primary reactor to
0.41.
According to this, the longer the coal retention time in the volatile matter burning area of the primary reactor,
the lower the NOx generation amount. This is likely because the organic nitrogen gas (NH , HCN) etc. generated
3
in the air-short volatile matter burning area is partially reduced to N due to the existence of unburned gas.
2
Figure 11 shows the relation between the NOx generation amount and the air ratio in the primary reactor.
According to this, the NOx generation amount is largely changed by the air ratio in the primary reactor.
2.6.3 Pulverized Coal Combustion Equipment
The pulverized coal combustion equipment mainly consists of a stoker, coal pulverizer (mill), pulverized-coal
pipe, pulverized-coal burner and furnace (these are fuel supply- and combustion equipment behind the bunker);
and of a primary draft fan (PAF) and air preheater (AH) (these are primary draft equipment).
The above equipments are described below:
2.6.3.1 Pulverized Coal Burning Method
The pulverized coal burning method generally employed is classified into two types: (1) according to the burner
arrangement and (2) according to the method of pulverized coal feed (direct/indirect).
(1) Classification according to burner arrangement
The combustion method is classified into the following according to the relation between the furnace and the
burner arrangement.
Figure 12 shows the combustion method according to the burner arrangement.
(1) Front firing (2) Opposed (3) Tangential (4) Vertical
firing firing firing
Fig. 12 Combustion methods according to burner arrangement
1. Horizontal firing (horizontal combustion)
The method, where burners are placed at the front or rear of the furnace wall, is called a front firing or rear
firing method, while the method, where burners are placed at both the front and rear sides of the walls, is
115
)edis
laretaL(
)edis
ecafruS(
)edis
tnorF(
)edis
laretaL(

called an opposed firing method. In these methods, circling motions are given to combustion air to shorten
flames and the fuel and air are circulated and mixed, thereby forming high temperature flames.
2. Tangential corner firing
In this method, burners are placed at the four corners of the furnace, from which pulverized coal and air
are injected tangentially into a virtual circle in the center of the furnace. Each burner independently forms a
flame while the entire flame is swirling slowly in the furnace to form a single flame (fireball), featuring a
long flame trajectory and slow combustion.
Stack
Desulfurization
equipment
Regenerative
preheater Induced draft fan
Electric dust
collector
Forced draft fan
Bunker
Steam air preheater
Secondary air
Stoker
Primary draft fan
Coal Coal pulverizer
Seal air fan
pulverizer
Fig. 13 Direct combustion method
Primary air
3. Vertical firing (vertical combustion)
Burners are installed downward from the ceiling of the lower furnace, where pulverized coal and air are
injected downward once, but the flames flow upward while burning. Since the frame trajectory adopts a
U-shape, it is also called U-firing. In this method, because the combustion time can be longer and the
radiation from flames is received at the burner, the burner’s heat load becomes larger, and because the
pulverized coal injection speed can be lowered, the combustibility and ignitability are better. This is
generally suitable for coal such as anthracite whose combustibility is poor.
(2) Classification According to Pulverized Coal Feed Method
The pulverized coal burning system is classified into the following according to the difference in pulverized
coal feed methods:
(1) Direct combustion method (direct system)
(2) Storing combustion method (bin system)
The direct combustion system, which has had rich achievements, has generally been employed as a standard of
boilers for bituminous coal with high volatile matter.
On the other hand, the bin system has been employed since long ago for the purpose of combustion
improvement in boilers for anthracite coal with low volatile matter of approx. 15% or less. Each method has the
following characteristics:
1. System of combustion method
In the case of the direct combustion method (Fig.13), coal from the bunker is flow-controlled and fed to
the mill by the stoker. Next, the pulverized coal, which has been ground in the mill and dried, is directly
transferred and fed to the burner by the primary air through the pulverized-coal pipe. Hence, the fuel
system and arrangement after the mill are simple.
Though, in the case of the bin system there are various patterns, this example (Fig.14) shows the system
which uses exhaust gas for transferring and drying pulverized coal in the mill.
The bin system is fundamentally different from the direct combustion method in terms of the system after
the mill, and is more or less complex, having more devices. To dry pulverized coal in the mill, combusted
exhaust-gases taken from the entrance and exit of the air preheater are utilized, and each amount of the
116

gases is adjusted so that they reach the necessary temperature at the mill entrance.
The gas-mixed pulverized coal from the mill is separated into pulverized coal and exhaust gas when it
passes through the cyclone (primary) and the bag filter (secondary). The pulverized coal captured here is
stored in the bin while the exhaust gas is returned to the air preheater exit by the exhaust fan.
The pulverized coal is transferred by the pulverized-coal stoker from the bin to the burner entrance, where
it is blended with the primary air and fed into the burner.
2. Operability
In the direct combustion method, the mill operation and burner operation are directly interlocked, and the
load operation is restricted both by the mill operation (the minimum mill load and the dynamics including
mill startup) and by the combustibility at the burner.
Bag filter
Bunker
Stack
117
enolcyC noitazirufluseD
tnempiuqe
Exhaust fan
Stoker
Screw conveyor
Induced draft
Coal fan
pulverizer
Regenerative
Pulverized-coal Electric dust
air preheater
bin collector
Stoker Forced draft facfan
Steam air preheater
Primary draft fan
Distributor Secondary air
Fig. 14 Bin system for pulverized coal
Primary air
In the bin system, coal grinding and drying in the mill and combustion at the burner can be separated, so
there is no operation restriction by the mill in terms of the load operation, but the combustion alone at the
burner is restricted. This is a little more advantageous than the direct combustion method.
3. Combustibility
In the direct combustion method, when a mill load is low, the air/fuel ratio becomes larger as the load is
lowered, thereby combustibility is apt to worsen.
In the bin system, as aforementioned, grinding and drying in the mill and the pulverized coal input to the
burner can be independently operated (however, within the bin’s capacity), and the coal moisture
evaporated in the mill is discharged outside the system. Therefore, the burner can ensure the optimal, dried
primary air/ratio with high to low load. This is especially much better for combustibility with a low load
than in the direct combustion method. However, the direct combustion method can also maintain
combustibility equivalent to that in the bin system by employing a high turndown burner (where an
air-pulverized coal mixture is separated into thick and thin types to burn).
4. Maintainability
In the direct combustion method, the greater the number of mills, the more frequent the maintenance and
services of the mills, but it is possible to schedule the intervals of maintenance and services by installing
backup mills.
In the bin system, the mill’s maintenance and services become easier because the number of mills can be
reduced. And mills can be halted for a short time (depending on the bin capacity), during which
maintenance is possible. However, the frequency of maintenance and services for other devices (a cyclone,
bag filter, exhaust fan, etc) increases.
5. Safety
In the direct combustion method, special safety measures are not needed because there is no pulverized

coal storage, whereas in the bin system, strict safety measures (sealing the bin by inert gas, installing
electrostatic, explosion-proof-type explosion doors, enhancing monitor systems, arranging fire
extinguishing equipment, etc.) are required in order to prevent pulverized coal in the bin from sparking and
exploding.
2.6.3.2 Furnace
Furnaces must fulfill certain functions: to convert the chemical energy of fuel into thermal energy effectively,
that is to say, to have combustion equipment (a chamber) to burn fuel completely; and to let the internal can-water
absorb generated heat through the surrounding water pipes. For these purposes, furnaces must be equipped with
the proper type and quantity of burners according to the fuel, and have the appropriate shape and space to
completely burn fuel, as well as the structure to withstand the thermal load.
Typical
bituminous coal Heavy oil
Gas
Fig. 15 Conceptual comparison of fuel and furnace size
Especially, because the coal (pulverized coal) combustibility is fairly inferior to that of other fuels (heavy oil,
gas, etc.), a larger sized chamber (furnace) is required. The furnace size must be selected by taking into account
the combustibility and also the slagging characteristic of coal (ash adherence to the furnace).
Figure 15 shows the comparison between the type of fuel and furnace size.
As shown in the comparison between the type of coal (coal rank) and furnace size in Fig. 16, the furnace size
varies largely with the type of coal. The difference in some furnaces is larger than that in fuels (typical bituminous
coal and heavy oil).
For recent furnace walls, a welded wall structure, where both pipes are welded by a fin or a weld metal to
ensure air tightness of the furnace, has been employed to decrease heat losses and repair costs.
2.6.3.3 Pulverized Coal Burner
The coal combustion method generally employed is mainly classified into two types: the grate-type combustion
method in which coal is not ground; and the burner combustion method in which coal is pulverized into minute
grains by the coal pulverizer and float-fired in the air.
Though the former features relatively less power consumption and less flying ash, it is not suitable as
combustion equipment for large capacity boilers.
On the other hand, the latter uses pulverized-coal burners to feed pulverized coal into the furnace and burn it.
Compared with the grate-type combustion method, this has many advantages: (1) excess air is less and the
combustion efficiency is high, (2) adjustment of load and combustion is easier and ignition and extinguishing time
is shorter, (3) automatic control is easier, and (4) combustion by mixing with liquid- or gas fuel is easier.
118

B v i w t o u i l t a m h t i i l n m e o e m u d s a i u t c t m o e a r l S v e c o o m l a a i- l t b i w le it i u t m h m a h in t ig t o e h u r s w B i r t o h w lo n w c o N a a l w B it r h o w m
N
n
a
e c d o iu a m l w B it r h o w H n ig c h o N al a
Fig. 16 Conceptual comparison of coal rank and furnace size
In the pulverized coal burner, a premixed airflow of both the pulverized coal ground by the pulverizer and the
primary air is injected into the furnace through a boxy or cylindrical nozzle, and from the vicinity of this nozzle,
the secondary air heated by the air preheater is blown in. The pulverized coal, which has been injected together
with the primary air, diffuses rapidly while slowing the speed after coming out of the nozzle, and is ignited and
burned while mixing with the secondary air from the outside by receiving radiant heat from the high-temperature
furnace wall and flames. The flow rate of the mixed gas of pulverized coal and primary air is set by taking into
account the flame velocity and the pulverized coal settling velocity.
Figures 17-19 show the structures of typical pulverized coal burners. The burners in Figs. 17 and 18 have been
designed so that the rotating device gives rotating motions to the mixed gas of pulverized coal and primary air.
The pulverized coal burner in Fig. 19, called a tangential tilting burner, has been designed so that the nozzle of
the burner tip moves up and down each at the angle of approx. 30 degrees to adjust steam temperature.
Either burner is usually equipped with an ignition burner in the center or the side.
The pulverized coal burner requires maintenance because the tip is especially apt to be deformed and damaged
by receiving radiant heat in the furnace and vulnerable to abrasion by pulverized coal. Therefore, recently new
techniques have been developed for durability improvement, such as lining the burner with material (made into a
tile form) - ceramic etc. with high heat and abrasion resistance -, or flame-spray coating the surface. Some of them
have been practically used.
Air adjustment handle
119
edortcelE
Ignition burner
Air cylinder
Transformer
rellepmI
Air cylinder
Heavy oil burner
laoc
dezirevluP renrub
Pulverized coal
entrance
Air register (circular type)
Inspection window
Fig. 17 Circular burner
In addition to the abovementioned durability, the following functions are required for pulverized coal burners:
(1) Low NOx combustibility
(2) High turndown
The background is: nowadays we must comply with strict environmental regulations; our country has been
importing coal from all over the world, hence we must deal with such various properties of foreign coal; the need
for coal-fired power as intermediate-load thermal power has been rising because nuclear power generation has
recently increased and the difference between the day and night power demands has increased.
Next, a representative low NOx burner is described below:

Figure 20 shows the structure of a DF inter-vane pulverized coal burner.
The secondary air is supplied toward the burner throat through two independent channels so that flames are
stabilized and the mixture of fuel and secondary air can be adjusted. The circular nozzle, from which fuel is
injected, consists of an outer casing and a combustion liner. Each end of the nozzle is narrowed down so that the
fuel concentrates on the center of the axis. The end of the combustion liner can be moved toward the axis, thereby
adjusting the mixture of fuel and secondary air.
Figure 21 shows the structure of the NR burner.
The pulverized-coal nozzle is placed in the center of the burner. On the concentric circle of the outer periphery,
a cylindrical nozzle is mounted to supply inner-peripheral burning-air. Furthermore, outside of this, a
burning-air-rotating device is installed to adjust outer-peripheral burning-air. Around the periphery of the
pulverized-coal nozzle tip, a ceramic-made flame-stabilizer ring is mounted so that minute vortices can be
generated in the pulverized coal flow, enabling quick ignition of the pulverized coal, and stabilizing
high-temperature reduction flames of excess fuel.
Shroud ring
Pulverized-coal
outer casing
Pulverized-coal
combustion liner
Oil burner
Tertiary damper
Front Vane support
plate plate
Vane
Tertiary air pipe
Fig. 18 Inter-vane type burner
Secondary air
(heavy oil burner)
Pulverized coal +
primary air
Secondary air
(heavy oil burner)
Fig. 19 Tangential tilting burner
Figure 22 shows a pulverized coal PM burner.
This burner utilizes the characteristic that NOx generating during pulverized-coal combustion decreases at both
the thick/thin pulverized-coal density sides after the primary air/coal weight ratio reaches 3-4. That is to say, by
installing a distributor at the burner entrance, the air-fuel mixture, whose usual primary-air/coal weight ratio is 2-3,
is divided into the higher and lower mixtures of the pulverized coal density, and is fed into the furnace through
separate nozzles and burned so that NOx becomes lowest.
The high-turndown burner, in principle, divides the air-fuel mixture of pulverized coal into thick and thin
120

mixtures. Though with common burners, the pulverized coal density becomes lower and the ignition stability
worsens when the burner load is lower, this high-turndown burner maintains better ignition stability with this thick
mixture even when the burner load is low.
Primary air + pulverized coal
Burner tile cooling air
Separate plate
Combustion liner Moving
driving device combustion Flow divider
Heavy oil entrance liner
Pitot tube
Primary air + pulverized coal
Combustion Heavy oil burner
liner Inner secondary air
Purge air connection inlet Outer secondary air
Outer
Secondary-air vane casing
opening/closing device Inner-vane
Furnace front
Tertiary air damper Heat sealed plate wall and furnace
wall pipe
Secondary-air vane
Inner-vane opening/closing device
Secondary air
Tertiary air pipe
Pulverized coal entrance manifold
Heat pipe
Fig. 20 DF inter-vane pulverized coal burner
Figures 23 and 24 show high-turndown burners. The aforementioned PM is also a high-turndown burner.
The burner in Fig. 23 is called a split burner. The burner body has a diaphragm and the nozzle tip has a deflector.
When a primary-air-fuel mixture flows through the bend section of the burner entrance, the high mixture (bend
outer-periphery side) and the low mixture (inner-periphery side) of the pulverized coal density are divided by the
centrifugal force of the pulverized coal.
Pilot torch High-performance
combustion-air circling path
Flame stabilizing
ring
(with ceramic parts)
Guide sleeve
Pulverized coal + Inner-periphery Outer-periphery
primary air combustion air combustion air
Fig. 21 NR burner
121

Fig. 22
Pulverized coal PM
burner
Burner front side Burner side face Variable separator
Coal nozzle tip Horizontal diaphragm
Seal plate Coal nozzle
Entrance
elbow
Thick mixture
Thin mixture No kicker
block
Fig. 23 Split burner
122

Pulverized coal entrance
(primary air)
(1)
High load position
Low load position
Low load position
High load
position
(2) (3)
(6)
(5)
(4)
(7)
(9)
(8)
Tertiary air Secondary air
(1) Split damper (2) Traverse-mounted cyclone (3)Cyclone
exit damper (4) Pilot torch (5) Swirler (6) Burner nozzle (7)Oil
burner (8) Tertiary damper (9) Low load nozzle
Fig. 24 Wide-range burner
In the wide-range burner in Fig.24, the traverse-mounted separator on the burner entrance separates the
pulverized coal flow into high-density and low-density.
Mill outlet damper
Classifier
Oil pressure
load equipment
Separator body
Separator
Body liner
Roll
Pull ring
segment
Fig. 25 Bowl mill
2.6.3.4 Coal Pulverizer (hereafter referred to as mill)
The coal pulverizer is the most important equipment to govern the operability and reliability of coal burning
boilers. Therefore, an optimum mill type must be selected from the comprehensive viewpoint according to the
coal properties and the operation conditions. The mills are classified broadly according to the grinding method,
structure, and draft method. As far as the mills used in thermal power stations are concerned, they can be
classified into the following:
(1) Upright mill
123

(2) Hammer mill and beater wheel mill
Upright mills are suitable for bituminous coal, semi-bituminous coal and part of brown coal; tube mills and
beater wheel mills are used for high-ash content coal; and hammer mills are used for high-moisture brown coal.
Nowadays, domestic coal burning boilers mainly use an upright mill for the following reasons:
1) It can be used for broad types of coal and is suitable for bituminous and semi-bituminous coal burned in
domestic boilers.
2) It needs low consumption power.
3) It is easy to adjust the pulverization degree and start/stop, and excellent in load responsiveness.
4) Necessary floor space is smaller and noise is smaller.
(1) Upright Mill
1. Structure
Figures 25-29 show the structures of various types of upright mills.
The upright mills mainly consist of a reducer section, grinding and drying section, and coarse grain separator
section.
Raw coal (1)
Pulverized coal
(2)
(3)
(4)
(5)
(6)
(7)
Hot air
entrance
(1) Pulverized-coal pipe (2) Vane driving equipment
(3) Coarse-grain separator vane (4) Reject shoot
(5) Stoker pipe (6) Grinding roller (three pieces)
(7) Roller pressurizer (8) Air port ring
(9) Table segment (10) Grinding table
(11) Foreign substance discharge scraper
(12) Foreign substance discharge hole (13)Reducer
Fig. 26 Upright MBF mill: drawing of whole assembly
Coal, which is fed from the stoker through the stoker pipe positioned in the center of the mill, falls into the
rotating bowl (table), and is spread by centrifugal force, forming a coal layer. This coal layer is inserted between
the roll and the segment liner on the bowl (table), and ground by the roll with the grinding load applied to the roll
by the loading device.
The pulverized coal is blown up by hot air, which is fed by the periphery of the grinding section, and classified
by the upper classifier while being dried. There are two types of classifiers: a fixed type cyclone separator and a
rotary separator. Nowadays, the rotary separator (Fig. 29) is often used because of high combustion efficiency and
energy saving. This provides a high pulverization degree of more than 90% by 200-mesh passing.
The foreign substances and pyrite mixed in coal fall from the air blow section to beneath the bowl, and are
discharged by the scraper into the pyrite hopper through the pyrite discharge pipe.
124

Coal
entrance
Primary air
inlet
Supply
and drain
wa ter
Fig. 27 Cross-sectional view of large scale E mill
Mill exit stop-valve
Stoker pipe entrance section
Mill upper
housing
Coarse grain
Sealing air piping
separator
(classifier)
Upper-housing
disassembling
support leg
Loading rod
seal Spring frame
Pressure frame Grinding Spring
Loading rod -roller Mill intermediate
ring seat housing
cover
Grinding ring
Throat ring
Lower housing Ring seat
Pyrite Yoke Primary air inlet
blow
Pyrite box
Yoke
seal air Gear box
Pressure
cylinder
Fig. 28
Nowadays, coal burning boilers have often employed pressure mills whose abrasive exhausters need not be
repaired. For these mills, seal air is supplied to prevent pulverized coal leak. Also as a measure to prevent coal
blockage in the stoker pipe, a rotary-type pipe is mounted.
125

Raw coal
Stoker pipe
Classifier driving
equipment
Outlet port
Rotary type classifier
Hydraulic
loading device Hot-air inlet
duct
Pull ring
segment
Bowl
Fig. 29 MRS type bowl mill
2. Operation and maintenance
The operation of upright mills is simple and start/stop operation can be completely automated.
Also, the wide range of the mill operation load adjustment is important for coal boiler operability.
The upright mill is available for 40-50% turndown, but recently some types of upright mills have become
available for high-turndown operation up to 30% or less.
For mills operation, the maintenance of abrasive parts is also extremely important. So, studies have been
conducted to develop abrasion-resistant materials and to simplify the replacement of roll rings, liners, etc. As for
the material of rolls, in addition to conventional abrasion-resistant cast iron, curing cladding-welding material
with several times abrasion-resistance of cast iron has also been used.
Because the life of the grinding section varies with the coal properties and the operation conditions, etc, it is
necessary to measure periodically the abrasion depth of the rolls or segments of each plant and to schedule the
intervals of replacement. Generally, rolls/rings/liners replacement is conducted in such a manner that one unit of
extra mill per boiler is installed, and maintenance intervals are set, and each mill is maintained sequentially.
Fig. 30 Tube mill
126

Fig. 31 Structure of horizontal-type bowl mill
Pulverized coal + gas mixture
Hot gas + coal
Pulverizer housing
Pulverizer wheel
Hot air (for sealing)
Coal pulverizer
gate mill gage Abrasion-resistant
plate
Primary grinder
Bearing Driving machine
Fig.32 Beater wheel mill
(2) Hammer mill and beater wheel mill
The hammer mill is a machine that smashes coal with the beating impacts of many hammers or heads rotated at
high-speed. This is used for inferior coal (high moisture coal, brown coal) or to grind coal coarsely. (Fig.32)
Many hammer mills have been used for brown-coal burning boilers in Europe and Australia, but our country
has no application example.
2.6.3.5 Stoker
The stoker is equipment which plays an essential role to determine the combustion rate corresponding to the
load variation and maintain the optimum air/fuel ratio in the coal combustion system.
The most important point when selecting a stoker is that it feeds the correct amount of coal into the pulverizer
from the bunker or silo smoothly and uniformly according to the fuel demand signals.
The following are the types and characteristics of stokers commonly used for pulverized coal boilers.
(1) Belt-type volumetric feeder
This stoker, using rubber belts, has a stable feeding capacity because coal is cut out equally in width and height.
With little interruption of coal feeding and good maintainability, this is generally used for pulverized coal
combustion equipment. Since this is a volume-control type, the coal weight sometimes varies according to the
coal density variation.
127

(2) Belt-type gravimetric feeder
Figure 33 shows the structure of the belt-type gravimetric feeder.
This is a belt-type stoker equipped with a measuring mechanism with a load cell. Because the fuel demand can
be met based on the coal weight and the feeding is exact and stable, the fuel variation caused by the coal density is
compensated.
Thus, because the fuel is correctly controlled and the weight and flow measurements are highly accurate and
maintainability is also excellent, this is suitable for sophisticated plant control with a calculator.
2.6.3.6 Primary Draft Equipment
In the direct combustion method, the primary air is used for not only burning pulverized coal, but also drying
and transferring it to the burner in the mill.
In the primary draft system, the primary draft fan (PAF) is placed in two methods relative to the air preheater
(AH) according to the air temperature: a Cold Primary Air Fan method (PAF is installed upstream of the AH,
dealing with cold air) and a Hot Primary Air Fan method (PAF is installed downstream of the AH in the upstream
of the mill, dealing with hot air).
Figure 34 shows the comparison among these circuits.
(1) Comparison between Cold PAF and Hot PAF methods
1. PAF capacity
Cold PAF has a capacity to deal with a primary air flow rate of all mills by one to two PAFs (depending on the
number of draft circuits) regardless of the number of mills.
Fig. 33 Belt-type gravimetric feeder
128
ecnartne
laoC
)reknub
morf(
Downspout
Dresser coupling Measuring span roller
Measuring module
Puddle switch for on-belt coal
Entrance door
Measuring shortage monitor
End plate E (fi n x t e ra d n t c y e p e g ) a te roller Head pulley Illuminating lamp
Measuring span
Exit door
Belt scraper
tixe
laoC
)llim
ot(
Cell preening Cleaning conveyor take-up pulley Support roller Tension pulley Cleaning-conveyor
Seal air manifold chain sprocket Cleaning conveyor
Belt take-up adjust screw chain take-up
On the other hand, Hot PAF is installed in the one PAF - one mill base and the capacity is one mill’s worth of
the primary air amount, so the same number of units as that of mills is required.
Comparing the total capacities (power) of each method, the Hot PAF method, which deals with hot air, has
larger capacity.
2. AH type
In the Cold PAF method, the air pressure in the primary air circuit is higher than that in the secondary air circuit,
so the AH flow path must be divided into two: for the primary and for the secondary.
The AH is mainly classified into two: an integrated type and a separate type, as shown in Fig. 35. For common
pulverized coal burning boilers, the integrated AH type is often employed because the duct and AH placement
become simpler and the necessary space is smaller.
In the Hot PAF method, the air pressure in the primary air circuit is lower than that in the secondary circuit, so
the AH flow path need not be separated for the primary and the secondary. Figure 34 shows a standard type of AH,
through which the total air flow rate of the primary and secondary air circuits passes AH and then the primary hot
air diverges to be absorbed by PAF.

3. Operation power
Cold PAF method Hot PAF method
Mill Mill
Control
Control
damper
damper
129
ria
dloc
yramirP
Fig. 34 Comparison of PAF systems
When operated with high load using many mills, the Cold PAF method has high fan efficiency because fewer
PAFs deal with the primary air flow rate necessary for the operation of all moving mills, and the power
consumption is smaller than that of Hot PAF since cold air is dealt with.
On the contrary, when operated with low load using fewer mills, the Hot PAF method consumes smaller power
in total than that of the Cold PAF method (if the Cold PAF efficiency drops notably with low load) because the
idling mill’s PAFs can be stopped and the fan efficiency of the moving PAFs is as high as that during high load
operation with the high mill load.
4. Operability
Fig. 35 Comparison of AH types in Cold PAF method
When the mill load and moisture in coal are changed, the necessary temperature at the mill entrance is changed.
The Hot PAF is affected directly by this temperature change and its operation point changes. However, the Cold
PAF is always constant in cold air. Even when necessary temperature at the mill entrance is changed (a change in
the ratio of hot air to cold air), the Cold PAF is less affected by air volume and air pressure fluctuation, and easily
controlled.
riatohyramirP ria
yradnoceS noitsubmoC
sag
ria dloc
yramirP
toh
yramirP ria
ria
yradnoceS noitsubmoC
sag
Integrated type
Separate type
Twin flow type Tri-sector type
System
From boiler From boiler From boiler
To mill To To
To boiler mill To boiler mill
To boiler
Inner Outer Three- way split
periphery periphery
From FDF
From From From From From
PAF FDF PAF FDF PAF
From IDF From IDF From IDF
Secondary air
Secondary air
Gas
Gas
Gas
Secondary Gas
Gas air
Gas
Primary air Gas
Primary air Primary air
Primary air Distribution adjustment of gas flow Distribution adjustment of gas flow Positive-and inverse rotations
temperature rate to primary- and secondary AHs rate to primary- and secondary air are available and large change
control can be available sides can be available alone is possible
Duct work Slightly complex Relatively simple Relatively simple
Construction cost, power
cost and air leak amount Almost same

5. Economic efficiency
As for equipment cost, AH is higher and PAF is lower in the Cold PAF method than in the Hot PAF method, but
these cannot simply be compared because, as a matter of fact, they largely vary with equipment arrangement, duct
work, etc. As for operation power, the efficiency is reversed depending on the operation load area, as
aforementioned, so it is necessary to estimate the economic effect comprehensively, including operation patterns,
to decide the path to be taken.
Generally speaking, high-capacity, exclusive coal-combustion boilers often employ the Cold PAF method while
small-capacity boilers with fewer mills or co-combustion boilers often employ the Hot PAF method.
(2) PAF placement and type
In the Cold PAF method, there are two ways to place PAF: in series with FDF or in parallel with FDF. The
comparison between them is shown in Table 4.
Regarding the PAF types, a centrifugal type has traditionally been used because the air pressure required by
PAF is high and flat across the entire area as shown in Fig. 36 and because the conventional axial-flow fans could
not be enlarged or improved in performance to prevent surging.
Nowadays, the axial-flow fans have been improved against surging characteristics, and some of them have been
provided with a casing treatment suitable for the rotating-blade tips to enhance the fan efficiency.
2.6.3.7 Bunker
The design of bunkers must be fully considered so that they do not cause coal retention or blockage because
such bunker problems are crucial issues causing a load decrease or unit trip in the power stations.
(1) Design of bunker
1. Capacity
The bunker capacity is determined by the following expressions:
The coal amount stored within an available feeding time is:
QT
Vc=
γ
Vc
Hence, the bunker capacity becomes V =
(η/100)
However, V: bunker capacity (m3)
Vc: storage capacity (m3)
Q: feeding capacity (conveyor capacity) (t/h)
T: available feeding time (h)
γ: coal volume specific gravity (foreign coal generally has approx. 0.8) (t/m3)
η: volumetric efficiency (the ratio of storage capacity to bunker capacity is generally 0.6-1.0)
(%)
Table 4 Comparison between PAF layouts
System type PAF-FDF series configuration PAF/FDF parallel configuration
System structure
Boiler Mill Boiler Mill
FDF air flow rate is larger but PAF air FDF air flow rate decreases by the
pressure decreases by the amount of amount of PAF air flow rate compared
Fundamental characteristics
FDF discharged air pressure compared with the method described at left.
with the method described at right.
The method with a higher economic effect should be employed by taking into
account the characteristics of primary- and secondary air flow rates and air
Selection criterion
pressure required by the pulverized coal combustion equipment as well as the
characteristics of fans (varies with the types).
130

2. Bunker shape
Generally, there are two types of bunkers: a conical shape and a pyramidal shape. They are almost the same in
flow characteristics in a bunker, but the conical shape is excellent in the space-occupation rate while the pyramidal
shape is excellent in strength.
3. Inclination angle of hopper wall face
In order for coal to assume an arch shape and not to cause blockage in the bunker, the arch bending moment
must be large. Because the arch bending moment is proportional to the squared distance between the fulcrums and
to the load applied to the arch, the cross-sectional area of the exit and the inclination angle of the wall face must
be more or less large. Generally, an angle of more than 70 degrees has been employed.
Characteristic of
conventional type PAF
(large type)
Fig. 36 PAF characteristic improvement provided with casing treatment
4. Bunker exit
Though the bunker exit is restricted by the diameter of the downspout or the stoker, the larger the bunker exit,
the better blockage prevention. There is a method to enlarge the cross-sectional area of the main bunker exit by
installing a sub-bunker under the bunker.
5. Material
Almost all bunkers are made of steel plates. The bunker exit, where blockage is most apt to occur, is usually
provided with a lining of high corrosion resistant stainless steel or polymeric synthetic resin. Also, Gunite is
sometimes used as a lining material on the vertical section by taking into account the resistance to abrasion.
Fig. 37 Plug flow and mass flow
(2) Flow form and the determination factors
There are two types of coal flow forms: a plug flow (core flow) and a mass flow.
In the plug flow, as shown in Fig.37, the coal near the bunker wall does not move but the coal in or around the
center only flows out. On the contrary, in the mass flow, the coal in the bunker gradually flows out from the lower
position of the bunker.
131
)OHmm(
H
erusserp
riA
2
(With casing
treatment)
Improved
type
Necessary Q-H characteristic
Conventional type PAF (without casing treatment)
Air flow rate Q (m3/min.)
Adhesive coal
Non adhesive
coal
Plug flow Mass flow
(core flow)

Therefore, the mass flow does not retain coal for a long time in the bunker, but the plug flow always retains
coal in the lower position in the bunker.
The flow form is mainly determined by the following factors:
1. Type of coal
Adhesive coal is apt to take the plug flow pattern, causing blockage.
2. Inclination angle of hopper wall face
It is confirmed by the experiments that if the inclination angle of the wall face exceeds 65-70 degrees, the
flow separates into a mass flow and a plug flow.
3. Material for bunker inner face
When corrosion-prone material, such as steel plates, is used for a bunker inner face, corroded portions cause
an adherence phenomenon, resulting in the retention or blockage of coal. Hence, corrosion resistant material is
usually used: the inner face is often provided with a lining of high corrosion resistant stainless steel or
polymeric synthetic resin to prevent corrosion.
(3) Coal properties and blockage
1. Repose angle
The larger the coal grains the more often blockage occurs. The coal flow is affected by grain size distribution,
ash and clay contents and moisture as mentioned below (Fig. 38).
132
elgna
esopeR
)eerged(
rep
etar-wolf
egrahcsid
reknuB
)s3mkg(
tixe
eht
fo
aera
lanoitces-ssorc
Moisture (%) Repose angle (degree)
Fig. 38 Repose angle and blockage
2. Grain size distribution
The finer the grains, the more blockage is apt to occur, though slightly different according to the moisture
content.
3. Ash and clay contents
Ash and clay contents are no problem if their surface moisture is slight. But if it is large, adherence occurs,
resulting in blockage.
4. Moisture
Moisture (especially surface moisture) is a crucial factor. The smaller the grain, the larger the influence, and
10-15% moisture has the highest possibility of causing blockage. However, when exceeding this rate, on the
contrary, adhesiveness decreases. This means that when moisture is slight, it exists as a film over a grain surface,
causing surface friction among coal grains, whereas when moisture increases, this film breaks, developing
lubricating action.
(4) Blockage prevention measures
As aforementioned, blockage can be significantly prevented by bunker specifications by considering the coal
flow- and hopper discharge characteristics, but the following methods are also effective for blockage:
(1) Blending coal
(2) Installing a corner plate
(3) Providing a poking hole and a hammering seat
(4) Installing an air-blaster
(5) Installing a vibrator

2.7 Examples for the Operation of Soot Blowers
Reduction of Steam Volume by Revising the Operation of
Low Load Soot Blowers in Tsuruga Thermal Power Plant
The Sun
Shift C
Power Generation Environment
Section
Tsuruga Thermal Power Plant
Hokuriku Electric Power Co., Ltd.
◎ Keywords: radiation, prevention of thermal loss due to thermal conduction
◎ Outline of the Theme
Rapid surges electric load are frequently observed early in the morning at coal thermal power plants. For
Unit 1 of Tsuruga Thermal Power Plant, when an electric load range of less than 250 MW continued for 8
hours or more, all soot blowers were activated to uplift the electric load. In this project, an examination was
to determine which soot blowers should be turned on to improve the soot blower operations and maintain the
electric load the volume of steam at appropriate levels.
◎ Period of the Study (April 2001 – March 2003)
･ Planning: 6 months (April – September 2001)
･ Measures Taken: 12 months (October 2001 – September 2002)
･ Assessment of Results: 6 months (October 2002 – March 2003)
◎ Outline of Tsuruga Thermal Power Plant
･ Production: Electricity (Unit 1: 500 MW, Unit 2: 700 MW)
･ Employees: 107
･ Annual consumption of energy (as of FY2002)
Coal: 2,294,398 (ton)
Heavy Oil: 3,355 (kl)
◎ Outline of the Facility
High temperature
reheated steam pipe
Detailed drawing
Main steam pipe of the boiler
retaeheR WW3 level
Super-
Turbine
heater
WW2 level
Generator
WW1 level
Condenser
Low temperature
Boiler
reheated steam pipe
Soot blower
Main water feed pipe
Water feed
pump
Fig. 1: Outline of the Facility
133

1. Background of the Theme Selection
There is a growing gap in electricity consumption between daytime and nighttime. Even in coal thermal
power plants, electric load adjustment is frequently performed excluding the high electric load time. In Unit
1 of Tsuruga Thermal Power Plant, all soot blowers set up in the plant used to be turned on to uplift the
power from the low electric load range to the high electric load range to compensate for the gap in the
electric demand. Before doing so, the unit was subject to be in low electric load operation for 2 hours and
45 minutes before starting the blowers. The way the soot blowers are used is subject to a revision in this
project to smoothen the shift from the low electric load to the high electric load range, to minimize the
transition time of electric load restriction and to lower the volume of steam consumed.
2. Current Conditions and Analysis
(1) Current Conditions
a. Aim and Type of Soot Blowers
Coal contains 10% ash, and combustion of coal generates even more ash. When the ash is deposited in the
steam pipe, the heat transfer performance decreases. The thicker the ash layer on the pipe, the greater the
heat transfer performance deteriorates causing a decrease in steam temperature. The ash layer is not
uniformly distributed throughout the pipe, but attaches in a random manner on the inner wall of the pipe.
This causes difference in temperature of the metal surface of the pipe, increases thermal stress and may
damage to the pipe. In order to remove the ash, a soot blower is used. As shown in Fig. 2 and 3, a lance
tube rotates and moves forward driven by a motor and injects high pressure steam from the nozzle attached to
it to clean the thermal transfer surface of the boiler.
Swivel tube Steam pipe
Motor
Steam
Steam
valve
As h (deposits)
Fig. 2 Appearance of a Furnace Soot Blower
Motor
Furnace
Ash (deposits)
Lance tube
Steam valve
Fig. 3: Appearance of a Long Soot Blower
Table 1 shows the types of soot blowers. The blowers are installed as shown in Fig. 1 considering the
balance of collecting thermal energy by the boiler.
Table 1: Types of Soot Blowers
Nos. of Moving Steam
Type R.P.M.
Units distance consumption
Furnace soot
Furnace (WW) 54 290(mm) 1.0(rpm) 35.5(kg/pc.)
blower
Superheater (SH) 16
Long soot Reheater (RH) 10
7,950(mm) 16.9(rpm) 656.5(kg/pc.)
blower Rear thermal
8
transmission part
Air preheater ＡＨ 2 2,540(mm) − 7,300(kg/pc.)
Total 90 − − 24,240(kg)
134

b. Operation of Soot Blowers
Figures 4, 5 and 6 show the process of operating a soot blower, rotation mode and the relationship between
the stain indicator and the soot blower respectively. In the high electric load range (250 MW or above), the
stain indicator is calculated to express the condition of ash deposited onto the thermal transfer surface, to
automatically operate the soot blower to the ash deposit areas only. However, in the low electric load range
(less than 250 MW), the stain indicator calculation is unreliable, necessitating operation of all soot blowers,
otherwise ash cannot be removed completely from all the areas of the thermal transmission area, causing
temperature surge of the metal surfaces and widened difference in the internal wall temperature of the
furnace.
hsa
fo
tnemhcattA
lamreht
eht
ot
secafrus
noissimsnart
lamreht
fo
esaerceD
noissimsnart ecnamrofrep
laoc
fo
esaercnI
noitpmusnoc
latem
fo
esaercnI
erutarepmet
ecafrus
laoc
fo
noitsubmoC
gniwolb
tooS
Fig. 4: Process of Soot Blowing
"Operation Mode" "Soot Blower to be Operated"
Soot Blower Start Graph
Start
Sequence Control All units Stop
Automatic Area of ash deposits (of over
Stain Indicator Graph
Combustion Control and above the designated stain
indicator level)
Load of 250 MW or above
Fig. 5: Operation Mode of Soot Blowers Fig. 6: Soot Blower and Stain Indicators
(2) Analysis of the Current Conditions
In the electric load range shown in Fig. 7, the thermal collection performance of the furnace is not balanced.
If a soot blower is used, the boiler is subject to a disturbance and hence, the areas for which soot blowing is
prohibited are designated. If the low electric load condition continues for 8 hours or more after all soot
blowers are operated before decreasing the electric load to the low electric load area, the thermal
transmission surface is stained with uneven distribution of ash deposits. Thus, the duration of 2 hours and
45 minutes is set during which the low electric load condition is maintained, and, after 2 hours and 45
minutes, soot blowing is conducted using all soot blowers. (See Fig. 8)
The ranges in which soot
blowing is prohibited
)WM(
tuptuO
rotareneG
)WM(
tuptuO
rotareneG
Starts all Starts all
soot blowers soot blowers
8 hours or more 2 hours and
45 minutes
Fig. 7: Soot Blowing Prohibition Zones Fig.8: Timing of Soot Blowing
135

3. Progress of Actions
(1) Organization
At Tsuruga Thermal Power Plant, ‘decreasing the power generation cost’ and ‘enhancing the reliability of the
power generation facilities’ prioritized. In line with this policy, a series of actions was implemented to
further decrease the power generation cost.
(2) Setting Targets
When an electric load is uplifted by starting soot blowers at a constant electric load of 125 MW after
confirming that the low electric load range of less than 250 MW continues for 8 hours or more, which soot
blowers should be used is determined to reduce the number of soot blowers to be used for removing ash and
hence to reduce steam consumption. The reduction target is set for each group of furnaces, superheaters and
reheaters by considering the balance of thermal collection performance.
Target steam consumption: 8,500 kg/time
Current steam consumption: 24,240 kg/time
(reduction of 65%)
(3) Challenges and Examinations
Coal thermal power plants use various types of coal to generate electricity. The degree of ash deposited
and combustion performance greatly vary from coal-to-coal. An important indicator for determining the
combustion performance of coal includes the combustion ratio, which is expressed by the ratio of fixed
carbon and volatile matter content.
Combustion ratio = Fixed carbon/Volatile matter content
Coals are categorized in terms of the combustion ratio to examine the part where soot blowing should be
conducted.
Table 2: Combustibility of Coal
Coal Combustibility Ash content SH and RH sides
Highly combustible coal Low High SH/RH side
Standard coal
Low combustible coal High Low Furnace side
4. Measures Taken
(1) Selection of Soot Blower Group
After considering the coal categories and combustibility shown in Table 2, a soot blower operation test was
conducted to two patterns as shown in Fig. 9 and 10.
[Pattern 1] Test Group 1: (A), (E) and (C) [Pattern 2] Test Group 3: (A), (B) and (C)
Test Group 2: (C), (D) and (F)
? WW3 level WW3 level
WW2 level WW2 level
WW1 level WW1 level
Fig. 9: Soot Blower Operation Pattern 1 Fig. 10: Soot Blower Operation Pattern 2
The coal shown in Table 3 was used as the representative coal categorized by the combustion ratio and the
test was conducted on Test Group 1, 2 and 3 to determine the response of automatic control of the boiler
against a change in the electric load. In addition, refer to a Fig. 11 about Test Process.
136

Table 3: Representative Coal Categorized by Coal Type
Highly combustible coal Standard Coal Low combustible coal
Test Group 1 Mora Coal (Mra) Hunter Valley Coal (HV) Prima Coal
Test Group 2 Country of origin: Australia Country of origin: Australia Country of origin: Indonesia
Combustion ratio: 1.99 Combustion ratio: 1.57 Combustion ratio: 1.21
Test Group 3
(2) Test Process
･ All soot blowers are started at the electric load of 250 MW or above before decreasing it.
･ After decreasing the electric load, the electric load of 250 MW or below is maintained for at least 8 hours,
and then the electric load of 125 MW is maintained for at least 4 hours.
･ Soot blowing of either Pattern 1 or 2.
･ The electric load is uplifted up to 360 MW.
- To reduce the electric load
retention time Confirm the response
- To reproduce stain condition of of automatic control of
the thermal transmission surface boilers
under the low electric load range
Starts all
soot blowers
- Remove ash on the thermal
transmission surface
Maintain for at least 8 hours
Maintain for
at least 4 hours Start a start blower of either
one of Test Group 1, 2 or 3.
)WM(
tuptuO
rotareneG
Fig. 11: Test Process
(3) Criteria for Determining the Response of the Automatic Control of Boilers to the Shift of the Load
･ The temperature of the main steam must not deviate greatly from the set values along with the increase in
electric load.
･ The reheated steam temperature of which set values are subject to change along with the shift of the electric
load must not deviate greatly from the set values.
･ The difference of the internal wall temperature of the furnace must be within the controlled temperature of
150℃.
(4) Examination of the Location of Ash Attachment
Considering the characteristics of coal, ash is likely to attach to the locations shown in Fig. 12. In the low
electric load zone, air tends to be excessively supplied and combustibility is enhanced. Thus, ash generated
from the combustion of even highly combustible coal is likely to deposit on the furnace side. For
combusting highly combustible coal, it is effective to operate all soot blowers of the furnace shown in Pattern
2. However, the coal contains a lot of ash and soot blowing only on the furnace side involves decreasing the
main steam temperature and widening the gap of the temperature on the surface area.
137

Highly combustible coal
SShhiifftt ttoo tthhee
ffuurrnnaaccee iinn llooww
eelleeccttrriicc llooaadd zzoonnee
Furnace
Low combustible coal
Fig. 12: Location of Ash Deposit Anticipated
(5) Results
Table 4 indicates the results of the test for highly combustible coal, standard coal and low combustible coal.
Table 4: Test Results by Coal Type
Assessment
Test group Soot blower group Highly Combustible Coal Standard Coal Low Combustible Coal
Mra Hv Pr
1 (A) → (E) → (G) × (*1) ○ −
2 (C) → (D) → (F) ○ ○ −
3 (A) → (B) → (C) ◎ ◎ ◎
* The temperature gap on the rear wall surface: 168.9℃ (max.)
Table 5: Burner Angle Change Program for Highly Combustible Coal
Upper limit: +30℃
【Front View】 【Side View】
)°(
elgnA
renruB
Fine
powder
coal
Burner angle
Lower limit: −30℃ Before change
After change
Fig. 13 Coal Burner Angle Change
Load (MW)
a. Test Group 1
(a) Highly Combustible Coal
The temperature difference on the surface exceeding its controlled value is largely attributable to the
burner angle when the electric load was increased from 180 MW to 250 MW, which caused a change in the
flow of gas to affect the thermal collection performance on the furnace side. For the reason, the burner
angle program was changed to that shown in Table 5 to remove such gaps and continue the following tests.
In addition, coverage of coal burner angle change is shown in Fig. 13.
(b) Standard Coal
Good results were obtained without any particular problems.
138

b. Test Group 2 and 3
(a) Highly Combustible Coal
After the burner angle program was changed, the temperature gap on the surface area was able to be
restricted and good results were obtained.
(b) Standard Coal
Good results were obtained without any particular problems.
(c) Low Combustible Coal
For Test Group 3, good results were obtained without any particular problems.
(6) Assessment of the Response of Automatic Control of Boiler to the Load Shift
As a representative of all coal categories, the response to the electric load shift for main steam temperature
(MST) and reheated steam temperature (RST) when all soot blowers are operated for highly combustible coal
are shown in Table 6, 7 and 8. For Test Group 3, the soot blower of the furnace was operated only.
Though the decrease in main steam and reheated steam temperature just after starting the soot blower was
slightly larger than that when all soot blowers were turned on, the difference was narrowed gradually as the
electric load went up. The performance was favorable with no adverse effects on the increase of the electric
load.
Table 6: MST and RST before and after the Operation of Soot Blowers
Set temperature Temperature before Temperature after starting Temperature
Soot blower
(℃) starting a soot blower (℃) a soot blower (℃) decrease (℃)
group
MST/RST MST/RST MST/RST MST/RST
All 566 (constant)/ 552/525 529/495 ▲23/▲30
varies depending on
(A)→(B)→(C) 559/521 519/476 ▲40/▲45
electric load
Table 7: Response to the Load Shift of Table 8: Response to the Load Shift of
Main Steam Temperature Reheated Steam Temperature
)℃(
erutarepmeT
maetS
niaM
)℃(
erutarepmeT
maetS
detaeheR
Good response observed. Good response observed.
Set Values for the Main Set Values for the Reheated
Steam Temperature Steam Temperature
All soot blowers used. All soot blowers used.
Furnace soot blower is Furnace soot blower is
used only. used only.
Generator Output (MW) Generator Output (MW)
139

Table 9: Temperature Difference on the Surface
in Increasing the Electric Load
no
ecnereffiD
erutarepmeT
)℃(
ecafruS
eht
All soot blowers used.
Furnace soot blower
is used only. All soot blowers of the
furnace can be applied.
Table 10: Steam Volume of Soot Blowers
Generator Output (MW)
)gk(
emuloV
maetS
Decreased by 22,323 kg
All Test Test Test
Group 1 Group 2 Group 3
For all coal categories, it was confirmed that the response of automatic control of boiler against the electric
load shift was good when all soot blowers of the furnace were used only.
As to the temperature difference on the surface, the values were all within the controlled limit and good
results were obtained.
5. Effectiveness of the Measures
(1) Reduction of Steam Consumption used by the Soot Blowers
Table 11: Effects of Improving Soot Blower Operation
Before After Results
Blowing time 2 hours and 45 minutes 45 minutes Curtailed by 2 hours
Response of the main
No problems No problems −
steam temperature
Response of the reheated
No problems No problems −
steam temperature
Steam consumption 24,240（ｋｇ） 1,917（ｋｇ） Reduced by 92%
a. Reduction of Annual Steam Consumption
Reduction of 1,451,000 (kg) of annual steam consumption achieved.
(equivalent to 130 kl/year of crude oil)
Calculation Formula of Converting Steam Consumption to Crude Oil Consumption
(kl/time)
(Calculation Conditions)
･ Enthalpy of the sot blower steam source: 3,140 (kJ/kg)
･ Calorific power of crude oil: 38.2×106 (kJ/kl)
･ Boiler efficiency: 90%
･ Number of times of changing the electric load: Once in two days or 65 times a year (except for summer
and winter time)
140

6. Summary
For all coal categories, use of furnace soot blowers in low electric load conditions only in low electric load
conditions did not reveal any problems in increasing the electric load, and the automatic control of boilers
functioned well. We were successful in reduction of soot blower steam consumption in response to the
change of operation mode of the coal thermal power generation system.
7. Future Plans
To anticipate future diversification in coal procurement, we will attempt to achieve a stable power supply and
reduce costs through energy saving after examining all operating conditions. At the same time, we will
raise the mind toward energy saving and address measures against it.
141
