# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:14:52 2022

@author: jario
"""

import random

class Nodo:
    
    def __init__(self,valor,sig=None):
        #Condicion inicial del nodo vacío
        self.valor = valor
        self.sig =sig
        
class Lista:
    #Condición inicial de la lista vacía
    def __init__(self,cabeza=None,cola=None): 
        self.cabeza = cabeza
        self.cola = cola
        
    def ad_valor(self,valor):
        #La lista está vacia
        if(self.cabeza == None):
            #Si está vacía el primer elemento que ingrese es cabeza y cola
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            #Se le añade un elemento a la lista
            n = Nodo(valor)
            self.cola.sig = n
            self.cola = n
            
    def __str__(self):
        n = self.cabeza
        str_rep =""
        while(n is not None):
            str_rep += "["+str(n.valor)+"]"
            n = n.sig
        return str_rep
    
    def metodoBurbuja(self):
        #Se debe ordenar primero antes de realizar busqueda binaria
        if(self.cabeza != None):
          actual = None
          estado = 1
          while(estado == 1):
            estado = 0
            actual = self.cabeza
            while(actual != None and actual.sig != None):
                #Cuando el valor del nodo actual es menor que el del nodo anterior
                if(actual.valor > actual.sig.valor):
                    #Intercambiar valores de nodo
                    actual.valor=actual.valor+actual.sig.valor
                    actual.sig.valor=actual.valor - actual.sig.valor
                    actual.valor=actual.valor - actual.sig.valor
                    estado=1
        
                actual=actual.sig

        else:
           print("Lista vacía")
    
        
    #Devuelve el nodo medio en el rango dado
    def valorMedio(self, primero, ultimo) :
        #Algunas variables auxiliares
        medio = primero
        temp = primero.sig
		#Encuentra el nodo medio
        while (temp != None and temp != ultimo) :
            temp = temp.sig 
            if (temp != ultimo) :
				#Visita al siguiente nodo
                medio = medio.sig
                temp = temp.sig
                
        return medio
	
	#Esto está realizando la operación de búsqueda binaria.
    def busquedaBinaria(self, valorb) :
        if (self.cabeza == None) :
            print("\n Lista vacía", end = "")
            return
		
		#Algunas variables auxiliares
        primero = self.cabeza
        ultimo = self.cola
        resultado = None
        medio = self.cabeza
        if (primero.valor == valorb) :
			#Cuando busque el primer elemento
            resultado = primero
		
        if (ultimo.valor == valorb) :
			#Al buscar el último elemento
            resultado = ultimo
		
		#Este bucle detecta un elemento dado mediante la búsqueda binaria.
        while (resultado == None and medio != None and primero != ultimo) :
			#Primero encuentra el elemento medio
            medio = self.valorMedio(primero, ultimo)
            if (medio == None) :
				#Esto es útil cuando no sabemos sobre el último nodo inicial 
				#y el elemento de búsqueda es más grande que el último nodo
                resultado = None
            elif (medio.valor == valorb) :
				#Cuando obtenga el nodo de búsqueda
                resultado = medio
            elif (medio.valor > valorb) :
				#Seleccionar nuevo último nodo
                ultimo = medio
            else :
				#Seleccionar nuevo nodo inicial
                primero = medio.sig
			
		
        if (resultado != None) :
            print("Elemento dado", valorb,"está presente", end = " ")
            
        else :
            print("Elemento dado", valorb ,"no está presente", end = " ")
		
def inicializar():
    random.seed(28)
    lis = Lista()
    for i in range(22):
        lis.ad_valor(random.randint(1,10))
    return lis 

def main():
    lis = inicializar()
    print("Lista Original")
    print(lis)
    print("\n")
    
    lis.metodoBurbuja()
    print("Lista Organizada")
    print(lis)
    print("\n")
    
    print("Busqueda Binaria")
    lis.busquedaBinaria(3)
    print("\n")
    
main()
