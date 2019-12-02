num_people = int(input("How many people to get takeout?"))
price_total = float(input("How much in total?"))

price_people = price_total / num_people

print("Each people needs to pay", price_people, "yuan.")

# --------------------------
num_students = int(input("How many students?"))
num_perGroup = int(input("How many students per group?"))

num_groups = num_students // num_perGroup
num_left = num_students - num_groups * num_perGroup

print("There will have", num_groups, "groups, and",
      num_left, "students will left over.")

# --------------------------
a = input("First string")
b = input("Second string")
c = input("Third string")
d = input("Fourth string")

print("{3},{2},{1},{0}".format(a, b, c, d))

# --------------------------
num = int(input("numerator"))
deno = int(input("denominator"))

print("{:.2%}".format(num / deno))
