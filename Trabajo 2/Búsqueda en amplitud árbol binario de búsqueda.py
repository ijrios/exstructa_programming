import matplotlib.pyplot as plot
import random,time,math
#crear clase para arbol binario de busqueda
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self):
        self.raiz = None
    def insertar(self, dato):
        if self.raiz == None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)
    def _insertar(self, dato, nodo_raiz):
        if dato < nodo_raiz.dato:
            if nodo_raiz.izq is None:
                nodo_raiz.izq = Nodo(dato)
            else:
                self._insertar(dato, nodo_raiz.izq)
        else:
            if nodo_raiz.der is None:
                nodo_raiz.der = Nodo(dato)
            else:
                self._insertar(dato, nodo_raiz.der)
    def preorden(self):
        self._preorden(self.raiz)
    def _preorden(self, nodo_raiz):
        if nodo_raiz is not None:
            print(nodo_raiz.dato)
            self._preorden(nodo_raiz.izq)
            self._preorden(nodo_raiz.der)
    def inorden(self):
        self._inorden(self.raiz)
    def _inorden(self, nodo_raiz):
        if nodo_raiz is not None:
            self._inorden(nodo_raiz.izq)
            print(nodo_raiz.dato)
            self._inorden(nodo_raiz.der)
    def postorden(self):
        self._postorden(self.raiz)
    def _postorden(self, nodo_raiz):
        if nodo_raiz is not None:
            self._postorden(nodo_raiz.izq)
            self._postorden(nodo_raiz.der)
            print(nodo_raiz.dato)

    #funcion para busqueda en amplitud arbol binario de busqueda
    def bfs(self, valor):
            contador = 0
            if self.raiz is None:
                contador += 1
                return contador 
            queue = [self.raiz]
            
            encontrado = False
            while len(queue) > 0 and not encontrado:
                cur_node = queue.pop(0)
                
                if cur_node.dato == valor:
                    encontrado = True
                    contador += 1
                    return contador
                
                else:
                    if cur_node.izq is not None:
                        contador += 1
                        queue.append(cur_node.izq)
        
                    if cur_node.der is not None:
                        contador += 1
                        queue.append(cur_node.der)
                        
            return contador

arbol = Arbol()
random.seed(28)
inicial = time.time_ns()
for i in range(1000):
    Num = random.randint(1, 1000)
    arbol.insertar(Num)
print('Tiempo generando la lista ms',str((time.time_ns()-inicial)/1000000))

NumerosBuscar = []
NumeroDeIteraciones = []
TiempoEjecuciones = []
for i in range(500):
    inicial = time.time_ns()
    contador = 0
    Num = random.randint(1, 1000)
    NumerosBuscar.append(Num)
    NumeroDeIteraciones.append(arbol.bfs(Num))
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