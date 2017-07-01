class Nodo:

	def __init__(self,nombre, contraseña):
		self.nombre = nombre
		self.contraseña = contraseña
		self.estado = False # conetado o nodo 
		self.lista = None # puntero ala lista de registros 
		self.derecho = None
		self.izquierdo = None
		