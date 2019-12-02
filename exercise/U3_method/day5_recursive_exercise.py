def countDown(input_num):
    if input_num == 0:
        return 0
    else:
        print(input_num)
        return countDown(input_num - 1)

# ----------------------


def countUp(num, n=1):
    if n != num:
        print(n)
        return countUp(num, n+1)
    else:
        return num


print(countUp(5))


import math


def m3(a, b):
    return (int(math.pow(b, a)))


def m2(inta):
    b = int(a * 3 / 1.8)
    return b-1


def m1(inta):
    a = a - 1 / 4 * 3
    return a


def m4(inta, intb):
    c = b
    b = a
    a = c


def m5(inta, intb):
    c = b
    b = a
    a = c
    print(a+""+b)


def f(x):
    if 1 == x or 3 == x:
        return x
    else:
        return x * f(x - 1)


def string_splosion(str):
    op = ""
    for num in range(len(str)+1):
        sn = str[:num]
        op = op + sn
    else:
        return op



def string_bits1(str):
    def countDown(input_num=0):
        if input_num == 0:
            return 0
        else:
            return countDown(input_num - 1)

def dosth(n):
    if n > 0:
        dosth(n-1)
        dosth(n-1)
        print(n)
'''
def string_bits(string):
  if len(string) == 1:
    return string
  else:
    return string_bits(string)

print(string_bits("abcde"))
