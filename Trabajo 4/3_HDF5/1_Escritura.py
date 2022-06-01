# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:29:41 2022

@author: jario
"""

import pandas as pd
import h5py
 
#Se inicializan los datos, se crea diccionario con notas de estudiantes
dict = {'Duber': [3.2,2.8,2.1,4.5,3.8], 'Jose': [3.3,2.7,4.6,4.8,3.9], 'Jorge': [4.2,4.1,4.7,4.2,3.9]}
 
df = pd.DataFrame(dict, index=[0,1,2,3,4])
 
#Creando archivo 
df.to_hdf('original.hdf5', key='df', mode='w')
print("Creando Arcvivo","------>","original.hdf5")

with h5py.File('copia.hdf5', 'w') as f:
    dset = f.create_dataset("default", data = df)
    