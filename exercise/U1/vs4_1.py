from datetime import datetime

dn = datetime.now()
yi = int(input("What's your birthyear?\n"))

age_f = int(dn.year) - yi + 1

print("Your age is",age_f,"in next year!")