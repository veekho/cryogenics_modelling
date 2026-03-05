import numpy as np
import matplotlib.pyplot as plt

time = 5*3600 #hours *3600 = sec

p_room = 80e5 #bar *10^5 = Pa
p_cool = p_room*1/300
v_mole = 27.58e-6 #molar volume of he4, cc/mol x10^-6
v_evap = 20e-6 #estimate of evaporator volume, cc/mol x10^-6
v_pump = 20e-6 #estimate of cryopump volume, cc/mol x10^-6
temp_pump = 3 #K
temp_evap = 1 #K

tube_len = 10e-2 #cm *10^-2
tube_wall = 0.25e-3 #mm *10^-3
tube_dia = 1e-2 #cm *10^-2

int_points = 1000 #Number of points in integral
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


def temperature_height(height, pump_temp=temp_pump, evap_temp=temp_evap, length=tube_len):
    return evap_temp + (pump_temp-evap_temp)*height/length

temperatures = temperatures = np.linspace(temp_evap, temp_pump, int_points)
cooling_power = np.pi*tube_dia*tube_wall/tube_len * np.trapezoid(thermal_conductivity(temperatures), temperatures)
evap_rate = cooling_power/latent_heat #Moles per sec
n_l = evap_rate*time
print(f"Moles of liquid He in evaporator: {n_l}")

n_e = p_cool*(v_evap - n_l*v_mole)/(8.31*temp_evap)
print(f"Moles of He vapour in evaporator: {n_e}")

n_p = p_cool*(v_pump)/(8.31*temp_pump)
print(f"Moles of He vapour in cryopump: {n_p}")

heights = np.linspace(0, tube_len, int_points)
n_t = np.trapezoid(temperature_height(heights), heights)*p_cool*np.pi*tube_dia**2/(4*8.31)
print(f"Moles of liquid He in cryopump: {n_t}")

n = n_l + n_e + n_p + n_t
print(f"Total number of moles of He4 required: {n}")
print(f"Volume of He4 (at STP) required: {n*22.4:.3f}L")
