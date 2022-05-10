class Car:
    def __init__(self, fuel, maxspeed):
        self.fuel = fuel
        self.maxspeed = maxspeed

    def refuel(self, amount):
        self.fuel += amount

    def drive(self):
        if self.fuel > 0:
            print("Driving")
            self.fuel-= 1
        else:
            print("NO fuel")

polo = Car(20, 185)
mini = Car(10, 170)
bettle = Car (0,150)

print("Polo has" + str(polo.fuel) + "of fuel")
polo.drive()

print("Polo has" + str(polo.fuel) + "of fuel")

print("___")
print("Bettle has" + str(polo.fuel) + "of fuel")
bettle.drive()
print("___")
print("Mini has" + str(polo.fuel) + "of fuel")
mini.drive()
print("Bettle has" + str(polo.fuel) + "of fuel")
