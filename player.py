import hashlib
import os


class Player:
    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.id = hashlib.sha256(os.urandom(50)).hexdigest()
        self.money = 0
        self.property = []
