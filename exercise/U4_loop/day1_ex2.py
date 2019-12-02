import random

rad_num = random.randint(1,10)
ip_num = int(input("Give an integer"))

while ip_num != rad_num:
    ip_num = int(input("Try again"))
else:
    print("That's right!")