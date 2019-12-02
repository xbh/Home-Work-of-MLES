'''
CCC Test 2018
Problem J1
'''
firstDigit = int(input())
secondDigit = int(input())
thirdDigit = int(input())
lastDigit = int(input())

if firstDigit == 8 or firstDigit == 9:
    if lastDigit == 8 or lastDigit == 9:
        if secondDigit == thirdDigit:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")