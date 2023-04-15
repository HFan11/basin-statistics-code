# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 01:39:55 2023

@author: Administrator
"""

import numpy as np

Qm = 10  # mean baseflow
QA = 5   # amplitude of the seasonal variation
days_in_year = 365
t = np.arange(days_in_year)

Qs = Qm + QA * np.cos(2 * np.pi * t / days_in_year + np.pi)
Qs_sorted = np.sort(Qs)[::-1]  # sort the slow flow values in descending order
P_slow = np.arange(1, days_in_year + 1) / days_in_year

Qmin = 1  # minimum fast flow
Q0 = 10   # initial fast flow
k = 0.1   # recession constant
n = 20    # number of identical recessions

t_event = np.linspace(0, days_in_year, n)
Qf = np.zeros(days_in_year)

for i in range(n):
    Qf += np.piecewise(t, [t < t_event[i], t >= t_event[i]], [0, lambda t: Qmin + (Q0 - Qmin) * np.exp(-k * (t - t_event[i]))])
Qf_sorted = np.sort(Qf)[::-1]  # sort the fast flow values in descending order
P_fast = np.arange(1, days_in_year + 1) / days_in_year
Q = Qs + Qf
Q_sorted = np.sort(Q)[::-1]  # sort the total flow values in descending order
P_total = np.arange(1, days_in_year + 1) / days_in_year
import matplotlib.pyplot as plt

plt.figure()
plt.plot(Qs_sorted, P_slow, label='Slow Flow')
plt.plot(Qf_sorted, P_fast, label='Fast Flow')
plt.plot(Q_sorted, P_total, label='Total Flow')
plt.xlabel('Flow')
plt.ylabel('Cumulative Probability')
plt.title('Flow Duration Curves')
plt.legend()
plt.grid()
plt.show()
