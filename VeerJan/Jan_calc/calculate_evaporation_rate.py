"""
Helium evaporation rate calculation for cryogenic system.
"""

L = 83  # Latent heat of 4He at ~1 K (J/mol)


def calculate_evaporation(Q_dot, operating_hours):
    """
    Calculate helium evaporation rate and total moles evaporated.
    
    Parameters:
    Q_dot : float
        Heat leak rate (W)
    operating_hours : float
        Operating time (hours)
    
    Returns:
    n_dot : float
        Evaporation rate (mol/s)
    n_total : float
        Total moles evaporated
    """
    # Evaporation rate (mol/s)
    n_dot = Q_dot / L
    
    # Operating time (seconds)
    t = operating_hours * 3600
    
    # Total moles evaporated
    n_total = n_dot * t
    
    return n_dot, n_total
