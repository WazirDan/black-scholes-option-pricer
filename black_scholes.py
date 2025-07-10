import math
from scipy.stats import norm
import matplotlib.pyplot as plt

# --- Functions ---
def black_scholes_call(S, K, T, r, sigma):
    d1 = (math.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    C = S * norm.cdf(d1) - K * math.exp(-r*T) * norm.cdf(d2)
    return C

def put_call_parity(C, S, K, r, T):
    return C - S + K * math.exp(-r*T)

# --- Inputs ---
try:
    S = float(input("Enter current share price S: "))
    K = float(input("Enter strike price K: "))
    t_months = float(input("Enter time to maturity in months (e.g. 4): "))
    T = t_months / 12
    x = float(input("Enter the value of x (from Q1): "))
    sigma = 0.22 * x

    mode = input("Type 't' to tabulate P over r = 9x% to 14x%, or type a specific interest rate in %: ").strip()

    if mode.lower() == 't':
        r_values = []
        p_values = []

        print("\nInterest Rate (%) | Put Price (P)")
        print("------------------|--------------")
        for i in range(9, 15):
            r = i * x
            C = black_scholes_call(S, K, T, r, sigma)
            P = put_call_parity(C, S, K, r, T)
            r_values.append(r * 100)
            p_values.append(P)
            print(f"{i}x = {r*100:.2f}%       | {P:.4f}")

        # --- Plotting ---
        plt.plot(r_values, p_values, marker='o', color='blue')
        plt.title('Put Option Price vs Interest Rate')
        plt.xlabel('Interest Rate (%)')
        plt.ylabel('Put Option Price (P)')
        plt.grid(True)
        plt.savefig("put_vs_r.png")  # Optional: save to file
        plt.show()

    else:
        r_input = float(mode)
        r = r_input / 100
        C = black_scholes_call(S, K, T, r, sigma)
        P = put_call_parity(C, S, K, r, T)

        print("\nResult for r = {:.2f}%:".format(r_input))
        print(f"Call Option Price: {C:.4f}")
        print(f"Put Option Price:  {P:.4f}")

except Exception as e:
    print("❌ Error:", e)
# --- End of Code ---
# This code implements the Black-Scholes model for option pricing and allows for both tabulation and specific interest rate calculations.
# It also includes error handling for user inputs and plots the results if tabulation is selected.
# The plot is saved as "put_vs_r.png" in the current directory.
# Ensure you have the required libraries installed: scipy, matplotlib.
# You can install them using pip if they are not already installed:
# pip install scipy matplotlib
# This code is designed to be run in a Python environment with access to the console for inputs and outputs.
# It is a complete implementation that can be executed directly.