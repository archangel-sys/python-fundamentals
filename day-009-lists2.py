print ("Test 1")
scores = [88, 90, 70, 85, 67, 21, 69]

for score in scores:
    if score >= 75:
        print (f"{score} - Passed")
    else:
        print (f"{score} - Failed")

print ("Test 2")
passed = 0

for score in scores:
    if score >= 75:
        passed = passed + 1
print (f"total passed: {passed} out of {len(scores)}")