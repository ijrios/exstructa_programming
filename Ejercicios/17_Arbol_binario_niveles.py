# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:13:01 2022

@author: jario
"""

#Arboles Binarios, recorridos por niveles

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
                
            #nodo control ---->   None
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
        
    def niveles(self):
        h = self.altura(self.raiz)
        for i in range(1, h+1):
            self.niveles_recur(self.raiz, i)
        
    def niveles_recur(self,nodo,nivel):
        if nodo is None:
            return
        if nivel == 1:
            print(nodo.val)
        elif nivel > 1:
            self.niveles_recur(nodo.izquierdo, nivel-1)
            self.niveles_recur(nodo.derecho, nivel-1)
       
    def altura(self,nodo):
        if nodo is None:
            return 0
        else:
            # Calcula la altura de cada subárbol
            # El metodo se va a llamar hasta que llegue al criterio de parada
            lh = self.altura(nodo.izquierdo)
            rh= self.altura(nodo.derecho)
     
            #Luego de terminar el criterio quedan las dos en 0 y se incrementa cada que se hace la llamada recursiva
            if lh > rh:
                return lh+1
            else:
                return rh+1
 
 
arbol = Arbol_simple()
arbol.add_binario(10)
arbol.add_binario(8)
arbol.add_binario(7)
arbol.add_binario(20)
arbol.add_binario(22)
arbol.add_binario(5)
arbol.add_binario(4)
arbol.niveles()
    