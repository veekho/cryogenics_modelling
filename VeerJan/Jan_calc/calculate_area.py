"""
Calculate cross-sectional area of steel tube.
"""

import numpy as np


def calculate_area(diameter_tube, steel_thickness):
    """
    Calculate the cross-sectional area of the steel tube.
    
    Parameters:
    diameter_tube : float
        Diameter of the tube (m)
    steel_thickness : float
        Thickness of the steel wall (m)
    
    Returns:
    area : float
        Cross-sectional area (m²)
    """
    area_tube = np.pi * (diameter_tube / 2) ** 2
    area_hollow = np.pi * (diameter_tube / 2 - steel_thickness) ** 2
    area = area_tube - area_hollow
    return area