# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:33:10 2022

@author: b12s307e22
"""

#DEFINICION 
#================================================
# separador de campo = ";"
# separador de registro = "\n"
#================================================

sep = ";"
sep_reg = "\n"

archivo = open('prueba.txt','w')

nom = "juan"
eda = 23
tel = "43743734734"

linea = nom+sep+str(eda)+sep+tel+sep_reg
archivo.write(linea)

archivo.close()
