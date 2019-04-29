from transaction import Transaction
from user import User
import sys
import hashlib
import json

block = Transaction()


def Main():
    User.add('Hello')
    # block.add(sys.argv[1], getWallet(), sys.argv[2])

def getWallet():

    with open('../wallet/keys.b', 'r') as f:
        if f.read():
            with open('../wallet/keys.b', 'r') as f:
                wallet = json.loads(f.read())
                return wallet['publicKey']
        else:
            return False


if __name__ == "__main__":
    Main()
