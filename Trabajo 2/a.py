import matplotlib.pyplot as plot
import random 

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
    
    for i in range(1000):
        LisSim.add(random.randint(1, 1000))

    for i in range(10):
        NumeroDeIteraciones.append(LisSim.busqueda(random.randint(1, 1000)))

    print(NumeroDeIteraciones)
    plot.hist(NumeroDeIteraciones)
    plot.show()


main()