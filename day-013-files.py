file = open ("notes.txt", "w")
file.write ("Day 013 - file handling\n")
file.write ("This is saved permanently\n")
file.close()

file = open ("notes.txt", "r")
content = file.read()
file.close()
print (content)

file = open ("notes.txt", "a")
file.write("Adding a new line without deleting the rest\n")
file.close()