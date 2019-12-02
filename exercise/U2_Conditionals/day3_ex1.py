day = int(input("What day of today?"))
vocation = input("Are we on a vacation?(Yes or no)")

if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    print("7:00")
elif day == 0 or day == 6:
    if vocation == "Yes" or vocation == "yes":
        print("off")
    else:
        print("10:00")
else:
    print("You stupid!")

# ----------------------------------------

string = input("Input a string.")

if string[0] == "f" or string[0] == "F":
    if string[-1] == "b":
        print("FizzBuzz")
    else:
        print("Fizz")
elif string[-1] == "b":
    print("Buzz")
else:
    print("You stupid!")
