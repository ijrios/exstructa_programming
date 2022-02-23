# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:51:45 2022

@author: jario
"""

#Implementar un programa que calcule la factorial de un número 
# utilizando la tecnica de recursividad

def numeros(num,i):
    if(num <= 10):
        print("ciclo_"+str(i),"--->" ,num)
        numeros(num+1,i+1)
           
def factorial(num):
    if(num >0):
        return num*factorial(num-1)
    else:
        return 1
        

def main():
    #numeros(0,1)
    y = 5
    x = factorial(y)
    print(str(y)+"!=",x)
    
main()

