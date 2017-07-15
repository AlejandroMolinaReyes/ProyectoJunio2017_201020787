/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package peticion;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;
import static consulta.WebServer.consultaPython;
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
     * @throws org.apache.commons.fileupload.FileUploadException
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response){
        response.setContentType("text/html;charset=UTF-8");
        
        File fichero = null;
        FileReader fr = null;
        BufferedReader br = null;
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            try{
                String path = "C:\\proyectoJspEDD\\web\\csv";
                String verificar = "";
                FileItemFactory factory = new DiskFileItemFactory();
                ServletFileUpload upload = new ServletFileUpload(factory);
                List items = upload.parseRequest(request);
                
                

                for (Object item : items) {
                    FileItem uploaded = (FileItem) item;
                    if (uploaded.isFormField()) {
                        if(uploaded.getFieldName().equals("gender")){
                            verificar = uploaded.getString();
                        }  
                    }else{
                        fichero = new File(path, uploaded.getName());
                        uploaded.write(fichero);
                    }
                }
                fr = new FileReader (fichero);
                br = new BufferedReader(fr);
                String linea;
                while((linea=br.readLine())!=null){
                    //System.out.println(linea);
                    String[]datos = linea.split(",");
                    if(datos[0]!=null){
                        String dato = datos[0].trim().toLowerCase();
                        switch(verificar){
                            case "usuario":
                                    if(!dato.equals("usuario")){
                                        if(datos[0]!=null&&datos[1]!=null&&datos[2]!=null){
                                            String user = datos[0].trim().toLowerCase();
                                            String pass = datos[1].trim().toLowerCase();
                                            String estado = datos[2].trim().toLowerCase();
                                            RequestBody formBody = new FormEncodingBuilder().add("user",user)
                                                                                            .add("pass",pass)
                                                                                            .add("estado",estado).build();
                                            String respuesta = consultaPython("cargarUsuario", formBody);
                                            //System.out.println(respuesta);
                                        }
                                    }
                                break;
                            case "juegos":
                                if(!dato.equals("usuario base")){
                                    if(datos[0]!=null&&datos[1]!=null&&datos[2]!=null&&datos[3]!=null&&datos[4]!=null&&datos[5]!=null&&datos[6]!=null){
                                        String user = datos[0].trim().toLowerCase();
                                        String oponente = datos[1].trim().toLowerCase();
                                        String tirosRealizados = datos[2].trim().toLowerCase();
                                        String tirosAcertados = datos[3].trim().toLowerCase();
                                        String tirosFallados = datos[4].trim().toLowerCase();
                                        String gano = datos[5].trim().toLowerCase();
                                        String daño = datos[6].trim().toLowerCase();
                                        RequestBody formBody = new FormEncodingBuilder().add("user",user)
                                                                                        .add("oponente",oponente)
                                                                                        .add("tirosR",tirosRealizados)
                                                                                        .add("tirosA",tirosAcertados)
                                                                                        .add("tirosF",tirosFallados)
                                                                                        .add("gano",gano)
                                                                                        .add("daño",daño).build();
                                        String respuesta = consultaPython("cargarJuegos", formBody);
                                        //System.out.println(respuesta);
                                    }
                                }
                                break;
                            case "juego":
                                if(!dato.equals("usuario1")){
                                    if(datos[0]!=null&&datos[1]!=null&&datos[2]!=null&&datos[3]!=null&&datos[4]!=null&&datos[5]!=null&&datos[6]!=null&&datos[7]!=null){
                                        String user1 = datos[0].trim().toLowerCase();
                                        String user2 = datos[1].trim().toLowerCase();
                                        String x = datos[2].trim().toLowerCase();
                                        String y = datos[3].trim().toLowerCase();
                                        String variante = datos[4].trim().toLowerCase();
                                        String tiempo = datos[5].trim().toLowerCase();
                                        String disparo = datos[6].trim().toLowerCase();
                                        String rafaga = datos[7].trim().toLowerCase();
                                        RequestBody formBody = new FormEncodingBuilder().add("user1",user1)
                                                                                        .add("user2",user2)
                                                                                        .add("x",x)
                                                                                        .add("y",y)
                                                                                        .add("variante",variante)
                                                                                        .add("tiempo",tiempo)
                                                                                        .add("disparo",disparo)
                                                                                        .add("rafaga",rafaga).build();
                                        String respuesta = consultaPython("JuegoActual", formBody);
                                        System.out.println(respuesta);
                                    }
                                }
                                break;
                            case "naves":
                                if(!dato.equals("jugador1")){
                                    if(datos[0]!=null&&datos[1]!=null&&datos[2]!=null&&datos[3]!=null&&datos[4]!=null&&datos[5]!=null){
                                        String user1 = datos[0].trim().toLowerCase();
                                        String columna = datos[1].trim().toLowerCase();
                                        String fila = datos[2].trim().toLowerCase();
                                        String nivel = datos[3].trim().toLowerCase();
                                        String modo= datos[4].trim().toLowerCase();
                                        String dirrecion = datos[5].trim().toLowerCase();
                                        RequestBody formBody = new FormEncodingBuilder().add("user1",user1)
                                                                                        .add("columna",columna)
                                                                                        .add("fila",fila)
                                                                                        .add("nivel",nivel)
                                                                                        .add("modo",modo)
                                                                                        .add("dirrecion",dirrecion).build();
                                        //String respuesta = consultaPython("naves", formBody);
                                        //System.out.println(respuesta);
                                        }
                                    }
                                break;
                        }
                    }         
                }
            }catch(Exception e){
            }finally{
                try{                    
                    if( null != fr ){   
                        fr.close();     
                    }                  
                }catch (IOException ex){}
                response.sendRedirect("CargarDatos.jsp");
            }
            
        }catch(Exception e2){}
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
