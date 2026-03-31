print ("Test 1 - Basic function with no input")
def greet():
    print ("Hello, World")
greet()
greet()
greet()

print ("Test 2 - Function that accepts input")
def greet(name):
    print (f"Hello, {name}.")
greet("Stella")
greet("Jiwoo")
greet("Ian")

print ("Test 3 - Function that returns a value")
def add(a,b):
    return a + b
result = add (10,15)
print(result)

print ("Test 4 - Function with a condition inside")
def check_pass(score):
    if score >= 75:
        return "Passed"
    else:
        return "Failed"
print (check_pass(80))
print (check_pass(70))