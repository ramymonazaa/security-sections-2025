def encrypt(plaintext, key):
    """Encrypt plaintext using A5/1 stream cipher."""
    # Convert plaintext to binary list
    plaintext_bits = []
    for c in plaintext:
        bits=f"{ord(c):08b}"
        plaintext_bits.extend(int(i) for i in bits)
    # Initialize registers (R1: 19 bits, R2: 22 bits, R3: 23 bits)
    R1=[int(i) for i in bin(key&0x7FFFF)[2:].zfill(19)]#first 19 bits
    R2=[int(i) for i in bin((key>>19)&0x3FFFFF)[2:].zfill(22)]#next 22 bits
    R3=[int(i) for i in bin((key>>41)&0x7FFFFF)[2:].zfill(23)]#last 23 bits
    # Feedback taps for LFSR shifting
    keystream = []

    for i in range(len(plaintext_bits)):
        # Majority clocking
        majority = (R1[8]+R2[10]+R3[10])>=2
        if R1[8] == majority:
            newbit=R1[13]^R1[16]^R1[17]^R1[18]
            R1=[newbit]+R1[:-1]
            #x 0 1 2 3 4 5
        if R2[10] == majority:
            newbit=R2[20]^R2[21]
            R2=[newbit]+R2[:-1]
        if R3[10] == majority:
            newbit=R3[7]^R3[20]^R3[21]^R3[22]
            R3=[newbit]+R3[:-1]

        # Keystream bit is XOR of last bits of R1, R2, and R3
        keystream.append(R1[18] ^ R2[21] ^ R3[22])

    # XOR plaintext with keystream to get ciphertext
    # ciphertext = [p ^ k for p, k in zip(plaintext_bits, keystream)]
    ciphertext =[]
    for i,j in zip(plaintext_bits, keystream):
        ciphertext.append(i ^ j)
    ciphertext_chars = []
    print(ciphertext)
    for i in range(0, len(ciphertext), 8):
        x=map(str,ciphertext[i:i+8])
        x_int=int(''.join(x),2)
        ciphertext_chars.append(chr(x_int))
    return ''.join(ciphertext_chars)  # Return as string

def decrypt(ciphertext, key):
    """Decrypt ciphertext using A5/1 (same as encryption)."""
    return encrypt(ciphertext, key)  # XORing twice cancels out encryption

import random
# Example Usage
key = random.getrandbits(64)  # 64-bit key
plaintext = "HELLO"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted: ", decrypted_text)