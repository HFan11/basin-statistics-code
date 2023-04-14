# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 23:47:56 2023

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt


file_path = 'MOPEX_Daily.xlsx'
sheet_name = '262_30years'
df = pd.read_excel(file_path, engine='openpyxl', sheet_name=sheet_name, usecols=[0, 3, 5], names=['Year', 'Precipitation', 'Runoff'])



precipitation_sorted = df['Precipitation'].sort_values(ascending=False)
runoff_sorted = df['Runoff'].sort_values(ascending=False)

total_data_points = len(df)
cumulative_prob_precipitation = [(i+1) / total_data_points for i in range(total_data_points)]
cumulative_prob_runoff = [(i+1) / total_data_points for i in range(total_data_points)]


plt.subplot(1, 2, 1)
plt.plot(cumulative_prob_precipitation, precipitation_sorted, label='Precipitation')
plt.xlabel('Cumulative Probability')
plt.ylabel('Precipitation (mm/day)')
plt.title('Precipitation Duration Curve')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(cumulative_prob_runoff, runoff_sorted, label='Runoff')
plt.xlabel('Cumulative Probability')
plt.ylabel('Runoff (mm/day)')
plt.title('Flow Duration Curve')
plt.grid()

plt.tight_layout()
plt.show()
