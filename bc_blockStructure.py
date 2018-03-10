import datetime as date
import hashlib as hasher

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    temp_str=str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
    temp_str=temp_str.encode('utf-8')
    sha.update(temp_str)
    return sha.hexdigest()