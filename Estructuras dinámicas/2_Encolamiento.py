# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:26:36 2022

@author: jario
"""

# Las colas son colecciones donde los nuevos elementos se ingresan al final de la serie

class Nodo:
    
    def __init__(self,valor,sig=None):
        #Condicion inicial del nodo vacío
        self.valor = valor
        self.sig =sig
        
class Cola:
    #pass #cuando está sin metodos
    #Lista vacía sin cola y cabeza
    def __init__(self): 
        self.cabeza = None
        self.cola = None
        
    def encolar(self,valor):
        
        if(self.cabeza == None):
            nodo = Nodo(valor)
            #si está vacía el primer elemento que ingrese es cabeza y cola
            self.cabeza = nodo
            self.cola = nodo
        else:
            # Se le añade un elemento a la lista
            # Se enlaza el nuevo elemento con el ultimo 
            n = Nodo(valor)
            self.cola.sig = n
            #Se actualiza cola
            self.cola = n
        
    def desencolar(self):
        
        if(self.cabeza != None):
            nodo = self.cabeza
            self.cabeza = self.cabeza.sig
            nodo.sig = None
            return nodo.valor
        else:
            return None
        
    def show(self):
        
        n = self.cabeza
        while(n != None):
            print(n.valor)
            n = n.sig
        
def main():
    
    lista_simp = Cola()
    lista_simp.encolar("Hola")
    lista_simp.encolar("Casa")
    lista_simp.encolar("Carro")
    
    val = lista_simp.desencolar()
    print("Valor por fuera: ", val)
    print("Lista..............")
    lista_simp.show()
    
main()
         
        

