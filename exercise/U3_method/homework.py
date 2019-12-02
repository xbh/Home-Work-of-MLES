def printOut(input_a):
    print(input_a)
    op = printOut(input_a)
    return op

print(printOut("a"))