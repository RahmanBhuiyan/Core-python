from animal import Animal

# Cat class extends from Animal.
class Cat (Animal):

    def __init__(self, name, age, height):
        # Call to contructor of parent class (Animal)
        # to assign value to attribute 'name' of parent class.
        super().__init__(name)

        self.age = age
        self.height = height

    def showInfo(self):
        print("I'm " + self.name)
        print(" age " + str(self.age))
        print(" height " + str(self.height))