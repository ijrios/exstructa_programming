# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:44:17 2022

@author: b12s307e22
"""

sep = ";"

archivo = open('prueba.txt','r')

li = archivo.readline()
nom,eda,tel = tuple(li[:-1].split(sep))
eda = int(eda)

print(nom)
print(eda)
print(tel)

print(type(eda))

#for li in archivo:
#    print(li)
    
    
    
archivo.close()