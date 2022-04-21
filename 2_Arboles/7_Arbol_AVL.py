# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:58:01 2022

@author: jario

"""

class Nodo(object):
	def __init__(self, valor):
		self.valor = valor
		self.l = None
		self.r = None
		self.h = 1

class ArbolAVL(object):

	def insertar(self, raiz, val):
	
		if not raiz:
			return Nodo(val)
		elif val < raiz.valor:
			raiz.l = self.insertar(raiz.l, val)
		else:
			raiz.r = self.insertar(raiz.r, val)

		raiz.h = 1 + max(self.Altura(raiz.l),
						self.Altura(raiz.r))

		b = self.Balanceo(raiz)

        #El nodo está equilibrado y su subárbol derecho es un nivel más alto.
		if b > 1 and val < raiz.l.valor:
			return self.rRotacion(raiz)

        #El nodo está equilibrado y su subárbol izquierdo es un nivel más alto.
		if b < -1 and val > raiz.r.valor:
			return self.lRotacion(raiz)

        #Doble rotación a la derecha
		if b > 1 and val > raiz.l.valor:
			raiz.l = self.lRotacion(raiz.l)
			return self.rRotacion(raiz)

        #Doble rotación a la izquierda
		if b < -1 and val < raiz.r.valor:
			raiz.r = self.rRotacion(raiz.r)
			return self.lRotacion(raiz)

		return raiz

	def lRotacion(self, z):

		y = z.r
		T2 = y.l

		y.l = z
		z.r = T2

		z.h = 1 + max(self.Altura(z.l),
						self.Altura(z.r))
		y.h = 1 + max(self.Altura(y.l),
						self.Altura(y.r))

		return y

	def rRotacion(self, z):

		y = z.l
		T3 = y.r

		y.r = z
		z.l = T3

		z.h = 1 + max(self.Altura(z.l),
						self.Altura(z.r))
		y.h = 1 + max(self.Altura(y.l),
						self.Altura(y.r))

		return y

	def Altura(self, raiz):
		if not raiz:
			return 0

		return raiz.h

	def Balanceo(self, raiz):
		if not raiz:
			return 0

		return self.Altura(raiz.l) - self.Altura(raiz.r)


	def preOrden(self, raiz):

		if not raiz:
			return
		print("{0} ".format(raiz.valor),)
		self.preOrden(raiz.l)
		self.preOrden(raiz.r)

                   
        
Arbol = ArbolAVL()
raiz = None

raiz = Arbol.insertar(raiz, 1)
raiz = Arbol.insertar(raiz, 2)
raiz = Arbol.insertar(raiz, 3)
raiz = Arbol.insertar(raiz, 4)
raiz = Arbol.insertar(raiz, 5)
raiz = Arbol.insertar(raiz, 6)

# Recorrido Preorder 
print("Recorrido Preorder de el ",
	"árbol AVL construido es: ")
Arbol.preOrden(raiz)
print()