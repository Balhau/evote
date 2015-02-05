from crypto.keypair import KeyPair

__author__ = 'balhau'


kp=KeyPair()


kp.generateRSAKeyPair(1024)


kp.exportPrivateKey("priv")
kp.exportPublicKey("pub")
