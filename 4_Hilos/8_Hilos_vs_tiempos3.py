# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:42:42 2022

@author: s205e19
"""

# Corregir errores en los tiempos e implementar archivos planos para imprimir
# todos los primos encontrados en cada proceso.

import threading
import time
import random
import os

class ProcessPrimes(threading.Thread):
    
    def __init__(self, name, listN):
        threading.Thread.__init__(self)
        self.name = name
        self.listN = listN
        self.count_primes = 0
        self.primes = []

    def run(self):
        archivo = open("data.txt", 'w')
        itime = time.time()
        for num in self.listN:
            c_div = 0
            for x in range(2,num):
                if(num%x == 0):
                    c_div += 1
                    break
            if(c_div == 0):
                #is prime number 
                self.count_primes += 1
                self.primes.append(num)
                archivo.write(str("\n Cantidad de primos - "))
                archivo.write(str(self.count_primes))
                archivo.write(str("\n Primos encontrados - "))
                archivo.write(str(self.primes))
                

        ftime = time.time()
        ttp = (ftime-itime)        
        print(self.name,"---->",self.count_primes, "primes in",ttp,"seconds") 
        print(self.primes)
        archivo.close()


    def assign_nums(self,lisN):
        self.listN = lisN

    def get_cant_primes(self):
        return self.count_primes

    def get_primes(self):
        return self.primes
    
    def archivo(self):
        print ("\n Creating file")
        print ("================")

        FILE_NAME = 'data.txt'

        archivo = open(FILE_NAME, 'w')
        archivo.write(str(self.count_primes))
        archivo.write(str(self.primes))
        archivo.close()

        if FILE_NAME in os.listdir("."):
            print ("\nFile created")
        else:
            print ("The file was not created!!!\n")

def main():
    GItime = time.time()
    range_end = 10000
    lis_num_procs = [1,2,3,4,5,6,7,8,9,12] 
    l_times = [] 
    batch_nums  = list(range(2,range_end))
    random.shuffle(batch_nums,random.random)

    for n_procs in lis_num_procs:
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-")
        itime = time.time()
        range_init = 2
        load = (len(batch_nums))//n_procs
        process = []
        for i in range(n_procs):
            print(range_init,"<--->",range_init+load)
            prc = ProcessPrimes("H"+str(i),batch_nums[range_init:range_init+load])
            process.append(prc)
            range_init = range_init+load


        for prc in process:
            prc.start()
            time.sleep(0.1)

        for prc in process:
            prc.join()
        
        ftime = time.time()
        ttp = (ftime-itime)
        l_times.append(ttp)
        #print(n_procs,"threads-","process time (current)...",ttp)        

    GFtime = time.time()
    print("OVERALL WEATHER...",(GFtime-GItime))
    print(l_times)


main()     