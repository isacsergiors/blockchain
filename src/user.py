import datetime as Date
import hashlib
import os
import json
import shutil
from random import randint


class User:

    @staticmethod
    def add(words=None):

        path = '../data/users/users.b'
        users = []

        if not words:
            words = str(randint(0, 9999)) + str(Date.datetime.now())

        h = hashlib.md5()
        h.update(str(words).encode())

        with open(path, 'r') as f:
            if f.read():
                with open(path, 'r') as f:
                    u=json.loads(f.read())
                    for i in range(len(u)):
                        users.append(u[i])

                    with open(path, 'w') as f:
                        users.append(({
                            'publicKey': h.hexdigest(),
                            'balance': '0',
                            'transitions_total': '0'
                            }))
                        f.write(json.dumps(users))
            else:
                users.append(({
                    'publicKey': h.hexdigest(),
                    'balance': '0',
                    'transitions_total': '0'
                    }))
                with open(path, 'w') as f:
                    f.write(json.dumps(users))