# Monte Carlo Option Pricing

A Python implementation of European call option pricing using Monte Carlo
simulation, benchmarked against the Black-Scholes analytical solution.

## Project Overview

This project demonstrates how Monte Carlo simulation can be used to estimate
the value of a European call option under the geometric Brownian motion model.

The implementation compares simulated option prices against the Black-Scholes
closed-form solution and studies convergence as the number of simulations
increases.

## Methodology

The terminal stock price is simulated using:

ST = S0 × exp((r - 0.5σ²)T + σ√T Z)

where:

- S0 is the initial stock price
- K is the strike price
- T is time to maturity
- r is the risk-free interest rate
- σ is volatility
- Z is a standard normal random variable

The European call payoff is:

max(ST - K, 0)

and the Monte Carlo option value is obtained by discounting the expected payoff
to the present.

## Features

- Black-Scholes European call pricing
- Monte Carlo option pricing
- Convergence analysis across increasing simulation counts
- Absolute pricing-error comparison against Black-Scholes
- Sensitivity analysis across different volatility levels
- Visualization of Monte Carlo and Black-Scholes prices

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib

## Example Parameters

- Initial stock price: 100
- Strike price: 100
- Time to maturity: 1 year
- Risk-free rate: 5%
- Volatility: 20%

## Convergence Study

Monte Carlo estimates are evaluated using:

- 1,000 simulations
- 5,000 simulations
- 10,000 simulations
- 50,000 simulations
- 100,000 simulations

The resulting estimates are compared against the Black-Scholes price to observe
how simulation error changes with sample size.

## Running the Project

Install the dependencies:

pip install numpy scipy matplotlib

Then run:

python option_pricing.py
