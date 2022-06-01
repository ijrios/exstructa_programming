# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:16:45 2022

@author: jario
"""

import threading 
from threading import *
import time
sema = threading.Semaphore()

class ProcessPrimes(threading.Thread):
    
    def __init__(self, name,file):
        threading.Thread.__init__(self)
        self.name = name
        self.file = file
        self.primes = []
        self.count_primes = 0
        self.lock = threading.Lock()
        
    
    def run(self):
        sema.acquire()
        print("Inicio del hilo")
        with open(self.file, "r") as file:
            for line in file:
                currentline = line.split(",")
                currentline.pop()
                int_list = list(map(int, currentline))
               #print(int_list)
          
            for num in int_list:
                c_div = 0
                for x in range(2,num):
                    if(num%x == 0):
                        c_div += 1
                        break
                if(c_div == 0):
                    #es primo
                    self.count_primes += 1
                    self.primes.append(num)
                    
            print(self.name,"---->",self.count_primes, "primos") 
            print(self.primes)
            #Write final file
            writeFile("finalFile.txt", self.primes,self.name)   
            sema.release()
            
    def getprime(self):
        return self.primes
    

def writeFile(file,string,name):
    archivo = open(file,'a')
    archivo.write("Primos encontrados "+name)
    archivo.write("\n")
    archivo.write(str(string))
    archivo.write("\n")
    archivo.close()
    
                
def main():
    
    process = []
    for j in range(10):
            prc = ProcessPrimes("Thread"+str(j),"testFile_"+str(j)+".txt")
            process.append(prc)
            
    for prc in process:
            prc.start()
                
    for prc in process:
            prc.join()
         
main()    