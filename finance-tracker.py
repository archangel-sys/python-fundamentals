print("Finances")
from datetime import datetime

def save_record(entry):
    file=open("finance.txt", "a")
    file.write(entry + "\n")
    file.close()
def show_records():
    try:
        file=open("finance.txt", "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("no records yet")

income=float(input("Enter Total Income: "))
expenses=float(input("Enter Total Expenses: "))
balance= income - expenses
now=datetime.now()
date=f"{now.year}-{now.month}-{now.day}"

if balance >= 0:
    status="Savings"
else:
    status="In debt"
report=f"{date}|Income={income}|Expenses={expenses}|Balance={balance}|Status={status}"

print(report)
save_record(report)
print("===All Records===")
show_records()