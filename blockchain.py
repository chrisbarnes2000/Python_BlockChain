class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        #This function creates new blocks and then adds to the existing chain
        pass


    def new_transaction(self):
        #This function adds a new transaction to already existing transactions
        pass


    @staticmethod
    def hash(block):
        #Used for hashing a block
        pass

    @property
    def last_block(self):
        # Calls and returns the last block of the chain
        pass