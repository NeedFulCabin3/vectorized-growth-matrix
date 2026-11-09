import numpy as np
import pandas as pd


def generate_growth_matrix(
    principal: float, rates: np.ndarray, years: np.ndarray
) -> pd.DataFrame:
    """Generates a 2D matrix of future values using NumPy meshgrid and array broadcasting."""
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if np.any(rates < 0) or np.any(years < 0):
        raise ValueError("Rates and time horizons must be non-negative.")

    # Create 2D coordinate grids for rates and years
    rate_grid, year_grid = np.meshgrid(rates, years)

    # Vectorized compounding calculation: A = P * (1 + r)^t
    growth_matrix = principal * np.power(1 + rate_grid, year_grid)

    # Format table axis labels
    rate_labels = [f"{r * 100:.1f}%" for r in rates]
    year_labels = [f"Year {y}" for y in years]

    return pd.DataFrame(growth_matrix, index=year_labels, columns=rate_labels)


def get_float_input(prompt: str, min_val: float = 0.0) -> float:
    """Helper function to safely get and validate float inputs from terminal."""
    while True:
        try:
            val = float(input(prompt))
            if val <= min_val:
                print(f"  --> Please enter a value greater than {min_val}.")
                continue
            return val
        except ValueError:
            print("  --> Invalid entry. Please enter a valid number.")


def get_int_input(prompt: str, min_val: int = 1) -> int:
    """Helper function to safely get and validate integer inputs from terminal."""
    while True:
        try:
            val = int(input(prompt))
            if val < min_val:
                print(f"  --> Please enter a number greater than or equal to {min_val}.")
                continue
            return val
        except ValueError:
            print("  --> Invalid entry. Please enter a valid integer.")


def main():
    print("===========================================")
    print("      Compound Interest Matrix Generator   ")
    print("===========================================\n")

    try:
        # Dynamic inputs from terminal
        principal = get_float_input("Enter initial principal amount (₹): ", min_val=0)
        min_rate = get_float_input("Enter starting interest rate (%): ", min_val=-0.001) / 100
        max_rate = get_float_input("Enter ending interest rate (%): ", min_val=min_rate * 100) / 100
        rate_steps = get_int_input("Enter number of rate columns to generate: ", min_val=1)
        max_years = get_int_input("Enter duration in years: ", min_val=1)

        # Generate rate and year vectors
        rate_range = np.linspace(min_rate, max_rate, rate_steps)
        year_range = np.arange(1, max_years + 1)

        # Calculate matrix
        matrix_df = generate_growth_matrix(principal, rate_range, year_range)

        # Print formatted output using Indian Rupee (₹) symbol
        print(f"\n--- Projected Growth Matrix (Principal: ₹{principal:,.2f}) ---\n")
        formatted_df = matrix_df.map(lambda x: f"₹{x:,.2f}")
        print(formatted_df.to_string())

    except Exception as err:
        print(f"\nAn error occurred: {err}")


if __name__ == "__main__":
    main()