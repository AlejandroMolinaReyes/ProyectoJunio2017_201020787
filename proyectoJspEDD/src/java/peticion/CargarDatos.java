/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package peticion;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileItemFactory;
import org.apache.commons.fileupload.FileUploadException;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;


/**
 *
 * @author alejandro
 */
@WebServlet(name = "CargarDatos", urlPatterns = {"/CargarDatos"})
public class CargarDatos extends HttpServlet {

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
            throws ServletException, IOException, FileUploadException, Exception {
        response.setContentType("text/html;charset=UTF-8");
        
        File fichero = null;
        FileReader fr = null;
        BufferedReader br = null;
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            String path = "C:\\proyectoJspEDD\\web\\csv";
            FileItemFactory factory = new DiskFileItemFactory();
            ServletFileUpload upload = new ServletFileUpload(factory);
            List items = upload.parseRequest(request);
            

            for (Object item : items) {
                FileItem uploaded = (FileItem) item;

                if (!uploaded.isFormField()) {
                fichero = new File(path, uploaded.getName());
                uploaded.write(fichero);
                }
            }
            
            fr = new FileReader (fichero);
            br = new BufferedReader(fr);
            String linea;
            int bandera = 0;
            while((linea=br.readLine())!=null){
                System.out.println(linea);
                String[]datos = linea.split(",");
                if(datos[0].trim().toLowerCase().equals("usuario")&& datos[1].trim().toLowerCase().equals("contraseña")){
                   
                }else if(true){
                
                }
            
            }
            out.print("<META HTTP-EQUIV=\"REFRESH\" CONTENT=\"0.0001;URL=CargarDatos.jsp\">");
        }catch(Exception e){}finally{
            
            try{                    
                if( null != fr ){   
                    fr.close();     
                }                  
                }catch (Exception e2){ 
                    e2.printStackTrace();
                }finally{
                    fichero.delete();
                }
                
        }
        
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
        try {
            processRequest(request, response);
        } catch (Exception ex) {
            Logger.getLogger(CargarDatos.class.getName()).log(Level.SEVERE, null, ex);
        }
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
        try {
            processRequest(request, response);
        } catch (Exception ex) {
            Logger.getLogger(CargarDatos.class.getName()).log(Level.SEVERE, null, ex);
        }
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
