'''
num = int(input("num please"))


def pyramid(num):
    for i in range(num+1):
        string = ""
        for i in range(i):
            string = string + "*"
        print(string)

print(pyramid(num))
'''
# ------------------
'''

def sumNumbers(ip_list):
    sum = 0
    for i in ip_list:
        num_flag = str.isdigit(str(i))
        if num_flag == True:
            sum = sum + i
    else:
        return sum


print(sumNumbers("a234"))
# --------------------------
'''

def maxBlock(ip):
    count = 0
    count_final = 0
    for i in range(len(ip) - 1):
        if i < len(ip):
            if ip[i] == ip[i + 1]:
                count = count + 1
            else:
                if count > count_final:
                    count_final = count
                    count = 0
                else:
                    count = 0
    else:
        return count_final

print(maxBlock("abccc"))
