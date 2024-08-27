from math import gcd

# defining a function to perform RSA approch


def rsa(p: int, q: int, m: int):
    # calculating n
    n = p * q

    # calculating totient, t
    t = (p - 1) * (q - 1)

    # selecting public key, e
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break

    # selecting private key, d
    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1

    # performing encryption
    c = pow(m, e, n)
    print(f"Encrypted message is {c}")

    # performing decryption
    m = pow(c, d, n)
    print(f"Decrypted message is {m}")


# Testcase - 1
rsa(p=53, q=59, m=89)

# Testcase - 2
rsa(p=3, q=7, m=12)
