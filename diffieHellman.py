from math import gcd
import random

### Diffie-Hellman Key Exchange Algorithm

#### Steps: Generate Prime number of 1024 bits max
def get_prime_size():
    while True:
        try:
            size = int(input("Enter the size of the prime number (in bits, max 1024 bits): "))
            if size < 2 or size > 1024:
                print("Please enter a size between 2 and 1024 bits.")
            else:
                return size
        except ValueError:
            print("Invalid input, please enter a valid integer.")

def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Décompose n - 1 en 2^r * d
    def miller_test(d, n):
        # Choisir un témoin aléatoire a dans [2, n-2]
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Calcul rapide : a^d % n
        if x == 1 or x == n - 1:
            return True

        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Effectuer k tests indépendants
    for _ in range(k):
        if not miller_test(d, n):
            return False
    return True

def generate_large_prime(bits):
    if bits < 2:
        raise ValueError("The number of bits must be greater than or equal to 2.")
    while True:
        prime_candidate = random.getrandbits(bits)
        prime_candidate |= (1 << bits - 1) | 1
        if is_prime_miller_rabin(prime_candidate):
            return prime_candidate

############################################################################################
#### Steps: Check if base is a primitive root

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

############################################################################################
#### Steps: Generate key
def generate_private_key(prime):
    secure_random = random.SystemRandom()
    return secure_random.randint(2, prime - 2)

def generate_public_key(prime, base, private_key):
    return pow(base, private_key, prime)

############################################################################################
#### Steps: Generate shared secret
def generate_shared_secret(prime, public_key, private_key):
    return pow(public_key, private_key, prime)