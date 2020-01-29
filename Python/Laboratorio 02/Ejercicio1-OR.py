from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64
# Datos necesarios
key = get_random_bytes(16) # Clave aleatoria de 128 bits
IV = get_random_bytes(16) # IV aleatorio de 128 bits para CBC
BLOCK_SIZE_AES = 8 # Bloque de 64 bits
data1 = "Hola amigos de la seguridad".encode("utf-8") # Datos a cifrar
data2 = "Hola amigas de la seguridad".encode("utf-8") # Datos a cifrar
print('Texto1: ',data1)
print('Texto2: ',data2)
# CIFRADO #######################################################################
# Creamos un mecanismo de cifrado DES en modo CBC con un vector de inicialización IV
cipher = AES.new(key, AES.MODE_CBC, IV)
# Ciframos, haciendo que la variable “data” sea múltiplo del tamaño de bloque
ciphertext1 = cipher.encrypt(pad(data1,BLOCK_SIZE_AES))
ciphertext2 = cipher.encrypt(pad(data2,BLOCK_SIZE_AES))
# Mostramos el cifrado por pantalla en modo binario y en modo base 64
print('Cifrado de Texto1: ',ciphertext1)
print('Cifrado de Texto2: ',ciphertext2)
encoded_ciphertext1 = base64.b64encode(ciphertext1)
encoded_ciphertext2 = base64.b64encode(ciphertext2)
print('b64 encode(text1): ',encoded_ciphertext1)
print('b64 encode(text2): ',encoded_ciphertext2)
# DESCIFRADO #######################################################################
# Creamos un mecanismo de (des)cifrado DES en modo CBC con un vector de
# inicialización IV para CBC
# Ambos, cifrado y descifrado, se crean de la misma forma
decipher_des = AES.new(key, AES.MODE_CBC, IV)
# Desciframos, eliminamos el padding, y recuperamos la cadena
new_data1 = unpad(decipher_des.decrypt(ciphertext1), BLOCK_SIZE_AES).decode("utf-8","ignore")
new_data2 = unpad(decipher_des.decrypt(ciphertext2), BLOCK_SIZE_AES).decode("utf-8","ignore")
# Imprimimos los datos descifrados
print('Data descifrada: ',new_data1)
print('Data descifrada: ',new_data2)