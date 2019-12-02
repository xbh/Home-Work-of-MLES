def numba(var):
    sum = 0
    i = 0
    while i <= var:
        sum = sum + i
        i = i + 1
    else:
        return sum

print(numba(1))