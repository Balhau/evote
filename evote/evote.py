__author__ = 'balhau'

import sys, argparse
from evote.crypto.KeyPair import KeyPair

def usage():
    out='''evote <opts> <args>
            -o : output file
            -g : generate key
            -l : key size
        '''
    print out

# Command tool to operate with the evote service as well as to manage the cryptographic tokens
def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--output')
        parser.add_argument('-g', '--generate')
        parser.add_argument('-l', '--length')
        parser.add_argument('-v', dest='verbose', action='store_true')
        if parser.generate :
            klen=1024
            name="key"
            if parser.length:
                klen=parser.length
            if parser.output:
                name=parser.output
            kp=KeyPair()
            kp.generateRSAKeyPair(klen)
            kp.exportPrivateKey(name+"_priv")
            kp.exportPublicKey(name+"_pub")
    except:
        usage()
        sys.exit(2)


if __name__ == "__main__":
    main()