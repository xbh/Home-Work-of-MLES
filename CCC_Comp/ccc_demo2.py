'''
Demo program for CCC Test 2018
Problem J2
'''
digits = int(input())
col_a = input()
col_b = input()
counter = 0

for i in range(digits):
    if col_a[i] == col_b[i]:
        if col_a[i] == ".":
            pass
        else:
            counter = counter + 1

print(counter)