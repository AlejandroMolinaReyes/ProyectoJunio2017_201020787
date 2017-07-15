<%-- 
    Document   : MenuUser
    Created on : 4/07/2017, 02:28:47 AM
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
                <th><a href="MenuUser.jsp">Juego</a></th>
                <th><a href="index.jsp">Cerrar Sesíon</a></th> 
            </tr> 
        </table>
        <center>
        <p><h2>Juego</h2></p><br>
    </body>
</html>
