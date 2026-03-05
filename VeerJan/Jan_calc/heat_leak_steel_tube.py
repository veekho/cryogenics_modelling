"""
Heat leak calculation through steel tube support rod.
Uses thermal conductivity from thermal_conductivity module.
"""

import numpy as np
from thermal_conductivity import thermal_conductivity


def qdot_steel_tube_conduction(T_cold, T_hot, length, area):
    """
    Calculate heat leak through a support rod using thermal conductivity integration.
    
    Parameters:
    T_cold : float
        Cold end temperature (K)
    T_hot : float
        Hot end temperature (K)
    length : float
        Length of the rod (m)
    area : float
        Cross-sectional area (m²)
    
    Returns:
    Q_dot : float
        Heat leak rate (W)
    """
    # Numerical integration of k(T) dT
    T_vals = np.linspace(T_cold, T_hot, 5000)
    integral_k = np.trapezoid(thermal_conductivity(T_vals), T_vals)
    
    # Heat leak calculation
    Q_dot = (area / length) * integral_k
    
    return Q_dot
