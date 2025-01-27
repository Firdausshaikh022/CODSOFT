import random
import string

def generate_password(length, complexity):
    """
    Generate a random password with the specified length and complexity.
    :param length: Length of the password.
    :param complexity: Complexity level (1: Letters, 2: Letters+Digits, 3: Letters+Digits+Special Characters).
    :return: Generated password.
    """
    if length < 1:
        return "Password length must be at least 1 character."

    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Determine the character set based on complexity
    if complexity == 1:
        char_pool = letters
    elif complexity == 2:
        char_pool = letters + digits
    elif complexity == 3:
        char_pool = letters + digits + special_chars
    else:
        return "Invalid complexity level. Choose 1, 2, or 3."

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        print("Select the complexity level:")
        print("1: Letters only")
        print("2: Letters and digits")
        print("3: Letters, digits, and special characters")
        complexity = int(input("Enter the complexity level (1, 2, or 3): "))

        # Generate and display the password
        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter numbers for length and complexity.")

if __name__ == "__main__":
    main()
