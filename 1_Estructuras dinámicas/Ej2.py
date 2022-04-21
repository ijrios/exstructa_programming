# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:50:52 2022

@author: jario
"""

'''
Cree una lista de 100 elementos con numeros aleatorios
para la lista crear un metodo buscar elemento que indique
si un numero se encuentra o no dentro de la lista
'''

import random

class Nodo:
    
    def __init__(self,valor,sig=None):
        #Condicion inicial del nodo vacío
        self.valor = valor
        self.siguiente =sig
        
class Lista:
    #Condicion inicial de la lista vacía
    def __init__(self,cabeza=None,cola=None): 
        self.cabeza = cabeza
        self.cola = cola
        
    def ad_valor(self,valor):
        #lista está vacia
        if(self.cabeza == None):
            #si está vacía el primer elemento que ingrese es cabeza y cola
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            # Se le añade un elemento a la lista
            n = Nodo(valor)
            self.cola.siguiente = n
            self.cola = n
 
   
    def buscar(self,elemento):
       n = self.cabeza
       while(n != None):
           if(n.valor == elemento):
               return True
           n = n.siguiente
       return False

def main():
    
    lista_simple = Lista()
    #Llenar la lista
    for i in range(1,101):
        lista_simple.ad_valor(i*random.randint(0,10))
        
    #Recorrer la lista
    n = lista_simple.cabeza
    while(n != None):
        print(n.valor)
        n = n.siguiente
        
    print(lista_simple.buscar(40))
        
main()