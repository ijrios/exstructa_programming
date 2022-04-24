import matplotlib.pyplot as plot
import random, time, math

class Nodo:
    def __init__(self,valor,sig=None):
        #Condicion inicial del nodo vacío
        self.valor = valor
        self.sig = sig
        
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
        str_rep = ""
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
            while(actual != None and actual.sig != None): #mientras que el actual y el que le siga no sean vacios
                #Cuando el valor del nodo actual es menor que el del nodo anterior
                if(actual.valor > actual.sig.valor): #comparamos valores
                    #Intercambiar valores de nodo
                    actual.valor = actual.valor + actual.sig.valor
                    actual.sig.valor = actual.valor - actual.sig.valor
                    actual.valor = actual.valor - actual.sig.valor
                    estado = 1
        
                actual=actual.sig #avanzamos

        else:
           print("Lista vacía")
    
    #Devuelve el nodo medio en el rango dado
    def valorMedio(self, primero, ultimo) :
        #Algunas variables auxiliares
        medio = primero
        temp = primero.sig
		#Encuentra el nodo medio
        while (temp != None and temp != ultimo):
            temp = temp.sig 
            if (temp != ultimo):
				#Visita al siguiente nodo
                medio = medio.sig
                temp = temp.sig
        return medio
	
	#Esto está realizando la operación de búsqueda binaria.
    def busquedaBinaria(self, valorb) :
        if (self.cabeza == None) :
            print("\n Lista vacía", end = "")
            return 1
		
		#Algunas variables auxiliares
        primero = self.cabeza
        ultimo = self.cola
        resultado = None
        medio = self.cabeza
        contador = 0
        if (primero.valor == valorb) :
			#si el numero esta de primeras
            resultado = primero
            contador += 1
		
        if (ultimo.valor == valorb) :
	    #si el numero esta de ultimas
            resultado = ultimo
            contador += 1
	
        #Este bucle detecta un elemento dado mediante la búsqueda binaria.
        #cuando no haya encontrado en la 1ra o ultima posicion
        #y que el primero sea diferente del ultimo
        while (resultado == None and primero != ultimo) :
			#Primero encuentra el elemento medio
            medio = self.valorMedio(primero, ultimo)
            if (medio == None) :
		#Esto es útil cuando no sabemos sobre el último nodo inicial 
		#y el elemento de búsqueda es más grande que el último nodo
                resultado = None
                contador += 1
            elif (medio.valor == valorb) :
		#Cuando obtenga el nodo de búsqueda
                contador += 1
                resultado = medio
            elif (medio.valor > valorb) :
		#Seleccionar nuevo último nodo
                ultimo = medio
                contador += 1
            else :
		#Seleccionar nuevo nodo inicial
                primero = medio.sig
			
        return contador

def main():
    Lis = Lista()
    random.seed(28)
    
    inicial = time.time_ns()
    for i in range(1000):
        Lis.ad_valor(random.randint(1, 1000))

    Lis.metodoBurbuja()
    print('Tiempo generando la lista ms',str((time.time_ns()-inicial)/1000000))
    
    NumeroDeIteraciones = []
    TiempoEjecuciones = []
    for i in range(500):
        inicial = time.time_ns()
        NumeroDeIteraciones.append(Lis.busquedaBinaria(random.randint(1, 1000)))
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
    
main()