def douple_trans_encrypt(plaintext,rows,cols,perR,perC):
    ciphertext=[]
    for i in range(rows):
        ciphertext.append([])
        for j in range(cols):
            ciphertext[i].append('.')
    for i in range(rows):
        for j in range(cols):
            ciphertext[i][j]=plaintext[perR[i]-1][perC[j]-1]
    
    return ciphertext
def double_trans_decrypt(ciphertext,rows,cols,perR,perC):
    plaintext=[]
    for i in range(rows):
        plaintext.append([])
        for j in range(cols):
            plaintext[i].append('.')
    for i in range(rows):
        for j in range(cols):
            plaintext[perR[i]-1][perC[j]-1]=ciphertext[i][j]
    
    return plaintext
rows,cols
perR=[3,2,1]
perC=[4,2,1,3]
plaintext=[['a','t','t','a'],['c','k','a','t'],['d','a','w','n']]
rows=len(plaintext)
cols=len(plaintext[0])
cipher=douple_trans_encrypt(plaintext,rows,cols,perR,perC)
print("cipher: ",cipher)
text=double_trans_decrypt(cipher,rows,cols,perR,perC)
print("text: ",text)

