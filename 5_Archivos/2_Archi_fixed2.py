# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:32:25 2022

@author: b12s307e22
"""

archivo = open('prueba_fixed.txt','r')

archivo.seek(73*4,0)

nom_f = archivo.read(50)
eda_f = archivo.read(3)
tel_f = archivo.read(20)

#retirar los rellenos
nom = nom_f.replace(" ", "") 
eda = int(eda_f)
tel = tel_f.replace(" ", "") 


print(nom)
print(eda)
print(tel)


#for li in archivo:
#    print(li)
    
    
    
archivo.close()