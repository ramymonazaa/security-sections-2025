# Python Program for implementation of RSA Algorithm
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


# Function to find modular inverse of e modulo phi(n)
def mod_inv(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return -1


# RSA Key Generation
def get_key():
    p, q = 11, 19
    N = p * q
    phi = (p - 1) * (q - 1)
    e = 1
    for i in range(2, phi):
        if gcd(phi, i) == 1:
            e = i
            break

    # Compute d such that e * d ≡ 1 (mod phi(n)) ==> (e * d) % 7 ≡ 1
    d = mod_inv(e, phi)
    return N, e, d


def RSA(base, N, e):
    result = 1
    while e > 0:
        if e % 2 == 1:
            result *= base
            result %= N
        base *= base
        base %= N
        e = e // 2
    return result


N, e, d = get_key()
print(f"Public Key (e, n): ({e}, {N})")
print(f"Private Key (d, n): ({d}, {N})")
M = 123
print(f"Original Message: {M}")
cipher = RSA(M, N, e)
print(f"Encrypted Message: {cipher}")
plain = RSA(cipher, N, d)
print(f"Decrypted Message: {plain}")
