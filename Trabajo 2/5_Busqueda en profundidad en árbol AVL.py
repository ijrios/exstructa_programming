import matplotlib.pyplot as plot
import random
import time
import math
# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

	# Recursive function to insert key in
	# subtree rooted with node and returns
	# new root of subtree.
	def insert(self, root, key):
	
		# Step 1 - Perform normal BST
		if not root:
			return TreeNode(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		# Step 2 - Update the height of the
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and key < root.left.val:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and key > root.right.val:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and key > root.left.val:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def leftRotate(self, z):

		y = z.right
		T2 = y.left

		# Perform rotation
		y.left = z
		z.right = T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def rightRotate(self, z):

		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)


	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.val), end="")
		self.preOrder(root.left)
		self.preOrder(root.right)

def buscar(root, dato, contador):
	if root == None:
		contador += 1
		return contador
	
	else:
		
		if root.val == dato:
			contador += 1
			return contador
		else: 
			if dato < root.val:
				contador += 1
				return buscar(root.left, dato, contador)
			else:
				contador += 1
				return buscar(root.right, dato, contador)


def main():
    # Driver program to test above function
    inicial = time.time_ns()
    myTree = AVL_Tree()
    random.seed(28)
    root = None
    
    for i in range(1000):
        root = myTree.insert(root, random.randint(1, 1000))
    print('Tiempo generando la lista ms',str((time.time_ns()-inicial)/1000000))
    
    NumerosBuscar = []
    NumeroDeIteraciones = []
    TiempoEjecuciones = []
    for i in range(500):
        inicial = time.time_ns()
        contador = 0
        Num = random.randint(1, 1000)
        NumerosBuscar.append(Num)
        NumeroDeIteraciones.append(buscar(root,Num,contador))
        final = time.time_ns()
        TiempoEjecuciones.append(final-inicial)
  
    plot.hist(NumeroDeIteraciones)
    plot.title("Numero de Iteraciones")
    plot.ylabel("Frecuencia")
    plot.xlabel("Numero de comparaciones")
    plot.grid()
    plot.show()
    plot.bar(list(range(1,len(TiempoEjecuciones)+1)),TiempoEjecuciones)
    plot.title("Tiempo de ejecucion busqueda de cada elemento")
    plot.ylabel('Tiempo de ejecucion ns')
    plot.xlabel('# de ejecución')
    plot.grid()
    plot.show()
    print('Tiempo medio de ejecución ns: ',(sum(TiempoEjecuciones))/len(TiempoEjecuciones))
    mean = sum(TiempoEjecuciones) / len(TiempoEjecuciones)
    var = sum((l-mean)**2 for l in TiempoEjecuciones) / len(TiempoEjecuciones)
    st_dev = math.sqrt(var)
    print('Desviación estandar ns: ', str(st_dev))
    print('Max tiempo de ejecución ns: ', max(TiempoEjecuciones))

main()