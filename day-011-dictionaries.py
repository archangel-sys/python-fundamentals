print("Test 1")
person = {"name":"Angel", "Age":21, "House":"Slytherin"}
print(person["name"])
print(person["Age"])
print(person["House"])

print("Test 2")
person["country"] = "Canada"
person["Age"] = 22
print(person)

print("Test 3")
for key, value in person.items():
    print(f"{key}: {value}")