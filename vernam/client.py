import random
 
def encrypt(text, key):
    ciphertext = []
 
    x = []
    for i in range(len(text)):
        x.append(ord(text[i]))
 
    for i in range(len(text)):
        ciphertext.append(x[i]^key[i])
 
    return ciphertext
 
def gen_key(length):
 
    key= [ ]
 
    for i in range(length):
        key.append(random.randint(0,127))
 
    return key
 
 
def decrypt(cipher,key):
 
    x = []
    for i in range(len(cipher)):
        x.append(cipher[i]^key[i])
 
    text = ''
    for i in x:
        text = text + chr(i)
 
    return text
 
 
 
text = raw_input()
key = gen_key(len(text))
crypt = encrypt(text, key)
print decrypt(crypt,key)