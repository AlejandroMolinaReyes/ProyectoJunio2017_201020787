from .nodo import Nodo

class ArbolAVL:

	def __init__(self):
		self.__raiz = None
		self.texto = ""

############################## insertar #################################

#----------------------------- factor de equilibrio ---------------------

	def fe(self,raiz,nivel):#Factor Equilibrio
		if raiz==None:
			return 0;
		else:
			altura = self.fe(raiz.izquierdo,nivel+1)
			if nivel>altura:
				altura = nivel
			alturaDer = self.fe(raiz.derecho,nivel+1)
			if alturaDer>altura:
				altura = alturaDer
			return altura

#--------------------------------------------------------------------------

	def rotaciones(self,raiz):
		if raiz!=None:
			if raiz.factorEquilibrio==-2 and raiz.derecho.factorEquilibrio==-1:
				auxRaiz = raiz
				auxDer = raiz.derecho.izquierdo
				raiz = raiz.derecho
				raiz.izquierdo = auxRaiz
				auxRaiz.derecho = auxDer
				raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				raiz.izquierdo.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				return raiz
			if raiz.factorEquilibrio==2 and raiz.izquierdo.factorEquilibrio==1:
				auxRaiz = raiz 
				auxIzq = raiz.izquierdo.derecho
				raiz = raiz.izquierdo
				raiz.derecho = auxRaiz
				auxRaiz.izquierdo = auxIzq
				raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				raiz.derecho.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				return raiz
			if raiz.factorEquilibrio==-2 and raiz.derecho.factorEquilibrio==1:
				auxRaiz = raiz
				auxDer = raiz.derecho
				auxIzq = raiz.derecho.izquierdo
				raiz = auxIzq
				auxDer.izquierdo = raiz.derecho
				auxRaiz.derecho = raiz.izquierdo
				raiz.izquierdo = auxRaiz
				raiz.derecho = auxDer
				raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				raiz.derecho.factorEquilibrio = self.fe(raiz.derecho.izquierdo,1)-self.fe(raiz.derecho.derecho,1)#calculo factor de equilibrio
				raiz.izquierdo.factorEquilibrio = self.fe(raiz.izquierdo.izquierdo,1)-self.fe(raiz.izquierdo.derecho,1)#calculo factor de equilibrio
				return raiz
			if raiz.factorEquilibrio==2 and raiz.izquierdo.factorEquilibrio==-1:
				auxRaiz = raiz
				auxIzq = raiz.izquierdo
				auxDer = raiz.izquierdo.derecho
				raiz = auxDer
				auxIzq.derecho = raiz.izquierdo
				auxRaiz.izquierdo = raiz.derecho
				raiz.izquierdo = auxIzq
				raiz.derecho = auxRaiz
				raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				raiz.derecho.factorEquilibrio = self.fe(raiz.derecho.izquierdo,1)-self.fe(raiz.derecho.derecho,1)#calculo factor de equilibrio
				raiz.izquierdo.factorEquilibrio = self.fe(raiz.izquierdo.izquierdo,1)-self.fe(raiz.izquierdo.derecho,1)#calculo factor de equilibrio
				return raiz
			if raiz.factorEquilibrio==2 and raiz.izquierdo.factorEquilibrio==0:
				auxRaiz = raiz
				auxIzq = raiz.izquierdo
				raiz = auxIzq
				auxRaiz.izquierdo = raiz.derecho
				raiz.derecho = auxRaiz
				raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				raiz.derecho.factorEquilibrio = self.fe(raiz.derecho.izquierdo,1)-self.fe(raiz.derecho.derecho,1)#calculo factor de equilibrio
				return raiz
			if raiz.factorEquilibrio==-2 and raiz.derecho.factorEquilibrio==0:
				auxRaiz = raiz
				auxDer = raiz.derecho
				raiz = auxDer
				auxRaiz.derecho = raiz.izquierdo
				raiz.izquierdo = auxRaiz
				raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				raiz.izquierdo.factorEquilibrio = self.fe(raiz.izquierdo.izquierdo,1)-self.fe(raiz.izquierdo.derecho,1)#calculo factor de equilibrio
				return raiz
			return raiz



#-------------------------------- insertar --------------------------------
	
	def __insertar(self,raiz,usuario,nick,contra):
		if raiz==None:# si la raiz esta vacia inserto
			return Nodo(usuario,nick,contra,0)
		else:
			if raiz.nickName<nick:# buscando la posicion del nodo 
				if raiz.derecho==None:# si el nodo izquierdo esta vacio
					raiz.derecho = Nodo(usuario,nick,contra,0)
					raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
					raiz = self.rotaciones(raiz)
					return raiz
				else:
					raiz.derecho = self.__insertar(raiz.derecho,usuario,nick,contra)#direccionar nodo derecho 
					raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
					raiz = self.rotaciones(raiz)
					return raiz
			elif raiz.nickName>nick:
				if raiz.izquierdo == None:
					raiz.izquierdo = Nodo(usuario,nick,contra,0)
					raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
					raiz = self.rotaciones(raiz)
					return raiz
				else:
					raiz.izquierdo = self.__insertar(raiz.izquierdo,usuario,nick,contra)#direccionar nodo izquierdo
					raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
					raiz = self.rotaciones(raiz)
					return raiz
			else:
				return raiz


	def insertar(self,usuario,nick, contra):
		self.__raiz = self.__insertar(self.__raiz,usuario,nick,contra)


#--------------------------------------------------------------------------



############################################################################

######################################## eliminar ##########################

#------------------------------- buscar meno de los mayores ----------------

	def menor(self,raiz):# buscar el menor de los mayores nodos
		if raiz.derecho!=None:
			raiz.derecho , aux = self.menor(raiz.derecho)
			raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
			raiz = self.rotaciones(raiz)
			return  raiz , aux
		else:
			return raiz.izquierdo ,raiz


#---------------------------------------------------------------------------

	def __eliminar(self,raiz,nick):
		if raiz!=None:# la raiz esta vacia 
			if raiz.nickName == nick: # encuentra el nombre
				if raiz.izquierdo ==None and raiz.derecho ==None:# si es una hoja
					return None
				elif raiz.izquierdo == None  and raiz.derecho != None: #si tiene un hijo derecho
					return raiz.derecho
				elif raiz.izquierdo !=None  and raiz.derecho ==None:# si tiene un hijo izquierdo
					return raiz.izquierdo
				elif raiz.izquierdo !=None and raiz.derecho !=None: # si tiene dos hijos 
					raiz.izquierdo , aux = self.menor(raiz.izquierdo)
					raiz.nickName = aux.nickName
					raiz.usuario = aux.usuario
					raiz.contraseña = aux.contraseña
					raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
					raiz = self.rotaciones(raiz)
					return raiz
			elif raiz.nickName > nick:# direccion al lado izquierdo para buscar 
				raiz.izquierdo =  self.__eliminar(raiz.izquierdo,nick)
				raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				raiz = self.rotaciones(raiz)
				return raiz
			elif raiz.nickName < nick:# dirrecion al lado derecho para buscar 
				raiz.derecho = self.__eliminar(raiz.derecho,nick)
				raiz.factorEquilibrio = self.fe(raiz.izquierdo,1)-self.fe(raiz.derecho,1)#calculo factor de equilibrio
				raiz = self.rotaciones(raiz)
				return raiz
		else:
			return None

	def eliminar(self,nick):# recursividad 
		self.__raiz = self.__eliminar(self.__raiz,nick)

############################################################################

####################################### buscar #############################

	def __buscar(self,raiz,nick):# para buscar nodo 
		if raiz!=None:
			if raiz.nickName == nick:
				return raiz
			elif raiz.nickName > nick:
				return self.__buscar(raiz.izquierdo,nick)
			elif raiz.nickName < nick:
				return self.__buscar(raiz.derecho,nick)
		else:
			return None

	def buscar(self,nick):
		return self.__buscar(self.__raiz,nick)

#############################################################################

################################ actualizar #################################

	def actualizar(self, nick,nickName,contra,usuario):# actualizacion 
		if self.__raiz!=None:
			aux = self.buscar(nick)
			if aux!=None:
				self.eliminar(nick)
				self.insertar(usuario,nickName, contra)
				return True
			else:
				return False
		else:
			return False

###############################################################################

##################################### reportes #######################################

#------------------------------------  imagen -----------------------------

	def __imagen(self,raiz):
		if raiz!=None:
			if raiz.izquierdo==None and raiz.derecho==None and self.__raiz==raiz:
				self.texto = self.texto + "\""+raiz.nickName+"\""
			if raiz.izquierdo!=None:
				self.texto = self.texto + "\""+raiz.nickName+"\""
				self.texto = self.texto +"->"+"\""+raiz.izquierdo.nickName+"\"[label=\"izquierdo\"];\n"
			if raiz.derecho!=None:
				self.texto = self.texto + "\""+raiz.nickName+"\""
				self.texto = self.texto +"->"+"\""+raiz.derecho.nickName+"\"[label=\"derecho\"];\n"
			self.__imagen(raiz.izquierdo)
			self.__imagen(raiz.derecho)

	def imagen(self):
		self.texto = "digraph G { \n node[style=filled,shape=record,width=1,height=1];\n"
		self.texto = self.texto + "	subgraph clusterArbol{ \n label=\"arbol AVL\";\n"
		self.__imagen(self.__raiz)
		self.texto = self.texto  + "\n		}\n"
		self.texto = self.texto  + "\n}"
		return self.texto

#---------------------------------------------------------------------------------------------

################################################################################

################################## imprimir ###################################

	def __imprimir(self,raiz):
		if raiz!=None:
			self.__imprimir(raiz.izquierdo)
			print(raiz.nickName,raiz.factorEquilibrio,'-')
			if raiz.izquierdo!=None:
				print(raiz.izquierdo.nickName,raiz.izquierdo.factorEquilibrio,"izq")
			if raiz.derecho!=None:
				print(raiz.derecho.nickName,raiz.derecho.factorEquilibrio,"der")
			self.__imprimir(raiz.derecho)

	def imprimir(self):
		self.__imprimir(self.__raiz)


############################################################################
