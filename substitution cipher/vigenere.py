def vig_encrypt(plain_text,key):
    cipher_text=""
    for i,ch in enumerate(plain_text):
        if ch.isalpha():
            key_ind=(i%len(key))
            baseK=ord('A') if key[key_ind].isupper() else ord('a')
            shift_val=ord(key[key_ind])-baseK
            base=ord('A') if ch.isupper() else ord('a')
            cipher_text+=chr(base+((ord(ch)-base+shift_val+26)%26))
        else:
            cipher_text+=ch
    return cipher_text

def vig_decrypt(cipher_text,key):
    plain_text=""
    for i,ch in enumerate(cipher_text):
        if ch.isalpha():
            key_ind=(i%len(key))
            baseK=ord('A') if key[key_ind].isupper() else ord('a')
            shift_val=ord(key[key_ind])-baseK
            base=ord('A') if ch.isupper() else ord('a')
            plain_text+=chr(base+((ord(ch)-base-shift_val+26)%26))
        else:
            plain_text+=ch
    return plain_text

key="ali"
text="Ramy & ,"
ciphertext=vig_encrypt(text,key)
print("ciphertext:",ciphertext)
plaintext=vig_decrypt(ciphertext,key)
print("plaintext:",plaintext)