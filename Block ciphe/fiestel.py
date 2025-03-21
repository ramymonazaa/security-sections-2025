import random
def generate_keys(num):
    return [random.randint(0,255)for _ in range(num)]
def round_f(plaintext,key):
    return bytes([p^key for p in plaintext])
def feistel_encrypt(plaintext,keys):
    plaintext=plaintext.encode()
    mid=len(plaintext)//2
    # mid=int(mid)
    L,R=plaintext[:mid],plaintext[mid:] 
    #rounds
    for k in keys:
        round_res=round_f(R,k)
        new_left=R
        new_right=[a^b for a,b in zip(L,round_res)]
        L,R=new_left,new_right
        # L,R=R,[a^b for a,b in zip(L,round_res)]
    return L+R
def feistel_decrypt(ciphertext,keys):
    mid=len(ciphertext)//2
    L,R=ciphertext[:mid],ciphertext[mid:] 
    for k in reversed(keys):
        L,R=[a^b for a,b in zip(R,round_f(L,k))],L
    return bytes(L+R).decode()

num=4
keys=generate_keys(num)
print(keys)
plaintext="Hello, world!"
ciphertext=feistel_encrypt(plaintext,keys)
print("cihertext: ",ciphertext)
print("plaintext: ", feistel_decrypt(ciphertext,keys))
