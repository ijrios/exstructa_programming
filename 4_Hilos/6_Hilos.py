# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:41:04 2022

@author: jario
"""

# Implementar un programa que indique los numeros primos en el siguiente
# rango [2,x] repartir las cargas de trabajo en diferentes ejecuciones, haciendo
# uso de diferentes cantidades de hilos, analizar resultados

import threading
import time

class Proceso(threading.Thread):
    def __init__(self, name, numIni,numFin):
        threading.Thread.__init__(self)
        self.name =name
        self.numIni = numIni
        self.numFin = numFin
        self.con_primos = 0
        
    def run(self):
        for num in range(self.numIni,self.numFin+1):
            c_div = 0
            for x in range(2,num):
                if(num%x == 0):
                    c_div +=1
                if (c_div == 0):
                    #Es primo
                    self.con_primos +=1
            
            print(self.name,"----->",self.con_primos, "Primos")
                    
    def get_cant_primos(self):
        return self.con_primos
    
def main():
    
    Gtime = time.time()
    rango_f = 100
    lis_num_prcs = [1,2,3,4,5,6,7,8,9,10,12,15,18,21,22,23,24,26,27,45,76,89,100,200,400,10,23,45]
    l_tiempos = []
    
    for n_procs in lis_num_prcs:
        itime = time.time()
        time.sleep(1)
        rango_i = 2
        carga = (rango_f-rango_i)//n_procs
        procesos =[]
        
        for i in range(n_procs):
            print(rango_i, "<--->", rango_i+carga)
            prc = Proceso("H"+str(i),rango_i,rango_i+carga)
            procesos.append(prc)
            rango_i = rango_i+carga
            
        for prc in procesos:
            prc.start()
            
        for prc in procesos:
            prc.join()
            
        ftime = time.time()
        ttp = (ftime-itime)
        l_tiempos.append(ttp)
        print(n_procs, "hilos", "tiempo del proceso(actual)...",ttp)
        
    GFtime = time.time()    
    print("Tiempo general del proceso... ",(GFtime-Gtime))

main()


