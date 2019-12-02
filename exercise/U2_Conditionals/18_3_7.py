n = 333
a1 = 3
an = 999

s = (3 + 999) * 333 / 2
s1 = (5 + 1000) * 200 / 2
s2 = (15 + 990) * 66 / 2
sa = s + s1 - s2 - 1000

print(sa)

#   -------------------------------------------------

total_sum = 0
for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum+i
print(total_sum)
