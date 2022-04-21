import matplotlib.pyplot as plot
import random

class Nodo:
    def __init__(self, valor):
        self.val =  valor
        self.izq = None
        self.der = None
        
class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def add_bin(self, valor):
        n = Nodo(valor)
        if (self.raiz == None):
            self.raiz = n
        else:
            nc = self.raiz
            ant = None
            while(nc != None):
                ant = nc
                if(n.val < nc.val):
                    nc = nc.izq  
                elif (n.val > nc.val):
                    nc = nc.der
                else:
                    break
            
            #nc --> mayor o menor
            if(n.val < ant.val):
                ant.izq = n
            elif(n.val > ant.val):
                ant.der = n
                
    def preOrden(self):
        self.preOrden_recur(self.raiz)

    def preOrden_recur(self,nodo):
       print(nodo.val)
       if(nodo.izq != None):
           self.preOrden_recur(nodo.izq)
       if(nodo.der != None):
           self.preOrden_recur(nodo.der)
           
    def inOrden(self):
        self.inOrden_recur(self.raiz)

    def inOrden_recur(self,nodo):       
       if(nodo.izq != None):
           self.inOrden_recur(nodo.izq)
       print(nodo.val)
       if(nodo.der != None):
           self.inOrden_recur(nodo.der)

    def posOrden(self):
        self.posOrden_recur(self.raiz)

    def posOrden_recur(self,nodo):       
        if(nodo.izq != None):
           self.posOrden_recur(nodo.izq)
        if(nodo.der != None):
           self.posOrden_recur(nodo.der)           
        print(nodo.val)
        
    def altura(self,nodo):
        if (nodo is None):
            return 0
        else:
            # Compute the height of each subtree
            altura_izq = self.altura(nodo.izq)
            altura_der = self.altura(nodo.der)
 
        # Use the larger one
        if altura_izq > altura_der:
            return altura_izq + 1
        else:
            return altura_der + 1
    
    def nivel_actual(self,root,level):
        if root is None:
            return
        if level == 1:
            print(root.val)
        elif level > 1:
            self.nivel_actual(root.izq, level-1)
            self.nivel_actual(root.der, level-1)
        
    def niveles(self):
        h = self.altura(self.raiz)
        print("Nivel del arbol: ",h)
        for i in range(1, h+1):
            self.nivel_actual(self.raiz, i)
    

def busqueda_en_profundidad(arbol, valor):
    if arbol is None:
        return False
    if arbol.nodo.val == valor:
        return True
    return busqueda_en_profundidad(arbol.izq, valor) or busqueda_en_profundidad(arbol.der, valor)

arb = ArbolBinario()

random.seed(28)

for i in range(1000):
    arb.add_bin(random.randint(1, 1000))

NumeroDeIteraciones = []

for i in range(10):
    
    NumeroDeIteraciones.append(busqueda_en_profundidad(arb,random.randint(1, 1000)))

print(NumeroDeIteraciones)
plot.hist(NumeroDeIteraciones)
plot.show()
