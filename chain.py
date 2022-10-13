import hashlib
from Block import Block


class Chain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.block = []
        self.pool = []
        self.create_origin_block()

    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode("utf-8"))
        return (
            block.hash.hexdigest() == hash.hexdigest()
            and int(hash.hexdigest(), 16) < 2 ** (256 - self.difficulty)
            and block.previous_hash == self.block[-1].hash
        )

    # Here we're adding the objectabove to the chain
    def add_to_chain(self, block):
        if self.proof_of_work(block):
            self.block.append(block)

    # Here we are going to add date into the pool
    def add_to_pool(self, data):
        self.pool.append(data)

    # Here we specify the data frame to the block
    def create_origin_block(self):
        h = hashlib.sha256()
        h.update("".encode("utf-8"))
        origin = Block("Origin", h)
        origin.mine(self.difficulty)
        self.block.append(origin)

    # Mining the data that is in the pool
    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.block[-1].hash)
            block.mine(self.difficulty)
            self.add_to_chain(block)
            print("\n\n ==============================================================")
            print("Hash: \t\t", block.hash.hexdigest())
            print("Previous Hash: \t\t", block.previous_hash.hexdigest())
            print("Nonce: \t\t", block.nonce)
            print("Data: \t\t", block.data )
            print("\n\n ==============================================================")

