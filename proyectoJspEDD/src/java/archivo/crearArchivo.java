/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package archivo;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

/**
 *
 * @author alejandro
 */
public class crearArchivo {
    
     public static void crearArchivo(String respuesta,String nombre){
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
    
}
