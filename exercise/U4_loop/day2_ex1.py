for i in range(5):
    print("Mr. Lee is strange?")
# ---------------------------

ip_num = int(input("intrger"))

if ip_num >= 1:
    for i in range(1, ip_num + 1):
        print(i)
else:
    for i in range(ip_num, 0):
        print(i)
# -----------------------------

count_from = int(input("count from: "))
count_to = int(input("count to: "))
count_by = int(input("count by: "))

for i in range(count_from, count_to + 1, count_by):
    print(i)
# -----------------------------

sum_students = int(input("How many students?"))
sum_mark = 0

for num_students in range(sum_students):
    print("What is the mark of student #", num_students)
    current_mark = float(input())
    sum_mark = sum_mark + current_mark
else:
    print("Average mark is ", sum_mark / sum_students)
# -----------------------------

ip = str(input("Give a string: "))

for i in range(len(ip)):
    if str.islower(ip[i]):
        print(str.upper(ip[i]), end="")
    elif str.isupper(ip[i]):
        print(str.lower(ip[i]), end="")
    else:
        print(ip[i])
else:
    print()
# ---------------------------------------

import math

ip = str(input("Give a string"))
num_ra = math.ceil(len(ip) / 7)
ra = "raccoon" * num_ra

for i in range(len(ip)):
    print(ip[i], end="")
    if i < len(ip) - 1:
        print(ra[i], end="")
else:
    print()
