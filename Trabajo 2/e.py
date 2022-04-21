#implementar una busqueda binaria para una lista enlazada simple
# https://www.geeksforgeeks.org/binary-search-on-singly-linked-list/

class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.sig = None
    
class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def add(self,valor):
        n = Nodo(valor)
        if (self.cabeza == None):
            self.cabeza = n
            self.cola = n
        else:
            self.cola.sig = n
            self.cola = n
    
    def show(self):
        n = self.cabeza
        while(n != None):
            print(n.valor)
            n = n.sig
            
    def Ordenamiento(self):
        def Lista_Ord(self,cabeza):
            interc = 0
            if(self.cabeza != None): #si la lista no esta vacia
                while (1):
                    interc = 0
                    temporal = self.cabeza
                    while (temporal.sig != None):
                        if (temporal.valor > temporal.sig.valor):
                            interc += 1
                            p = temporal.valor
                            temporal.valor = temporal.valor.sig
                            temporal.valor.sig = p
                            temporal = temporal.sig
                        else:
                            temporal = temporal.sig
                    if (interc == 0):
                        break
                    else:
                        continue
                return self.cabeza
            else:
                return self.cabeza

def main():
    lis = ListaSimple()
    lis.add(45)
    lis.add(48)
    lis.add(35)
    lis.add(12)
    lis.add(58)
    lis.add(98)
    print("===================================")
    print("Lista Simple:")
    lis.show()
    print("===================================")
    print("Lista Simple ordenada:")
    lis_ord = lis.Ordenamiento()
    print(lis_ord)
    
main()