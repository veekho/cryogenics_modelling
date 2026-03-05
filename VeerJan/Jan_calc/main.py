"""
Main calculation script for helium evaporation and volume in cryogenic system.
"""

import numpy as np
from heat_leak_steel_tube import qdot_steel_tube_conduction
from calculate_evaporation_rate import calculate_evaporation
from calculate_volumes import calculate_volume_at_pressure, calculate_volume_at_stp
from calculate_area import calculate_area


def main():
    """Main calculation script."""
    
    # Temperature limits for integration
    T_cold = 1
    T_hot = 3
    emissivity = 0.1  # Emissivity of steel
    sigma = 5.670374419e-8  # Stefan-Boltzmann
    k_resistance = 1e-4  # Kapitza resistance (m²·K/W)
    
    # Support rod geometry
    length = 0.10  # 10 cm (m)
    diameter_tube = 0.01  # 1 cm (m)
    steel_thickness = 0.00022  # 0.22 mm wall thickness (m)
    
    # Calculate cross-sectional area
    area = calculate_area(diameter_tube, steel_thickness)  # m²
    
    # Calculate heat leak
    Q_dot_ss_conduction = qdot_steel_tube_conduction(T_cold, T_hot, length, area)
    #Q_dot_radiation = emissivity*sigma*area*(T_hot**4 - T_cold**4)  # Radiation heat leak (W)
    #Q_dot_kapitza = (area/4*k_resistance)*(T_hot - T_cold)  # Kapitza resistance heat leak (W)
    #Q_dot=Q_dot_ss_conduction + Q_dot_radiation + Q_dot_kapitza
    Q_dot=Q_dot_ss_conduction  # Total heat leak (W)
    print(f"Heat leak rate (Q_dot): {Q_dot:.6f} W")
    
    # Helium evaporation calculation
    operating_hours = 5
    
    n_dot, n_total = calculate_evaporation(Q_dot, operating_hours)
    print(f"\nEvaporation rate (n_dot): {n_dot:.9f} mol/s")
    print(f"Operating time: {operating_hours} hours")
    print(f"Total moles evaporated: {n_total:.6f} mol")
    
    # Calculate volume at different pressures
    pressures = [1, 5, 10, 20]  # atm
    volumes = calculate_volume_at_pressure(n_total, pressures)
    
    print(f"\nRequired volume at different pressures:")
    for P_atm, V_liters in volumes.items():
        print(f"  {P_atm} atm: {V_liters:.2f} L")
    
    # Calculate volume at STP
    V_STP = calculate_volume_at_stp(0.22)
    print(f"\nRequired volume at STP: {V_STP:.2f} L")


if __name__ == "__main__":
    main()
