# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:06:32 2022

@author: b12s307e22
"""
#DEFINICION 
#================================================
# tamño de los campos
# nom --> 150 bytes -- fill:esp -- algn_valor = izq
# eda --> 3 bytes -- fill:ceros -- algn_valor = der
# tel --> 50 bytes -- fill:esp  -- algn_valor = izq
#================================================


archivo = open('prueba_fixed.txt','w')

nom = "juan"
eda = 23
tel = "43743734734"

nom_f = (nom+(" "*50))[:50] 
eda_f = (("0"*3)+str(eda))[-3:]
tel_f = (tel+(" "*20))[:20] 

registro = nom_f+eda_f+tel_f
archivo.write(registro)

archivo.close()