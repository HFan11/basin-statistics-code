# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 02:06:13 2023

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

Q0 = 100
Qmin = 1
Qmax = 50
Pmax = 2.5e6
durations = np.linspace(0, 1, 1000)

Q = Q0 * np.exp(-np.log(Q0 / Qmin) * durations)
P = (4 * Pmax / Qmax) * Q - (4 * Pmax / Qmax**2) * Q**2

plt.figure()
plt.plot(durations, Q, label='Flow Duration Curve')
plt.xlabel('Duration (d)')
plt.ylabel('Streamflow (Q, m³/s)')
plt.title('Flow Duration Curve')
plt.grid()
plt.show()

plt.figure()
plt.plot(durations, P, label='Power Duration Curve')
plt.xlabel('Duration (d)')
plt.ylabel('Power (P, Watts)')
plt.title('Power Duration Curve')
plt.grid()
plt.show()

mean_flow = np.trapz(Q, durations)
total_power = np.trapz(P, durations) * 24 * 365 / 1e3  # Convert to kWh

print(f"Mean flow: {mean_flow} m³/s")
print(f"Total power generated over the year: {total_power} kWh")

OMR = 200000  # Operations and maintenance costs ($/year)
r = 0.03  # Interest rate (3%)
n = 50  # Lifetime of the power plant (years)
electricity_price = 0.05  # $/kWh

CRF_n = r * (1 + r)**n / ((1 + r)**n - 1)
annual_income = total_power * electricity_price

# TAC = CRF_n * C0 + OMR
# The plant is feasible if the annual income equals the total annual cost:
# annual_income = TAC

C0 = (annual_income - OMR) / CRF_n

print(f"Construction cost at which the plant would be feasible: ${C0:.2f}")
