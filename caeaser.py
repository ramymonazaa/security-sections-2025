def caeser_encrypt(plain_text,shift):
    cipher_text=""
    for ch in plain_text:
        if ch.isalpha():
            base=ord('A') if ch.isupper() else ord('a')
            cipher_text+=chr(base+((ord(ch)-base+shift+26)%26))
        else:
            cipher_text+=ch
    return cipher_text

def caeser_decrypt(cipher_text,shift):
    plain_text=""
    for ch in cipher_text:
        if ch.isalpha():
            base=ord('A') if ch.isupper() else ord('a')
            plain_text+=chr(base+((ord(ch)-base-shift+26)%26))
        else:
            plain_text+=ch
    return plain_text

shift=3
text="Ramy"
ciphertext=caeser_encrypt(text,shift)
print("ciphertext:",ciphertext)
plaintext=caeser_decrypt(ciphertext,shift)
print("plaintext:",plaintext)