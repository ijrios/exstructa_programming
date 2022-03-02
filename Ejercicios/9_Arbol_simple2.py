# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:50:08 2022

@author: jario
"""

# Crear arbol de forma recursiva

class Nodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def Arbol(raiz):
    arbol = []

    recursion(raiz, arbol)
    return arbol

def recursion(raiz, arbol):

    if raiz is None:
        return
    
    recursion(raiz.derecho, arbol)
    
    recursion(raiz.izquierdo, arbol)

    arbol.append(raiz.valor)

    return
 
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

print(Arbol(raiz))