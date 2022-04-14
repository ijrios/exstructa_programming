# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:31:40 2022

@author: jario
"""

'''
Crear metodo recursivo para el metodo
 buscar elemento del ejercicio anterior
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
   
    def buscar_rec(self,elemento):
       return self.buscar_recursivo(self.cabeza,elemento)
   
    def buscar_recursivo(self,n,elemento):
       if(n != None and n.valor == elemento):
           return True
       elif(n == None):
           return False
       else:
           return self.buscar_recursivo(n.siguiente,elemento)
       
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