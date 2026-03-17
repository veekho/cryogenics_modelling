#Tracking temperature correspondance
#   - Agreement between split condenser temp and He3 pots (actuated by He3 heat switches)
#   - Agreement between 4K plate and He4 pumps (actuated by He4 heat switches)
#   - Correlation between hot plates and cold plates of each system (and acuating heaters)
#   - Times of cooling in MC(3T_MC>=T_HX)/Maximisation of cooling(T_Hx=T_MC) (Correlation with still heater) 

import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, CheckButtons

str2dt = lambda s: dt.datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')

titles = np.genfromtxt('./VeerJan/cryosystem_model/slow_control.csv', delimiter=',', dtype=str, max_rows=1)
data = np.genfromtxt('./VeerJan/cryosystem_model/slow_control.csv', delimiter=',', skip_header=1, converters={0: str2dt}, unpack=True)

time, switch_4a, pump_4a, switch_3a, pump_3a, switch_4b, pump_4b, switch_3b, pump_3b, pot_4a, pot_3a, pot_4b, pot_3b, split_condenser, plate_50k, plate_4k, mixing_chamber, still = data

"""
print(time)
print(switch_4a)
print(pump_4a)
print(switch_3a)
print(pump_3a)
print(switch_4b)
print(pump_4b)
print(switch_3b)
print(pump_3b)
print(pot_4a)
print(pot_3a)
print(pot_4b)
print(pot_3b)
print(split_condenser)
print(plate_50k)
print(plate_4k)
print(mixing_chamber)
print(still)
#"""

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel("Time")
ax.set_ylabel("Temperature (K)")

#Pulse tube cooler
#ax.plot(time, plate_50k, label="50K Plate")
ax.plot(time, plate_4k, label="4K Plate")

##Sorption pump A
ax.plot(time, switch_4a, label="He4 Switch A")
ax.plot(time, switch_3a, label="He3 Switch A")
ax.plot(time, pump_4a, label="He4 Pump A")
ax.plot(time, pump_3a, label="He3 Pump A")
ax.plot(time, pot_4a, label="He4 Pot A")
ax.plot(time, pot_3a, label="He3 Pot A")

##Sorption pump B
#ax.plot(time, switch_4b, label="He4 Switch B")
#ax.plot(time, switch_3b, label="He3 Switch B")
#ax.plot(time, pump_4b, label="He4 Pump B")
#ax.plot(time, pump_3b, label="He3 Pump B")
#ax.plot(time, pot_4b, label="He4 Pot B")
#ax.plot(time, pot_3b, label="He3 Pot B")

##Split condenser
#ax.plot(time, split_condenser, label="Split Condenser")

##Mini DR
#ax.plot(time, mixing_chamber, label="Mixing Chamber")
#ax.plot(time, still, label="Still")

ax.set_yscale('log')

fig.subplots_adjust(right=0.8)
#fig.legend()
fig.legend(bbox_to_anchor=(0.7, 0, 0.2, 0.6))

"""
fig.subplots_adjust(bottom=0.25, right=0.75)

plots = {}
for i, title in enumerate(titles):
    if i!=0:
        plots[title] = ax.plot(data[0], data[i], label=title)
fig.legend(ncols=5, bbox_to_anchor=(-0.2, 0, 0.8, 0.2))

ax_checkbuttons = fig.add_axes((0.75, 0.25, 0.2, 0.6))
check = CheckButtons(ax_checkbuttons, list(titles[1:]), np.ones(len(titles)-1, dtype=bool))

def reset_visibility(label):
    plots[label].set_visible(not plots[label].get_visible())

check.on_clicked(reset_visibility)
#"""

plt.show()
