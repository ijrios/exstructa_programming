# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:47:24 2022

@author: jario
"""

import pandas as pd
import pyarrow.feather as feather
import matplotlib.pyplot as plt

#Leemos sin pandas
with open("./archivo.ftr", 'rb') as f:
    read_df = feather.read_feather(f)
    
#Leemos con pandas
data = pd.read_feather('./archivo.ftr')

# Graficamos
muestra = data[:9].copy()
axis = muestra.plot(kind='bar',y='roundtriptime',rot=0, ylabel = 'Tiempo de ida y vuelta',xlabel='Servidores',color='g')
plt.show()
print(data)