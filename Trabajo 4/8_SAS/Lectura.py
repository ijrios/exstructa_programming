# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:46:49 2022

@author: jario
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_sas('./sterling.sas7bdat',format='sas7bdat')
df.plot()
plt.title("Tipo del cambio del euro con la libra")

print(df)