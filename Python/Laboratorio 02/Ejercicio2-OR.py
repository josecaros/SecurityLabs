from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64
import json
def crypAESmodeECB(data1):
  key = get_random_bytes(16) # Clave aleatoria de 128 bits
  BLOCK_SIZE_AES = 8 # Bloque de 64 bits
  print('Texto1: ',data1)
  # CIFRADO ########################################################################
  #  # Creamos un mecanismo de cifrado AES en modo ECB con un vector de inicialización IV
  cipher = AES.new(key, AES.MODE_ECB)
  # Ciframos, haciendo que la variable “data” sea múltiplo del tamaño de bloque
  ciphertext1 = cipher.encrypt(pad(data1,BLOCK_SIZE_AES))
  # Mostramos el cifrado por pantalla en modo binario y en modo base 64
  print('Cifrado de Texto1: ',ciphertext1)
  encoded_ciphertext1 = base64.b64encode(ciphertext1)
  print('b64 encode(text1): ',encoded_ciphertext1)
  # DESCIFRADO #######################################################################
  # Creamos un mecanismo de (des)cifrado DES en modo CBC con un vector de
  # inicialización IV para CBC
  # Ambos, cifrado y descifrado, se crean de la misma forma
  decipher_aes = AES.new(key, AES.MODE_ECB)
  # Desciframos, eliminamos el padding, y recuperamos la cadena
  new_data1 = unpad(decipher_aes.decrypt(ciphertext1), BLOCK_SIZE_AES).decode("utf-8","ignore")
  # Imprimimos los datos descifrados
  print('Data descifrada: ',new_data1)

def crypAESmodeCTR(data1):
  key = get_random_bytes(16)
  nonce_bytes = get_random_bytes(8)
  print('Texto: ',data1)

  cipher = AES.new(key, AES.MODE_CTR, nonce=nonce_bytes)
  cipherText_bytes = cipher.encrypt(data1)
  print('Cifrado de Texto (bytes): ',cipherText_bytes)
  cipherText = base64.b64encode(cipherText_bytes).decode('utf-8')
  nonce= base64.b64encode(nonce_bytes).decode('utf-8')
  print('nonce: ',nonce)
  print('Texto Cifrado: ', cipherText)

  ##Decipher
  
  decipher_des = AES.new(key, AES.MODE_CTR, nonce=nonce_bytes)
  decipherText = decipher_des.decrypt(cipherText_bytes)

  print('Mensaje Descifrado: ',decipherText)

def crypAESmodeOFB(data1):
  key = get_random_bytes(16)
  IV = get_random_bytes(16)
  print('Texto: ',data1)

  ##Cifrado
  cipher= AES.new(key, AES.MODE_OFB, iv=IV)
  cipherText_bytes = cipher.encrypt(data1)
  print("Texto cifrado (bytes): ",cipherText_bytes)
  cipherText = base64.b64encode(cipherText_bytes).decode('utf-8')
  print("Texto cifrado: ", cipherText)

  print("Clave IV: ", base64.b64encode(IV).decode('utf-8'))
  decipher_des = AES.new(key, AES.MODE_OFB, iv=IV)
  decipherText = decipher_des.decrypt(cipherText_bytes)

  print("Texto descifrado: ", decipherText)

def crypAESmodeCFB(data1):
  key = get_random_bytes(16)
  IV = get_random_bytes(16)
  print('Texto: ',data1)

  ##Cifrado
  cipher= AES.new(key, AES.MODE_CFB, iv=IV)
  cipherText_bytes = cipher.encrypt(data1)
  print("Texto cifrado (bytes): ",cipherText_bytes)
  cipherText = base64.b64encode(cipherText_bytes).decode('utf-8')
  print("Texto cifrado: ", cipherText)

  print("Clave IV: ", base64.b64encode(IV).decode('utf-8'))
  decipher_des = AES.new(key, AES.MODE_CFB, iv=IV)
  decipherText = decipher_des.decrypt(cipherText_bytes)

  print("Texto descifrado: ", decipherText)

def crypAESmodeGCM(header, data1):
  key = get_random_bytes(16)
  nonce = get_random_bytes(16)
  mac_len = 8
  header=header.encode('utf-8')
  print('Texto: ',data1)

  ##Cifrado
  cipher= AES.new(key, AES.MODE_GCM, nonce=nonce, mac_len=mac_len)
  cipher.update(header)
  cipherText_bytes, tag = cipher.encrypt_and_digest(data1)

  print("Texto cifrado (bytes): ",cipherText_bytes)
  cipherText = base64.b64encode(cipherText_bytes).decode('utf-8')
  print("Texto cifrado: ", cipherText)

  print("nonce: ", base64.b64encode(nonce).decode('utf-8'))
  decipher_des = AES.new(key, AES.MODE_GCM, nonce=nonce, mac_len=mac_len)
  decipher_des.update(header)
  decipherText = decipher_des.decrypt_and_verify(cipherText_bytes,tag)

  print("Texto descifrado: ", decipherText)

  
    

data1 = "Hola amigos de la seguridad".encode("utf-8") # Datos a cifrar
crypAESmodeECB(data1)
#crypAESmodeGCM("key", data1)