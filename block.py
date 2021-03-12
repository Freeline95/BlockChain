from hashCalculator import HashCalculator


class Block(object):

    def __init__(self, index, timestamp, proof, previous_hash, previous_block=None):
        self.index = index
        self.timestamp = timestamp
        self.proof = proof
        self.previous_hash = previous_hash
        self.previous_block = previous_block
        self.hash_calculator = HashCalculator

    def validate(self):
        if self.index == 1 and self.previous_hash != '0':
            raise Exception('First block must has zero previous hash \'' + self.previous_hash + '\' given')

        if self.index != 1:
            if self.previous_block is None:
                raise Exception('Block with index ' + str(self.index) + ' do not have previous block')

            if self.previous_block.get_block_hash() != self.previous_hash:
                raise Exception('Block with index ' + str(self.index) + ' has wrong previous hash')

            expression_for_hashing = str(self.proof ** 2 - self.previous_block.proof ** 2).encode()
            if self.hash_calculator.calculate_hash(expression_for_hashing)[:4] != '0000':
                raise Exception('Block with index ' + str(self.index) + ' has wrong proof hash')

    def get_block_hash(self):
        return self.hash_calculator.calculate_hash(str(self.serialize()).encode())

    def serialize(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'proof': self.proof,
            'previous_hash': self.previous_hash
        }
