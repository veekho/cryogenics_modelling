import numpy as np
import matplotlib.pyplot as plt

time = 5 #hours
pressure = 80 #bar

tube_len = 10 #cm
tube_wall = 0.25 #mm
condenser_len = 1 #cm
latent_heat = 0#

def thermal_conductivity(temperature):
    #Return thermal conductivity of stainless steel at a given temperature
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

temp_range = np.linspace(0.3, 1)
