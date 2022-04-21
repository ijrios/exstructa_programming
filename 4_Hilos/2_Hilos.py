# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:08:41 2022

@author: jario
"""

# Implementar un programa que dispare un hilo, que sume los números del 1 al 10
# capturas el resultado del programa princial y mostrarlo por pantalla
# simular un retardo de medio segundo en el proceso general

# Agregar un segundo hilo que sume los numeros del 1 al 20
# al final el programa debe imprimir la suma total de los dos hilos


import threading
import time

class Proceso_suma(threading.Thread):
    def __init__(self,name,n):
        threading.Thread.__init__(self)
        self.name = name
        self.n = n
        self.suma = 0
        
    #Lo que el hilo va a ejecutar
    def run(self):
        for i in range(self.n+1):
            self.suma += i
            time.sleep(0.5)
        print("termina ------->", self.name)

    def get_suma(self):
        return self.suma

def main():
    
    t1 = time.time()
    h1 = Proceso_suma("Hilo 1",10)
    h2 = Proceso_suma("Hilo 2",20)
    h1.start()
    h2.start()
    # Obliga al principal a que h1 acabe
    h1.join() 
    h2.join() 
    valor = h1.get_suma()
    valor2 = h2.get_suma()
    
    print("Resultados del calculo: ",(valor+valor2))
    t2 = time.time()
    print("Tiempo de ejecucion: ",(t2-t1))

main()
