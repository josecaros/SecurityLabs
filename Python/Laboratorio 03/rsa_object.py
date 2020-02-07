from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pss
class RSA_OBJECT:
  def __init__(self):
    self.key = None
    self.private_key=None
    self.public_key = None

  def create_KeyPair(self):
    self.key = RSA.generate(2048)
    self.private_key = self.key
    self.public_key = self.key.publickey()

  def save_PrivateKey(self, file, password):
    key_cifrada = self.private_key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
    file_out = open(file, "wb")
    file_out.write(key_cifrada)
    file_out.close()

  def load_PrivateKey(self, file, password):
    key_cifrada = open(file, "rb").read()
    self.private_key = RSA.import_key(key_cifrada, passphrase=password)

  def save_PublicKey(self, file):
    key_cifrada = self.public_key.export_key()
    file_out = open(file, "wb")
    file_out.write(key_cifrada)
    file_out.close()

  def load_PublicKey(self, file):
    keyFile = open(file, "rb").read()
    self.public_key = RSA.import_key(keyFile)

  def cifrar(self, datos):
    #data = datos.encode("utf-8")
    engineRSACipher = PKCS1_OAEP.new(self.public_key)
    cifrado = engineRSACipher.encrypt(datos)
    return cifrado
    #Cifra el parámetro datos (de tipo binario) con la clave self.public_key, y devuelve
    #el resultado. En caso de error, se devuelve None
  def descifrar(self, cifrado):
    engineRSACipher = PKCS1_OAEP.new(self.private_key)
    datos = engineRSACipher.decrypt(cifrado)
    #datos = datos.decode('utf-8')
    return datos
    # Descrifra el parámetro cifrado (de tipo binario) con la clave self.private_key, y
    # Devuelve el resultado (de tipo binario). En caso de error, se devuelve None"""
  def firmar(self, datos):
    h= SHA256.new(datos)
    print(h.hexdigest())
    signature = pss.new(self.private_key).sign(h)
    return signature
    # Firma el parámetro datos (de tipo binario) con la clave self.private_key, y devuelve
    # el resultado. En caso de error, se devuelve None."""
  def comprobar(self, text, signature):
    h = SHA256.new(text)
    print(h.hexdigest())
    verificador = pss.new(self.public_key)
    try:
      verificador.verify(h,signature)
      return True
    except(ValueError, TypeError):
      return False

    # Comprueba el parámetro text (de tipo binario) con respecto a una firma signature
    # (de tipo binario), usando para ello la clave self.public_key.
    # Devuelve True si la comprobacion es correcta, o False en caso contrario o
    # en caso de error.

# y guardar en ficheros la clave privada (protegida) y publica
password = "password"
private_file = "rsa_key.pem"
public_file = "rsa_key.pub"
RSA_key_creator = RSA_OBJECT()
RSA_key_creator.create_KeyPair()
RSA_key_creator.save_PrivateKey(private_file, password)
RSA_key_creator.save_PublicKey(public_file)
# Crea dos clases, una con la clave privada y otra con la clave publica
RSA_private = RSA_OBJECT()
RSA_public = RSA_OBJECT()
RSA_private.load_PrivateKey(private_file, password)
RSA_public.load_PublicKey(public_file)
# Cifrar y Descifrar con PKCS1 OAEP
cadena = "Lo desconocido es lo contrario de lo conocido. Pasalo."
cifrado = RSA_public.cifrar(cadena.encode("utf-8"))
print(cifrado)
descifrado = RSA_private.descifrar(cifrado).decode("utf-8")
print(descifrado)
# Firmar y comprobar con PKCS PSS
firma = RSA_private.firmar(cadena.encode("utf-8"))
if RSA_public.comprobar(cadena.encode("utf-8"), firma):
  print("La firma es valida")
else:
  print("La firma es invalida")