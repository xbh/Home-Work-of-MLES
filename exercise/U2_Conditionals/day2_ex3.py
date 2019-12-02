age = int(input("How old are you?"))

if age <= 0:
    print("You stupid!!!")
elif age < 16 and age > 0:
    print("You can't drive")
elif age >= 16 and age <= 17:
    print("You can drive but not vote")
elif age >= 18 and age <= 24:
    print("You can vote but not rent a car")
else:
    print("You can do pretty much anything")