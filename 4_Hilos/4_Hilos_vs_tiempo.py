# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:17:11 2022

@author: b12s307e22
"""
import matplotlib.pyplot as plt
import threading
import time

class Proceso (threading.Thread):
    def __init__(self, ptime, name):
        threading.Thread.__init__(self)
        self.ptime = ptime
        self.name = name
    
    def run(self):
        #print("inicio...")
        time.sleep(self.ptime)
        print(self.name,"...fin")
    
def portapapeles():
    l_tiempo = [30,20,40,50]
    l_tiempo2 = l_tiempo.copy()
    l_tiempo2.insert(0,l_tiempo[0])
    mejora = []
    for i in range(0,len(l_tiempo)):
        m = (l_tiempo2[i-1]/l_tiempo2[i])
        mejora.append(m)
     
def main():
    GItime = time.time()
    t_max = 60
    n_procs = [1,2,3,4,5,6,8,10,12,15,18,21]
    l_tiempos = [] 
    
    for n_proc in n_procs:
        itime = time.time()
        time.sleep(1)
        h_procs = []
        for i in range(n_proc):
            h_procs.append(Proceso(t_max/n_proc,"sp"+str(i)))
        
        for i in range(n_proc):
            h_procs[i].start()
    
        for i in range(n_proc):
            h_procs[i].join()
        
        ftime = time.time()
        ttp = (ftime-itime)
        l_tiempos.append(ttp)
        print(n_proc,"hilos-","tiempo del proceso (actual)...",ttp)
    
    print(l_tiempos)
    GFtime = time.time()
    print("TIEMPO GENERAL...",(GFtime-GItime))
    
   
    l_tiempos2 = l_tiempos.copy()
    l_tiempos2.insert(0,l_tiempos[0])
    l_inc_vel = [  l_tiempos2[x-1]/l_tiempos2[x] for x in range(1,len(l_tiempos2))]
    
    print(l_inc_vel)
    print(len(l_tiempos)) 
    print(len(l_inc_vel))
    
    plt.bar(n_procs,l_inc_vel)
    plt.show()    
    
main()
    