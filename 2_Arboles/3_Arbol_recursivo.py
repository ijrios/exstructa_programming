# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:17:34 2022

@author: jario
"""

# Crear un metodo recursivo para crear y llenar arbol

class Nodo:
    
    def __init__(self, valor):
        self.val = valor
        self.izquierdo = None
        self.derecho = None
        
class Arbol:
    
    #Nodo vacío
    def __init__(self):
        self.raiz = None
        
    #Se añade valor   
    def add_nodo(self,valor):
        n = Nodo(valor)
        
        if(self.raiz == None):
            self.raiz = n
        else:
            actual = self.raiz
            anterior = None
            while(actual != None):
                anterior = actual
                if(actual.derecho == None):
                    actual = actual.derecho
                elif (actual.izquierdo == None):
                    l = actual.izquierdo 
                else:
                    actual = actual.izquierdo
                    
            if(anterior.izquierdo == None):
                anterior.izquiedo = n
            elif(anterior.derecho == None):
                anterior.derecho = n
                
    def insertar(self,val):
        n = Nodo(val)
        if(self.raiz == None):
            self.raiz = n
        else:
            self.insertar_rec(self.raiz, n)
            
    def insertar_rec(self, anterior, n):
        
        if(anterior.izquierdo == None):
            anterior.izquierdo = n
        elif(anterior.derecho == None):
            anterior.derecho = n
        else:
            self.insertar_rec(anterior.izquierdo, n)
        
                
ar2 = Arbol()
'''
ar.add_nodo("A")
ar.add_nodo("B")
ar.add_nodo("C")
ar.add_nodo("D")
ar.add_nodo("E")
ar.add_nodo("F")
'''      
ar = Arbol()
ar.insertar("A")
ar.insertar("B")
ar.insertar("C")
ar.insertar("D")
ar.insertar("E")
ar.insertar("F")     