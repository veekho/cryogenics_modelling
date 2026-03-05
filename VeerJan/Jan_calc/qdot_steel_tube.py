"""
Heat leak calculation through steel tube support rod.
Uses thermal conductivity from thermal_conductivity module.
"""

import numpy as np
from thermal_conductivity import thermal_conductivity

# Constants for steel tube geometry
diameter_tube = 0.01  # 1 cm (m)
steel_thickness = 0.00022  # 0.22 mm wall thickness (m)


def calculate_area():
    """
    Calculate the cross-sectional area of the steel tube.
    
    Returns:
    area : float
        Cross-sectional area (m²)
    """
    area_tube = np.pi * (diameter_tube / 2) ** 2
    area_hollow = np.pi * (diameter_tube / 2 - steel_thickness) ** 2
    area = area_tube - area_hollow
    return area


def qdot_ss(T_cold, T_hot, length):
    """
    Calculate heat leak through a support rod using thermal conductivity integration.
    
    Parameters:
    T_cold : float
        Cold end temperature (K)
    T_hot : float
        Hot end temperature (K)
    length : float
        Length of the rod (m)
    
    Returns:
    Q_dot : float
        Heat leak rate (W)
    """
    # Calculate cross-sectional area
    area = calculate_area()
    
    # Numerical integration of k(T) dT
    T_vals = np.linspace(T_cold, T_hot, 5000)
    integral_k = np.trapezoid(thermal_conductivity(T_vals), T_vals)
    
    # Heat leak calculation
    Q_dot = (area / length) * integral_k
    
    return Q_dot
