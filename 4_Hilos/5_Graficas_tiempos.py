# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:13:55 2022

@author: b12s307e22
"""
import matplotlib.pyplot as plt

l_tiempos =  [61.05793118476868, 31.036792278289795, 21.051433563232422, 16.060885906219482, 13.059105634689331, 11.055532932281494, 8.567114353179932, 7.081006288528442, 6.060971021652222, 5.066401720046997, 4.406562328338623, 3.925243616104126]
n_procs = [1,2,3,4,5,6,8,10,12,15,18,21]

l_tiempos2 = l_tiempos.copy()
l_tiempos2.insert(0, 61.00919985771179)
l_inc_vel = [  l_tiempos2[0]/l_tiempos2[x] for x in range(1,len(l_tiempos2))]

print(l_inc_vel)
print(len(l_tiempos)) 
print(len(l_inc_vel))

plt.bar(n_procs,l_inc_vel)
plt.show()