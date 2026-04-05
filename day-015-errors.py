try:
    number = int(input("Enter a number: "))
    print (10/number)
except ValueError:
    print ("That is not a valid number.")
except ZeroDivisionError:
    print ("Cannot divide by 0.")
finally:
    print ("Program Finished.")