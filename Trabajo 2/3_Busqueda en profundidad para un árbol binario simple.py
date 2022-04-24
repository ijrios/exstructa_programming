import matplotlib.pyplot as plot
import random, time, math

#crear arbol binario simple
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
			aux = self.raiz
			while aux != None:
				if dato < aux.dato:
					if aux.izq == None:
						aux.izq = Nodo(dato)
						break
					else:
						aux = aux.izq
				else:
					if aux.der == None:
						aux.der = Nodo(dato)
						break
					else:
						aux = aux.der
	def inorden(self, aux):
		if aux != None:
			self.inorden(aux.izq)
			print(aux.dato)
			self.inorden(aux.der)
	def preorden(self, aux):
		if aux != None:
			print(aux.dato)
			self.preorden(aux.izq)
			self.preorden(aux.der)
	def postorden(self, aux):
		if aux != None:
			self.postorden(aux.izq)
			self.postorden(aux.der)
			print(aux.dato)
	def buscar(self, aux, dato):
		if aux != None:
			if dato == aux.dato:
				return True
			elif dato < aux.dato:
				return self.buscar(aux.izq, dato)
			else:
				return self.buscar(aux.der, dato)
		else:
			return False
	def busqueda_en_profundidad(self, aux, dato,contador):
		if aux != None:
			contador += 1
			if dato == aux.dato:
				contador += 1
				return contador
			elif dato < aux.dato:
				contador += 1
				return self.busqueda_en_profundidad(aux.izq, dato, contador)
			else:
				contador += 1
				return self.busqueda_en_profundidad(aux.der, dato, contador)
		else:
			contador += 1
			return contador
		
	def getRaiz(self):
		return self.raiz

arb = Arbol()

random.seed(28)
inicial = time.time_ns()
for i in range(1000):
    arb.insertar(random.randint(1, 1000))
print('Tiempo generando la lista ms',str((time.time_ns()-inicial)/1000000))

NumeroDeIteraciones = []
TiempoEjecuciones = []
for i in range(500):
    contador = 0
    inicial = time.time_ns()
    NumeroDeIteraciones.append(arb.busqueda_en_profundidad(arb.getRaiz(),random.randint(1, 1000), contador))
    final = time.time_ns()
    TiempoEjecuciones.append(final-inicial)
    
#este es porque la escala, abarcan numeros muy dispersos, muy grandes
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
