# Cryptography_Diffie-Hellman_ElGamal

This project includes implementations of two fundamental cryptographic algorithms: **Diffie-Hellman Key Exchange** and **ElGamal Encryption**. Both algorithms are widely used in secure communication protocols to ensure data confidentiality and integrity.

## Diffie-Hellman Key Exchange

In the **Diffie-Hellman Key Exchange**, two parties can securely exchange cryptographic keys over an insecure channel, allowing them to establish a shared secret. This shared secret can then be used to encrypt further communication without the need to directly transmit the secret key itself.

### Steps of Diffie-Hellman Key Exchange:

1. **Agree on public parameters**: Both parties agree on a large prime number (`p`) and a base (`g`), which are used in all calculations. These are public and can be transmitted openly.

2. **Private key selection**: Each party selects a private key. This private key is kept secret and is never transmitted.

3. **Generate public keys**: Each party computes a public key by raising the base (`g`) to the power of their private key, modulo the prime number (`p`). This public key is then shared with the other party.

4. **Compute the shared secret**: Each party takes the other party's public key and raises it to the power of their own private key, modulo `p`. This results in a shared secret that is the same for both parties, even though the key was never directly exchanged.

The **Diffie-Hellman Key Exchange** algorithm enables secure communication without the need to transmit sensitive information, thus reducing the risk of interception by unauthorized parties.

### Implementation in this project:
- The implementation uses the **Miller-Rabin primality test** for generating large prime numbers.
- It allows users to select the key size (128, 256, 512, or 1024 bits) and generates the required prime numbers and public keys.
- The private keys are securely generated, and the shared secret is computed for both parties (e.g., Alice and Bob), ensuring that both derive the same secret key for encryption.

---

## ElGamal Encryption

The **ElGamal Encryption** system is a public-key cryptosystem that provides encryption and decryption through asymmetric key pairs. It is based on the Diffie-Hellman key exchange protocol but adds encryption/decryption steps.

### Steps of ElGamal Encryption:

1. **Key Generation**: A large prime number `p` and a generator `g` are selected, just like in Diffie-Hellman. A private key `x` is selected randomly, and the corresponding public key `y = g^x mod p` is computed.

2. **Encryption**: To encrypt a message, the sender chooses a random value `k` and computes two values:
    - `c1 = g^k mod p` (which is part of the ciphertext)
    - `c2 = m * y^k mod p` (where `m` is the plaintext message).

   The ciphertext consists of the pair `(c1, c2)`.

3. **Decryption**: The receiver uses their private key `x` to decrypt the ciphertext. The decryption involves computing the shared secret `s = c1^x mod p` and using it to recover the original message `m = c2 * s^(-1) mod p`.

ElGamal encryption provides semantic security, meaning that even if an attacker intercepts the ciphertext, they cannot deduce any information about the plaintext without the private key.

### Implementation in this project:
- The **ElGamal encryption** implementation generates the necessary public and private keys.
- The system allows the encryption of a plaintext message with the recipient's public key and provides the decryption process using their private key.

---

## Project Features:
- **Key Exchange and Encryption**: This project demonstrates both the Diffie-Hellman key exchange and ElGamal encryption systems, offering a comprehensive approach to understanding how these algorithms work together.
- **Key Size Selection**: You can choose the key size (128, 256, 512, or 1024 bits) to determine the strength of the cryptographic operations.
- **Real-time Computation**: The project calculates the prime numbers, public keys, and shared secrets in real-time, making the learning process interactive.

## Conclusion:
This project is a practical implementation of two essential cryptographic algorithms—Diffie-Hellman and ElGamal. It provides a simple yet comprehensive way to understand how these algorithms work and how they are applied in secure communications. Whether you're learning about cryptography or working on securing communications, this implementation is a useful resource.
