import secrets
import random
from sympy import primefactors


# ElGamal Cryptosystem is an asymmetric key encryption algorithm for public-key cryptography which is based
# on the Diffie-Hellman key exchange.

# 1.1 Generate a prime
def miller_rabin_test(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):  # k est le nombre de répétitions
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_large_prime(bits):
    while True:
        # Générer un nombre aléatoire impair
        num = secrets.randbits(bits)
        if num % 2 == 0:
            num += 1
        # Tester la primalité avec Miller-Rabin
        if miller_rabin_test(num):
            return num


# 1.2 Get generator
def get_generator(p: int):
    for g in range(2, p):  # Teste les petites valeurs
        if all(pow(g, (p - 1) // pf, p) != 1 for pf in get_prime_factors(p - 1)):
            return g
    raise ValueError("Pas de générateur trouvé.")


def get_prime_factors(n: int):
    return primefactors(n)


def find_generator(p: int, phi: int, prime_factors: list):
    for g in range(2, p):  # Tester tous les candidats g de 2 à p-1
        if is_valid_generator(g, p, phi, prime_factors):
            return g  # Retourne le premier générateur valide trouvé
    return None


def is_valid_generator(g: int, p: int, phi: int, prime_factors: list):
    for pf in prime_factors:
        if pow(g, phi // pf, p) == 1:  # Si g^{phi/pf} % p == 1, ce n'est pas un générateur
            return False
    return True  # g est un générateur valide


# 2. Encrypt and Decrypt
def encrypt(p, g, h, message):
    # Convert the message to an integer
    message_int = text_to_int(message)

    if message_int >= p:
        raise ValueError(f"Message : {message} is {message_int} BITS it's too large for the modulo {p}.")

    k = random.randint(1, p - 1)  # Random session key

    c1 = pow(g, k, p)  # c1 = g^k mod p
    c2 = (message_int * pow(h, k, p)) % p  # c2 = message * h^k mod p

    return c1, c2


def decrypt(p, x, c1, c2):
    c1_powered = pow(c1, x, p)  # c1^x mod p

    c1_inv = mod_inverse(c1_powered, p)  # Modular inverse of c1^x

    decrypted_message_int = (c2 * c1_inv) % p  # Decrypted message
    decrypted_message = int_to_text(decrypted_message_int)  # Convert to text

    return decrypted_message


# 3. Modular inverse
def extended_euclidean(a: int, b: int):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t  # Retourne (pgcd, s, t)


def mod_inverse(a: int, m: int):
    g, s, t = extended_euclidean(a, m)
    if g != 1:
        raise ValueError(f"{a} has no inverse modulo {m}")
    return s % m


# 4. Generate keys
def generate_keys(bits=128):
    p = generate_large_prime(bits)
    print(p)

    g = get_generator(p)  # generator
    x = secrets.randbelow(p - 1)  # private key
    h = pow(g, x, p)  # public key

    return (p, g, h), (p, x)  # Retourner les clés publiques et privées


# 5 Messages
def text_to_int(text: str):
    # Convertir le texte en entier en UTF-8
    return int.from_bytes(text.encode('utf-8'), 'big')


def int_to_text(number):
    byte_length = (number.bit_length() + 7) // 8  # Calculate the byte length
    return number.to_bytes(byte_length, 'big').decode('utf-8', errors='ignore')


# 6. Main
def main():
    public_key, private_key = generate_keys()
    p, g, h = public_key

    print("Public key:", public_key)
    print("Private key:", private_key)

    message = input("Enter a message you want to encrypt: ")
    print(f"Message original: {message}")

    c1, c2 = encrypt(p, g, h, message)
    print("Message chiffré (c1, c2):", c1, c2)

    decrypted_message = decrypt(*private_key, c1, c2)
    print("Message déchiffré:", decrypted_message)


if __name__ == "__main__":
    main()
