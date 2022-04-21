# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:24:24 2022

@author: jario
"""

import threading
import time

class Proceso(threading.Thread):
    def __init__(self, threadID,ptime):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.ptime = ptime
        
    def run(self):
        #print("Inicio ")
        time.sleep(self.ptime)
        print(self.threadID, "... fin")

        
def main():
    
    itime = time.time()
    # tiempo = x0
    # tiempo = xo / numero de hilos
    tmax = 60
    time.sleep(1)
    #Hilos
    h_procs = []
    #Numero de hilos
    n_procs = int(input("Ingrese el numero de hilos: "))
 
    for i in range(n_procs):
        h_procs.append(Proceso("sp"+str(i),tmax/n_procs))
        
    for i in range(n_procs):
        h_procs[i].start()
        
    for i in range(n_procs):
        h_procs[i].join()

    ftime = time.time()
    print("Tiempo general del proceso... ",(ftime-itime))
    #A mayor hilos, menor tiempo, pero el procesador se ve afectado

main()


