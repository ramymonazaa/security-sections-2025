import os 
def generate_key(length):
    return os.urandom(length)
def OTP_encrypt(plaintext):
    text_pytes=plaintext.encode('utf-8')
    key=generate_key(len(text_pytes))
    ciphertext=[p^k for p,k in zip(text_pytes,key)]
    return ciphertext,key
def OTP_decrypt(ciphertext,key):
    plaintext=[p^k for p,k in zip(ciphertext,key)]
    return bytes(plaintext).decode()
plaintext="hello everyone"
ciphertext,key=OTP_encrypt(plaintext)
print(ciphertext)
print(OTP_decrypt(ciphertext,key))