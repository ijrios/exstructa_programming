# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:31:33 2022

@author: jario
"""

import pandas as pd

#Creamos archivo
datos = {
    'Persona': ["Rakesh", "Kishan", "Adesh", "Nitish"],
    'Peso': [50, 60, 70, 80],
    'Edad': [22, 35, 18, 64],
    'IMC': [19.1, 22.4, 26.8, 30.9],

}

df = pd.DataFrame(data=datos)
  
#Usamos pandas.DataFrame.to_stata metodo
df.to_stata('archivo.dta')
print("Escribiendo archivo","---->","archivo.dta")
