__author__ = 'balhau'

from M2Crypto import RSA



class KeyPair:

    def __init__(self):
        self.keyPair=None

    def generateRSAKeyPair(self,keyLength):
        self.keyPair=RSA.gen_key(keyLength,65537)

    def exportPrivateKey(self,fileName):
        self.keyPair.save_key_der(fileName+".der")

    def exportPublicKey(self,filename):
        self.keyPair.save_pub_key(filename+".pem")
