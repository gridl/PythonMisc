#hashlib
import hashlib
md5 = hashlib.md5()
md5.update(b'Python rocks') # to use an md5 hash yoy have to pass it a byte string instead of a regular string
print(md5.digest())


#key derivation

import binascii
dk = hashlib.pbkdf2_hmac(hash_name='sha256', password=b'bad_password34', salt=b'bad_salt',iterations=100000)
print(dk)

# Encrypting a string

from Crypto.Cipher import DES
key = b'abcdefgh'
def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

des = DES.new(key, DES.MODE_ECB)
text = b'Python rocks!'
padded_text = pad(text)
