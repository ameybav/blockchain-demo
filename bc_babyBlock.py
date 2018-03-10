from bc_blockStructure import *

# Generate genesis block
def firstBlock():
  return Block(0, date.datetime.now(), {
    "Million-Dollar-Number": 11,
    "transactions": None
  }, "0")