<%-- 
    Document   : CargarDatos
    Created on : 30/06/2017, 06:37:58 PM
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
        <center><p><h1>Bienvenido Usuario "<%= session.getAttribute("user") %>"</h1></p></center>
        <table border="0" width="1000" align="center">
             <tr bgcolor="skyblue">
                <th><a href="MenuPrincipal.jsp">Usuarios</a></th>
                <th><a href="CargarDatos.jsp">Cargar Datos</a></th>
                <th><a href="Reportes.jsp">Reportes</a></th>
                <th><a href="index.jsp">Cerrar Sesíon</a></th> 
            </tr> 
        </table>
        <br>
        <br>
        <center>
            <p><h2>Cargar Datos</h2></p>
            <form action="CargarDatos" enctype="multipart/form-data" method="post">
                <p>Selecione un archivo:<input type="file" required="" accept=".csv" name="path" id="user"><br></p>
                <p><input type="radio" name="gender" value="usuario" checked>Usuarios
                    <input type="radio" name="gender" value="juegos">Juegos
                    <input type="radio" name="gender" value="juego">JuegoActual
                    <input type="radio" name="gender" value="naves">Naves<p/>
                <p><input type="submit" id="cargar" value="Cargar Datos"></p>
            </form>
        </center>
    </body>
</html>
