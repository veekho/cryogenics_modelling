"""
Main calculation script for helium evaporation and volume in cryogenic system.
"""

import numpy as np
from qdot_steel_tube import qdot_ss, diameter_tube
from calculate_evaporation_rate import calculate_evaporation
from calculate_volumes import calculate_volume_at_stp
from calculate_total_n_for_he4 import calculate_total_n_he4
from calculate_total_n_for_he3 import calculate_total_n_he3
from display_info import display_information

p_room = 80e5 #bar *10^5 = Pa
p_cool = p_room*1/300
v_evap = 20e-6 #estimate of evaporator volume, cc/mol x10^-6
v_pump = 20e-6 #estimate of cryopump volume, cc/mol x10^-6
L_4HE = 85 #Latent heat of 4He at ~1 K (J/mol)
L_3HE = 25 #Latent heat of 3He at ~1 K (J/mol)
v_mole_4he = 27.58e-6 #molar volume of he4, cc/mol x10^-6
v_mole_3he = 36.8e-6 #molar volume of he3, cc/mol x10^-6
int_points = 5000 #Number of points in integral

# Temperature limits for integration
T_cold_4he = 1
T_hot_4he = 3
T_cold_3he = 0.3
T_hot_3he = 1

# Support rod geometry
length_4he = 0.10  # 10 cm (m)
length_3he = 0.15  # 15 cm (m)


def main():
    """Main calculation script."""
    
    # Calculate heat leak
    Q_dot_4He = qdot_ss(T_cold=T_cold_4he, T_hot=T_hot_4he, length=length_4he)
    Q_dot_3He = qdot_ss(T_cold=T_cold_3he, T_hot=T_hot_3he, length=length_3he)
    
    # Helium evaporation calculation
    operating_hours = 5
    
    # Calculate for Helium-3
    n_total_3He = calculate_total_n_he3(
        Q_dot=Q_dot_3He, 
        operating_hours=operating_hours, 
        latent_heat=L_3HE, 
        p_cool=p_cool, 
        v_mole=v_mole_3he, 
        v_evap=v_evap,
        temp_evap=T_cold_3he, 
        v_pump=v_pump, 
        temp_pump=T_hot_3he, 
        length=length_3he, 
        diameter_tube=diameter_tube, 
        int_points=int_points,
        temp_pump_val=T_hot_3he, 
        temp_evap_val=T_cold_3he
    )

    # Calculate for Helium-4
    n_total_4He = calculate_total_n_he4(
        Q_dot=Q_dot_4He, 
        operating_hours=operating_hours, 
        latent_heat=L_4HE, 
        p_cool=p_cool, 
        v_mole=v_mole_4he, 
        v_evap=v_evap,
        temp_evap=T_cold_4he, 
        v_pump=v_pump, 
        temp_pump=T_hot_4he, 
        length=length_4he, 
        diameter_tube=diameter_tube, 
        int_points=int_points,
        temp_pump_val=T_hot_4he, 
        temp_evap_val=T_cold_4he
    )
    
    # Calculate volumes at STP
    V_STP_4he = calculate_volume_at_stp(n_total_4He)
    V_STP_3he = calculate_volume_at_stp(n_total_3He)
    
    display_information(operating_hours, n_total_4He, V_STP_4he, n_total_3He, V_STP_3he)

    print(f"He3 Cooling power: {Q_dot_3He}")
    print(f"He4 Cooling power: {Q_dot_4He}")


if __name__ == "__main__":
    main()
