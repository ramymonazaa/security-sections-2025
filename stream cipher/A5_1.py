def shift(register, taps):
    """Perform LFSR shift with given feedback taps."""
    new_bit = 0
    for t in taps:
        new_bit ^= register[t]  # XOR feedback bits
    return [new_bit] + register[:-1]  # Shift right and insert new bit

def encrypt(plaintext, key):
    """Encrypt plaintext using A5/1 stream cipher."""

    # Convert plaintext to binary list
    binary_plaintext = [int(b) for b in ''.join(format(ord(c), '08b') for c in plaintext)]

    # Initialize registers (R1: 19 bits, R2: 22 bits, R3: 23 bits)
    R1 = [int(b) for b in bin(key & 0x7FFFF)[2:].zfill(19)]  # Use 19 bits from key
    R2 = [int(b) for b in bin((key >> 19) & 0x3FFFFF)[2:].zfill(22)]  # Next 22 bits
    R3 = [int(b) for b in bin((key >> 41) & 0x7FFFFF)[2:].zfill(23)]  # Last 23 bits

    # Feedback taps for LFSR shifting
    taps_R1 = [13, 16, 17, 18]  # Taps for R1
    taps_R2 = [20, 21]  # Taps for R2
    taps_R3 = [7, 20, 21, 22]  # Taps for R3

    keystream = []

    for _ in range(len(binary_plaintext)):
        # Majority clocking
        majority = ((R1[8]^R2[10])|(R1[8]^R3[10])|(R2[10]^R2[10]))

        if R1[8] == majority:
            R1 = shift(R1, taps_R1)
        if R2[10] == majority:
            R2 = shift(R2, taps_R2)
        if R3[10] == majority:
            R3 = shift(R3, taps_R3)

        # Keystream bit is XOR of last bits of R1, R2, and R3
        keystream.append(R1[-1] ^ R2[-1] ^ R3[-1])

    # XOR plaintext with keystream to get ciphertext
    ciphertext = [p ^ k for p, k in zip(binary_plaintext, keystream)]
    ciphertext_chars = []
    for i in range(0, len(ciphertext), 8):
        ciphertext_chars.append(chr(int(''.join(map(str, ciphertext[i:i + 8])), 2)))

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
