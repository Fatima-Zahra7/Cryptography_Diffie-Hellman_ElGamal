from sympy import isprime
import secrets
from sympy.ntheory.primetest import isprime


def miller_rabin_test(n, k=5):
    """Test de primalité probabiliste de Miller-Rabin."""
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
    """Génère un nombre premier probable de `bits` bits."""
    while True:
        # Générer un nombre aléatoire impair
        num = secrets.randbits(bits)
        if num % 2 == 0:
            num += 1
        # Tester la primalité avec Miller-Rabin
        if miller_rabin_test(num):
            return num


def main():
    # Exemple d'utilisation :
    prime_number = generate_large_prime(1024)
    print(prime_number)


if __name__ == "__main__":
    main()
