import datetime as Date
import hashlib
import os
import json
import shutil
from random import randint


class Transaction:

   PATH_BLOCK = '../data/blocks/'

   blocks = []

   data = None
   timestamp = None
   from_user = None
   received = None

   def add(self, data, _from , _wallet):

      if not _from or not _wallet or not data:
         exit()

      try:
         data = float(data)
      except(ValueError):
         exit()
         
      if type(data) == int or type(data) == float:
         self.data = str(data)
      else:
         exit()
      
      self.timestamp = str(Date.datetime.now())
      self.received = str(_wallet)
      self.from_user = str(_from)

      self.blocks.append({
         "from": self.from_user,
         "received": self.received,
         "data": self.data,
         "timestamp": self.timestamp,
      })

      self.setTemp()
         

   def getLastBlock(self):
      if self.blocks and len(self.blocks) > 0:
         return self.blocks[-1]
      else:
         return []

   def setTemp(self):

      with open(self.PATH_BLOCK+'temp.b', 'r') as f:
         if f.read():
            f = open(self.PATH_BLOCK+'temp.b', 'r')
            b = json.loads(f.read())
            f.close()
            for i in range(len(b)):
               self.blocks.append(b[i])
            self.setTempFile()
         else:
            self.setTempFile()

   def setTempFile(self):
      with open(self.PATH_BLOCK+'temp.b', 'w') as f:
         f.write(json.dumps(self.blocks))
