# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:28:04 2022

@author: jario
"""


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
    pila = Pila()
    pila.apilar(" es decir, el mundo pensado, modelo del mundo sensible")
    pila.apilar("Su pensamiento o Su razón (Logos) el mundo de las Ideas,")
    pila.apilar("   El primer día de la creación Dios concibió en")
    pila.apilar("--------------------------------------------------")
    pila.apilar("-------------Pienso luego existo------------------")
    pila.apilar("--------------------------------------------------")
    pila.apilar("   ya que de él procedéis (y) a él tornaréis.")
    pila.apilar("        vosotros encontraréis el Reino,")
    pila.apilar("        Bienaventurados los solitarios:")
    pila.apilar("Miguelito")
    
    val = pila.desapilar()
    print("Valor por fuera: ", val)
    print("Lista..............")
    pila.show()
    
main()