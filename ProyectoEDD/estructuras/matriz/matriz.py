from .nodo import Nodo

class Matriz:

	def __init__(self,columna,fila,profundida):
		self.matriz = None
		self.crear(columna,fila,profundida)

	def crear(self,columna,fila,profundida):
		contadorColumna = 1
		contadorFila = 1
		contadorProfundida = 1

		ultimoFila= None
		ultimoColumna = None
		ultimoProfundida = None
		auxColumna = None

		auxFila = None
		auxFondo = None

		while contadorProfundida<=profundida:
			#print("whileFondo")
			while contadorFila<=fila:
				#print("whileFila")

				while contadorColumna<=columna:
					if self.matriz==None:# crear el primer nodo de la matriz
						#print("entro1")
						nuevo = Nodo(contadorColumna,contadorFila,contadorProfundida)
						self.matriz = ultimoProfundida = ultimoFila = ultimoColumna = auxColumna = auxFondo = auxFila = nuevo
						#print(nuevo.columna,nuevo.fila,nuevo.profundida)
					elif ultimoProfundida.arriba ==None and ultimoFila.izquierda==None:# crear la linea de la matriz del primer nivel 
						#print("entro2")
						nuevo = Nodo(contadorColumna,contadorFila,contadorProfundida)
						ultimoColumna.siguiente = nuevo
						nuevo.anterior = ultimoColumna
						ultimoColumna = nuevo
						#print(nuevo.columna,nuevo.fila,nuevo.profundida)
					elif ultimoProfundida.arriba == None and ultimoFila.izquierda!=None:# es para crear las otras lineas de la matriz del primer nivel 
						#print("entro4")
						auxColumna = auxColumna.siguiente
						if auxColumna!=None:
							nuevo = Nodo(contadorColumna,contadorFila,contadorProfundida)
							ultimoColumna.siguiente = nuevo
							nuevo.anterior = ultimoColumna
							auxColumna.derecha = nuevo
							nuevo.izquierda = auxColumna
							ultimoColumna = nuevo
							#print(nuevo.columna,nuevo.fila,nuevo.profundida)
					elif ultimoProfundida.arriba !=None and ultimoFila.izquierda==None:# es para crear  la primera linea de la siguientes nivel  
						#print("entro6")
						auxFondo = auxFondo.siguiente
						if auxFondo !=None:
							nuevo = Nodo(contadorColumna,contadorFila,contadorProfundida)
							nuevo.anterior = ultimoColumna
							ultimoColumna.siguiente = nuevo
							auxFondo.abajo = nuevo
							nuevo.arriba = auxFondo
							ultimoColumna = nuevo
							#print(nuevo.columna,nuevo.fila,nuevo.profundida)
					elif ultimoProfundida!=None and ultimoFila.izquierda!=None:# para rellenar los siguiente niveles
						#print("entro7")
						auxFondo = auxFondo.siguiente
						auxColumna = auxColumna.siguiente
						nuevo = Nodo(contadorColumna,contadorFila,contadorProfundida)
						ultimoColumna.siguiente = nuevo
						nuevo.anterior = ultimoColumna
						auxColumna.derecha = nuevo
						nuevo.izquierda = auxColumna
						nuevo.arriba = auxFondo
						auxFondo.abajo = nuevo
						ultimoColumna = nuevo
						#print(nuevo.columna,nuevo.fila,nuevo.profundida)
					
					contadorColumna+=1

				contadorColumna=1
				contadorFila+=1
				if contadorFila <=fila:
					#print("entro3")
					if ultimoProfundida.arriba == None:#es para crear  el primer nodo de la siguiente linea del primer nivel 
						#print("1")
						auxColumna = ultimoFila
						nuevo = Nodo(contadorColumna,contadorFila,contadorProfundida)
						auxColumna.derecha = nuevo
						nuevo.izquierda = auxColumna
						ultimoFila = ultimoColumna = nuevo
						contadorColumna+=1
					elif ultimoProfundida.arriba!=None:# es para crear el primer nodo de los siguiente niveles
						#print("2")
						auxFila = auxFondo = auxFila.derecha
						auxColumna = ultimoFila
						nuevo = Nodo(contadorColumna,contadorFila,contadorProfundida)
						auxColumna.derecha = nuevo 
						nuevo.izquierda = auxColumna
						auxFondo.abajo = nuevo
						nuevo.arriba = auxFondo
						ultimoFila = ultimoColumna = nuevo
						contadorColumna+=1

					#print(nuevo.columna,nuevo.fila,nuevo.profundida)
						
			contadorFila = 1
			contadorProfundida+=1
			if contadorProfundida <= profundida:# crear el primer nodo del siguiente nivel 
				#print("entro5")
				nuevo = Nodo(contadorColumna,contadorFila,contadorProfundida)
				nuevo.arriba = ultimoProfundida
				ultimoProfundida.abajo = nuevo
				auxFondo = auxFila = ultimoProfundida
				ultimoProfundida = ultimoColumna = ultimoFila = auxColumna = nuevo
				contadorColumna+=1
				#print(nuevo.columna,nuevo.fila,nuevo.profundida)
				

	def imprimir(self):
		auxf = self.matriz
		auxc = self.matriz
		auxfo = self.matriz
		while auxfo:
			print("----Nivel"+str(auxfo.profundida)+"------")
			while auxf:
				print("----fila"+str(auxf.fila)+"------")
				while auxc:
					print("-----------------------------------------------------")
					if auxc.izquierda!=None:
						print("izquierda",auxc.izquierda.columna,auxc.izquierda.fila,auxc.izquierda.profundida,)
					if auxc.abajo!=None:
						print("abajo",auxc.abajo.columna,auxc.abajo.fila,auxc.abajo.profundida,)
					if auxc.anterior!=None:
						print("anterior",auxc.anterior.columna,auxc.anterior.fila,auxc.anterior.profundida,)
					print("columna",auxc.columna,auxc.fila,auxc.profundida,)
					if auxc.siguiente!=None:
						print("siguiente",auxc.siguiente.columna,auxc.siguiente.fila,auxc.siguiente.profundida,)
					if auxc.arriba!=None:
						print("arriba",auxc.arriba.columna,auxc.arriba.fila,auxc.arriba.profundida,)
					if auxc.derecha!=None:
						print("derecha",auxc.derecha.columna,auxc.derecha.fila,auxc.derecha.profundida,)
					print("-----------------------------------------------------")
					auxc = auxc.siguiente
				auxf = auxc= auxf.derecha
			auxfo = auxf = auxc = auxfo.abajo




#matriz = Matriz(3,3,3)#columan,fila,profundidad
#matriz.imprimir()





