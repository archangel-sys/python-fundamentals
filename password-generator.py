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
    date=