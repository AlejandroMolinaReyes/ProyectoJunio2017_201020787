from .nodo import Nodo

class Arbol:

	def __init__(self):
		self.__raiz = None

########################################## insertar ###############################

	def __insertar(self, raiz, nombre,contraseña):
		if raiz==None:# raiz esta vacia 
			return Nodo(nombre,contraseña)
		else:
			if raiz.nombre < nombre:# dirrecion al lado izquierdo para la insertar 
				if raiz.derecho == None: # vericando si el nodo esta vacio 
					raiz.derecho = Nodo(nombre,contraseña)
					return raiz
				else:# no esta vacio 
					raiz.derecho = self.__insertar(raiz.derecho,nombre,contraseña)
					return raiz
			elif raiz.nombre > nombre:# dirreccion al lado derecho para el insertar
				if raiz.izquierdo == None:# verificacion si esta vacio 
					raiz.izquierdo = Nodo(nombre,contraseña)
					return raiz
				else:# no esta vacio 
					raiz.izquierdo = self.__insertar(raiz.izquierdo,nombre,contraseña)
					return raiz
			else:
				return raiz


	def insertar(self,nombre,contraseña):# recursividad 
		self.__raiz = self.__insertar(self.__raiz,nombre,contraseña)

############################################## eliminar #############################

	def __eliminar(self,raiz,nombre):
		if raiz!=None:# la raiz esta vacia 
			if raiz.nombre == nombre: # encuentra el nombre
				if raiz.izquierdo ==None and raiz.derecho ==None:# si es una hoja
					return None
				elif raiz.izquierdo == None  and raiz.derecho != None: # si tiene un hijo derecho
					return raiz.derecho
				elif raiz.izquierdo !=None  and raiz.derecho ==None:# si tiene un hijo izquierdo
					return raiz.izquierdo
				elif raiz.izquierdo !=None and raiz.derecho !=None: # si tiene dos hijos 
					padre = raiz # padre del cambio de nodo 
					aux = padre.izquierdo # nodo a cambiar 
					while aux.derecho!=None:
						padre = aux
						aux = aux.derecho
					raiz.nombre = aux.nombre# -- inicio cambio --
					raiz.contraseña = aux.contraseña
					raiz.estado = aux.estado
					raiz.lista = aux.lista# -- fin del cambio -- 
					if aux.izquierdo !=None and aux.derecho==None:# si el nodo tiene un hijo 
						if padre.derecho == aux:# verificando que puntero es del nodo ( nodo izquierdo para el padre es el hijo )
							padre.derecho = aux.izquierdo
							aux.izquierdo = None
						elif padre.izquierdo == aux:#verificando que puntero es del nodo ( nodo derecho para el padre es el hijo )
							padre.izquierdo = aux.izquierdo
							aux.izquierdo = None
					elif aux.izquierdo==None and aux.derecho==None:# nodo no tiene hijos 
						if padre.derecho == aux:# verificacion de que nodo es l hijo para eliminar el puntero ( derecho )
							padre.derecho=None
						elif padre.izquierdo == aux:#verificar de que nodo es el hijo para eliminar el puntero ( izquierdo )
							padre.izquierdo=None
					return raiz
			elif raiz.nombre > nombre:# direccion al lado izquierdo para buscar 
				raiz.izquierdo =  self.__eliminar(raiz.izquierdo,nombre)
				return raiz
			elif raiz.nombre < nombre:# dirrecion al lado derecho para buscar 
				raiz.derecho = self.__eliminar(raiz.derecho,nombre)
				return raiz
		else:
			return None

	def eliminar(self,nombre):# recursividad 
		self.__raiz = self.__eliminar(self.__raiz,nombre)



################################################## buscar #############################

	def __buscar(self,raiz,nombre):# para buscar nodo 
		if raiz!=None:
			if raiz.nombre == nombre:
				return raiz
			elif raiz.nombre > nombre:
				return self.__buscar(raiz.izquierdo,nombre)
			elif raiz.nombre < nombre:
				return self.__buscar(raiz.derecho,nombre)
		else:
			return None

	def buscar(self,nombre):
		return self.__buscar(self.__raiz,nombre)


######################################### actualizar #################################

	def actualizar(self, nombre,actualizacion):# actualizacion 
		if self.__raiz!=None:
			aux = self.buscar(nombre)
			if aux!=None:
				self.eliminar(nombre)
				self.insertar(actualizacion,aux.contraseña)
				self.buscar(actualizacion).estado = aux.estado
				self.buscar(actualizacion).lista = aux.lista
				return True
			else:
				return False
		else:
			return False

#################################################### imprimir ##########################

	def __imprimir(self,raiz):# imprimir 
		if raiz!=None:	
			self.__imprimir(raiz.izquierdo)
			print(raiz.nombre,raiz.contraseña,raiz.estado,raiz.lista)
			self.__imprimir(raiz.derecho)


	def imprimir(self):
		self.__imprimir(self.__raiz)
