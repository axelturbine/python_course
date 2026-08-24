class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(self.brand, "is now going", self.speed, "km/h")

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            print(self.brand, "is now going", self.speed, "km/h")
        else:
            print(self.brand, "is already stopped")

my_car = Car("Volvo", "black")
my_car .accelerate()
my_car .accelerate()
my_car .brake()
my_car .brake()
my_car .brake()

your_car = Car("BMW", "red")
your_car.accelerate()