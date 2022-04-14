# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:40:05 2022

@author: jario
"""

#Los arboles son estructuras de datos
#que disponen sus elementos según
#el concepto de árbol en la naturaleza, 
#se puede intuir que se trata de una estructura jerarquica
#Cuando el alrbol es recargado a la izquierda, queda con una complejidad de n

#Orden: numero de hijos
#Altura: Cantidad de niveles 

class Nodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        
class Arbol_simple:
    
    #Nodo vacío
    def __init__(self):
        self.raiz = None
        
    #Se añade valor   
    def add_nodo(self,valor):
        n = Nodo(valor)
        if(self.raiz == None):
            self.raiz = n
        else:
            #Arbol desbalanceado
            nodocontrol = self.raiz
            anterior = None
            while(nodocontrol != None):
                anterior = nodocontrol
                if(nodocontrol.derecho == None):
                    nodocontrol = nodocontrol.derecho
                else:
                    nodocontrol = nodocontrol.izquierdo
                
            if(anterior.izquierdo == None):
                anterior.izquierdo = n
            else:
                anterior.derecho = n
                
    def preOrden(self):
        self.preOrden_recur(self.raiz)
        
    def preOrden_recur(self,nodo):
        print(nodo.valor)
        if(nodo.izquierdo != None):
            self.preOrden_recur(nodo.izquierdo)
        if(nodo.derecho != None):
            self.preOrden_recur(nodo.derecho)
                
    def inOrden(self):
        self.inOrden_recur(self.raiz)
        
    def inOrden_recur(self,nodo):
        if(nodo.izquierdo != None):
            self.inOrden_recur(nodo.izquierdo)
            print(nodo.valor)
        if(nodo.derecho != None):
            self.inOrden_recur(nodo.derecho)
        
    def posOrden(self):
        self.posOrden_recur(self.raiz)
        
    def posOrden_recur(self,nodo):
        if(nodo.izquierdo != None):
            self.posOrden_recur(nodo.izquierdo)
        if(nodo.derecho != None):
            self.posOrden_recur(nodo.derecho)
            print(nodo.valor)
       

    
arbol = Arbol_simple()
arbol.add_nodo("A")
arbol.add_nodo("B")
arbol.add_nodo("C")
arbol.add_nodo("D")
arbol.add_nodo("E")
arbol.add_nodo("F")
arbol.add_nodo("G")
arbol.preOrden()
    