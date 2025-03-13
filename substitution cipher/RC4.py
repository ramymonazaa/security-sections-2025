def RC4(text,key):
    #KSA
    S=list(range(256))
    T=[]
    for i in range(256):
        T.append(key[i%len(key)])
    for i in range(256):
        j=(i+S[i]+T[i])%256
        S[i],S[j]=S[j],S[i]

    #PCGA
    keystream=[]
    j=i=0
    for _ in range(len(text)):
        i=(i+1)%256
        j=(S[i]+j)%256
        S[i],S[j]=S[j],S[i]
        keystream.append((S[i]+S[j])%256)
    result=[i^j for i,j in zip(text,keystream)]
    return bytes(result)

text="Ramy Monazaa TA"
key="Asdf"
text_bytes=text.encode()
key_bytes=key.encode()
ciphertext=RC4(text_bytes,key_bytes)
plaintext=RC4(ciphertext,key_bytes)
print("text:",text)
print("ciphertext:",ciphertext)
print("text:",plaintext.decode())