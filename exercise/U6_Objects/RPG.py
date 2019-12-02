class RPG:
    name = ""
    equip = ""
    skin_color = 50
    level = 0
    blood = 100
    money = 0

    def __init__(self, name, equip, skin_color, level, blood, money):
        self.name = name
        self.equip = equip
        self.skin_color = skin_color
        self.level = level
        self.blood = blood
        self.money = money

op = RPG("a","b",1,2,3,4)

print(op.name)
print(math.pi)