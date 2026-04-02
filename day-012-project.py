def check(score):
    if score >= 75:
        return "Passed"
    else:
        return "Failed"

students = []
count = int(input("How Many Students: "))

for i in range(count):
    name = input("Enter name: ")
    score = int(input("Enter Score: "))
    students.append({"name":name, "score": score})

print ("---Report---")
passed = 0

for student in students:
    results = check (student["score"])
    print (f"{student['name']}: {student['score']} - {results}")
    if results == "Passed":
        passed += 1

print (f"Total passed: {passed} out of {len(students)}")