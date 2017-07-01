class Nodo:

	def __init__(self,columna,fila,profundida):
		self.dato = None
		self.fila = fila
		self.columna = columna
		self.profundida = profundida
		self.siguiente = None
		self.anterior = None
		self.arriba = None
		self.abajo = None
		self.izquierda = None
		self.derecha = None
