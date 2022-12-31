import rsa

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(286)

# this is the string that we will be encrypting
#message = "hello geeks"
message = "\x03=\xfd\xb6>\xdc\xb4\xae\xca6~$\x1cQb\x9a\xb8e\x14\xcb2F\xa4OB\xdc\xc6\xc3\x9f\x07e\x0f\r\x1bW\xca"
# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(),
						publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)
