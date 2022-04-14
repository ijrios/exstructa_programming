# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:22:07 2022

@author: jario
"""


class Nodo:
    
    def __init__(self,valor,sig=None):
        #Condicion inicial del nodo vacío
        self.valor = valor
        self.siguiente =sig
        
class ControlLista:
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
            # Se le añade un elemnto a la lista
            n = Nodo(valor)
            self.cola.siguiente = n
            self.cola = n 
        
  
def main():
    
    lista_simple = ControlLista()
    #Llenar la lista
    for i in range(100,110):
        lista_simple.ad_valor(i)
        
    #Recorrer la lista
    n = lista_simple.cabeza
    while(n != None):
        print(n.valor)
        n = n.siguiente
        

def main2():
    n1 = Nodo(4)
    n2 = Nodo(5)
    n3 = Nodo(-5)
    n1.siguiente = n2
    n2.siguiente = n3
    
    n = n1
    while(n != None):
        print(n.valor)
        n = n.siguiente

main()