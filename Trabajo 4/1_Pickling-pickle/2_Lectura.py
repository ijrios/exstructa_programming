# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:09:39 2022

@author: jario
"""

import pickle
import pandas as pd
import matplotlib.pyplot as plt

#Leemos el archivo con pandas
unpickled_df = pd.read_pickle("./filename.pickle")  

#------------------- Graficas ------------------------ 
unpickled_df.groupby(['Ciudad','Genero']).size().unstack().plot(kind='bar',stacked=True,ylabel="")
plt.show()
muestra = unpickled_df[:9].copy()
s = unpickled_df['Faltas']
Nombres = unpickled_df['Nombre']
plt.pie(s, labels=Nombres, autopct="%0.1f %%")
plt.title("Faltas por cada alumno (Porcentaje) ")
plt.axis("equal")
plt.show()
print(unpickled_df)