from evote.crypto import KeyPair

__author__ = 'balhau'

kp=KeyPair.KeyPair()

kp.generateRSAKeyPair(1024)


kp.exportPrivateKey("priv")
kp.exportPublicKey("pub")
