import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Parameters
S0 = 100       # Initial stock price
K = 100        # Strike price
T = 1          # Time to maturity (years)
r = 0.05       # Risk-free rate
sigma = 0.2    # Volatility

# Black-Scholes Function
def black_scholes_call(S0, K, T, r, sigma):
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

# Monte Carlo Pricing Function
def monte_carlo_call(S0, K, T, r, sigma, N):
    Z = np.random.normal(0, 1, N)
    ST = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    payoff = np.maximum(ST - K, 0)
    return np.exp(-r*T) * np.mean(payoff)

# Convergence Study
simulations = [1000, 5000, 10000, 50000, 100000]
bs_price = black_scholes_call(S0, K, T, r, sigma)

print("Black-Scholes Price:", round(bs_price, 4))
print("\nMonte Carlo Convergence Study:\n")

for N in simulations:
    mc_price = monte_carlo_call(S0, K, T, r, sigma, N)
    error = abs(mc_price - bs_price)
    print(f"Simulations: {N:<7} | MC Price: {mc_price:.4f} | Error: {error:.6f}")

# Volatility Analysis
vol_range = np.linspace(0.1, 3, 40)
mc_prices = []
bs_prices = []

for vol in vol_range:
    mc_prices.append(monte_carlo_call(S0, K, T, r, vol, 50000))
    bs_prices.append(black_scholes_call(S0, K, T, r, vol))

plt.figure()
plt.plot(vol_range, mc_prices, label="Monte Carlo")
plt.plot(vol_range, bs_prices, linestyle="--", label="Black-Scholes")
plt.xlabel("Volatility")
plt.ylabel("Call Option Price")
plt.title("Option Price vs Volatility")
plt.legend()
plt.show()