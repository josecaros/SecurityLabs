package Laboratorio02;

import java.util.Scanner;

import javax.swing.text.html.HTMLDocument.HTMLReader.PreAction;

public class Vignere {
	public ABECEDARIO abc;
	
	public Vignere() {
		abc = new ABECEDARIO();
	}
	
	public static void main(String []arg) {
		Vignere cifrado = new Vignere();
		System.out.println(cifrado.abc);
		Scanner sc = new Scanner(System.in);
		System.out.println("Ingrese (1) si desea cifrar o (2) si desea descifrar");
		int option = Integer.parseInt(sc.nextLine());
		System.out.println("Ingrese el texto a procesar: ");
		String texto = sc.nextLine();
		
		System.out.println("Ingrese la clave: ");
		String clave = sc.nextLine();
		texto= cifrado.preProcesar(texto);
		clave = cifrado.preProcesar(clave);
		if(option == 1) {
			System.out.println("Cifrado: "+cifrado.cifrar(texto, clave));
		}else if(option == 2) {
			System.out.println("Cifrado: "+cifrado.descifrar(texto, clave));
		}else {
			System.out.println("Opcion Incorrecta");
		}
	}
	
	public String preProcesar(String text) {
		char[] caracteres = text.toCharArray();
		String cadenaSusti ="";
		for(int i=0;i<caracteres.length;i++) {
			int iniOrder = (int) caracteres[i];
			
			if(iniOrder>=97 && iniOrder<=122) {
				iniOrder = (iniOrder-97)+65;
			}
			iniOrder = sustituir(iniOrder);	
			if((iniOrder>=65 && iniOrder<=90)|| iniOrder==209) {
				cadenaSusti=cadenaSusti+ (char)iniOrder;
			}			
		}
		return cadenaSusti;
	}
	
	public int sustituir(int tilde) {
		//a
		if(tilde ==225 || tilde==193) 
			return 65;
		//e
		else if(tilde == 233 || tilde == 201)
			return 69;
		//i
		else if (tilde == 237 || tilde == 205)
			return 73;
		//o
		else if(tilde == 243 || tilde==211 )
			return 79;
		//u
		else if(tilde ==250 || tilde==218)
			return 85;
		//ñ
		else if(tilde == 241 || tilde == 209 )
			return 209;
		else
			return tilde;
	}
	
	public String cifrar(String texto, String clave) {
		char[] arrTexto = texto.toCharArray();
		char[] arrClave = clave.toCharArray();
		String resultado = "";
		int index = 0;
		while(index< arrTexto.length) {
			int lugarInicial = abc.obtenerPosicion( arrTexto[index]);
			int recorrido =abc.obtenerPosicion(arrClave[index % clave.length()]);
			resultado=  resultado+abc.obtenerLetra((lugarInicial+recorrido)%27);
			index++;
		}
		
		return resultado;
	}
	
	public String descifrar(String texto, String clave) {
		char[] arrTexto = texto.toCharArray();
		char[] arrClave = clave.toCharArray();
		String resultado = "";
		int index = 0;
		while(index< arrTexto.length) {
			int lugarInicial = abc.obtenerPosicion( arrTexto[index]);
			int recorrido =abc.obtenerPosicion(arrClave[index % clave.length()]);
			int fin = (lugarInicial-recorrido)%27;
			if(fin<0)
				fin = 27-fin*(-1);
			resultado=  resultado+abc.obtenerLetra(fin);
			index++;
		}
		
		return resultado;
	}

}
