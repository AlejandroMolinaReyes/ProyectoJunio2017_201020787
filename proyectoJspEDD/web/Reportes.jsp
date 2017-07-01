<%-- 
    Document   : Reportes.jsp
    Created on : 30/06/2017, 06:40:14 AM
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
                 <th><a href="MenuPrincipal.jsp">Juego</a></th>
                <th><a href="CargarDatos.jsp">Cargar Datos</a></th>
                <th><a href="Reportes.jsp">Reportes</a></th>
                <th><a href="CerrarSesion">Cerrar Sesíon</a></th>
            </tr> 
        </table>
        <center><p><h2>Reporte</h2></p></center>
        
        
    </body>
</html>
