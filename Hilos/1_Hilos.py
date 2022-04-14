# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:14:50 2022

@author: jario
"""

import threading
import time

class myHilo1 (threading.Thread):
    def __init__(self, threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
        imprimir_nums(self.name)


def imprimir_nums(name):
    for i in range(1,11):
        #time.sleep(1)
        print(name,"--->",i)
        
def main():
    print("inicio")
    h1 = myHilo1("abc","h1")
    h1.start()
    print("fin")

main()
