# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 01:22:37 2023

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

t_avg_values = [0.25, 0.5, 1.0, 2.0, 4.0]
t = np.linspace(0, 1, 1000)

plt.figure()

for t_avg in t_avg_values:
    q_t = t_avg * np.exp(-t_avg * t) / (1 - np.exp(-t_avg))
    plt.plot(t, q_t, label=f"t_avg = {t_avg}")

plt.xlabel("Normalized Time (t/tb)")
plt.ylabel("Flow (q/q')")
plt.title("Flow Duration Curves")
plt.legend()
plt.grid()
plt.show()
