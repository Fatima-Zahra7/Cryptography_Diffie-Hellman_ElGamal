import random
from math import sqrt

### Diffie-Hellman Key Exchange Algorithm

#### Steps: Generate Prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_large_prime():
    while True:
        prime = random.randint(10**9, 10**10)  # Choisir un nombre assez grand
        if is_prime(prime):
            return prime

############################################################################################
#### Steps: Check if base is a primitive root
def is_primitive_root(base, prime):
    """Vérifie si la base est une racine primitive modulo prime."""
    powers = set()
    for i in range(1, prime):
        powers.add(pow(base, i, prime))
    return len(powers) == prime - 1  # Une racine primitive génère tous les entiers de 1 à prime-1

def choose_base_for_prime(prime):
    """Choisit une base vérifiée comme racine primitive pour le nombre premier."""
    for base in [2, 3, 5]:
        if is_primitive_root(base, prime):
            return base
    return None  # Si aucune base vérifiée n'est trouvée

############################################################################################
#### Steps: Generate key
def generate_private_key(prime):
    return random.randint(2, prime - 2)

def generate_public_key(prime, base, private_key):
    return pow(base, private_key, prime)

############################################################################################
#### Steps: Generate shared secret
def generate_shared_secret(prime, public_key, private_key):
    return pow(public_key, private_key, prime)

############################################################################################
#### Main
if __name__ == "__main__":
    # Générer un nombre premier large et valide
    prime = generate_large_prime()
    base = choose_base_for_prime(prime)  # Exemple de base, qui devrait être une racine primitive dans un contexte réel

    print(f"Prime number is: {prime}")
    print(f"Base is: {base}")

    # Alice génère ses clés privées et publiques
    alice_private_key = generate_private_key(prime)
    alice_public_key = generate_public_key(prime, base, alice_private_key)
    print(f"Alice's Public Key: {alice_public_key}")

    # Bob génère ses clés privées et publiques
    bob_private_key = generate_private_key(prime)
    bob_public_key = generate_public_key(prime, base, bob_private_key)
    print(f"Bob's Public Key: {bob_public_key}")

    # Alice et Bob génèrent le secret partagé
    alice_shared_secret = generate_shared_secret(prime, bob_public_key, alice_private_key)
    bob_shared_secret = generate_shared_secret(prime, alice_public_key, bob_private_key)

    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")
    assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"
    print("Key exchange successful!")
