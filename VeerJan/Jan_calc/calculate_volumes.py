"""
Volume calculations for helium at different pressures and STP.
"""


def calculate_volume_at_pressure(n_total, pressures_atm):
    """
    Calculate volume at different pressures using ideal gas law.
    
    Parameters:
    n_total : float
        Total moles of helium
    pressures_atm : list
        List of pressures in atm
    
    Returns:
    volumes : dict
        Dictionary with pressure as key and volume in liters as value
    """
    R = 8.314  # Gas constant (J/(mol·K))
    T_ref = 273.15  # Reference temperature (K) for STP
    
    volumes = {}
    for P_atm in pressures_atm:
        P_pa = P_atm * 101325  # Convert atm to Pa
        V = (n_total * R * T_ref) / P_pa  # Volume in m³
        V_liters = V * 1000  # Convert to liters
        volumes[P_atm] = V_liters
    
    return volumes


def calculate_volume_at_stp(n_total):
    """
    Calculate volume at STP.
    
    Parameters:
    n_total : float
        Total moles of helium
    
    Returns:
    V_STP : float
        Volume at STP (L)
    """
    molar_volume_STP = 22.7  # L/mol
    V_STP = n_total * molar_volume_STP
    return V_STP