import math
from scipy.stats import norm

# --- Inputs ---
S = 400     # Current share price
K = 420     # Strike price
T = 4 / 12  # Time in years (4 months)
x = 0.05    # Value of x from Q1
sigma = 0.22 * x

# --- Function to calculate call price using Black-Scholes ---
def black_scholes_call(S, K, T, r, sigma):
    d1 = (math.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    C = S * norm.cdf(d1) - K * math.exp(-r*T) * norm.cdf(d2)
    return C

# --- Put-call parity formula ---
def put_call_parity(C, S, K, r, T):
    return C - S + K * math.exp(-r*T)

# --- Tabulate values of P for r = 9x% to 14x% ---
print("Interest Rate (%) | Put Price (P)")
print("------------------|--------------")
for i in range(9, 15):
    r = i * x
    C = black_scholes_call(S, K, T, r, sigma)
    P = put_call_parity(C, S, K, r, T)
    print(f"{i}x = {r*100:.2f}%       | {P:.4f}")
