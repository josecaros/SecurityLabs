from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
# Ver https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
# Ver https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html
def crear_ECCKey():
    key = ECC.generate(curve='P-256')
    return key
def guardar_ECCKey_Privada(fichero, key, password):
    f = open(fichero,'wt')
    f.write(key.export_key(format='PEM',passphrase=password,protection="scryptAndAES128-CBC"))
    f.close()
    
def cargar_ECCKey_Privada(fichero, password):
    keyCifra = open(fichero,'rt').read()
    key = ECC.import_key(keyCifra,passphrase=password)
    return key

def guardar_ECCKey_Publica(fichero, key):
    key_pub = key.public_key().export_key(format='PEM')
    file_out = open(fichero, "wt")
    file_out.write(key_pub)
    file_out.close()

def cargar_ECCKey_Publica(fichero):
    keyFile = open(fichero, "rt").read()
    key_pub = ECC.import_key(keyFile)
    return key_pub
# def cifrarECC_OAEP(cadena, key):
# El cifrado con ECC (ECIES) aun no está implementado
# Por lo tanto, no se puede implementar este método aun en la versión 3.9.0
# return cifrado
# def descifrarECC_OAEP(cifrado, key):
# El cifrado con ECC (ECIES) aun no está implementado
# Por lo tanto, no se puede implementar este método aun en la versión 3.9.0
# return cadena
def firmarECC_PSS(texto, key_private):
    h = SHA256.new(texto.encode("utf-8"))
    print(h.hexdigest())
    signature = DSS.new(key_private, 'fips-186-3').sign(h)
    return signature
# ...
# return 0
def comprobarECC_PSS(texto, firma, key_public):
    h= SHA256.new(texto.encode("utf-8"))
    verifier = DSS.new(key_public,'fips-186-3')
    try:
        verifier.verify(h, firma)
        print("Correcto")
        return True
    except (ValueError, TypeError):
        print("Incorrecto")
        return False

def saveData(fichero, data):
  file_out = open(fichero, "wb")
  file_out.write(data)
  file_out.close()
def loadData(fichero):
  data = open(fichero, "rb").read()
  return data

#key = crear_ECCKey()
#guardar_ECCKey_Publica("ECCPublic.pem", key)
#guardar_ECCKey_Privada("ECCPrivada.pem",key,"password")
clavPriv = cargar_ECCKey_Privada("ECCPrivada.pem","password")
clavPubli = cargar_ECCKey_Publica("ECCPublic.pem")
firma = firmarECC_PSS("Hola Amigos", clavPriv)
comprobarECC_PSS("Hola Amigos",firma,clavPubli)

