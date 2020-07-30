import base64
import hashlib
import os

from Crypto.Cipher import AES

"""
class Cipher:
    def __init__(self, key):
        i = os.urandom(1)[0] % 29
        self.key = base64.urlsafe_b64encode(hashlib.sha256(key).digest()[i:i + 3] * 8)
        print("Key: {}".format(self.key))
    def encrypt(self, raw):
        #raw = self._pad(raw)
        #print("Amount of padding: {}".format(len(raw)-len(flag)))
        cipher = AES.new(self.key, AES.MODE_ECB)
        return base64.urlsafe_b64encode(cipher.encrypt(raw))

    def _pad(self, s):
        return s.encode() + (AES.block_size - len(s) % AES.block_size) * (AES.block_size - len(s) % AES.block_size).to_bytes(1, 'big')
        """



alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
flag = "53rW_RiyUiwXq3PD7E4RHJuzjlHbw4YmG8wNRILXEQdBFiJZlpI2WjD_kNeQAUYG"
flag = base64.urlsafe_b64decode(flag)
for a in alphabet:
	for b in alphabet:
		for c in alphabet:
			for d in alphabet:
				key = a+b+c+d
				print("Trying key: {}".format(key))
				aes = AES.new(key*8,AES.MODE_ECB)
				m = aes.decrypt(flag)
				print("Current m: {}".format(m))
				if b"ctf{" in m:
					print("\nRight key found: {}".format(key)) # b7vZ
					print('Flag: {}\n'.format(m)) # ctf{AES_is_on1y_secure_if_prop3r1y_used}
					exit()
