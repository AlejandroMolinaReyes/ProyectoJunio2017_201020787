/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package consulta;

/**
 *
 * @author alejandro
 */
public class graphviz {
    
    public static  void graficar(String nombre){
        try {
      
            String dotPath = "C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe";
      
            String fileInputPath = "C:\\proyectoJspEDD\\web\\graficar\\"+nombre+".txt";
            String fileOutputPath = "C:\\proyectoJspEDD\\web\\img\\"+nombre+".jpg";

            String tParam = "-Tjpg";
            String tOParam = "-o";

            String[] cmd = new String[5];
            cmd[0] = dotPath;
            cmd[1] = tParam;
            cmd[2] = fileInputPath;
            cmd[3] = tOParam;
            cmd[4] = fileOutputPath;

            Runtime rt = Runtime.getRuntime();

            rt.exec( cmd );

        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
        }
    }
    
}
