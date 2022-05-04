# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:34:30 2022

@author: s205e19
"""

import threading
import time
import numpy as np 

class ProcesoPrimos(threading.Thread):
    def __init__(self, nom,numIni, numFin):
        threading.Thread.__init__(self)
        self.nom = nom
        self.numIni = numIni
        self.numFin = numFin
        self.con_primos = 0
        
    def run(self):
        itime = time.time()
        for num in range(self.numIni,self.numFin+1):
            c_div = 0
            for x in range(2,num):
                if(num%x == 0):
                    c_div += 1
                    break
            if(c_div == 0):
                #es primo
                self.con_primos += 1
        ftime = time.time()
        ttp = (ftime-itime)        
        print(self.nom,"---->",self.con_primos, "primos en",ttp,"segundos") 
        
    def get_cant_primos(self):
        return self.con_primos

def main():
    GItime = time.time()
    r_fin = 30000
    lis_num_prcs = [1,2,3,4,5,6] #,8,10,12,15,18,21]
    l_tiempos = [] 
    
    for n_procs in lis_num_prcs:
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-")
        itime = time.time()
        time.sleep(1)   
        r_ini = 2
        carga = (r_fin-r_ini)//n_procs
        procesos = []
        for i in range(n_procs):
            print(r_ini,"<--->",r_ini+carga)
            prc = ProcesoPrimos("H"+str(i),r_ini,r_ini+carga)
            procesos.append(prc)
            r_ini = r_ini+carga
        
        for prc in procesos:
            prc.start()
                
        for prc in procesos:
            prc.join()
        
     
        
        ftime = time.time()
        ttp = (ftime-itime)
        l_tiempos.append(ttp)
        #print(n_procs,"hilos-","tiempo del proceso (actual)...",ttp)        
        
    GFtime = time.time()
    print("TIEMPO GENERAL...",(GFtime-GItime))
    print(l_tiempos)
    
    
main()    