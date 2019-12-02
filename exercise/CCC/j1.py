'''
a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

sum_a = a3*3 + a2*2 + a1
sum_b = b3*3 + b2*2 + b1

if sum_a > sum_b:
    print("A")
elif sum_b > sum_a:
    print("B")
else:
    print("T")
'''
def RemoveAdjacentRepeatCharacters(a):
    if(a==''):
        return a
    b=''
    for i in a:
        if (b == ''):
            b += i
        if(i==b[len(b)-1]):
            pass
        else:
            b=b+i
    return b

print(RemoveAdjacentRepeatCharacters(input()))