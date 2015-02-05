from crypto.keypair import KeyPair
from client.evoteclient import EvoteClient

__author__ = 'balhau'

import sys
import argparse


def generateKP(length,fileoutput):
    klen=1024
    name="key"
    if length:
        klen=length
    if fileoutput:
        name=fileoutput
    kp=KeyPair()
    kp.generateRSAKeyPair(int(klen))
    kp.exportPrivateKey(name+"_priv")
    kp.exportPublicKey(name+"_pub")

def registerUser(server,user,pubkey,mail):
    c=EvoteClient(server)
    f=file(pubkey,'r')
    pubkeydata=file.read(f)
    return c.createUser(user,pubkeydata,mail)



# Command tool to operate with the evote service as well as to manage the cryptographic tokens
def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-o',  '--output')
        parser.add_argument('-g',  '--generate')
        parser.add_argument('-l',  '--length')
        parser.add_argument('-Pk', '--pubkey')
        parser.add_argument('-pk', '--privkey')
        parser.add_argument('-s',  '--server')
        parser.add_argument('-m',  '--email')
        parser.add_argument('-u',  '--username')
        parser.add_argument('-v', dest='verbose', action='store_true')
        args = parser.parse_args()
        #generate a keypair
        if args.generate =='kpair' :
            generateKP(args.length,args.output)

        #Register user in evote service
        if args.generate =='user':
            server='http://127.0.0.1:5000'
            if args.server:
                server=args.server
            print registerUser(server,args.username,args.pubkey,args.email)


    except Exception as inst:
        print inst.message
        sys.exit(2)


if __name__ == "__main__":
    main()