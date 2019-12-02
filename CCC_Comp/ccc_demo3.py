'''
Demo program for CCC Test 2018
Problem J3
'''
houses = []
num = ""

input_array = input()

for i in range(len(input_array) - 1):
    num = num + str(input_array[i])
    if input_array[i + 1] == " ":
        i = i + 1
    else:
        houses.append(num)

for i in houses:
    print("is:", i)
