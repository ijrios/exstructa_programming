# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:29:42 2022

@author: jario
"""
import numpy as np
import pandas as pd
import h5py

# Abriendo archivo 'f'
with h5py.File('copia.hdf5', 'r') as f:
    data = f['default'][()]
    f.close()
    
df1 = pd.read_hdf('original.hdf5')
#Para seleccionar un dato en especifico
promedio_1 = df1['Duber']
promedio_2 = df1['Jose']
promedio_1.mean()
promedio_2.mean()

#Graficar nota más alta
#df_prices = df1.groupby("Duber").agg([np.mean, np.std])
df1.mean().plot(kind='bar',color="g",title="Nota final")
df1.std().plot(kind='bar',color="b",title="Nota final")
      
print("  Dataframe pandas\n", df1)
print(df1.describe())