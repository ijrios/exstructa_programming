# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:35:52 2022

@author: jario
"""

'''
Analisis de datos:
Implementar un programa que cree una lista de 50000 numeros
aletorios y a continuación cree un metodo para buscar un elemento
dentre de esa lista, no returna f o v el metodo returnará el 
numero de comparaciones realizadas hasta encontrar el elemento

- Graficar un histograma con los resultados obtenidos en el experimento
'''
import random
import matplotlib.pyplot as plt


def buscar(lista,elemento):
    contador = 0
    for x in lista:
        if(x==elemento):
            return contador+1
        else:
            contador += 1
    return contador
    

def main():
   
    lista = []
    lista_contador=[]
    random.seed(10)
    
    lista = [random.randint(1,20) for i in range(1000)]

         
    for i in range(100):
        numb = random.randint(0,10)
        #Cuando tengo caos (incertidumbre) en el ingreso
        #El algoritmo tiende hacer todas las repeticiones
        find = buscar(lista,numb)
        lista_contador.append(find)
    
    
    print("Numero de comparaciones para",numb,"----->",find)
    print(lista_contador)
    
    plt.hist(lista_contador)
    plt.show
         

        
main()
