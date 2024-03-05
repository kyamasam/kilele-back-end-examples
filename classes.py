# class Person():
#     def __init__(self, name='Peter', location='Westlands'):
#         self.name = name
#         self.location = location

#     def walk(self):
#         print(self.name + "  is walking" + " from "+ self.location)


# # instance of a class
# first_person = Person("Jason", "Woodley")
# # instance of the class
# second_person = Person("Agnes", "Nairobi")

# first_person.walk()
# second_person.walk()

# Object oriented programming
# classes 

# global scope
name ="Crow"

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

    

# creating an instance of the class
farm_cow = Animal("Cow", color="grey", habitat="House")
farm_cow.color ="red"
farm_cow.habitat = "Wild"
house_dog = Animal("Dog")
# print(repr(house_dog))
print(farm_cow)

# print(type(farm_cow))
# print(type('team'))
# print(farm_cow.color)
# print(house_dog.color)
# farm_cow.walk()
# farm_cow.eats()
# house_dog.walk()
# house_dog.eats()