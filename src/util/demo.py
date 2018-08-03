from pycrypto import AESCipher

cipher = AESCipher('mysecretpassword')
encrypted = cipher.encrypt('password')
decrypted = cipher.decrypt(encrypted)
print(encrypted)
print(decrypted)