
package consulta;

/** @author alejandro */

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

public class WebServer {
    
     public static OkHttpClient webClient = new OkHttpClient();
     
     public static String consultaPython(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://localhost:9090/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(consulta.WebServer.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(consulta.WebServer.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
