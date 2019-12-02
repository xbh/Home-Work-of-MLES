text = "Hello"

for i in range(0,len(text),2):
    print("{:^5}".format(text[: i + 1]))

# ----------------------------------

text = "abccba"
flag = 0
for i in range(int(len(text) / 2)):
    if text[i] == text[-i - 1]:
        flag = flag + 1
    else:
        pass

if flag == int(len(text) / 2):
    print(True)
else:
    print(False)

