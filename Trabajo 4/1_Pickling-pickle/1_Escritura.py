# -*- coding: utf-8 -*-
"""
Created on Sat May 21 14:22:42 2022

@author: jario
"""
import pickle
import pandas as pd

#Se inicializan los datos, se crea diccionario
data = {'ID': {0: 23, 1: 43, 2: 12,
              3: 13, 4: 67, 5: 89,
              6: 90, 7: 56, 8: 34}, 
       'Nombre': {0: 'Ram', 1: 'Deep',
                2: 'Yash', 3: 'Aman', 
                4: 'Arjun', 5: 'Aditya',
                6: 'Divya', 7: 'Chalsea',
                8: 'Akash' }, 
       'Faltas': {0: 22, 1: 12, 2: 4, 3: 7,
                 4: 2, 5: 8, 6: 13, 7: 24,
                 8: 8}, 
       'Nota': {0: 2.5, 1: 3.4, 2: 3.8, 3: 4.2,
                 4: 3.3, 5: 2.2, 6: 2.7, 7: 3.7,
                 8: 4.6},
       'Genero': {0: 'M', 1: 'M', 2: 'M', 3: 'F',
                 4: 'M', 5: 'F', 6: 'F', 7: 'F',
                 8: 'M'},
       'Ciudad': {0: 'Bello', 1: 'Medellín', 2: 'Bello', 3: 'Copacabana',
                 4: 'Medellín', 5: 'Medellín', 6: 'Medellín', 7: 'Medellín',
                 8: 'Caldas'}
      }

df = pd.DataFrame(data)
#a =  pd.DataFrame({"foo": range(5), "bar": range(5, 10)})  

with open('filename.pickle', 'wb') as f:
    pickle.dump(df, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as f:
    b = pickle.load(f)
    print("Archivo generado",'------>', 'filename.pickle')


