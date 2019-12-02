class Superhero:
    name = "sb."
    superpower = "none"
    feature = "weight"
    hight = 0
    weight = 0

    def __init__(self, n, s, f, h, w):
        self.name = n
        self.superpower = s
        self.feature = f
        self.hight = h
        self.weight = w


aslan = Superhero("Leo", "make other smart", "fat", 1.01, 2000.01)

print(aslan.name + "is his name")


class Vehicle:
    brand = ""
    model = ""
    maxCapacitor = 0
    currentPassengers = 0
    speed = 0
    direction = ""

    def __init__(self, brand, model, maxCapacitor, currentPassengers, speed, direction):
        self.brand = brand
        self.model = model
        self.maxCapacitor = maxCapacitor
        self.currentPassengers = currentPassengers
        self.speed = speed
        self.direction = direction


car_a = Vehicle("Tesla", "Model X", 7, 5, 220, "S")

print(car_a.brand, car_a.model, car_a.maxCapacitor,
      car_a.currentPassengers, car_a.speed, car_a.direction)
