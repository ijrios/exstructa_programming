# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:40:34 2022

@author: s205e19
"""

num_reg = 5
tam_reg = 73

archivo = open('prueba_fixed2.txt','r')


archivo.seek(tam_reg*4,0)

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