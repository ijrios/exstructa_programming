# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:33:42 2022

@author: jario
"""

#Los arboles son estructuras de datos
#que disponen sus elementos según
#el concepto de árbol en la naturaleza, 
#se puede intuir que se trata de una estructura jerarquica

#Orden: numero de hijos
#Altura: Cantidad de niveles 

class Nodo:
    
    def __init__(self, valor):
        self.val = valor
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
                if(nodocontrol.derecho != None):
                    nodocontrol = nodocontrol.derecho
                else:
                    nodocontrol = nodocontrol.izquierdo
                
            if(anterior.izquierdo == None):
                anterior.izquierdo = n
            else:
                anterior.derecho = n
    
arbol = Arbol_simple()
arbol.add_nodo("D")
arbol.add_nodo("B")
arbol.add_nodo("O")
    
    


                
         
        