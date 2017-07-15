class Nodo:

	def __init__(self,nombre, contraseña):
		self.nombre = nombre
		self.contraseña = contraseña
		self.estado = "0" # conetado o nodo 
		self.lista = None # puntero ala lista de registros 
		self.matriz = None# puntero matriz del juego
		self.juego = None
		self.derecho = None
		self.izquierdo = None
		