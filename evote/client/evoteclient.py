from M2Crypto.PGP.RSA import RSA
from crypto.keypair import KeyPair

__author__ = 'balhau'
import requests
import json

#Client for the Evote services

class EvoteClient:

    def __init__(self,url):
        self.url=url

    def createUser(self,username,pubkeydata,email):
        req={'name':username,'pubkey':pubkeydata,'mail':email}
        r=requests.post(self.url+"/newuser",json.dumps(req))
        return r.text

    def registerPubKey(self,user,privKeySign,regKey):
        pk=KeyPair()
        pk.loadPrivateKey(privKeySign)
        pubKeyData=open(regKey,'r').read()
        b64sign=pk.signB64sha1(pubKeyData)
        req={'user':user,'key':pubKeyData,'signature':b64sign}
        r=requests.post(self.url+"/regkey",json.dumps(req))
        return r.text

    def registerSurvey(self,name,description):
        req={'surveyname':name,'description':description}
        r=requests.post(self.url+"/newsurvey",json.dumps(req))
        return r.text

    def listSurveys(self):
        r=requests.get(self.url+"/listsurveys")
        return r.text


pk=KeyPair()
pk.loadPrivateKey("/home/balhau/workspace/evote/evote/balhau_priv.der")
pk.loadPublicKey("/home/balhau/workspace/evote/evote/balhau_pub.pem")

