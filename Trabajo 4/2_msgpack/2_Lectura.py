# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:09:39 2022

@author: jario
"""
import pandas as pd
import msgpack 
import matplotlib.pyplot as plt

# Lectura del archivo msgpack 
with open("data.msgpack", "rb") as data_file:
    byte_data = data_file.read()

data = msgpack.unpackb(byte_data, strict_map_key=False)
df = pd.DataFrame(data)

#------------------- Graficas ------------------------ 

muestra = df[:9].copy()
s = df['Faltas']
Nombres = df['Nombre']
plt.pie(s, labels=Nombres, autopct="%0.1f %%")
plt.title("Faltas por cada alumno (Porcentaje) ")
plt.axis("equal")
plt.show()
print(df)