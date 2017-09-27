from Crypto.PublicKey import RSA
from Crypto import Random

class CryptoLines:

    def __init__(self):
        self.random_generator = Random.new().read
        self.key = RSA.generate(1024, self.random_generator)
        #generate pub and priv key
        self.publickey = self.key.publickey() # pub key export for exchange


    def encrypt(self,msg):
        # Function for encrypting a msg using RSA
        #  encrypted e_msg for msg

        #convert string into BytesString
        msg = msg.encode(encoding='utf-8')
        encrypted = self.publickey.encrypt(msg, 32)
        # message to encrypt is in the above line 'encrypt this message'
        # encrypted = encrypted[0]
        # encrypted.decode('utf-8')
        print("after encryption ")
        print(encrypted[0])
        # print(str(encrypted[0]))
        return encrypted[0]

    def decrypt(self,encrypted):
        decrypted = self.key.decrypt(encrypted)
        print(decrypted)
        decrypted = decrypted.decode('utf-8')
        print("decrypted msg")
        print(decrypted)
        return decrypted

def test():

    #var -> tuple of Key object and PublicKey object
    var = CryptoLines()
    emsg = var.encrypt("Amol")
    print(emsg)
    dmsg = var.decrypt(emsg)
    print(dmsg)
#test()

