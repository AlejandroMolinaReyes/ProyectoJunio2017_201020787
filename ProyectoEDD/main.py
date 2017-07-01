from flask import Flask , request
from estructuras import Arbol, Lista

usuarios = Arbol()

servidor = Flask(__name__)


@servidor.route("/registrar",methods=['POST'])
def registrarUsuario():# registra a los usuarios
	print("-----Registro Usuario-----")
	user = str(request.form['user'])
	password = str(request.form['pass'])

	if usuarios.buscar(user)==None:
		usuarios.insertar(user,password)
		print("Registro exitoso")
		usuarios.imprimir()
		print("--------------------------")
		return "False"
	else:
		usuarios.imprimir()
		print("--------------------------")
		return "True"
	

@servidor.route("/auntenticar",methods=['POST'])
def autenticarUsuario():# ver si existe el usuario
	print("-----------Login----------")
	user = str(request.form['user'])
	password = str(request.form['pass'])
	auxUser = usuarios.buscar(user)
	if auxUser==None:
		print("No existe Usuario")
		usuarios.imprimir()
		print("--------------------------")
		return "False"
	elif auxUser.nombre == user and auxUser.contraseña == password:
		auxUser.estado = True
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
def cerrarSesion():
	print("-----------Cerrar----------")
	user = str(request.form['user'])
	auxUser = usuarios.buscar(user)
	if auxUser!=None:
		auxUser.estado= False
		print("Session Cerrada")
		usuarios.imprimir()
		print("--------------------------")
		return "True"
		print("Session Cerrada")
		usuarios.imprimir()
		print("--------------------------")
	return "False"
@servidor.route("/CargarUsuario",methods=['POST'])
def cargarUsuarios():
	print("-----------cargar usuario----------")
	user = str(request.form['user'])
	password = str(request.form['pass'])
	estado = str(request.form['user'])
	if estado == "1":
		estado=True
	elif estado == "0":
		estado = False
	usuarios.insertar(user,password)
	auxUser = usuarios.buscar(user)
	if auxUser!=None:
		auxUser.estado = estado
		print("carga con exito")
	print("--------------------------")



if __name__ == "__main__":
  servidor.run(debug=True, host='127.0.0.1', port=9090)