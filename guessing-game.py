import random
from datetime import datetime

def save_result(attempts):
    now=datetime.now()
    date=f"{now.year}, {now.month}, {now.day}"
    file=open("game-results.txt", "a")
    file.write(f"{date} | Solved in {attempts} attempts\n")
    file.close

target=random.randint(1, 100)
attemps=0

print("Guess a number between 1 and 100")

while true:
    try:
        guess=int(input("Your guess: "))
        attempt += 1
        if guess < target:
            print ("Too high")
        elif:
            print