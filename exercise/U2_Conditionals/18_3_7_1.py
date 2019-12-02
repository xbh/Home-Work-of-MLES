total_sum = 0
a = 1
b = 2

while a < 4000000:
    a = a + b
    if a % 2 == 0 and a < 4000000:
        total_sum = total_sum + a
    b = a + b
    if b % 2 == 0 and b < 4000000:
        total_sum = total_sum + b

print (total_sum + 2)
