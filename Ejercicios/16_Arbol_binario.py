# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:17:58 2022

@author: jario
"""

#Arboles Binarios

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
                if(nodocontrol.derecho == None):
                    nodocontrol = nodocontrol.derecho
                else:
                    nodocontrol = nodocontrol.izquierdo
                
            #nodo control ---->  None
            if(anterior.izquierdo == None):
                anterior.izquierdo = n
            else:
                anterior.derecho = n
                
            
    #Se añade valor   
    def add_binario(self,valor):
        n = Nodo(valor)
        if(self.raiz == None):
            self.raiz = n
        else:
            #Arbol semibalanceado binario
            nodocontrol = self.raiz
            anterior = None
            while(nodocontrol != None):
                anterior = nodocontrol
                if(n.val < nodocontrol.val):
                    nodocontrol = nodocontrol.izquierdo
                elif(n.val > nodocontrol.val):
                    nodocontrol = nodocontrol.derecho
                elif(n.val == nodocontrol.val):
                    print("Valor " + str(n.val) + " ya ingresado")
                    # Puede ser --- nodocontrol = None
                    break
                    
            #nodo control ---->   < o >    
            if(n.val < anterior.val):
                anterior.izquierdo = n
            elif(n.val > anterior.val):
                anterior.derecho = n
                
                     
    def preOrden(self):
        self.preOrden_recur(self.raiz)
        
    def preOrden_recur(self,nodo):
        print(nodo.val)
        if(nodo.izquierdo != None):
            self.preOrden_recur(nodo.izquierdo)
        if(nodo.derecho != None):
            self.preOrden_recur(nodo.derecho)
                
    def inOrden(self):
        self.inOrden_recur(self.raiz)
        
    def inOrden_recur(self,nodo):
        if(nodo.izquierdo != None):
            self.inOrden_recur(nodo.izquierdo)
        print(nodo.val)
        if(nodo.derecho != None):
            self.inOrden_recur(nodo.derecho)
        
    def posOrden(self):
        self.posOrden_recur(self.raiz)
        
    def posOrden_recur(self,nodo):
        if(nodo.izquierdo != None):
            self.posOrden_recur(nodo.izquierdo)
        if(nodo.derecho != None):
            self.posOrden_recur(nodo.derecho)
        print(nodo.val)
        
  
   
arbol = Arbol_simple()
arbol.add_binario(10)
arbol.add_binario(8)
arbol.add_binario(7)
arbol.add_binario(20)
arbol.add_binario(22)
arbol.add_binario(5)
arbol.add_binario(4)
arbol.preOrden()
    