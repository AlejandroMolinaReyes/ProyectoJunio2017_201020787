class Nodo:

	def __init__(self,id,nombreOponente,tirosRealizados,tirosAcertados,tirosFallados,ganoPerdido,daño):
		self.id = id
		self.nombreOponente = nombreOponente
		self.tirosRealizados = tirosRealizados
		self.tirosAcertados = tirosAcertados
		self.tirosFallados = tirosFallados
		self.ganoPerdido = ganoPerdido
		self.daño = daño
		self.siguiente = None
		self.anterior = None
