# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:51:59 2022

@author: jario
"""

# Generador de archivos
import random
random.seed(12345)
max_num = 10
number_files = 10


for j in range(number_files):
    archivo = open('testFile_'+str(j)+'.txt','w')
    for i in range(max_num): 
        x = random.randint(100, 999)
        archivo.write(str(x))
        archivo.write(",")
        
    archivo.close()