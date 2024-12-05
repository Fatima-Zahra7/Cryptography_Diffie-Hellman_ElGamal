import math, random

########################################################################
### ElGamal Cryptosystem
# ElGamal is an asymmetric key encryption algorithm for public-key cryptography which is based on the Diffie-Hellman key exchange.

#### 1.1 Generate numbers
def get_prime_size():
    while True:
        try:
            size = int(input("Enter the size for the key (in bits, max 1024 bits): "))
            if size < 2 or size > 1024:
                print("Please enter a size between 2 and 1024 bits.")
            else:
                return size
        except ValueError:
            print("Invalid input, please enter a valid integer.")

def is_prime(n: int) :
    if n < 2 :
        return False
    else :
        for i in range(2, int(math.sqrt(n)) + 1) :
            if n % i != 0:
                return True

def get_prime_number(bits: int) :
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

#### 1.2 Get generator
def get_generator(p: int):
    #Étapes 1 & 2 : Trouver les diviseurs premiers de phi
    if p < 2:
        raise ValueError("p must be a prime number greater or equals to 2.")

    phi = p - 1
    prime_factors = []

    # Étape 3 : Trouver les diviseurs premiers de phi
    for d in range(2, phi + 1):
        if phi % d == 0:
            # Vérifie si d est premier
            is_prime = True
            for i in range(2, int(d**0.5) + 1):
                if d % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_factors.append(d)

    # Étape 4 : Tester les candidats g
    for g in range(2, p):  # Parcourir tous les entiers g de 2 à p-1
        is_generator = True

        # Vérifie la condition g^{phi/pf} % p != 1 pour tous les diviseurs premiers pf
        for pf in prime_factors:
            if pow(g, phi // pf, p) == 1:  # Utilise l'exponentiation modulaire
                is_generator = False
                break

        if is_generator:
            return g  # Retourne le premier générateur trouvé

    return None  # Si aucun générateur n'est trouvé (rare)

########################################################################
#### 2. Generate keys
def generate_keys(bits: int) :
    p=get_prime_number(bits) #prime number
    g=get_generator(p) #generator

    x = random.randint(1, p-2) #private key
    h = pow(g,x,p) #public key

    return (p, g, h), (p, x) # Retourner les clés publiques et privées
