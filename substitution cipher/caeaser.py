def caeser_encrypt_decrypt(text,shift):
    result=""
    for ch in text:
        if ch.isalpha():
            base=ord('A') if ch.isupper() else ord('a')
            result+=chr(base+((ord(ch)-base+shift+26)%26))
        else:
            result+=ch
    return result


shift=3
text="Ramy"
ciphertext=caeser_encrypt_decrypt(text,shift)
print("ciphertext:",ciphertext)
plaintext=caeser_encrypt_decrypt(ciphertext,shift)

print("plaintext:",plaintext)
