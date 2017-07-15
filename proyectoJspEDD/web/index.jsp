<%-- 
    Document   : index
    Created on : 30/06/2017, 01:26:26 AM
    Author     : alejandro
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/style.css"/>
        <title>Proyecto</title>
    </head>
    <body>
        <center><p><h1>Menu de Inicio</h1></p></center>
        <table border="0" width="1000" align="center">
            <tr bgcolor="skyblue">
                <th><a href="index.jsp">Inicio Sesion</a></th>
                <th><a href="RegistroUsuario.jsp">Registro de Usuarios</a></th> 
            </tr> 
        </table>
    <br>
    <br>
    <center>
        <p><h2>Login</h2></p>
        <form action="AutenticarUsuario" method="post">
            <table> 
                    <tr>
                        <th>Nombre Usuario:</th>
                        <th><input type="text" name="user" id="user" min="0" max="10" pattern="[a-z0-9]+" required=""></th>
                    </tr>
                    <tr>
                        <th>Contraseña:</th>
                        <th><input type="password" name="pass" id="pass" min="0" max="10" pattern="[a-z0-9]+" required=""></th>
                    </tr>
                </table>
                <p><input type="submit" name="entrar" id="entrar" value="Entrar"></p>
        </form>
    </center>
        
    </body>
</html>
