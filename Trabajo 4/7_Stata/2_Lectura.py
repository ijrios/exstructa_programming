# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:28:11 2022

@author: jario
"""

import pandas as pd
import matplotlib.pyplot as plt

#Leemos el archivo con el dataframe
data = pd.read_stata('archivo.dta')
   
data.plot(x="Persona", y=["Peso", "Edad", "IMC"], kind="bar",figsize=(9,8))
plt.title("Información de pacientes")
plt.show()

print(data)