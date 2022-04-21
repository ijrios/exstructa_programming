import matplotlib.pyplot as plot
import random

#crear un arbol binario de busqueda
def insertar(arbol, dato):
    if arbol == None:
        arbol = Nodo(dato)
    else:
        if dato < arbol.dato:
            arbol.izq = insertar(arbol.izq, dato)
        else:
            arbol.der = insertar(arbol.der, dato)
    return arbol
def inorden(arbol):
    if arbol != None:
        inorden(arbol.izq)
        print(arbol.dato, end=" ")
        inorden(arbol.der)
def preorden(arbol):
    if arbol != None:
        print(arbol.dato, end=" ")
        preorden(arbol.izq)
        preorden(arbol.der)
def postorden(arbol):
    if arbol != None:
        postorden(arbol.izq)
        postorden(arbol.der)
        print(arbol.dato, end=" ")
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

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

arbol = None
random.seed(28)

for i in range(1000):
    arbol = insertar(arbol,random.randint(1, 1000))

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