print(chr("A"), chr("a"), chr("Z"), chr("z"), chr("0"), chr("5"))

print(chr(32), chr(10), chr(33))

# ---------------------------------
string = str(input("input a string"))

if str.isalpha(string):
    for i in range(0, 3):
        if str.islower(string[i]):
            a = str.upper(string[i])
            print(a)
        else:
            b = str.lower(string[i])
            print(b)
else:
    print(string)

# -------------------------------------------
string_i = str(input("Input a string"))
Sum = 0

for i in range(0, 3):
    if str.isdigit(string_i[i]):
        Sum = Sum + int(string_i[i])
    else:
        pass
else:
    print(Sum)

import math

A = float(49)
B = float(5)
c = float(7)

a = math.sqrt(B ** 2 + c ** 2 - 2 * B * c * math.cos(A))
