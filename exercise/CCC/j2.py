rowcount = int(input())
op = ""
ip_list = []
# counter = 0
multiple = ""
contain = ""

for i in range(rowcount):
    ip_list.append(input())

for element in ip_list:
    for char in element:
        if char != " ":
            multiple = multiple + str(char)
        else:
            contain = element[-1]
            break
    print(contain * int(multiple))
    contain = ""
    multiple = ""

