# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:37:50 2022

@author: jario
"""

# Implementar un programa que genere una lista de objetos tipo persona, 
# de las personas se tiene la siguiente información, nombre, cedula, edad, 
# trabajarlo en OOP, aplicar compresiones sobre las estructuras que me 
# permitan extraer las personas menores de edad, promedio de edad, manejar excepciones.

import numpy
  
class Persona:
      
    # Constructor
    def __init__(self, nombre, cedula, edad):
          
        self.name = nombre
        self.id = cedula
        self.age = edad
        
    def __str__(self):
        cadena = self.name+","+str(self.id)+","+str(self.age)
        return cadena
    
 
#Listade objetos         
list = []
#list.append(Persona("Jose", 1402, 28))
#list.append(Persona("Dbr", 2027, 34))
#list.append(Persona("Angelica", 1002, 19)) 
#list.append(Persona("Miguelito", 1125, 13))  


n=int(input("Cuantas personas desea ingresar: "))

for x in range(n):
    
    nombre=str(input("Ingrese el nombre de la persona: "))
    
    while True:
        
     try:
         cedula=int(input("Ingrese la cedula de la persona: "))
         break
     except ValueError:
         print("Oops!  formato invalido debe ser entero. prueba de nuevo...")
   
    while True:
        
     try:
         edad=int(input("Ingrese la edad de la persona: "))
         break
     except ValueError:
        print("Oops!  formato invalido debe ser entero. prueba de nuevo...")
   
    person = Persona(nombre,cedula,edad)
    list.append(person)
   
    
#lista completa
print("-----    Lista completa   ---------")
for obj in list:
    print( obj.name, obj.id, obj.age, sep =' ' )
print("-----------------------------------")
  
#Menores de edad - compresion
list_menor = [p for p in list if p.age < 18]

print("------  Menores de edad   ---------")
for person in list_menor:
   print(person.name, person.id, person.age, sep =' ' )
print("-----------------------------------")

#Mayores de edad - compresion
list_mayor = [x for x in list if x.age > 18]

print("------  Menores de edad   ---------")
for person in list_mayor:
   print(person.name, person.id, person.age, sep =' ' )
print("-----------------------------------")
   
#Promedio
listmean = []
for obj in list:
    listmean.append(obj.age)
    
print("El promedio de las edades es: ")
mean = numpy.mean(listmean)
print(mean)

    