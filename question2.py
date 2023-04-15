# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 00:41:36 2023

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\Administrator\Desktop\CEE450\MOPEX_Daily.xlsx' #you need to change
sheet_name = '262_3years' #I choose the first 3 years in catchment 262
df_3years = pd.read_excel(file_path, engine='openpyxl', sheet_name=sheet_name, usecols=[0, 3, 5], names=['Year', 'Precipitation', 'Total_Flow'])

alpha = 0.925
fast_flow = [0]
base_flow = [0]

for i in range(1, len(df_3years)):
    qf = alpha * fast_flow[-1] + 0.5 * (1 + alpha) * (df_3years['Total_Flow'][i] - df_3years['Total_Flow'][i - 1])
    if qf < 0:
        qf = 0
    fast_flow.append(qf)
    base_flow.append(df_3years['Total_Flow'][i] - qf)

df_3years['Fast_Flow'] = fast_flow
df_3years['Base_Flow'] = base_flow

precipitation_sorted = df_3years['Precipitation'].sort_values(ascending=False)
total_flow_sorted = df_3years['Total_Flow'].sort_values(ascending=False)
fast_flow_sorted = df_3years['Fast_Flow'].sort_values(ascending=False)
base_flow_sorted = df_3years['Base_Flow'].sort_values(ascending=False)

total_data_points = len(df_3years)
cumulative_prob = [(i+1) / total_data_points for i in range(total_data_points)]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(cumulative_prob, precipitation_sorted, label='Precipitation')
plt.xlabel('Cumulative Probability')
plt.ylabel('Precipitation (mm/day)')
plt.title('Precipitation Duration Curve')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(cumulative_prob, total_flow_sorted, label='Total Flow')
plt.plot(cumulative_prob, fast_flow_sorted, label='Fast Flow')
plt.plot(cumulative_prob, base_flow_sorted, label='Slow (Base) Flow')
plt.xlabel('Cumulative Probability')
plt.ylabel('Flow (mm/day)')
plt.title('Flow Duration Curves')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
