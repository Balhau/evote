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

    def registerPubKey(self,user,regKey,signature):
        req={'user':user,'key':regKey,'signature':signature}
        r=requests.post(self.url+"/regkey",json.dumps(req))
        return r.text
