# main.py
import elGamal
import diffieHellman


def main():
    while True:
        print("=== Cryptography System ===")
        print("1. ElGamal Cryptography System")
        print("2. Diffie-Hellman Key Exchange")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if choice == 1:
                elGamal.main()
            elif choice == 2:
                diffieHellman.main()
            elif choice == 3:
                print("Thank you for using the Cryptography System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
