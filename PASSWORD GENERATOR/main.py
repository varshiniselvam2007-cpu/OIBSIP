import random
import string

while True:
    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Password length must be at least 8.")
        continue

    print("Choose character types:")
    upper = input("Include Uppercase letters? (yes/no): ").lower() == "yes"
    lower = input("Include Lowercase letters? (yes/no): ").lower() == "yes"
    numbers = input("Include Numbers? (yes/no): ").lower() == "yes"
    symbols = input("Include Symbols? (yes/no): ").lower() == "yes"

    characters = ""

    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    selected_types = sum([upper, lower, numbers, symbols])

    if selected_types < 2:
        print("Please select at least two character types.")
        continue

    password = "".join(random.choice(characters) for _ in range(length))

    print("\nGenerated Password:", password)

    again = input("\nGenerate another password? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using Password Generator!")
        break
