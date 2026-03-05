def display_information(operating_hours, n_total_4he, V_STP_4he, n_total_3he, V_STP_3he):
    """Display all calculation results for both He4 and He3."""
    print("\n","-"*40)
    print("Calculation Results:")
    print(f"Operating time: {operating_hours} hours")
    print(f"\nHelium-4:")
    print(f"  Total moles: {n_total_4he:.6f} mol")
    print(f"  Required volume at STP: {V_STP_4he:.2f} L")
    print(f"\nHelium-3:")
    print(f"  Total moles: {n_total_3he:.6f} mol")
    print(f"  Required volume at STP: {V_STP_3he:.2f} L")
    print("-" * 40,"\n")