'''
Powered by JerryX
2018.3.6 21:00

'''
num_dog = int(input("How many dogs?"))
num_cat = int(input("How many cats?"))
num_man = int(input("How many humans?"))

op_dict = {"dog_less": "\nThe world is too dry!",
           "cat_many": "Too many cats! The world is doomed!",
           "dog_many": "\nDogs will drool over the world!",
           "cat_enough": "Just enough cats…",
           "dog_enough": "\nJust enough dogs…",
           "cat_less": "Not too many cats! The world is saved!"}

if num_dog < num_man:
    print("{dog_less}".format(**op_dict))
elif num_dog > num_man:
    print("{dog_many}".format(**op_dict))
else:
    print("{dog_enough}".format(**op_dict))

if num_cat < num_man:
    print("{cat_less}".format(**op_dict))
elif num_cat > num_man:
    print("{cat_many}".format(**op_dict))
else:
    print("{cat_enough}".format(**op_dict))


# -----------------------------------------------
int_a = int(input("Int A\n"))
int_b = int(input("Int B\n"))

quotient = int_a // int_b
remainder = int_a % int_b

print(int_a, "divided by", int_b, "is", quotient, end="")
if remainder:
    print("\000with the remainder", remainder, "\n")
else:
    print("\n")


# -----------------------------------------------
num_s = int(input("How many students?"))

if num_s > 1:
    print(num_s, "students in the room")
if num_s <= 1 and num_s >= 0:
    print(num_s, "student in the room")
if num_s < 0:
    print("You stupid!!!")


# ------------------------------------------------
age = int(input("How old are you?"))

if age < 16:
    print("You can't drive")
if age < 18:
    print("You can't vote")
if age < 25:
    print("You can't rent a car")
if age >= 25:
    print("You can do anything")