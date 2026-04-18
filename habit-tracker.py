from datetime import datetime

def log_habit(habit):
    now=datetime.now()
    date=f"{now.year}-{now.month}-{now.day}"
    file=open("habits.txt", "a")
    file.write(f"{date} | {habit}\n")
    file.close()
    print (f"Logged: {habit}")

def show_log():
    try:
        file=open("habits.txt", "r")
        content=file.read()
        file.close()
        print ("--- Habit Log ---")
        print (content)
    except FileNotFoundError:
        print("No habits logged yet")

habit=input("What did you complete today?")
log_habit(habit)
show_log()