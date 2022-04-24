import matplotlib.pyplot as plot
import random, time, math

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
inicial = time.time_ns()

for i in range(1000):
    arbol = insertar(arbol,random.randint(1, 1000))
print('Tiempo generando la lista ms',str((time.time_ns()-inicial)/1000000))

NumerosBuscar = []
NumeroDeIteraciones = []

TiempoEjecuciones = []
for i in range(500):
    inicial = time.time_ns()
    contador = 0
    Num = random.randint(1, 1000)
    NumerosBuscar.append(Num)
    NumeroDeIteraciones.append(buscar(arbol,Num,contador))
    final = time.time_ns()
    TiempoEjecuciones.append(final-inicial)

plot.hist(NumeroDeIteraciones)
plot.title("Numero de Iteraciones")
plot.ylabel("Frecuencia")
plot.xlabel("Numero de comparaciones")
plot.grid()
plot.show()
plot.bar(list(range(1,len(TiempoEjecuciones)+1)),TiempoEjecuciones)
plot.title("Tiempo de ejecucion busqueda de cada elemento")
plot.ylabel('Tiempo de ejecucion ns')
plot.xlabel('# de ejecución')
plot.grid()
plot.show()
print('Tiempo medio de ejecución ns: ',(sum(TiempoEjecuciones))/len(TiempoEjecuciones))
mean = sum(TiempoEjecuciones) / len(TiempoEjecuciones)
var = sum((l-mean)**2 for l in TiempoEjecuciones) / len(TiempoEjecuciones)
st_dev = math.sqrt(var)
print('Desviación estandar ns: ', str(st_dev))
print('Max tiempo de ejecución ns: ', max(TiempoEjecuciones))