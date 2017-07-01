from .nodo import Nodo


class Lista:

	def __init__(self):
		self.__primero = None
		self.__ultimo = None

############################################### vacio  #############################################

	def vacio(self):
		if self.__primero == None:
			return True
		else:
			return False

######################################### agregar  ##############################################

	def agregar(self,id,nombreOponente,tirosRealizados,tirosAcertados,tirosFallados,ganoPerdido,daño):
		if self.vacio(): # verificar si esta vacia 
			self.__primero = self.__ultimo = Nodo(id,nombreOponente,tirosRealizados,tirosAcertados,tirosFallados,ganoPerdido,daño)
		else:# no esta vacio 
			nuevo = Nodo(id,nombreOponente,tirosRealizados,tirosAcertados,tirosFallados,ganoPerdido,daño)
			self.__ultimo.siguiente = nuevo
			nuevo.anterior = self.__ultimo
			self.__ultimo = nuevo

########################################### eliminar #######################################

	def eliminar(self,id):
		aux = self.__primero
		if ~self.vacio():
			while aux:
				if aux.id ==id:
					if self.__primero == self.__ultimo:
						self.__primero = self.__ultimo = None
					elif aux == self.__primero:
						self.__primero = aux.siguiente
						self.__primero.anterior = None
						aux.siguiente = None
					elif aux == self.__ultimo:
						self.__ultimo = aux.anterior
						self.__ultimo.siguiente = None
						aux.anterior = None
					else:
						aux.anterior.siguiente = aux.siguiente
						aux.siguiente.anterior = aux.anterior
						aux.siguiente = None
						aux.anterior = None
					return aux
				aux = aux.siguiente
		return None

					

############################################### buscar ##############################################

	def buscar(self, id):
		aux = self.__primero
		if ~self.vacio():
			while aux:
				if aux.id == id:
					return aux
					break
				aux = aux.siguiente

	def registros(self):
		aux = self.__primero
		if ~self.vacio():
			while aux:
				yield aux
				aux = aux.siguiente

######################################## imprimir  ############################################

	def imprimir(self): 
		aux = self.__primero
		while aux:
			print(aux.id,aux.nombreOponente,aux.tirosRealizados,aux.tirosAcertados,aux.tirosFallados,aux.ganoPerdido,aux.daño)
			aux = aux.siguiente
