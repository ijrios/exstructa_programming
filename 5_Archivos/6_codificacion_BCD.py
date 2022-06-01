# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:22:40 2022

@author: jario
"""

def to_BCD(num):
    bindata = []
    snum = str(num)
    sdata= list(snum)
    sdata = list(map(lambda x: int(x),sdata))
    if(len(sdata)%2 == 1):
        sdata= [0]+sdata 
    
    print("Lista original decimal: ",sdata)
    stemp = sdata.copy()
    for i in range(len(stemp)//2):
        x = 0
        x = sdata[i*2]
        x = x<<4
        x = x | sdata[i*2+1]
        bindata.append(x)
        
    sbcd = "".join([chr(c) for c in bindata])
    print("Lista convertida y codificada hexadecimal: ",bindata)
    return sbcd

def to_NUM(sbin):
    data = []
    sdata = list(sbin)
    print("Lista en string binario: ",sdata)
    #ord obtenr el codigo ascii del caracter
    sdata = [ord(c) for c in sdata]
    print("Lista decodificada hexadecimal: ",sdata)
    
    for i in sdata:
        x = i>>4
        y = i&0xF
        data.append(x)
        data.append(y)
    print("Lista original decimal: ",data)
    sint = "".join([str(c) for c in data])
    return int(sint)
    
sbin = to_BCD(12345)
print("Numero en string binario: ",sbin)
num = to_NUM(sbin)
print("Numero en formato string: ",num)
