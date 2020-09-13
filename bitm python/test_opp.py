class person:
    def __init__(self, name, age=1, gender="Male"):
        self.name = name
        self.age = age
        self.gender = gender

    def showInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

aimee = person("Aimee", 21, "Female")
aimee.showInfo()
print (" --------------- ")
# default age, gender.
alice = person( "Alice" )
alice.showInfo()
print (" --------------- ")
# Default gender.
tran = person("Tran", 37)
tran.showInfo()




