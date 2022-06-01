# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:31:08 2022

@author: jario
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt

#Leemos el archivo con el Dataframe de pandas
data = pd.read_parquet('./archivo_final.parquet')
muestra = data[:9].copy()
s = data['Patrimonio']
Nombres = data['Nombre']
plt.pie(s, labels=Nombres, autopct="%0.1f %%")
plt.title("Patrimonio neto(Porcentaje) ")
plt.axis("equal")
plt.show()
axis = data.plot(kind='bar',y='Patrimonio',rot=0, ylabel = 'Patrimonio (en miles de millones de dólares)',x="SN",color='g')
plt.show()
print(data)

