hi = "hi"
ip = str(input("Give me a string"))
count = 0

for i in range(1, len(ip)):
    if ip[i] == "i" and ip[i - 1] == "h":
        count = count + 1
    else:
        pass
else:
    print(count)
# -------------------------------------

ip = str(input("Give me a string"))
half_leng = int(len(ip) / 2)
count = 0

for i in range(half_leng):
    if ip[i] == ip[-i - 1]:
        count = count + 1
    else:
        pass
else:
    if count != half_leng:
        print(False)
    else:
        print(True)
# ----------------------------------------

ip_num = int(input("Input a num"))

for i in range(ip_num + 1):
    print("star", end="")
else:
    print()
