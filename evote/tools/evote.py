
__author__ = 'balhau'

import sys
import argparse


from ..crypto.keypair import KeyPair



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
        args = parser.parse_args()
        if args.generate :
            klen=1024
            name="key"
            if args.length:
                klen=args.length
            if args.output:
                name=args.output
            kp=KeyPair()
            kp.generateRSAKeyPair(int(klen))
            kp.exportPrivateKey(name+"_priv")
            kp.exportPublicKey(name+"_pub")
    except Exception as inst:
        usage()
        print inst.message
        sys.exit(2)


if __name__ == "__main__":
    main()