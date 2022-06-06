# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:15:11 2022

@author: jario
"""
import os

class Nodo:
    
    def __init__(self,valor,sig=None):
        self.valor = valor
        self.sig =sig
        
class Cola:
    
    def __init__(self): 
        self.cabeza = None
        self.cola = None
        
    def encolar(self,valor):
        
        if(self.cabeza == None):
            nodo = Nodo(valor)
            self.cabeza = nodo
            self.cola = nodo
        else:
            n = Nodo(valor)
            self.cola.sig = n
            self.cola = n
        
    def desencolar(self):
        
        if(self.cabeza != None):
            nodo = self.cabeza
            self.cabeza = self.cabeza.sig
            nodo.sig = None
            return nodo.valor
        else:
            return None
        
    def show(self):
        
        n = self.cabeza
        while(n != None):
            print(n.valor)
            n = n.sig
            
def menu():
    
    
	os.system('cls') #Limpiar menu
	print ("Selecciona una opción por favor")
	print ("1 - Ingresar datos")
	print ("2 - Mostrar datos")
	print ("3 - Generar archivo")
	print ("9 - Salir")
 
 
def to_BCD(num):
    bindata = []
    snum = str(num)
    sdata= list(snum)
    sdata = list(map(lambda x: int(x),sdata))
    if(len(sdata)%2 == 1):
        sdata= [0]+sdata 
    
    #print("Lista original decimal: ",sdata)
    stemp = sdata.copy()
    for i in range(len(stemp)//2):
        x = 0
        x = sdata[i*2]
        x = x<<4
        x = x | sdata[i*2+1]
        bindata.append(x)
        
    sbcd = "".join([chr(c) for c in bindata])
    #print("Lista convertida y codificada hexadecimal: ",bindata)
    return sbcd

def main():
    
    
    while True:
	# Mostramos el menu
    	menu()
        
        # Solicituamos una opción al usuario
    	opcionMenu = input("Inserta un numero valor >> ")
     
    	if opcionMenu=="1":
    		
            print("Has pulsado la opción 1... \n Ingresar datos \n ")
            fecha = int(input("Ingrese la Fecha formato ddmmyyyy: \n"))
            ubicación = input("Ingrese el nombre de la ubicación: \n")
            signolat = int(input("Ingrese el signo Latitud (0 positivo, 1 negativo): \n"))
            latitud = float(input("Ingrese la Latitud: \n"))
            signolon = int(input("Ingrese el signo longitud (0 positivo, 1 negativo): \n"))
            longitud = float(input("Ingrese la Longitud: \n"))
            
            lista = Cola()
            lista.encolar(fecha)
            lista.encolar(ubicación)
            lista.encolar(signolat)
            lista.encolar(latitud)
            lista.encolar(signolon)
            lista.encolar(longitud)
            
            
            print("\n Datos Ingresados correctamente\n")
            

    	elif opcionMenu=="2":
            
            print("Has pulsado la opción 2... \n Mostrar datos \n")
            lista.show()
            print(" ")

    	elif opcionMenu=="3":
    		
            print("Has pulsado la opción 3... \ Generar archivo")
            # Generando archivo
            archivo = open('prueba_fixed.txt','w')
            
            # Codificación BCD
            sbin = to_BCD(fecha)
            sbin1 = to_BCD(signolat)
            sbin2 = to_BCD(int(latitud))
            sbin3 = to_BCD(signolon)
            sbin4 = to_BCD(int(longitud))
            
            fecha_f = (sbin)
            ubicacion_f = (ubicación+(" "*25))[-25:]
            signolat_f = (("0"*1)+sbin1)[:1] 
            latitud_f = (("0"*8)+sbin2)[:8]
            signolon_f = (("0"*1)+sbin3)[:1] 
            longitud_f = (("0"*8)+sbin4)[:8]
            
            registro = fecha_f+ubicacion_f+signolat_f+latitud_f+signolon_f+longitud_f
            archivo.write(registro)
            archivo.close()
            print("Archivo generado\n ")

    
    	elif opcionMenu=="9":
    		break
    	else:
    		print ("")
    		print("No has pulsado ninguna opción correcta...")            
    
main()