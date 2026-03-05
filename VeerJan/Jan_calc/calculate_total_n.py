"""
Calculate total moles of helium in the cryogenic system.
"""

import numpy as np


def calculate_total_n(Q_dot, operating_hours, latent_heat, p_cool, v_mole, v_evap, temp_evap, v_pump, temp_pump, length, diameter_tube, int_points):
    """
    Calculate total moles of helium including evaporation, evaporator, pump, and tube components.
    
    Parameters:
    Q_dot : float
        Heat leak rate (W)
    operating_hours : float
        Operating time (hours)
    latent_heat : float
        Latent heat of evaporation (J/mol)
    p_cool : float
        Cool pressure (Pa)
    v_mole : float
        Molar volume (m³/mol)
    v_evap : float
        Evaporator volume (m³)
    temp_evap : float
        Evaporator temperature (K)
    v_pump : float
        Pump volume (m³)
    temp_pump : float
        Pump temperature (K)
    length : float
        Tube length (m)
    diameter_tube : float
        Tube diameter (m)
    int_points : int
        Number of integration points
    
    Returns:
    n_total : float
        Total moles of helium
    """
    from calculate_evaporation_rate import calculate_evaporation
    
    # Temperature height function
    def temperature_height(height, pump_temp=temp_pump, evap_temp=temp_evap, length=length):
        return evap_temp + (pump_temp - evap_temp) * height / length
    
    # Helium evaporation calculation
    n_l = calculate_evaporation(Q_dot, operating_hours, latent_heat)
    
    # Helium in evaporator
    n_e = p_cool * (v_evap - n_l * v_mole) / (8.31 * temp_evap)
    
    # Helium in pump
    n_p = p_cool * (v_pump) / (8.31 * temp_pump)
    
    # Helium in tube (integrated over temperature gradient)
    heights = np.linspace(0, length, int_points)
    n_t = np.trapezoid(temperature_height(heights), heights) * p_cool * np.pi * diameter_tube**2 / (4 * 8.31)
    
    # Total moles
    n_total = n_l + n_e + n_p + n_t
    
    return n_total