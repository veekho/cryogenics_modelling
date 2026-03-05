import numpy as np
import matplotlib.pyplot as plt

time = 5*3600 #hours *3600 = sec
p_room = 80e5 #bar *10^5 = Pa
temp_pump = 3 #K
temp_evap = 1 #K
temp_step = 0.001 #K

tube_len = 10e-2
tube_wall = 0.25e-3
tube_dia = 1e-2

latent_heat = 85 #J mol^-1

def thermal_conductivity(temperature):
    #Return thermal conductivity (W m^-1 K^-1) of stainless steel at a given temperature
    #Coefficients from NIST data for thermal conductivity: https://trc.nist.gov/cryogenics/materials/304Stainless/304Stainless_rev.htm

    coeffs = []

    coeffs.append(-1.4087)
    coeffs.append(1.3982)
    coeffs.append(0.2543) 
    coeffs.append(-0.6260)
    coeffs.append(0.2334)
    coeffs.append(0.4256)
    coeffs.append(-0.4658)
    coeffs.append(0.1650)
    coeffs.append(-0.0199)

    y = 0
    for i in range(len(coeffs)):
        y+=coeffs[i]*np.log10(temperature)**i

    return 10**y

#"""
temperatures = np.linspace(temp_evap, temp_pump, int((temp_pump-temp_evap)/temp_step))

cooling_power = np.pi*tube_dia*tube_wall/tube_len * np.trapezoid(thermal_conductivity(temperatures), temperatures)
print(f"Cooling power:\t{cooling_power} W")

evap_rate = cooling_power/latent_heat #Moles per sec
print(f"Moles of Helium:\t{evap_rate*time} mol")

#print(f"Litres of He at STP: {evap_rate*time*22.4}")
print(f"Litres of He at STP: {evap_rate*time*8.31*300/101.325e3 * 1000}")

"""
temp_range = np.linspace(0, 1, 100)
k_range = thermal_conductivity(temp_range)

fig = plt.figure()
ax  =fig.add_subplot(111)
ax.scatter(temp_range, k_range, marker='.')
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Thermal conductivity(W m^-1 K^-1)")
plt.show()
#"""

# 05/03

def temperature_height(height, pump_temp=temp_pump, evap_temp=temp_evap, length=tube_len):
    return evap_temp + (pump_temp-evap_temp)*height/length

v_mole = 27.58e-6 #cc/mol x10^-6
v_evap = 20e-6 #estimate, cc/mol x10^-6
v_pump = 20e-6 #estimate, cc/mol x10^-6
p_cool = p_room*1/300

n_l = evap_rate*time
heights = np.linspace(0, tube_len, 1000)
n_t = np.trapezoid(temperature_height(heights), heights)*np.pi*tube_dia*p_cool/(4*8.31)
n_tot = n_l*(1-p_cool*v_mole/(8.31*temp_evap)) + p_cool*v_evap/(8.31*temp_evap) + p_cool*v_pump/(8.31*temp_pump) + n_t

print("\n2ND TRY:")
print(f"Moles of Helium:\t{n_tot} mol")
print(f"Litres of He at STP: {n_tot*8.31*300/101.325e3 * 1000}")