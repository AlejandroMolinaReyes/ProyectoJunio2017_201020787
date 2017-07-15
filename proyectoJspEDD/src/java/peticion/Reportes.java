/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package peticion;

import static consulta.WebServer.consultaPython;
import static consulta.graphviz.graficar;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author alejandro
 */
@WebServlet(name = "Reportes", urlPatterns = {"/Reportes"})
public class Reportes extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            String arbol = consultaPython("imgArbol", null);
            this.crearFile(arbol, "arbol");
            graficar("arbol");
            
            String espejo = consultaPython("imgEspejo", null);
            this.crearFile(espejo, "espejo");
            graficar("espejo");
            
            response.sendRedirect("Reportes.jsp");
        }catch(Exception e){}
    }
   
   private void crearFile(String respuesta,String nombre){
       try{
        String ruta = "C:\\proyectoJspEDD\\web\\graficar\\"+nombre+".txt";
            File archivo = new File(ruta);
            BufferedWriter bw;
            if(archivo.exists()) {
                bw = new BufferedWriter(new FileWriter(archivo));
                bw.write(respuesta);
                } else {
                    bw = new BufferedWriter(new FileWriter(archivo));
                    bw.write(respuesta);
                }
                bw.close();
       }catch(Exception e){}
   
   }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
