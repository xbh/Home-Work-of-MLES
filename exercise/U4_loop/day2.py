ip = int(input())
position = ip + 65
op = 65

if ip <= 122:
    while op < position:
        print(chr(op),"", end="")
        op = op + 1
    else:
        print("")
else:
    print("F word")

for i in range(1,11):
    print(i)

text = "WHAT THE FXXX" 

for i in range(len(text)):
    print(text[i])