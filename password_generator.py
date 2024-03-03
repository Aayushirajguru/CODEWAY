import random
import string

def generate_password(length, complexity):
    if complexity == "simple":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "complex":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Using simple complexity.")
        characters = string.ascii_letters

    password = random.choice(string.ascii_uppercase)  # first letter is capital
    password += ''.join(random.choice(characters) for _ in range(length - 1))
    return password

def main():
    print("===== Password Generator =====")
    length = int(input("Enter the desired password length: "))
    complexity = input("Enter complexity level (simple, medium, complex): ").lower()
    password = generate_password(length, complexity)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
