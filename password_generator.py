import random
import string
    
def generate_passwords(length):
    custom_punctution = "@!$"
    characters = string.ascii_letters + string.digits + custom_punctution
    password = "".join(random.choice(characters)for _ in range(length))
    return password

def valid_length():
    while True:
        password_length = int(input("Enter the desired password length (at least 6): "))
        if password_length >= 6:
            return password_length
        else:
            print("Length should be at least 6 charecters.")
  

def main():
    print("~ ~ ~ ~PASSWORD GENERATOR~ ~ ~ ~")
    
    num_passwords = int(input("How many passwords do you want to generate: "))
    password_length = valid_length()
    
    for i in range(num_passwords):
        password = generate_passwords(password_length)
        print(f"Password {i + 1} --> {password}")

if __name__ == "__main__":
    main()