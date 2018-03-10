from bc_babyBlock import *
from flask import Flask
from flask import request
import json

node = Flask(__name__)
#node.register_blueprint(comeOver)

#miner Addresses
potentialMiners = ["ramharivitthala",
                      "shamharivitthala",
                      "sitaharivitthala",
                      "lakhsmanharivitthala",
                      "vitthalavitthalavitthala",
                      "tukaramharivitthala",
                      "gyandevharivitthala",
                      "jaishivajijaibhawani",
                      "bharatmatakijai",
                      "jaimaharashtra",
                      "jaijavanjaikisan",
                      "tummujhekhoondomaitumheazadidonga"]

blockchain = []
blockchain.append(firstBlock())

currentTransaction = []

#data to create a chain
peer_nodes = []

mining = True

@node.route('/comeOver', methods=['POST'])
def transaction():
  
  newBlock = request.get_json()
  currentTransaction.append(newBlock)
  print ("New transaction")
  print ("FROM: {}".format(newBlock['from'].encode('ascii','replace')))
  print ("TO: {}".format(newBlock['to'].encode('ascii','replace')))
  print ("AMOUNT: {}\n".format(newBlock['amount']))
  return "Transaction submission successful\n"

@node.route('/blocks', methods=['GET'])
def get_blocks():
  displayBlocks = blockchain
  
  for i in range(len(displayBlocks)):
    block = displayBlocks[i]
    block_index = str(block.index)
    block_timestamp = str(block.timestamp)
    block_data = str(block.data)
    block_hash = block.hash
    displayBlocks[i] = {
      "index": block_index,
      "timestamp": block_timestamp,
      "data": block_data,
      "hash": block_hash
    }
  displayBlocks = json.dumps(displayBlocks,indent=3)
  return displayBlocks

def newChains():
  
  other_chains = []
  for node_url in peer_nodes:
    block = requests.get(node_url + "/blocks").content
    block = json.loads(block)
    other_chains.append(block)
  return other_chains

def consensus():
  other_chains = newChains()
 
  longestChain = blockchain
  for chain in other_chains:
    if len(longestChain) < len(chain):
      longestChain = chain
 
  blockchain = longestChain

def nightWatch(last_proof):
  incrementor = last_proof + 1
 
  while not (incrementor % 9 == 0 and incrementor % last_proof == 0 and incrementor % 18 == 0):
    incrementor += 1
  return incrementor

@node.route('/mine', methods = ['GET'])
def mine():
  
  last_block = blockchain[len(blockchain) - 1]
  last_proof = last_block.data['Million-Dollar-Number']
  
  proof = nightWatch(last_proof)
  
  print("Enter the details of the amount to be send")
  amountToBeSend = input()
  print("Enter the sender's address")
  fromAddress = input()
  if fromAddress not in potentialMiners:
    print("Enter the address of the registered miner")
    exit()
  print("Enter the reciever's address")
  toAddress = input()
  if toAddress not in potentialMiners:
    print("Enter the address of the registered miner")
    exit()
  currentTransaction.append(
    { "from": fromAddress, "to": toAddress, "amount": amountToBeSend }
  )
  
  new_block_data = {
    "Million-Dollar-Number": proof,
    "transactions": list(currentTransaction)
  }
  new_block_index = last_block.index + 1
  new_block_timestamp = this_timestamp = date.datetime.now()
  last_block_hash = last_block.hash
  
  currentTransaction[:] = []
  
  mined_block = Block(
    new_block_index,
    new_block_timestamp,
    new_block_data,
    last_block_hash
  )
  blockchain.append(mined_block)
  
  return json.dumps({
      "index": new_block_index,
      "timestamp": str(new_block_timestamp),
      "data": new_block_data,
      "hash": last_block_hash
  }) + "\n" +"\n"

node.run()