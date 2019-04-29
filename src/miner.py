import datetime as Date
import hashlib
import os
import json
import shutil
from random import randint


class Miner:

    PATH_BLOCK = '../data/blocks/'
    PATH_DATA = '../data/'

    transitions = []
    index = 0
    
    def __init__(self):
        self.index = self.getBlockIndex() + 1

    def setBlockNewIndex(self):

      with open(self.PATH_DATA+'config.b', 'r') as f:
         config = json.loads(f.read())
         config[0].update({'blockNo': str(int(self.index))})
         h = hashlib.md5()
         h.update(str(config[0]).encode('utf-8'))
         config[1].update({'hash': h.hexdigest()})

         print(config)

      with open(self.PATH_DATA+'config.b', 'w') as f:
         f.write(json.dumps(config))

    def getBlockIndex(self):

      if self.isChainConfigValid():

         with open(self.PATH_DATA+'config.b', 'r') as f:
            config = json.loads(f.read())

            return int(config[0]['blockNo'])
      else:
         return False


    def isChainConfigValid(self):
      with open(self.PATH_DATA+'config.b', 'r') as f:

         config = json.loads(f.read())

         h = hashlib.md5()
         h.update(str(config[0]).encode('utf-8'))

         if h.hexdigest() == config[1]['hash']:
            return True
         else:
            return False
