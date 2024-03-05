class Animal():
    # local scope
    # name ="Dog"

    # constructor
    def __init__(self, name, color="White", habitat="Domestic"):
        self.name = name
        self.habitat = habitat
        self.color = color

        # print("Class has been created")

    def __str__(self) :
        return "Animal is called " + self.name + " and is color "+ self.color + " stays in the " + self.habitat

    def walk(self):
        print(str(self.name)+ " Walks")
    
    def eats(self):
        print(str(self.name)+ "eats")

# Vehicle
# Car, MotorBike

class Vehicle():
    color ="Green"
    def __init__(self, axels, color="White", fuel="Petrol"):
        self.axels = axels
        self.color = color
        self.fuel = fuel
    
    def move(self):
        print("vehicle is moving from a to b")

# inheritance
class Car(Vehicle):
    def __init__(self, axels, color="White", fuel="Petrol", break_pad_type="Disk"):

        super().__init__(axels, color, fuel)

        self.break_pad_type = break_pad_type
    def reverse(self):
        print("vehicle is reversing")

class Plane(Vehicle):
    def __init__(self,axels, color="White", fuel="Petrol", max_elevation=200, no_propellers=1):
        super().__init__(axels, color, fuel)
        self.max_elevation = max_elevation
        self.no_propellers = no_propellers
    
    def take_off(self):
        print("plane is taking off")

car1 = Car(2, color="red", fuel="Petrol")
print(car1.axels, car1.color, car1.fuel)
car1.move()
car1.reverse()
print(car1.color)
plane1 = Plane(2, color="red", fuel="Jet Fuel")
print(plane1.axels, plane1.color, plane1.fuel)

plane1.move()
plane1.take_off()




