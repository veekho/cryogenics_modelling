"""
Helium evaporation rate calculation for cryogenic system.
"""


def calculate_evaporation(Q_dot, operating_hours, latent_heat):
    """
    Calculate total helium moles evaporated.
    
    Parameters:
    Q_dot : float
        Heat leak rate (W)
    operating_hours : float
        Operating time (hours)
    latent_heat : float
        Latent heat of evaporation (J/mol)
    
    Returns:
    n_total : float
        Total moles evaporated
    """
    # Evaporation rate (mol/s)
    n_dot = Q_dot / latent_heat
    
    # Operating time (seconds)
    t = operating_hours * 3600
    
    # Total moles evaporated
    n_total = n_dot * t
    
    return n_total
