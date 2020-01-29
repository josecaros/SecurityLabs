
def cifradoCesarMayus(cadena):
  resultado = ''
  i = 0
  while i < len(cadena):
    ordenClaro = ord(cadena[i])
    ordenCifrado = 0
    if(ordenClaro >= 65 and ordenClaro <= 90):
      ordenCifrado = (((ordenClaro-65)+3) % 26)+65
    resultado = resultado+chr(ordenCifrado)
    i = i+1
  return resultado

def descifradoCesarMayus(cadena):
  resultado=''
  i=0
  while i<len(cadena):
    ordenNormal = ord(cadena[i])
    ordenAlterado = 0
    if(ordenNormal>=65 and ordenNormal<=90):
      ordenAlterado=(((ordenNormal-65)-3)%26)+65
    resultado = resultado+chr(ordenAlterado)
    i=i+1
  return resultado

def cifradoCesarMayusAndMinus(cadena):
  resultado = ''
  i = 0
  while i < len(cadena):
    ordenClaro = ord(cadena[i])
    ordenCifrado = 0
    if(ordenClaro >= 65 and ordenClaro <= 90):
      ordenCifrado = (((ordenClaro-65)+3) % 26)+65
    if(ordenClaro>=97 and ordenClaro<=122):
      ordenCifrado = (((ordenClaro-97)+3) % 26)+97
    resultado = resultado+chr(ordenCifrado)
    i = i+1
  return resultado

def descifradoCesarMayusAndMinus(cadena):
  resultado=''
  i=0
  while i<len(cadena):
    ordenNormal = ord(cadena[i])
    ordenAlterado = 0
    if(ordenNormal >= 65 and ordenNormal <= 90):
      ordenAlterado = (((ordenNormal-65)-3) % 26)+65
    if(ordenNormal>=97 and ordenNormal<=122):
      ordenAlterado = (((ordenNormal-97)-3) % 26)+97
    resultado = resultado+chr(ordenAlterado)
    i=i+1
  return resultado

def cifradoCesar(cadena, M):
  resultado = ''
  i = 0
  while i < len(cadena):
    ordenClaro = ord(cadena[i])
    ordenCifrado = 0
    if(ordenClaro >= 65 and ordenClaro <= 90):
      ordenCifrado = (((ordenClaro-65)+M) % 26)+65
    if(ordenClaro>=97 and ordenClaro<=122):
      ordenCifrado = (((ordenClaro-97)+M) % 26)+97
    resultado = resultado+chr(ordenCifrado)
    i = i+1
  return resultado

def descifradoCesar(cadena,M):
  resultado=''
  i=0
  while i<len(cadena):
    ordenNormal = ord(cadena[i])
    ordenAlterado = 0
    if(ordenNormal >= 65 and ordenNormal <= 90):
      ordenAlterado = (((ordenNormal-65)-M) % 26)+65
    if(ordenNormal>=97 and ordenNormal<=122):
      ordenAlterado = (((ordenNormal-97)-M) % 26)+97
    resultado = resultado+chr(ordenAlterado)
    i=i+1
  return resultado


cadena = input("Cadena para Cifrar:")
print(cadena)
cifrado = cifradoCesar(cadena,9)
print('Cifrado Cesar(9): '+cifrado)
print('Descifrado Cesar(9): '+ descifradoCesar(cifrado,9))

