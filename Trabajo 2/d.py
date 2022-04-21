import matplotlib.pyplot as plot
import random

#crear un arbol binario simple
def crearArbol(lista):
    if len(lista) == 0:
        return None
    else:
        return Arbol(lista[0], crearArbol(lista[1:]), crearArbol(lista[1:]))
def preorden(arbol):
    if arbol == None:
        return
    else:
        print(arbol.dato, end=" ")
        preorden(arbol.izq)
        preorden(arbol.der)
def inorden(arbol):
    if arbol == None:
        return
    else:
        inorden(arbol.izq)
        print(arbol.dato, end=" ")
        inorden(arbol.der)
def postorden(arbol):
    if arbol == None:
        return
    else:
        postorden(arbol.izq)
        postorden(arbol.der)
        print(arbol.dato, end=" ")
        
#buscar en profundidad arbol binario 
def buscar(arbol, dato, contador):
    if arbol == None:
        
        contador += 1
        return contador
    else:
        if arbol.dato == dato:
            contador += 1
            return contador
        else:
            if dato < arbol.dato:
                contador += 1
                return buscar(arbol.izq, dato, contador)
            else:
                contador += 1
                return buscar(arbol.der, dato, contador)
            
class Arbol:
    def __init__(self, dato, izq = None, der = None):
        self.dato = dato
        self.izq = izq
        self.der = der
        
def main():
    
    Lista = []
    for i in range(500):
        Lista.append(random.randint(1, 1000))
    
    arbol = crearArbol(Lista)
    
    NumerosBuscar = []
    NumeroDeIteraciones = []
    
    for i in range(10):
        contador = 0
        Num = random.randint(1, 1000)
        NumerosBuscar.append(Num)
        NumeroDeIteraciones.append(buscar(arbol,Num,contador))
    
    print(NumerosBuscar)
    print(NumeroDeIteraciones)
    plot.hist(NumeroDeIteraciones)
    plot.show()
    
main()