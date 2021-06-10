import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        #This function creates new blocks and then adds to the existing chain
        """This method will contain two parameters proof, previous hash"""
        block = {
            'index': len(self.chain) + 1,
            'timestamp' : time(),
            'transactions': self.current_transactions,
            'proof': proof,
            previous_hash: previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions=[]
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        # Calls and returns the last block of the chain
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        #This function adds a new transaction to already existing transactions
        """This will create a new transaction which will be sent to the next block. 
        It will contain three variables including sender, recipient and amount
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(self, block):
        #Used for hashing a block
        """The follow code will create a SHA-256 block hash and also ensure that the dictionary is ordered"""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof(self, last_proof):
        """This method is where you the consensus algorithm is implemented.
        It takes two parameters including self and last_proof"""
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """This method validates the block"""
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexigest()
        return guess_hash[:4] == "0000"

blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal", '5 BTC')
blockchain.new_block(blockchain.proof, 12345)

t4 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
t5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
t6 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
blockchain.new_block(blockchain.proof, 6789)

print("Genesis block: ", blockchain.chain)