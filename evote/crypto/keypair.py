from _sha512 import sha512
from apt_pkg import sha1sum

__author__ = 'balhau'

from M2Crypto import RSA, BIO
from Crypto.PublicKey import RSA as CRSA
from M2Crypto.RSA import RSA
import base64


class KeyPair:

    def __init__(self):
        self.keyPair=None
        self.pubkey=None
        self.privkey=None

    def generateRSAKeyPair(self,keyLength):
        self.keyPair=RSA.gen_key(keyLength,65537)

    def exportPrivateKey(self,fileName):
        self.keyPair.save_key_der(fileName+".der")

    def exportPublicKey(self,filename):
        self.keyPair.save_pub_key(filename+".pem")


    def loadPrivateKey(self,filename):
        data=open(filename,'r').read()
        self.privkey = CRSA.importKey(data)

    def signB64sha1(self,data):
        s1=sha1sum(data)
        signature=self.privkey.sign(s1,"sha1")
        return base64.b64encode(str(signature[0]))

    def verifyB4sha1(self,data,signature):
        sig=base64.b64decode(signature)
        sh1=sha1sum(str(data))
        return self.pubkey.verify(sh1,[long(sig)])

    def loadPublicKeyFromString(self,pkdata):
        self.pubkey=CRSA.importKey(pkdata)

    def loadPublicKey(self,filename):
        self.pubkey=CRSA.importKey(open(filename).read())
