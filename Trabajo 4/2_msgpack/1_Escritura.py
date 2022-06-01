# -*- coding: utf-8 -*-
"""
Created on Sat May 21 14:50:57 2022

@author: jario
"""

import pandas as pd
import msgpack 


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
       'Grado': {0: 'B', 1: 'A', 2: 'F', 3: 'C',
                 4: 'E', 5: 'C', 6: 'A', 7: 'B',
                 8: 'B'}
      }

#df = pd.DataFrame(data)

#Escritura del archivo
with open("data.msgpack", "wb") as outfile:
    packed = msgpack.packb(data)
    outfile.write(packed)
    print("Archivo creado","------>","data.msgpack")


