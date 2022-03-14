# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:09:02 2022

@author: jario
"""

import random

class Nodo:
    
    def __init__(self,valor,sig=None):
        #Condicion inicial del nodo vacío
        self.valor = valor
        self.sig =sig
        
class Lista:
    #Condicion inicial de la lista vacía
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
    
def inicializar():
    random.seed(52)
    lis = Lista()
    for i in range(10):
        lis.ad_valor(random.randint(1,8))
    return lis 

def mostrar_rec(n):
    if(n is not None):
        print(n.val,"-",end="")
        mostrar_rec(n.sig)
        
def invertir(lista_original):
    lis = Lista()
    crear_copia_inv(lista_original.cabeza,lis)
    return lis

def crear_copia_inv(n,lis_new):
    if(n is not None):
        crear_copia_inv(n.sig,lis_new)
        lis_new.ad_valor(n.valor)
        
# Rcurrrencia recursividad 
def retirar_ocurrencia(n,lis,elemento):
    if(n is not None):
        if(n == elemento):
            n  = n.sig
            lis.cabeza = n
        elif(n.sig != None and n.sig.valor == elemento):
            n.sig = n.sig.sig
        retirar_ocurrencia(n.sig,lis,elemento)
            
#Retirar sin recursividad 

def retirar(lis,elemento):
    n = lis.cabeza
    anterior = None
    while(n is not None):
        if(n.valor == elemento and anterior ==None):
            lis.cabeza = n.sig
        elif(n.valor == elemento and anterior != None):
            anterior.sig = n.sig
        else:
            anterior = n
        n = n.sig
            
def peso_rec(n):
    if(n is None):
        return 0
    else: 
        return n.valor + peso_rec(n.sig)

def contar_rec(n,elemento):
    if(n is not None):
        z = 0
        if(n.valor == elemento):
            z = 1
        return z+contar_rec(n.sig,elemento)
    else:
        return 0

def main():
    lis = inicializar()
    print("Lista Original")
    print(lis)
    print("\n")
    
    lisn = invertir(lis)
    print("Lista Invertida")
    print(lisn)
    print("\n")
    
    retirar(lis,7)
    print("Lista nueva con valor eliminado")
    print(lis)
    print("\n")
    
    pes = peso_rec(lis.cabeza)
    print("Peso de la lista")
    print(pes)
    print("\n")
    
    num = 3
    cont = contar_rec(lis.cabeza,num)
    print("Cantidad de repeticiones del número "+str(num))
    print(cont)
    print("\n")

main()