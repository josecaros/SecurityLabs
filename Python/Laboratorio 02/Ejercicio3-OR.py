from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class AES_CIPHER_CBC:
  BLOCK_SIZE_AES = 16
  

  def __init__(self, key):
    self.key = key
    pass

  def cifrar(self, cadena, IV ):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    cadena = cadena.encode('utf-8')
    result = cipher.encrypt(pad(cadena, AES_CIPHER_CBC.BLOCK_SIZE_AES))
    result = base64.b64encode(result)
    return result

  def descifrar(self, cifrado, IV):
    descipher = AES.new(key, AES.MODE_CBC, IV)
    cifrado_bytes = base64.b64decode(cifrado)
    result = unpad(descipher.decrypt(cifrado_bytes), AES_CIPHER_CBC.BLOCK_SIZE_AES)
    result = result.decode('utf-8','ignore')
    return result

key = get_random_bytes(16) # Clave aleatoria de 128 bits
IV = get_random_bytes(16) # IV aleatorio de 128 bits
datos = "Hola Mundo con AES en modo CBC"
d = AES_CIPHER_CBC(key)
cifrado = d.cifrar(datos, IV)
print(cifrado)
descifrado = d.descifrar(cifrado, IV)
print(descifrado)