# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:16:14 2022

@author: jario
"""

# Recursivida
# El metodo recursivo se llama así mismo, se implementa con pilas

def numeros(num,i):
    if(num < 10):
        print(i,"--->" ,num)
        numeros(num+1,i+1)
           

def main():
    numeros(0,1)
    
main()
        
# Si el problema es recurisvo la implementación se simplifica