import secrets
from math import gcd
import random
import time


# Diffie-Hellman Key Exchange Algorithm

# Steps: Generate Prime number of 1024 bits max
def ask_len_prime():
    options = {1: 128, 2: 256, 3: 512, 4: 1024}
    while True:
        try:
            print("Select the number of bits to generate your keys:")
            for key, value in options.items():
                max_message_length = value // 8 - 1  # Calculer la longueur max en octets
                print(f"{key}. {value} bits (max message length: {max_message_length} characters)")
            choice = int(input("Enter your choice (1-4): "))

            if choice in options:
                return options[choice]
            else:
                print("Invalid choice. Please select a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")


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


# Steps: Check if base is a primitive root

def is_primitive_root(base, prime):
    if gcd(base, prime) != 1:
        return False  # La base doit être coprime avec prime

    # Calculer les facteurs de (prime - 1)
    phi = prime - 1
    factors = set()
    n = phi
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1

    if n > 1:
        factors.add(n)

    # Vérifier que base^(phi/f) != 1 (mod prime) pour tous les facteurs f
    for factor in factors:
        if pow(base, phi // factor, prime) == 1:
            return False
    return True


def choose_base_for_prime(prime):
    if prime < 2:
        raise ValueError("Le nombre doit être un nombre premier supérieur ou égal à 2.")

    # Bases prédéfinies à tester en premier
    predefined_bases = [2, 3, 5, 7, 11, 13]
    attempts = predefined_bases + [random.randint(2, prime - 1) for _ in range(100)]

    for base in attempts:
        if is_primitive_root(base, prime):
            return base

    # Si aucune base n'est trouvée après tous les essais
    return None


# Steps: Generate key
def generate_private_key(prime):
    secure_random = random.SystemRandom()
    return secure_random.randint(2, prime - 2)


def generate_public_key(prime, base, private_key):
    return pow(base, private_key, prime)


# Steps: Generate shared secret
def generate_shared_secret(prime, public_key, private_key):
    return pow(public_key, private_key, prime)


def main():
    print("=== Diffie-Hellman Key Exchange ===")

    prime_size = ask_len_prime()
    prime = generate_large_prime(prime_size)
    print(f"\n✔ Generated prime number ({prime_size} bits): {prime}")

    base = choose_base_for_prime(prime)
    if base:
        print(f"✔ The base {base} was found as a primitive root for the prime number {prime}.")

        # Alice's keys
        alice_private_key = generate_private_key(prime)
        alice_public_key = generate_public_key(prime, base, alice_private_key)
        print(f"🔑 Alice's Public Key: {alice_public_key}")

        # Bob's keys
        bob_private_key = generate_private_key(prime)
        bob_public_key = generate_public_key(prime, base, bob_private_key)
        print(f"🔑 Bob's Public Key: {bob_public_key}")

        # Shared secret
        alice_shared_secret = generate_shared_secret(prime, bob_public_key, alice_private_key)
        bob_shared_secret = generate_shared_secret(prime, alice_public_key, bob_private_key)

        print(f"🤝 Alice's Shared Secret: {alice_shared_secret}")
        print(f"🤝 Bob's Shared Secret: {bob_shared_secret}")

        if alice_shared_secret == bob_shared_secret:
            print("✔ Key exchange successful!")
        else:
            print("❌ Key exchange failed. Shared secrets do not match.")
    else:
        print(f"❌ No primitive root found for the prime number {prime}.\nPlease try again.")

    print("Thank you for using the Diffie-Hellman Key Exchange. Goodbye!")