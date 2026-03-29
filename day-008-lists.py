goals = ["Graduate", "Canada", "Actor", "SKKU Masters"]

print (goals[0])
print (goals[1])
print (len(goals))

for goal in goals:
    print (f"target: {goal}")

goals.append ("Korea")
goals.remove ("Canada")
print (goals)