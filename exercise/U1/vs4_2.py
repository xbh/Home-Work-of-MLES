c_total = int(input("How many cookies you have?\n"))
p_total = int(input("How many people you have?\n"))

c_person = c_total // p_total
c_left = c_total % p_total

print("Everyone could get",c_person,"piece of cookies,\nand there are",c_left,"piece of cookies left over.")
