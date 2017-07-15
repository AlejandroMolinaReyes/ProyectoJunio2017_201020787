class TablaHash:

	def __init__(self):
		self.factorCarga = 0# porcentaje ocupacion de la carga elemnentos/tamaño
		self.elementos = 0#elementos actuales en la tabla 
		self.__tamaño = 47#capacidad de alojamiento de elementos de la tabla
		self.__tabla = []
		for valor in range(self.__tamaño):
			self.__tabla.append(None)


	def __hash(self,key):
		sumaASCCI = 0# inicilizando variable de la suma ascci de la cadena
		contador = 0# inicilizandp el contador para recorrer la cadena
		resultado = ""# el resultado del hash

		for letra in key:# sumando el valor ascci de los caracteres
			sumaASCCI+=ord(letra)
		sumaASCCI = sumaASCCI*sumaASCCI# la suma al cuadrado
		sumaASCCI = str(sumaASCCI)# converto a string la suma ascci
		posicion = str(len(sumaASCCI)/2).split(".")#la mitad de la cadena y miro si la cadena es par o impar con el decimal
		iteracion = int(posicion[0])#convierto a entero las tiraciones 		
		while contador<=iteracion-1:#recorrdo la mitad de la cadena 
			if posicion[1]=="0" and contador==iteracion-1:# si par y si es la ultima iteracion
				resultado = sumaASCCI[contador]+sumaASCCI[contador+1]# si es par es la ultima iteracion y la siguiente
			if posicion[1]!="0" and contador==iteracion-1:# si impar y si es la ultima iteracion
				resultado = sumaASCCI[contador+1]#si es impar la ultima iteracion	
			contador+=1
		return int(resultado)

	def insertar(self,key, valor):
		clave = self.__hash(key)
		if clave < self.__tamaño:
			pass
		else:
			pass

		print(valor,clave)

	def eliminar(self,key):
		pass

	def buscar(self,key):
		pass




tablaHash = TablaHash()
tablaHash.insertar(" ","admin")

