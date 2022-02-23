# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:12:57 2022

@author: jario
"""

#Implementar un programa que genere una pila utilizando 
#estructuras dinamicas y desapilar los elementos con una funcion recursiva


class Nodo:
    
    def __init__(self,valor,sig=None):
        #Condicion inicial del nodo vacío
        self.valor = valor
        self.sig =sig
        
class Pila:
    #pass #cuando está sin metodos
    #pila vacía tiene cabeza y no cola
    def __init__(self): 
        self.cabeza = None
        
    def apilar(self,valor):
        nodo = Nodo(valor)
        if(self.cabeza == None):
            #si está vacía el primer elemento que ingrese es cabeza
            self.cabeza = nodo
        else:
            # Se le añade un elemento a la lista
            # Se enlaza el nuevo elemento a la pila con el primero
           
            nodo.sig = self.cabeza
            #Se actualiza cabeza
            self.cabeza = nodo
            
        
    def desapilar(self):
        
        if(self.cabeza == None):
            return None
        else:
            nodo = self.cabeza
            self.cabeza = self.cabeza.sig
            nodo.sig = None
            return nodo.valor
        
    def show(self):
        
        n = self.cabeza
        while(n != None):
            print(n.valor)
            n = n.sig
        
def desapilartodos(pila):
    if(pila.cabeza == None):
        return 
    valp= pila.desapilar()
    print("Elemento desapilado: ", valp)
    desapilartodos(pila)
        
def main():
    
    pila = Pila()
    pila.apilar("Puede que lo encuentres y tambien puedas entrar")
    pila.apilar("Dicen que si esperas y te sientas en silencio")
    desapilartodos(pila)
       
main()
