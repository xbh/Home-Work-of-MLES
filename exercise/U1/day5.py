name = input("What is your name? Type here:")

leng = len(name)

a_line = "{:*^30}".format("")
start_b = "{:*<1}".format("")
b_line = "{:^28}".format(name)
c_line = "{:*^30}".format("")
end_b = "{:*>1}".format("")

print(a_line,end = "")
print("*"*int(leng - 28))
print(start_b,end = "")
print(b_line,end = "")
print(end_b)
print("*"*int(leng - 28),end = "")
print(c_line)
