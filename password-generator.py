import random
import string
from datetime import datetime

def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=""
    for i in range(length):
        password+=random.choice(characters)
    return password

def save_password(password):
    now=datetime.now()
    date=f"{now.year}-{now.month}-{now.day}"
    file=open("password.txt", "a")
    file.write(f"{date} | {password}\n")
    file.close()

length=int(input("Enter Password length: "))
password=generate_password(length)
print(f"Generated: {password}")
save_password(password)
print("Saved to password.txt")