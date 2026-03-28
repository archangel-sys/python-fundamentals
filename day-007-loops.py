print ("Test 1")
for day in range (1, 8):
    print (f"day {day} in training complete.")
    
print ("Test 2")
target = int(input("Enter your target year: "))
current = 2026
for year in range (current, target + 1):
    print (f"{year} - locked in.")

print ("Test 3")
for i in range (1, 11):
    if i % 2 == 0:
        print (f"{i} is even")
    else:
        print (f"{i} is odd")