<%-- 
    Document   : MenuPrincipal
    Created on : 30/06/2017, 04:34:40 AM
    Author     : alejandro
--%>

<%@page import="static consulta.WebServer.consultaPython"%>
<%@page import="com.squareup.okhttp.FormEncodingBuilder"%>
<%@page import="com.squareup.okhttp.RequestBody"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/style.css"/>
        <title>Proyecto</title>
    </head>
    <body>
        <center><p><h1>Bienvenido Usuario "<%= session.getAttribute("user") %>"</h1></p></center>
        <table border="0" width="1000" align="center">
             <tr bgcolor="skyblue">
                <th><a href="MenuPrincipal.jsp">Usuarios</a></th>
                <th><a href="CargarDatos.jsp">Cargar Datos</a></th>
                <th><a href="Reportes.jsp">Reportes</a></th>
                <th><a href="index.jsp">Cerrar Sesíon</a></th> 
            </tr> 
        </table>
        <center>
            <p><h2>Usuarios</h2></p><br>
            <form action="ActualizarUsuario" method="post">
                <table>
                    <p><h3>Modificar</h3></p>
                    <tr>
                        <th>Selecionar un usuario:</th>
                        <th>
                            <select name="update" id="update" required="">
                            <%          
                            String valor =  consultaPython("listaUsuarios", null);
                            String[]usuarios = valor.split(",");
                            for(String cadena:usuarios){
                                if(!cadena.equals("")){
                            %>
                            <option><%= cadena%> </option>
                            <%  }
                            }
                            %>
                        </select>
                        </th>
                    </tr>
                    <tr>
                        <th>Nombre Usuario:</th>
                        <th><input type="text" name="user" id="user" min="0" max="10" pattern="[a-z0-9]+" required=""></th>
                    </tr>
                    <tr>
                        <th>Contraseña:</th>
                        <th><input type="text" name="pass" id="pass" min="0" max="10" pattern="[a-z0-9]+" required=""></th>
                    </tr> 
                </table>
                        <center><p><input type="submit" name="actualizar" id="actualizar" value="Actualizar"></p></center>
            </form>
            <form action="EliminarUsuario" method="post">
                <table>
                    <p><h3>Eliminar</h3></p>
                    <tr>
                        <th>Selecionar un usuario:</th>
                        <th>
                        <select name="delete" id="delete" required="">
                            <%          
                            String consulta =  consultaPython("listaUsuarios", null);
                            String[]cadenas = consulta.split(",");
                            for(String cadena:cadenas){
                                if(!cadena.equals("")){
                            %>
                            <option><%= cadena%> </option>
                            <%  }
                            }
                            %>
                        </select>
                        </th>
                    </tr>
                </table>
                <center><p><input type="submit" name="eliminar" id="Elimnar" value="Eliminar"></p></center>
            </form>
                
        </center>

    </body>
</html>
