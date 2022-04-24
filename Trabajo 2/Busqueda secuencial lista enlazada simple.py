import matplotlib.pyplot as plot
import random
import time
import math

class Nodo:
    #en la clase nodo se encuentra el valor del nodo y el siguiente que es donde
    #apunta al siguiente nodo
    def __init__(self,valor,siguiente = None): #The init method is used to create an instance of the class
        self.valor = valor
        self.siguiente = siguiente
    
class ListaSimple:
    #pass para tener la clase vacia, sin ningun parametro
    #pass
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def add(self, valor):
        #creo un nuevo nodo
        nodo = Nodo(valor)
        
        #si la lista esta vacia, el primer nodo es cabeza y cola al mismo tiempo
        #el siguiente es None
        if (self.cabeza == None):
            self.cabeza = nodo
            self.cola = nodo
        else:
            #self.cola = nodo #aqui estoy asignando el valor, no esta enlazando 
            #el nuevo elemento con el ultimo nodo
            self.cola.siguiente = nodo
            #actualizo la cola
            self.cola = nodo
    
    def show(self):
        nodo = self.cabeza
        while (nodo != None):
            print(nodo.valor)
            nodo = nodo.siguiente
            
    #Busqueda de un elemento en una lista enlazada simple
    def busqueda(self, elemento):
        nodo = self.cabeza
        encontrado = False
        contador = 0
        while (nodo != None or encontrado != False):
            if(nodo.valor == elemento):
                encontrado = True
                contador += 1
                return contador
            else:
                nodo = nodo.siguiente
                contador += 1
        return contador
            
def main():
    LisSim = ListaSimple()
    
    random.seed(10)
    NumeroDeIteraciones = []
    
    inicial = time.time_ns()
    for i in range(1000):
        LisSim.add(random.randint(1, 1000))
    print('Tiempo generando la lista ms',str((time.time_ns()-inicial)/1000000))
    
    TiempoEjecuciones = []
    for i in range(500):
        inicial = time.time_ns()
        NumeroDeIteraciones.append(LisSim.busqueda(random.randint(1, 1000)))
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
    print('Tiempo medio de ejecución ns:',(sum(TiempoEjecuciones))/len(TiempoEjecuciones))
    mean = sum(TiempoEjecuciones) / len(TiempoEjecuciones)
    var = sum((l-mean)**2 for l in TiempoEjecuciones) / len(TiempoEjecuciones)
    st_dev = math.sqrt(var)
    print('Desviación estandar ns', str(st_dev))
    print('Max tiempo de ejecución ns', max(TiempoEjecuciones))
    
main()