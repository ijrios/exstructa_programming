# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:14:31 2022

@author: jario
"""

#Metodo de buscar recursivo, tomando la lista y el elemento

def buscar(lista, elemento):
    def buscar_rec(lst, ele):
        if(lst[0] == ele and lst != None):
            return True
        return buscar_rec(lst[1:], ele)
    try: return buscar_rec(lista, elemento)
    except IndexError: return -1


def main():
   
    lista = []
    lista = ["hola","alo","hi","hello"]
    lista.append("HELO")

         
    for i in range(100):
        numb = "ho"
        find = buscar(lista,numb)
    
    print("(-1:No find) - Número",numb,"-",find)
    print(lista)
        
main()