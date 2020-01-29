package Laboratorio02;

public class ABECEDARIO {
	public int len = 27;
	char letras[];
	
	public ABECEDARIO() {
		letras=new char[len];
		int posicion=0;
		for(int i=0;i<len-1;i++) {
			if(i<14) {
				letras[i] = (char)(i+65);
			}else
				letras[i+1] = (char)(i+65);
		}
		letras[14] = (char)209;
	}
	
	public String toString() {
		String result="";
		for(int i=0;i<len;i++) {
			result = result + letras[i]+"("+i+")"+" ";
		}
		return result;
	}
	
	public char obtenerLetra(int letra) {
		if(letra==-1000) {
			return letras[letras.length-1];
		}
		return letras[letra];
	}
	public int obtenerPosicion(char caracter) {
		for(int i = 0;i<letras.length;i++) {
			if(letras[i]==caracter)
				return i;
		}
		return -1;
	}

}
