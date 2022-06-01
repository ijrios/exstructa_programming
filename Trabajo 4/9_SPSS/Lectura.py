# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:08:06 2022

@author: jario
"""

import pandas as pd
import savReaderWriter
import matplotlib.pyplot as plt


#with savReaderWriter.SavReader('./survey.sav', ioUtf8 = True) as reader:
    #df = pandas.DataFrame(reader.all(), columns = [s.decode('CP1252') for s in reader.header])
#df.head()

df = pd.read_spss('./survey.sav')
df1 = pd.read_spss('./experim.sav')
#------------------- Graficas ------------------------ 
data_1 = df['age'].mean()
edad = df1['age']
sexo = df['sex']
data_2 = df['age'].min()
data_3 = df['age'].max()
data_4 = df['sex']
edad.plot()
plt.title("Distribución de edades encuestados")

print(df1)
print("Promedio de edades",data_1)
print("Edad minima",data_2)
print("Edad maxima",data_3)
