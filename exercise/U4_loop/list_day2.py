def reverseList (ip_list):
    for i in range(len(ip_list) // 2):
        swap = ip_list[i]
        i_r = i + 1
        ip_list[i] = ip_list[-i_r]
        ip_list[-i_r] = swap
    return ip_list

def countEven(ip_list):
    count = 0
    for i in ip_list:
        if i // 2 == 0:
            count = count + 1
    return count

def isEverywhere(ip_list,element):
    count = 0
    for i in ip_list:
        if ip_list[i] == element or ip_list[i - 1] == element:
            count = count + 1
    if count == len(ip_list):
        return True
    else:
        return False

print(isEverywhere([0,2,1,3,1],1))