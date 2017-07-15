from flask import Flask , request
from estructuras import Arbol, Lista, Matriz, ArbolAVL
from juego import Juego

usuarios = Arbol()
usuarios.insertar("admin","admin")
contadorId = 0
listaUser = []


servidor = Flask(__name__)


@servidor.route("/registrar",methods=['POST'])
def registrarUsuario():# registra a los usuarios
	print("-----Registro Usuario-----")
	user = str(request.form['user'])
	password = str(request.form['pass'])
	global usuarios
	global listaUser
	if usuarios.buscar(user)==None:
		usuarios.insertar(user,password)
		listaUser.append(user)
		print("Registro exitoso")
		usuarios.imprimir()
		print("--------------------------")
		return "True"
	else:
		usuarios.imprimir()
		print("--------------------------")
		return "False"
	

@servidor.route("/auntenticar",methods=['POST'])
def autenticarUsuario():# ver si existe el usuario
	print("-----------Login----------")
	user = str(request.form['user'])
	password = str(request.form['pass'])
	global usuarios
	auxUser = usuarios.buscar(user)
	if auxUser==None:
		print("No existe Usuario")
		usuarios.imprimir()
		print("--------------------------")
		return "False"
	elif auxUser.nombre == user and auxUser.contraseña == password:
		auxUser.estado = "1"
		usuarios.imprimir()
		print("Exitoso login")
		print("--------------------------")
		return "True"
	else:
		print("usuario o contraseña mala")
		print("--------------------------")
		return "False"
	print("--------------------------")

@servidor.route("/CerrarSesion",methods=['POST'])
def cerrarSesion():#cerrar sesion
	print("-----------Cerrar sesion----------")
	global usuarios
	user = str(request.form['user'])
	auxUser = usuarios.buscar(user)
	if auxUser!=None:
		auxUser.estado= "0"
		print("Session Cerrada")
		usuarios.imprimir()
		print("--------------------------")
		return "True"
		print("Session Cerrada")
		usuarios.imprimir()
		print("--------------------------")
	return "False"

@servidor.route("/cargarUsuario",methods=['POST'])
def cargarUsuarios():#cargar usuarios de archivo
	print("-----------cargar usuario----------")
	user = str(request.form['user'])
	password = str(request.form['pass'])
	estado = str(request.form['estado'])
	global usuarios
	global listaUser
	if user!="" and password!="" and usuarios.buscar(user)==None:
		usuarios.insertar(user,password)
		listaUser.append(user)
	auxUser = usuarios.buscar(user)
	if auxUser!=None:
		auxUser.estado = estado
		print("carga con exito Usuarios")
		usuarios.imprimir()
		print("--------------------------")
		return "True"
	print("--------------------------")
	return "False"
	

@servidor.route("/cargarJuegos",methods=['POST'])
def cargarJuegos():#cargar lista de juegos
	print("-----------cargar juegos----------")
	user = str(request.form['user'])
	oponente = str(request.form['oponente'])
	tirosRealizados = str(request.form['tirosR'])
	tirosAcertados = str(request.form['tirosA'])
	tirosFallados = str(request.form['tirosF'])
	gano = str(request.form['gano'])
	dañoRecibido = str(request.form['daño'])
	global usuarios
	global contadorId
	usuario = usuarios.buscar(user)
	print("-----------------------usar a ingrear -------")
	print(usuario.nombre)
	print("----------------------------------")
	if usuario!=None:
		if usuario.lista!=None:
			contadorId+=1
			usuario.lista.agregar(contadorId,oponente,tirosRealizados,tirosAcertados,tirosFallados,gano,dañoRecibido)
			print("carga exitosa")
			usuario.lista.imprimir()
			print("----------------------------------")
			return "True"
		else:
			contadorId+=1
			usuario.lista = Lista()
			usuario.lista.agregar(contadorId,oponente,tirosRealizados,tirosAcertados,tirosFallados,gano,dañoRecibido)
			print("carga exitosa")
			usuario.lista.imprimir()
			print("----------------------------------")
			return "True"
	print("carga Fallida")
	print("----------------------------------")
	return "False"

@servidor.route("/listaUsuarios",methods=['POST'])
def listaUsuarios():
	global listaUser
	cadena =""
	for item in listaUser:
		cadena = item+","+cadena
	return cadena

@servidor.route("/actualizarUsuario",methods=['POST'])
def actualizarUser():
	print("-----------Actualizar usuario----------")
	user = str(request.form['user'])
	password = str(request.form['pass'])
	update = str(request.form['update'])
	global usuarios
	global listaUser
	if user == update:
		auxUser = usuarios.buscar(update)
		if auxUser!=None:
			auxUser.contraseña = password
			usuarios.imprimir()
			print("----------------------------------")
			return "True"
	
	else:
		if usuarios.buscar(update)!=None:
			listaUser.remove(update)
			usuarios.eliminar(update)
			listaUser.append(user)
			usuarios.insertar(user,password)
			usuarios.imprimir()
			print("----------------------------------")
			return "True"
	usuarios.imprimir()
	return "False"
	print("----------------------------------")

@servidor.route("/EliminarUsuario",methods=['POST'])
def eliminarUser():
	print("-----------Eliminar usuario----------")
	eliminar = str(request.form['delete'])
	global usuarios
	global listaUser
	if usuarios.buscar(eliminar)!=None:
		listaUser.remove(eliminar)
		usuarios.eliminar(eliminar)
		usuarios.imprimir()
		print("----------------------------------")
		return "True"
	usuarios.imprimir()
	print("----------------------------------")
	return "False"

@servidor.route("/naves",methods=['POST'])
def naves():
	user1 = str(request.form['user1'])
	columna = str(request.form['columna'])
	fila = str(request.form['fila'])
	nivel = str(request.form['nivel'])
	modo = str(request.form['modo'])
	dirrecion = str(request.form['dirrecion'])
	return "en contruccion"

@servidor.route("/JuegoActual",methods=['POST'])
def juegoActual():
	print("-----------Juego Actual----------")
	user1 = str(request.form['user1'])
	user2 = str(request.form['user2'])
	x = str(request.form['x'])
	y = str(request.form['y'])
	variante = str(request.form['variante'])
	tiempo = str(request.form['tiempo'])
	disparo = str(request.form['disparo'])
	rafaga = str(request.form['rafaga'])
	juego  = Juego(x,y,variante,tiempo,disparo,rafaga)
	global usuarios
	if x.isdigit() and y.isdigit():
		x =int(x)
		y =int(y)
		user1M = Matriz(x,y,4)
		user2M = Matriz(x,y,4)
		if usuarios.buscar(user1)!=None and usuarios.buscar(user2)!=None:
			usuarios.buscar(user1).juego =juego
			usuarios.buscar(user2).juego =juego
			usuarios.buscar(user1).matriz = user1M
			usuarios.buscar(user2).matriz = user2M
			print("Carga exitosa")
			print("----------------------------------")
			return "True"
	print("Carga Fallida")
	print("----------------------------------")
	return "False"
@servidor.route("/imgArbol",methods=['POST'])
def imgArbol():
	print("-----------img Arbol----------")
	global usuarios
	usuarios.imagen()
	print("exitoso")
	print("---------------------")
	return usuarios.texto

@servidor.route("/imgEspejo",methods=['POST'])
def imgEspejo():
	print("-----------img Espejo----------")
	global usuarios
	usuarios.espejo()
	print("exitoso")
	print("---------------------")
	return usuarios.texto

@servidor.route("/alturaArbol",methods=['POST'])
def arbolAltura():
	print("-----------Altura del Arbol----------")
	global usuarios
	altura = usuarios.altura()
	print("exitoso")
	print("----------------------------")
	return str(altura+1)

@servidor.route("/nivelArbol",methods=['POST'])
def arbolNivel():
	print("-----------nivel del Arbol----------")
	global usuarios
	nivel = usuarios.altura()
	print("exitoso")
	print("----------------------------")
	return str(nivel)

@servidor.route("/hojaslArbol",methods=['POST'])
def arbolHojas():
	print("-----------hojas del Arbol----------")
	global usuarios
	hojas = usuarios.hojas()
	print("exitoso")
	print("----------------------------")
	return str(hojas)

@servidor.route("/ramaArbol",methods=['POST'])
def ramaHojas():
	print("-----------rama del Arbol----------")
	global usuarios
	rama = usuarios.rama()
	print("exitoso")
	print("----------------------------")
	return str(rama)


if __name__ == "__main__":
	servidor.run(debug=True, host='127.0.0.1', port=9090)