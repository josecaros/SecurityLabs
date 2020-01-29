def cifradoMonoAlbabetico(cadena, clave):
  resultado=''
  i=0
  while i<len(cadena):
    inicial=ord(cadena[i])
    final=0
    mov = ord(clave[i % len(clave)])
    if(mov >= 65 and mov <= 90):
      mov = (mov-64)%26
    if(mov >= 97 and mov <= 122):
      mov = (mov-96)%26
    if(inicial >= 65 and inicial <= 90):
      final = (((inicial-65)+mov) %26)+65
    if(inicial >= 97 and inicial <= 122):
      final = (((inicial-97)+mov) %26)+97
    resultado = resultado+chr(final)
    i=i+1
  return resultado

def descifradoMonoAlfabetico(cadena, clave):
  resultado=''
  i=0
  while i<len(cadena):
    inicial=ord(cadena[i])
    final=0
    mov = ord(clave[i % len(clave)])
    if(mov >= 65 and mov <= 90):
      mov = (mov-64)%26
    if(mov >= 97 and mov <= 122):
      mov = (mov-96)%26
    if(inicial >= 65 and inicial <= 90):
      final = (((inicial-65)-mov) %26)+65
    if(inicial >= 97 and inicial <= 122):
      final = (((inicial-97)-mov) %26)+97
    resultado = resultado+chr(final)
    i=i+1
  return resultado


cadena = input('Ingrese cadena a cifrar: ')
clave = input('Ingrese Palabra clave: ')
cifrado = cifradoMonoAlbabetico(cadena, clave)
print('Cadena Cifrada: '+cifrado)
print('Cadena descifrada: ',descifradoMonoAlfabetico(cifrado,clave))