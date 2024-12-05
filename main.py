from diffieHellman import *
import time

def main():
    print("=== Diffie-Hellman Key Exchange ===")

    start_time = time.time()

    prime_size = get_prime_size()
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

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\n⏱ Execution Time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()