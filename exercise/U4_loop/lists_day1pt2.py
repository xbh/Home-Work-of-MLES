total_num = int(input("How many number you want to print?"))

num_lst = []

for i in range(0, total_num):
    print("What is the #", i, "number should be?")
    ip_num = int(input())
    list.append(num_lst, ip_num)

print(num_lst)

# -----------------------------

input_name = 0
name_list = []

while input_name != "STOP":
    input_name = str(input("What is your name?"))
    list.append(name_list, input_name)

print(name_list[:-1])

name_remove = str(input("Which name that you want to remove?"))
list.remove(name_list, name_remove)

print(name_list[:-1])

# -------------------------------


def middle_way(ip_list_a, ip_list_b):
    mid_a = ip_list_a[1]
    mid_b = ip_list_b[1]
    return [mid_a, mid_b]


def rorate_left(ip_list):
    swap = ip_list[0]
    ip_list[0] = ip_list[1]
    ip_list[1] = swap
    return ip_list


def rorate_any_num(ip_list, switch_num_a, switch_num_b):
    swap = ip_list[switch_num_a]
    ip_list[switch_num_a] = ip_list[switch_num_b]
    ip_list[switch_num_b] = swap
    return ip_list
