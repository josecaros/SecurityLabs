package Laboratorio01;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;

public class Encriptacion {
	public static class Letras{
		public int repeticiones;
		public char caracter;
		
		public Letras(char a){
			caracter=a;
			repeticiones=0;
		}
	}
	
	public static void main(String[] args) {
		String cadena = "Puedo escribir los versos más tristes esta noche.\n" + 
				"Escribir, por ejemplo: “La noche está estrellada,\n" + 
				"y tiritan, azules, los astros, a lo lejos.”\n" + 
				"El viento de la noche gira en el cielo y canta.\n" + 
				"Puedo escribir los versos más tristes esta noche.\n" + 
				"Yo la quise, y a veces ella también me quiso.\n" + 
				"En las noches como ésta la tuve entre mis brazos.\n" + 
				"La besé tantas veces bajo el cielo infinito.\n" + 
				"Ella me quiso, a veces yo también la quería.\n" + 
				"Cómo no haber amado sus grandes ojos fijos.\n" + 
				"Puedo escribir los versos más tristes esta noche.\n" + 
				"Pensar que no la tengo. Sentir que la he perdido.\n" + 
				"Oir la noche inmensa, más inmensa sin ella.\n" + 
				"Y el verso cae al alma como al pasto el rocío.\n" + 
				"Qué importa que mi amor no pudiera guardarla.\n" + 
				"La noche está estrellada y ella no está conmigo.";
		char[] caracteres = cadena.toCharArray();
		String cadenaSusti ="";
		for(int i=0;i<caracteres.length;i++) {
			int iniOrder = (int) caracteres[i];
			int aux =iniOrder;
			if(iniOrder>=97 && iniOrder<=122) {
				iniOrder = (iniOrder-97)+65;
			}
			iniOrder = sustituir(iniOrder);	
			if(iniOrder>=65 && iniOrder<=90) {
				cadenaSusti=cadenaSusti+ (char)iniOrder;
			}			
		}
		//System.out.println(cadenaSusti);
		escribirArchivo(cadenaSusti,"/home/carlos/poema20_pre.txt");
		String lectura = leerArchivo("/home/carlos/poema20_pre.txt");
		frecuencias(lectura);
		UNICODE8(lectura);
		addWord(lectura);
		Kasiski(lectura);
	}
	
	public static int sustituir(int tilde) {
		//a
		if(tilde ==225 || tilde==193) 
			return 65;
		//e
		else if(tilde == 233 || tilde == 201)
			return 69;
		//i
		else if (tilde == 237 || tilde == 205 || tilde == 72 || tilde == 74)
			return 73;
		//o
		else if(tilde == 243 || tilde==211 )
			return 79;
		//u
		else if(tilde ==250 || tilde==218 || tilde ==85 || tilde==87)
			return 86;
		//ñ
		else if(tilde == 209 || tilde == 241 )
			return 78;
		//k
		else if(tilde == 75)
			return 76;
		//y
		else if(tilde ==89)
			return 90;
		else
			return tilde;
	}
	
	public static void escribirArchivo(String cadena, String path) {
		FileWriter fichero = null;
        PrintWriter pw = null;
        try
        {
            fichero = new FileWriter(path);
            pw = new PrintWriter(fichero);

            pw.println(cadena);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
           try {
           // Nuevamente aprovechamos el finally para 
           // asegurarnos que se cierra el fichero.
           if (null != fichero)
              fichero.close();
           } catch (Exception e2) {
              e2.printStackTrace();
           }
        }
	}
	
	public static String leerArchivo(String path) {
		  File archivo = null;
	      FileReader fr = null;
	      BufferedReader br = null;

	      try {
	         // Apertura del fichero y creacion de BufferedReader para poder
	         // hacer una lectura comoda (disponer del metodo readLine()).
	         archivo = new File (path);
	         fr = new FileReader (archivo);
	         br = new BufferedReader(fr);

	         // Lectura del fichero
	         String linea;
	         String lineaFinal="";
	         while((linea=br.readLine())!=null)
	            lineaFinal=lineaFinal+linea;
	         return lineaFinal;
	      }
	      catch(Exception e){
	         e.printStackTrace();
	         return null;
	      }finally{
	         // En el finally cerramos el fichero, para asegurarnos
	         // que se cierra tanto si todo va bien como si salta 
	         // una excepcion.
	         try{                    
	            if( null != fr ){   
	               fr.close();     
	            }                  
	         }catch (Exception e2){ 
	            e2.printStackTrace();
	         }
	      }
	}
	
	public static Letras[] ordenar(Letras[] arreglo) {
		for(int i = 0; i < arreglo.length - 1; i++)
        {
            for(int j = 0; j < arreglo.length - 1; j++)
            {
                if (arreglo[j].repeticiones < arreglo[j + 1].repeticiones)
                {
                    Letras tmp = arreglo[j+1];
                    arreglo[j+1] = arreglo[j];
                    arreglo[j] = tmp;
                }
            }
        }
		return arreglo;
	}
	
	public static void frecuencias(String cadena) {
		Letras[] abc = new Letras[26];
		for(int i=0;i<abc.length;i++) {
			abc[i]= new Letras((char)(i+65));
		}
		char[] caracteres = cadena.toCharArray();
		for(int i=0;i<caracteres.length;i++) {
			char unico = caracteres[i];
			int pos = ((int)unico)-65;
			abc[pos].repeticiones=abc[pos].repeticiones+1;
		}
		abc=ordenar(abc);
		for(int i=0;i<abc.length;i++) {
			System.out.println(abc[i].caracter+ " --> "+ abc[i].repeticiones);
		}
		
	}
	
	public static void UNICODE8(String cadena) {
		String resultado = "";
		char[] caracteres = cadena.toCharArray();
		for(int i =0;i<cadena.length();i++) {
			resultado=resultado+ (int)caracteres[i];
		}
		System.out.println(resultado);
	}
	
	public static void addWord(String cadena) {
		String resultado ="";
		char[] caracteres = cadena.toCharArray();
		int a=0;
		for(int i=0;i<cadena.length();i++) {
			resultado = resultado+ caracteres[i];
			a=a+1;
			if(a==20) {
				resultado=resultado+ "AQUI";
				a=0;
			}
		}
		int i =0;
		while(i<4) {
			if(resultado.length()%4!=0) {
				resultado=resultado+"X";
			}else {
				break;
			}
			i++;
		}
		System.out.println(resultado);
		System.out.println(resultado.length());
		
	}
	
	public static void Kasiski(String cadena) {
		char[] caracteres = cadena.toCharArray();
		String salida="inicio";
		int tri=1;
		char trigLetra='-';
		int distancia=0;
		for(int i=1; i<caracteres.length;i++) {
			if(caracteres[i-1]==caracteres[i]) {
				tri=tri+1;
			}
			else {
				tri=1;
			}
			distancia=distancia+1;
			if(tri==3) {
				trigLetra=caracteres[i];
				salida=salida+" "+ distancia+" "+trigLetra;
				distancia =0;
			}
		}
		System.out.println(salida);
	}

}
