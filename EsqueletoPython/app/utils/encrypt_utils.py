from Crypto.Hash import SHA1

class Encryption():

    @staticmethod
    def encrypt_value(language):
        encryptSha = SHA1.new()
        encryptValue = ''
        for value in language:
            encryptSha.update(value.encode())
            encryptValue += encryptSha.hexdigest()
        
        return encryptValue