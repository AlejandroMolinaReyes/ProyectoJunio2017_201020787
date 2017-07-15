<%-- 
    Document   : Reportes.jsp
    Created on : 30/06/2017, 06:40:14 AM
    Author     : alejandro
--%>

<%@page import="static consulta.graphviz.graficar"%>
<%@page import="static archivo.crearArchivo.crearArchivo"%>
<%@page import="static consulta.WebServer.consultaPython"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
        <%
            String arbol = consultaPython("imgArbol", null);
            crearArchivo(arbol, "arbol");
            graficar("arbol");
            
            String espejo = consultaPython("imgEspejo", null);
            crearArchivo(espejo, "espejo");
            graficar("espejo");
            Thread.sleep(2000);
        %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/style.css"/>
        <title>Proyecto</title>
        <meta http-equiv="Expires" content="0">
        <meta http-equiv="Last-Modified" content="0">
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
        <center><p><h2>Reporte</h2></p></center>
        <center>
            <tabla>
                <tr>
                    <th>
                        <figcaption>Arbol de Usuarios</figcaption>
                        <figure>
                            <div class="imagen"><img src="img/arbol.jpg" alt=" ✘ Imagen No Cargada." title="Arbol." width="640" height="480" ></div>
                        </figure>
                    </th>
                </tr>
                <tr>
                    <th>
                        <figure>
                            <figcaption>Arbol Espejo</figcaption>
                            <div class="imagen"><img src="img/espejo.jpg" alt=" ✘ Imagen No Cargada." title="Espejo." width="640" height="480" ></div>
                        <figure>
                    </th>
                </tr>
                <tr>
                    <th>Altura del Arbol:</th>
                    <th>
                        <%String altura =  consultaPython("alturaArbol", null);%>
                        <%= altura%>
                    </th>
                </tr>
                <tr>
                    <th>Nivel del Arbol:</th>
                    <th>
                        <%String nivel =  consultaPython("nivelArbol", null);%>
                        <%= nivel%>
                    </th>
                </tr>
                <tr>
                    <th>Nodos Hojas:</th>
                    <th>
                        <%String nodoHoja =  consultaPython("hojaslArbol", null);%>
                        <%= nodoHoja%>
                    </th>
                </tr>
                <tr>
                    <th>Nodos Rama:</th>
                    <th>
                        <%String nodoRama =  consultaPython("ramaArbol", null);%>
                        <%= nodoRama%>
                    </th>
                </tr>
            </tabla>
        </center>
        
        
    </body>
</html>
