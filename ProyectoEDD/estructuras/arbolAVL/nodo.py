class Nodo:

	def __init__(self,usuario,nick,contra,fe):
		self.usuario = usuario
		self.nickName = nick
		self.contraseña = contra
		self.factorEquilibrio = fe
		self.derecho = None
		self.izquierdo = None