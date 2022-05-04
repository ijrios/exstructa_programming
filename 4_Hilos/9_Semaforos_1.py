# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:20:53 2022

@author: b12s307e22
"""

from threading import *         
import time        
  
# creating thread instance where count = 3
obj = Semaphore(2)        
  
# creating instance
def display(name):    
    
    # calling acquire method
    obj.acquire()                
    for i in range(5):
        print('Hello, '+name+'')
        time.sleep(0.5)
    # calling release method
    obj.release()    
          
# creating multiple thread 
t1 = Thread(target = display , args = ('T-1',))
t2 = Thread(target = display , args = ('T-2',))
t3 = Thread(target = display , args = ('T-3',))
t4 = Thread(target = display , args = ('T-4',))
t5 = Thread(target = display , args = ('T-5',))
  
# calling the threads 
t1.start()
t4.start()
t5.start()
t2.start()
t3.start()
