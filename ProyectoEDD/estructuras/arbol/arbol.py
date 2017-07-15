from .nodo import Nodo

class Arbol:

	def __init__(self):
		self.__raiz = None
		self.texto = ""

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

##################################### reportes #######################################

#------------------------------------  imagen con lista -----------------------------

	def __imagen(self,raiz):
		if raiz!=None:
			if raiz.izquierdo==None and raiz.derecho==None and self.__raiz==raiz:
				self.texto = self.texto + "\""+raiz.nombre+"\""
			if raiz.izquierdo!=None:
				self.texto = self.texto + "\""+raiz.nombre+"\""
				self.texto = self.texto +"->"+"\""+raiz.izquierdo.nombre+"\"[label=\"izquierdo\"];\n"
			if raiz.derecho!=None:
				self.texto = self.texto + "\""+raiz.nombre+"\""
				self.texto = self.texto +"->"+"\""+raiz.derecho.nombre+"\"[label=\"derecho\"];\n"
			self.__imagen(raiz.izquierdo)
			self.__imagen(raiz.derecho)

	def __imgLista(self,raiz):
		if raiz!=None:
			if raiz.lista!=None:
				self.texto = self.texto + "subgraph cluster"+raiz.nombre+"{ \n label=\""+raiz.nombre+"\"\n"
				for nodo in raiz.lista.registros():
					if nodo.anterior!=None:
						self.texto = self.texto + "\""+str(nodo.id)+","+nodo.nombreOponente+"\""+"->"+"\""+str(nodo.anterior.id)+","+nodo.anterior.nombreOponente+"\"\n"
					if nodo.siguiente!=None:
						self.texto = self.texto + "\""+str(nodo.id)+","+nodo.nombreOponente+"\""+"->"+"\""+str(nodo.siguiente.id)+","+nodo.siguiente.nombreOponente+"\"\n"
				self.texto = self.texto +"}\n"
			self.__imgLista(raiz.izquierdo)
			self.__imgLista(raiz.derecho)

	def imagen(self):
		self.texto = "digraph G { \n node[style=filled,shape=record,width=1,height=1];\n"
		self.texto = self.texto + "	subgraph clusterArbol{ \n label=\"arbol\";\n"
		self.__imagen(self.__raiz)
		self.texto = self.texto  + "\n}\n"
		self.__imgLista(self.__raiz)
		self.texto = self.texto  + "\n}"

#---------------------------------------------------------------------------------------------

#------------------------------------- imagen espejo del arbol -------------------------------

	def __espejo(self,raiz):
		if raiz!=None:
			if raiz.izquierdo==None and raiz.derecho==None and self.__raiz==raiz:
				self.texto = self.texto + "\""+raiz.nombre+"\""
			if raiz.derecho!=None:
				self.texto = self.texto + "\""+raiz.nombre+"\""
				self.texto = self.texto +"->"+"\""+raiz.derecho.nombre+"\"[label=\"derecho\"];\n"
			if raiz.izquierdo!=None:
				self.texto = self.texto + "\""+raiz.nombre+"\"" 
				self.texto = self.texto +"->"+"\""+raiz.izquierdo.nombre+"\"[label=\"izquierdo\"];\n"
			self.__espejo(raiz.izquierdo)
			self.__espejo(raiz.derecho)

	def espejo(self):
		self.texto = "digraph G { \n node[style=filled,shape=record,width=1,height=1];\n"
		self.texto = self.texto + "	subgraph clusterArbol{ \n label=\"Espejo\";\n"
		self.__espejo(self.__raiz)
		self.texto = self.texto  + "\n}\n"
		self.texto = self.texto + "}"

#------------------------------------------------------------------------------------------------

#-------------------------------------- Nivel --------------------------------------------------
	
	def __altura(self, raiz,nivel):
		if raiz==None:
			return 0;
		else:
			altura = self.__altura(raiz.izquierdo,nivel+1)
			if nivel>altura:
				altura = nivel
			alturaDer = self.__altura(raiz.derecho,nivel+1)
			if alturaDer>altura:
				altura = alturaDer
			return altura
			

	def altura(self):
		return  self.__altura(self.__raiz,0)
#------------------------------------------------------------------------------------------------

#-------------------------------------- Nodos hojas ---------------------------------------------

	def __hojas(self,raiz,contador):
		if raiz==None:
			return contador
		else:
			if raiz.izquierdo==None and raiz.derecho==None and self.__raiz!=raiz:
				contador+=1
			contador = self.__hojas(raiz.izquierdo,contador)
			contador = self.__hojas(raiz.derecho,contador)
			return contador

	def hojas(self):
		return self.__hojas(self.__raiz,0)

#------------------------------------------------------------------------------------------------

#-------------------------------------- Nodos rama ----------------------------------------------

	def __rama(self,raiz,contador):
		if raiz==None:
			return contador
		else:
			if raiz.izquierdo!=None or raiz.derecho!=None and self.__raiz!=raiz:
				contador+=1
			contador = self.__rama(raiz.izquierdo,contador)
			contador = self.__rama(raiz.derecho,contador)
			return contador

	def rama(self):
		return self.__rama(self.__raiz,0)

#------------------------------------------------------------------------------------------------


#################################################### imprimir ##########################

	def __imprimir(self,raiz):# imprimir 
		if raiz!=None:	
			self.__imprimir(raiz.izquierdo)
			print(raiz.nombre,raiz.contraseña,raiz.estado)
			self.__imprimir(raiz.derecho)


	def imprimir(self):
		self.__imprimir(self.__raiz)
