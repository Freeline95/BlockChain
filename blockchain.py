import datetime
from block import Block
from hashCalculator import HashCalculator


class BlockChain(object):

    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
        self.hash_calculator = HashCalculator

    def create_block(self, proof, previous_hash, previous_block=None):
        block = Block(
            len(self.chain) + 1,
            datetime.datetime.now(),
            proof,
            previous_hash,
            previous_block
        )

        block.validate()
        self.chain.append(block)

        return block

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while True is True:
            new_hash = self.hash_calculator.calculate_hash(str(new_proof ** 2 - previous_proof ** 2).encode())
            if new_hash[:4] == '0000':
                return new_proof
            else:
                new_proof += 1

    def validate(self):
        for block in self.chain:
            block.validate()

        return True

    def serialize(self):
        serialized_content = []

        for block in self.chain:
            serialized_content.append(block.serialize())

        return serialized_content
