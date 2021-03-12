import hashlib


class HashCalculator(object):

    @staticmethod
    def calculate_hash(data):
        return hashlib.sha256(data).hexdigest()
