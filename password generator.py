import random 
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password
def paswd():
    length=int(input("Enter the desired length of password:"))
    password=generate_password(length)
    print("Generated password:", password)
paswd()
print("Thank you for generating the password")