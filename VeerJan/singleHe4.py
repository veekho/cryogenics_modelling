import numpy as np
import matplotlib.pyplot as plt

time = 4*3600 #hours
pressure = 80 #bar
temp_init = 3
temp_cool = 0.843
temp_step = 0.001

tube_len = 10e-2
tube_wall = 1e-3
tube_dia = 0.6e-2
condenser_len = 1e-2

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

def integrate(y, dx):
    (y[1:]+y[:-1])*dx/2

#"""
temperatures = np.linspace(temp_cool, temp_init, int((temp_init-temp_cool)/temp_step))

cooling_power = np.pi*tube_dia*tube_wall/tube_len * np.trapezoid(thermal_conductivity(temperatures), temperatures)
print(f"Cooling power:\t{cooling_power} W")

evap_rate = cooling_power/latent_heat #Moles per sec
print(f"Moles of Helium:\t{evap_rate*time} mol")

#print(f"Litres of He at STP: {evap_rate*time*22.4}")
print(f"Litres of He at STP: {evap_rate*time*8.31*300/101.325e3 * 1000}")

"""
temp_range = np.linspace(0, 300, 100)
k_range = thermal_conductivity(temp_range)

fig = plt.figure()
ax  =fig.add_subplot(111)
ax.scatter(temp_range, k_range, marker='.')
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Thermal conductivity(W m^-1 K^-1)")
plt.show()
#"""

