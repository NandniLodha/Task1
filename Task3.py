import random
import string

def generate_password(length):
    # Define the character set (uppercase, lowercase, digits, special characters)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by randomly selecting characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user for the desired password length
    try:
        length = int(input("Enter the desired length for the password: "))
        
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated Password: {password}")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
