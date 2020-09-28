import hashlib

class SHA1:
    def __init__(self):
        self.hash = ""
        self.count = 0

    def encrypt(self, hash):
        self.hash = hash
        return hashlib.sha1(hash)

    def decrypt(self, hash):
        pass