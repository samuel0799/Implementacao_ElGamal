import random
from Crypto.Util import number

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

p = 467
g = 2
x = 127
y = mod_exp(g, x, p)

def set_parameters(new_p, new_g, new_x):
    global p, g, x, y
    p = new_p
    g = new_g
    x = new_x
    y = pow(g, x, p)

def get_parameters():
    return {"p": p, "g": g, "x": x, "y": y}

def generate_random_parameters(bits):
    p = number.getPrime(bits)
    # print("p:", p)
    # print("Dígitos de p:", len(str(p)))
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)
    return p, g, x

def text_to_int_list(text):
    return [ord(c) for c in text]

def int_list_to_text(lst):
    return ''.join(chr(i) for i in lst)

def encrypt_text(text):
    int_list = text_to_int_list(text)
    encrypted = []
    for m in int_list:
        k = random.randint(1, p - 2)
        a = mod_exp(g, k, p)
        b = (m * mod_exp(y, k, p)) % p
        encrypted.append((a, b))
    return encrypted

def decrypt_pairs(pairs):
    decrypted = []
    for a, b in pairs:
        s = mod_exp(a, x, p)
        s_inv = modinv(s, p)
        m = (b * s_inv) % p
        decrypted.append(m)
    return int_list_to_text(decrypted)
