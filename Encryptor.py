
class Encryptor:
    def __init__(self):
        self.key = 84523

    def crypt(self, message):
        encrypted_message = ''
        for symbol in message:
            encrypted_message += chr(ord(symbol) ^ self.key)
        return encrypted_message
