import random
import string

# Function to generate password
def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
def main():
    print("---- PASSWORD GENERATOR ----")
    try:
        length = int(input("Enter password length: "))
    except:
        print("Invalid length!")
        return

    print("\nInclude in password?")
    upper = input("Uppercase letters (y/n): ").lower() == 'y'
    digits = input("Numbers (y/n): ").lower() == 'y'
    symbols = input("Special characters (y/n): ").lower() == 'y'
    password = generate_password(length, upper, digits, symbols)
    print("\nGenerated Password:")
    print(password)

# Run program
if __name__ == "__main__":
    main()