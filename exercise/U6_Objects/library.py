class Book:
    def __init__(self, name, author, serialNumber, barcode, description):
        self.name = name
        self.author = author
        self.serialNumber = serialNumber
        self.barcode = barcode
        self.description = description


class CheckedOutItem:
    def __init__(self, expireTime):
        self.expireTime = expireTime

    def renew(self, expireTime):
        self.expireTime = 7


class Student:
    def __init__(sefl, parameter_list):
        pass


#a = Book("q","a",1,2,"aaa")
a = CheckedOutItem(8)
print(a.renew())
