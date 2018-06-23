import binascii, hashlib
input_str = str(input("Enter a password to hash: "))
ntlm_hash = binascii.hexlify(hashlib.new('md4', input_str.encode('utf-16le')).digest())
print(ntlm_hash)
