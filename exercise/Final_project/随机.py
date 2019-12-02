import random

print("按一次回车生成一个随机数")

while True:
    input()
    random_num = random.randint(1, 30)
    print("随机数为"+str(random_num))
