import random
import string

# Function to generate a password
def generate_password(length):
    # Define the character pool: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by choosing 'length' number of characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Main function
def main():
    try:
        # Ask user for the desired password length
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:  # Set a minimum length for security reasons
            print("Password length should be at least 4 characters.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the program
if __name__ == '__main__':
    main()
